# 🔬 Advanced Backend Engineering: Staff/Principal Engineer Yol Haritası

## 📋 İçindekiler

1. [Giriş](#giriş)
2. [Distributed Systems Deep Dive](#-distributed-systems-deep-dive)
3. [Performance Engineering](#-performance-engineering)
4. [Advanced Database Architectures](#-advanced-database-architectures)
5. [Platform Engineering](#-platform-engineering)
6. [Advanced Observability](#-advanced-observability)
7. [Streaming & Real-time Systems](#-streaming--real-time-systems)
8. [Advanced Kubernetes & Cloud Native](#-advanced-kubernetes--cloud-native)
9. [Security Architecture](#-security-architecture)
10. [Machine Learning Integration](#-machine-learning-integration)
11. [Compliance & Regulations](#-compliance--regulations)
12. [Technical Leadership & Influence](#-technical-leadership--influence)
13. [Open Source & Community](#-open-source--community)
14. [Career Development](#-career-development)
15. [Chaos Engineering & Resilience](#-chaos-engineering--resilience)
16. [Özet & Next Steps](#-özet--next-steps)
17. [Final Thoughts](#-final-thoughts)

---

## 🎯 Giriş

Bu doküman, senior backend engineer seviyesini aşmış ve **Staff/Principal Engineer** seviyesine ulaşmak isteyen yazılım mühendisleri içindir. Burada:

- **Teorik derinlik** + **Pratik uygulama**
- **Trade-off analysis** (Her şeyin pros/cons'u)
- **Real-world production scenarios**
- **Less known but critical topics**

**Hedef Kitle:**
- 5+ yıl deneyimli backend developers
- Tech lead pozisyonundakiler
- Architecture seviyesinde düşünmek isteyenler
- Distributed systems meraklıları

---

## 🌐 Distributed Systems Deep Dive

### Consistency Models

**CAP Theorem Gerçeği:**
```
CAP Theorem: Consistency, Availability, Partition Tolerance
"Pick 2" is misleading - partitions WILL happen

Gerçek: PACELC Theorem (CAP'in genişletilmişi)
- PA/EL: Partition → Availability, Else → Latency (Cassandra, DynamoDB)
- PC/EC: Partition → Consistency, Else → Consistency (MongoDB, HBase)

Examples:
CP Systems: MongoDB (default), HBase, Redis, Zookeeper
AP Systems: Cassandra, DynamoDB, Riak, CouchDB
```

**Consistency Levels (Database):**
```
Strong Consistency (Linearizable):
- İmkansız distributed systems'te (tek node hariç)
- Her okuma en son yazılan veriyi görür
- Performans maliyeti yüksek
- Example: Spanner (Google), FaunaDB

Sequential Consistency:
- Tüm process'ler aynı order'da görür
- Real-time order garanti değil
- Example: Some distributed databases

Causal Consistency:
- Cause-effect relationship korunur
- A->B ise, herkes önce A sonra B görür
- Performans ve consistency dengesi
- Example: MongoDB causal consistency

Eventual Consistency:
- Sonunda consistent olur (ne zaman belli değil)
- En yüksek availability & performance
- Conflict resolution gerekir
- Example: DynamoDB, Cassandra (default)

Read Your Writes:
- User kendi yazdığını okuyabilir
- Ama başkaları görmeyebilir
- Session consistency
```

**Implementation Example:**
```javascript
// Strong Consistency (SQL transaction)
async function transferMoney(fromId, toId, amount) {
  const transaction = await db.transaction();
  try {
    await transaction.query(
      'UPDATE accounts SET balance = balance - $1 WHERE id = $2',
      [amount, fromId]
    );
    await transaction.query(
      'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
      [amount, toId]
    );
    await transaction.commit();
  } catch (err) {
    await transaction.rollback();
    throw err;
  }
}

// Eventual Consistency (with conflict resolution)
async function updateUserProfile(userId, updates) {
  const currentVersion = await getVersion(userId);
  
  // Vector clock for conflict resolution
  const vectorClock = {
    nodeId: NODE_ID,
    version: currentVersion + 1,
    timestamp: Date.now()
  };
  
  await db.put({
    userId,
    ...updates,
    vectorClock
  });
  
  // Async replication to other nodes
  replicateAsync(userId, updates, vectorClock);
}

// Conflict Resolution (Last Write Wins)
function resolveConflict(versions) {
  return versions.reduce((latest, current) => {
    if (current.vectorClock.timestamp > latest.vectorClock.timestamp) {
      return current;
    }
    return latest;
  });
}
```

### Consensus Algorithms

Dağıtık sistemlerin en temel sorusu şudur: **"Birden fazla makine, bir konuda nasıl anlaşır?"** Buna **consensus** (uzlaşma) denir ve inanılmaz zor bir problemdir.

Şöyle düşünün: 5 arkadaş WhatsApp grubunda akşam yemeği için restoran seçmeye çalışıyor. Herkes farklı şey yazıyor, mesajlar gecikmeli geliyor, birinin telefonu kapanıyor, biri mesajı görüp cevap vermiyor. İşte dağıtık sistemlerde consensus tam olarak bu kaos ortamında "herkesin aynı karara varması" demek.

**Neden consensus gerekli?**
- **Leader election:** Bir cluster'da kimin boss olduğuna karar vermek (Kubernetes'te etcd bunu yapar)
- **Distributed locks:** Aynı kaynağa aynı anda erişimi engellemek
- **State machine replication:** Tüm node'ların aynı state'e sahip olmasını garantilemek
- **Configuration management:** Tüm node'ların aynı config'i görmesini sağlamak

FLP Impossibility Theorem (1985) der ki: Asenkron bir sistemde, tek bir node bile crash olabiliyorsa, **deterministic consensus imkansızdır**. Ama pratikte timeout'lar ve randomization ile bu sorunu "yeterince iyi" çözüyoruz. İşte Raft ve Paxos bu "yeterince iyi" çözümler.

#### Raft (Understandable Consensus)

Raft, 2014'te Diego Ongaro ve John Ousterhout tarafından tasarlandı. Motivasyonu çok basit: **"Paxos'u kimse anlamıyor, anlaşılabilir bir consensus algoritması yapalım."** Ve başardılar! Raft'ın en büyük gücü anlaşılabilirliğidir.

Raft'ı bir **şirket toplantısı** gibi düşünün:
- **Leader (CEO):** Tüm kararları alır ve dağıtır. Tek bir lider vardır.
- **Followers (Çalışanlar):** Liderin kararlarını uygular. Pasif olarak beklerler.
- **Candidates (Aday):** Lider düştüğünde seçime giren adaylar.

Lider düzenli olarak "heartbeat" gönderir — "Ben hâlâ buradayım" mesajı. Heartbeat gelmezse, follower'lar "lider öldü" der ve seçim başlar. Tıpkı bir CEO'nun toplantıya gelmemesi gibi — birileri "ben yönetiyorum artık" der.

**Core Concepts:**
```
Leader Election:
- Bir leader seçilir (follower'lar oy verir)
- Leader tüm yazma isteklerini handle eder
- Heartbeat ile leader'lık sürer

Log Replication:
- Client -> Leader'a istek
- Leader -> Follower'lara log entry
- Majority commit -> Apply to state machine

Safety:
- Committed entry asla kaybolmaz
- Logs eventually consistent
```

**Implementation Insight:**
```go
// Raft state machine
type RaftNode struct {
    currentTerm int
    votedFor    string
    log         []LogEntry
    commitIndex int
    lastApplied int
    state       NodeState // Leader, Follower, Candidate
}

// Leader election
func (r *RaftNode) StartElection() {
    r.currentTerm++
    r.state = Candidate
    r.votedFor = r.id
    
    votes := 1
    for _, peer := range r.peers {
        if peer.RequestVote(r.currentTerm, r.id) {
            votes++
        }
    }
    
    if votes > len(r.peers)/2 {
        r.BecomeLeader()
    }
}

// Log replication
func (r *RaftNode) AppendEntries(entry LogEntry) error {
    if r.state != Leader {
        return ErrNotLeader
    }
    
    // Append to own log
    r.log = append(r.log, entry)
    
    // Replicate to followers
    successCount := 1
    for _, peer := range r.peers {
        if peer.AppendEntries(entry) {
            successCount++
        }
    }
    
    // Majority check
    if successCount > len(r.peers)/2 {
        r.commitIndex = len(r.log) - 1
        return nil
    }
    
    return ErrNotCommitted
}
```

**Real-world Usage:**
- etcd (Kubernetes backend)
- Consul
- CockroachDB

#### Paxos (Original Consensus)

Paxos, Leslie Lamport tarafından 1989'da yayınlandı (aslında 1990'da bir Yunan adasındaki parlamenter sistem analojisiyle). Akademik dünyada **"consensus = Paxos"** denirdi yıllarca. Ama bir sorun var: Lamport'un kendi makalesini bile insanlar anlamakta zorlandı. Google, Chubby lock service'ini Paxos üzerine kurdu ve mühendisler "bu algoritmayı implement etmek kabus" dedi.

Paxos'un arkasındaki fikir aslında basit: **"Çoğunluk ne derse o olur, ama herkes önceki sözlerini tutmalı."** Ama edge case'leri ve multi-round senaryoları işleri çok karmaşıklaştırır.

**Daha karmaşık ama proven:**
```
Roles:
- Proposer: Proposes values
- Acceptor: Votes on proposals
- Learner: Learns chosen value

Phases:
1. Prepare: Proposer sends proposal number
2. Promise: Acceptors promise not to accept lower proposals
3. Accept: Proposer sends value
4. Accepted: Acceptors accept value

Properties:
- Only one value chosen
- Learner eventually learns chosen value
```

**Neden Raft Tercih Edilir:**
- Raft daha anlaşılır — Ongaro'nun doktora tezinde öğrencilere Raft ve Paxos öğretildi, Raft'ı öğrenenler sınavda %33 daha yüksek puan aldı!
- Implementation kolaylığı — etcd, Consul, CockroachDB hepsi Raft kullanıyor
- Debugging easier — state'ler net tanımlı: Leader, Follower, Candidate. Paxos'ta "bu node şu an ne yapıyor?" sorusuna cevap vermek zor
- Paxos mathematically proven ama karmaşık — Google bile Chubby'yi implement ederken zorlandı

**Gerçek dünya kullanımları:**
- **etcd (Kubernetes'in beyni):** K8s tüm cluster state'ini etcd'de tutar. etcd Raft kullanır. Yani her `kubectl apply` yaptığınızda, arka planda Raft consensus çalışıyor!
- **CockroachDB:** Distributed SQL database, her range (veri parçası) için ayrı bir Raft group çalıştırır
- **Consul:** HashiCorp'un service discovery ve configuration aracı
- **TiKV:** TiDB'nin storage engine'i, Raft ile replicate eder

### Distributed Transactions

#### Two-Phase Commit (2PC)

**How it works:**
```
Phase 1 - Prepare:
Coordinator: "Can you commit this transaction?"
Participants: "Yes" or "No"

Phase 2 - Commit/Abort:
If all "Yes": Coordinator: "Commit!"
If any "No": Coordinator: "Abort!"
```

**Problem:**
```javascript
// Blocking problem
async function twoPhaseCommit(participants, transaction) {
  // Phase 1: Prepare
  const votes = await Promise.all(
    participants.map(p => p.prepare(transaction))
  );
  
  if (votes.every(v => v === 'YES')) {
    // Phase 2: Commit
    // ⚠️ If coordinator crashes here, participants block forever!
    await Promise.all(
      participants.map(p => p.commit(transaction))
    );
    return 'COMMITTED';
  } else {
    // Phase 2: Abort
    await Promise.all(
      participants.map(p => p.abort(transaction))
    );
    return 'ABORTED';
  }
}

// Issues:
// 1. Coordinator single point of failure
// 2. Participants block if coordinator fails
// 3. Not partition-tolerant
// 4. Performance overhead
```

#### Three-Phase Commit (3PC)

**Improvement over 2PC:**
```
Phase 1: CanCommit
Phase 2: PreCommit
Phase 3: DoCommit

Advantage:
- Non-blocking (uses timeout)
- Can make progress with coordinator failure

Disadvantage:
- Still not partition-tolerant
- More network round trips
```

#### Saga Pattern (Modern Approach)

Neden "Modern Approach" diyoruz? Çünkü dağıtık sistemlerde transaction yönetiminin eski yöntemi **Two-Phase Commit (2PC)** idi. 2PC'yi düşünün: bir düğün organizatörü gibi — "Herkes hazır mı? Evet? Tamam, hep birlikte başlıyoruz!" Kulağa güzel geliyor ama pratikte **ölçeklenmiyor**. Bir servis yanıt vermezse tüm sistem kilitleniyor, coordinator çökerse herkes askıda kalıyor. Microservices dünyasında 10-20 servisin aynı anda 2PC ile koordine olmasını hayal edin — kabus!

Saga Pattern, microservices'in bu soruna verdiği **modern cevap**. Temel fikir şu: büyük bir distributed transaction'ı küçük, birbirini takip eden **lokal transaction'lara** böl. Her servis kendi işini yapsın, başarısız olursa **compensating action** (telafi edici işlem) çalıştırsın.

Saga'nın iki tadı (flavor) var:

**1. Choreography (Koreografi — Event-Driven):** Her servis kendi başına dans eder. Bir event yayınlar, diğer servisler bu event'i dinleyip tepki verir. Hiçbir merkezi koordinatör yok — herkes kendi rolünü bilir.
- ✅ **Avantajları:** Loosely coupled (gevşek bağlı), basit, her servis bağımsız. Yeni servis eklemek kolay — sadece event'i dinle.
- ❌ **Dezavantajları:** Akışı takip etmek zor ("Bu event'i kim dinliyor?" sorusuna cevap aramak kabus). Merkezi bir görünüm yok, debugging cehennem. 10 servisten sonra spaghetti event akışı oluşur.

**2. Orchestration (Orkestrasyon — Central Coordinator):** Bir orkestra şefi var. Saga Orchestrator her adımı sırayla yönetir: "Önce sen yap, sonra sen, sonra sen." Her şey merkezi bir yerden kontrol edilir.
- ✅ **Avantajları:** Akış net ve anlaşılır, debug etmesi kolay, saga'nın hangi adımda olduğunu her zaman bilirsiniz.
- ❌ **Dezavantajları:** Single point of failure riski (orchestrator çökerse?), merkezi coordinator tüm iş mantığını bilmek zorunda — servisler arası coupling artabilir.

**Ne Zaman Saga Kullanmalı?**
Cross-service business transaction'larda Saga şart:
- **E-commerce sipariş akışı:** Sipariş oluştur → Stok düş → Ödeme al → Kargo başlat. Ödeme başarısız? → Stoku geri koy, siparişi iptal et.
- **Ride-sharing (Uber modeli):** Yolcu eşle → Sürücü ata → Ödeme al → Yolculuğu başlat. Ödeme başarısız? → Sürücüyü serbest bırak, yolcuya bildir.

**Idempotency — Hayati Önem!** 🚨
Compensating action'lar birden fazla kez çalışabilir (network retry, message duplicate). Bu yüzden her compensating action **idempotent** OLMAK ZORUNDA. Yani aynı işlemi 1 kez de çalıştırsan 10 kez de çalıştırsan sonuç aynı olmalı. Örnek: "Ödemeyi iade et" işlemi 3 kez çağrılırsa, müşteriye 3 kez değil 1 kez iade yapmalı!

**Saga Log — Orchestrator Çökerse Ne Olur?**
Saga state'ini **persist etmek** (kalıcı hale getirmek) zorundasınız. Neden? Orchestrator saga'nın 5. adımındayken çökerse, restart sonrası "Nerede kalmıştık?" sorusuna cevap verebilmeli. Saga log olmadan, yarım kalmış bir transaction'ı ne tamamlayabilirsiniz ne de geri alabilirsiniz — en kötü senaryo: **veri tutarsızlığı**. Bu yüzden saga state'i veritabanında veya event store'da saklanır.

**Choreography-based:**
```javascript
// Each service listens to events and acts

// Order Service
async function createOrder(orderData) {
  const order = await Order.create(orderData);
  await eventBus.publish('OrderCreated', order);
  return order;
}

eventBus.on('PaymentFailed', async (event) => {
  await Order.update(event.orderId, { status: 'CANCELLED' });
  await eventBus.publish('OrderCancelled', { orderId: event.orderId });
});

// Payment Service
eventBus.on('OrderCreated', async (event) => {
  try {
    const payment = await processPayment(event);
    await eventBus.publish('PaymentSucceeded', payment);
  } catch (err) {
    await eventBus.publish('PaymentFailed', { orderId: event.orderId });
  }
});

// Inventory Service
eventBus.on('PaymentSucceeded', async (event) => {
  try {
    await reserveInventory(event.items);
    await eventBus.publish('InventoryReserved', event);
  } catch (err) {
    await eventBus.publish('InventoryReservationFailed', event);
    // Payment service will need to refund
  }
});

eventBus.on('OrderCancelled', async (event) => {
  await releaseInventory(event.orderId);
});
```

**Orchestration-based (Better for complex flows):**
```javascript
// Saga Orchestrator
class OrderSaga {
  async execute(orderData) {
    const saga = new SagaRunner();
    
    try {
      // Step 1: Create order
      const order = await saga.step(
        'createOrder',
        () => orderService.create(orderData),
        (order) => orderService.cancel(order.id) // compensating action
      );
      
      // Step 2: Process payment
      const payment = await saga.step(
        'processPayment',
        () => paymentService.charge(order.total, order.userId),
        (payment) => paymentService.refund(payment.id)
      );
      
      // Step 3: Reserve inventory
      const reservation = await saga.step(
        'reserveInventory',
        () => inventoryService.reserve(order.items),
        (reservation) => inventoryService.release(reservation.id)
      );
      
      // Step 4: Schedule shipping
      await saga.step(
        'scheduleShipping',
        () => shippingService.schedule(order.id),
        (shipment) => shippingService.cancel(shipment.id)
      );
      
      await saga.commit();
      return { success: true, order };
      
    } catch (error) {
      // Automatically runs compensating actions in reverse order
      await saga.rollback();
      throw error;
    }
  }
}

// Saga Runner (tracks state)
class SagaRunner {
  constructor() {
    this.sagaId = crypto.randomUUID(); // ✅ sagaId tanımla!
    this.steps = [];
    this.completedSteps = [];
  }
  
  async step(name, action, compensate) {
    try {
      const result = await action();
      this.completedSteps.push({ name, result, compensate });
      return result;
    } catch (error) {
      console.error(`Step ${name} failed:`, error);
      throw error;
    }
  }
  
  async rollback() {
    // Execute compensating actions in reverse
    for (const step of this.completedSteps.reverse()) {
      try {
        await step.compensate(step.result);
        console.log(`Compensated: ${step.name}`);
      } catch (err) {
        console.error(`Compensation failed for ${step.name}:`, err);
        // Log to DLQ for manual intervention
      }
    }
  }
  
  async commit() {
    // Mark saga as complete
    await sagaLog.markComplete(this.sagaId);
  }
}
```

**Saga Pattern Trade-offs:**
```
Pros:
✓ No distributed locks
✓ Works across services/databases
✓ Partition tolerant
✓ Scalable

Cons:
✗ Eventual consistency
✗ Compensating logic complexity
✗ Debugging harder
✗ Idempotency required
```

### Clock Synchronization & Ordering

#### Logical Clocks (Lamport Timestamps)

Dağıtık sistemlerin en temel ve en sinir bozucu problemiyle başlayalım: **Global bir saat YOK!** 🕐

Bunu şöyle düşünün: 5 kişi, 5 ayrı odada, her birinin kolunda farklı bir saat var. Birinin saati 14:00'ü gösterirken diğerininki 14:02, bir diğerininki 13:58. Şimdi bu 5 kişiye "Saat tam 14:00'de düğmeye basın" deseniz, hepsi farklı zamanlarda basacak. İşte dağıtık sistemlerdeki sunucular tam olarak bu durumda.

**NTP (Network Time Protocol)** saatleri senkronize etmeye çalışır, ama network latency yüzünden saatler **HİÇBİR ZAMAN** mükemmel şekilde senkronize olamaz. En iyi durumda bile milisaniye düzeyinde sapma (drift) var. "Ama milisaniye ne ki?" diyebilirsiniz — bir veritabanı saniyede binlerce işlem yapıyorsa, milisaniye farkı hangi yazmanın önce geldiğini belirleyememeniz demek!

**Leslie Lamport'un dahice içgörüsü** şuydu: Gerçek zamana ihtiyacımız yok, **sıralamaya** ihtiyacımız var! Önemli olan saat kaçta olduğu değil, A olayının B olayından **önce** gerçekleşip gerçekleşmediği (happened-before relationship, `A → B`).

**Lamport Clock nasıl çalışır?**
- Her işlemde (process) bir sayaç var, 0'dan başlar.
- **Lokal olay** olduğunda: sayacı 1 artır.
- **Mesaj gönderirken:** sayacı 1 artır ve mesajla birlikte gönder.
- **Mesaj alırken:** `max(kendi_sayacı, gelen_sayaç) + 1` yap.

Bu kadar basit! Ama bir **sınırlama** var: Lamport Clock size `A → B` (A, B'den önce oldu) diyebilir. Ama iki olayın timestamp'i aynıysa veya aralarında mesaj alışverişi yoksa, hangisinin önce olduğunu **BİLEMEZSİNİZ**. Bu olaylara **concurrent (eşzamanlı)** denir.

Bu sınırlama yüzünden **Vector Clock'lar** icat edildi. Vector Clock'lar her process için ayrı bir sayaç tutar, böylece concurrent event'leri de tespit edebilir. "Bu iki olay birbirinden bağımsız mı, yoksa biri diğerinden önce mi oldu?" sorusuna kesin cevap verir.

**Gerçek dünya örneği:** Amazon DynamoDB, conflict resolution (çakışma çözümleme) için vector clock'ları kullanır. İki kullanıcı aynı anda aynı veriyi güncellerse, DynamoDB vector clock'larla hangi yazmanın "kazandığını" belirler veya çakışmayı uygulamaya bildirir.

```javascript
// Lamport Clock implementation
class LamportClock {
  constructor() {
    this.time = 0;
  }
  
  // On local event
  increment() {
    this.time++;
    return this.time;
  }
  
  // On receive message
  update(messageTime) {
    this.time = Math.max(this.time, messageTime) + 1;
    return this.time;
  }
}

// Usage in distributed system
class DistributedNode {
  constructor(nodeId) {
    this.nodeId = nodeId;
    this.clock = new LamportClock();
  }
  
  async sendMessage(toNode, data) {
    const timestamp = this.clock.increment();
    await toNode.receive({
      from: this.nodeId,
      data,
      timestamp
    });
  }
  
  async receive(message) {
    this.clock.update(message.timestamp);
    console.log(`Node ${this.nodeId} received at time ${this.clock.time}`);
    await this.processMessage(message.data);
  }
}

// Property: if A -> B, then timestamp(A) < timestamp(B)
// But timestamp(A) < timestamp(B) doesn't mean A -> B
```

#### Vector Clocks (Better Causality)

Lamport Clock'ların bir eksikliği var: Size olayların sırasını söyler ama **"bu iki olay birbirinden bağımsız mı (concurrent)?"** sorusuna cevap veremez. Lamport'ta `timestamp(A) < timestamp(B)` ise, A'nın B'den önce olduğunu **garanti edemezsiniz** — sadece saat değeri küçük.

Vector Clock'lar bu sorunu çözer. Her node, **tüm node'ların saat değerini** bir vektörde tutar. Üç node'lu bir sistemde: `[Node1: 2, Node2: 5, Node3: 1]`. İki vektörü karşılaştırdığınızda üç sonuç çıkar:

1. **BEFORE (Önce):** Bir vektörün tüm elemanları diğerinden küçük veya eşit → nedensellik var
2. **AFTER (Sonra):** Tam tersi
3. **CONCURRENT (Eşzamanlı):** Bazı elemanlar büyük, bazıları küçük → **bu iki olay birbirinden bağımsız!** İşte Lamport'un yapamadığı şey bu!

**Trade-off:** Vector clock'un boyutu node sayısıyla doğru orantılı büyür. 1000 node'lu bir sistemde her mesajla birlikte 1000 elemanlı bir vektör taşımanız gerekir. Bu yüzden pratikte **dotted version vectors** veya **interval tree clocks** gibi optimizasyonlar kullanılır.

**Gerçek dünya:** Amazon DynamoDB, conflict resolution için vector clock'ların bir varyantını kullanır. Bir shopping cart'a iki farklı cihazdan aynı anda ürün eklediğinizde, DynamoDB bunu concurrent yazma olarak algılar ve uygulamaya "hey, bu iki versiyon conflict'te, sen çöz" der. Bu sayede veri kaybı yaşanmaz — en kötü ihtimalle kullanıcı iki versiyonu görür.

```javascript
// Vector Clock - detects concurrent events
class VectorClock {
  constructor(nodeId, numNodes) {
    this.nodeId = nodeId;
    this.clock = new Array(numNodes).fill(0);
  }
  
  increment() {
    this.clock[this.nodeId]++;
    return [...this.clock];
  }
  
  update(otherClock) {
    for (let i = 0; i < this.clock.length; i++) {
      this.clock[i] = Math.max(this.clock[i], otherClock[i]);
    }
    this.clock[this.nodeId]++;
  }
  
  // Compare two vector clocks
  static compare(a, b) {
    let aGreater = false;
    let bGreater = false;
    
    for (let i = 0; i < a.length; i++) {
      if (a[i] > b[i]) aGreater = true;
      if (a[i] < b[i]) bGreater = true;
    }
    
    if (aGreater && !bGreater) return 'AFTER';  // a happened after b
    if (bGreater && !aGreater) return 'BEFORE'; // a happened before b
    if (!aGreater && !bGreater) return 'EQUAL';
    return 'CONCURRENT'; // can't determine order
  }
}

// Conflict resolution with vector clocks
class ReplicatedKVStore {
  constructor(nodeId, numNodes) {
    this.nodeId = nodeId;
    this.store = new Map();
    this.clock = new VectorClock(nodeId, numNodes);
  }
  
  put(key, value) {
    const version = this.clock.increment();
    this.store.set(key, {
      value,
      version: [...version]
    });
  }
  
  merge(key, remoteValue, remoteVersion) {
    const local = this.store.get(key);
    
    if (!local) {
      this.store.set(key, { value: remoteValue, version: remoteVersion });
      return;
    }
    
    const comparison = VectorClock.compare(local.version, remoteVersion);
    
    switch (comparison) {
      case 'BEFORE':
        // Remote is newer, accept it
        this.store.set(key, { value: remoteValue, version: remoteVersion });
        break;
      case 'AFTER':
        // Local is newer, keep it
        break;
      case 'CONCURRENT':
        // Conflict! Need resolution strategy
        const resolved = this.resolveConflict(local.value, remoteValue);
        this.store.set(key, {
          value: resolved,
          version: this.mergeVersions(local.version, remoteVersion)
        });
        break;
    }
  }
  
  resolveConflict(localValue, remoteValue) {
    // Strategy: Last-write-wins, merge, or application-specific
    // For demo, merge arrays
    if (Array.isArray(localValue) && Array.isArray(remoteValue)) {
      return [...new Set([...localValue, ...remoteValue])];
    }
    return localValue; // Default: keep local
  }
  
  mergeVersions(v1, v2) {
    return v1.map((val, i) => Math.max(val, v2[i]));
  }
}
```

**Real-world Usage:**
- DynamoDB (vector clocks for conflict resolution)
- Riak
- Cassandra (similar concept)

#### CRDTs (Conflict-free Replicated Data Types)

Vector Clock'lar conflict'leri **tespit eder** ama çözmez — uygulamanın karar vermesi gerekir. Peki ya veri yapısı kendisi conflict'leri **otomatik olarak çözebilseydi**? İşte CRDT'ler tam olarak bunu yapar.

CRDT, **"ne olursa olsun, merge edilebilir"** veri yapılarıdır. İki replica birbirinden bağımsız güncellense bile, merge edildiğinde tutarlı ve doğru bir sonuç garanti eder. Matematiksel olarak, CRDT'ler **join-semilattice** yapısına sahiptir — yani merge işlemi commutative (sıra farketmez), associative (gruplama farketmez) ve idempotent (aynı merge'i tekrar yapsan sonuç değişmez).

Bunu bir **oy sayımı** gibi düşünün: Her sandıkta ayrı ayrı oylar sayılıyor. Sonra hepsini topluyorsunuz. Hangi sırayla toplarsanız toplayın, sonuç aynı çıkar. İşte G-Counter CRDT'si tam olarak bu.

**Temel CRDT Tipleri:**

1. **G-Counter (Grow-only Counter):** Sadece artabilen sayaç. Her node kendi sayacını artırır, toplam = tüm node'ların toplamı. YouTube view count buna benzer.

2. **PN-Counter (Positive-Negative Counter):** İki G-Counter'dan oluşur — biri artış, biri azalış. Sonuç = P - N. Beğeni/beğenmeme sistemi gibi.

3. **G-Set (Grow-only Set):** Sadece eleman eklenebilen küme. Silme yok. Basit ama kısıtlı.

4. **OR-Set (Observed-Remove Set):** Hem ekleme hem silme destekler. Concurrent add ve remove olduğunda, **add kazanır** (add-wins semantics). En pratik CRDT.

5. **LWW-Register (Last-Writer-Wins):** Timestamp'e bakarak son yazanı kabul eder. Basit ama veri kaybı riski var.

```javascript
// G-Counter CRDT Implementation
class GCounter {
  constructor(nodeId) {
    this.nodeId = nodeId;
    this.counts = {}; // { nodeId: count }
  }

  increment() {
    this.counts[this.nodeId] = (this.counts[this.nodeId] || 0) + 1;
  }

  value() {
    return Object.values(this.counts).reduce((sum, c) => sum + c, 0);
  }

  merge(other) {
    // Her node için maksimum değeri al — CONFLICT OLMAZ!
    for (const [nodeId, count] of Object.entries(other.counts)) {
      this.counts[nodeId] = Math.max(this.counts[nodeId] || 0, count);
    }
  }
}

// OR-Set CRDT Implementation
class ORSet {
  constructor(nodeId) {
    this.nodeId = nodeId;
    this.elements = new Map(); // element -> Set of unique tags
    this.tombstones = new Set(); // removed tags
    this.counter = 0;
  }

  add(element) {
    const tag = `${this.nodeId}:${++this.counter}`;
    if (!this.elements.has(element)) {
      this.elements.set(element, new Set());
    }
    this.elements.get(element).add(tag);
  }

  remove(element) {
    const tags = this.elements.get(element);
    if (tags) {
      for (const tag of tags) {
        this.tombstones.add(tag);
      }
      this.elements.delete(element);
    }
  }

  merge(other) {
    // Diğerinin tombstone'larını ekle
    for (const tag of other.tombstones) {
      this.tombstones.add(tag);
    }

    // Diğerinin elementlerini ekle (tombstone'da olmayanları)
    for (const [element, tags] of other.elements) {
      if (!this.elements.has(element)) {
        this.elements.set(element, new Set());
      }
      for (const tag of tags) {
        if (!this.tombstones.has(tag)) {
          this.elements.get(element).add(tag);
        }
      }
    }

    // Kendi elementlerimizden tombstone'da olanları temizle
    for (const [element, tags] of this.elements) {
      for (const tag of tags) {
        if (this.tombstones.has(tag)) tags.delete(tag);
      }
      if (tags.size === 0) this.elements.delete(element);
    }
  }

  values() {
    return [...this.elements.keys()];
  }
}

// Kullanım örneği: İki offline cihaz
const phone = new GCounter('phone');
const laptop = new GCounter('laptop');

phone.increment(); phone.increment(); // phone: 2
laptop.increment(); // laptop: 1

// Merge — sıra farketmez!
phone.merge(laptop);
console.log(phone.value()); // 3 — conflict yok, kayıp yok!
```

**Gerçek dünya kullanımları:**
- **Redis CRDT (Redis Enterprise):** Active-Active geo-replication'da CRDT kullanır. İki datacenter arasında conflict-free sync.
- **Figma:** Collaborative design tool, CRDT-benzeri yapılar kullanarak birden fazla kullanıcının aynı anda düzenleme yapmasını sağlar. Cursor pozisyonları, layer sıralaması — hepsi CRDT.
- **Apple Notes:** iCloud sync'te CRDT kullanır. Uçak modundayken not alırsınız, inerken sync olur — conflict olmadan.
- **Yjs / Automerge:** Açık kaynak CRDT kütüphaneleri. Google Docs benzeri real-time collaborative editing yapabilirsiniz.

**CRDT'lerin trade-off'ları:**
- ✅ Conflict-free — merge her zaman başarılı
- ✅ Offline-first uygulamalar için ideal
- ✅ Eventual consistency garanti
- ❌ Metadata overhead — tombstone'lar, tag'ler fazla yer kaplar
- ❌ Silme karmaşık (tombstone problemi)
- ❌ Her veri yapısı CRDT'ye dönüştürülemez

---

## ⚡ Performance Engineering

### Profiling & Benchmarking

#### CPU Profiling

```javascript
// Node.js built-in profiler
const { Session } = require('inspector');
const fs = require('fs');

// Start profiling
const session = new Session();
session.connect();

session.post('Profiler.enable', () => {
  session.post('Profiler.start', () => {
    // Run your code
    runExpensiveOperation();
    
    // Stop profiling
    session.post('Profiler.stop', (err, { profile }) => {
      fs.writeFileSync('profile.cpuprofile', JSON.stringify(profile));
      session.disconnect();
    });
  });
});

// View in Chrome DevTools
// chrome://inspect -> Load profile
```

**Production Profiling (with 0x):**
```bash
# Install
npm install -g 0x

# Profile
0x node server.js

# Generate flamegraph
# Opens flamegraph in browser
```

**Continuous Profiling (Pyroscope):**
```javascript
const Pyroscope = require('@pyroscope/nodejs');

Pyroscope.init({
  serverAddress: 'http://pyroscope:4040',
  appName: 'my-nodejs-app',
  tags: {
    environment: 'production',
    region: 'us-east-1'
  }
});

Pyroscope.start();

// Now all your code is continuously profiled
```

#### Memory Profiling

Node.js'te memory profiling, **doktorun kan testi yapması** gibidir — her şey yolunda görünse bile, arka planda sessizce büyüyen bir sorun olabilir. V8 JavaScript engine'i otomatik garbage collection (GC) yapar, ama bu "otomatik" kelimesine fazla güvenmeyin.

**V8 Garbage Collector Temelleri:**
V8'in heap'i iki ana bölgeden oluşur:
- **Young Generation (New Space):** Yeni oluşturulan objeler buraya gelir. Küçük ve hızlı GC (Scavenge). Çoğu obje burada ölür — "infant mortality" derler.
- **Old Generation (Old Space):** Young Generation'da hayatta kalan objeler buraya promote edilir. Daha yavaş ama kapsamlı GC (Mark-Sweep-Compact).

**Yaygın Memory Leak Nedenleri:**
1. **Global değişkenler:** `global.cache = []` yazıp sonra temizlemeyi unutmak. Bu array sonsuza dek büyür.
2. **Closure'lar:** Bir closure dış scope'taki büyük bir objeye referans tutuyorsa, o obje GC'lenemez. "Ben sadece küçük bir fonksiyonum" diye masum görünür ama arkasında 50MB'lık bir objeyi esir tutar.
3. **Event Listener'lar:** `emitter.on('data', handler)` ekleyip `removeListener` yapmamak. Her request'te yeni listener eklenirse, bu klasik bir leak.
4. **Timer'lar:** `setInterval` ile başlatılan ama `clearInterval` ile kapatılmayan timer'lar. Timer callback'i içindeki tüm referanslar GC'lenemez.
5. **Kapatılmayan stream'ler ve connection'lar:** Database connection, file stream, socket — açıp kapatmamak hem memory hem de file descriptor leak'e yol açar.

**Heap Snapshot Analizi:**
Chrome DevTools'ta heap snapshot yükleyip şunlara bakın:
- **Retained Size:** Bir obje GC'lenirse ne kadar memory geri kazanılır? Büyük retained size = potansiyel leak.
- **Comparison view:** İki snapshot arasındaki farkı görün — hangi objeler büyüyor?
- **Allocation timeline:** Zaman içinde hangi objeler allocate ediliyor ve GC'lenemiyor?

```javascript
// Heap snapshot
const v8 = require('v8');
const fs = require('fs');

function takeHeapSnapshot() {
  const snapshot = v8.writeHeapSnapshot();
  console.log('Heap snapshot written to', snapshot);
}

// Trigger on memory threshold
setInterval(() => {
  const used = process.memoryUsage().heapUsed / 1024 / 1024;
  if (used > 500) { // 500 MB
    console.log(`High memory usage: ${used} MB`);
    takeHeapSnapshot();
  }
}, 60000);

// Analyze with Chrome DevTools
// Load the snapshot and investigate
```

**Memory Leak Detection:**
```javascript
const memwatch = require('@airbnb/node-memwatch');

memwatch.on('leak', (info) => {
  console.error('Memory leak detected:', info);
  // Alert ops team
  // Take heap snapshot
});

memwatch.on('stats', (stats) => {
  console.log('GC stats:', stats);
});
```

#### Application Performance Monitoring

APM nedir? Uygulamanız için **doktor kontrolü** gibi düşünün — vital bulgularınızı (kalp atışı, tansiyon, ateş) sürekli izliyorsunuz. Uygulamanın nabzını, nefes alış hızını, ateşini ölçüyorsunuz. Bir şey anormal olduğunda alarm çalıyor. Doktor "tansiyonunuz yüksek" dediğinde sorunu erken yakalarsınız — APM de uygulamanız için aynı şeyi yapar.

**Observability'nin Üç Sütunu (Three Pillars):**
1. **Metrics (Metrikler):** Sayısal veriler. CPU kullanımı %85, request/saniye 1500, error rate %2.3. Hızlı bakışta sistemin genel sağlığını gösterir.
2. **Traces (İzler):** Bir request'in sistemdeki yolculuğu. API Gateway → Auth Service → User Service → Database → Cache. Hangi adımda ne kadar süre harcandı? Bottleneck nerede?
3. **Logs (Günlükler):** Detaylı olay kayıtları. "User 12345 login failed: invalid password". Sorunun ne olduğunu anlamak için.

Bu üçü birlikte **unified observability** sağlar. Metrik alarm verir → Trace'le hangi servisin yavaş olduğunu bulursunuz → Log'larla sorunun detayını anlarsınız.

**Key Metrics — RED ve USE Metodları:**
- **RED Method** (request-driven servisler için): **R**ate (saniyedeki istek sayısı), **E**rrors (hata oranı), **D**uration (istek süresi). Microservice'ler için ideal.
- **USE Method** (kaynak odaklı): **U**tilization (kullanım oranı), **S**aturation (doygunluk — kuyrukta bekleyen iş), **E**rrors. CPU, memory, disk için ideal.

**APM Araçları Karşılaştırması:**
- **New Relic:** All-in-one platform, güçlü auto-instrumentation, geniş dil desteği.
- **Datadog:** Infra monitoring + APM birlikte, dashboard'ları çok güçlü, ama pahalı.
- **Dynatrace:** AI-powered root cause analysis, enterprise seviyesi, kurulum karmaşık ama güçlü.
- **Grafana Cloud:** Open-source temelli (Prometheus + Tempo + Loki), maliyet avantajı, ama kendiniz kurmalısınız.

**Auto-instrumentation vs Manual:** Çoğu APM agent'ı otomatik olarak HTTP request'leri, DB query'leri, external API çağrılarını instrument edebilir — tek satır kod yazmadan! Ama custom business metric'ler ("checkout başarı oranı", "ödeme işlem süresi") için manual instrumentation gerekir.

**APM'in ROI'si:** "Bu yatırıma değer mi?" Kesinlikle evet. Yavaş bir query'yi APM ile 5 dakikada bulmak vs. log'larda saatlerce aramak — mühendislik saatini düşünün. Bir production incident'ta MTTR (Mean Time To Resolution) APM ile dramatik şekilde düşer.

**Gerçek dünya hikayesi:** "P99 latency öğleden sonra 3'te 200ms'den 2 saniyeye fırladı. APM dashboard'una baktık — trace'ler gösterdi ki yeni deploy edilen bir servis, veritabanında full table scan yapan bir query çalıştırıyordu. Index ekledik, 5 dakikada çözüldü. APM olmasaydı, bu sorunu bulmak saatler sürerdi."

```javascript
// Custom metrics
const { Histogram, Counter, Gauge } = require('prom-client');

// Track request duration
const httpRequestDuration = new Histogram({
  name: 'http_request_duration_ms',
  help: 'Duration of HTTP requests in ms',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.1, 5, 15, 50, 100, 500]
});

// Track active connections
const activeConnections = new Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});

// Track errors
const httpErrors = new Counter({
  name: 'http_errors_total',
  help: 'Total HTTP errors',
  labelNames: ['method', 'route', 'status_code']
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();
  activeConnections.inc();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    
    httpRequestDuration
      .labels(req.method, req.route.path, res.statusCode)
      .observe(duration);
    
    if (res.statusCode >= 400) {
      httpErrors
        .labels(req.method, req.route.path, res.statusCode)
        .inc();
    }
    
    activeConnections.dec();
  });
  
  next();
});
```

### Performance Optimization Techniques

#### Database Query Optimization

Query optimizasyonu neden bu kadar önemli? Şöyle bir analoji düşünün: aynı yere gitmek için **otobana** mı çıkarsınız, **şehir içi ara sokaklardan** mı gidersiniz? Varış noktası aynı ama süre çok farklı! Bir query'nin doğru yazılması ile yanlış yazılması arasındaki fark, 30 milisaniye ile 30 saniye arasındaki fark olabilir — bu 1000 kat!

**EXPLAIN ANALYZE — En Yakın Dostunuz** 🔍
Bir query'nin neden yavaş olduğunu anlamak için EXPLAIN ANALYZE kullanın. Bu komut, PostgreSQL'in query'yi çalıştırırken **gerçekte ne yaptığını** gösterir. Tahmini maliyeti değil, gerçek süreyi ve satır sayısını verir.

**EXPLAIN Çıktısını Nasıl Okumalı?**
- **Seq Scan (Sequential Scan):** Tablonun TAMAMINI satır satır tarıyor 😱. Küçük tablolarda sorun değil ama 10 milyon satırlık tabloda felaket.
- **Index Scan:** Index kullanarak doğrudan ilgili satırlara gidiyor ✅. Otobandan gitmek gibi.
- **cost:** PostgreSQL'in tahmini maliyeti (düşük = iyi).
- **actual time:** Gerçek çalışma süresi (milisaniye cinsinden).
- **rows:** Dönen satır sayısı — tahmini vs gerçek arasında büyük fark varsa, istatistikler güncel değil demek (`ANALYZE` çalıştırın).

**Index Türleri — Her Derde Bir Deva:**
- **B-tree (varsayılan):** Eşitlik ve aralık sorguları için (`=`, `<`, `>`, `BETWEEN`). Çoğu durumda bu yeterli.
- **Hash:** Sadece eşitlik sorguları için (`=`). B-tree'den biraz daha hızlı ama sınırlı kullanım.
- **GIN (Generalized Inverted Index):** Full-text search, JSONB sorguları, array'ler için mükemmel.
- **BRIN (Block Range Index):** Time-series veriler için ideal (loglar, event'ler). Çok az yer kaplar.
- **GiST (Generalized Search Tree):** Geometrik veriler, coğrafi sorgular (PostGIS), en yakın komşu aramaları.

**N+1 Query Problemi — Sessiz Katil** 🔪
Bu klasik hatayı herkes en az bir kez yapar: 100 kullanıcıyı çekiyorsunuz (1 query), sonra her kullanıcının siparişlerini ayrı ayrı çekiyorsunuz (100 query). Toplam: **101 query!** Bu, markete gidip her seferinde tek bir ürün alıp eve dönmek gibi. Çözüm: **JOIN** kullanın veya **DataLoader** pattern'ini uygulayın.

**DataLoader Pattern:** N+1'i 2 query'ye düşürür. Tüm kullanıcı ID'lerini toplar, tek bir `WHERE id IN (...)` query'si ile tüm siparişleri çeker. Facebook tarafından popülerleştirildi, GraphQL dünyasında standart.

**Connection Pool — Neden Çok Bağlantı Veritabanını Öldürür?**
Her PostgreSQL bağlantısı **yaklaşık 10MB RAM** tüketir. 100 bağlantı = 1GB RAM sadece bağlantılar için! Bağlantı sayısı arttıkça context switching maliyeti de artar. Bu yüzden **connection pooling** (PgBouncer, pgpool) kullanın. Genellikle `max_connections` değerini CPU çekirdek sayısının 2-4 katı olarak ayarlayın.

**Gerçek dünya hikayesi:** "Bir production API'miz 30 saniyede yanıt veriyordu. Kullanıcılar çıldırıyordu. EXPLAIN ANALYZE çalıştırdık — 5 milyon satırlık tabloda Seq Scan yapılıyordu. `created_at` sütununa tek bir B-tree index ekledik. Sonuç? 30 saniyeden **30 milisaniyeye** düştü. Tek bir eksik index, performansı 1000 kat kötüleştirmişti." 💡

```sql
-- Explain Analyze (PostgreSQL)
EXPLAIN ANALYZE
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '30 days'
GROUP BY u.id;

-- Look for:
-- - Seq Scan (bad for large tables)
-- - Index Scan (good)
-- - Nested Loop (can be slow)
-- - Hash Join (usually good)

-- Add index
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Partial index (for specific queries)
CREATE INDEX idx_active_users 
ON users(created_at) 
WHERE status = 'active';

-- Covering index (index-only scan)
CREATE INDEX idx_users_email_name 
ON users(email, name);

-- Now this query only touches index, not table
SELECT email, name FROM users WHERE email = 'user@example.com';
```

**Query Optimization Strategies:**
```javascript
// ❌ Bad: N+1 query
async function getUsers() {
  const users = await User.findAll();
  for (const user of users) {
    user.orders = await Order.findAll({ where: { userId: user.id } });
  }
  return users;
}

// ✅ Good: Join or eager loading
async function getUsers() {
  return await User.findAll({
    include: [{
      model: Order,
      as: 'orders'
    }]
  });
}

// ✅ Better: Dataloader (batching + caching)
const DataLoader = require('dataloader');

const orderLoader = new DataLoader(async (userIds) => {
  const orders = await Order.findAll({
    where: { userId: userIds }
  });
  
  // Group by userId
  const ordersByUser = userIds.map(id => 
    orders.filter(o => o.userId === id)
  );
  
  return ordersByUser;
});

async function getUsers() {
  const users = await User.findAll();
  return await Promise.all(
    users.map(async (user) => ({
      ...user,
      orders: await orderLoader.load(user.id)
    }))
  );
}
```

#### Caching Strategies (Advanced)

**Multi-level caching** kavramını anlamak için şu analojiyi düşünün: **masanızın çekmecesi → dosya dolabı → arşiv deposu**. Çekmeceye uzanmak 1 saniye, dolaba yürümek 30 saniye, arşiv deposuna inmek 5 dakika sürer. Verinizi ne kadar yakında tutarsanız o kadar hızlı erişirsiniz.

**L1 — In-Memory Cache (Map/LRU):**
En hızlı seviye. Process'in kendi belleğinde yaşar. Mikrosaniyeler düzeyinde erişim. Ama bazı dezavantajları var: her process'in kendi cache'i var (paylaşılmaz), process restart olunca kaybolur, bellek sınırlı. Node.js'de basit bir `Map()` veya LRU cache ile implemente edilir.

**L2 — Redis / Memcached:**
Hızlı ama L1'den biraz daha yavaş (network hop var — ~1ms). Tüm process'ler arasında **paylaşılır**, restart'larda hayatta kalır (Redis persistence ile). Tipik kullanım: session store, rate limiting, leaderboard, pub/sub.

**L3 — Database:**
En yavaş seviye ama **source of truth** (gerçeğin kaynağı). Disk I/O gerektirdiği için milisaniyeler sürer. Diğer cache katmanları sonuçta buradan beslenir.

**Cache Warming — Soğuk Başlangıcı Önle** 🔥
Uygulamanız yeni deploy edildiğinde cache boş. İlk kullanıcılar tüm istekleri doğrudan veritabanına gönderir — bu "cold start" problemi. Cache warming, trafik gelmeden ÖNCE en çok erişilen verileri cache'e yüklemektir. Bunu deploy pipeline'ınıza ekleyin: deploy → cache warm → traffic aç.

**Stale-While-Revalidate (SWR):**
Cache süresi dolduğunda kullanıcıyı **bekletmek yerine**, eski (stale) veriyi hemen servis et, arka planda cache'i yenile. Kullanıcı her zaman hızlı yanıt alır. Facebook, Twitter gibi platformlar bu stratejiyi yoğun kullanır — timeline'daki veri birkaç saniye eski olabilir ama kullanıcı bunu fark etmez.

**Cache Stampede / Thundering Herd — Sürü Paniği** 🐂
En tehlikeli cache senaryosu: popüler bir cache key'inin süresi dolar, **aynı anda 1000 request** veritabanına koşar. Veritabanı bu yükü kaldıramaz ve çöker. Çözümler:
- **Mutex/Lock:** İlk request cache'i yeniler, diğerleri bekler.
- **Probabilistic Early Expiration:** Cache süresini biraz rastgele yapın, hepsinin aynı anda dolmasını engelleyin.
- **SWR:** Stale veri servis ederken arka planda yenileyin.

**Cache Invalidation Stratejileri:**
- **TTL (Time-To-Live):** En basit. "Bu veri 5 dakika geçerli." Basit ama veri eski olabilir.
- **Event-Based:** Veri değiştiğinde event yayınla, cache'i temizle. En tutarlı ama karmaşık.
- **Write-Through:** Veriyi yazarken hem DB'ye hem cache'e yaz. Tutarlı ama yazma yavaşlar.
- **Write-Behind (Write-Back):** Önce cache'e yaz, sonra asenkron olarak DB'ye yaz. Hızlı ama veri kaybı riski var.

> *"There are only two hard things in computer science: cache invalidation and naming things."* — Phil Karlton

Bu söz yazılım dünyasının en meşhur sözlerinden biri ve kesinlikle doğru. Cache invalidation, doğru zamanda doğru veriyi temizlemek, yazılım mühendisliğinin en zor problemlerinden biridir. Çok erken temizlerseniz performans kaybedersiniz, çok geç temizlerseniz eski veri servis edersiniz.

**Gerçek dünya örneği:** Facebook'un **TAO** cache sistemi günde **milyarlarca** isteği in-memory cache'den karşılar. Sosyal grafı (arkadaşlıklar, beğeniler, yorumlar) tamamen bellekte tutar. Veritabanına giden istek oranı toplam trafiğin %1'inden az. Bu olmasa Facebook'un veritabanları saniyeler içinde çökerdi.

```javascript
// Multi-level cache with cache warming
class MultiLevelCache {
  constructor() {
    this.l1 = new Map(); // In-memory (fast)
    this.l2 = redisClient; // Redis (medium)
    // L3 would be database
  }
  
  async get(key) {
    // L1: Memory
    if (this.l1.has(key)) {
      return this.l1.get(key);
    }
    
    // L2: Redis
    const l2Value = await this.l2.get(key);
    if (l2Value) {
      this.l1.set(key, JSON.parse(l2Value));
      return JSON.parse(l2Value);
    }
    
    // L3: Database
    const dbValue = await database.get(key);
    if (dbValue) {
      // Populate caches
      this.l1.set(key, dbValue);
      await this.l2.setEx(key, 3600, JSON.stringify(dbValue));
      return dbValue;
    }
    
    return null;
  }
  
  async set(key, value, ttl = 3600) {
    this.l1.set(key, value);
    await this.l2.setEx(key, ttl, JSON.stringify(value));
  }
  
  async invalidate(key) {
    this.l1.delete(key);
    await this.l2.del(key);
  }
}

// Cache warming (prevent cold start)
async function warmCache() {
  const popularProducts = await database.query(
    'SELECT * FROM products ORDER BY view_count DESC LIMIT 100'
  );
  
  for (const product of popularProducts) {
    await cache.set(`product:${product.id}`, product);
  }
  
  console.log('Cache warmed with top products');
}

// Run at startup and periodically
warmCache();
setInterval(warmCache, 3600000); // Every hour
```

**Cache-Aside Pattern with Stale-While-Revalidate:**
```javascript
async function getWithSWR(key, fetchFn, ttl = 60) {
  const cached = await redis.get(key);
  
  if (cached) {
    const { value, expiresAt } = JSON.parse(cached);
    
    // If stale, refresh in background
    if (Date.now() > expiresAt) {
      // Return stale data immediately
      setImmediate(async () => {
        try {
          const fresh = await fetchFn();
          await redis.setEx(key, ttl * 2, JSON.stringify({
            value: fresh,
            expiresAt: Date.now() + (ttl * 1000)
          }));
        } catch (err) {
          console.error('Background refresh failed:', err);
        }
      });
    }
    
    return value;
  }
  
  // Cache miss
  const value = await fetchFn();
  await redis.setEx(key, ttl * 2, JSON.stringify({
    value,
    expiresAt: Date.now() + (ttl * 1000)
  }));
  
  return value;
}

// Usage
app.get('/products/:id', async (req, res) => {
  const product = await getWithSWR(
    `product:${req.params.id}`,
    () => Product.findById(req.params.id),
    300 // 5 minutes
  );
  res.json(product);
});
```

#### Connection Pooling Optimization

Connection pooling'i anlamanın en güzel yolu **havaalanı taksi kuyruğu** analojisidir. Düşünün: havaalanından çıktınız, taksi lazım. İki senaryo var:

**Senaryo 1 (Pool OLMADAN):** Her yolcu için şehrin öbür ucundan yeni bir taksi çağrılıyor. Taksi gelene kadar 50-100ms bekle (yani DB connection kurma süresi). Yolcu inince taksi eve gidiyor, bir daha kullanılmıyor. Saçmalık değil mi?

**Senaryo 2 (Pool İLE):** Havaalanında 20 taksilik bir kuyruk var. Yolcu çıkıyor, ilk boş taksiye biniyor. Taksi yolcuyu bırakıp geri kuyruğa dönüyor. Taksi sayısı sabit, bekleme süresi minimum. İşte connection pooling budur! 🚕

**Neden bu kadar önemli?**

Her yeni PostgreSQL bağlantısı kurmak ciddi bir maliyet:
- **TCP handshake** → 3-way handshake süresi
- **TLS negotiation** → SSL kullanıyorsanız ek süre
- **Authentication** → kullanıcı doğrulama
- **Process fork** → PostgreSQL her bağlantı için YENİ BİR PROCESS oluşturur!
- **Bellek maliyeti** → Her connection yaklaşık **~10MB RAM** tüketir

Matematik yapalım: 1000 eşzamanlı connection = **10GB RAM** sadece bağlantılar için! Daha sorgu çalıştırmadık bile. Bu, veritabanı sunucunuzun tüm RAM'ini yiyebilir.

**Pool boyutu nasıl hesaplanır?**

PostgreSQL'in yaratıcılarının önerdiği formül:

```
connections = (core_count * 2) + effective_spindle_count
```

Yani 4 çekirdekli bir sunucu + 1 SSD disk = **(4 × 2) + 1 = 9 connection**. Evet, sadece 9! Çoğu insan bunu duyunca şok olur: "Ama benim 500 kullanıcım var!" — Evet, ama o 500 kullanıcının 499'u herhangi bir anda sorgu ÇALIŞTIRMIYOR. Bekliyor. Pool sayesinde 9-20 connection ile yüzlerce kullanıcıya hizmet verebilirsiniz.

**Gerçek dünya dersi:** Bir ekip PostgreSQL'de `max_connections=5000` ayarladı. Sonuç? Sunucu sürekli OOM (Out of Memory) ile çöktü. Pool'u **200'den 20'ye** düşürdüklerinde response time **%40 iyileşti**. Daha az connection = daha az context switching = daha hızlı sorgular. Paradoks gibi ama gerçek.

**pgBouncer — Dış Connection Pooler:**

Uygulama başına pool yetmediğinde (örneğin 50 microservice, her biri 20 connection = 1000 toplam) **pgBouncer** devreye girer. Tüm uygulamaların bağlantılarını tek bir havuzda toplar ve PostgreSQL'e sadece gerçekten gereken sayıda connection açar. Üç modu var:
- **Session pooling**: bağlantı session boyunca tutulur
- **Transaction pooling**: bağlantı sadece transaction süresince tutulur (en verimli!)
- **Statement pooling**: her SQL statement için ayrı bağlantı (çok kısıtlı)

```javascript
// PostgreSQL connection pool tuning
const { Pool } = require('pg');

const pool = new Pool({
  host: 'localhost',
  database: 'mydb',
  max: 20,                    // Maximum connections
  min: 5,                     // Minimum idle connections
  idleTimeoutMillis: 30000,   // Close idle connections after 30s
  connectionTimeoutMillis: 2000, // Wait 2s for available connection
  maxUses: 7500,              // Close connection after N uses (prevents leaks)
  
  // Advanced: statement timeout
  statement_timeout: 30000,   // Kill queries > 30s
  
  // Connection lifecycle
  async onConnect(client) {
    // Set session variables
    await client.query('SET TIME ZONE "UTC"');
    await client.query('SET statement_timeout TO 30000');
  }
});

// Monitor pool
pool.on('connect', () => {
  console.log('New client connected');
});

pool.on('acquire', () => {
  console.log('Client acquired from pool');
});

pool.on('remove', () => {
  console.log('Client removed from pool');
});

// Metrics
setInterval(() => {
  console.log({
    total: pool.totalCount,
    idle: pool.idleCount,
    waiting: pool.waitingCount
  });
}, 10000);
```

**HTTP Connection Pooling:**
```javascript
const http = require('http');
const https = require('https');

// Keep-Alive agent
const httpAgent = new http.Agent({
  keepAlive: true,
  maxSockets: 50,        // Max open sockets per host
  maxFreeSockets: 10,    // Max idle sockets per host
  timeout: 60000,        // Active socket timeout
  freeSocketTimeout: 30000 // Idle socket timeout
});

const httpsAgent = new https.Agent({
  keepAlive: true,
  maxSockets: 50,
  maxFreeSockets: 10
});

// Use with fetch or axios
const axios = require('axios');
const client = axios.create({
  httpAgent,
  httpsAgent
});

// Reuse connections
await client.get('http://api.example.com/users'); // Opens connection
await client.get('http://api.example.com/posts'); // Reuses connection
```

### Load Testing & Benchmarking

```javascript
// Artillery config (artillery.yml)
const artilleryConfig = {
  config: {
    target: 'http://localhost:3000',
    phases: [
      { duration: 60, arrivalRate: 10, name: 'Warm up' },
      { duration: 300, arrivalRate: 50, name: 'Sustained load' },
      { duration: 120, arrivalRate: 100, name: 'Spike' }
    ],
    payload: {
      path: 'users.csv',
      fields: ['email', 'password']
    }
  },
  scenarios: [
    {
      name: 'User flow',
      flow: [
        { post: { url: '/login', json: { email: '{{ email }}', password: '{{ password }}' } } },
        { get: '/dashboard' },
        { get: '/products' },
        { post: { url: '/cart/add', json: { productId: '123' } } },
        { post: '/checkout' }
      ]
    }
  ]
};

// Run: artillery run artillery.yml
```

**k6 (Scripting load tests):**
```javascript
// load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

const errorRate = new Rate('errors');

export const options = {
  stages: [
    { duration: '2m', target: 100 },   // Ramp up to 100 users
    { duration: '5m', target: 100 },   // Stay at 100 users
    { duration: '2m', target: 200 },   // Spike to 200 users
    { duration: '5m', target: 200 },   // Stay at 200
    { duration: '2m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% requests < 500ms
    errors: ['rate<0.01'],             // Error rate < 1%
  },
};

export default function () {
  const payload = JSON.stringify({
    email: 'user@example.com',
    password: 'password123',
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const loginRes = http.post('http://localhost:3000/login', payload, params);
  
  check(loginRes, {
    'login successful': (r) => r.status === 200,
    'has token': (r) => r.json('token') !== undefined,
  }) || errorRate.add(1);

  const token = loginRes.json('token');

  const dashboardRes = http.get('http://localhost:3000/dashboard', {
    headers: { Authorization: `Bearer ${token}` },
  });

  check(dashboardRes, {
    'dashboard loaded': (r) => r.status === 200,
  }) || errorRate.add(1);

  sleep(1);
}

// Run: k6 run load-test.js
```

#### Worker Threads (CPU-Intensive İşler)

Node.js **single-threaded** diye bilirsiniz — bu doğru ama eksik bir bilgi. Event loop tek thread'de çalışır, ama Node.js v10.5'ten beri **Worker Threads** modülü ile ek thread'ler oluşturabilirsiniz. Peki ne zaman lazım?

Bir restoran düşünün: **Event loop = garson**, **Worker Thread = aşçı**. Garson siparişleri alır, mutfağa iletir, diğer masalara bakar. Ama garson mutfağa girip yemek pişirmeye başlarsa? Diğer müşteriler aç kalır! İşte CPU-intensive iş yapınca event loop'a olan da budur — **tüm request'ler bloklanır**.

**Ne zaman Worker Threads kullanmalı?**
- 🖼️ **Image processing:** Sharp, Jimp ile resim resize/crop — CPU-bound iş
- 🔐 **Cryptography:** bcrypt hash, PDF generation, encryption — ağır hesaplama
- 📊 **Data parsing:** Büyük CSV/JSON parse etme, XML dönüşümleri
- 🧮 **Matematiksel hesaplamalar:** ML inference, istatistik, simülasyonlar
- 🗜️ **Compression:** Büyük dosyaları sıkıştırma/açma

**Worker Threads vs Cluster vs Child Process:**

| Özellik | Worker Threads | Cluster | Child Process |
|---------|---------------|---------|---------------|
| Memory | Paylaşımlı (SharedArrayBuffer) | Ayrı (her process kendi heap'i) | Ayrı |
| İletişim | Hızlı (postMessage, SharedArrayBuffer) | IPC (daha yavaş) | IPC |
| Kullanım | CPU-intensive görevler | HTTP server scaling | External program çalıştırma |
| Overhead | Düşük | Yüksek (her biri tam process) | Yüksek |
| İzolasyon | Kısmi (crash main thread'i etkileyebilir) | Tam (bir worker crash olsa diğerleri çalışır) | Tam |

```javascript
// worker-pool.js — Production-ready Worker Thread Pool
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');
const os = require('os');

class WorkerPool {
  constructor(workerScript, poolSize = os.cpus().length) {
    this.workers = [];
    this.queue = [];
    this.activeWorkers = 0;
    this.poolSize = poolSize;
    this.workerScript = workerScript;
  }

  run(taskData) {
    return new Promise((resolve, reject) => {
      const task = { data: taskData, resolve, reject };

      if (this.activeWorkers < this.poolSize) {
        this._runTask(task);
      } else {
        this.queue.push(task); // Kuyrukta beklet
      }
    });
  }

  _runTask(task) {
    this.activeWorkers++;
    const worker = new Worker(this.workerScript, { workerData: task.data });

    worker.on('message', (result) => {
      task.resolve(result);
      this.activeWorkers--;
      this._processQueue();
    });

    worker.on('error', (err) => {
      task.reject(err);
      this.activeWorkers--;
      this._processQueue();
    });
  }

  _processQueue() {
    if (this.queue.length > 0 && this.activeWorkers < this.poolSize) {
      this._runTask(this.queue.shift());
    }
  }
}

// image-worker.js — Worker thread tarafı
if (!isMainThread) {
  const sharp = require('sharp');
  const { imagePath, width, height } = workerData;

  sharp(imagePath)
    .resize(width, height)
    .jpeg({ quality: 80 })
    .toBuffer()
    .then((buffer) => parentPort.postMessage(buffer))
    .catch((err) => { throw err; });
}

// main.js — API handler'da kullanım
const pool = new WorkerPool('./image-worker.js', 4); // 4 worker thread

app.post('/resize', async (req, res) => {
  // Bu ASLA event loop'u bloklamaz!
  const result = await pool.run({
    imagePath: req.file.path,
    width: 800,
    height: 600
  });
  res.send(result);
});
```

**SharedArrayBuffer ile Zero-Copy Data Sharing:**
```javascript
// Main thread ve Worker thread arasında memory paylaşımı
const { Worker } = require('worker_threads');

// 1MB paylaşımlı buffer oluştur
const sharedBuffer = new SharedArrayBuffer(1024 * 1024);
const sharedArray = new Int32Array(sharedBuffer);

const worker = new Worker('./compute-worker.js', {
  workerData: { sharedBuffer } // Kopyalanmaz, REFERANS geçer!
});

// Worker tarafında:
// const { sharedBuffer } = workerData;
// const arr = new Int32Array(sharedBuffer);
// Atomics.add(arr, 0, 1); // Thread-safe increment
```

**Pratik tavsiyeler:**
- Worker pool boyutunu CPU sayısı kadar tutun — daha fazlası context switching overhead yaratır
- Büyük veriyi Worker'a geçirirken `transferList` kullanın (zero-copy transfer)
- Worker'lar arası iletişim için `SharedArrayBuffer` + `Atomics` kullanın (lock-free concurrency)
- Her request için yeni Worker oluşturmayın — pool kullanın! Worker oluşturma ~30ms sürer
- Piscina veya workerpool gibi battle-tested kütüphaneler kullanmayı düşünün

---

## 🗄️ Advanced Database Architectures

### Time-Series Databases

**When to Use:**
- Metrics & monitoring data
- IoT sensor data
- Financial tick data
- Log aggregation

**TimescaleDB (PostgreSQL extension):**
```sql
-- Create hypertable (partitioned by time)
CREATE TABLE sensor_data (
  time        TIMESTAMPTZ NOT NULL,
  sensor_id   INTEGER NOT NULL,
  temperature DOUBLE PRECISION,
  humidity    DOUBLE PRECISION
);

SELECT create_hypertable('sensor_data', 'time');

-- Automatic partitioning by time
-- Optimized for time-range queries

-- Insert data
INSERT INTO sensor_data VALUES
  (NOW(), 1, 22.5, 65.3),
  (NOW(), 2, 23.1, 63.8);

-- Time-series query
SELECT 
  time_bucket('1 hour', time) AS hour,
  sensor_id,
  AVG(temperature) as avg_temp,
  MAX(temperature) as max_temp
FROM sensor_data
WHERE time > NOW() - INTERVAL '24 hours'
GROUP BY hour, sensor_id
ORDER BY hour DESC;

-- Continuous aggregates (materialized views)
CREATE MATERIALIZED VIEW sensor_data_hourly
WITH (timescaledb.continuous) AS
SELECT 
  time_bucket('1 hour', time) AS hour,
  sensor_id,
  AVG(temperature) as avg_temp,
  MIN(temperature) as min_temp,
  MAX(temperature) as max_temp
FROM sensor_data
GROUP BY hour, sensor_id;

-- Auto-refresh
SELECT add_continuous_aggregate_policy('sensor_data_hourly',
  start_offset => INTERVAL '3 hours',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');

-- Data retention policy
SELECT add_retention_policy('sensor_data', INTERVAL '90 days');
```

**InfluxDB (Purpose-built time-series):**
```javascript
const { InfluxDB, Point } = require('@influxdata/influxdb-client');

const client = new InfluxDB({ url: 'http://localhost:8086', token: 'my-token' });
const writeApi = client.getWriteApi('org', 'bucket');

// Write data
const point = new Point('temperature')
  .tag('sensor_id', 'sensor_1')
  .tag('location', 'warehouse_a')
  .floatField('value', 22.5)
  .timestamp(new Date());

writeApi.writePoint(point);
await writeApi.close();

// Query data (Flux language)
const queryApi = client.getQueryApi('org');

const query = `
  from(bucket: "sensors")
    |> range(start: -1h)
    |> filter(fn: (r) => r["_measurement"] == "temperature")
    |> filter(fn: (r) => r["sensor_id"] == "sensor_1")
    |> aggregateWindow(every: 5m, fn: mean)
`;

const result = await queryApi.collectRows(query);
console.log(result);
```

### Vector Databases (for AI/ML)

**Use Cases:**
- Semantic search
- Recommendation systems
- Image similarity
- Anomaly detection

**Pinecone:**
```javascript
const { PineconeClient } = require('@pinecone-database/pinecone');

const pinecone = new PineconeClient();
await pinecone.init({ apiKey: 'your-api-key', environment: 'us-west1-gcp' });

// Create index
await pinecone.createIndex({
  createRequest: {
    name: 'product-embeddings',
    dimension: 1536, // OpenAI embeddings
    metric: 'cosine'
  }
});

const index = pinecone.Index('product-embeddings');

// Insert vectors
await index.upsert({
  upsertRequest: {
    vectors: [
      {
        id: 'product-1',
        values: [0.1, 0.2, 0.3, ...], // 1536 dimensions
        metadata: { name: 'iPhone 15', category: 'electronics' }
      },
      {
        id: 'product-2',
        values: [0.4, 0.5, 0.6, ...],
        metadata: { name: 'MacBook Pro', category: 'computers' }
      }
    ]
  }
});

// Similarity search
const queryVector = await getEmbedding('laptop computer');

const results = await index.query({
  queryRequest: {
    vector: queryVector,
    topK: 10,
    includeMetadata: true,
    filter: { category: { '$eq': 'computers' } }
  }
});

console.log(results.matches);
// Returns most similar products
```

**pgvector (PostgreSQL extension):**
```sql
-- Enable extension
CREATE EXTENSION vector;

-- Create table with vector column
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name TEXT,
  embedding vector(1536) -- 1536 dimensions
);

-- Create index for fast similarity search
CREATE INDEX ON products USING ivfflat (embedding vector_cosine_ops);

-- Insert
INSERT INTO products (name, embedding) VALUES
  ('iPhone 15', '[0.1, 0.2, 0.3, ...]');

-- Similarity search (cosine distance)
SELECT name, 1 - (embedding <=> '[0.4, 0.5, 0.6, ...]') AS similarity
FROM products
ORDER BY embedding <=> '[0.4, 0.5, 0.6, ...]'
LIMIT 10;
```

### NewSQL Databases

**CockroachDB (Distributed SQL):**
```sql
-- Globally distributed, ACID transactions

-- Create table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email STRING UNIQUE NOT NULL,
  name STRING,
  region STRING,
  created_at TIMESTAMP DEFAULT now()
);

-- Geo-partitioning (data locality)
ALTER TABLE users PARTITION BY LIST (region) (
  PARTITION us VALUES IN ('us-east', 'us-west'),
  PARTITION eu VALUES IN ('eu-west', 'eu-central'),
  PARTITION asia VALUES IN ('ap-southeast', 'ap-northeast')
);

-- Pin partitions to specific regions
ALTER PARTITION us OF TABLE users CONFIGURE ZONE USING constraints = '[+region=us-east]';
ALTER PARTITION eu OF TABLE users CONFIGURE ZONE USING constraints = '[+region=eu-central]';

-- Distributed transaction (across multiple nodes)
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 'user-1';
  UPDATE accounts SET balance = balance + 100 WHERE id = 'user-2';
COMMIT;

-- Multi-region queries
SELECT * FROM users WHERE region = 'us-east';
-- This query runs on US nodes only
```

### Graph Databases

**Neo4j:**
```cypher
-- Create nodes and relationships
CREATE (u:User {name: 'Alice', email: 'alice@example.com'})
CREATE (p:Product {name: 'iPhone', price: 999})
CREATE (u)-[:PURCHASED {date: date()}]->(p)

-- Find friends of friends
MATCH (me:User {email: 'alice@example.com'})-[:FRIENDS_WITH]->(friend)-[:FRIENDS_WITH]->(fof)
WHERE NOT (me)-[:FRIENDS_WITH]->(fof) AND me <> fof
RETURN fof.name, COUNT(*) as mutual_friends
ORDER BY mutual_friends DESC
LIMIT 10

-- Recommendation: Products bought by similar users
MATCH (me:User {email: 'alice@example.com'})-[:PURCHASED]->(p:Product)<-[:PURCHASED]-(other:User)
MATCH (other)-[:PURCHASED]->(recommendation:Product)
WHERE NOT (me)-[:PURCHASED]->(recommendation)
RETURN recommendation.name, COUNT(*) as score
ORDER BY score DESC
LIMIT 5

-- Shortest path
MATCH path = shortestPath(
  (start:User {name: 'Alice'})-[*]-(end:User {name: 'Bob'})
)
RETURN path
```

**Use Cases:**
- Social networks
- Recommendation engines
- Fraud detection
- Knowledge graphs

---

## 🏗️ Platform Engineering

### Internal Developer Platform (IDP)

**What is IDP:**
```
Goal: Reduce cognitive load on developers
- Self-service infrastructure provisioning
- Standardized deployment pipelines
- Golden paths (opinionated best practices)
- Developer portal (service catalog)
```

**Backstage (Spotify):**
```yaml
# catalog-info.yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: order-service
  description: Order processing microservice
  annotations:
    github.com/project-slug: myorg/order-service
    pagerduty.com/integration-key: abc123
spec:
  type: service
  lifecycle: production
  owner: backend-team
  providesApis:
    - order-api
  consumesApis:
    - payment-api
    - inventory-api
  dependsOn:
    - resource:postgresql
    - resource:redis
```

**Service Template (Scaffolder):**
```yaml
# template.yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: nodejs-microservice
  title: Node.js Microservice
  description: Create a new Node.js microservice with all best practices
spec:
  owner: platform-team
  type: service
  parameters:
    - title: Service Info
      required:
        - name
        - description
      properties:
        name:
          title: Name
          type: string
        description:
          title: Description
          type: string
        owner:
          title: Owner
          type: string
          ui:field: OwnerPicker
  steps:
    - id: fetch-base
      name: Fetch Base Template
      action: fetch:template
      input:
        url: ./skeleton
        values:
          name: ${{ parameters.name }}
          description: ${{ parameters.description }}
    
    - id: create-repo
      name: Create GitHub Repository
      action: publish:github
      input:
        repoUrl: github.com?repo=${{ parameters.name }}
        description: ${{ parameters.description }}
    
    - id: create-k8s
      name: Create Kubernetes Manifests
      action: kubernetes:create
      input:
        namespace: ${{ parameters.owner }}
        manifest: ./k8s
    
    - id: register-catalog
      name: Register in Catalog
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps['create-repo'].output.repoContentsUrl }}
        catalogInfoPath: '/catalog-info.yaml'
```

### Service Mesh

**Istio Architecture:**
```
┌─────────────────────────────────────────┐
│           Control Plane (istiod)         │
│  ┌──────────┐  ┌──────────┐             │
│  │  Pilot   │  │  Citadel │             │
│  │(Traffic) │  │(Security)│             │
│  └──────────┘  └──────────┘             │
└─────────────────────────────────────────┘
              │
    ┌─────────┼─────────┐
    │         │         │
┌───▼───┐ ┌───▼───┐ ┌───▼───┐
│ Pod A │ │ Pod B │ │ Pod C │
│┌─────┐│ │┌─────┐│ │┌─────┐│
││ App ││ ││ App ││ ││ App ││
│└─────┘│ │└─────┘│ │└─────┘│
│┌─────┐│ │┌─────┐│ │┌─────┐│
││Envoy││ ││Envoy││ ││Envoy││ <- Sidecar Proxy
│└─────┘│ │└─────┘│ │└─────┘│
└───────┘ └───────┘ └───────┘
```

**Virtual Service (Traffic Management):**
```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v1
      weight: 90
    - destination:
        host: reviews
        subset: v2
      weight: 10
```

**Destination Rule (Load Balancing, Circuit Breaker):**
```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews
spec:
  host: reviews
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpHeaderName: user-id
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 10
        http2MaxRequests: 100
        maxRequestsPerConnection: 2
    outlierDetection:
      consecutiveErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

**mTLS (Mutual TLS):**
```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: prod
spec:
  mtls:
    mode: STRICT  # All traffic encrypted

---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-frontend
  namespace: prod
spec:
  selector:
    matchLabels:
      app: backend
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/prod/sa/frontend"]
    to:
    - operation:
        methods: ["GET", "POST"]
```

**Why Service Mesh:**
```
Pros:
✓ Traffic management (routing, retries, timeouts)
✓ Security (mTLS, RBAC)
✓ Observability (metrics, tracing)
✓ No application code changes

Cons:
✗ Complexity
✗ Performance overhead (sidecar)
✗ Learning curve
✗ Operational burden
```

---

## 🔭 Advanced Observability

### OpenTelemetry (Unified Observability)

**Auto-instrumentation:**
```javascript
// app.js
const opentelemetry = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const sdk = new opentelemetry.NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'order-service',
    [SemanticResourceAttributes.SERVICE_VERSION]: '1.0.0',
  }),
  traceExporter: new OTLPTraceExporter({
    url: 'http://otel-collector:4318/v1/traces',
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();

// Now all HTTP, DB, Redis calls are automatically traced!
```

**Custom Spans:**
```javascript
const { trace } = require('@opentelemetry/api');

async function processOrder(orderId) {
  const tracer = trace.getTracer('order-service');
  
  return tracer.startActiveSpan('processOrder', async (span) => {
    span.setAttribute('order.id', orderId);
    
    try {
      // Child span
      const order = await tracer.startActiveSpan('fetchOrder', async (childSpan) => {
        const result = await Order.findById(orderId);
        childSpan.setAttribute('order.total', result.total);
        childSpan.end();
        return result;
      });
      
      // Another child span
      await tracer.startActiveSpan('validateOrder', async (childSpan) => {
        await validateOrder(order);
        childSpan.end();
      });
      
      span.setStatus({ code: SpanStatusCode.OK });
      return order;
    } catch (error) {
      span.recordException(error);
      span.setStatus({
        code: SpanStatusCode.ERROR,
        message: error.message,
      });
      throw error;
    } finally {
      span.end();
    }
  });
}
```

**Context Propagation (Cross-service tracing):**
```javascript
const { propagation, context } = require('@opentelemetry/api');

// Service A
async function callServiceB(data) {
  const headers = {};
  
  // Inject trace context into headers
  propagation.inject(context.active(), headers);
  
  const response = await axios.post('http://service-b/api', data, { headers });
  return response.data;
}

// Service B (automatically extracts context)
app.use((req, res, next) => {
  // Auto-instrumentation handles this
  // But you can manually extract if needed
  const extractedContext = propagation.extract(context.active(), req.headers);
  context.with(extractedContext, next);
});
```

### eBPF-based Observability

**Pixie (Kubernetes observability without instrumentation):**
```bash
# Install Pixie
kubectl apply -f https://docs.px.dev/install/pixie.yaml

# View live requests
px live http_data

# View SQL queries
px live mysql_data

# View DNS requests
px live dns_data
```

**What eBPF Captures:**
- HTTP/HTTPS requests (without TLS decryption)
- Database queries (MySQL, PostgreSQL, Redis)
- DNS lookups
- TCP connections
- System calls

**Advantages:**
- Zero code changes
- No performance overhead
- Kernel-level visibility
- Works with any language

---

## 🌊 Streaming & Real-time Systems

### Kafka Internals

**Partitioning Strategy:**
```javascript
// Custom partitioner
class UserPartitioner {
  partition(topic, partitionCount, message) {
    const userId = message.key;
    
    // Same user always goes to same partition
    const hash = this.hashCode(userId);
    return Math.abs(hash) % partitionCount;
  }
  
  hashCode(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash = hash & hash;
    }
    return hash;
  }
}

// Producer with custom partitioner
const producer = kafka.producer({
  partitioner: Partitioners.LegacyPartitioner
});

await producer.send({
  topic: 'user-events',
  messages: [
    {
      key: 'user-123',  // Partition key
      value: JSON.stringify({ event: 'login' })
    }
  ]
});
```

**Exactly-Once Semantics:**
```javascript
// Producer (idempotent + transactional)
const producer = kafka.producer({
  idempotent: true,  // Prevents duplicates
  transactionalId: 'order-processor-1'
});

await producer.connect();

// Start transaction
const transaction = await producer.transaction();

try {
  await transaction.send({
    topic: 'orders',
    messages: [{ key: orderId, value: orderData }]
  });
  
  await transaction.send({
    topic: 'inventory',
    messages: [{ key: productId, value: inventoryUpdate }]
  });
  
  // Commit transaction
  await transaction.commit();
} catch (error) {
  await transaction.abort();
  throw error;
}
```

**Consumer Groups & Rebalancing:**
```javascript
const consumer = kafka.consumer({
  groupId: 'order-processors',
  sessionTimeout: 30000,
  heartbeatInterval: 3000,
  maxWaitTimeInMs: 100
});

await consumer.connect();
await consumer.subscribe({ topic: 'orders', fromBeginning: false });

// Rebalance listeners
consumer.on('consumer.group.rebalance', (event) => {
  console.log('Rebalance:', event);
  // Save current state before partitions are revoked
});

await consumer.run({
  partitionsConsumedConcurrently: 3,  // Process 3 partitions in parallel
  
  eachMessage: async ({ topic, partition, message }) => {
    const order = JSON.parse(message.value.toString());
    
    try {
      await processOrder(order);
      
      // Manual offset commit
      await consumer.commitOffsets([{
        topic,
        partition,
        offset: (parseInt(message.offset) + 1).toString()
      }]);
    } catch (error) {
      console.error('Processing failed:', error);
      // Don't commit offset, will retry
    }
  }
});
```

### Stream Processing Patterns

**Windowing:**
```javascript
// Tumbling window (non-overlapping)
// [0-5s] [5-10s] [10-15s]

// Sliding window (overlapping)
// [0-5s] [1-6s] [2-7s]

// Session window (activity-based)
// User active -> window extends
// User inactive for 30min -> window closes

// KsqlDB example
CREATE STREAM page_views (
  user_id VARCHAR,
  page VARCHAR,
  timestamp BIGINT
) WITH (
  KAFKA_TOPIC='page-views',
  VALUE_FORMAT='JSON'
);

-- Tumbling window: Count page views per 5 minutes
CREATE TABLE page_views_per_5min AS
SELECT 
  page,
  COUNT(*) as view_count
FROM page_views
  WINDOW TUMBLING (SIZE 5 MINUTES)
GROUP BY page;

-- Sliding window: Moving average
CREATE TABLE active_users AS
SELECT
  COUNT(DISTINCT user_id) as active_count
FROM page_views
  WINDOW HOPPING (SIZE 1 HOUR, ADVANCE BY 5 MINUTES);
```

**Stateful Processing:**
```javascript
// Flink/Kafka Streams style
const { KafkaStreams } = require('kafka-streams');

const config = {
  kafkaHost: 'localhost:9092',
  groupId: 'user-session-processor'
};

const streams = new KafkaStreams(config);

const stream = streams.getKStream('user-events');

// Stateful aggregation
stream
  .mapJSONConvenience()
  .groupBy(event => event.userId)
  .reduce((agg, event) => {
    return {
      userId: event.userId,
      totalEvents: (agg.totalEvents || 0) + 1,
      lastSeen: event.timestamp,
      events: [...(agg.events || []), event]
    };
  })
  .to('user-sessions');

streams.start().then(() => {
  console.log('Stream processing started');
});
```

---

## ☸️ Advanced Kubernetes & Cloud Native

### Custom Resource Definitions (CRDs)

**Creating Custom Resource:**
```yaml
# crd.yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.mycompany.com
spec:
  group: mycompany.com
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
                enum: [postgres, mysql]
              version:
                type: string
              storage:
                type: string
                pattern: '^[0-9]+(Gi|Mi)$'
              replicas:
                type: integer
                minimum: 1
                maximum: 5
          status:
            type: object
            properties:
              phase:
                type: string
              endpoint:
                type: string
  scope: Namespaced
  names:
    plural: databases
    singular: database
    kind: Database
    shortNames:
    - db
```

**Using Custom Resource:**
```yaml
# my-database.yaml
apiVersion: mycompany.com/v1
kind: Database
metadata:
  name: my-app-db
spec:
  engine: postgres
  version: "14"
  storage: 10Gi
  replicas: 3
```

### Kubernetes Operators

**Operator Pattern:**
```javascript
// Simple operator with Node.js
const k8s = require('@kubernetes/client-node');

const kc = new k8s.KubeConfig();
kc.loadFromDefault();

const k8sApi = kc.makeApiClient(k8s.CustomObjectsApi);
const coreApi = kc.makeApiClient(k8s.CoreV1Api);

// Watch for Database resources
async function watchDatabases() {
  const watch = new k8s.Watch(kc);
  
  await watch.watch(
    '/apis/mycompany.com/v1/databases',
    {},
    async (type, obj) => {
      console.log(`Event: ${type}`, obj.metadata.name);
      
      if (type === 'ADDED' || type === 'MODIFIED') {
        await reconcile(obj);
      } else if (type === 'DELETED') {
        await cleanup(obj);
      }
    },
    (err) => console.error('Watch error:', err)
  );
}

async function reconcile(database) {
  const name = database.metadata.name;
  const namespace = database.metadata.namespace;
  const spec = database.spec;
  
  // Create StatefulSet for database
  const statefulSet = {
    apiVersion: 'apps/v1',
    kind: 'StatefulSet',
    metadata: { name, namespace },
    spec: {
      serviceName: name,
      replicas: spec.replicas,
      selector: { matchLabels: { app: name } },
      template: {
        metadata: { labels: { app: name } },
        spec: {
          containers: [{
            name: spec.engine,
            image: `${spec.engine}:${spec.version}`,
            ports: [{ containerPort: 5432 }],
            volumeMounts: [{
              name: 'data',
              mountPath: '/var/lib/postgresql/data'
            }]
          }]
        }
      },
      volumeClaimTemplates: [{
        metadata: { name: 'data' },
        spec: {
          accessModes: ['ReadWriteOnce'],
          resources: { requests: { storage: spec.storage } }
        }
      }]
    }
  };
  
  // Apply StatefulSet
  try {
    await k8sApi.createNamespacedStatefulSet(namespace, statefulSet);
  } catch (err) {
    if (err.statusCode === 409) {
      // Already exists, update it
      await k8sApi.patchNamespacedStatefulSet(
        name,
        namespace,
        statefulSet,
        undefined,
        undefined,
        undefined,
        undefined,
        { headers: { 'Content-Type': 'application/merge-patch+json' } }
      );
    }
  }
  
  // Update status
  await updateStatus(database, 'Running', `${name}.${namespace}.svc.cluster.local`);
}

async function updateStatus(database, phase, endpoint) {
  const name = database.metadata.name;
  const namespace = database.metadata.namespace;
  
  await k8sApi.patchNamespacedCustomObjectStatus(
    'mycompany.com',
    'v1',
    namespace,
    'databases',
    name,
    { status: { phase, endpoint } },
    undefined,
    undefined,
    undefined,
    { headers: { 'Content-Type': 'application/merge-patch+json' } }
  );
}

watchDatabases();
```

**Real-world Operators:**
- Prometheus Operator
- MySQL Operator
- PostgreSQL Operator (Zalando)
- Kafka Operator (Strimzi)

### Admission Controllers

**Validating Webhook:**
```javascript
// Webhook server
const express = require('express');
const app = express();

app.use(express.json());

app.post('/validate', (req, res) => {
  const request = req.body.request;
  const object = request.object;
  
  // Validate Pod
  if (object.kind === 'Pod') {
    // Enforce resource limits
    for (const container of object.spec.containers) {
      if (!container.resources || !container.resources.limits) {
        return res.json({
          apiVersion: 'admission.k8s.io/v1',
          kind: 'AdmissionReview',
          response: {
            uid: request.uid,
            allowed: false,
            status: {
              message: 'All containers must have resource limits'
            }
          }
        });
      }
    }
  }
  
  // Allow
  res.json({
    apiVersion: 'admission.k8s.io/v1',
    kind: 'AdmissionReview',
    response: {
      uid: request.uid,
      allowed: true
    }
  });
});

app.listen(8443);
```

**Mutating Webhook (Sidecar Injection):**
```javascript
app.post('/mutate', (req, res) => {
  const request = req.body.request;
  const object = request.object;
  
  const patch = [];
  
  // Add sidecar container
  if (object.kind === 'Pod' && !hasSidecar(object)) {
    patch.push({
      op: 'add',
      path: '/spec/containers/-',
      value: {
        name: 'sidecar',
        image: 'my-sidecar:latest',
        ports: [{ containerPort: 9090 }]
      }
    });
  }
  
  // Add label
  patch.push({
    op: 'add',
    path: '/metadata/labels/injected',
    value: 'true'
  });
  
  res.json({
    apiVersion: 'admission.k8s.io/v1',
    kind: 'AdmissionReview',
    response: {
      uid: request.uid,
      allowed: true,
      patchType: 'JSONPatch',
      patch: Buffer.from(JSON.stringify(patch)).toString('base64')
    }
  });
});
```

---

## 🛡️ Security Architecture

### Zero Trust Architecture

**Principles:**
```
1. Never trust, always verify
2. Assume breach
3. Verify explicitly
4. Least privilege access
5. Microsegmentation
```

**Implementation:**
```javascript
// Service-to-service authentication with mTLS
const https = require('https');
const fs = require('fs');

// Server (requires client cert)
const server = https.createServer({
  key: fs.readFileSync('server-key.pem'),
  cert: fs.readFileSync('server-cert.pem'),
  ca: fs.readFileSync('ca-cert.pem'),
  requestCert: true,
  rejectUnauthorized: true
}, app);

// Verify client certificate
app.use((req, res, next) => {
  const cert = req.socket.getPeerCertificate();
  
  if (!cert || !cert.subject) {
    return res.status(401).json({ error: 'Client certificate required' });
  }
  
  // Extract identity from certificate
  const serviceName = cert.subject.CN;
  req.serviceIdentity = serviceName;
  
  // Check authorization
  if (!isAuthorized(serviceName, req.path, req.method)) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  
  next();
});

// Client (presents cert)
const agent = new https.Agent({
  key: fs.readFileSync('client-key.pem'),
  cert: fs.readFileSync('client-cert.pem'),
  ca: fs.readFileSync('ca-cert.pem')
});

const response = await axios.get('https://service-b:8443/api', {
  httpsAgent: agent
});
```

### Secret Management

**HashiCorp Vault:**
```javascript
const vault = require('node-vault')({
  endpoint: 'http://vault:8200',
  token: process.env.VAULT_TOKEN
});

// Store secret
await vault.write('secret/data/database', {
  data: {
    username: 'admin',
    password: 'super-secret',
    host: 'db.example.com'
  }
});

// Read secret
const result = await vault.read('secret/data/database');
const dbConfig = result.data.data;

// Dynamic secrets (auto-rotating)
const dbCreds = await vault.read('database/creds/my-role');
// Returns temporary credentials that auto-expire

// Transit encryption (encryption as a service)
const encrypted = await vault.write('transit/encrypt/my-key', {
  plaintext: Buffer.from('sensitive data').toString('base64')
});

const decrypted = await vault.write('transit/decrypt/my-key', {
  ciphertext: encrypted.data.ciphertext
});
```

**AWS Secrets Manager with Rotation:**
```javascript
const AWS = require('aws-sdk');
const secretsManager = new AWS.SecretsManager();

// Get secret
async function getSecret(secretName) {
  const data = await secretsManager.getSecretValue({ SecretId: secretName }).promise();
  return JSON.parse(data.SecretString);
}

// Rotation Lambda
exports.handler = async (event) => {
  const token = event.Token;
  const secretId = event.SecretId;
  const step = event.Step;
  
  switch (step) {
    case 'createSecret':
      // Generate new password
      const newPassword = generateSecurePassword();
      await secretsManager.putSecretValue({
        SecretId: secretId,
        ClientRequestToken: token,
        SecretString: JSON.stringify({ password: newPassword }),
        VersionStages: ['AWSPENDING']
      }).promise();
      break;
      
    case 'setSecret':
      // Update database with new password
      const pending = await getSecret(secretId, 'AWSPENDING');
      await database.query('ALTER USER app PASSWORD $1', [pending.password]);
      break;
      
    case 'testSecret':
      // Test new credentials
      const testCreds = await getSecret(secretId, 'AWSPENDING');
      await testDatabaseConnection(testCreds);
      break;
      
    case 'finishSecret':
      // Mark as current
      await secretsManager.updateSecretVersionStage({
        SecretId: secretId,
        VersionStage: 'AWSCURRENT',
        MoveToVersionId: token
      }).promise();
      break;
  }
};
```

### Security Scanning

**Container Scanning (Trivy):**
```bash
# Scan Docker image
trivy image myapp:latest

# Scan in CI/CD
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:latest

# Scan Kubernetes cluster
trivy k8s --report summary cluster

# Scan IaC (Terraform)
trivy config ./terraform
```

**SAST (Static Application Security Testing):**
```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/javascript
            p/nodejs
            p/owasp-top-ten
            
      - name: Run npm audit
        run: npm audit --audit-level=high
        
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

---

## 🤖 Machine Learning Integration

### ML Model Serving

**TensorFlow Serving:**
```javascript
// Client
const tf = require('@tensorflow/tfjs-node');
const axios = require('axios');

async function predict(inputData) {
  const response = await axios.post('http://tf-serving:8501/v1/models/my_model:predict', {
    instances: [inputData]
  });
  
  return response.data.predictions[0];
}

// Example: Image classification
const imageBuffer = fs.readFileSync('image.jpg');
const imageTensor = tf.node.decodeImage(imageBuffer);
const preprocessed = tf.image.resizeBilinear(imageTensor, [224, 224]);
const normalized = preprocessed.div(255.0);

const prediction = await predict(normalized.arraySync());
console.log('Prediction:', prediction);
```

**Custom Model Server:**
```javascript
const express = require('express');
const tf = require('@tensorflow/tfjs-node');

const app = express();
app.use(express.json());

// Load model at startup
let model;
(async () => {
  model = await tf.loadLayersModel('file://./model/model.json');
  console.log('Model loaded');
})();

// Prediction endpoint
app.post('/predict', async (req, res) => {
  const input = req.body.input;
  
  // Convert to tensor
  const inputTensor = tf.tensor2d([input]);
  
  // Predict
  const prediction = model.predict(inputTensor);
  const result = await prediction.data();
  
  // Cleanup
  inputTensor.dispose();
  prediction.dispose();
  
  res.json({ prediction: Array.from(result) });
});

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: model ? 'ready' : 'loading',
    modelLoaded: !!model
  });
});

app.listen(8080);
```

### Feature Store

Feature Store'u anlamak için şu analojiyi düşünün: **bir restoranın hazırlık mutfağı (mise en place)**. Şef yemek yaparken her seferinde soğanı soyup doğramaz — sabahtan hazırlanmış, doğranmış, ölçülmüş malzemeler tezgahta bekler. Feature Store da ML modelleri için aynı şeyi yapar: önceden hesaplanmış, tutarlı, her zaman taze "malzemeler" (features) sunar. 🧑‍🍳

**Çözdüğü problem nedir?**

Bir şirkette data scientist'ler ve ML engineer'lar var diyelim. Data scientist Jupyter notebook'ta `user_purchase_count` hesaplıyor: `SELECT COUNT(*) FROM orders WHERE user_id = ?`. ML engineer production'da aynı feature'ı hesaplıyor ama farklı bir SQL yazıyor, farklı bir zaman penceresi kullanıyor. Sonuç? **Training-Serving Skew** — model eğitilirken gördüğü veri ile production'da gördüğü veri FARKLI. Model "bu kullanıcı 50 alışveriş yapmış" diye eğitilmiş ama production'da aynı kullanıcı için "30 alışveriş" hesaplanıyor. Tahminler çöp oluyor.

Feature Store bu sorunu kökten çözer: **feature bir kez tanımlanır, her yerde aynı şekilde hesaplanır.**

**Online vs Offline Feature Serving:**

| | **Offline (Batch)** | **Online (Real-time)** |
|---|---|---|
| **Kullanım** | Model eğitimi | Canlı tahmin |
| **Latency** | Dakikalar-saatler | Milisaniyeler |
| **Storage** | Data Warehouse (BigQuery, S3) | Redis, DynamoDB |
| **Örnek** | "Son 1 yıldaki ortalama sepet tutarı" | "Son 5 dakikadaki tıklama sayısı" |

**Feature Reuse — Bir kez yaz, her yerde kullan:**

Engineering ekibi `user_purchase_count` feature'ını bir kez hesaplar. Fraud detection modeli kullanır, recommendation modeli kullanır, churn prediction modeli kullanır. Kimse aynı hesaplamayı tekrar yazmaz. Bu hem **tutarlılık** sağlar hem de **compute maliyetini** düşürür.

**Popüler Feature Store araçları:**
- **Feast** → Açık kaynak, Kubernetes-native, en yaygın
- **Tecton** → Feast'in ticari versiyonu gibi, enterprise-ready
- **AWS SageMaker Feature Store** → AWS ekosistemiyle entegre
- **Vertex AI Feature Store** → Google Cloud'un çözümü
- **Hopsworks** → Açık kaynak, tam platform

**Gerçek dünya örneği:** Uber'in **Michelangelo** platformu, sürüş fiyatlandırma ve fraud detection için **10 milyondan fazla feature** işler. Her gün milyarlarca tahmin yapılır ve her tahmin için doğru feature'ların milisaniyeler içinde servise edilmesi gerekir. Feature Store olmadan bu ölçek imkansız olurdu.

**Feast (Feature Store):**
```python
# feature_repo/features.py
from feast import Entity, Feature, FeatureView, FileSource, ValueType
from datetime import timedelta

# Entity
user = Entity(name="user_id", value_type=ValueType.INT64)

# Feature source
user_features_source = FileSource(
    path="data/user_features.parquet",
    event_timestamp_column="event_timestamp",
)

# Feature view
user_features = FeatureView(
    name="user_features",
    entities=["user_id"],
    ttl=timedelta(days=1),
    features=[
        Feature(name="age", dtype=ValueType.INT64),
        Feature(name="country", dtype=ValueType.STRING),
        Feature(name="total_purchases", dtype=ValueType.INT64),
        Feature(name="avg_purchase_value", dtype=ValueType.FLOAT),
    ],
    online=True,
    source=user_features_source,
)
```

```javascript
// Node.js client
const { FeatureStore } = require('@feast-dev/feast');

const store = new FeatureStore('./feature_repo');

// Online serving (low latency)
async function getUserFeatures(userId) {
  const features = await store.getOnlineFeatures({
    features: [
      'user_features:age',
      'user_features:country',
      'user_features:total_purchases'
    ],
    entities: { user_id: userId }
  });
  
  return features;
}

// Use in ML prediction
app.post('/recommend', async (req, res) => {
  const userId = req.user.id;
  
  // Get features from feature store
  const userFeatures = await getUserFeatures(userId);
  
  // Get model prediction
  const recommendation = await model.predict(userFeatures);
  
  res.json({ recommendation });
});
```

### A/B Testing Framework

A/B testing'i anlamanın en basit yolu: **kör tadım testi**. Gözleriniz bağlı, iki bardak kola veriyorlar — biri Pepsi, biri Coca-Cola. Hangisi daha lezzetli? Önyargısız, veriye dayalı karar. İşte A/B testing de yazılımda aynı şeyi yapar: "Hangisi daha iyi çalışıyor?" sorusuna VERİYLE cevap verir, fikirle değil. 🧪

**Neden backend'de A/B testing?**

Geleneksel yaklaşım: PM toplantıda "Checkout butonunu yeşil yapalım" der, CTO "Hayır mavi olsun" der, CEO "Kırmızı!" der. Herkes kendi fikrini savunur. A/B testing yaklaşımı: "Üçünü de yapalım, %33-%33-%34 oranında kullanıcılara gösterelim, 2 hafta sonra conversion rate'e bakalım. Veri ne diyorsa o." **HiPPO (Highest Paid Person's Opinion)** yerine DATA konuşur.

**Temel kavramlar:**
- **Control Group (A)**: Mevcut versiyon. Değişmeyen grup.
- **Treatment Group (B)**: Yeni versiyon. Test edilen değişiklik.
- **Metric**: Neyi ölçüyorsunuz? (conversion rate, revenue per user, session duration...)
- **Randomization**: Kullanıcılar rastgele gruplara atanmalı (yaş, lokasyon vs. eşit dağılmalı)

**İstatistiksel anlamlılık (Statistical Significance):**

Bu KRITIK bir kavram. 10 kullanıcıda test yapıp "B grubu %50 daha iyi!" demek HİÇBİR ŞEY ifade etmez. Neden? Çünkü 10 kişilik örneklemde şans faktörü çok yüksek. İstatistiksel olarak anlamlı sonuç için:
- **p-value < 0.05** → Sonucun şansa bağlı olma olasılığı %5'ten az
- **Sample size** → Genellikle binlerce, hatta on binlerce kullanıcı gerekir
- **Test süresi** → En az 1-2 tam hafta (hafta sonu ve hafta içi davranış farkı!)

**Feature Flags + A/B Testing = Güçlü Combo:**

Kodu deploy ediyorsunuz ama sadece kullanıcıların %10'una gösteriyorsunuz. Sorun çıkarsa anında kapatıyorsunuz. Bu ikisinin birleşimi modern product development'ın temelidir.

**Yaygın tuzaklar:**
1. **Peeking** → Sonuçlara erken bakmak. 3 gün sonra "Vay B %20 daha iyi!" deyip testi durdurmak. Sonuç: false positive.
2. **Novelty Effect** → Kullanıcılar yeniliğe ilk başta olumlu tepki verir, sonra eskiye döner. 2 hafta bekleyin.
3. **Çok fazla değişken** → A/B/C/D/E/F test etmek = hiçbir sonuç çıkmaz. Basit tutun.
4. **İstatistiksel gücü hesaplamamak** → Test için kaç kullanıcı gerektiğini ÖNCEDEN hesaplayın.

**Gerçek dünya örnekleri:**
- **Google** bir zamanlar link rengi için **41 mavi tonu** test etti. Kazanan ton yılda **$200M ek gelir** getirdi.
- **Amazon** her küçük değişikliği test eder. Sayfa yükleme süresindeki her 100ms gecikme = **%1 satış kaybı**.
- **Netflix** thumbnail görsellerini A/B test eder — doğru görsel, izlenme oranını **%20-30** artırabilir.

```javascript
class ABTestFramework {
  constructor(redis, analytics) {
    this.redis = redis;
    this.analytics = analytics;
  }
  
  // Assign user to variant
  async assignVariant(userId, experimentId) {
    // Check if already assigned
    const assigned = await this.redis.hGet(`experiment:${experimentId}`, userId);
    if (assigned) return assigned;
    
    // Get experiment config
    const config = await this.getExperimentConfig(experimentId);
    
    // Determine variant based on user hash
    const hash = this.hashUser(userId);
    const rand = hash % 100;
    
    let cumulative = 0;
    let variant = 'control';
    
    for (const [variantName, percentage] of Object.entries(config.variants)) {
      cumulative += percentage;
      if (rand < cumulative) {
        variant = variantName;
        break;
      }
    }
    
    // Store assignment
    await this.redis.hSet(`experiment:${experimentId}`, userId, variant);
    
    // Track assignment
    await this.analytics.track('experiment_assigned', {
      userId,
      experimentId,
      variant
    });
    
    return variant;
  }
  
  // Track conversion
  async trackConversion(userId, experimentId, metricName, value = 1) {
    const variant = await this.assignVariant(userId, experimentId);
    
    // Increment metric
    await this.redis.hIncrBy(
      `experiment:${experimentId}:metrics:${metricName}`,
      variant,
      value
    );
    
    await this.analytics.track('conversion', {
      userId,
      experimentId,
      variant,
      metric: metricName,
      value
    });
  }
  
  // Get results
  async getResults(experimentId) {
    const config = await this.getExperimentConfig(experimentId);
    const results = {};
    
    for (const variantName of Object.keys(config.variants)) {
      const users = await this.redis.hLen(`experiment:${experimentId}`);
      const conversions = await this.redis.hGet(
        `experiment:${experimentId}:metrics:purchase`,
        variantName
      );
      
      results[variantName] = {
        users,
        conversions: parseInt(conversions || 0),
        conversionRate: conversions / users
      };
    }
    
    // Statistical significance (simplified)
    const pValue = this.calculatePValue(results.control, results.treatment);
    
    return {
      results,
      significant: pValue < 0.05,
      pValue
    };
  }
  
  hashUser(userId) {
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = ((hash << 5) - hash) + userId.charCodeAt(i);
      hash = hash & hash;
    }
    return Math.abs(hash);
  }
}

// Usage
const abTest = new ABTestFramework(redis, analytics);

app.get('/homepage', async (req, res) => {
  const variant = await abTest.assignVariant(req.user.id, 'homepage_redesign');
  
  if (variant === 'treatment') {
    res.render('homepage_new');
  } else {
    res.render('homepage_old');
  }
});

app.post('/purchase', async (req, res) => {
  // Track conversion
  await abTest.trackConversion(req.user.id, 'homepage_redesign', 'purchase', req.body.amount);
  
  // ... process purchase
  res.json({ success: true });
});

// Admin: Get experiment results
app.get('/admin/experiments/:id', async (req, res) => {
  const results = await abTest.getResults(req.params.id);
  res.json(results);
});
```

---

## 📜 Compliance & Regulations

### GDPR Compliance

GDPR (General Data Protection Regulation), Avrupa Birliği'nin **Mayıs 2018**'den beri yürürlükte olan veri koruma yasasıdır. "Ben backend developer'ım, hukuk beni ilgilendirmez" mi diyorsunuz? Tekrar düşünün: GDPR ihlallerinde cezalar **€20 milyon** veya **küresel yıllık cironun %4'ü** (hangisi BÜYÜKSE o!) kadar olabilir. Evet, şirketiniz yılda $1 milyar kazanıyorsa ceza $40 milyon olabilir. Bu artık sadece hukukçuların değil, **her backend developer'ın** meselesidir. ⚖️

**Gerçek cezalar — bunlar şaka değil:**
- **Amazon** → €746 milyon (2021)
- **Meta/Facebook** → €1.2 milyar (2023, veri transferi ihlali)
- **Google** → €50 milyon (2019, şeffaflık eksikliği)
- **H&M** → €35 milyon (çalışan verilerini izinsiz işleme)

**GDPR'ın temel ilkeleri:**
1. **Lawfulness (Yasallık)**: Veriyi işlemek için yasal bir dayanağınız olmalı (consent, contract, legitimate interest...)
2. **Purpose Limitation (Amaç Sınırlaması)**: Veriyi topladığınız amaç dışında kullanamazsınız. "Sipariş teslimatı" için aldığınız adresi "reklam" için kullanamazsınız.
3. **Data Minimization (Veri Minimizasyonu)**: Sadece GEREKLİ veriyi toplayın. Bir blog sitesine kayıt için doğum tarihi, kan grubu, anne kızlık soyadı istemek → GDPR ihlali.
4. **Storage Limitation (Saklama Sınırlaması)**: Veriyi sonsuza kadar saklayamazsınız. Amacınız sona erince veri silinmeli.

**Data Subject Rights — Kullanıcı hakları (sade dille):**

| Hak | Ne Demek? | Backend'de Ne Yapmalı? |
|---|---|---|
| **Right to Access** | "Bende ne veriniz var, HEPSİNİ gösterin" | Tüm tabloları tarayıp kullanıcıya ait veriyi JSON olarak export et |
| **Right to Erasure** | "TÜM verilerimi SİLİN" (unutulma hakkı) | Soft delete yetmez! Hard delete veya anonymization gerekebilir |
| **Right to Portability** | "Verilerimi makine tarafından okunabilir formatta VERİN" | JSON/CSV export endpoint'i |
| **Right to Rectification** | "Yanlış verimi DÜZELTİN" | Kullanıcının kendi verisini güncelleyebileceği endpoint |
| **Right to Restrict Processing** | "Verimi saklayın ama KULLANMAYIN" | İşleme flag'i ekle, sorgularda filtrele |
| **Right to Object** | "Verimi pazarlama için KULLANMAYIN" | Opt-out mekanizması |

**Consent (Onay) — Pre-checked checkbox YASADIŞI:**

Onay şu özellikleri taşımalı:
- **Freely given**: "Onay vermezsen hizmet alamazsın" → geçersiz onay
- **Specific**: "Tüm verilerinizi her amaçla kullanabiliriz" → geçersiz (her amaç için ayrı onay)
- **Informed**: Kullanıcı neye onay verdiğini açıkça bilmeli
- **Unambiguous**: Önceden işaretlenmiş checkbox → **YASADIŞI**. Kullanıcı aktif olarak tıklamalı.

**Data Processor vs Data Controller:**
- **Controller**: Verinin neden ve nasıl işleneceğine karar veren taraf (genellikle siz)
- **Processor**: Controller adına veriyi işleyen taraf (cloud provider, analytics hizmeti)
- Birçok şirket **ikisi birden** — hem kendi müşteri verisinin controller'ı hem de müşterilerinin verisi için processor

**Privacy by Design — Sonradan ekleme değil, tasarımdan itibaren:**

GDPR açıkça "Privacy by Design" ilkesini zorunlu kılar. Yani sistemi kurarken güvenliği ve gizliliği EN BAŞTAN düşünmelisiniz:
- Encryption at rest ve in transit
- Veri erişim logları (kim, ne zaman, hangi veriye erişti?)
- Otomatik veri silme (retention policy)
- Anonymization/pseudonymization
- Least privilege access

**Data Subject Rights:**
```javascript
// Right to Access
app.get('/api/users/me/data', authenticate, async (req, res) => {
  const userId = req.user.id;
  
  // Collect all user data
  const userData = {
    profile: await User.findById(userId),
    orders: await Order.findAll({ where: { userId } }),
    pageViews: await Analytics.findAll({ where: { userId } }),
    emails: await EmailLog.findAll({ where: { userId } })
  };
  
  // Return as downloadable JSON
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Content-Disposition', 'attachment; filename=my-data.json');
  res.json(userData);
});

// Right to Erasure (Right to be Forgotten)
app.delete('/api/users/me', authenticate, async (req, res) => {
  const userId = req.user.id;
  
  // Anonymize or delete data
  await db.transaction(async (t) => {
    // Delete personal data
    await User.update({
      name: 'Deleted User',
      email: `deleted-${userId}@example.com`,
      phone: null,
      address: null,
      deleted: true,
      deletedAt: new Date()
    }, { where: { id: userId }, transaction: t });
    
    // Keep order history but anonymize
    await Order.update({
      userName: 'Deleted User',
      userEmail: null,
      shippingAddress: null
    }, { where: { userId }, transaction: t });
    
    // Delete from third-party services
    await analyticsService.deleteUser(userId);
    await emailService.deleteUser(userId);
  });
  
  res.json({ message: 'Account deleted' });
});

// Right to Data Portability
app.get('/api/users/me/export', authenticate, async (req, res) => {
  const userId = req.user.id;
  
  // Export in machine-readable format (JSON, CSV, XML)
  const data = await exportUserData(userId);
  
  res.json(data);
});
```

**Consent Management:**
```javascript
class ConsentManager {
  async recordConsent(userId, purpose, granted) {
    await Consent.create({
      userId,
      purpose,  // marketing, analytics, personalization
      granted,
      grantedAt: new Date(),
      ipAddress: req.ip,
      userAgent: req.headers['user-agent']
    });
  }
  
  async checkConsent(userId, purpose) {
    const consent = await Consent.findOne({
      where: { userId, purpose },
      order: [['grantedAt', 'DESC']]
    });
    
    return consent?.granted || false;
  }
  
  async withdrawConsent(userId, purpose) {
    await this.recordConsent(userId, purpose, false);
    
    // Stop processing for this purpose
    if (purpose === 'marketing') {
      await emailService.unsubscribe(userId);
    }
    if (purpose === 'analytics') {
      await analytics.optOut(userId);
    }
  }
}

// Middleware
async function requireConsent(purpose) {
  return async (req, res, next) => {
    const hasConsent = await consentManager.checkConsent(req.user.id, purpose);
    
    if (!hasConsent) {
      return res.status(403).json({
        error: 'Consent required',
        purpose
      });
    }
    
    next();
  };
}

// Usage
app.post('/api/newsletter/subscribe', 
  authenticate, 
  requireConsent('marketing'), 
  subscribeHandler
);
```

**Data Retention:**
```javascript
// Automatic data deletion based on retention policy
class DataRetentionService {
  constructor() {
    this.policies = {
      logs: 90,           // days
      analytics: 365,
      backups: 30,
      tempFiles: 7
    };
  }
  
  async enforceRetention() {
    for (const [type, days] of Object.entries(this.policies)) {
      const cutoffDate = new Date();
      cutoffDate.setDate(cutoffDate.getDate() - days);
      
      switch (type) {
        case 'logs':
          await Log.destroy({ where: { createdAt: { [Op.lt]: cutoffDate } } });
          break;
        case 'analytics':
          await Analytics.destroy({ where: { createdAt: { [Op.lt]: cutoffDate } } });
          break;
        case 'backups':
          await deleteOldBackups(cutoffDate);
          break;
      }
      
      console.log(`Deleted ${type} older than ${days} days`);
    }
  }
  
  // Run daily
  start() {
    setInterval(() => this.enforceRetention(), 24 * 60 * 60 * 1000);
  }
}
```

### SOC 2 Compliance

**Audit Logging:**
```javascript
class AuditLogger {
  async log(event) {
    await AuditLog.create({
      eventType: event.type,
      userId: event.userId,
      resource: event.resource,
      action: event.action,
      changes: event.changes,
      ipAddress: event.ipAddress,
      userAgent: event.userAgent,
      timestamp: new Date(),
      success: event.success,
      errorMessage: event.error
    });
  }
}

// Middleware
app.use(async (req, res, next) => {
  const start = Date.now();
  
  res.on('finish', async () => {
    await auditLogger.log({
      type: 'http_request',
      userId: req.user?.id,
      resource: req.path,
      action: req.method,
      ipAddress: req.ip,
      userAgent: req.headers['user-agent'],
      success: res.statusCode < 400,
      duration: Date.now() - start
    });
  });
  
  next();
});

// Track data changes
async function updateUser(userId, updates) {
  const oldUser = await User.findById(userId);
  const newUser = await User.update(userId, updates);
  
  await auditLogger.log({
    type: 'data_modification',
    userId: req.user.id,
    resource: `users/${userId}`,
    action: 'UPDATE',
    changes: {
      before: oldUser,
      after: newUser
    },
    success: true
  });
}
```

**Access Control Audit:**
```javascript
// Log all permission checks
function can(user, action, resource) {
  const allowed = checkPermission(user, action, resource);
  
  auditLogger.log({
    type: 'access_control',
    userId: user.id,
    resource,
    action,
    success: allowed,
    errorMessage: allowed ? null : 'Permission denied'
  });
  
  return allowed;
}
```

---

## 🎤 Technical Leadership & Influence

### Technical Writing

**RFCs (Request for Comments):**
```markdown
# RFC-001: Migrate to Microservices Architecture

## Metadata
- Author: Your Name
- Date: 2024-04-13
- Status: Proposed
- Reviewers: Team Leads, Architects

## Summary
Migrate monolithic application to microservices architecture to improve scalability and development velocity.

## Background
Current monolith has 500K LOC, 20 developers, deployment takes 2 hours, scaling is all-or-nothing.

## Motivation
- Independent deployment per service
- Technology diversity
- Team autonomy
- Granular scaling

## Proposal

### Phase 1: Identify Bounded Contexts (Month 1-2)
- Domain-driven design workshops
- Service boundaries definition
- API contracts

### Phase 2: Strangler Fig Pattern (Month 3-12)
- Extract services one by one
- Start with user-service
- Each service has own database

### Architecture Diagram
[Insert diagram]

### Technology Stack
- Node.js for services
- PostgreSQL per service
- Kafka for async communication
- Kubernetes for orchestration

## Implementation Plan

### Q1 2024
- [ ] Setup infrastructure (Kubernetes, Kafka)
- [ ] Extract user-service
- [ ] Setup monitoring

### Q2 2024
- [ ] Extract order-service
- [ ] Extract payment-service

## Trade-offs

### Pros
- Independent deployment
- Better fault isolation
- Technology flexibility

### Cons
- Operational complexity
- Distributed tracing needed
- Data consistency challenges

## Alternatives Considered

### 1. Keep Monolith, Optimize
- Pros: Simpler
- Cons: Doesn't solve scaling/deployment issues

### 2. Modular Monolith
- Pros: Middle ground
- Cons: Still all-or-nothing deployment

## Success Metrics
- Deployment time: < 15 minutes (currently 2 hours)
- Deployment frequency: 10+ per day (currently weekly)
- Time to onboard new dev: < 1 week (currently 1 month)

## Open Questions
1. How to handle distributed transactions?
2. Database per service or shared?
3. API gateway vs direct service calls?

## References
- [Microservices.io patterns](https://microservices.io/)
- [Building Microservices - Sam Newman]
```

### Technical Talks

**Conference Proposal Example:**
```markdown
# Talk Proposal: Zero to Production: Building Resilient Microservices

## Format
45-minute technical talk

## Audience Level
Intermediate to Advanced

## Abstract (150 words)
Learn how we scaled from a monolith to 50+ microservices serving 10M users. This talk covers practical patterns for building resilient distributed systems: circuit breakers, retries, timeouts, and graceful degradation. We'll dive into real production incidents and the lessons learned. You'll leave with actionable patterns you can apply immediately.

## Outline
1. Our journey (5 min)
2. Resilience patterns (25 min)
   - Circuit breakers in practice
   - Retry strategies (exponential backoff, jitter)
   - Timeout propagation
   - Bulkheads & rate limiting
3. Production war stories (10 min)
   - Cascade failure incident
   - How we recovered
   - Prevention going forward
4. Q&A (5 min)

## Takeaways
- Implement circuit breakers
- Design for failure
- Observability is key
- Test failure scenarios

## Speaker Bio
Backend Engineer at [Company]. Built distributed systems serving 10M users. Open source contributor. Previously at [Company].
```

### Mentorship Program

**Mentorship Framework:**
```javascript
// Mentorship tracking
class MentorshipProgram {
  async createPair(mentorId, menteeId) {
    const pair = await MentorshipPair.create({
      mentorId,
      menteeId,
      startDate: new Date(),
      goals: [],
      status: 'active'
    });
    
    // Schedule first meeting
    await this.scheduleMeeting(pair.id);
    
    return pair;
  }
  
  async setGoals(pairId, goals) {
    await MentorshipPair.update({
      goals: goals.map(g => ({
        description: g,
        completed: false,
        targetDate: addMonths(new Date(), 3)
      }))
    }, { where: { id: pairId } });
  }
  
  async trackProgress(pairId, updates) {
    await MeetingLog.create({
      pairId,
      date: new Date(),
      topics: updates.topics,
      progress: updates.progress,
      nextSteps: updates.nextSteps
    });
  }
}

// Mentorship goals template
const mentoringGoals = {
  technical: [
    'Learn Kubernetes fundamentals',
    'Contribute to open source',
    'Design first system from scratch',
    'Present tech talk internally'
  ],
  soft_skills: [
    'Lead code reviews',
    'Write technical documentation',
    'Mentor junior developer',
    'Present at team meeting'
  ],
  career: [
    'Define senior engineer path',
    'Build technical portfolio',
    'Expand network'
  ]
};
```

---

## 🌟 Open Source & Community

### Contributing to Open Source

**Finding Projects:**
```
1. Projects you use daily
   - Check GitHub issues labeled "good first issue"
   - Fix bugs you've encountered
   
2. awesome-* lists
   - awesome-nodejs
   - awesome-microservices
   
3. First Timers Only
   - firsttimersonly.com
```

**Making Good PRs:**
```markdown
# Pull Request Template

## Description
Brief description of changes and why

Fixes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing performed

## Screenshots (if applicable)

## Checklist
- [ ] Code follows project style guide
- [ ] Self-reviewed code
- [ ] Commented complex logic
- [ ] Updated documentation
- [ ] No console.log or debug code
```

### Building in Public

**Technical Blog Topics:**
```
1. Problem-solution posts
   - "How we reduced API latency by 80%"
   - "Debugging a production memory leak"
   
2. Tutorial/Guide
   - "Building a rate limiter from scratch"
   - "Kubernetes for backend developers"
   
3. Architecture deep-dives
   - "Our microservices journey"
   - "Event-driven architecture lessons learned"
   
4. Tool comparisons
   - "PostgreSQL vs MongoDB: When to use each"
   - "REST vs GraphQL vs gRPC"
```

**Content Structure:**
```markdown
# Title: How We Reduced API Latency by 80%

## The Problem
Our API p95 latency was 2.5 seconds, users complaining

## Investigation
[Show profiling screenshots, metrics]

## Root Cause
1. N+1 queries (found via Datadog APM)
2. Missing database indexes
3. Synchronous external API calls

## Solutions
### 1. Fixed N+1 queries
[Show before/after code]

### 2. Added indexes
[Show EXPLAIN ANALYZE output]

### 3. Async external calls
[Show implementation]

## Results
- p95 latency: 2.5s -> 450ms (82% improvement)
- Throughput: 100 req/s -> 500 req/s

## Lessons Learned
- Always profile before optimizing
- Database indexes matter
- Monitor performance continuously

## Code
[Link to GitHub]
```

---

## 🚀 Career Development

### Staff Engineer Path

**Scope Levels:**
```
Junior:     Task (individual features)
Mid:        Features (small projects)
Senior:     Projects (cross-team initiatives)
Staff:      Organization (company-wide impact)
Principal:  Industry (external influence)
```

**Staff Engineer Archetypes:**
```
1. Tech Lead
   - Deep in implementation
   - Guides team technically
   - Owns critical projects

2. Architect
   - System design & standards
   - Cross-team coordination
   - Long-term vision

3. Solver
   - Tackles hardest problems
   - Moves between teams
   - Unblocks others

4. Right Hand
   - Extends executive reach
   - Strategic initiatives
   - Organizational problems
```

### Building Your Brand

**Technical Portfolio:**
```
1. GitHub
   - Open source contributions
   - Personal projects
   - Code quality

2. Blog
   - Technical deep-dives
   - Lessons learned
   - Tutorials

3. Speaking
   - Internal tech talks
   - Meetups
   - Conferences

4. Writing
   - Documentation
   - RFCs
   - Technical specs

5. Mentoring
   - Code reviews
   - Pair programming
   - Career guidance
```

### Staying Current

**Learning Strategy:**
```
Daily (30 min):
- Hacker News / r/programming
- Tech Twitter
- Newsletter (ByteByteGo, Pointer)

Weekly (2 hours):
- Deep dive one topic
- Read 1 blog post deeply
- Try one new tool/library

Monthly (4 hours):
- Start/continue side project
- Read papers (papers.we.love)
- Contribute to open source

Quarterly:
- Attend conference/meetup
- Review learning goals
- Update resume/portfolio
```

**Resources:**
```
Papers:
- Google: MapReduce, BigTable, Spanner
- Amazon: Dynamo
- Facebook: TAO, Memcache@FB

Books:
- Designing Data-Intensive Applications
- Site Reliability Engineering
- The Staff Engineer's Path

Courses:
- MIT Distributed Systems
- Stanford CS244b
- CMU Database Systems
```

---

## 💥 Chaos Engineering & Resilience

### Neden Chaos Engineering? 

```
"Everything fails, all the time." — Werner Vogels (Amazon CTO)

Chaos Engineering TESTİN ÖTESİNDEDİR:
  → Unit test: "Bu fonksiyon doğru çalışıyor mu?"
  → Integration test: "Bu servisler birlikte doğru çalışıyor mu?"
  → Chaos test: "Bu sistem KIRILDIĞINDA ne oluyor?"

Production'da MUTLAKA bir şeyler KIRILACAK:
  → Network partition
  → Disk doluluğu
  → CPU spike
  → Memory leak
  → DNS failure
  → Bir microservice'in tamamen ölmesi

Soru: "Ne zaman kırılır?" değil → "Kırıldığında NE OLUR?"
```

### Chaos Engineering Prensipleri

```
1. Steady State Tanımla
   → "Normal" nedir? (QPS, latency P99, error rate)
   → Baseline olmadan chaos ANLAMLI DEĞİL

2. Hipotez Kur
   → "Redis öldüğünde sisteim gracefully degrade olacak"
   → "DB failover'da max 30 sn kesinti olacak"

3. Blast Radius'u SINIRLA
   → İlk deneyleri staging'de yap
   → Production'da: canary seti üzerinde
   → ABORT mekanizması her zaman hazır olsun

4. Otomatikleştir
   → Manuel chaos = bir kere yapılır ve unutulur
   → Otomatik chaos = SÜREKLİ güven
```

### Chaos Engineering Araçları

Chaos engineering araçlarını anlamak için şu analojiyi düşünün: **yangın tatbikatı**. Gerçek yangını BEKLEMEZSİNİZ tepkinizi test etmek için — önceden, kontrollü bir ortamda prova yaparsınız. İtfaiye nasıl gelecek? Merdiven çıkışları yeterli mi? İnsanlar panik yapıyor mu? Chaos engineering araçları da sisteminize "kontrollü yangın" çıkarır ve tepkisini gözlemler. 🔥

**Popüler araçların karşılaştırması:**

| Araç | Tür | Güçlü Yanı | Zayıf Yanı |
|---|---|---|---|
| **LitmusChaos** | K8s-native, CNCF projesi | Kubernetes ile mükemmel entegrasyon, ChaosHub marketplace | Sadece K8s, öğrenme eğrisi |
| **Gremlin** | SaaS | Kullanımı çok kolay, enterprise-ready, güzel UI | Ücretli, vendor lock-in |
| **Chaos Monkey** | Netflix OSS | OG chaos aracı, basit ve etkili | Sadece instance terminate eder, sınırlı |
| **Chaos Mesh** | K8s-native | Çok güçlü, detaylı kontrol, CNCF sandbox | Karmaşık konfigürasyon |
| **Toxiproxy** | Network proxy | Network chaos'ta uzman (latency, timeout, reset) | Sadece network seviyesi |

**Kademeli yaklaşım — küçükten büyüğe:**

Chaos engineering'e ASLA "production'daki tüm pod'ları öldürelim" diye başlamayın. Kademeli olarak ilerleyin:

1. **Pod Kill** → Tek bir pod'u öldürün. Yenisi başlıyor mu? Trafik diğer pod'lara yönleniyor mu?
2. **Network Latency** → 500ms gecikme ekleyin. Timeout'lar doğru çalışıyor mu? Circuit breaker devreye giriyor mu?
3. **Disk Fill** → Diski doldurun. Loglar yazılamayınca ne oluyor? Alerting çalışıyor mu?
4. **Node Failure** → Bir node'u kapatın. Pod'lar başka node'lara schedule ediliyor mu?
5. **Zone/Region Failure** → Tüm bir availability zone'u devre dışı bırakın. Multi-AZ gerçekten çalışıyor mu?

**⚠️ Production'da chaos ASLA şunlar olmadan yapılmaz:**

1. **Monitoring/Alerting hazır olmalı** → Chaos deneyi sırasında metrikleri izleyemiyorsanız, kör uçuş yapıyorsunuz demektir
2. **Abort butonu hazır olmalı** → İşler sarpa sararsa deneyi ANİDEN durdurabilmelisiniz (kill switch)
3. **Stakeholder'lar bilgilendirilmeli** → Gecenin 3'ünde on-call mühendis "Neden her şey çöküyor?!" diye panik yapmamalı
4. **Blast radius sınırlı olmalı** → Deney sadece BELİRLİ pod/service/namespace'i etkilemeli, tüm sistemi değil

**Gerçek dünya:** Netflix'in **"Chaos Kong"** deneyi efsanedir. Tüm bir **AWS REGION'ını** (mesela us-east-1) kapatarak sistemin başka region'a otomatik failover yapıp yapmadığını test ederler. Düşünün: milyonlarca kullanıcıya hizmet veren bir platform, bilinçli olarak bir bölgeyi kapatıyor. Bu cesaret, yıllarca küçük chaos deneylerinden elde edilen güvenle gelir.

**Toxiproxy özel notu:** Shopify tarafından geliştirilen bu araç, network seviyesinde chaos üretmek için harikadır. Servisleriniz arasına proxy olarak oturur ve kontrollü olarak latency ekler, bağlantıları kopartır, bandwidth'i kısar. Unit test'lerinizde bile kullanabilirsiniz — "Redis 2 saniye geç cevap verirse ne olur?" sorusunu test ortamında cevaplayabilirsiniz.

```javascript
// Kubernetes'te Chaos — LitmusChaos örneği
const chaosExperiments = {
  // Pod Kill — En temel chaos deneyi
  podKill: {
    kind: 'ChaosExperiment',
    spec: {
      definition: {
        scope: 'Namespaced',
        permissions: [{ apiGroups: [''], resources: ['pods'], verbs: ['delete'] }],
        env: [
          { name: 'TOTAL_CHAOS_DURATION', value: '30' },
          { name: 'CHAOS_INTERVAL', value: '10' },
          { name: 'FORCE', value: 'false' },
        ],
      },
    },
  },

  // Network Latency — Ağ gecikmesi enjekte et
  networkLatency: {
    spec: {
      definition: {
        env: [
          { name: 'NETWORK_INTERFACE', value: 'eth0' },
          { name: 'NETWORK_LATENCY', value: '2000' }, // 2 saniye gecikme!
          { name: 'JITTER', value: '500' },
        ],
      },
    },
  },

  // CPU Stress — CPU'yu zorlama
  cpuStress: {
    spec: {
      definition: {
        env: [
          { name: 'CPU_CORES', value: '2' },
          { name: 'CPU_LOAD', value: '80' }, // %80 CPU kullanımı
          { name: 'TOTAL_CHAOS_DURATION', value: '60' },
        ],
      },
    },
  },
};
```

### Game Day Protokolü 🎮

```
GAME DAY PLANI (Netflix/Amazon/Google'dan esinlenildi):

  HAZIRLIK (1 hafta önce):
    □ Deney hipotezini yaz
    □ Steady state metriklerini belirle
    □ Abort planı hazırla
    □ İlgili ekipleri bilgilendir
    □ On-call sırasında YAPMA!

  UYGULAMA (Game Day):
    □ Steady state'i doğrula — baseline al
    □ Blast radius'u confirm et — sadece hedef servis
    □ Deneyi başlat — parmak ABORT butonunda
    □ Metrikleri izle — dashboard'lar açık
    □ Unexpected behavior varsa → HEMEN ABORT
    □ Sonuçları kaydet

  ANALIZ (sonra):
    □ Hipotez doğrulandı mı?
    □ Hangi alarm/alert çalıştı?
    □ MTTR (Mean Time To Recovery) ne kadar?
    □ Action item'ları belirle
    □ Postmortem yaz (blameless!)
```

### Resilience Patterns

Dağıtık sistemlerde bir şeyi garanti edebilirsiniz: **Bir şeyler MUTLAKA bozulacak.** Network kopacak, disk dolacak, bir servis cevap vermeyecek, bir dependency timeout'a düşecek. Soru "bozulacak mı?" değil, "bozulduğunda ne olacak?" — ve doğru cevap **graceful degradation** olmalı, total meltdown değil.

Bu pattern'leri bir **gemi** analojisiyle açıklayalım:

**Bulkhead (Bölme Duvarı):** Gemilerin gövdesi neden bölmelere ayrılır? Çünkü bir bölme su alırsa, sadece o bölme dolar — gemi batmaz! Yazılımda Bulkhead = **izolasyon**. Payment servisine giden istekler için ayrı bir connection pool, notification servisine giden istekler için ayrı bir pool. Payment servisi çökse bile, notification servisi etkilenmez. `pLimit(10)` ile concurrent request sayısını sınırlarsınız — bir servisin tüm kaynaklarınızı tüketmesini engellersiniz.

**Circuit Breaker (Devre Kesici):** Evinizdeki sigorta gibi! Aşırı akım geldiğinde sigorta atar ve elektriği keser — kablolar yanmasın diye. Yazılımda: bir servis sürekli hata veriyorsa (%50 hata oranı), Circuit Breaker devreyi **açar** ve o servise istek göndermeyi DURDURUR. Neden? Çünkü zaten çalışmayan bir servise istek göndermek:
  1. Timeout'a düşer → kullanıcı bekler
  2. Thread/connection havuzunu doldurur → diğer servisler de etkilenir (**cascading failure**)
  3. Bozuk servise daha fazla yük biner → recovery'si daha da zorlaşır

Circuit Breaker'ın üç state'i vardır:
- **CLOSED (Normal):** İstekler geçer. Hatalar sayılır.
- **OPEN (Devre açık):** İstekler BLOKLANIR. Fallback çalışır (cache'ten veri, default değer, vs.)
- **HALF-OPEN (Test):** resetTimeout sonrası birkaç istek denenir. Başarılıysa CLOSED'a döner, değilse OPEN kalır.

**Retry with Exponential Backoff + Jitter:** "İlk denemede olmadı, bir daha dene" — ama NASIL denediğin önemli! 
- **Sabit aralıkla retry:** 100 client aynı anda 1 saniye sonra tekrar dener → **thundering herd** — sunucu yine çöker!
- **Exponential backoff:** 1s, 2s, 4s, 8s... giderek artan bekleme süresi
- **+ Jitter (rastgele gecikme):** Her client farklı süre bekler → istekler zamana yayılır. `delay = min(baseDelay * 2^attempt + random(0, 1000), maxDelay)`

**Kombine Pattern (Circuit Breaker + Bulkhead + Retry):**
Bu üçü birlikte kullanıldığında akış şöyle olur:
`İstek → Bulkhead (max 10 concurrent) → Retry (max 3 deneme, exponential backoff) → Circuit Breaker (hata oranı kontrolü) → External Service`

Bulkhead kaynakları korur, Retry geçici hataları tolere eder, Circuit Breaker kalıcı hatalarda devreyi keser. Üçü birlikte **defense in depth** sağlar.

```javascript
// Circuit Breaker + Bulkhead + Retry KOMBINE

const circuitBreaker = require('opossum');
const pLimit = require('p-limit');

// Bulkhead: Maksimum concurrent request sınırla
const bulkhead = pLimit(10); // Aynı anda max 10 istek

// Circuit Breaker: Belirli hata oranında devreyi KES
const breaker = new circuitBreaker(callExternalService, {
  timeout: 3000,           // 3 sn timeout
  errorThresholdPercentage: 50, // %50 hata → OPEN
  resetTimeout: 10000,     // 10 sn sonra tekrar dene
  volumeThreshold: 5,      // Min 5 istek sonrası değerlendir
});

// Fallback: Devre açıkken ne yapılacak?
breaker.fallback(() => {
  return { source: 'cache', data: getCachedData() }; // Stale data > No data
});

// Retry: Geçici hatalarda tekrar dene
async function resilientCall(params) {
  return bulkhead(() => 
    withRetry(() => breaker.fire(params), { 
      maxRetries: 3, 
      baseDelay: 500 
    })
  );
}

// Kullanım:
const data = await resilientCall({ endpoint: '/api/pricing' });
// Akış: Bulkhead(10) → Retry(3) → CircuitBreaker → External Service
```

---

## ✅ Özet & Next Steps

### Bu Dokümanı Tamamladıysanız

**Artık Şunları Biliyorsunuz:**
- ✅ Distributed systems internals (Raft, Paxos, 2PC, Saga)
- ✅ Performance engineering (profiling, optimization)
- ✅ Advanced databases (time-series, vector, NewSQL, graph)
- ✅ Platform engineering (IDP, service mesh)
- ✅ Advanced observability (OpenTelemetry, eBPF)
- ✅ Streaming systems (Kafka internals, stream processing)
- ✅ Advanced Kubernetes (CRDs, operators, admission controllers)
- ✅ Security architecture (zero trust, secret management)
- ✅ ML integration (model serving, feature stores, A/B testing)
- ✅ Compliance (GDPR, SOC 2)
- ✅ Technical leadership (RFCs, mentoring, speaking)
- ✅ Open source contribution

### Gelecek Adımlar

**Staff Engineer Olmak İçin:**
1. **Büyük Proje Sahipliği**
   - Company-wide impact
   - 6+ ay süren proje
   - Cross-team coordination

2. **Technical Leadership**
   - RFC yazıp onaylatın
   - Architecture review yapın
   - Mentorship program başlatın

3. **External Visibility**
   - Conference talk verin
   - Technical blog yazın
   - Open source contribute edin

4. **Domain Expertise**
   - Bir alanda derinleşin (distributed systems, performance, security)
   - Industry expert olun
   - Internal go-to person

**Principal Engineer Olmak İçin:**
1. **Industry Impact**
   - Research papers
   - Open source projects (creator/maintainer)
   - Conference keynotes

2. **Strategic Vision**
   - Company technical strategy
   - Multi-year roadmap
   - Technology bets

3. **Thought Leadership**
   - Blog following
   - Book authorship
   - Advisory roles

### Pratik Projeler

**Staff Level Projects:**
1. Build distributed database (Raft consensus)
2. Create service mesh from scratch
3. Implement distributed tracing system
4. Build ML platform (training + serving)
5. Create internal developer platform

**Katkı Sağlayın:**
- Kubernetes: CRD or operator
- Prometheus: Exporter
- Terraform: Provider
- Node.js: Core or popular library

---

## 🎬 Final Thoughts

**Bu seviyeye gelmek:**
- 7-10+ yıl sürer
- Continuous learning gerektirir
- Failure'dan öğrenmeyi gerektirir
- Patience & persistence

**Unutmayın:**
- Perfect code yoktur, trade-off vardır
- Technology değişir, fundamentals değişmez
- Communication > Technical skills (senior level'da)
- Impact > Lines of code

**Başarının Anahtarı:**
```
Curiosity + 
Continuous Learning + 
Hands-on Practice + 
Sharing Knowledge + 
Building in Public
= Staff/Principal Engineer
```

---

**Şimdi çık ve harika şeyler yap! 🚀**

*"The only way to do great work is to love what you do and never stop learning."*
