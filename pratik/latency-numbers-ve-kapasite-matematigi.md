# ⏱️ Latency Numbers & Kapasite Matematiği

> **"Bir mühendis kestirim yapamadığında, sezgisi çalışmaz; sezgisi çalışmadığında, hatalı sistem kurar."** — *Jeff Dean'in seminal "Numbers Everyone Should Know" listesi (Stanford 2009)*

Bu doküman staff+ bir mühendisin **ezbere bilmesi gereken** sayıları ve bunları üretim sistem kararlarında nasıl kullanacağını anlatır.

---

## 📑 İçindekiler

1. [Jeff Dean Sayıları — 2025 Güncel](#1--jeff-dean-sayıları--2025-güncel)
2. [Disk, Network, RAM Karşılaştırması](#2--disk-network-ram-karşılaştırması)
3. [Little's Law — Kapasitenin Anahtar Denklemi](#3--littles-law--kapasitenin-anahtar-denklemi)
4. [Kuyruk Teorisi — Utilization Curve](#4--kuyruk-teorisi--utilization-curve)
5. [p50 vs p99 vs p99.9 — Kuyruk Gecikmesi](#5--p50-vs-p99-vs-p999--kuyruk-gecikmesi)
6. [Coordinated Omission — Ölçüm Hatası](#6--coordinated-omission--ölçüm-hatası)
7. [HdrHistogram — Doğru Ölçüm](#7--hdrhistogram--doğru-ölçüm)
8. [Pratik Kapasite Hesabı (Vakalar)](#8--pratik-kapasite-hesabı-vakalar)
9. [Sayısal Sezgi Egzersizleri](#9--sayısal-sezgi-egzersizleri)

---

## 1. 🧮 Jeff Dean Sayıları — 2025 Güncel

| İşlem | Süre | İnsan ölçeğine taşırsak (1 ns = 1 sn) |
|---|---|---|
| L1 cache referansı | **0.5 ns** | 0.5 sn |
| Branch misprediction | 5 ns | 5 sn |
| L2 cache referansı | **7 ns** | 7 sn |
| Mutex lock/unlock (uncontended) | 25 ns | 25 sn |
| Main memory (RAM) erişimi | **100 ns** | 1.5 dakika |
| Compress 1 KB (Snappy) | 2 µs | 33 dakika |
| Send 1 KB üzerinden 1 Gbps ağ | 10 µs | 2.7 saat |
| SSD random read 4 KB | **16 µs** | 4.5 saat |
| Read 1 MB sequentially RAM | 3 µs | 50 dakika |
| Read 1 MB sequentially SSD | **49 µs** | 13.5 saat |
| Round-trip same datacenter | **0.5 ms** | 5.8 gün |
| Read 1 MB sequentially 1 Gbps ağ | 1 ms | 11.6 gün |
| Read 1 MB sequentially HDD | **5 ms** | 58 gün |
| Disk seek (HDD) | 4 ms | 46 gün |
| TCP packet retransmit | 1-3 ms | 2-3 hafta |
| Round-trip CA→Hollanda (~9000km) | **150 ms** | 4.7 yıl |
| Round-trip aynı continent (intra-region cross-AZ) | **1-2 ms** | 11-23 gün |
| Round-trip cross-region (US→EU) | **70-90 ms** | 2.2-2.8 yıl |
| Round-trip mobile cellular (4G) | 50-100 ms | 1.5-3 yıl |
| Cold container start (Lambda Node.js) | **100-300 ms** | 3-9 yıl |
| Cold container start (Lambda Java) | **2-5 s** | 60-150 yıl |
| TLS handshake (yeni) | 50-150 ms | 1.5-4.7 yıl |
| TLS handshake (resumption) | ~RTT | … |
| DNS query (cache miss) | 30-80 ms | 1-2.5 yıl |
| Postgres simple SELECT (warm cache, indexed) | **0.1-0.5 ms** | 1.2-5.8 gün |
| Postgres SELECT (cold cache, disk seek) | **5-20 ms** | 58-231 gün |
| Redis GET (LAN) | **0.5-1 ms** | 5.8-11 gün |
| ElasticSearch query (basit) | 5-50 ms | 58-579 gün |

> **Mental Model:** "1 ns ≈ 1 saniye" ölçeğinde düşünmek, 4-5 büyüklük mertebesi farkı sezgisel hale getirir.

### Önemli Oranlar (ezberlenecek)

```
RAM ≈ 200× SSD random
SSD ≈ 100× HDD seek
Aynı DC RTT ≈ 5000× RAM access
Cross-region RTT ≈ 100× aynı DC RTT
TLS handshake yeni ≈ 100× TLS resumption
```

---

## 2. 💾 Disk, Network, RAM Karşılaştırması

### Throughput (sequential)

| Medya | Throughput | Tipik kullanım |
|---|---|---|
| L1 cache | ~1 TB/s | CPU iç |
| L3 cache | ~400 GB/s | CPU iç |
| DDR4 RAM | ~25-50 GB/s | Main memory |
| NVMe SSD (PCIe 4.0) | **5-7 GB/s** | Production DB local disk |
| SATA SSD | ~500 MB/s | Düşük tier disk |
| HDD (7200 rpm) | ~150 MB/s | Cold storage / archive |
| 100 Gbps NIC | ~12 GB/s | Hyperscaler datacenter |
| 25 Gbps NIC | ~3 GB/s | Tipik bulut VM |
| 10 Gbps NIC | ~1.2 GB/s | Yaygın baseline |
| 1 Gbps NIC | ~120 MB/s | Eski hardware |

### IOPS (random 4 KB)

| Medya | IOPS |
|---|---|
| Optane DC PMM | ~2 M |
| NVMe SSD enterprise | 500 K — 1 M |
| Cloud SSD (gp3 / pd-ssd) | 3 K — 16 K (provisionable) |
| HDD 7200 rpm | **~80** |
| HDD 15000 rpm enterprise | ~200 |

> **Pratik:** Bir HDD'den dakikada ~5000 random read alabilirsin. PostgreSQL warm cache'siz HDD üzerinde çalışıyorsa, **IOPS senin tavanın**.

---

## 3. 📐 Little's Law — Kapasitenin Anahtar Denklemi

$$L = \lambda \cdot W$$

- **L** = sistemdeki ortalama eşzamanlı iş sayısı (concurrency)
- **λ** = saniyedeki gelen iş sayısı (throughput / arrival rate)
- **W** = bir işin sistemdeki ortalama süresi (latency)

> **Formülün gücü:** Üç değişkenden ikisini biliyorsan üçüncüsü matematiksel olarak vardır. Tahmini değil, **ispatlı**.

### Vaka 1: Kaç worker / connection / thread gerekir?

> Servis **1000 RPS** alıyor, ortalama istek **50 ms** sürüyor. Ne kadar eşzamanlılık taşımalı?

$$L = 1000 \cdot 0.050 = 50 \text{ eşzamanlı istek}$$

→ Connection pool / thread pool / worker sayısı ≥ 50 olmalı. Düşükse kuyruk birikir, p99 patlar.

### Vaka 2: DB connection pool tuning

> Postgres'e RPS = 500, ortalama query süresi = 20 ms. Pool size?

$$L = 500 \cdot 0.020 = 10 \text{ connection}$$

→ Pool 10'dan az → kuyruk; çok fazla → DB CPU overhead. **Kural:** Little's Law sonucunun **1.5×** ile başla, p99 sapmasına göre artır/azalt.

### Vaka 3: Lambda concurrency

> Lambda 100 RPS alıyor, ortalama 200 ms sürüyor. Provisioned concurrency?

$$L = 100 \cdot 0.200 = 20$$

→ AWS Lambda concurrency limit'ini **20'nin üstünde** tutmalısın (genelde +%50 buffer = 30).

> ⚠️ **Tuzak:** Little's Law **kararlı durumda** geçerlidir. Trafik patlamasında (spike) `L` anlık olarak çok daha yüksek olabilir.

---

## 4. 📈 Kuyruk Teorisi — Utilization Curve

M/M/1 kuyruğunda bekleme süresi:

$$W_q = \frac{\rho}{1-\rho} \cdot \frac{1}{\mu}$$

- **ρ** = utilization (0-1 arası)
- **μ** = service rate

### Sayısal sezgi

| Utilization (ρ) | Bekleme süresi katsayısı | Pratik anlamı |
|---|---|---|
| 0.5 | 1.0× | Rahatlık |
| 0.7 | 2.3× | Sağlıklı çalışma |
| **0.8** | **4.0×** | **Pratik tavan** |
| 0.9 | 9.0× | Tehlikeli — küçük sapmalar büyük gecikme |
| 0.95 | 19.0× | Crash beklenen |
| 0.99 | 99.0× | Sistem patlamış |

> **Kural:** Web servislerini **ρ ≤ 0.7** civarında tut. 0.8'i aştığında tail latency lineer değil, **eksponansiyel** kötüleşir.

### Görsel sezgi

```
Latency
  ▲
  │                                      .  ← ρ=0.95
  │                               .
  │                         .
  │                   .  ← ρ=0.85
  │            .
  │       .
  │   .          ← ρ=0.5 (lineer bölge)
  │_._.________________________________________→ Utilization
  0%            70%      85%   95%       100%
```

> **Pratik karar:** Cloud autoscale eşiğini CPU %70'te tetikle, %85'te değil. %85'te tetiklersen, scale-out olana kadar (3-5 dk) p99 zaten patlamıştır.

---

## 5. 📊 p50 vs p99 vs p99.9 — Kuyruk Gecikmesi

### Yanlış: Ortalama (mean / avg)

> Asla ortalama latency'le karar verme. **"Bir kişi 5 m boyunda, dokuz kişi 1.7 m" → ortalama 2 m.** Yanıltıcı.

### Doğru: Yüzdelikler (percentiles)

| Yüzdelik | Anlamı | Hangi durumda kritik? |
|---|---|---|
| p50 (medyan) | %50 isteğin altında | "Tipik kullanıcı" deneyimi |
| p95 | %95 isteğin altında | Genel duyarlılık |
| **p99** | %99 isteğin altında | SLO sözleşmesi |
| **p99.9** | %99.9 isteğin altında | Yüksek QPS sistemler |
| p99.99 | %99.99 isteğin altında | Trillion-scale (Google, Meta) |

### Tail at scale problemi (Dean & Barroso 2013)

> Bir sayfa yüklemesi **10 mikro-servise** seri çağrı yapıyorsa ve her birinin p99'u 100 ms ise:

**Olasılık matematiği:**
$$P(\text{en az biri yavaş}) = 1 - 0.99^{10} = 0.096 \approx 9.6\%$$

→ **p99 sayfa latency'si**, en yavaş servisin **p99'undan büyük** olur.
→ %10 kullanıcı 100ms+ gecikme yaşar.

**Çözümler:**
- **Hedged requests:** İlk N ms'te yanıt yoksa ikinci kopyaya gönder.
- **Tied requests:** İki kopyaya aynı anda yolla, ilk dönen kazansın.
- **Backup requests:** İstatistiksel olarak yavaş çıkacaksa fallback.
- **Micro-partitioning:** Partition boyutunu küçült, hot-spot riskini düşür.

### p99 ≠ "%1 yavaş kullanıcı"

> Bir kullanıcı **20 istek** yapan tek sayfa açıyorsa:
> $P(\text{hepsi p99 altında}) = 0.99^{20} = 0.82$
> → **%18 kullanıcı** p99-üstü deneyim yaşar.

---

## 6. ⚠️ Coordinated Omission — Ölçüm Hatası

> **Gil Tene'nin 2013 keşfi:** Çoğu yük testi aracı (eski JMeter, ab) latency'yi **yanlış ölçer** çünkü kuyruktaki bekleme süresini görmez.

### Problem

```
Sistem 100 RPS göndermeye çalışıyor → her istek arası 10 ms hedef.
Sistem 1 saniye boyunca kilit (lock) tarafından bekledi.
Bu süre içinde 100 istek "üretmeli"ydi ama üretilemedi.
Test aracı: "Hata yok, latency normal" ←❌

Gerçek: 100 kullanıcı 1 saniye bekledi.
```

### Coordinated omission'lı veri ne gösterir?

```
Yanlış histogram (omission ile):
p50 = 5 ms
p99 = 50 ms          ← Görünüşte "iyi"
max = 100 ms

Düzeltilmiş histogram:
p50 = 5 ms
p99 = 850 ms         ← 17× gerçek!
max = 1100 ms
```

### Çözüm: Sabit gönderim (constant throughput)

- Yük üreticisi **planlanan zamanı**na göre istek gönderir.
- Geç kalmış istekleri **biriktirir** ve gecikme olarak rapor eder.
- `wrk2`, `tlp-stress`, `Gatling`, modern `k6` doğru ölçer; **eski `ab`, `wrk` v1, basit `curl --time` döngüleri yanlış ölçer.**

### Ölçüm araçları için kontrol listesi

- [ ] Constant throughput modu var mı?
- [ ] HdrHistogram tabanlı raporlama yapıyor mu?
- [ ] p99.9 hesaplanabiliyor mu?
- [ ] Latency'yi **kuyruğa girişten** itibaren mi sayıyor?

---

## 7. 📏 HdrHistogram — Doğru Ölçüm

### Neden basit array yetmez?

100 milyon istek için:
- Naive array: 100M × 8 byte = 800 MB **bellek**.
- Linear bucket: precision = bucket genişliği — küçük yapsan bucket sayısı patlar.

### HdrHistogram'ın çözümü

- **Sabit doğruluk** (örn. 3 anlamlı ondalık) tüm dynamic range'de.
- **Logaritmik bucket'lar** + her bucket içinde lineer alt-bölme.
- Bellek: ~64 KB ile **trilyon farklı değer**i 3 hane hassasiyetle tutar.
- p50 ve p99.99 aynı doğrulukta hesaplanır.

### Kullanım

```java
Histogram h = new Histogram(3); // 3 significant digits
long start = System.nanoTime();
doWork();
h.recordValue(System.nanoTime() - start);
// ...
System.out.printf("p99.9 = %d µs%n", h.getValueAtPercentile(99.9) / 1000);
```

```javascript
// Node.js
const Hdr = require('hdr-histogram-js');
const h = Hdr.build();
h.recordValue(latencyNs);
console.log(h.getValueAtPercentile(99.9));
```

### Birleştirme (merge)

> Birden fazla pod'dan toplanan histogram'lar **doğru toplanır** (yüzdelik ortalaması alınamaz).

```
❌ Yanlış: pod1.p99 + pod2.p99 / 2
✅ Doğru: histogram1.add(histogram2).getValueAtPercentile(99)
```

→ **Prometheus histogram metric'lerinin doğru kullanımı** budur. `histogram_quantile(0.99, sum by (le) (rate(...)))` agregasyon-after-quantile değil, agregasyon-before-quantile yapar.

---

## 8. 🎯 Pratik Kapasite Hesabı (Vakalar)

### Vaka 1: E-ticaret peak günü

> Kara Cuma. Tarihsel olarak normal günün **15×**'i trafik. Normal: 200 RPS. Peak: 3000 RPS.
> Tipik istek 80 ms (DB query + serialize). DB connection limit'i 100.

**Hesap:**
$$L_{peak} = 3000 \cdot 0.080 = 240 \text{ eşzamanlı}$$

→ DB pool 100 → **bottleneck**. Çözümler:
1. **Pool'u artır** (DB CPU dayanırsa). Postgres'te 100 üstü genelde overhead getirir → PgBouncer.
2. **Read replica + read/write split** → yazma 30, okuma 210.
3. **Cache layer** (Redis) → DB hit oranını %30'a indir → 240 × 0.3 = 72 < 100 ✅

### Vaka 2: Microservice fan-out

> API gateway → 8 servise paralel çağrı yapıyor. Her servis p99 = 50 ms.

```
P(en az 1 yavaş) = 1 - 0.99^8 = 7.7%
→ Sayfa p99 ≈ servis p99 × 1.4 ≈ 70 ms (yaklaşık)
```

→ %8 kullanıcı 50ms+ ek görür. Çözüm: **hedged request** (en yavaş 2'sini paralel ikinci kopyaya yolla).

### Vaka 3: Kafka consumer lag

> 10 K msg/s üretiliyor. Consumer her mesajı 5 ms işliyor. Kaç partition + consumer gerekir?

$$\text{Tek consumer kapasitesi} = \frac{1}{0.005} = 200 \text{ msg/s}$$

$$\text{Min consumer} = \frac{10000}{200} = 50$$

→ **Topic en az 50 partition**. Buffer için **75 partition + 50 consumer** (autoscale için).

### Vaka 4: Kullanıcı session storage

> 10 milyon DAU, ortalama session boyutu 2 KB, 30 dakika TTL. Redis cluster boyutu?

$$\text{Aktif session} \approx \frac{10^7 \cdot 0.5}{24} = 208\text{K eşzamanlı}$$

(varsayım: kullanıcılar günde 30 dk aktif → her an 1/48'i online)

$$\text{RAM} = 208000 \cdot 2 \text{ KB} = 416 \text{ MB}$$

→ Tek küçük Redis instance yeter. Ama **HA için** primary + replica + cross-AZ → 3 × 1 GB instance.

### Vaka 5: S3 egress maliyeti

> 1 TB/gün dış kullanıcıya video servis ediliyor. AWS US-East-1 → internet egress: $0.09/GB.

$$\text{Aylık} = 1000 \text{ GB} \cdot 30 \cdot 0.09 = \$2700$$

→ CDN (CloudFront) önüne koy → cache hit %90 → ~$270 + CDN $0.085/GB ilk 10TB → çok daha az. **Tek değişiklik = $2400/ay tasarruf.**

---

## 9. 🧠 Sayısal Sezgi Egzersizleri

> Staff+ mühendis bu soruları **30 saniyede** cevaplayabilmeli.

### Soru 1
> Postgres tablosunda 100M satır var, indeksli kolon üzerinden tek satır SELECT. RAM'de mi disk'te mi karar veremiyorum, en kötü durumda ne kadar sürer?

<details>
<summary>Cevap</summary>

B-tree depth ≈ log₁₀₀(100M) ≈ 4 seviye. Her seviye disk seek = 5 ms. Toplam: **~20 ms**. RAM'de cache'liyse 0.1 ms.

</details>

### Soru 2
> 1 GB veriyi başka kıtaya 1 Gbps link üzerinden göndermek ne kadar sürer?

<details>
<summary>Cevap</summary>

1 GB / (1 Gbps / 8) = **8 saniye**. Ama RTT 150 ms ve TCP slow start var → gerçekte **30-60 saniye**. Multipart upload + paralel akış kullan.

</details>

### Soru 3
> 100 K eşzamanlı WebSocket bağlantısı. Tek pod'da kaç connection tutabilirim?

<details>
<summary>Cevap</summary>

Linux default file descriptor 1024 → artırmadan zaten ölü. `ulimit -n 65535` ile 60K limit. Ephemeral port (~28K) ve memory (~10 KB/conn → 1 GB) hesaba kat. **Pratik tavan tek pod'da ~50K**. Üzeri için **horizontal sharding** + sticky LB.

</details>

### Soru 4
> Redis'e 10K item insert atıyorum, hep 1 ms dönüyor. Tek connection mu, paralel mi?

<details>
<summary>Cevap</summary>

Tek connection ardışık: 10K × 1 ms = **10 saniye**. Pipelining: 1 batch × 1 RTT ≈ **5-20 ms**. Pipelining olmadan Redis'in marjinal hızının %1'ini kullanırsın.

</details>

### Soru 5
> JWT verify CPU'da ne kadar sürer? Saniyede kaç verify yapabilirim?

<details>
<summary>Cevap</summary>

RS256 (RSA-2048): ~0.3 ms/verify → ~3000 verify/sec/core. HS256: ~5 µs → ~200K/sec/core. **API gateway'de RSA varsa CPU bottleneck olur**, HMAC'e geç.

</details>

---

## ⚠️ Kapasite Planlama Anti-Pattern'leri

| Anti-Pattern | Neden Tehlikeli | Doğru Yaklaşım |
|---|---|---|
| **Ortalama (mean) ile planlama** | p99 spike'larını gizler; kuyruk gecikmeleri görünmez olur | p50 + p99 + p99.9 ile planla; **p99 ≈ 10× p50** kuralını unut-ma |
| **Peak'i hesaplamama** | Steady-state'te yeterli kaynak → Black Friday'de çöküş | Peak/baseline oranını ölç (genellikle 3-10×); headroom bırak |
| **Headroom bırakmama** | %80+ utilization → kuyruk teorisi gereği latency eksponansiyel artar | %60-70 CPU ceiling target; auto-scale trigger %70'te |
| **Tek boyutlu kapasite bakışı** | Sadece CPU izlenir; memory/disk/network/connection pool darboğazı kaçırılır | USE method: her kaynak için Utilization, Saturation, Errors |
| **Coordinated omission** | Load test aracı yavaş yanıtlarda bekler → gerçek p99'u ölçemez | Closed-loop yerine open-loop test (wrk2, Gatling constant-rate) |
| **"Daha fazla instance ekleriz"** | Stateful bileşen (DB, cache) scale etmez; Amdahl yasası | Vertical limit + sharding planı; DB connection pool = darboğaz |

---
## 🎯 Staff+ Kapasite Kontrol Listesi

### Yeni servis launch öncesi

- [ ] Peak traffic tahmini yapıldı mı? (Baseline × peak factor; genellikle 3-10×)
- [ ] Little's Law ile minimum instance sayısı hesaplandı mı?
- [ ] p99 latency SLO tanımlandı mı? (p50 değil, p99 hedef)
- [ ] Darboğaz noktası belirlendi mi? (CPU, memory, DB connection, network)
- [ ] Auto-scale trigger'ları ve ceiling'ler tanımlı mı? (Scale-up %70, scale-down %30)

### Kapasite review (çeyreklik)

- [ ] Utilization trendleri incelendi mi? (6 aylık projeksiyon)
- [ ] DB connection pool utilization %70 altında mı?
- [ ] Disk growth rate ile provisioned storage uyumlu mu?
- [ ] Load test son 3 ayda yapıldı mı? (Open-loop, coordinated omission'sız)
- [ ] Cost-per-request trendi izleniyor mu? (Efficiency metriği)

### Incident sonrası

- [ ] Capacity-related root cause varsa headroom artırıldı mı?
- [ ] Cascading failure senaryosu simüle edildi mi?
- [ ] Back-of-envelope hesap postmortem'e eklendi mi?

---
## 📚 İleri Okuma

- Jeff Dean — *Numbers Everyone Should Know* (Stanford 2009 sunumu)
- Gil Tene — *How NOT to Measure Latency* (Strange Loop 2015 sunumu)
- Dean, Barroso 2013 — *The Tail at Scale*
- Brendan Gregg — *Systems Performance* 2nd ed., bölüm 2 (Methodologies)
- Neil Gunther — **Guerrilla Capacity Planning**
- Aleksey Shipilёv — *Nanotrusting the Nanotime* (JMH talk)
- HdrHistogram — github.com/HdrHistogram/HdrHistogram

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
