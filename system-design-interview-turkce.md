# 🏗️ System Design Interview Vol 1 — Türkçe Kapsamlı Rehber

> **"Doğru cevap yoktur. İyi trade-off'lar vardır."**
> — System Design'ın altın kuralı

Bu kitap, büyük ölçekli sistemlerin nasıl tasarlanacağını öğretir.
Her bölüm bir **gerçek dünya problemi** alır ve adım adım çözüm tasarlar.
Mülakat formatında yazılmış olsa da, içindeki bilgiler
**günlük mühendislik kararlarında** hayati önem taşır. 🎯

---

## 📖 İçindekiler

1. [Ölçekleme Temelleri](#1--ölçekleme-temelleri)
2. [Back-of-the-Envelope Hesapları](#2--back-of-the-envelope-hesapları)
3. [System Design Framework](#3--system-design-framework)
4. [Rate Limiter Tasarımı](#4--rate-limiter-tasarımı)
5. [Consistent Hashing](#5--consistent-hashing)
6. [Key-Value Store Tasarımı](#6--key-value-store-tasarımı)
7. [Unique ID Generator](#7--unique-id-generator)
8. [URL Shortener Tasarımı](#8--url-shortener-tasarımı)
9. [Web Crawler Tasarımı](#9--web-crawler-tasarımı)
10. [Notification System Tasarımı](#10--notification-system-tasarımı)
11. [News Feed Tasarımı](#11--news-feed-tasarımı)
12. [Chat System Tasarımı](#12--chat-system-tasarımı)
13. [Search Autocomplete Tasarımı](#13--search-autocomplete-tasarımı)
14. [YouTube Tasarımı](#14--youtube-tasarımı)
15. [Google Drive Tasarımı](#15--google-drive-tasarımı)
16. [Büyük Şirketlerde System Design Gerçekleri](#16--büyük-şirketlerde-system-design-gerçekleri)
17. [Yapay Zeka Çağında System Design](#17--yapay-zeka-çağında-system-design)
18. [Sonuç ve Bağlantılar](#18--sonuç-ve-bağlantılar)

---

## 1. 📐 Ölçekleme Temelleri

### Tek Sunucu → Milyon Kullanıcı

```
Bir web uygulaması sıfırdan milyonlara nasıl ölçeklenir?
Adım adım gidelim:

ADIM 1: TEK SUNUCU 🖥️
  ┌──────────────────────────┐
  │  [Web + App + DB]        │
  │  Hepsi TEK makinede      │
  │  IP: 123.45.67.89        │
  └──────────────────────────┘
  → 100 kullanıcıya kadar OK 👍
  → Sonra disk, CPU, RAM sınırları gelir

ADIM 2: VERİTABANI AYIRMA 🗄️
  ┌─────────────┐    ┌─────────────┐
  │ Web/App     │───→│ Database    │
  │ Server      │    │ Server      │
  └─────────────┘    └─────────────┘
  → Her biri bağımsız ölçeklenebilir
  → SQL mi NoSQL mi?

  SQL (İlişkisel):
    → Tablo yapısı, JOIN, ACID, schema
    → MySQL, PostgreSQL
    → Ne zaman? → İlişkisel veri, karmaşık sorgular, tutarlılık kritik

  NoSQL (İlişkisel olmayan):
    → Key-value, document, graph, column
    → MongoDB, Cassandra, DynamoDB, Redis
    → Ne zaman? → Süper düşük gecikme, devasa veri, esnek schema,
                   serileştirme/deserileştirme yeterli (JOIN gereksiz)

ADIM 3: LOAD BALANCER ⚖️
  ┌─────────────┐
  │   Client    │
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │   Load      │
  │   Balancer  │  ← Public IP burada
  └──┬─────┬────┘
     │     │
  ┌──▼──┐ ┌▼───┐
  │ S1  │ │ S2 │  ← Private IP, dışarıdan ERİŞİLEMEZ
  └─────┘ └────┘
  → S1 çökerse → LB trafiği S2'ye yönlendirir → NO DOWNTIME!
  → Trafik artarsa → S3, S4... ekle (horizontal scaling)

ADIM 4: DATABASE REPLİKASYONU 📋
  ┌────────┐     ┌────────┐
  │ Master │────→│ Slave1 │  ← READ
  │ (WRITE)│────→│ Slave2 │  ← READ
  └────────┘     │ Slave3 │  ← READ
                 └────────┘
  → WRITE: Master'a
  → READ: Slave'lerden (genelde READ >> WRITE, %80-90!)
  → Master çökerse → bir Slave PROMOTE edilir
  → Slave çökerse → diğer Slave'ler devam eder → yüksek kullanılabilirlik!

ADIM 5: CACHE 🚀
  Client → LB → Server → CACHE → Database
                          ↑
                     HIT? geri dön!
                     MISS? DB'den al, cache'e yaz

  Cache neden önemli?
  → DB sorgusu: ~10ms
  → Cache okuma (Redis): ~0.1ms (100x DAHA HIZLI!)
  → Okuma ağırlıklı sistemlerde OYUN DEĞİŞTİRİCİ!

  Cache Stratejileri:
  ┌────────────────────────────────────────────────────────────┐
  │ READ-THROUGH: Cache miss → DB'den oku → cache'e yaz       │
  │ WRITE-THROUGH: Her yazma → cache + DB aynı anda           │
  │ WRITE-BEHIND: Yazma → cache'e → sonra ASYNC DB'ye         │
  │ CACHE-ASIDE: App kendi yönetir (en yaygın)                │
  └────────────────────────────────────────────────────────────┘

  ⚠️ DİKKAT:
  → Cache hangi zaman expire olacak? (TTL)
  → Tutarsızlık riski: DB güncellendi ama cache eski!
  → Tek sunucu cache → SPOF! (Redis Cluster kullan)
  → Cache eviction: LRU (Least Recently Used) en yaygın

ADIM 6: CDN (Content Delivery Network) 🌐
  → Statik içerik (resim, CSS, JS) → CDN'den servis et
  → Kullanıcıya EN YAKIN sunucudan → düşük latency
  → Origin server yükünü AZALTIR
  → CloudFront, Cloudflare, Akamai

ADIM 7: STATELESS WEB SERVER 📦
  → Session bilgisini sunucuda TUTMA!
  → Neden? → LB farklı sunucuya yönlendirirse session KAYBOLUR!
  → Çözüm: Session'ı dışarıda tut (Redis, DB)
  → Artık HER sunucu HER isteği işleyebilir → kolay ölçekleme!

ADIM 8: MULTIPLE DATA CENTERS 🌍
  ┌─────────┐     ┌─────────┐
  │ DC-EU   │     │ DC-US   │
  │ (Avrupa)│     │ (ABD)   │
  └─────────┘     └─────────┘
  → GeoDNS: Kullanıcıyı EN YAKIN DC'ye yönlendir
  → Bir DC çökerse → diğerine yönlendir (disaster recovery)
  → Data senkronizasyonu: EN ZOR KISIM!

ADIM 9: MESSAGE QUEUE 📬
  Producer → [Queue] → Consumer
  → Asenkron işleme: "Hemen yapmam gerekmiyor"ları kuyruğa at
  → Producer ve Consumer BAĞIMSIZ ölçeklenir
  → Kafka, RabbitMQ, SQS

ADIM 10: MONITORING & LOGGING 📊
  → Metrikler: CPU, bellek, istek/sn, hata oranı
  → Loglar: Merkezi log sistemi (ELK Stack, Datadog)
  → Alerting: Eşik aşılınca ALARM
  → "Ölçemediğin şeyi iyileştiremezsin!"
```

### Vertical vs Horizontal Scaling

```
VERTICAL SCALING (Scale Up) ⬆️
  → Daha güçlü makine al (daha çok CPU, RAM, disk)
  → Basit! Kod DEĞİŞMİYOR
  → AMA: Fiziksel LIMIT var (ne kadar büyük makine olabilir?)
  → SPOF: Tek makine çökerse → HER ŞEY ÇÖKER!
  → Küçük/orta projeler için OK

HORIZONTAL SCALING (Scale Out) ↔️
  → Daha fazla makine EKLE
  → Teorik olarak SINIRSIZ
  → Kod DEĞİŞMELİ (stateless olmalı!)
  → Daha karmaşık AMA daha dayanıklı
  → Büyük projeler için ŞART

  💡 Pratik Kural:
  "Vertical ile başla, horizontal'a ihtiyacın olduğunda GEÇ."
  → Premature optimization is the root of all evil!
  → AMA horizontal'a geçişi kolaylaştıracak şekilde TASARLA
    (stateless, cache, queue → bu temeller olsun)
```

---

## 2. 🧮 Back-of-the-Envelope Hesapları

### Neden Kabataslak Hesap?

```
System design'da kesin rakamlar değil, BÜYÜKLÜK SIRASI veriyoruz.
"Tam olarak 847,293 istek/saniye" değil → "yaklaşık 1 milyon istek/saniye"
Amaç: Doğru mimari KARARLARI alabilmek!

"10 GB RAM gerekiyor" → tek makineye sığar, cache yeterli!
"10 TB RAM gerekiyor" → dağıtılmış çözüm LAZIM!
→ BÜYÜKLÜK SIRASI fark yaratır, kesin rakam değil!
```

### Temel Sayılar (Ezberlenmeli!)

```
┌─────────────────────────────────────────────────┐
│ İŞLEM                          │ SÜRE           │
├─────────────────────────────────┼────────────────┤
│ L1 cache referans               │ 0.5 ns         │
│ L2 cache referans               │ 7 ns           │
│ RAM referans                    │ 100 ns         │
│ Mutex lock/unlock               │ 25 ns          │
│ 1 KB sıkıştır (Zippy)          │ 10,000 ns (10μs)│
│ 1 KB ağ üzerinden gönder       │ 10,000 ns      │
│ SSD'den 4KB oku                 │ 150,000 ns     │
│ SSD'den 1MB sequential oku     │ 1,000,000 ns (1ms)│
│ HDD'den 1MB sequential oku     │ 20,000,000 ns (20ms)│
│ Aynı DC'de paket gönder        │ 500,000 ns     │
│ Disk seek (HDD)                │ 10,000,000 ns  │
│ California → Hollanda round trip│ 150,000,000 ns │
│                                │ (150ms)        │
└─────────────────────────────────┴────────────────┘

ÇIKARIMLAR:
  → Bellek okuması disk okumasından ~1000x hızlı → CACHE KULLAN!
  → SSD, HDD'den ~20x hızlı → SSD tercih et!
  → Ağ round trip PAHALI → minimize et!
  → Sıkıştırma UCUZ → veriyi sıkıştır, ağdan daha az gönder!
  → Sequential okuma random okumadan ÇOK DAHA HIZLI → tasarımda bunu düşün!
```

### Güç Hesapları (Powers of 2)

```
2^10  = 1,024          ≈ 1 Bin (Kilo)         → 1 KB
2^20  = 1,048,576      ≈ 1 Milyon (Mega)      → 1 MB
2^30  = 1,073,741,824  ≈ 1 Milyar (Giga)      → 1 GB
2^40  =                ≈ 1 Trilyon (Tera)      → 1 TB
2^50  =                ≈ 1 Katrilyon (Peta)    → 1 PB

FAYDALI KISAYOLLAR:
  1 gün = 86,400 saniye ≈ ~10^5 saniye (100K)
  1 gün ≈ 100K saniye (hesaplarda bu yeter!)

  QPS (Query Per Second) hesabı:
  → DAU (Daily Active Users) = 10 milyon
  → Her kullanıcı günde 5 istek yapıyor
  → Günlük toplam = 50 milyon istek
  → QPS = 50M / 100K = ~500 QPS
  → Tepe noktası (peak) = QPS × 2~3 = ~1000-1500 QPS

DEPO HESABI:
  → 10M kullanıcı, her biri 1 tweet/gün, tweet = 280 char + metadata ≈ 1KB
  → Günlük: 10M × 1KB = 10GB
  → Yıllık: 10GB × 365 = 3.65TB
  → 5 yıl: ~18TB
  → "18TB depolama lazım" → çok mu az mı? → Gayet yönetilebilir!
```

### Örnek: Twitter QPS Hesabı

```
Varsayımlar:
  → MAU (Monthly Active Users): 300M
  → DAU ≈ %50 → 150M
  → Her kullanıcı günde 2 tweet atıyor
  → %10 tweet medya içeriyor (resim/video)

Tweet yazma QPS:
  → 150M × 2 / 100K = 3,000 QPS
  → Peak: ~6,000 QPS

Tweet okuma QPS (her kullanıcı 100 tweet okuyor):
  → 150M × 100 / 100K = 150,000 QPS!
  → Okuma >> Yazma (50:1 oranı!)
  → CACHE çok kritik!

Depolama (5 yıl):
  → Tweet metin: 150M × 2 × 1KB × 365 × 5 = ~550 TB
  → Medya: 150M × 2 × 0.1 × 1MB × 365 × 5 = ~55 PB!
  → Medya depolama DEVASA → CDN + Object Storage (S3) ŞART!
```

---

## 3. 🎯 System Design Framework

### 4 Adımlık Yaklaşım

```
Her system design probleminde bu 4 adımı izle:

╔═══════════════════════════════════════════════════════╗
║ ADIM 1: GEREKSİNİMLERİ ANLA (3-5 dk)                ║
║   → Fonksiyonel: Sistem NE yapmalı?                  ║
║   → Non-fonksiyonel: Ölçek, performans, tutarlılık?  ║
║   → ASLA varsayma → SOR!                             ║
║                                                       ║
║ ADIM 2: ÜST DÜZEY TASARIM (10-15 dk)                ║
║   → Ana bileşenler (API, DB, Cache, Queue)           ║
║   → Veri akışı diyagramı                              ║
║   → API endpoint'leri                                 ║
║                                                       ║
║ ADIM 3: DERİN DALMA (10-15 dk)                       ║
║   → Kritik bileşenleri detaylandır                   ║
║   → Data model & schema                              ║
║   → Darboğazları çöz                                 ║
║   → Trade-off'ları tartış                             ║
║                                                       ║
║ ADIM 4: ÖZET & TARTIŞMA (3-5 dk)                     ║
║   → Bottleneck'ler nerede?                           ║
║   → Daha da ölçeklenseydi ne yapardık?               ║
║   → Hata senaryoları (failure modes)                 ║
╚═══════════════════════════════════════════════════════╝
```

### Gereksinimler Soruları (Her Tasarımda Sor!)

```
FONKSIYONEL:
  → "Hangi feature'lar KAPSAM İÇİNDE?"
  → "Kullanıcılar neler YAPABİLMELİ?"
  → "Hangi platform? (web, mobil, API)"

NON-FONKSIYONEL:
  → "Kaç kullanıcı? DAU?" (ölçek)
  → "Okuma mı yazma mı ağırlıklı?" (cache stratejisi)
  → "Gecikme hedefi?" (p99 < 200ms?)
  → "Tutarlılık mı kullanılabilirlik mi?" (CAP trade-off)
  → "Veri ne kadar süre saklanmalı?" (depolama)

KISITLAR:
  → "Mevcut altyapı var mı?"
  → "Bütçe kısıtı var mı?"
  → "Düzenleyici gereksinimler?" (GDPR, KVKK)
```

---

## 4. 🚦 Rate Limiter Tasarımı

### Problem

```
AMAÇ: API'ye gelen istekleri SINIRLA
  → DDoS koruması
  → Maliyet kontrolü (her API çağrısı = para!)
  → Kötüye kullanımı engelle
  → Kaynakları adil paylaştır

ÖRNEKLER:
  → Twitter: 300 tweet/3 saat
  → Google Docs: 300 okuma/dakika/kullanıcı
  → Stripe API: 100 istek/saniye
```

### Nereye Koyacağız?

```
3 seçenek:

1. CLIENT-SIDE ❌
   → Kolay bypass edilir (curl ile direkt istek at!)
   → Güvenilmez

2. SERVER-SIDE ✅
   → API handler'dan ÖNCE kontrol
   → Güvenli AMA her servise ayrı implement etmek lazım

3. MIDDLEWARE (API Gateway) ✅✅
   → Tüm istekler gateway'den geçer → TEK NOKTADA rate limit
   → AWS API Gateway, Kong, Nginx
   → Microservices'te en yaygın

  Client → [API Gateway / Rate Limiter] → Server
             ↓ limit aşıldı?
           429 Too Many Requests!
```

### Rate Limiting Algoritmaları

```
1. TOKEN BUCKET 🪣 (En yaygın! Amazon, Stripe kullanıyor)
   ─────────────────────────────────────────────
   Kova var, içinde token'lar var.
   → Her istek 1 token harcar
   → Token yoksa → REJECT (429)
   → Token'lar sabit hızda YENILENIR

   Parametre:
     → Bucket size: max kaç token? (burst kapasitesi)
     → Refill rate: saniyede kaç token eklenir?

   Örnek: size=10, refill=2/sn
     → Başlangıçta 10 token → 10 burst istek yapabilir
     → Sonra saniyede 2 istek yapabilir
     → Token bittiyse → bekle veya 429!

   AVANTAJ: Basit, bellek verimli, burst'e izin verir
   DEZAVANTAJ: İki parametreyi tune etmek gerekiyor

2. LEAKING BUCKET 🚿
   ─────────────────────────────────────────────
   FIFO kuyruk (sabit boyut)
   → İstek gelir → kuyruğa girer
   → Kuyruktan SABİT HIZDA işlenir
   → Kuyruk doluysa → REJECT

   AVANTAJ: İstekleri düzgün hızda işler (smoothing)
   DEZAVANTAJ: Burst traffic'te eski istekler kuyruğu doldurur,
               yeni istekler reddedilir

3. FIXED WINDOW COUNTER 🪟
   ─────────────────────────────────────────────
   Sabit zaman pencereleri (örn: her dakika)
   → Zaman penceresi başına sayaç tut
   → Sayaç limit'i aştı → REJECT

   Sorun: PENCERE SINIRI problemi!
   ┌──────────┐┌──────────┐
   │ 00:00    ││ 01:00    │
   │ limit:5  ││ limit:5  │
   │     ■■■■■││■■■■■     │
   └──────────┘└──────────┘
   → Son 30sn'de 5, ilk 30sn'de 5 = 1 dk'da 10 İSTEK!
   → Limit 5 ama 10 geçti! 😱

4. SLIDING WINDOW LOG 📜
   ─────────────────────────────────────────────
   Her isteğin TIMESTAMP'ini logla
   → Yeni istek gelince: son 1 dk'daki istekleri say
   → Limit aşıldı → REJECT
   → Eski timestamp'leri temizle

   AVANTAJ: Pencere sınırı problemi YOK, çok doğru
   DEZAVANTAJ: Bellek yoğun (her timestamp saklanıyor!)

5. SLIDING WINDOW COUNTER 🏅 (En iyi trade-off!)
   ─────────────────────────────────────────────
   Fixed window + sliding window karışımı
   → Önceki pencere sayacı: 7
   → Mevcut pencere sayacı: 3
   → Mevcut penceredeki konum: %30 geçmiş

   Tahmini sayı = önceki × (1 - 0.3) + mevcut = 7 × 0.7 + 3 = 7.9
   → Limit 10 ise → OK!
   → Limit 7 ise → REJECT!

   AVANTAJ: Bellek verimli, oldukça doğru
   DEZAVANTAJ: Tahmini (ama pratikte %0.003 hata, ihmal edilebilir!)
```

### Dağıtık Rate Limiting

```
Tek sunucu rate limit → basit (in-memory counter)
Birden fazla sunucu → SORUN!

  Server1: sayaç = 3
  Server2: sayaç = 2
  → Toplam 5 ama her sunucu 3 ve 2 biliyor!
  → Limit 4 ise → her ikisi de geçiriyor (3<4, 2<4) → TOPLAM 5 > 4! 💀

ÇÖZÜM: Merkezi store kullan → REDIS!

  Server1 ─┐
           ├──→ Redis (sayaç burada!) → atomik INCR
  Server2 ─┘

  Redis INCR komutu: atomik, yarış koşulu YOK
  → Tüm sunucular aynı sayacı görüyor ✅
```

```javascript
// Rate Limiter - Token Bucket (basitleştirilmiş)
class TokenBucket {
  constructor(maxTokens, refillRate) {
    this.maxTokens = maxTokens;
    this.tokens = maxTokens;
    this.refillRate = refillRate; // token/saniye
    this.lastRefill = Date.now();
  }

  tryConsume() {
    this._refill();
    
    if (this.tokens >= 1) {
      this.tokens -= 1;
      return true; // İstek KABUL ✅
    }
    
    return false; // İstek REDDEDİLDİ ❌ → 429!
  }

  _refill() {
    const now = Date.now();
    const elapsed = (now - this.lastRefill) / 1000;
    const tokensToAdd = elapsed * this.refillRate;
    this.tokens = Math.min(this.maxTokens, this.tokens + tokensToAdd);
    this.lastRefill = now;
  }
}

// Kullanım:
const limiter = new TokenBucket(10, 2); // Max 10, 2 token/sn

function handleRequest(req, res) {
  if (!limiter.tryConsume()) {
    res.status(429).json({ error: 'Too Many Requests' });
    res.setHeader('Retry-After', '5');
    res.setHeader('X-RateLimit-Remaining', '0');
    return;
  }
  // Normal işlem...
}
```

---

## 5. 🔄 Consistent Hashing

### Problem: Sunucular Arası Veri Dağıtımı

```
10 milyon key'in 4 sunucuya dağıtılması:

NAIVE YAKLAŞIM: serverIndex = hash(key) % N

  hash("user:1") % 4 = 1 → Server1
  hash("user:2") % 4 = 3 → Server3
  hash("user:3") % 4 = 0 → Server0
  ...

BU TAMADIR! Ta ki... sunucu EKLERSEN veya ÇIKARIRSAN! 😱

  Sunucu eklendi: N=4 → N=5

  hash("user:1") % 5 = ?  ← FARKLI sunucu!
  hash("user:2") % 5 = ?  ← FARKLI sunucu!
  → Neredeyse TÜM key'ler yeniden dağıtılmalı!
  → 10M key varsa → 10M cache MISS → DB'ye YIĞILMA → çökme! 💀

  Bu "REHASH FIRTINASI" olarak bilinir.
```

### Consistent Hashing Çözümü

```
FİKİR: Hash'leri bir DAİRE (ring) üzerinde düşün!

  Daire: 0 ——→ 2^32 (ve tekrar 0'a döner)

  Sunucuları daire üzerine yerleştir:
       S0 (pos: 100)
      /            \
    /                \
  S3 (pos: 800)    S1 (pos: 300)
    \                /
      \            /
       S2 (pos: 600)

  Key'i daire üzerine hash'le → SAAT YÖNÜNDE ilk sunucuya ata!

  hash("user:1") = 150 → saat yönünde → S1 (pos: 300) ✅
  hash("user:2") = 500 → saat yönünde → S2 (pos: 600) ✅
  hash("user:3") = 750 → saat yönünde → S3 (pos: 800) ✅

SUNUCU EKLENDİĞİNDE:
  S4 (pos: 450) eklendi
  → Sadece 300-450 arasındaki key'ler ETKİLENİR!
  → S1'den S4'e taşınır
  → Diğer TÜM key'ler YERİNDE KALIR! ✅
  → 10M key'den sadece ~2M etkilenir (~%20 = K/(N+1))

SUNUCU ÇIKARTIĞINDA:
  S2 silindi
  → S2'nin key'leri saat yönünde sonraki sunucuya (S3) gider
  → Diğerleri ETKİLENMEZ! ✅
```

### Virtual Nodes (Sanal Düğümler)

```
SORUN: Sunucular daire üzerinde DENGESİZ dağılabilir!
  → S0: %10 key
  → S1: %60 key  ← AŞIRI YÜK!
  → S2: %5 key
  → S3: %25 key

ÇÖZÜM: Her sunucu için BİRDEN FAZLA nokta (virtual node)!

  S0 →  S0_1, S0_2, S0_3, S0_4, S0_5 (5 sanal düğüm)
  S1 →  S1_1, S1_2, S1_3, S1_4, S1_5
  S2 →  S2_1, S2_2, S2_3, S2_4, S2_5
  S3 →  S3_1, S3_2, S3_3, S3_4, S3_5

  → 4 fiziksel sunucu × 5 sanal = 20 nokta daire üzerinde
  → Daire üzerinde DAHA DÜZGÜN dağılım
  → Her sunucu yaklaşık %25 key → DENGELİ! ✅

  Pratikte sanal düğüm sayısı: 100-200 → çok dengeli dağılım!
  Trade-off: Daha fazla virtual node = daha dengeli AMA daha fazla bellek

KULLANAN SİSTEMLER:
  → Amazon DynamoDB
  → Apache Cassandra
  → Discord
  → Akamai CDN
```

---

## 6. 🗃️ Key-Value Store Tasarımı

### Hedef

```
Distributed, scalable, highly available key-value store tasarla!
(Amazon DynamoDB, Redis, Memcached gibi)

Operasyonlar:
  put(key, value)
  get(key) → value

Gereksinimler:
  → Düşük gecikme (< 10ms)
  → Yüksek kullanılabilirlik (99.99%)
  → Key-value boyutu < 10KB
  → Otomatik ölçekleme
```

### CAP Teoremi (ÖNEMLİ!)

```
DAĞITIK bir sistemde aynı anda EN FAZLA 2 garanti sağlanabilir:

  C — Consistency (Tutarlılık):  Her okuma en son yazılan veriyi döner
  A — Availability (Kullanılabilirlik): Her istek yanıt alır
  P — Partition Tolerance (Bölünme Dayanıklılığı): Ağ bölünmesinde çalışmaya devam

  AMA: P kaçınılamaz! (ağlar ER GEÇ bölünür!)
  → Gerçek seçim: CP veya AP

  CP (Consistency + Partition tolerance):
    → Ağ bölünmesinde → KESİNLİKLE tutarlı ama bazı istekler BAŞARISIZ
    → Banka transferi: "Yanlış bakiye GÖSTERMEKTEZse, hiç gösterme!"
    → HBase, MongoDB (default)

  AP (Availability + Partition tolerance):
    → Ağ bölünmesinde → HER İSTEĞE yanıt ver ama ESKİ veri görebilir
    → Sosyal medya feed: "Eski tweet göster, hiç göstermemekten İYİ!"
    → Cassandra, DynamoDB, CouchDB

  💡 "Banka mısın yoksa Instagram mısın?"
     → Banka: CP → yanlış bakiye KABULEDİLEMEZ
     → Instagram: AP → 2 sn gecikmeli like sayısı KABUL edilebilir
```

### Veri Bölümleme (Partitioning)

```
10TB veri → tek sunucuya SIĞMAZ → BÖLÜMLE!

  Consistent hashing ile:
  → Key → hash → ring → sunucu
  → Otomatik dağıtım
  → Sunucu ekle/çıkar → minimal yeniden dağıtım

REPLIKASYON:
  Her veri N replika'da saklanır (N=3 tipik)

  Ring üzerinde:
  Key → S1 (primary) → S2 (replica) → S3 (replica)
  → S1 çökerse → S2 veya S3'ten oku → yüksek kullanılabilirlik!

TUTARLILIK MODELLERI:
  → N = replika sayısı (örn: 3)
  → W = yazma quorum'u (kaç replika'ya yazılmalı?)
  → R = okuma quorum'u (kaç replika'dan okunmalı?)

  W + R > N → GÜÇLÜ tutarlılık (strong consistency)
  → En az 1 replika hem yazma hem okumada ORTAK!

  Örnekler:
  N=3, W=1, R=3 → Hızlı yazma, yavaş okuma, tutarlı
  N=3, W=3, R=1 → Yavaş yazma, hızlı okuma, tutarlı
  N=3, W=2, R=2 → Dengeli, tutarlı (en yaygın!)
  N=3, W=1, R=1 → Hızlı ama tutarlılık garantisi YOK (eventual)
```

### Çakışma Çözümleme (Conflict Resolution)

```
2 replika aynı anda farklı değer yazdı → ÇAKIŞMA!

VEKTÖR SAATLER (Vector Clocks):
  Her sunucu kendi sayacını tutar:

  D1: S1 yazdı → [(S1, 1)]
  D2: S1 güncelledi → [(S1, 2)]
  D3: S2 okudu ve güncelledi → [(S1, 2), (S2, 1)]
  D4: S3 okudu ve güncelledi → [(S1, 2), (S3, 1)]

  D3 ve D4 → ÇAKIŞMA! (ne S2>S3 ne S3>S2, paralel!)
  → Client'a İKİ VERSİYON da gönder → client ÇÖZSÜN
  → Veya "last write wins" (basit ama veri KAYBI riski!)

SIL-ÖLÜM (Tombstone): 🪦
  → Key silindi → gerçekten SİLME, TOMBSTONE koy!
  → Neden? → Replikalar arası senkronizasyonda "silinmiş" bilgisi LAZıM
  → Tombstone ile "bu key silindi" bilgisi yayılır
  → Belirli süre sonra (garbage collection) temizlenir
```

### Hata Tespiti & Kurtarma

```
GOSSIP PROTOCOLU: 🗣️ (Dedikodu!)
  → Her sunucu heartbeat listesi tutar
  → Periyodik olarak RASTGELE bir sunucuyla gossip yapar
  → "S3'ten haber alamıyorum" → diğerlerine sor
  → Birkaç sunucu da S3'ten haber alamıyor → S3 ÇÖKTÜ! 🔴

  Neden gossip?
  → Merkezi heartbeat sunucusu → SPOF!
  → Gossip → merkezsiz, dayanıklı, ölçeklenebilir

HINT HANDOFF (Geçici Devretme):
  → S3 çöktü → S3'ün sorumlu olduğu yazmaları geçici olarak S4 ÜSTLENIR
  → S3 geri gelince → S4 birikmiş verileri S3'e GERİ VERİR (handoff)
  → Kullanıcı hiçbir KESINTI hissetmez! ✅

MERKLE TREE (Anti-entropy):
  → Replikalar arası veri TUTARLILIĞINI kontrol et
  → Tüm veriyi karşılaştırmak pahalı → Merkle tree ile SADECE farklı dalları bul
  → Farklılıkları SENKRONIZE et
  → Tamamen tutarlı hale getir ✅
```

---

## 7. 🆔 Unique ID Generator

### Problem

```
Dağıtık sistemde TÜM verilere benzersiz ID lazım.
→ Tek DB'de auto_increment → ama dağıtık sistemde?

GEREKSİNİMLER:
  → Benzersiz (unique)
  → Sayısal (sortable → sıralanabilir)
  → 64 bit
  → Saniyede 10,000+ ID üretilebilmeli
  → Zamana göre sıralı (yaklaşık olarak)
```

### Yaklaşımlar

```
1. MULTI-MASTER REPLICATION
   → Auto increment AMA artış = N (sunucu sayısı)
   → S1: 1, 3, 5, 7...  S2: 2, 4, 6, 8...
   ❌ Zaman sıralı değil, sunucu ekleme/çıkarma ZOR

2. UUID (V4: rastgele)
   → 128 bit, her yerde üretilebilir, çakışma olasılığı ihmal edilebilir
   ✅ Basit, koordinasyon gereksiz
   ❌ 128 bit (64 bit istedik!), sıralı değil, indeks performansı DÜŞÜK

3. TICKET SERVER (Flickr yöntemi)
   → Merkezi DB'de auto_increment
   ✅ Basit, sayısal ID
   ❌ SPOF! Tek DB çökerse → ID üretim DURUR

4. TWITTER SNOWFLAKE ❄️ (En iyi yaklaşım!)
   → 64 bit ID'yi parçalara böl:

   ┌─────┬──────────────────────┬────────┬───────────┐
   │Sign │   Timestamp (41 bit) │DC (5b) │Machine(5b)│Seq(12b)│
   │ 0   │ millisecond epoch    │ 0-31   │ 0-31      │ 0-4095 │
   └─────┴──────────────────────┴────────┴───────────┘

   → Sign: Her zaman 0 (pozitif)
   → Timestamp: Custom epoch'tan ms cinsinden fark (41 bit ≈ 69 yıl!)
   → Datacenter ID: 5 bit = 32 datacenter
   → Machine ID: 5 bit = 32 makine/datacenter = toplam 1024 makine
   → Sequence: 12 bit = aynı ms'de 4096 ID/makine

   KAPASİTE:
   → 1024 makine × 4096 ID/ms = 4,194,304 ID/ms = 4 MİLYAR ID/sn!
   → Fazlasıyla yeterli!

   AVANTAJLAR:
   → 64 bit ✅
   → Zamana göre sıralı ✅ (timestamp en anlamlı bitlerde)
   → Dağıtık, koordinasyon gereksiz ✅
   → Çok yüksek throughput ✅
```

```javascript
// Snowflake ID Generator (basitleştirilmiş)
class SnowflakeGenerator {
  constructor(datacenterId, machineId) {
    this.epoch = 1609459200000n; // 2021-01-01 özel epoch
    this.datacenterId = BigInt(datacenterId);
    this.machineId = BigInt(machineId);
    this.sequence = 0n;
    this.lastTimestamp = -1n;
  }

  nextId() {
    let timestamp = BigInt(Date.now());

    if (timestamp === this.lastTimestamp) {
      this.sequence = (this.sequence + 1n) & 4095n; // 12 bit mask
      if (this.sequence === 0n) {
        // Aynı ms'de 4096 ID üretildi → sonraki ms'yi bekle!
        while (timestamp <= this.lastTimestamp) {
          timestamp = BigInt(Date.now());
        }
      }
    } else {
      this.sequence = 0n;
    }

    this.lastTimestamp = timestamp;

    return (
      ((timestamp - this.epoch) << 22n) |   // 41 bit timestamp
      (this.datacenterId << 17n) |           // 5 bit DC
      (this.machineId << 12n) |              // 5 bit machine
      this.sequence                          // 12 bit sequence
    );
  }
}

const generator = new SnowflakeGenerator(1, 1);
console.log(generator.nextId()); // 6920312345678901234n gibi bir sayı
// → Sıralı, benzersiz, 64-bit, dağıtık! ✅
```

---

## 8. 🔗 URL Shortener Tasarımı

### Problem

```
TinyURL / bit.ly gibi bir servis tasarla:
  → Uzun URL → kısa URL oluştur
  → Kısa URL'ye tıkla → uzun URL'ye yönlendir
  → Ölçek: 100M URL/gün oluşturma
```

### Gereksinimler

```
FONKSİYONEL:
  → POST /api/shorten { longUrl } → { shortUrl }
  → GET /{shortUrl} → 301 Redirect → longUrl

NON-FONKSİYONEL:
  → 100M URL/gün = ~1160 URL/sn (yazma)
  → Okuma yazma oranı 10:1 → ~11,600 okuma/sn
  → URL 7 karakter (a-z, A-Z, 0-9 = 62 karakter)
  → 62^7 = 3.5 trilyon kombinasyon → 100 yıl+ yeter!
  → URL'ler 10 yıl saklanır → 365 milyar URL
```

### Hash + Base62 Yaklaşımı

```
YAKLAŞIM 1: HASH
  → longUrl'yi hash'le (MD5, SHA256)
  → İlk 7 karakteri al
  → ÇAKIŞma riski! → çakışırsa → önceden tanımlı string ekle, tekrar hash'le

YAKLAŞIM 2: BASE62 + Auto-increment ID ✅ (Daha iyi!)
  → ID = 11157 (auto-increment veya Snowflake)
  → 11157'yi Base62'ye çevir:
    11157 / 62 = 179 kalan 59 → 59 = "X"
    179 / 62 = 2 kalan 55 → 55 = "T"
    2 / 62 = 0 kalan 2 → 2 = "2"
    → shortUrl = "2TX"

  ID → Base62 → shortUrl → ÇAKIŞMA İMKANSIZ! (ID benzersiz!)
```

### Mimari

```
┌────────┐     ┌─────────────┐     ┌──────────┐
│ Client │────→│ API Server  │────→│ DB       │
└────────┘     │ (stateless) │     │ (MySQL)  │
               └──────┬──────┘     └──────────┘
                      │
                ┌─────▼─────┐
                │  Cache     │
                │  (Redis)   │
                └────────────┘

YAZMA AKIŞI:
  1. longUrl geldi → DB'de var mı? (de-dup)
  2. Yoksa → ID üret (Snowflake) → Base62'ye çevir → DB'ye kaydet
  3. shortUrl döndür

OKUMA AKIŞI:
  1. /{shortUrl} geldi
  2. Redis cache → HIT? → redirect (çoğu istek BURADA biter!)
  3. MISS? → DB'den al → cache'e yaz → redirect

301 vs 302:
  → 301 Moved Permanently: Tarayıcı CACHE'LER, bir daha sunucuya sormaz
    → Sunucu yükü AZ ama analitik KAYBEDERSIN!
  → 302 Found: Her seferinde sunucuya sorar
    → Analitik toplayabilirsin (tıklama sayısı!) ama sunucu yükü FAZLA
  → ÇOĞU URL shortener 302 kullanır (analitik önemli!)
```

---

## 9. 🕷️ Web Crawler Tasarımı

### Problem

```
Google gibi web'i tarayan (crawl eden) bir sistem tasarla.
  → Seed URL'lerden başla → linkleri takip et → sayfaları indir → indexle
  → Milyarlarca sayfa
  → Politik, yasal kısıtlar (robots.txt)
```

### Tasarım

```
┌─────────────┐     ┌────────────┐     ┌───────────┐
│ Seed URLs   │────→│ URL        │────→│ URL       │
│             │     │ Frontier   │     │ Fetcher   │
└─────────────┘     │ (Queue)    │     │ (Download)│
                    └────────────┘     └─────┬─────┘
                         ↑                    │
                         │              ┌─────▼─────┐
                    ┌────┴────┐         │ Content   │
                    │ URL     │         │ Parser    │
                    │ Extractor│←────────│           │
                    └─────────┘         └─────┬─────┘
                                              │
                                        ┌─────▼─────┐
                                        │ Content   │
                                        │ Storage   │
                                        └───────────┘

BFS (Breadth-First) crawling:
  → URL frontier = FIFO kuyruk
  → Seed URL'leri kuyruğa koy
  → Kuyruktan al → indir → linkleri çıkar → kuyruğa ekle → TEKRARLA!
```

### Kritik Sorunlar

```
1. DENGELİ CRAWLING (Politeness) 🤝
   → Aynı domain'e saniyede 100 istek atma! → sunucuyu ÇÖKERTISIN!
   → Çözüm: Domain başına AYRI kuyruk + delay

   queue_getir.com → [url1, url2, url3] → Worker1 (arada 1sn bekle!)
   queue_google.com → [url4, url5] → Worker2

2. URL DE-DUP ♻️
   → Aynı sayfayı TEKRAR indirme!
   → Ziyaret edilen URL'leri SET'te tut
   → Milyarlarca URL → Bloom Filter kullan! (bellek verimli, olasılıksal)

3. TUZAKLAR 🕳️
   → Sonsuz döngü: a.com/1 → a.com/2 → a.com/1 → ...
   → Çözüm: Maksimum derinlik limiti (max depth)
   → Spider trap: Dinamik sayfa sonsuz URL üretiyor
   → Çözüm: URL pattern tespiti + blacklist

4. ROBOTS.TXT 🤖
   → Her sitenin "neyi crawl edebilirsiniz" kuralı
   → SAYGILI ol! robots.txt'i oku ve UY
   → User-agent: *
   → Disallow: /private/
   → Crawl-delay: 5

5. İÇERİK DUPLICATE 📋
   → Farklı URL, aynı içerik (http vs https, www vs non-www)
   → Çözüm: İçerik hash'i → simhash ile benzerlik tespiti

6. ÖNCELİKLENDİRME 🏅
   → Tüm URL'ler EŞİT DEĞİL! google.com > rastgeleblog.com
   → PageRank, güncelllik sıklığı, domain otoritesi
   → Yüksek öncelikli URL'ler ÖNCE crawl edilir
```

---

## 10. 🔔 Notification System Tasarımı

### Problem

```
Push notification, SMS, email gönderen bir sistem tasarla.
  → iOS/Android push, SMS, email
  → 10M+ mobil push/gün, 1M SMS/gün, 5M email/gün
  → Soft real-time (birkaç saniye gecikme OK)
  → Kullanıcı tercihlerine saygı (opt-out)
```

### Bildirim Türleri

```
iOS PUSH:
  App Server → APNs (Apple Push Notification Service) → iPhone

Android PUSH:
  App Server → FCM (Firebase Cloud Messaging) → Android

SMS:
  App Server → Twilio/Nexmo → Telefon

EMAIL:
  App Server → SendGrid/SES → Email Client

→ Her kanal FARKLI 3. parti servise bağımlı → AYRI işle!
```

### Mimari

```
┌──────────┐     ┌────────────────┐     ┌─────────────┐
│ Service  │────→│ Notification   │────→│ Message     │
│ (caller) │     │ Service        │     │ Queues      │
└──────────┘     └────────────────┘     └──┬──┬──┬────┘
                                           │  │  │
                                    ┌──────┘  │  └──────┐
                                    ↓         ↓         ↓
                              ┌─────────┐┌────────┐┌────────┐
                              │iOS Queue││SMS Q.  ││Email Q.│
                              └────┬────┘└───┬────┘└───┬────┘
                                   ↓         ↓         ↓
                              ┌─────────┐┌────────┐┌────────┐
                              │iOS      ││SMS     ││Email   │
                              │Worker   ││Worker  ││Worker  │
                              └────┬────┘└───┬────┘└───┬────┘
                                   ↓         ↓         ↓
                              ┌─────────┐┌────────┐┌────────┐
                              │ APNs    ││Twilio  ││SES     │
                              └─────────┘└────────┘└────────┘

NEDEN MESSAGE QUEUE?
  → Decouple: Bildirim servisi 3. parti servise BAĞIMLI olmamalı
  → Buffer: Twilio yavaşsa → kuyrukta BİRİK → kuyruğu kendi hızında tüket
  → Retry: Başarısız → kuyruğa GERİ KOY → tekrar dene!
  → Farklı kanallar BAĞIMSIZ ölçeklenir
```

### Kritik Özellikler

```
1. GÜVENILIRLIK (Reliability) 🛡️
   → Bildirim KAYBOLMAMALI!
   → Log tablosuna yaz → gönderildi mi? → status tracking
   → Retry mekanizması: üstel geri çekilme (exponential backoff)
   → Dead Letter Queue: 3 denemede başarısız → DLQ'ya at → sonra incele

2. TEK BİLDİRİM GARANTİSİ (Exactly-once? At-least-once!) 📩
   → Exactly-once ZORDUR → at-least-once + de-dup
   → Her bildirime event_id ver
   → Göndermeden önce: "Bu event_id daha önce gönderildi mi?"
   → Evet → ATLA! Hayır → GÖNDER + kaydet

3. OPT-OUT / TERCİHLER 🙅
   → Kullanıcı: "SMS istemiyorum!"
   → notification_preferences tablosu:
     user_id | channel | opt_in
     123     | sms     | false
     123     | email   | true
   → Göndermeden ÖNCE kontrol et!

4. RATE LIMITING 🚦
   → Kullanıcıya günde MAX 5 push gönder
   → Fazlası → SPAM → kullanıcı uygulamayı SİLER! 🗑️

5. ANALİTİK 📊
   → Açılma oranı (open rate)
   → Tıklama oranı (click rate)
   → Hangi bildirimler ETKİLİ?
   → A/B test: "Siparişiniz yolda!" vs "🚚 Siparişiniz YOLA ÇIKTI!"
     → Hangisi daha çok tıklama alıyor?

6. TEMPLATE SİSTEMİ 📝
   → Her bildirim için ayrı metin yazma!
   → Template: "Merhaba {name}, siparişiniz {status}!"
   → Parametre değiştir → binlerce varyasyon!
```

---

## 11. 📰 News Feed Tasarımı

### Problem

```
Facebook/Twitter gibi bir haber akışı (news feed) tasarla.
  → Kullanıcı post atar
  → Takipçilerin feed'inde GÖRÜNür
  → Feed kronolojik + relevance sıralamalı
```

### İki Temel API

```
1. POST YAYINLAMA (Feed Publishing):
   POST /api/feed
   Body: { content, media_ids }
   → Post DB'ye kaydedilir
   → Takipçilerin feed'ine DAĞITILIR

2. FEED ÇEKME (Feed Retrieval):
   GET /api/feed?page=1
   → Kullanıcının feed'ini döner (takip ettiklerinin postları)
```

### Fanout: Push vs Pull

```
İKİ YAKLAŞIM:

1. FANOUT ON WRITE (Push modeli) 📤
   ─────────────────────────────────
   Ali post attı → ALI'NIN TÜM takipçilerinin feed cache'ine YAZ!

   Ali post → Feed Service → [Takipçi 1 cache'i ✅]
                            → [Takipçi 2 cache'i ✅]
                            → [Takipçi 3 cache'i ✅]
                            → ... (1000 takipçi = 1000 yazma!)

   AVANTAJ:
   → Feed OKUMA çok hızlı! (önceden hazırlanmış, sadece cache'den oku!)
   → Real-time: post atılır atılmaz feed'de!

   DEZAVANTAJ:
   → Hotkey/Ünlü problemi: Ronaldo 500M takipçi → 500M yazma?! 💀
   → İnaktif kullanıcılara da yazıyorsun → israf!
   → Yazma işlemi YAVAŞ (çok fanout)

2. FANOUT ON READ (Pull modeli) 📥
   ─────────────────────────────────
   Kullanıcı feed'i açar → o AN takip ettiklerinin postlarını çek!

   Kullanıcı feed açtı → "Kimleri takip ediyorum?"
     → Ali, Ayşe, Mehmet
     → Ali'nin postlarını çek + Ayşe'ninkileri + Mehmet'inkileri
     → Birleştir + sırala → feed!

   AVANTAJ:
   → Yazma zamanı HIZLI (sadece kendi kaydını yaz)
   → İnaktif kullanıcılar için gereksiz iş YOK
   → Ünlü problemi YOK

   DEZAVANTAJ:
   → Feed OKUMA yavaş! (her seferinde birleştirme yapılıyor)
   → N takip = N sorgu → yavaş!

3. HİBRİT YAKLAŞIM ✅ (Facebook/Twitter böyle yapıyor!)
   ─────────────────────────────────────────────────
   → NORMAL kullanıcılar (< 5000 takipçi) → fanout on WRITE (push)
   → ÜNLÜLER (> 5000 takipçi) → fanout on READ (pull)

   Feed oluştururken:
   1. Önceden push edilmiş postları cache'den al (normal kullanıcılar)
   2. Ünlülerin postlarını PULL et (az sayıda ünlü, manageable)
   3. Birleştir + sırala → feed!

   → En iyi iki dünyanın birleşimi! ✅
```

### Feed Sıralama (Ranking)

```
Basit: Kronolojik (en yeni üstte)
  → Kolay ama EN İYİ değil!
  → Önemli postları KAÇIRIRSIN

Akıllı: Relevance Score
  → Etkileşim potansiyeli (bu post seni ilgilendirecek mi?)
  → Yakınlık (bu kişiyle ne kadar etkileşiyorsun?)
  → Taze mi eski mi? (recency)
  → İçerik türü (video daha mı çok izleniyor?)

  Score = w1 × recency + w2 × affinity + w3 × engagement_prediction + ...
  → ML modeli ile optimize edilir
  → Facebook EdgeRank'in temel fikri bu!
```

---

## 12. 💬 Chat System Tasarımı

### Problem

```
WhatsApp/Messenger gibi bir chat sistemi tasarla:
  → 1:1 mesajlaşma
  → Grup mesajlaşma (max 100 kişi)
  → Online/offline durumu
  → 50M DAU
```

### Protocol Seçimi

```
HTTP POLLING 🔄
  Client: "Yeni mesaj var mı?" (her 5 sn)
  Server: "Hayır... hayır... hayır... EVET!"
  → İsraf! %95 istek BOŞ dönüyor!

LONG POLLING ⏳
  Client: "Yeni mesaj var mı?" (bağlantıyı AÇIK TUT!)
  Server: ... bekler ... mesaj gelince → cevapla!
  → Daha iyi! AMA:
  → Sender ve receiver farklı sunucuya bağlı olabilir
  → Sunucu çok fazla AÇIK BAĞLANTI tutuyor
  → Timeout yönetimi karmaşık

WEBSOCKET ✅ (En iyi!)
  Client ←→ Server (çift yönlü, kalıcı bağlantı)
  → Server mesajı ANINDA push edebilir!
  → Real-time için IDEAL
  → Tek TCP bağlantısı üzerinden İKİ YÖN

  ⚠️ WebSocket STATEFUL → sunucu affinity gerekli!
  → Kullanıcı X her zaman AYNI chat sunucusuna bağlanmalı
  → Service discovery ile yönetilir
```

### Mimari

```
┌────────┐  WebSocket   ┌─────────────┐     ┌──────────┐
│Client A│◄─────────────►│ Chat Server │────→│ Message  │
└────────┘               │ (Stateful)  │     │ Queue    │
                         └──────┬──────┘     └─────┬────┘
                                │                   │
                         ┌──────▼──────┐     ┌─────▼────┐
                         │ Presence    │     │ Chat Srv │
                         │ Service     │     │ (B'nin)  │
                         └─────────────┘     └─────┬────┘
                                                    │
                                              ┌─────▼────┐
                                              │Client B  │
                                              └──────────┘

1:1 MESAJ AKIŞI:
  1. A mesaj yazar → WebSocket → Chat Server
  2. Message ID üret (Snowflake → zamana göre sıralı!)
  3. Message Queue'ya at
  4. Message DB'ye kaydet (key-value store → Cassandra)
  5. B online mı?
     → Evet: B'nin chat server'ına push → WebSocket → B
     → Hayır: Push notification gönder! 📱

GRUP MESAJI:
  → Üye sayısı < 100 → HER üyeye AYRI kuyruk (fanout on write)
  → Her üye kendi kuyruktan okur
  → Neden ayrı kuyruk? → Her üyenin okuma durumu FARKLI
    (Ali 5. mesaja kadar okumuş, Ayşe 3.'ye kadar)
```

### Message Storage

```
HANGİ VERİTABANI?

Düşünelim:
  → Yazma: çok yoğun (mesaj yağmuru!)
  → Okuma: SADECE son mesajlar okunur (random access az)
  → Sequential access ağırlıklı (bir sohbetteki sıralı mesajlar)
  → Veri hiç silinmez veya nadiren silinir

  CEVAP: Key-Value Store → HBase veya Cassandra ✅
  → Yazma optimized (LSM tree → sequential write)
  → Row key: (chat_id, created_at) → bir sohbetin mesajları YANYANA
  → Range query: "Son 20 mesajı getir" → ÇOK HIZLI!

SCHEMA:
  ┌─────────────────────────────────────────────┐
  │ message_id (Snowflake, PK)                  │
  │ chat_id                                      │
  │ sender_id                                    │
  │ content (text/media)                         │
  │ created_at                                   │
  │ type (text, image, video, file)              │
  └─────────────────────────────────────────────┘

MESSage_id olarak SNOWFLAKE:
  → Auto-increment → NEDEN OLMAZ?
  → Çünkü dağıtık DB'de auto-increment YOK!
  → Snowflake → zamana göre sıralı + benzersiz + dağıtık ✅
```

### Online/Offline Durumu (Presence)

```
ONLINE DURUMU:

  Kullanıcı login → WebSocket bağlantısı açıldı → status = "online" 🟢
  Kullanıcı logout → WebSocket kapandı → status = "offline" ⚫
  Bağlantı koptu → heartbeat timeout → status = "offline"

HEARTBEAT MEKANİZMASI:
  Client her 5 saniyede → "Ben hâlâ buradayım!" → Server
  30 saniye heartbeat gelmezse → "Offline oldu!" 🔴

FANUT SORUSY:
  Ali online oldu → 500 arkadaşına "Ali online!" bildirimi?
  → 500 × 50M DAU = DELİ GIBI trafik!

  ÇÖZÜM:
  → Küçük gruplar: Gerçek zamanlı bildir ✅
  → Büyük arkadaş listesi: LAZY load → sohbet açınca kontrol et!
  → "Ali şu an online mı?" → Ali'nin sohbetini açtığında SOR
```

---

## 13. 🔍 Search Autocomplete Tasarımı

### Problem

```
Google arama çubuğu gibi otomatik tamamlama:
  → Kullanıcı "sis" yazıyor → ["sistem tasarımı", "sistem analizi", ...]
  → Her karakter girişinde ÖNERİLER
  → Gecikme < 100ms ŞART! (kullanıcı beklemez!)
  → Popülerliğe göre sıralı
```

### Trie (Prefix Tree) Veri Yapısı

```
En temel veri yapısı: TRIE

        (root)
       /  |  \
      s   t   ...
     /
    i
   / \
  s   z
  |   |
  t   e → "size" (freq: 500)
  |
  e
  |
  m → "sistem" (freq: 10000) ✅

  "sis" yazıldığında:
  → root → s → i → s → alt ağaçtaki TÜM kelimeleri bul
  → Frekansa göre sırala → ilk 5'i döndür!

SORUN: Alt ağaçta milyonlarca kelime olabilir → hepsini dolaşmak YAVAŞ!

ÇÖZÜM: Her düğümde "top k sonuç" ONCEDEN hesapla ve SAKLA!

  s → [sistem(10K), sıralama(8K), sinema(7K)]
  si → [sistem(10K), sınav(6K), sinema(7K)]
  sis → [sistem(10K), sistematik(3K)]

  → Sorgu gelince → düğüme git → hazır listeyi DÖN! → O(prefix_length) ✅
  → Trade-off: Daha fazla bellek ama ÇOK hızlı sorgular!
```

### Veri Toplama ve Güncelleme

```
FREKANS GÜNCELLEME:
  Her arama yapıldığında Trie'ı güncellemeli miyiz?
  → HAYIR! Her karakter girişinde Trie'ı değiştirmek ÇOK PAHALI!

  ÇÖZÜM: İKİ AŞAMALI

  1. GERÇEK ZAMANLI LOG:
     → Her arama olacak bir şekilde loglanır
     → search_logs tablosu: (query, timestamp)
     → Veya Kafka/Kinesis streaming

  2. PERİYODİK GÜNCELLEME (Offline):
     → Haftalık/günlük batch job
     → Logları aggregate et → frekansları hesapla → yeni Trie oluştur
     → Eski Trie'ı ATOMİK olarak yenisiyle değiştir!

  Neden gerçek zamanlı değil?
  → Trie güncellemesi = kilitlenmeler, yarış koşulları, yavaşlık
  → Autocomplete sonuçlarının 1 saat eski olması KABUL EDİLEBİLİR
  → Trend konular hariç! (bunlar ayrı, gerçek zamanlı pipeline ile)
```

### Ölçekleme

```
TRIE ÇÖZÜMÜ:

  Trie bellekte: 1 trie = ~1GB
  → TEK sunucu yeterli! ama SPOF...

ÇÖZÜM 1: REPLİKASYON
  → Aynı Trie'ın N kopyası → load balancer ile dağıt
  → Bir replika çökerse → diğerleri devam eder ✅

ÇÖZÜM 2: SHARDİNG (bölümleme)
  → Trie çok büyükse → prefix'e göre böl!
  → Shard A: a-m ile başlayanlar
  → Shard B: n-z ile başlayanlar
  → Akıllı sharding: popüler prefix'ler AYRI shard
    (ör: "s" çok popüler → kendi shard'ı olsun!)

ÇÖZÜM 3: CDN + CACHE
  → Autocomplete sonuçları çok yüksek CACHE HIT oranı
  → "sis" araması → sonuçlar aynı → CDN'de cache'le!
  → p99 gecikme: <50ms (kullanıcıya en yakın CDN'den!)

FILTRELEME:
  → Nefret söylemi, müstehcen içerik filtreleme
  → Filter katmanı: Trie sonuçlarından geçir → blacklist'te mi? → çıkar!
```

---

## 14. 🎬 YouTube Tasarımı

### Problem

```
YouTube gibi video streaming servisi tasarla:
  → Video yükleme
  → Video izleme (streaming)
  → 5M DAU, 10% video yükler = 500K video/gün
  → Ortalama video: 300MB → 150TB/gün depolama!
```

### Video Yükleme Pipeline

```
┌────────┐     ┌────────────┐     ┌─────────────┐     ┌──────────┐
│ Client │────→│ API Server │────→│ Transcoding │────→│ Object   │
│        │     │             │     │ Service     │     │ Storage  │
└────────┘     └────────────┘     └─────────────┘     │ (S3/GCS) │
                     │                                 └──────┬───┘
                     ▼                                        │
               ┌──────────┐                             ┌─────▼────┐
               │ Metadata │                             │ CDN      │
               │ DB       │                             │          │
               └──────────┘                             └──────────┘

AKIŞ:
  1. Client video yükler → API Server
  2. Orijinal video → Object Storage (S3)
  3. Transcoding Service video'yu İŞLER:
     → 360p, 480p, 720p, 1080p, 4K formatlarına dönüştür
     → H.264, VP9, AV1 codec'lerine encode et
     → Thumbnail üret
  4. İşlenmiş videolar → CDN'e dağıt
  5. Metadata (başlık, açıklama, URL) → DB'ye kaydet
```

### Video Transcoding

```
NEDEN TRANSCODING?
  → Kullanıcı 4K yükledi ama izleyenin interneti yavaş → BUFFER! 🔄
  → Çözüm: BİRDEN FAZLA kaliteye dönüştür
  → Adaptive bitrate streaming: video otomatik kalite düşür/artır

  Orijinal: 4K (15GB)
     ↓ Transcoding
  ├── 4K    (15 GB)  → Fiber internet
  ├── 1080p (3 GB)   → Normal internet
  ├── 720p  (1.5 GB) → Mobil
  ├── 480p  (700 MB) → Yavaş bağlantı
  └── 360p  (300 MB) → Çok yavaş bağlantı

DAG (Directed Acyclic Graph) Pipeline:
  → Video → [Split into segments] → [Parallel encode]
  → Her segment BAĞIMSIZ encode edilir → paralellik! 🚀
  → Segment 1 encode bitti → kullanıcı İZLEMEYE BAŞLAR!
    (tüm video bitmesini beklemesine GEREK YOK!)
```

### Video Streaming (İzleme)

```
STREAMING PROTOKOLLERİ:
  → MPEG-DASH: Adaptive, açık standart
  → Apple HLS: iOS/Safari'de yaygın
  → Her ikisi de: Video segmentlere bölünür → segment segment indirilir

  İzleme akışı:
  1. Kullanıcı play'e bastı
  2. Video player → CDN'den en yakın sunucuyu bul
  3. Manifest dosyasını indir (segment listesi + kalite seçenekleri)
  4. İlk segmentleri indir → OYNATMAYA BAŞLA! ▶️
  5. İnternet hızına göre kaliteyi OTOMATIK ayarla
     → Hız düştü → 720p'ye geç (buffer olmasın!)
     → Hız arttı → 1080p'ye geç (daha kaliteli!)

PRE-SIGNED URL:
  → Video URL'leri tahmin edilemez olmalı (güvenlik!)
  → CDN'den pre-signed URL al → belirli süre GEÇERLİ → sonra expire!

CDN OPTIMIZASYONU:
  → Popüler videolar: TÜM CDN edge'lerinde cache ✅
  → Az izlenen videolar: Sadece origin'de → istek gelince CDN'e çek
  → "Long tail" → videoların %80'i az izleniyor → hepsi CDN'de olmasın (maliyet!)
```

### Maliyet Optimizasyonu

```
Video depolama PAHALI! (150TB/gün!)

OPTİMİZASYONLAR:
  1. Popüler videolar → CDN'de tut (SIK erişim)
     Az izlenen → ucuz depolama (S3 Glacier) → nadiren erişim

  2. Short video → tüm kalitelerde encode et
     Long video (3 saat film) → sadece popülerse yüksek kalite

  3. Belirli bölgede popüler → O CDN'de tut
     (Türkçe video → Avrupa CDN'de tut, ABD CDN'de tutma!)

  4. Kendi CDN'ini MİNİMİZE et → partner CDN kullan
     (Akamai, CloudFront ilk yıllarda daha ucuz)
```

---

## 15. 📁 Google Drive Tasarımı

### Problem

```
Google Drive / Dropbox gibi dosya depolama ve senkronizasyon servisi:
  → Dosya yükleme/indirme
  → Dosya senkronizasyonu (birden fazla cihaz)
  → Dosya paylaşımı
  → Dosya versiyonları (revision history)
  → 50M kullanıcı, 10M DAU
```

### Temel Bileşenler

```
┌─────────┐     ┌────────────┐     ┌────────────┐     ┌───────────┐
│ Client  │────→│ API Server │────→│ Metadata   │     │ Block     │
│ (App)   │     │ (stateless)│     │ DB         │     │ Storage   │
└────┬────┘     └────────────┘     └────────────┘     │ (S3)     │
     │                                                 └───────────┘
     │           ┌────────────┐     ┌────────────┐
     └──────────→│ Block      │────→│ Cloud      │
       upload    │ Server     │     │ Storage    │
                 └────────────┘     └────────────┘

BLOCK STORAGE (ANAHTAR KONSEPT!):
  → Dosyayı BÜTÜN olarak yükleme! → Çok yavaş ve israf!
  → Dosyayı BLOKLARA böl (4MB chunk'lar)

  Örnek: 100MB dosya = 25 blok
  → 1 blok değişti → SADECE o bloğu yeniden yükle!
  → %96 tasarruf! (25 blok yerine 1 blok)

  + Delta sync: Sadece DEĞİŞEN byte'ları gönder (rsync gibi)
  + Sıkıştırma (compression): gzip ile blokları sıkıştır → daha az upload
```

### Dosya Senkronizasyonu

```
A cihazında dosya değişti → B cihazına nasıl yansır?

NOTIFICATION SERVICE:
  → Long polling veya WebSocket
  → "Dosya değişti!" bildirimi → diğer cihazlara

AKIŞ:
  1. Client A: dosya değişti → değişen blokları tespit et
  2. Sadece değişen blokları upload et → Block Storage
  3. Metadata güncelle (yeni blok hash'leri, versiyon++)
  4. Notification: "file_123 güncellendi!" → Client B, C'ye bildir
  5. Client B: bildirimi aldı → metadata çek → değişen blokları indir → birleştir
  → Dosya senkronize! ✅

ÇAKIŞMA ÇÖZÜMÜ:
  → A ve B AYNI ANDA aynı dosyayı değiştirdi!
  → İlk kaydeden KAZANIR
  → İkinciye: "ÇAKIŞMA var! İki versiyon oluşturuldu, birini seç!"
  → Google Docs: Operational Transform (OT) veya CRDT ile gerçek zamanlı çözüm
    (bu ayrı bir tasarım konusu!)
```

### Metadata Database

```
TABLOLAR:

  users:           files:                   blocks:
  ─────            ──────                   ───────
  user_id (PK)     file_id (PK)            block_id (PK)
  email            file_name                file_version_id
  name             owner_id → users         block_order
  quota_used       is_folder                block_hash (SHA256)
  quota_limit      parent_id → files        size
                   latest_version           storage_path

  file_versions:             sharing:
  ──────────────             ────────
  version_id (PK)            file_id → files
  file_id → files            user_id → users
  version_number             permission (read/write)
  created_at                 created_at
  created_by → users

KAYDETME STRATEJİSİ:
  Metadata → İlişkisel DB (MySQL) → ACID, JOIN, tutarlılık
  Bloklar → Object Storage (S3) → Ucuz, dayanıklı, ölçeklenebilir
  → İkisi AYRI! Doğru araç, doğru iş! ✅
```

### Güvenilirlik

```
VERİ KAYBI = KABULEDİLEMEZ! 💀

KORUMA KATMANLARI:
  1. Block Storage (S3): %99.999999999 dayanıklılık (11x9!)
     → 10M dosyada 10,000 YILDA 1 kayıp!

  2. Multi-region replikasyon:
     → Aynı blok EU + US + ASIA'da
     → Bir region çökse → diğerinden oku

  3. Versiyonlama:
     → Her değişiklik = yeni versiyon
     → Yanlışlıkla silme → eski versiyona GERİ DÖN!
     → 30 gün boyunca versiyonlar saklanır

  4. Silme koruması:
     → "Çöp kutusu" → 30 gün bekle → sonra kalıcı sil
     → Kazara silme → kurtarılabilir!
```

---

## 16. � Büyük Şirketlerde System Design Gerçekleri

### Google — Borg, MapReduce ve Ölçek

```
Google'ın ölçeği kitaptaki HER kavramı ZORUNLU kılar:

  → Consistent Hashing: Bigtable, Spanner'da temel
  → Rate Limiter: Tüm public API'larda (Maps, YouTube, Cloud)
  → Message Queue: Pub/Sub ile günde trilyonlarca mesaj
  → Blob Storage: Google Cloud Storage = Google Drive altyapısı

Interview'da Google sorduğunda:
  → Scale BÜYÜK düşün (milyarlarca kullanıcı)
  → "Single point of failure nerede?" sorusu HER ZAMAN sorulur
  → Cost optimization her zaman gündemde
```

### Meta (Facebook) — News Feed & Social Graph

```
Kitaptaki News Feed design Meta'dan ilham alır:

  → Fan-out on write (celebrity problemi dahil)
  → Social graph: Milyarlarca düğüm, trilyon kenar
  → Photo/Video storage: Her gün petabyte'larca yeni veri
  → Real-time chat: WhatsApp → 2B kullanıcı, minimum sunucu

Meta interview'da:
  → "Trade-off'ları açıkla" EN ÖNEMLİ yetenek
  → "Bu tasarım 10x büyüdüğünde ne olur?" HER ZAMAN sorulur
```

### Amazon — DynamoDB ve Distributed Systems

```
Amazon'ın Dynamo makalesi (2007):
  → Consistent hashing'in ENDÜSTRİ UYGULAMASI
  → Eventually consistent model
  → Vector clock ile conflict resolution
  → Kitaptaki Key-Value Store bölümü BURADAN geliyor

Lesson: Alex Xu'nun kitabını okumak iyi,
        ama KAYNAK MAKALELERİ de oku:
  → Google MapReduce (2004)
  → Amazon Dynamo (2007)
  → Facebook TAO (2013)
  → Google Spanner (2012)
```

---

## 17. 🤖 Yapay Zeka Çağında System Design

### AI Sistemi Tasarımı — Yeni Interview Soruları

```
2024+ system design interview'larında AI soruları GELİYOR:

  1. "Design a Recommendation System"
     → Collaborative filtering vs content-based
     → Feature store + model serving
     → Real-time vs batch prediction
     → A/B testing infrastructure

  2. "Design a Machine Learning Pipeline"
     → Data ingestion → Feature engineering → Training → Serving
     → Model versioning (MLflow, Weights & Biases)
     → Canary deployment for models

  3. "Design a Search Engine with Semantic Search"
     → Traditional inverted index + vector embedding
     → Approximate Nearest Neighbor (ANN)
     → Hybrid scoring: BM25 + cosine similarity
```

### AI ile System Design Interview Hazırlığı

```
TASARIM PRATİĞİ:
  "Bana bir system design sorusu sor ve 45 dakikalık 
   interview simülasyonu yapalım. Alex Xu'nun formatını kullan:
   1. İlk 5 dk: Gereksinimleri netleştir
   2. 10 dk: High-level design çiz (ASCII diagram)
   3. 15 dk: Deep dive — bir bileşeni detaylandır
   4. 5 dk: Bottleneck'ları ve scaling stratejilerini tartış
   
   Her adımda beni yönlendir ama cevabı verme.
   Hatalı varsayım yaparsam düzelt."

BACK OF ENVELOPE:
  "Şu senaryo için back-of-the-envelope hesaplama yap:
   - DAU: [X] milyon
   - Her kullanıcı günde [Y] işlem yapıyor
   - Her işlem [Z] KB veri
   QPS, storage, bandwidth, cache gereksinimlerini hesapla.
   Jeff Dean'in latency tablosunu kullan."

TRADE-OFF ANALİZİ:
  "Bu iki yaklaşımı karşılaştır:
   Yaklaşım A: [açıklama]
   Yaklaşım B: [açıklama]
   
   Karşılaştır: Consistency, Availability, Latency, 
   Complexity, Cost, Scalability açılarından.
   Hangi senaryoda hangisi DAHA İYİ?"
```

### Topluluk Görüşleri

```
Alex Xu (kitabın yazarı):
  "System design interview'da en sık yapılan hata:
   Hemen çözüme atlamak.
   İlk 5 dakikayı SORU SORMAYA harca.
   Interviewer'ın gerçekte ne sorduğunu anla."

Grokking System Design Interview (Educative):
  "Alex Xu'nun kitabı + bu online kurs = EN İYİ hazırlık.
   Kitap derinine gider, kurs pratik verir."

Reddit r/systemdesign:
  "Bu kitap sayesinde Amazon L5 system design round'unu geçtim.
   Rate limiter bölümü birebir soruldu."

ByteByteGo (Alex Xu'nun YouTube kanalı):
  → Kitaptaki tüm konular video formatında da var
  → Animasyonlu açıklamalar → görsel öğrenme
```

---

## 18. �🎯 Sonuç ve Bağlantılar

### Her Tasarımda Ortak Paternler

```
┌──────────────────────────────────────────────────┐
│  PATTERN                 │ KULLANILDIĞI YER       │
├──────────────────────────┼────────────────────────┤
│ Load Balancer            │ HER YERDE!             │
│ Cache (Redis)            │ HER YERDE!             │
│ Message Queue            │ Notification, Feed     │
│ Consistent Hashing       │ KV Store, Sharding     │
│ Snowflake ID             │ Chat, URL Shortener    │
│ CDN                      │ YouTube, Drive         │
│ Sharding                 │ KV Store, Chat, Feed   │
│ Replication              │ DB, Cache, Storage     │
│ Rate Limiting            │ API Gateway            │
│ WebSocket                │ Chat, Notification     │
│ Bloom Filter             │ Crawler, de-dup        │
│ Trie                     │ Autocomplete           │
│ Block Storage + Delta    │ Drive, File Sync       │
│ Fan-out (push/pull)      │ Feed, Chat, Notif.     │
│ Pre-signed URL           │ YouTube, Drive         │
│ Heartbeat/Gossip         │ KV Store, Presence     │
│ DAG Pipeline             │ Video Transcoding      │
└──────────────────────────┴────────────────────────┘
```

### System Design Kontrol Listesi

```
Her tasarımda bu soruları sor:

ÖLÇEK:
  □ Kaç kullanıcı? (DAU/MAU)
  □ QPS ne kadar? (Read QPS, Write QPS)
  □ Veri büyüklüğü? (şimdi ve 5 yıl sonra)
  □ Okuma/yazma oranı?

VERİ:
  □ Hangi DB? (SQL vs NoSQL, neye göre seçtim?)
  □ Schema nasıl?
  □ Sharding gerekli mi? Nasıl?
  □ Replication stratejisi?
  □ Cache stratejisi? (what, when, where to cache)

GÜVENİLİRLİK:
  □ Tek nokta arızası (SPOF) var mı?
  □ Replikasyon yeterli mi?
  □ Failover stratejisi?
  □ Veri kaybını engelliyor muyum?

PERFORMANS:
  □ Gecikme hedefi? (p50, p99)
  □ Darboğaz nerede?
  □ Cache ile latency düşüyor mu?
  □ CDN gerekli mi?

ÖLÇEKLENEBİLİRLİK:
  □ Horizontal scaling yapabilir miyim?
  □ Stateless mi?
  □ Auto-scaling var mı?
  □ Hot spot / hot key riski?
```

### Tüm Kitaplarla Bağlantı 🔗

```
📗 Grokking Algorithms → Trie, BFS (crawler), hash tabloları → temel veri yapıları
📕 Clean Code → API tasarımı, temiz interface, isimlendirme
📘 Pragmatic Programmer → Trade-off düşüncesi, "good enough" mimari
📙 Missing README → Incident response, on-call → monitoring & alerting
📗 Philosophy of Software Design → Deep modules → iyi API tasarımı
📘 Design Patterns → Observer (notification), Strategy (rate limit algo)
📕 DDIA → Replication, partitioning, consistency → KV Store, Chat, Feed
📙 Unit Testing → Test piramidi → her bileşeni test et
📗 Refactoring → Karmaşık sistemi adım adım iyileştir
🏛️ Clean Architecture → Katmanlı tasarım → servis ayrımları
🏗️ Fundamentals of SA → Mimari karakteristikler → ility'ler
🔬 Building Microservices → Servis iletişimi, event-driven, saga
🔥 Phoenix Project → Akış, WIP limitleri, monitoring kültürü
🏗️ System Design Interview → TÜM bunları SOMUT sistemlere UYGULAMA!

Bu kitap puzzle'ın SON parçasıdır:
Önceki kitaplar sana PRENSİPLERİ öğretti.
Bu kitap o prensipleri GERÇEK SİSTEMLERDE nasıl
uygulayacağını gösterir! 🧩
```

### Faz 3 İlerleme Durumu 📊

```
FAZ 3 — Mimari & Ölçek (12-18 ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Clean Architecture              ✅
  2. Fundamentals of Software Arch   ✅
  3. Building Microservices          ✅
  4. The Phoenix Project             ✅
  5. System Design Interview Vol 1   ✅  ← BURADASIN

  🎉 FAZ 3 TAMAMLANDI! 🎉
```

---

> **"System design'da 'doğru cevap' yoktur.
> Sadece 'daha iyi trade-off'lar' vardır.
>
> Her karar bir BEDEL taşır:
> Tutarlılık istiyorsan → gecikme ödersin.
> Hız istiyorsan → bellek ödersin.
> Ölçek istiyorsan → karmaşıklık ödersin.
>
> İyi mühendis, bu bedelleri BİLEN
> ve BILINÇLI tercih yapandır.
>
> 'Benim sistemim mükemmel!' diyen
> ya yeterince büyümemiştir,
> ya da trade-off'larını göremiyordur.
>
> Sistem tasarla, trade-off'ları BELGELE,
> ve her gün biraz daha iyi OL."** 🏗️
