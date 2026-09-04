# 🚀 Performance Engineering

> **"Optimize edilebilir olan ölçülebilir olmak zorundadır."** — Brendan Gregg

Bu doküman performans mühendisliğinin **disiplinini** tarif eder: nasıl ölçülür, hangi metoda göre adım adım analiz yapılır, hangi tuzaklar vardır.

---

## 📑 İçindekiler

1. [Performans Felsefesi](#1-performans-felsefesi)
2. [USE, RED, Four Golden Signals](#2-use-red-four-golden-signals)
3. [Latency vs Throughput vs Utilization](#3-latency-vs-throughput-vs-utilization)
4. [Profiling Türleri](#4-profiling-türleri)
5. [Flame Graph Okuma Sanatı](#5-flame-graph-okuma-sanatı)
6. [Mekanik Sempati & CPU](#6-mekanik-sempati--cpu)
7. [Memory & GC](#7-memory--gc)
8. [I/O Performansı](#8-io-performansı)
9. [Network Performansı](#9-network-performansı)
10. [Benchmarking Disiplini](#10-benchmarking-disiplini)
11. [Performance Anti-Pattern'leri](#11-performance-anti-patternleri)

---

## 1. Performans Felsefesi

### Önce ölç, sonra kararla

> *"Premature optimization is the root of all evil."* — Knuth

Ama eksik söylenen kısmı:
> *"Yet we should not pass up our opportunities in that critical 3%."*

**Anlamı:** Ölçmeden optimize etme; ama ölçtüğünde **kritik %3'ü** kaçırma.

### Optimization hiyerarşisi

```
1. Algoritma & data structure       (10-1000x kazanç)
2. Mimari (cache, async, batch)     (10-100x)
3. Implementation efficiency        (2-10x)
4. Compiler / runtime tuning        (1.1-2x)
5. Hardware                         (1.5-3x)
```

> Üst seviyede 1000x kazanç dururken alt seviyede mikro-optimization yapmak **zaman israfı**.

### Performans piramidi

```
    Architecture       ◀ tasarım, en büyük etki
       Code            ◀ algoritma, profiler-guided
       Runtime         ◀ JIT, GC, alloc
       OS              ◀ sched, fs, net stack
       Hardware        ◀ CPU, RAM, NVMe
```

---

## 2. USE, RED, Four Golden Signals

### USE (Brendan Gregg, sistem kaynakları için)

Her kaynak için **3 metrik** izle:

| | Açıklama | Örnek |
|---|---|---|
| **U**tilization | Yoğunluk % | CPU %85 |
| **S**aturation | Kuyruk derinliği | run queue length, swap |
| **E**rrors | Hata sayısı | network errors, disk I/O errors |

Kaynaklar: CPU, memory, disk, network, file descriptor, GPU.

### RED (Tom Wilkie, mikroservis için)

Her endpoint için:

| | Açıklama |
|---|---|
| **R**ate | Saniyede istek |
| **E**rror | Hata oranı |
| **D**uration | p50/p99 latency dağılımı |

### Four Golden Signals (Google SRE)

| | Açıklama |
|---|---|
| **Latency** | İsteğin süresi (başarılı + başarısız ayrı) |
| **Traffic** | Sistem üzerindeki yük |
| **Errors** | Hata oranı |
| **Saturation** | Sistemin "doluluk" hissi |

### Hangisi ne zaman?

| Bağlam | Method |
|---|---|
| Bare-metal / VM kapasitesi | USE |
| Mikroservis health | RED |
| User-facing servis | Four Golden Signals |
| Hepsi birlikte | Üçü tamamlayıcı, çatışmaz |

---

## 3. Latency vs Throughput vs Utilization

### Üçü arasındaki ilişki

```
λ = throughput (req/s)
W = latency (s)
L = sistemde anlık iş (queue depth)

Little's Law:  L = λ × W
```

### Utilization → Latency patlaması

```
W ≈ W_service / (1 - ρ)
   ρ = utilization
```

| ρ (utilization) | Latency çarpanı |
|---|---|
| 0.5 | 2x |
| 0.7 | 3.3x |
| 0.8 | 5x |
| 0.9 | 10x |
| 0.95 | 20x |
| 0.99 | 100x |

> **Tasarım kuralı:** Steady state %70 utilization'da kal. Üzeri → kuyruğa düşer, p99 patlar.
> Detay: [latency-numbers-ve-kapasite-matematigi.md](latency-numbers-ve-kapasite-matematigi.md)

### Throughput vs Latency trade-off

- **Batch** → throughput ↑, latency ↑.
- **Smaller request** → latency ↓, throughput ↓ (overhead).
- **Sweet spot**: workload-specific, ölç.

### Tail Latency

p50 = 10ms, p99 = 1000ms olabilir. **Microservice fan-out** durumunda:

```
99% latency of N parallel requests ≈ p99^N
N=10: %63 isteğin biri 1000ms gözükür → kullanıcının gördüğü %50 1000ms
```

> Dean & Barroso 2013 — *The Tail at Scale* (kaynakca.md).

---

## 4. Profiling Türleri

### Sampling vs Instrumentation

| | Sampling | Instrumentation |
|---|---|---|
| Yöntem | Periyodik stack snapshot | Her function entry/exit'te kayıt |
| Overhead | %1-2 | %10-50+ |
| Doğruluk | İstatistiksel | Tam |
| Hot path | Görünür | Görünür |
| Cold path | Görünmez | Görünür |
| **Üretim** | ✅ Evet | ❌ Genelde hayır |

### CPU Profiling

- **perf** (Linux) — sampling, kernel + userspace.
- **async-profiler** (JVM) — minimal overhead, perf integration.
- **pprof** (Go) — built-in.
- **py-spy** (Python) — sampling, GIL-aware.
- **Instruments** (macOS) — graphical.

### Off-CPU Profiling

> CPU **kullanılmazken** ne kadar süre? Lock bekleme, I/O, sleep.

`perf sched`, `bpftrace`, `offcpu-bpfcc`. **Latency analizi için kritik.**

### Continuous Profiling

> Üretim sürekli (rastgele 1-2 saniye) profiling.

Pyroscope, Parca, Datadog Continuous Profiler, Google Cloud Profiler.

### Memory Profiling

- **Heap dump**: Snapshot, post-mortem.
- **Heap profiler**: Allocation hotspot.
- **Leak detection**: Live set growth.
- Java: jmap + Eclipse MAT, async-profiler `-e alloc`.
- Go: `pprof -alloc_space`, `pprof -inuse_space`.

### eBPF tabanlı

Modern sahanın yıldızı:
- **bcc**: Python tabanlı eBPF tooling.
- **bpftrace**: DTrace-benzeri tek satır.
- **Pixie**: K8s observability.
- **Cilium Hubble**: network observability.

---

## 5. Flame Graph Okuma Sanatı

> Brendan Gregg'in ürünü. **Y ekseni stack derinliği, X ekseni zaman değil — örnekleme yüzdesi.**

```
█████████████████████ root (top frame)
███████ A         ████ B
█████ C  ██ D    ███ E
███ F        ██ G
```

### Okuma kuralları

1. **Genişlik = pahalı.** Geniş kutu → çok zaman.
2. **Yukarı bak**, yatay büyük kutuları ara — bottleneck.
3. **Plateau** (düz tepe) = tek function çok pahalı.
4. **Tower** (dik kulesi) = çağrı zinciri uzun, her biri kısa.
5. **Renk anlamsız** (varsayılan rastgele).

### Differential Flame Graph

İki run karşılaştırması — kırmızı **arttı**, mavi **azaldı**. Optimization sonrası ölçer.

### Off-CPU Flame Graph

Off-CPU zamanı görselleştirir. Lock bekleme, I/O wait, sleep.

---

## 6. Mekanik Sempati & CPU

> Martin Thompson'ın deyimi. Donanımı anlamadan yazılım hızı **dengelenmez**.

### CPU cache

| | Boyut | Latency | Hit eşiği |
|---|---|---|---|
| L1 | 32-64 KB | 1 ns | ~%95 |
| L2 | 256 KB - 1 MB | 4 ns | ~%80 |
| L3 | 4-64 MB | 12 ns | shared |
| RAM | 100+ GB | 100 ns | — |

### Cache line (64 byte) etkisi

- **Spatial locality**: Yan yana data → 1 cache miss tüm satırı getirir.
- **Temporal locality**: Tekrar erişilen data L1'de.

```c
// ✅ Cache-friendly: row-major iteration
for (i=0; i<N; i++) for (j=0; j<N; j++) sum += arr[i][j];

// ❌ Cache-hostile: 64-byte stride
for (j=0; j<N; j++) for (i=0; i<N; i++) sum += arr[i][j];
```

10x hız farkı **algoritma aynıyken**.

### False Sharing

İki thread aynı cache line'da farklı değişken günceller → cache coherence ping-pong.

```c
struct {
  int counter_a;  // thread A günceller
  int counter_b;  // thread B günceller
} state;          // SAME 64-byte line → false sharing!
```

**Çözüm:** Padding (`alignas(64)`).

### Branch Prediction

- Tahmin doğru → 1 cycle.
- Yanlış → 10-20 cycle (pipeline flush).
- Predictable branch (loop, monotonic) → fast.
- Random branch → slow.

```c
// Sıralı array → branch predictor hit
// Random array → miss → 3-5x yavaş
if (a[i] > 128) sum += a[i];
```

### SIMD / Vectorization

- AVX-512: 16 float aynı anda.
- Compiler auto-vectorize (kısıtlamalarla).
- Manuel intrinsic veya library (Eigen, NumPy, Polars).

### CPU bound mu? IO bound mu?

```bash
top  # CPU % yüksek + idle disk → CPU bound
iostat 1  # %iowait yüksek → I/O bound
```

---

## 7. Memory & GC

### Allocation maliyeti

- Stack: 0 cycle (sadece SP shift).
- Heap: 50-200ns + cache miss + GC pressure.
- Pool / arena: ~10ns.

### Object pool / Recycling

Hot path'te allocation **kaçınılır**.

```java
// ❌
for (int i=0; i<1M; i++) {
  byte[] buf = new byte[8192];  // GC pressure
  process(buf);
}

// ✅
byte[] buf = new byte[8192];
for (int i=0; i<1M; i++) {
  process(buf);
}
```

### GC tuneları

#### JVM (G1, ZGC, Shenandoah)

- **G1**: Default, throughput-friendly. Tipik p99 GC pause 100-300ms.
- **ZGC** (JDK 15+): Concurrent, < 10ms pause. Heap'i 16TB'a kadar.
- **Shenandoah** (Red Hat): Benzer ZGC.

```
-Xmx16g -Xms16g       # heap fixed
-XX:+UseZGC
-XX:+UseLargePages
```

#### Go GC

- Concurrent mark-sweep.
- Tipik pause < 1ms.
- `GOGC=100` (default) — heap %100 büyüdükçe collect.
- `GOMEMLIMIT` (1.19+) — soft heap limit.

#### Python / Ruby

- Reference counting + cycle detector.
- GIL nedeniyle multi-thread CPU yapamazsın.
- Multi-process veya async I/O.

### Memory leak diagnosis

| Belirti | Araç |
|---|---|
| RSS sürekli artıyor | jmap, pprof, py-spy --dump |
| Native heap büyüyor | Valgrind, jemalloc profiler |
| File descriptor leak | `lsof`, `/proc/[pid]/fd/` |
| Connection leak | `netstat`, conn pool metrik |

### Memory pressure

- Linux OOM killer rastgele süreç öldürür → kritik servis ölebilir.
- `oom_score_adj` ile koru.
- cgroups memory limit + monitoring.
- Çözüm: bellek hesaplı, swap kullanma, alert ayarla.

---

## 8. I/O Performansı

### Synchronous vs Async I/O

| | sync | async |
|---|---|---|
| Programlama | Basit | Karmaşık |
| Concurrency | Thread başına | Tek thread, çok bağlantı |
| Throughput | Sınırlı | Yüksek |
| Tipik | DB query | Network server |

### `io_uring` (Linux 5.1+)

Kernel ile shared ring buffer → syscall'siz batch I/O.
- 10K req/s'lik yüklerde **2-5x** improvement.
- ScyllaDB, RocksDB, FreeBSD `aio_*`.

### Direct I/O vs Buffered

- **Buffered** (default): OS page cache.
- **Direct** (`O_DIRECT`): Bypass cache, app-managed.
- Database iyice tune'luysa direct.
- Generic file ops için buffered.

### Disk perf metric

- **IOPS**: Saniyede I/O işlem sayısı (random read/write).
- **Bandwidth**: MB/s (sequential).
- **Latency**: p50, p99.

| Disk | IOPS | Bandwidth |
|---|---|---|
| HDD 7200rpm | 100-200 | 100-200 MB/s |
| SATA SSD | 50K-90K | 500-550 MB/s |
| NVMe SSD | 500K-1M | 3-7 GB/s |
| EBS gp3 | 16K (default) | 1 GB/s |
| EBS io2 Block Express | 256K | 4 GB/s |
| Local NVMe (i4i) | 1.5M | 12 GB/s |

### `iostat` okuma

```bash
iostat -xmt 1
# %util = 100 → disk doymuş
# await = total latency (ms)
# r_await + w_await > 100ms → sorun
```

---

## 9. Network Performansı

### TCP tuning

- **Window scaling** (modern kernel default).
- **Congestion control**: `cubic` (default), `bbr` (Google, throughput-friendly).
- **TCP nagle**: `TCP_NODELAY` low-latency için (ama küçük paket).
- **TCP_QUICKACK**: ACK gecikmesini kaldır.

```bash
sysctl -w net.ipv4.tcp_congestion_control=bbr
```

### Connection reuse

- HTTP/1.1 keep-alive: connection başına 50-200 req.
- HTTP/2 multiplex: tek connection üzerinde N stream.
- Connection pool zorunlu (pgbouncer, go's http.Client default).

### TLS overhead

- TLS 1.2 handshake: 2 RTT.
- TLS 1.3: 1 RTT (0-RTT resumption ile 0).
- Session resumption: ticket veya PSK.
- mTLS internal: 5-15% CPU artışı.

### CDN / Edge

- Static asset → CDN (CloudFront, Cloudflare, Fastly).
- Cache hit → user'a 10-30ms.
- Cache miss → origin'e fetch + cache.

### Network hop maliyeti

| | RTT |
|---|---|
| Same DC | 0.5-1 ms |
| Cross-AZ (same region) | 1-3 ms |
| Cross-region (intra-cont.) | 30-70 ms |
| Cross-continental | 70-150 ms |
| Mobile 4G | 50-100 ms |
| Mobile 5G | 10-30 ms |

---

## 10. Benchmarking Disiplini

### En sık hata: warmup yok

```
JIT (JVM, V8) ilk N çağrıyı interpret eder, sonra compile.
Cold benchmark gerçek perf'i göstermez.
```

**Çözüm:** Warmup phase + measurement phase ayrı (JMH, criterion.rs).

### Coordinated omission

> Yük üreteci kuyruğa düşmeyi ölçmüyor → gerçekçi olmayan p99.

Kullan: `wrk2`, `k6`, `gatling`, HdrHistogram. (latency-numbers... #6)

### Statistical rigor

- Tek run **anlamsız**.
- Min 5-10 run, ortalama ± stddev.
- Outlier filtreleme (IQR rule).
- Confidence interval bildir.

### Production-like environment

- 1 CPU local laptop ≠ 32 CPU prod server.
- Local SSD ≠ network EBS.
- "Microbenchmark hızlı" → prod'da rakam değişebilir.

### A/B in production

> Mikrobenchmark + load test + canary deployment + SLO comparison.

Real production traffic → real performance.

### Microbenchmark araçları

- **JMH** (Java).
- **Criterion** (Rust).
- **Google Benchmark** (C++).
- **Go testing.B**.

---

## 11. Performance Anti-Pattern'leri

### 1. Optimize without measuring

```
Mühendis: "Buradaki for loop yavaş."
Profiler: "Aslında database call %95 zamanı alıyor."
```

**Çözüm:** Always profile first.

### 2. Average latency'ye bakmak

p50 = 50ms, p99 = 5000ms olabilir. **%1 kullanıcı terkler**.

### 3. Synchronous everything

Her API call sync chain → tek yavaş bağımlılık tüm sistemi yavaşlatır.

### 4. N+1 queries

ORM lazy load → her object için ayrı query. (anti-pattern-katalogu #8)

### 5. Cache invalidation eksik

> *"There are only two hard things in CS: cache invalidation and naming things."* — Phil Karlton

**Stale data** > **No data**?  Çoğu zaman hayır.

### 6. Premature parallelism

```python
# ❌ 1ms işi thread pool'a atmak
# Setup overhead > work
```

**Çözüm:** Parallelism için iş ≥ 100μs (rule of thumb).

### 7. Lock granularity'si yanlış

- **Coarse lock** (whole map) → contention.
- **Fine lock** (per-key) → memory + complexity.
- **Lock-free** (CAS, atomic) → karmaşık ama hızlı.

### 8. Logging hot path'te

`logger.info(...)` her request'te → I/O bound olabilir. Async appender + sampled logging.

### 9. Over-allocation

Defensive copy, immutable everywhere → GC pressure.

### 10. Profiler reading hatası

- **Self time vs Total time** karıştırma.
- **Sampling bias** (GC pause sırasında snapshot).
- **Inlining** çağrı görünmez yapar.

---

## 🎯 Staff+ Performans Yaklaşımı

### Disipliner adımlar

1. **SLO tanımla** (numerical, user-facing).
2. **Metric topla** (RED, USE, Four Golden).
3. **Gözleme dayalı hipotez** (flame graph okuyarak).
4. **Hedeflenmiş değişiklik** (tek değişken).
5. **A/B test** (production-like).
6. **Decision: keep / revert / iterate**.

### "Bu yavaş" demek yerine

> "p99 latency 850ms, SLO 200ms. Flame graph'a göre %40 zaman `serializeJson` içinde, allocation profile JSON tree node'ları gösteriyor. Streaming serializer denersek 200ms civarı bekliyoruz."

### Hız için 10 quick win sıralaması

1. Index ekle (DB query).
2. N+1 → batch fetch.
3. Cache (Redis, in-memory, CDN).
4. Compression (gzip, brotli).
5. HTTP/2 + connection reuse.
6. Async I/O (block etmiyorsan).
7. Pagination + field selection.
8. Background job'a aktar.
9. Read replica.
10. Algoritma değişimi (O(n²) → O(n log n)).

---

## 📚 İleri Okuma

- Brendan Gregg — *Systems Performance* (2nd ed., 2020)
- Brendan Gregg — *BPF Performance Tools*
- Martin Thompson — Mechanical Sympathy bloğu, LMAX Disruptor papers
- Aleksey Shipilëv — JMH ve JVM perf yazıları
- Mark Callaghan — DB performance bloğu
- Charity Majors — observability yazıları
- High Performance MySQL — Schwartz et al.
- *Database Internals* — Alex Petrov

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
