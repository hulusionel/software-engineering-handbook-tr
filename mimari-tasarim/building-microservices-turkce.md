# 🔬 Building Microservices — Türkçe Kapsamlı Rehber

> **"Microservices, bağımsız deploy edilebilen servislerin
> bir iş domain'i etrafında modellenmiş koleksiyonudur."**
> — Sam Newman

Bu kitap, microservices mimarisinin **pratik el kitabıdır.**
Newman, "microservices yapmalısınız" demez — "EĞER yapacaksanız,
İŞTE böyle yapın, ve İŞTE dikkat etmeniz gerekenler" der.
Trade-off'ları saklamaz, acı gerçekleri söyler. 🎯

---

## 📖 İçindekiler

1. [Microservices Nedir?](#1--microservices-nedir)
2. [Modelleme: Domain-Driven Design](#2--modelleme-domain-driven-design)
3. [Monolith'i Parçalama](#3--monolithi-parçalama)
4. [İletişim Stilleri](#4--i̇letişim-stilleri)
5. [Senkron İletişim](#5--senkron-i̇letişim)
6. [Asenkron İletişim](#6--asenkron-i̇letişim)
7. [Workflow ve Saga](#7--workflow-ve-saga)
8. [Build (CI/CD)](#8--build-cicd)
9. [Deployment](#9--deployment)
10. [Test](#10--test)
11. [Monitoring ve Observability](#11--monitoring-ve-observability)
12. [Güvenlik](#12--güvenlik)
13. [Dayanıklılık (Resiliency)](#13--dayanıklılık-resiliency)
14. [Ölçekleme (Scaling)](#14--ölçekleme-scaling)
15. [Kullanıcı Arayüzü](#15--kullanıcı-arayüzü)
16. [Organizasyon](#16--organizasyon)
17. [Evrimsel Mimar](#17--evrimsel-mimar)
18. [Ne Zaman Microservices?](#18--ne-zaman-microservices)
19. [Büyük Şirketlerde Microservices Gerçekleri](#19--büyük-şirketlerde-microservices-gerçekleri)
20. [Yapay Zeka Çağında Microservices](#20--yapay-zeka-çağında-microservices)
21. [Son Sözler](#21--son-sözler)

---

## 1. 🎯 Microservices Nedir?

### Newman'ın Tanımı

```
Microservice = Bağımsız deploy edilebilen servisler koleksiyonu
               + İş domain'i etrafında modelleme
               + Kendi durumunu (state) kendi yönetir

3 ANAHTAR özellik:

1. BAĞIMSIZ DEPLOYABİLİTY ← EN ÖNEMLİSİ!
   "Servis A'yı deploy ederken B'ye DOKUNMAYA gerek yok."
   Bu GERÇEKTEN yapılabiliyorsa → microservice ✅
   Deploy için 3 servis birden güncellenmesi gerekiyorsa → ❌ dağıtık monolith!

2. İŞ DOMAIN'İ ETRAFINDA MODELLEME
   Teknik katmanlar (DB, API, UI) değil,
   iş kapasiteleri (sipariş, ödeme, envanter) etrafında organize et.

3. KENDİ STATE'İNİ YÖNETİR
   Her servis kendi verisine sahip.
   Başka servisin DB'sine DOĞRUDAN erişim YASAK!
   Veri lazımsa → API üzerinden SOR.
```

### Anahtar Kavramlar

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  INFORMATION HIDING (Bilgi Gizleme)                │
│  David Parnas, 1972                                 │
│                                                     │
│  "Bir modülün iç detayları dışarıdan GİZLENMELİ.  │
│   Dışarıya sadece İHTİYAÇ olan şey açılmalı."     │
│                                                     │
│  Microservice'te:                                   │
│  → İç veritabanı şeması GİZLİ                     │
│  → İç implementasyon GİZLİ                         │
│  → Sadece PUBLIC API açık                          │
│  → İç değişiklik dışarıyı ETKİLEMEMELİ            │
│                                                     │
└─────────────────────────────────────────────────────┘

Neden önemli?
  → Bağımsız deploy'un TEMELİ bilgi gizlemedir
  → İç yapını gizleyemiyorsan → bağımsız deploy YAPAMAZSIN
  → Bağımsız deploy yapamıyorsan → microservice DEĞİLSİN
```

### Microservice ≠ Küçük Servis

```
"Micro" kelimesi YANILTICI!

Newman: "Boyut önemli DEĞİL. Önemli olan:
  1. Bağımsız deploy edilebilir mi?
  2. Bir ekip tarafından sahiplenilebilir mi?
  3. İş domain'inin BİR parçasını temsil ediyor mu?"

ÇOK küçük servis:
  ❌ "addToCart" tek bir fonksiyon servis → NANO service!
  ❌ Çok fazla servis arası iletişim
  ❌ Operasyonel yük >> iş değeri

ÇOK büyük servis:
  ❌ Birden fazla domain bağlamını barındırıyor
  ❌ 3 farklı takım aynı serviste çalışıyor
  ❌ Deploy etmek riskli (çok şey değişiyor)

DOĞRU boyut:
  ✅ "Siparişler" servisi → sipariş yaşam döngüsünü yönetir
  ✅ Bir takım sahiplenebilir (2-pizza rule)
  ✅ Bağımsız deploy edilebilir
  ✅ Bounded Context sınırlarıyla uyumlu
```

---

## 2. 🧩 Modelleme: Domain-Driven Design

### Bounded Context

```
Eric Evans'ın DDD'sindeki en önemli kavram:

BOUNDED CONTEXT = Belirli bir modelin GEÇERLi olduğu SINIR.

Aynı kelime farklı bağlamlarda FARKLI anlama gelir:

  "Müşteri" kavramı:
    Sipariş bağlamı: isim, adres, sipariş geçmişi
    Ödeme bağlamı:   kredi kartı, bakiye, ödeme geçmişi
    Destek bağlamı:  ticket'lar, SLA, öncelik seviyesi
    Pazarlama bağlam: segmentasyon, tercihler, email opt-in

  AYNI müşteri, FARKLI veriler, FARKLI iş kuralları!

  ❌ YANLIŞ: Tek bir "Customer" entity'si HER yerde kullanılır
     → 50 alan, çoğu her yerde GEREKSİZ
     → Her bağlam tüm alanlara BAĞIMLI
     → Bir değişiklik HER YERİ etkiler

  ✅ DOĞRU: Her bağlamın KENDİ müşteri modeli var
     Sipariş bağlamı: OrderCustomer { name, shippingAddress }
     Ödeme bağlamı:   PaymentCustomer { paymentMethods, balance }
     Destek bağlamı:  SupportCustomer { tickets, priority }

Her Bounded Context = potansiyel bir Microservice!
```

```javascript
// ❌ KÖTÜ: "God Object" müşteri — her yerde aynı
class Customer {
  id; name; email; phone;
  creditCard; bankAccount; balance;         // Ödeme detayları
  shippingAddress; billingAddress;           // Sipariş detayları
  tickets; slaLevel; priority;              // Destek detayları
  segment; preferences; emailOptIn;         // Pazarlama detayları
  // 30+ alan... hepsi her yerde taşınıyor
}

// ✅ İYİ: Her bağlamın kendi modeli
// --- order-service ---
class OrderCustomer {
  constructor(id, name, shippingAddress) { /* sadece sipariş bilgisi */ }
}

// --- payment-service ---
class PaymentCustomer {
  constructor(id, paymentMethods, balance) { /* sadece ödeme bilgisi */ }
}

// --- support-service ---
class SupportCustomer {
  constructor(id, tickets, slaLevel) { /* sadece destek bilgisi */ }
}
```

### Aggregate (Küme)

```
Aggregate = BİRLİKTE yönetilmesi gereken entity'ler grubu

Sipariş Aggregate'i:
  ┌────────────────────────────┐
  │ Order (Aggregate Root)     │
  │   ├── OrderItem            │
  │   ├── OrderItem            │
  │   └── ShippingInfo         │
  └────────────────────────────┘

KURALLAR:
  1. Aggregate Root dışarıdan erişilen TEK giriş noktası
     → OrderItem'a doğrudan erişME, Order üzerinden eriş
  2. Bir aggregate = bir transaction sınırı
     → Order ve OrderItem'lar AYNI transaction'da güncellenir
  3. Aggregate'ler arası referans → sadece ID ile
     → Order.customerId = "c-123" (Customer nesnesini TUTMA!)

Microservice'te aggregate:
  → Bir servis genellikle 1-3 aggregate yönetir
  → Aggregate SINIRLARI = servis SINIRLARI (iyi bir başlangıç noktası)
  → Cross-aggregate operasyonlar = Saga Pattern gerektirir
```

### Mapping: Bağlam → Servis

```
ADIM 1: Domain'i anla (Event Storming ile)
  → Domain expert'lerle birlikte
  → Post-it'lerle olayları (event) kronolojik sırala
  → "Sipariş oluşturuldu" → "Ödeme alındı" → "Stok ayrıldı" → "Kargoya verildi"

ADIM 2: Bağlam sınırlarını çiz
  → Hangi olaylar BİRLİKTE oluşuyor?
  → Hangi olaylar FARKLI takımlar/departmanlar tarafından yönetiliyor?
  → Sınır çiz!

ADIM 3: Bağlam → Servis eşleştir
  → Her bağlam = potansiyel bir servis
  → Çok küçükse → birleştir
  → Çok büyükse → daha da böl

EVENT STORMING örneği:

  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │ SİPARİŞ BAĞLAMI  │  │ ÖDEME BAĞLAMI    │  │ KARGO BAĞLAMI    │
  │                  │  │                  │  │                  │
  │ Sipariş oluşturuld│  │ Ödeme alındı     │  │ Kargoya verildi  │
  │ Ürün eklendi     │  │ Ödeme reddedildi │  │ Teslim edildi    │
  │ Sipariş onaylandı│  │ İade yapıldı     │  │ İade kargosu     │
  │                  │  │                  │  │                  │
  │ → Order Service  │  │ → Payment Service│  │ → Shipping Svc   │
  └──────────────────┘  └──────────────────┘  └──────────────────┘
```

---

## 3. 🔨 Monolith'i Parçalama

### Monolith Tipleri

```
1. SINGLE PROCESS MONOLITH (Klasik)
   → Tüm kod tek bir process'te çalışır
   → En yaygın tür
   → Aslında KÖTÜ DEĞİL! Newman: "Monolith gayet iyi bir seçenek."

2. MODÜLER MONOLITH
   → Tek process AMA iç yapı modüler
   → İyi tanımlanmış modül sınırları
   → "Microservices'in avantajlarının çoğunu, karmaşıklığı olmadan alabilirsin!"
   → Newman bunun ÇOK iyi bir seçenek olduğunu vurgular!

3. DAĞITIK MONOLITH (Distributed Monolith) 💀
   → Birden fazla servis AMA hepsi birlikte deploy edilmek ZORUNDA
   → "Microservices'in dezavantajları + monolith'in dezavantajları"
   → EN KÖTÜ durum! Her iki dünyanın da en kötüsü.

Newman: "Dağıtık monolith yapacağıma, monolith KALIRIM."
```

### Monolith Önce! (Monolith First)

```
Newman'ın güçlü tavsiyesi:

╔══════════════════════════════════════════════════════╗
║ "Eğer microservices yapıp yapamayacağınızdan         ║
║  emin değilseniz, YAPMAYIN.                         ║
║  Monolith ile başlayın."                            ║
╚══════════════════════════════════════════════════════╝

Neden monolith önce?
  1. Domain'i henüz ANLAMIYORSUN → servis sınırlarını YANLIŞ çizersin
  2. Monolith'te sınır çizmek UCUZ (namespace/modül)
  3. Yanlış sınır düzeltmek: monolith'te KOLAY, microservice'te ÇOK ZOR
  4. Operasyonel yük yok (logging, tracing, deploy pipeline × N servis)

Süreç:
  1. Monolith yaz
  2. Domain'i öğren
  3. Sınırları keşfet (modüler monolith yap)
  4. İHTİYAÇ VARSA microservice'e geç (Strangler Fig ile)
```

### Strangler Fig Pattern 🌿

```
Ağaç sarmaşığı gibi: Eski sistemi kademeli olarak SAR ve DEĞİŞTİR.

ADIM 1: Proxy koy
  [Kullanıcılar] → [Proxy] → [Monolith]
  Tüm trafik hâlâ monolith'e gidiyor.

ADIM 2: Bir parçayı çıkar
  [Kullanıcılar] → [Proxy] ─→ [Monolith]
                           └→ [Sipariş Svc] ← yeni!
  /orders → yeni servise, geri kalan → monolith

ADIM 3: Daha fazla çıkar
  [Kullanıcılar] → [Proxy] ─→ [Monolith] (küçülüyor)
                           ├→ [Sipariş Svc]
                           └→ [Ödeme Svc]

ADIM N: Monolith tamamen ortadan kalkar
  [Kullanıcılar] → [API Gateway] ─→ [Sipariş Svc]
                                 ├→ [Ödeme Svc]
                                 ├→ [Envanter Svc]
                                 └→ [Müşteri Svc]

Her adımda:
  ✅ Sistem çalışıyor (downtime yok)
  ✅ Geri alınabilir (proxy'yi geri yönlendir)
  ✅ Risk düşük (tek seferde tek parça)
```

### Veritabanını Ayırma 🗄️

**En ZOR kısım!**

```
Kod ayırmak KOLAY. Veritabanı ayırmak ZOR!

Neden zor?
  1. Foreign key'ler → join yapamam artık!
  2. Transaction → ACID kayboluyor!
  3. Veri tutarlılığı → eventual consistency!
  4. Reporting → birden fazla DB'ye karşı rapor?

ADIM ADIM:

1. Önce KODU ayır, DB'yi PAYLAŞIK bırak (geçici!)
   [Order Svc]──┐
                ├──→ [Ortak DB]
   [Payment Svc]┘
   → Riskli ama geçiş için OK

2. Mantıksal ayırma: Ayrı şema, aynı sunucu
   [Order Svc] → [orders şeması]  ┐
                                  ├ Aynı DB sunucusu
   [Payment Svc] → [payments şeması]┘
   → Foreign key'ler kaldırılır
   → JOIN yapılamaz → API ile veri alınır

3. Fiziksel ayırma: Ayrı DB sunucuları
   [Order Svc] → [Orders DB]
   [Payment Svc] → [Payments DB]
   → Tam izolasyon ✅
   → AMA: consistency, latency sorunları başlar
```

```javascript
// ÖNCE: Monolith'te JOIN ile veri alma
const query = `
  SELECT o.*, c.name, c.email
  FROM orders o
  JOIN customers c ON o.customer_id = c.id
  WHERE o.id = $1
`;

// SONRA: Microservice'te API çağrısı ile veri toplama
async function getOrderWithCustomer(orderId) {
  // 1. Sipariş bilgisini kendi DB'nden al
  const order = await orderRepository.findById(orderId);

  // 2. Müşteri bilgisini BAŞKA servisten API ile iste
  const customer = await customerServiceClient.getCustomer(order.customerId);

  return {
    ...order,
    customerName: customer.name,
    customerEmail: customer.email,
  };
}
// → JOIN yok! API call var!
// → Daha yavaş (network hop)
// → AMA bağımsız! Customer DB şeması değişse bile Order Svc etkilenMEZ
```

---

## 4. 📡 İletişim Stilleri

### Genel Bakış

```
Servisler arası iletişim 2 eksenle tanımlanır:

EKSEN 1: Senkron vs Asenkron
  Senkron:  Çağıran BEKLER. Yanıt gelene kadar bloklanır.
  Asenkron: Çağıran BEKLEMEZ. Yanıt sonra gelir (veya hiç gelmez).

EKSEN 2: Request-Response vs Event-Driven
  Request-Response: "Şunu yap ve sonucu söyle" (komut)
  Event-Driven:     "Şu oldu, ilgilenen varsa dinlesin" (bildirim)

Kombinasyonlar:
┌──────────────────────┬─────────────────┬──────────────────┐
│                      │ Request-Response│ Event-Driven     │
├──────────────────────┼─────────────────┼──────────────────┤
│ Senkron              │ REST, gRPC      │ (nadir)          │
│ Asenkron             │ Async RPC       │ Kafka, RabbitMQ  │
└──────────────────────┴─────────────────┴──────────────────┘

GENEL PRENSİP:
  → Servis İÇİ (aynı servis): Senkron fonksiyon çağrısı
  → Servis ARASI: Mümkünse ASENKRON + EVENT-DRIVEN
  → Asenkron = loose coupling = bağımsız deploy
```

### API Tasarımı: Kontrat Önce

```
"Implementation First" vs "Contract First"

❌ Implementation First:
  1. Kodu yaz
  2. API otomatik oluştur (Swagger generate)
  3. Consumer'a söyle: "İşte API'ım"
  → Sorun: İç yapı değişince API da DEĞİŞİR → consumer KIRILIR!

✅ Contract First:
  1. API kontratını ÖNCE tanımla (OpenAPI, Protobuf, JSON Schema)
  2. Consumer ile kontratı DOĞRULA
  3. Kontrata göre kodla
  → API KARARLIII kalır
  → İç değişiklik API'ı ETKİLEMEZ

Newman: "Dışarıdan içeriye düşün.
Consumer ne istiyor? → Kontratı buna göre tasarla.
Sonra kodu kontrata göre yaz."
```

---

## 5. 🔄 Senkron İletişim

### REST

```
En yaygın servis arası iletişim:

AVANTAJLAR:
  ✅ Herkes biliyor
  ✅ Tooling zengin (Postman, Swagger, OpenAPI)
  ✅ HTTP standart — her dil destekler
  ✅ Cache mekanizmaları (HTTP cache headers)

DEZAVANTAJLAR:
  ❌ Request-response zorunlu → temporal coupling
  ❌ Her çağrı network hop = latency
  ❌ Server çöktüyse → client de ÇÖKER (cascade failure riski)
  ❌ Payload genellikle JSON → büyük, yavaş serialization

REST maturity (Richardson Maturity Model):
  Level 0: Tek URL, POST her şey (SOAP tarzı)
  Level 1: Resource'lar var (/orders, /customers)
  Level 2: HTTP metodları (GET, POST, PUT, DELETE)
  Level 3: HATEOAS (hypermedia) — pratik'te NADİR kullanılır
```

### gRPC

```
Google'ın geliştirdiği yüksek performanslı RPC framework:

AVANTAJLAR:
  ✅ Protocol Buffers (protobuf) → binary, JSON'dan 10x küçük/hızlı
  ✅ Strongly typed → derleme zamanında hata yakalama
  ✅ HTTP/2 → multiplexing, bidirectional streaming
  ✅ Kod üretimi (code generation) → client SDK otomatik
  ✅ Servis-arası iletişimde REST'ten ÇOK daha performanslı

DEZAVANTAJLAR:
  ❌ Browser desteği zayıf (gRPC-Web gerekir)
  ❌ Human-readable DEĞİL (binary)
  ❌ Tooling REST kadar zengin değil
  ❌ Öğrenme eğrisi var

İDEAL KULLANIM:
  → Servis-servis arası iletişim: gRPC ✅
  → Client (browser)-server arası: REST veya GraphQL ✅
```

```javascript
// protobuf tanımı
// order.proto
/*
syntax = "proto3";

service OrderService {
  rpc CreateOrder (CreateOrderRequest) returns (CreateOrderResponse);
  rpc GetOrder (GetOrderRequest) returns (Order);
}

message CreateOrderRequest {
  string customer_id = 1;
  repeated OrderItem items = 2;
}

message OrderItem {
  string product_id = 1;
  int32 quantity = 2;
}

message CreateOrderResponse {
  string order_id = 1;
  double total = 2;
}
*/

// → Bu tanımdan JavaScript, Go, Java, Python client'ları
//   OTOMATİK üretilir!
// → Tip güvenliği GARANTILI
// → Serialization/deserialization OTOMATİK ve HIZLI
```

### Senkron İletişimin Tehlikesi ⚠️

```
ZİNCİRLEME ÇAĞRILAR (Call Chain):

  Client → A → B → C → D → E

  D çöktü! 💥
  → C timeout bekliyor (30 saniye)
  → B timeout bekliyor (C'nin timeout'ı + kendi timeout'ı)
  → A timeout bekliyor (B + C + D timeout'ları)
  → Client 2 dakika yanıt alamıyor! 😱

  Bu = TEMPORAL COUPLING = "herkes birbirine bağımlı"

  E'nin 100ms gecikmesi:
  → D: 100ms → C: 200ms → B: 300ms → A: 400ms → Client: 500ms
  Gecikme TOPLANIR! (cascade latency — zincirleme gecikme problemi)

Newman: "Senkron çağrı zincirleri ne kadar uzunsa,
         sistem o kadar KIRILGANDIR."
```

---

## 6. 📨 Asenkron İletişim

### Event-Driven İletişim

```
İki model:

1. EVENT NOTIFICATION (Olay Bildirimi)
   "Sipariş oluşturuldu" → ilgilenen herkes DİNLER
   Event'te az veri: { type: "order.created", orderId: "123" }
   Consumer detay istiyorsa → API ile sorar

2. EVENT-CARRIED STATE TRANSFER (Olayla Taşınan Durum)
   Event'te TÜM veri: { type: "order.created", orderId: "123",
                         customer: { name: "Ali", address: "..." },
                         items: [...], total: 1500 }
   Consumer'ın API çağrısına GEREK YOK (veri zaten event'te)
   → AMA event boyutu BÜYÜR
   → Consumer kendi cache'ini oluşturabilir
```

### Message Broker Seçimi

```
┌────────────────┬──────────────────┬──────────────────────┐
│                │ RabbitMQ          │ Kafka                │
├────────────────┼──────────────────┼──────────────────────┤
│ Model          │ Message Queue     │ Event Log (Stream)   │
│ Mesaj ömrü     │ Consume edilince  │ Configurable retention│
│                │ SİLİNİR           │ (günler/sonsuza kadar)│
│ Consumer       │ Competing (biri   │ Consumer Group       │
│                │ alır, diğeri almaz)│ (replay mümkün!)    │
│ Sıralama       │ Queue içinde FIFO │ Partition içinde FIFO│
│ Throughput     │ Orta              │ ÇOK YÜKSEK          │
│ Kullanım       │ Task queue,       │ Event streaming,     │
│                │ work distribution │ event sourcing, CDC  │
│ Replay         │ ❌ (mesaj silindi) │ ✅ (offset'i geri al)│
└────────────────┴──────────────────┴──────────────────────┘

NE ZAMAN HANGİSİ?
  RabbitMQ: İş kuyruğu, task dağıtımı, basit pub/sub
  Kafka: Event streaming, event sourcing, audit log, replay ihtiyacı

Newman: "Çoğu proje için RabbitMQ yeter.
         Kafka'ya ihtiyacınız olduğunu BİLİYORSANIZ, zaten biliyorsunuzdur."
```

### Asenkron Zorlukları

```
1. EVENTUAL CONSISTENCY (Nihai Tutarlılık)
   "Veri ŞU AN tutarsız olabilir ama SONUNDA tutarlı olacak."
   → Kullanıcı siparişi verdi → ödeme henüz alınmadı → durum: "bekliyor"
   → 2 saniye sonra ödeme alındı → durum: "onaylandı"
   → Kullanıcı o 2 saniyede "bekliyor" görür → NORMAL!

   AMA: Para transferinde eventual consistency KABULedileMEZ!
   → Bankacılık: Strong consistency GEREKLİ → senkron tercih et

2. IDEMPOTENCY (Tekrarlı İşlem Güvenliği) 🔑
   "Aynı mesaj 2 kez gelirse ne olur?"
   → Ağ sorunu → retry → mesaj TEKRAR geldi!
   → İdempotent değilse: 2 kez ödeme alınır! 💸😱

   Çözüm:
   → Her mesaja UNIQUE ID ver
   → İşlemden önce "bu ID'yi daha önce işledim mi?" kontrol et
   → İşlediyse → ATLA
```

```javascript
// Idempotency uygulaması
class PaymentHandler {
  #processedIds = new Set(); // Gerçek hayatta Redis/DB kullan!

  async handlePayment(event) {
    // Idempotency check
    if (this.#processedIds.has(event.idempotencyKey)) {
      console.log(`Zaten işlendi: ${event.idempotencyKey}, ATLANIYOR`);
      return; // Tekrar işleme! ✅
    }

    // İşle
    await this.paymentGateway.charge(event.amount, event.customerId);

    // Başarılıysa kaydet
    this.#processedIds.add(event.idempotencyKey);
    console.log(`İşlendi: ${event.idempotencyKey}`);
  }
}

// Gerçek hayatta Redis ile:
async function isProcessed(key) {
  const result = await redis.setnx(`idempotency:${key}`, '1');
  await redis.expire(`idempotency:${key}`, 86400); // 24 saat TTL
  return result === 0; // 0 = zaten vardı (SET yapılmadı)
}
```

```
3. MESSAGE ORDERING (Mesaj Sıralama)
   "Sipariş oluşturuldu" → "Sipariş iptal edildi"
   Ama mesajlar TERS sırada gelirse?
   "İptal edildi" → "Oluşturuldu" → iptal EDİLMEMİŞ sipariş! 😱

   Çözümler:
   → Kafka: Partition key (orderId) ile aynı partition → SIRALAMA GARANTİ
   → Sequence number: Her mesaja sıra numarası ekle
   → Idempotent + compensating: Sıralama bozulsa bile telafi et

4. DEAD LETTER QUEUE (DLQ) 💀
   "3 kez denedim, hâlâ işleyemiyorum. Ne yapayım?"
   → DLQ'ya at → insanlar inceler → manual düzeltir veya tekrar dener
   → ASLA mesajı SİLME! Her zaman DLQ'ya yönlendir.
```

---

## 7. 🔄 Workflow ve Saga

### Dağıtık İşlemler

```
Monolith:
  BEGIN TRANSACTION
    INSERT INTO orders (...)
    UPDATE inventory SET stock = stock - 1
    INSERT INTO payments (...)
  COMMIT
  → ACID garantisi ✅ Hepsi olur ya da HİÇBİRİ olmaz

Microservice:
  Order Service → kendi DB'sine yazar
  Inventory Service → kendi DB'sine yazar
  Payment Service → kendi DB'sine yazar
  → 3 farklı DB! ACID YOK! Ya biri başarısız olursa? 😱

Çözüm: SAGA PATTERN
```

### Saga: Orkestrasyon vs Koreografi

```
ORKESTRASYON (Merkezi yönetim) 🎼

  [Saga Orchestrator]
       │
       ├──1. "Sipariş oluştur" → [Order Service] → "tamam"
       ├──2. "Ödeme al"        → [Payment Service] → "tamam"
       ├──3. "Stok ayır"       → [Inventory Service] → "tamam"
       └──4. "Kargola"         → [Shipping Service] → "tamam"

  HATA! (3. adımda stok yok):
       ├──← "Ödemeyi iade et"  → [Payment Service] → "iade tamam"
       └──← "Siparişi iptal et"→ [Order Service] → "iptal tamam"

  ✅ Akış net, debug kolay
  ✅ Hata yönetimi merkezi
  ❌ Orchestrator = single point of failure
  ❌ Tight coupling (orchestrator her servisi bilir)

KOREOGRAFİ (Dağıtık yönetim) 💃

  [Order Service] → EVENT: "order.created"
       ↓
  [Payment Service] dinler → ödeme alır → EVENT: "payment.completed"
       ↓
  [Inventory Service] dinler → stok ayırır → EVENT: "stock.reserved"
       ↓
  [Shipping Service] dinler → kargolar → EVENT: "shipment.created"

  HATA! (Inventory "stock.failed" yayınlar):
  [Payment Service] dinler → "payment.refunded"
  [Order Service] dinler → "order.cancelled"

  ✅ Loosely coupled (servisler birbirini bilmez!)
  ✅ Single point of failure YOK
  ❌ Akış dağınık, debug ZOR
  ❌ "Şu an sipariş hangi DURUMDA?" sorusu zor
  ❌ Yeni adım eklemek → hangi event'leri dinlemeli?
```

```javascript
// Orkestrasyon örneği (Saga Orchestrator)
class CreateOrderSaga {
  #steps = [];
  #completedSteps = [];

  constructor({ orderService, paymentService, inventoryService, shippingService }) {
    this.#steps = [
      {
        name: 'createOrder',
        execute: (ctx) => orderService.create(ctx.orderData),
        compensate: (ctx) => orderService.cancel(ctx.orderId),
      },
      {
        name: 'processPayment',
        execute: (ctx) => paymentService.charge(ctx.orderId, ctx.total),
        compensate: (ctx) => paymentService.refund(ctx.orderId),
      },
      {
        name: 'reserveStock',
        execute: (ctx) => inventoryService.reserve(ctx.items),
        compensate: (ctx) => inventoryService.release(ctx.items),
      },
      {
        name: 'createShipment',
        execute: (ctx) => shippingService.create(ctx.orderId, ctx.address),
        compensate: (ctx) => shippingService.cancel(ctx.orderId),
      },
    ];
  }

  async execute(context) {
    for (const step of this.#steps) {
      try {
        const result = await step.execute(context);
        this.#completedSteps.push(step);
        Object.assign(context, result); // Sonraki adımlar için context güncelle
      } catch (error) {
        console.error(`Saga HATA: ${step.name}`, error);
        await this.#compensate(context); // GERİ AL!
        throw new Error(`Saga başarısız: ${step.name}`);
      }
    }
    return context;
  }

  async #compensate(context) {
    // Tamamlanan adımları TERS SIRAYA al ve telafi et
    for (const step of this.#completedSteps.reverse()) {
      try {
        await step.compensate(context);
        console.log(`Kompanzasyon başarılı: ${step.name}`);
      } catch (error) {
        console.error(`Kompanzasyon HATASI: ${step.name}`, error);
        // 🚨 Manuel müdahale gerekebilir! Alert gönder!
      }
    }
  }
}
```

### Hangisini Seç?

```
┌──────────────────┬──────────────────┬──────────────────┐
│ Kriter           │ Orkestrasyon     │ Koreografi       │
├──────────────────┼──────────────────┼──────────────────┤
│ Adım sayısı      │ 3+ → tercih et  │ 2-3 → yeterli   │
│ Akış görünürlüğü │ ✅ Net           │ ❌ Dağınık       │
│ Coupling          │ Daha tight      │ Daha loose       │
│ Hata yönetimi    │ ✅ Kolay (merkez)│ ❌ Zor (dağıtık) │
│ Ölçeklenme       │ Bottleneck riski │ ✅ Bağımsız      │
│ Karmaşıklık      │ Orchestrator     │ Event spaghetti  │
└──────────────────┴──────────────────┴──────────────────┘

Newman: "İkisini de KARIŞTIRABİLİRSİN!
  Küçük akışlar → koreografi
  Karmaşık, kritik akışlar → orkestrasyon"
```

---

## 8. 🏗️ Build (CI/CD)

### Bir Repo mu, Çok Repo mu?

```
MONOREPO (Tek Repo):
  repo/
    services/
      order-service/
      payment-service/
      customer-service/
    libs/
      shared-utils/

  ✅ Atomik değişiklik (3 servisi tek commit'te güncelle)
  ✅ Kod paylaşımı kolay
  ✅ Refactoring kolay
  ❌ Build süreleri uzar (her şeyi build etme riski)
  ❌ Ownership belirsiz (herkes her yere commit atabilir)
  ❌ Tooling gerekir (Bazel, Nx, Turborepo)

MULTIREPO (Çok Repo):
  order-service/     → kendi repo'su
  payment-service/   → kendi repo'su
  customer-service/  → kendi repo'su

  ✅ Net ownership (takım = repo)
  ✅ Bağımsız build/deploy pipeline
  ✅ Erişim kontrolü kolay
  ❌ Kod paylaşımı zor (shared lib → npm paketi olmalı)
  ❌ Cross-service değişiklik → birden fazla PR

Newman: "Multirepo bağımsız deploy'u ZORLAR.
         Monorepo bağımsızlığı KOLAYLIKLA BOZAR."
→ Tercihi: Multirepo (çoğu durumda)
→ AMA: Monorepo yapılabilir, disiplin GEREKLİ
```

### CI/CD Prensipleri

```
CI (Continuous Integration):
  → Her commit → build → test → hızlı feedback
  → "Ana branch her zaman DEPLOYABLE"
  → Her servis için AYRI pipeline (multirepo'da doğal)

CD (Continuous Delivery):
  → Her başarılı build → staging'e OTOMATİK deploy
  → Production'a → tek tıkla veya otomatik

CD (Continuous Deployment):
  → Her başarılı build → PRODUCTION'a OTOMATİK deploy
  → İnsan müdahalesi SIFIR
  → "Microservices'in GERÇEK gücü bağımsız deploy'dur.
     Bunu CI/CD olmadan YAPAMAZSIN."

Her servisin KENDİ pipeline'ı olmalı:
  Order Service değişti → sadece Order Service build+test+deploy
  Payment Service ETKİLENMEZ!
  → Bu bağımsız deployability'nin ta kendisi! ✅
```

---

## 9. 🚀 Deployment

### Deployment Seçenekleri

```
1. FIZIKSEL SUNUCU
   → Bir servis = bir sunucu
   → Kaynak israfı! Çoğu zaman CPU %5
   → ❌ Microservices için kötü seçenek

2. SANAL MAKİNA (VM)
   → Bir servis = bir VM
   → Daha iyi izolasyon
   → AMA ağır (GB boyutunda image, dakikalar süren boot)

3. CONTAINER (Docker) 🐳
   → Bir servis = bir container
   → Hafif (MB boyutunda, saniyeler süren boot)
   → İzolasyon yeterli
   → ✅ Microservices için EN YAYGIN seçenek

4. KUBERNETES (K8s) ☸️
   → Container orkestrasyonu
   → Auto-scaling, self-healing, rolling update
   → ✅ Microservices için DE FACTO standart
   → ❌ Öğrenme eğrisi YÜKSEK, operasyonel yük VAR

5. SERVERLESS (FaaS)
   → AWS Lambda, Google Cloud Functions
   → Sadece çalıştığında ÖDE
   → Otomatik ölçeklenme (sıfırdan sonsuza)
   → ❌ Cold start, vendor lock-in, stateless zorunluluğu
   → ✅ Event-driven, düşük/düzensiz trafikli servisler için ideal
```

### Deployment Stratejileri

```
1. ROLLING UPDATE ↻
   Eski instance'ları TEK TEK yenisiyle değiştir.
   [v1] [v1] [v1] [v1]
   [v2] [v1] [v1] [v1]  → 1. instance güncellendi
   [v2] [v2] [v1] [v1]  → 2. instance güncellendi
   [v2] [v2] [v2] [v1]  → 3. instance güncellendi
   [v2] [v2] [v2] [v2]  → tamamlandı ✅
   ✅ Zero downtime
   ❌ Geçiş süresinde v1 ve v2 BİRLİKTE çalışır (uyumluluk şart!)

2. BLUE-GREEN DEPLOYMENT 🔵🟢
   İki ortam: mavi (eski), yeşil (yeni).
   [BLUE: v1] ← tüm trafik
   [GREEN: v2] ← hazırlanıyor, trafik YOK
   → Test et
   → Switch! Trafik GREEN'e yönlendir
   [BLUE: v1] ← trafik YOK (backup/rollback)
   [GREEN: v2] ← tüm trafik ✅
   ✅ Anında rollback (switch geri)
   ❌ 2x kaynak gerekir (iki ortam)

3. CANARY DEPLOYMENT 🐤
   Yeni versiyonu KÜÇÜK bir gruba aç, sonucu izle.
   [v1: %95 trafik] [v2: %5 trafik]
   → Hata oranı normal mi? Latency OK mi?
   → Evet! → %10, %25, %50, %100
   → Hayır! → v2'yi geri al (sadece %5 etkilendi)
   ✅ Düşük risk
   ✅ Gerçek kullanıcı verisiyle test
   ❌ Monitoring + routing karmaşıklığı
```

---

## 10. 🧪 Test

### Test Piramidi (Microservices İçin)

```
        ╱╲
       ╱  ╲        E2E Tests       → Çok az, YAVAS, KIRILGAN
      ╱    ╲       (end-to-end)       Tüm servisleri ayağa kaldır
     ╱──────╲
    ╱        ╲     Integration      → Servis sınırlarını test et
   ╱          ╲    Tests              API kontrat testleri
  ╱            ╲                       DB entegrasyon testleri
 ╱──────────────╲
╱                ╲  Unit Tests      → Çok fazla, HIZLI, GÜVENILIR
╱                  ╲                   İş mantığını test et
╱────────────────────╲

MICROSERVICES'TE FARK:
  → E2E testler ÇOK ZOR (10 servisi birden ayağa kaldır?)
  → Integration testlerin MALİYETİ yüksek
  → Contract testler çok ÖNEMLİ!
```

### Contract Testing (Kontrat Testi) 📜

```
Sorun:
  Order Service → Payment Service API'sine çağrı yapıyor.
  Payment Service ekibi API'yi DEĞİŞTİRDİ! 💥
  Order Service KIRILDI!
  → Kim test edecekti? İki ayrı takım, ayrı repo, ayrı pipeline...

Çözüm: CONSUMER-DRIVEN CONTRACT TESTING (Pact gibi)

  Consumer (Order Service):
    "Ben Payment Service'ten şu formatta cevap BEKLİYORUM:
    { transactionId: string, status: 'success' | 'failed' }"
    → Bu BEKLENTİ bir KONTRAT dosyası oluşturur

  Provider (Payment Service):
    "Consumer'ın kontratına göre test ediyorum.
     Benim API'ım bu kontratı sağlıyor mu?"
    → Sağlıyorsa ✅ → Deploy edilebilir
    → Sağlamıyorsa ❌ → Deploy ENGELLENIR! Breaking change!

  Akış:
    Consumer → kontrat yazar → Pact Broker'a yükler
    Provider → kontratı indirir → kendini test eder
    → İki taraf da bağımsız test eder, E2E'ye GEREK YOK!
```

```javascript
// Pact contract test örneği (consumer tarafı)
const { Pact } = require('@pact-foundation/pact');

describe('Payment Service Consumer Contract', () => {
  const provider = new Pact({
    consumer: 'OrderService',
    provider: 'PaymentService',
    port: 1234,
  });

  beforeAll(() => provider.setup());
  afterAll(() => provider.finalize());

  test('ödeme başarılı olduğunda transaction döner', async () => {
    // BEKLENTİ (kontrat)
    await provider.addInteraction({
      state: 'müşterinin geçerli kartı var',
      uponReceiving: 'ödeme isteği',
      withRequest: {
        method: 'POST',
        path: '/payments',
        body: { orderId: '123', amount: 100, currency: 'TRY' },
      },
      willRespondWith: {
        status: 201,
        body: {
          transactionId: Matchers.string('tx-abc-123'),
          status: 'success',
        },
      },
    });

    // GERÇEK çağrı (mock provider'a)
    const result = await paymentClient.charge('123', 100, 'TRY');

    expect(result.transactionId).toBeDefined();
    expect(result.status).toBe('success');
  });
});

// → Bu test bir "kontrat" dosyası üretir
// → Payment Service bu kontratı doğrular
// → İki taraf da bağımsız test eder ✅
```

### E2E Testlerin Sınırları

```
Newman: "E2E testlere MINIMUM yatırım yap."

Neden?
  1. YAVAŞ: 10 servis + DB'leri + message broker → dakikalar/saatler
  2. KIRILGAN: Herhangi bir servis çökerse test BAŞARISIZ
  3. BELIRSIZ: "Test başarısız — hangi servis bozdu?"
  4. BOTTLENECK: "E2E'ler geçene kadar deploy EDEMEYİZ" → bağımsızlık KAYBOLUR

Alternatif yaklaşım:
  → Unit test (çok) + Contract test (yeterli) + E2E (çok az)
  → "Smoke test": Production'da temel akışı doğrula
  → Synthetic monitoring: "Her 5 dakikada sipariş oluşturmayı DENE"
  → Canary deployment: Gerçek trafik ile test
```

---

## 11. 👁️ Monitoring ve Observability

### 3 Sütun

```
OBSERVABILITY = Log + Metrik + Trace

1. LOGLar 📝
   → "Ne oldu?"
   → Servis başına binlerce satır/saniye
   → YAPILANDIRILMIŞ (structured) log kullan!

2. METRİKLER 📊
   → "Sistem nasıl?"
   → CPU, bellek, istek sayısı, hata oranı, latency
   → Prometheus, Grafana, Datadog

3. DAĞITIK İZLEME (Distributed Tracing) 🔎
   → "Bir request tüm servislerde nasıl akar?"
   → Correlation ID ile izle
   → Jaeger, Zipkin, OpenTelemetry
```

### Correlation ID 🆔

```
SORUN:
  Kullanıcı "sipariş başarısız" diyor.
  Order Service logları: "200 OK"
  Payment Service logları: "timeout"
  Inventory Service logları: "stok yok"
  → HANGİ request? Loglar karışık! 10K request/saniye!

ÇÖZÜM: Correlation ID

  Client → Request (Header: X-Correlation-ID: "abc-123")
    → Order Service: [abc-123] Sipariş oluşturma başladı
      → Payment Service: [abc-123] Ödeme isteği gönderildi
        → Payment Gateway: [abc-123] Gateway timeout
      → Payment Service: [abc-123] Ödeme BAŞARISIZ
    → Order Service: [abc-123] Sipariş IPTAL edildi

  ARTIK: "abc-123" ile ARA → tüm servisler boyunca AKIŞI GÖR! ✅
```

```javascript
// Correlation ID middleware (Express)
const { v4: uuidv4 } = require('uuid');

function correlationIdMiddleware(req, res, next) {
  // Gelen request'te varsa kullan, yoksa oluştur
  const correlationId = req.headers['x-correlation-id'] || uuidv4();
  req.correlationId = correlationId;
  res.setHeader('x-correlation-id', correlationId);

  // Logger'a ekle (structured logging)
  req.log = req.log || logger.child({ correlationId });
  req.log.info({ method: req.method, path: req.path }, 'Request alındı');

  next();
}

// Başka servise çağrı yaparken ID'yi İLET
async function callPaymentService(orderId, amount, correlationId) {
  return fetch(`${PAYMENT_URL}/payments`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Correlation-ID': correlationId, // ← ID'yi taşı!
    },
    body: JSON.stringify({ orderId, amount }),
  });
}
```

### Alerting Stratejisi

```
HER metrriğe alert KOYMA! → Alert fatigue (uyarı yorgunluğu)

İYİ alerting:
  → USE Method (Brendan Gregg):
    U: Utilization (Kullanım) → CPU %90 üzeri
    S: Saturation (Doygunluk) → Queue'da 1000+ mesaj birikti
    E: Errors (Hatalar) → Hata oranı %5 üzeri

  → RED Method (Tom Wilkie):
    R: Rate (Hız) → request/saniye anormal düşüş
    E: Errors → hata oranı yükseliyor
    D: Duration → yanıt süresi normalin 2x üzeri

  → SLO bazlı alerting:
    "Son 1 saatte %99.9 availability sağlıyor muyuz?"
    Sağlıyorsa → alert VERME
    Sağlamıyorsa → alert VER (error budget TÜKENIYOR!)
```

---

## 12. 🔐 Güvenlik

### Servis Arası Güvenlik

```
MONOLITH: İç çağrılar güvenli (aynı process)
MICROSERVICE: Her çağrı AĞ ÜZERINDEN → GÜVENSIZ!

1. SERVIS-SERVIS AUTH:
   → mTLS (mutual TLS): Her servisin sertifikası var
     Servis A ↔ (TLS) ↔ Servis B
     İkisi de birbirini DOĞRULAR
     → Service Mesh (Istio) bunu OTOMATİK yapar ✅

   → JWT / API Key: Her servisin token'ı var
     Servis A → { Authorization: "Bearer <token>" } → Servis B
     B token'ı doğrular
     → Basit ama token yönetimi ZORDUR

2. LEAST PRIVILEGE:
   → "Her servisin sadece İHTİYACI olan yetkisi olmalı"
   → Payment Service → sadece ödeme DB'sine erişebilir
   → Order Service → Payment DB'sine erişEMEZ

3. DEFENSE IN DEPTH:
   → Tek bir güvenlik katmanına GÜVENME!
   → Network policy + mTLS + auth token + input validation
   → "Soğan gibi katmanlar" 🧅
```

### Confused Deputy Problem

```
SORUN:
  Kullanıcı → API Gateway (yetkili) → Mikro Servis (yetkili)
  "API Gateway benim adıma HER ŞEYİ yapabilir mi?"

  Kötü niyetli kullanıcı:
    "Başka kullanıcının verisini SİL" → API Gateway'e gönderir
    API Gateway yetkili olduğu için → Mikro Servis kabul eder! 💥
    → "Confused Deputy" = Yetkili ajan, yanlış kişi adına hareket edir

ÇÖZÜM:
  → End-user identity'yi TAŞI (JWT ile)
  → Her servis "BU İŞTEĞİ KİM yapıyor?" sorusunu sorsun
  → API Gateway'in yetkisi ≠ kullanıcının yetkisi
```

---

## 13. 💪 Dayanıklılık (Resiliency)

### Hata Kaçınılmazdır! 🔥

```
Newman: "Microservice'lerde hata OLACAK. Soru şu:
         Hata olduğunda sistem nasıl DAVRANIR?"

Monolith: Çöktü → HER ŞEY çöktü
Microservice: Bir servis çöktü → DİĞERLERİ çalışmaya DEVAM ETMELİ!

Bu TASARLANMALI — tesadüfen OLMAZ!
```

### Circuit Breaker Pattern 🔌

```
Elektrik sigortası gibi!

Normal durum (CLOSED):
  Order Svc → Payment Svc ✅
  Her çağrı geçer.

  Payment Svc yavaşlamaya başladı...
  Hata sayısı eşik değeri aştı!

Sigorta ATTI (OPEN):
  Order Svc → [Circuit Breaker: AÇIK] ✋ Payment Svc'ye GÖNDERMEZ!
  → Hemen fallback döner: "Ödeme şu an yapılamıyor"
  → Payment Svc'ye YÜKLENMEYI durdurur (toparlanma şansı verir!)

  Bir süre sonra...

Yarı açık (HALF-OPEN):
  Order Svc → [1 tane DENEME çağrı] → Payment Svc
  → Başarılı? → CLOSED'a dön (normal!)
  → Başarısız? → OPEN'a dön (hâlâ sorunlu!)
```

```javascript
// Circuit Breaker implementasyonu (basitleştirilmiş)
class CircuitBreaker {
  #state = 'CLOSED';         // CLOSED, OPEN, HALF_OPEN
  #failureCount = 0;
  #failureThreshold = 5;     // 5 hata → aç
  #resetTimeout = 30_000;    // 30 saniye sonra dene
  #lastFailureTime = null;

  async call(fn) {
    if (this.#state === 'OPEN') {
      if (Date.now() - this.#lastFailureTime > this.#resetTimeout) {
        this.#state = 'HALF_OPEN'; // Deneme zamanı
      } else {
        throw new Error('Circuit OPEN — çağrı engellendi ⚡');
      }
    }

    try {
      const result = await fn();
      this.#onSuccess();
      return result;
    } catch (error) {
      this.#onFailure();
      throw error;
    }
  }

  #onSuccess() {
    this.#failureCount = 0;
    this.#state = 'CLOSED';
  }

  #onFailure() {
    this.#failureCount++;
    this.#lastFailureTime = Date.now();

    if (this.#failureCount >= this.#failureThreshold) {
      this.#state = 'OPEN';
      console.warn(`Circuit OPEN! ${this.#failureCount} hata.`);
    }
  }
}

// Kullanım
const paymentCircuit = new CircuitBreaker();

async function processPayment(orderId, amount) {
  try {
    return await paymentCircuit.call(() =>
      paymentClient.charge(orderId, amount)
    );
  } catch (error) {
    // Fallback: "Ödeme gecikmeli işlenecek"
    await messageQueue.publish('payment.pending', { orderId, amount });
    return { status: 'pending', message: 'Ödemeniz kısa sürede işlenecek' };
  }
}
```

### Diğer Dayanıklılık Pattern'ları

```
1. TIMEOUT ⏱️
   → Her dış çağrıya MUTLAKA timeout koy
   → Default: yok! → Sonsuza kadar bekler! 💀
   → "3 saniye yanıt gelmezse → BIRAK!"

2. RETRY + EXPONENTIAL BACKOFF 🔁
   1. deneme: hemen
   2. deneme: 1 saniye sonra
   3. deneme: 2 saniye sonra
   4. deneme: 4 saniye sonra
   5. deneme: BIRAK! (DLQ'ya at)

   + JITTER: Rastgele süre ekle
     → 1000 client aynı anda retry yaparsa → thundering herd!
     → Jitter ile dağıt: 1s + random(0-500ms)

3. BULKHEAD (Bölme) 🚢
   Gemi bölmeleri gibi: bir bölme su alsa diğerleri KURU kalır!
   → Thread pool'ları ayır:
     Payment çağrıları → 10 thread
     Email çağrıları → 5 thread
     Payment çöktü → 10 thread tükendi
     AMA email thread'leri ETKİLENMEDI! ✅

4. FALLBACK (Yedek Plan) 🔄
   → Ana servis çöktüyse ne yapacaksın?
   → Cache'ten eski veri döndür (stale data > no data!)
   → Degraded mode: "Öneriler şu an yüklenemiyor"
   → Queue'ya at: "Sonra işlenecek"
```

---

## 14. 📈 Ölçekleme (Scaling)

### 4 Eksenli Ölçekleme

```
1. VERTICAL SCALING (Dikey) ⬆️
   → Daha büyük makine: daha fazla CPU, RAM
   → Sınırlı! (en büyük makine ne kadar büyük olabilir?)
   → ❌ Microservices için sınırlı fayda

2. HORIZONTAL SCALING (Yatay) ⬅️➡️
   → Daha çok instance: 1 → 5 → 20 → 100
   → Load balancer ile trafik dağıtımı
   → ✅ Microservices için TEMEL yaklaşım
   → Stateless servisler kolayca ölçeklenir

3. DATA PARTITIONING (Veri Bölümleme) 📊
   → Veritabanını parçala (sharding)
   → Müşteri A-M → DB1, N-Z → DB2
   → DDIA'da detaylı gördüğün konular!

4. FUNCTIONAL DECOMPOSITION (Fonksiyonel Ayrıştırma) 🧩
   → Farklı fonksiyonlar = farklı servisler = farklı ölçekleme
   → Sipariş servisi: 3 instance (düşük trafik)
   → Arama servisi: 20 instance (yüksek trafik)
   → Her servis KENDİ ihtiyacına göre ölçeklenir! ✅
```

### Caching Stratejileri

```
Microservices'te cache HAYATI!
Network hop'ları azalt, latency düşür.

1. CLIENT-SIDE CACHE
   → Consumer serviste cache
   → "Payment rates'i 5 dakika cache'le"
   → ✅ Çok hızlı (network hop yok!)
   → ❌ Stale data riski, invalidation ZOR

2. SERVER-SIDE CACHE
   → Producer serviste cache (Redis gibi)
   → "Sık sorulan ürün detaylarını Redis'te tut"
   → ✅ Tüm consumer'lar fayda görür
   → ❌ Ekstra altyapı (Redis cluster)

3. CACHE-ASIDE (Lazy Loading)
   → "Cache'te var mı? → Evet: döndür → Hayır: DB'den al, cache'e yaz, döndür"
   → En yaygın pattern!

4. WRITE-THROUGH
   → "DB'ye yaz + aynı anda cache'e yaz"
   → Cache her zaman GÜNCEL ama yazma YAVAŞ

CACHE INVALIDATION:
  "Bilgisayar bilimlerindeki en zor 2 şey:
   Cache invalidation ve isimlendirme." — Phil Karlton

  Newman: "TTL (Time-To-Live) en basit ve en GÜVENLİ yöntem.
           Karmaşık invalidation'a girmeden önce TTL'i dene!"
```

---

## 15. 🖥️ Kullanıcı Arayüzü

### Backend for Frontend (BFF) Pattern

```
SORUN:
  Web, iOS, Android → hepsi FARKLI veri ihtiyacına sahip
  Web: tam ürün detayı + yorumlar + öneriler
  Mobil: küçük resim + fiyat + stok durumu
  → Tek bir API herkese uymuyor!

ÇÖZÜM: Her frontend için ÖZEL bir backend

  [Web App]        [iOS App]       [Android App]
      ↓                ↓                ↓
  [Web BFF]        [iOS BFF]       [Android BFF]
      ↓                ↓                ↓
  ┌──────────────────────────────────────┐
  │   Microservices (Backend)            │
  │   Order, Payment, Product, User...   │
  └──────────────────────────────────────┘

BFF avantajları:
  → Her frontend KENDİ ihtiyacına göre veri toplar
  → Web BFF: 5 servis çağırır, zengin response
  → Mobil BFF: 2 servis çağırır, kompakt response
  → Frontend ekibi KENDİ BFF'ini yönetir
```

### API Gateway vs BFF

```
API GATEWAY:
  → TEK giriş noktası
  → Auth, rate limiting, routing
  → TÜM client'lara TEK API
  → Kong, AWS API Gateway, NGINX

BFF:
  → Her frontend için ÖZEL gateway
  → İş mantığı içerebilir (aggregation)
  → Frontend ekibi sahiplenir

KOMBİNASYON:
  [Clients] → [API Gateway] → [BFF'ler] → [Microservices]
  → Gateway: Cross-cutting (auth, rate limit)
  → BFF: Frontend-specific aggregation
```

### Micro Frontend 🧩

```
Backend → Microservices
Frontend → Micro Frontends?

  Klasik: Monolithik SPA (React/Vue/Angular)
  → Tek repo, tek build, tek deploy

  Micro Frontend: Her ekip KENDİ frontend parçasını build + deploy eder
  → Sipariş ekibi: /orders sayfası → kendi React uygulaması
  → Ürün ekibi: /products sayfası → kendi Vue uygulaması
  → "Shell" app sadece birleştirme yapar (Module Federation, iframe, web components)

Newman: "Micro frontend, microservices'in frontend karşılığıdır.
         AMA karmaşıklığı ÇOK ARTTIRABILIR. Dikkatli ol!"
```

---

## 16. 🏢 Organizasyon

### Conway's Law (Tekrar!)

```
"Sistem tasarımı, organizasyon yapısını YANSITIR."

Tersinden kullan (Inverse Conway Maneuver):
  İSTEDİĞİN mimariyi belirle → Ekipleri BUNA GÖRE organize et!

3 takımın varsa → en fazla 3 servis mantıklı
10 takımın varsa → 10 servis mantıklı
Tek takımla 20 microservice → 💥 FELAKET!
```

### Ekip Modelleri

```
1. PLATFORM TAKIMI 🏗️
   → Altyapı sağlar: CI/CD, monitoring, service mesh
   → Diğer ekiplerin işini KOLAYLAŞTTIRIR
   → "Internal Developer Platform"

2. STREAM-ALIGNED TAKIMI 🏊
   → Bir iş akışına/domain'e ODAKLANIR
   → "Sipariş takımı" → Order Service + Order BFF
   → End-to-end sahiplenme (you build it, you run it!)

3. ENABLING TAKIMI 📚
   → Diğer takımlara yeni beceriler KAZANDTIRIR
   → "Observability guild" → ekiplere tracing öğretir
   → Geçici (beceri kazandırınca geri çekilir)

4. COMPLICATED-SUBSYSTEM TAKIMI 🧮
   → Özel uzmanlık gerektiren alanlar
   → "ML Model takımı" → öneri motoru
   → Derinden uzman, dar alan

Kaynak: "Team Topologies" — Matthew Skelton & Manuel Pais
```

### Ownership — "You Build It, You Run It"

```
Amazon'un meşhur prensibi:

"Servisi YAZAN ekip, servisi İŞLETEN ekiptir."

Eski dünya:
  Dev ekibi → kodu yazar → "işletim ekibine" atar → "artık onların sorunu"
  → Dev ekibi production'dan KOPUK → kötü kararlar

Yeni dünya:
  Dev ekibi → kodu yazar → deploy eder → monitör eder → on-call olur
  → "Gece 3'te alarm çalıyorsa, kodu SEN düzeltirsin"
  → Dev ekibi production-aware KOD yazar (logging, monitoring, fallback)

Newman: "Servisi sahiplenmek, onu DAHA İYİ yapmak için
         en güçlü motivasyondur."
```

---

## 17. 🧭 Evrimsel Mimar

### Mimarın Rolü

```
Newman'a göre mimar:

❌ "Fildişi kule mimarı"
   → Diyagramlar çizer, ama kod yazMAZ
   → Kararları verir ama SONUÇLARINI görmez
   → Ekipten kopuk, gerçekçi olmayan tasarımlar

✅ "Evrimsel mimar"
   → Kodu biliyor, ara sıra yazıyor
   → Ekiplerle BERABER çalışıyor
   → Kararları veriyor VE sonuçlarını izliyor
   → Kuralları koyuyor AMA NEDEN'ini açıklıyor

Şehir planlamacısı metaforu:
  "Mimar bir binayı tasarlayan kişi DEĞİL.
   Şehrin GENEL PLANINI yapan kişi.
   Her binanın tasarımını ekiplere BIRAKIR.
   AMA yolların genişliğini, bölgeleri, altyapıyı BELİRLER."
```

### Governance (Yönetişim)

```
PRENSIP: "Rehberlik VER, mikro-yönetim YAPMA."

Newman'ın önerisi:
  → "İzin verilmiş teknolojiler" listesi oluştur
    "Node.js, Go, Python kullanılabilir. Rust ve Elixir deneysel."
  → "Altın yollar" tanımla (standart şablonlar)
    "Yeni servis? Bu template'i kullan: logging, monitoring, CI/CD hazır."
  → Standartları ZORLA ama NEDEN'ini açıkla
    "Structured logging ZORUNLU. Çünkü 50 servisin logunu grep'lemek İMKANSIZ."
  → Exemplar (örnek servis) sağla
    "Nasıl yapılacağını öğrenmek ister misin? Şu servise bak."
```

---

## 18. ❓ Ne Zaman Microservices?

### Microservices NE ZAMAN?

```
✅ MICROSERVICES İYİ SEÇENEKTİR:

  1. Bağımsız deploy GEREKLİ
     → Farklı takımlar farklı hızlarda deploy etmeli
     → "Order servisi günde 5 kez, Payment servisi haftada 1"

  2. Farklı ölçekleme GEREKLİ
     → Search: 100 instance, Payment: 5 instance

  3. BÜYÜK organizasyon (20+ geliştirici)
     → Tek repo'da 50 kişi çalışamaz (merge conflict cehennemi)

  4. Teknoloji ÇESITLILIGI
     → Order: Node.js, ML: Python, High-perf: Go

  5. Domain KARMAŞIK ve İTi ANLAŞILMIŞ
     → Bounded context'ler NET
     → Servis sınırları KARALI
```

```
❌ MICROSERVICES KÖTÜ SEÇENEKTİR:

  1. KÜÇÜK ekip (< 10 kişi)
     → Operasyonel yük >> fayda
     → "5 kişilik ekip 20 servisi nasıl yönetsin?"

  2. STARTUP / MVP
     → Hız önemli, mimari DEĞİL
     → Domain'i henüz ANLAMIYORSUN → sınırlar YANLIŞ olacak
     → "Monolith ile hızlıca market'e çık, sonra evril!"

  3. Domain İYİ ANLAŞILMAMIŞ
     → Servis sınırlarını yanlış çizersen → dağıtık monolith! 💀
     → Yanlış sınırı düzeltmek microservice'te ÇOK ZOR

  4. Operasyonel olgunluk YOK
     → CI/CD pipeline yok? Monitoring yok? Logging standardı yok?
     → ÖNCE bunları kur, SONRA microservices düşün!

  5. Performans kritik ve low-latency
     → Her network hop = latency ekler
     → Ultra-low latency? Monolith veya binary protokol
```

### Karar Matrisi

```
┌──────────────────────────┬─────────┬──────────┬──────────────┐
│ Kriter                    │Monolith │  SBA     │ Microservices│
├──────────────────────────┼─────────┼──────────┼──────────────┤
│ Ekip boyutu < 10         │ ✅✅✅  │ ✅✅     │ ❌           │
│ Ekip boyutu 10-50        │ ✅      │ ✅✅✅   │ ✅✅         │
│ Ekip boyutu 50+          │ ❌      │ ✅✅     │ ✅✅✅       │
│ Domain iyi anlaşılmış    │ ✅      │ ✅✅     │ ✅✅✅       │
│ Domain belirsiz          │ ✅✅✅  │ ✅       │ ❌           │
│ Hızlı MVP               │ ✅✅✅  │ ✅✅     │ ❌           │
│ Bağımsız deploy gerekli  │ ❌      │ ✅✅     │ ✅✅✅       │
│ Farklı ölçekleme gerekli │ ❌      │ ✅       │ ✅✅✅       │
│ Operasyonel olgunluk düşük│ ✅✅✅ │ ✅       │ ❌           │
│ Basitlik öncelikli       │ ✅✅✅  │ ✅✅     │ ❌           │
└──────────────────────────┴─────────┴──────────┴──────────────┘

Newman: "Microservices bir HEDEF değildir!
         Bağımsız deploy bir ARAÇTIR!
         Aracı kullanmanın maliyetini hesapla!"
```

---

## 19. � Büyük Şirketlerde Microservices Gerçekleri

### Amazon — Microservices'in Doğduğu Yer

```
2002: Jeff Bezos'un ünlü "API Mandate" mektubu:
  1. Tüm ekipler SERVİS ARAYÜZÜ üzerinden iletişim kuracak
  2. Doğrudan DB erişimi, shared memory, backdoor YASAK
  3. Teknoloji seçimi SERBest (HTTP, gRPC, ne istersen)
  4. BU KURALI uymayan KOVULACAK

Sonuç:
  → AWS bu iç altyapının dışarıya açılmasıyla doğdu
  → Her servis "two-pizza team" (8-10 kişi) tarafından sahiplenilir
  → "You build it, you run it" kültürü

Newman'ın kitabıyla bağlantı:
  → Ownership = "Bağımsız deploy edilebilirlik"
  → API Mandate = "Information Hiding"
  → Two-pizza = "Conway's Law'ı BİLİNÇLİ kullanma"
```

### Spotify — Squad Model ve Microservices

```
Spotify modeli:
  → Squad: 6-12 kişilik çapraz fonksiyonel ekip
  → Her squad 1-3 microservice sahiplenir
  → Tribe: İlgili squad'ların birleşimi
  → Chapter: Aynı uzmanlıktaki kişilerin bilgi paylaşımı

Newman'ın uyarısı geçerli:
  → Spotify modeli HER şirkete UYUMAZ
  → Spotify'ın kendisi bile modeli değiştirdi (2020+)
  → "Spotify Model" kopyalamak = Cargo Cult
```

### Getir — Monolith → Microservices Yolculuğu

```
Hızlı büyüyen startup'larda tipik yol:
  → Başlangıç: Monolith (hızlı geliştir, markete çık)
  → Büyüme: Darboğazlar ortaya çıkar (ölçekleme, deploy hızı)
  → Geçiş: Strangler Fig ile parça parça ayır
  → Olgunluk: Event-driven + microservices hibrit

Newman'ın tavsiyesi tam buna uyar:
  → "Monolith first"
  → Domain'i ANLA, sonra ayır
  → YANLIŞ yerde ayırırsan → distributed monolith olur
```

---

## 20. 🤖 Yapay Zeka Çağında Microservices

### AI ve Microservices: Yeni Zorluklar

```
AI/ML servisleri microservice dünyasına YENİ zorluklar getiriyor:

  1. MODEL SERVING:
     → ML modeli bir microservice olarak deploy edilir
     → Ama modeller BÜYÜK (GB'lar) → cold start problemi
     → Newman'ın "right-sizing" prensibi: Model servisi DAHA BÜYÜK olabilir

  2. FEATURE STORE:
     → ML feature'ları (eğitim verileri) nerede saklanacak?
     → Shared database anti-pattern MI?
     → Newman: "Feature store = paylaşılmış kütüphane gibi yönet"

  3. TRAINING vs INFERENCE:
     → Training: batch, uzun süreli, GPU gerekli
     → Inference: real-time, düşük gecikme, scale gerekli
     → İki FARKLI servis olarak tasarla

  4. DATA PIPELINE:
     → ETL/ELT işleri microservice olarak mı?
     → Newman'ın Saga pattern'ı burada da geçerli
     → Her adım (extract, transform, load) bağımsız servis
```

### AI ile Microservice Geliştirme Promptları

```
SERVİS TASARIMI:
  "Bu domain'i microservice'lere ayır.
   Sam Newman'ın Building Microservices kitabındaki prensipleri kullan:
   - Her servis tek bir Bounded Context'e ait olsun
   - Information Hiding: İç yapı dışarıya sızmasın
   - Bağımsız deploy edilebilir olsun
   - Database per service (shared DB YASAK)
   - API contract tanımla (OpenAPI/AsyncAPI)
   Domain: [domain açıklaması]"

SAGA PATTERN:
  "Bu iş akışını Saga pattern ile implemente et.
   Choreography-based mi Orchestration-based mı olmalı?
   Newman'ın kriterlerini kullan:
   - 3-4 adımdan fazla → Orchestration tercih et
   - Basit akış → Choreography yeterli
   - Her adım için compensating transaction tanımla
   İş akışı: [akış açıklaması]"

STRANGLER FIG MIGRATION:
  "Bu monolith fonksiyonaliteyi microservice'e taşı.
   Strangler Fig pattern kullan:
   1. Proxy katmanı ekle
   2. Yeni servise yönlendir
   3. Eski kodu kademeli olarak kaldır
   Her adımda geri dönüş (rollback) planı olsun."
```

### Topluluk Görüşleri

```
Sam Newman (2023 interview):
  "Microservices'in en büyük başarısızlık nedeni:
   Domain'i anlamadan servislere ayırmak.
   DDD olmadan microservices yapmayın."

Martin Fowler ("Microservices Prerequisites" makalesi):
  "Microservices'e başlamadan ÖNCE şunlar olmalı:
   - Rapid provisioning (dakikalar içinde sunucu)
   - Basic monitoring (her servis izlenebilir)
   - Rapid deployment (CI/CD pipeline)
   Bunlar YOKSA microservices yapma."

Kelsey Hightower (Google):
  "Monolith is the future. Hear me out:
   Modüler monolith + proper boundaries > 
   poorly designed microservices."

Reddit r/microservices'te en çok paylaşılan:
  "Newman'ın kitabını okumadan microservices'e başladık.
   Sonuç: Distributed monolith + network overhead + debugging nightmare.
   Keşke önce monolith'i düzgün yapıp, SONRA ayırsaydık."
```

---

## 21. �🎬 Son Sözler

### Newman'ın Altın Kuralları 🏆

| # | Kural | Açıklama |
|---|---|---|
| 1 | **Bağımsız deploy** | Bunu yapamıyorsan microservice DEĞİLSİN |
| 2 | **Domain bazlı modelleme** | Teknik değil, İŞ domain'i bazında ayır |
| 3 | **Monolith önce** | Domain'i anlamadan microservice'e geçme |
| 4 | **Strangler Fig** | Kademeli geçiş, büyük patlama DEĞİL |
| 5 | **Bilgi gizleme** | DB paylaşma, API üzerinden konuş |
| 6 | **Contract testing** | E2E yerine kontrat testi kullan |
| 7 | **Correlation ID** | Dağıtık izleme OLMAZSA OLMAZ |
| 8 | **Circuit Breaker** | Hata kaçınılmaz, hazırlan! |
| 9 | **You build it, you run it** | Servisi yazan, servisi işletir |
| 10 | **Her şey trade-off** | Microservices dahil! |

### Tüm Kitaplarla Bağlantı 🔗

```
📗 Grokking Algorithms → Algoritma bilgisi her serviste gerekli
📕 Clean Code → Her servis içinde temiz KOD yaz
📘 Pragmatic Programmer → DRY ama shared lib tuzağına düşme!
📙 Missing README → On-call kültürü = "you build it, you run it"
📗 Philosophy of Software Design → Deep modules = iyi servis tasarımı
📘 Design Patterns → Pattern'lar servis İÇİNDE kullanılır
📕 DDIA → Veri bölümleme, replikasyon, consistency = microservice DATA katmanı
📙 Unit Testing → Contract test, test piramidi = microservice test stratejisi
📗 Refactoring → Strangler Fig = büyük ölçekte refactoring
🏛️ Clean Architecture → DIP, boundaries = servis sınırları
🏗️ Fundamentals of SA → Mimari stiller karşılaştırma + trade-off düşüncesi
🔬 Building Microservices → UYGULAMA: "Tüm bilgileri dağıtık sistemde nasıl HAYATA geçirirsin?"

Bu kitap önceki tüm bilgilerin DAĞITIK DÜNYADA pratik uygulamasıdır.
→ Clean Code + Clean Architecture + DDIA + Testing + Refactoring
  hepsini microservices bağlamında BİRLEŞTİRİR.
```

### Faz 3 İlerleme Durumu 📊

```
FAZ 3 — Mimari & Ölçek (12-18 ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Clean Architecture              ✅
  2. Fundamentals of Software Arch   ✅
  3. Building Microservices          ✅  ← BURADASIN
  4. The Phoenix Project             ⬜
  5. System Design Interview Vol 1   ⬜
```

---

> **"Microservices, dağıtık sistemlerin TÜM zorluklarını
> kabul ettikten sonra yapılan BİLİNÇLİ bir seçimdir.
> Eğer bu zorlukları göze ALAMIYORSANIZ,
> eğer ekibiniz bu karmaşıklığı YÖNETEMİYORSA,
> eğer domain'inizi yeterince ANLAMADIYISANIZ:
> MONOLITH ile kalmak DOĞRU karardır.
> Microservices bir SON değil, bir ARAÇTIR.
> Ve her araç gibi, YANLIŞ kullanıldığında
> çözdüğünden DAHA FAZLA sorun yaratır."**
> — Sam Newman'ın ruhu
