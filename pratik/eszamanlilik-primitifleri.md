# 🧵 Eşzamanlılık (Concurrency) Primitifleri

> **"Threads are like goto for control flow."** — Edward Lee
> **"Don't communicate by sharing memory; share memory by communicating."** — Rob Pike

Bu doküman concurrency'nin **temel primitiflerini**, yaygın **patterns**'ları ve **tuzakları** kapsar.

---

## 📑 İçindekiler

1. [Concurrency vs Parallelism](#1-concurrency-vs-parallelism)
2. [Threading Modelleri](#2-threading-modelleri)
3. [Memory Model & Happens-Before](#3-memory-model--happens-before)
4. [Lock'lar](#4-locklar)
5. [Lock-Free & Atomics](#5-lock-free--atomics)
6. [Async/Await ve Coroutine'ler](#6-asyncawait-ve-coroutineler)
7. [Concurrency Pattern'leri](#7-concurrency-patternleri)
8. [Backpressure](#8-backpressure)
9. [Yaygın Bug'lar](#9-yaygın-buglar)
10. [Test Stratejileri](#10-test-stratejileri)

---

## 1. Concurrency vs Parallelism

| | Concurrency | Parallelism |
|---|---|---|
| Tanım | Birçok iş **lojik olarak** aynı anda | Birçok iş **fiziksel olarak** aynı anda |
| Donanım | 1 CPU yeterli | N CPU gerekir |
| Örnek | Async I/O, coroutine | Multi-thread CPU compute |
| Konu | İşleri yapılandırma | İşleri hızlandırma |

> Rob Pike: *"Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once."*

---

## 2. Threading Modelleri

### 1:1 (Native threads)

- Her user thread → bir kernel thread.
- Java, .NET, C++ standart.
- Context switch maliyeti: ~1-10 μs.
- Stack: ~1 MB / thread → 10K thread = 10GB.

### M:N (Green threads / Goroutine / Virtual thread)

- Çok user thread → az kernel thread.
- Go (goroutine, ~2KB stack), Erlang BEAM, Java 21+ Virtual Threads (Project Loom).
- Context switch ~100ns (user-space).
- 100K-1M concurrent ucuz.

### Event Loop (Single-threaded async)

- Tek thread + I/O multiplexing (`epoll`, `kqueue`, `io_uring`).
- Node.js, nginx, Redis, Tokio.
- CPU-bound iş thread pool'a atılır.
- ❌ CPU-bound work bloklarsa loop durur.

### Pratik karşılaştırma

```
10K concurrent connection için:
- Java 1:1 thread: ~10 GB RAM, 10K thread context
- Go goroutine: ~20 MB RAM
- Node.js event loop: ~50 MB RAM
- Java 21 Virtual Threads: ~10 MB RAM
```

---

## 3. Memory Model & Happens-Before

### Niye gerek var?

CPU optimize eder:
- **Out-of-order execution**: Komutlar yeniden sıralanır.
- **Cache**: Her core'un kendi L1/L2.
- **Compiler reorder**: Hot path optimizasyonu.

Sonuç: Bir thread'in yaptığı write **diğer thread tarafından** sırasız görülebilir.

### Happens-Before ilişkisi

A happens-before B → A'nın etkileri B'ye **garanti** görünür.

Ne kurar happens-before?
- **Program order** (tek thread içinde).
- **synchronizes-with** (lock release ↔ acquire).
- **Volatile write ↔ volatile read** (Java).
- **Atomic seq-cst** ops.
- **Thread start, join**.

### Volatile ≠ Atomic

```java
// ❌ volatile değil atomic
volatile int counter = 0;
counter++;  // 3 işlem: read, add, write — RACE
```

**Çözüm:** `AtomicInteger.incrementAndGet()`.

### Memory ordering (C++/Rust)

| Order | Garanti | Maliyet |
|---|---|---|
| `relaxed` | Sadece atomic | En ucuz |
| `acquire` | Sonraki op'lar bunu okuyana kadar görünür | Orta |
| `release` | Önceki op'lar bunu yazana kadar bitti | Orta |
| `acq_rel` | Hem | Orta |
| `seq_cst` | Total order | Pahalı |

> 99% durumda `seq_cst` kullan, sadece kritik hot path'te düşür.

---

## 4. Lock'lar

### Mutex (Mutual Exclusion)

```java
synchronized(lock) {
  // critical section
}
// veya
ReentrantLock lock = new ReentrantLock();
lock.lock(); try { ... } finally { lock.unlock(); }
```

### Read-Write Lock

- Çok reader, tek writer.
- Read-heavy load için.
- ❌ Writer starvation riski.

### Spin Lock

- Lock alamayınca **busy-wait**.
- Kısa critical section için.
- Çok core'da kötü (cache line bouncing).

### Lock anti-pattern'leri

#### Deadlock

```
T1: lock(A) → wait(B)
T2: lock(B) → wait(A)
→ Sonsuz bekleme
```

**Çözüm:** Lock'ları **her zaman aynı sırada** al. Sıralanmış lock disiplini.

#### Lock convoying

Çok thread aynı lock'a sırada → throughput çöker. Granularity ↑.

#### Priority inversion

Düşük öncelikli thread lock tutarken yüksek öncelikli bekler.
**Çözüm:** Priority inheritance protocol.

#### Lock contention

```
Profile gösteriyor: %40 zaman lock acquire'da.
```

**Çözüm:**
1. Critical section'ı küçült.
2. Granularity'i artır (per-key lock).
3. Lock-free data structure.
4. Thread-local + periodic merge.

---

## 5. Lock-Free & Atomics

### CAS (Compare-And-Swap)

```c
// atomic: if (*ptr == expected) *ptr = new; return ok
bool ok = CAS(&counter, expected, new);
```

**Lock-free counter:**
```c
do {
  old = counter;
  new = old + 1;
} while (!CAS(&counter, old, new));
```

### ABA Problem

```
T1 reads A
T2 changes A → B → A
T1 CAS(A, ...) succeeds, ama state aslında değişti
```

**Çözüm:** Tag bits, hazard pointer, RCU, generation counter.

### Lock-free veri yapıları

- **Treiber stack**, **Michael-Scott queue** (klasik).
- **Disruptor** (LMAX) — single producer / single consumer ring buffer.
- Java `ConcurrentHashMap`, Go `sync.Map` — striped locks (lock-free değil ama low-contention).

### Wait-free vs Lock-free vs Obstruction-free

- **Wait-free**: Her thread sınırlı adımda bitirir (en güçlü, ender).
- **Lock-free**: En az bir thread ilerler.
- **Obstruction-free**: Yalnız çalışırsa biter.

> Lock-free kodda **her zaman** doğrulama zor. Battle-tested kütüphane kullan.

### RCU (Read-Copy-Update)

Linux kernel'in en güçlü lock-free mekanizması. **Okuyucular hiçbir zaman bloklanmaz**; yazıcı mevcut veriyi kopyalar, kopyayı günceller, pointer'ı atomik olarak değiştirir ve eski versiyonu bir "grace period" sonra siler.

**Nasıl çalışır:**
1. **Read**: Reader `rcu_read_lock()` ile kritik bölgeye girer. Bu bir lock değil, preemption disable (veya sadece bir counter artışı). Sıfır overhead'e yakın.
2. **Copy-Update**: Writer mevcut veriyi kopyalar, kopyada değişiklik yapar, `rcu_assign_pointer()` ile atomik olarak yeni versiyona geçer.
3. **Grace period**: `synchronize_rcu()` çağrılır. Tüm mevcut okuyucular kritik bölgeden çıkana kadar bekler. Ardından eski veri güvenle free edilir.

**Kullanım alanları:**
- **Kernel**: Routing table, firewall rules, module unloading — okuma ağırlıklı, yazma nadir yapılar.
- **Userspace RCU (liburcu)**: High-performance key-value store, read-heavy cache, configuration hot-reload.
- **Java karşılığı**: `CopyOnWriteArrayList` kavramsal olarak benzer ama gerçek RCU değil (tam kopya maliyeti).

**Trade-off:** Okuma neredeyse bedava; yazma maliyetli (kopya + grace period bekleme). Write-heavy workload'larda uygun değil. Grace period süresi ms-saniye mertebesinde; gerçek zamanlı (PREEMPT_RT) kernel'de `SRCU` (Sleepable RCU) varyantı kullanılır.

---

## 6. Async/Await ve Coroutine'ler

### Coroutine = stack-saving function

```python
async def fetch(url):
  result = await http.get(url)  # suspend, başka coroutine çalışır
  return result.json()
```

`await` noktasında coroutine **uykuya yatar** + scheduler başkasını çalıştırır. I/O hazır olduğunda **uyandırılır**.

### Async runtime'lar

| Dil | Runtime |
|---|---|
| Python | asyncio, trio |
| Rust | tokio, async-std |
| JS / Node | event loop (V8) |
| Kotlin | kotlinx.coroutines |
| C# | Task / TPL |
| Go | (built-in scheduler, goroutine) |

### Cancellation

```python
# Python
task = asyncio.create_task(long_op())
task.cancel()
```

```rust
// Rust
let handle = tokio::spawn(long_op());
handle.abort();
```

```go
// Go
ctx, cancel := context.WithCancel(parent)
defer cancel()
```

> **Cancellation propagation** zorunlu — child task'ler de iptal edilmeli.

### Structured Concurrency

> **Tüm child task'ler parent kapsamı içinde** kalır. Parent biterse child'lar da biter.

- Trio (Python) — nursery.
- Kotlin — coroutineScope.
- Java 21 — StructuredTaskScope.
- Rust — `tokio::join!`, `tokio::try_join!`.

**Faydası:** Goroutine leak yok, exception propagation, cancel doğru çalışır.

### Async pitfalls

#### Blocking call in async context

```python
async def handler():
  time.sleep(1)  # ❌ event loop bloklanır!
  await asyncio.sleep(1)  # ✅
```

```rust
async fn handler() {
  std::thread::sleep(Duration::from_secs(1));  // ❌
  tokio::time::sleep(Duration::from_secs(1)).await;  // ✅
}
```

#### Function coloring

```
async function → only callable by another async function
```

Async kod sync koddan **çağrılamaz** (engine olmadan). Tüm stack async olmalı.

---

## 7. Concurrency Pattern'leri

### Producer-Consumer (Bounded Queue)

```go
ch := make(chan Job, 100)  // bounded

// Producer
go func() {
  for job := range incoming { ch <- job }
}()

// Consumer
for w := 0; w < 8; w++ {
  go func() {
    for job := range ch { process(job) }
  }()
}
```

**Bounded queue** = backpressure.

### Worker Pool

Sabit sayıda worker, bounded queue'dan iş çeker.
**Avantaj:** Kontrollü concurrency, predictable resource.

### Fan-out / Fan-in

```go
// Fan-out: 1 → N
for w := 0; w < N; w++ {
  go worker(jobsCh, resultsCh)
}

// Fan-in: N → 1
for r := range resultsCh {
  collect(r)
}
```

### Pipeline

Her stage kendi goroutine/coroutine, channel'larla bağlı.

### Single-Writer Principle

> Bir resource'a tek thread yazsın; diğerleri channel/queue ile rica etsin.

LMAX Disruptor, Redis (single-thread loop) — tasarım örneği.

### Actor Model

- State **kapsüllenmiş**, sadece mesaj ile.
- Mailbox per actor.
- No shared memory → no race.
- Erlang/OTP, Akka, Orleans, Elixir.

### CSP (Communicating Sequential Processes)

- Channel-based.
- Go, Clojure core.async.
- Rob Pike: *"Don't communicate by sharing memory."*

---

## 8. Backpressure

> **Hızlı producer + yavaş consumer = patlama.**
> Backpressure: consumer "yavaş ol" sinyali yollar.

### Mekanizmalar

1. **Bounded queue** — full ise producer bekler.
2. **Reactive Streams** (Java) — `request(N)` demand pull.
3. **TCP flow control** — kernel-level.
4. **HTTP/2 stream window**.
5. **Kafka consumer lag + pause()**.

### Pattern: drop policy

| Strateji | Ne zaman? |
|---|---|
| Block | Critical path, kayıp tolere edilemez |
| Drop newest | Latest data önemli, eski geçmiş |
| Drop oldest | Yeni data önemli (metric, log) |
| Sample | Yüke göre seyreltme |

### Anti-pattern: unbounded buffer

```java
// ❌ OOM riski
new LinkedBlockingQueue<>();  // unbounded
```

```java
// ✅
new LinkedBlockingQueue<>(1000);
```

> "Unbounded queue" = memory leak with extra steps.

---

## 9. Yaygın Bug'lar

### Race Condition

```
T1: x = readBalance()    // 100
T2: x = readBalance()    // 100
T1: writeBalance(x - 50) // 50
T2: writeBalance(x - 30) // 70
→ Lost update!
```

**Çözüm:** Lock, atomic CAS, optimistic locking (version column), serializable tx.

### Deadlock (yukarıda)

### Livelock

İki thread sırayla "ben bırakayım, sen geç" → ilerleme yok.

### Starvation

Bir thread her zaman geç → sürekli expired.
**Çözüm:** Fair lock (FIFO).

### Memory Visibility

```java
// Thread A
running = false;

// Thread B
while (running) { ... }   // Sonsuz döngü riski (kachinizmi visible değil)
```

**Çözüm:** `volatile` veya `AtomicBoolean`.

### Double-checked locking (eski klasik)

```java
// ❌ Pre-Java 5 broken
if (instance == null) {
  synchronized {
    if (instance == null) instance = new ...;
  }
}
```

**Java 5+ çözüm:** `volatile` instance veya holder idiom.

### Goroutine leak

```go
// ❌ ch hiç close edilmezse goroutine sızar
go func() {
  for v := range ch { ... }
}()
```

**Çözüm:** Context cancellation, defer close.

### Async exception swallow

```javascript
// ❌
async function bad() {
  doAsync();  // missing await — promise rejection lost
}

// ✅
await doAsync();
```

---

## 10. Test Stratejileri

### Unit test for concurrency

- Fake clock (`Clock.fixed`, `tokio::time::pause`).
- Deterministic scheduler (Loom for Rust, `JavaPathFinder`).

### Property-based testing

```rust
// Concurrent counter property
#[quickcheck]
fn concurrent_increment(n: u32) -> bool {
  let counter = AtomicU32::new(0);
  (0..n).into_par_iter().for_each(|_| { counter.fetch_add(1, ...); });
  counter.load(...) == n
}
```

### Stress test

- Çok thread çok iterasyon.
- ASAN, TSAN (thread sanitizer) ile.
- Saatlerce çalıştır.

### Race detector

- Go: `go test -race`.
- Rust: `cargo +nightly miri test`.
- C/C++: ThreadSanitizer (`-fsanitize=thread`).
- Java: jcstress.

### Model checking

- TLA+ — spec'i doğrula.
- Loom (Rust) — concurrent permutations.
- SPIN — process model checking.

---

## 🎯 Staff+ Concurrency Yaklaşımı

### Hierarchy of correctness

```
1. Tek thread + queue          (en güvenli)
2. Immutable + functional      
3. Actor / CSP                 
4. Lock-free with proven structure
5. Manual lock                 (en zorlu)
```

> **Tasarım kuralı:** Mümkün olan en üst katmandan başla. İhtiyaç **kanıtlanana** kadar inme.

### "Bu race var mı?" sezgisi

Her shared mutable state'e sor:
- [ ] Kim yazar? Tek mi, çok mu?
- [ ] Kim okur?
- [ ] Read-write race olabilir mi?
- [ ] Memory visibility var mı (happens-before)?
- [ ] Compound operation atomic mı (read-modify-write)?

### Senin yazmamanı dilediğin şeyler

- ❌ Custom mutex implementation.
- ❌ Lock-free queue (battle-tested kullan).
- ❌ "Sadece bir kez init" double-checked.
- ❌ Custom thread pool (built-in / library kullan).
- ❌ Manuel signal handling.

---

## 📚 İleri Okuma

- *The Art of Multiprocessor Programming* — Herlihy & Shavit
- *Concurrency in Go* — Katherine Cox-Buday
- *Java Concurrency in Practice* — Brian Goetz
- *Rust Atomics and Locks* — Mara Bos
- Doug Lea — Java util.concurrent designer's notes
- Martin Thompson — LMAX Disruptor papers
- Joe Armstrong — *Programming Erlang* (Actor)

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
