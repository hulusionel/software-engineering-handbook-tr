# 🏗️ Fundamentals of Software Architecture — Türkçe Kapsamlı Rehber

> **"Her şey trade-off'tur.
> Mimarlar seçim yapmaz — trade-off yapar."**
> — Mark Richards & Neal Ford

Bu kitap, yazılım mimarisini bir **meslek** olarak ele alır.
Mimari stilleri karşılaştırır, mimarın rolünü tanımlar,
ve en önemlisi: **"Doğru cevap yok, sadece daha az yanlış trade-off var"**
mesajını verir. Uncle Bob'un Clean Architecture'ı "ne yapmalı" diyorsa,
bu kitap "hangi seçenekler var ve nasıl karar vermeliyim" der. 🧭

---

## 📖 İçindekiler

1. [Yazılım Mimarisi Nedir?](#1--yazılım-mimarisi-nedir)
2. [Mimari Düşünce](#2--mimari-düşünce)
3. [Modülerlik](#3--modülerlik)
4. [Mimari Karakteristikler (ilities)](#4--mimari-karakteristikler-ilities)
5. [Karakteristikleri Belirleme](#5--karakteristikleri-belirleme)
6. [Karakteristikleri Ölçme](#6--karakteristikleri-ölçme)
7. [Bileşen Tabanlı Düşünce](#7--bileşen-tabanlı-düşünce)
8. [Mimari Stiller — Temeller](#8--mimari-stiller--temeller)
9. [Layered Architecture](#9--layered-architecture)
10. [Pipeline Architecture](#10--pipeline-architecture)
11. [Microkernel Architecture](#11--microkernel-architecture)
12. [Service-Based Architecture](#12--service-based-architecture)
13. [Event-Driven Architecture](#13--event-driven-architecture)
14. [Space-Based Architecture](#14--space-based-architecture)
15. [Microservices Architecture](#15--microservices-architecture)
16. [Mimari Kararlar](#16--mimari-kararlar)
17. [Mimari Risk Analizi](#17--mimari-risk-analizi)
18. [Diyagramlar ve Sunum](#18--diyagramlar-ve-sunum)
19. [Ekip ve Liderlik](#19--ekip-ve-liderlik)
20. [Büyük Şirketlerde Mimari Kararlar](#20--büyük-şirketlerde-mimari-kararlar)
21. [Yapay Zeka Çağında Yazılım Mimarisi](#21--yapay-zeka-çağında-yazılım-mimarisi)
22. [Son Sözler](#22--son-sözler)

---

## 1. 🤔 Yazılım Mimarisi Nedir?

### Tanım: 4 Boyut

```
Yazılım mimarisi 4 şeyin BİRLEŞİMİDİR:

1. YAPI (Structure)
   → Mimari stil: monolith, microservices, serverless, vb.
   → "Sistem hangi parçalardan oluşuyor?"

2. MİMARİ KARAKTERİSTİKLER (Architecture Characteristics)
   → "ilities": scalability, availability, reliability, security...
   → "Sistem NASIL davranmalı?" (fonksiyonel olmayan gereksinimler)

3. MİMARİ KARARLAR (Architecture Decisions)
   → "Servisler arası sadece async iletişim kullanılacak"
   → KURALLAR ve KISITLAMALAR

4. TASARIM PRENSİPLERİ (Design Principles)
   → "Mümkünse async tercih edilmeli" (kural değil, REHBERLİK)
   → Daha yumuşak yönergeler

                   Mimari
                     │
        ┌────────────┼────────────┐──────────────┐
        │            │            │              │
     Yapı      Karakteristik   Kararlar      Prensipler
   (stil)      (ilities)       (kurallar)    (rehberlik)
```

### Mimar ≠ Geliştirici (Ama İkisi de Gerekli!)

```
GELİŞTİRİCİ:                    MİMAR:
  Kodu yazar ✅                   Yapıyı belirler ✅
  "NASIL" yapılır?               "NE" yapılmalı?
  Derinlik (bir alanda)          Genişlik (birçok alanda)
  Detaylara odaklanır            Trade-off'lara odaklanır
  Teknik borcu ÜRETIR            Teknik borcu YÖNETIR

AMA! Mimar kod yazmayı BIRAKMAMALI!
  → "Fildişi kule mimarı" = ekipten kopuk, gerçekçi olmayan kararlar
  → İyi mimar hâlâ KOD YAZAR (en azından spike, POC, code review)
  → "Breadth over depth" — geniş bilgi, seçili alanlarda derinlik
```

---

## 2. 🧠 Mimari Düşünce

### Teknik Derinlik vs Teknik Genişlik

```
        Bilgi
    ┌──────────────────────────────────┐
    │                                  │
    │  BİLDİĞİN (Things you know)     │ ← Derinlik
    │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
    │                                  │
    │  BİLDİĞİN AMA UNUTTUĞUN         │
    │  ░░░░░░░░░░░░░░░░░░░░░          │
    │                                  │
    │  BİLMEDİĞİNİ BİLDİĞİN          │ ← Genişlik!
    │  ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬  │
    │                                  │
    │  BİLMEDİĞİNİ BİLMEDİĞİN        │ ← TEHLİKE!
    │  ??????????????????????????????????│
    └──────────────────────────────────┘

Geliştirici: Derinlik artır → "Java'yı çok iyi biliyorum"
Mimar:       Genişlik artır → "Java, Go, Rust, Python'un
             trade-off'larını BİLİYORUM.
             Hangisini ne zaman kullanmalıyız?"

EN TEHLİKELİ alan: "Bilmediğini bilmediğin" şeyler!
  → "gRPC diye bir şey varmış, 3 ay önce bilseydim
     REST yerine bunu seçerdik!" 😱
  → GENİŞLİK bu alanı KÜÇÜLTÜR
```

### Her Şey Trade-off'tur! ⚖️

**Kitabın en önemli mesajı:**

```
Richards'ın İlk Yazılım Mimarisi Yasası:

    ╔════════════════════════════════════════╗
    ║ "Yazılım mimarisinde HER ŞEY          ║
    ║  bir trade-off'tur."                   ║
    ╚════════════════════════════════════════╝

Richards'ın İkinci Yasası:

    ╔════════════════════════════════════════╗
    ║ "NEDEN daha önemlidir, NASIL'dan."     ║
    ╚════════════════════════════════════════╝

Kötü mimar: "Microservices kullanalım" → NASIL
İyi mimar:  "Microservices kullanalım ÇÜNKÜ takımlar 
             bağımsız deploy edebilmeli ve her servisin 
             farklı ölçeklenme ihtiyacı var." → NEDEN

"Bir mimarın avantajsız bir trade-off keşfetmesi
 biraz şüpheyle karşılanmalıdır." 🤨
→ Her seçimin bir bedeli var. Bedeli göremiyorsan yeterince analiz ETMEMİŞSİNDİR.
```

**Analoji — Pizza Sipariş Trade-off'u:** 🍕

```
Evde pişir:
  ✅ Ucuz, istediğin malzeme
  ❌ Zaman, efor, bulaşık

Sipariş ver:
  ✅ Hızlı, kolay
  ❌ Pahalı, seçenek sınırlı

Restoranda ye:
  ✅ Atmosfer, servis
  ❌ En pahalı, bekleme süresi

→ "EN İYİ" pizza çözümü YOK. Duruma bağlı!
→ Mimari kararlar da AYNI!
```

---

## 3. 🧩 Modülerlik

### Modülerlik Neden Önemli?

```
Modülerlik = İlgili kodu mantıksal gruplara ayırma

Neden?
  → Anlaşılabilirlik: Parça parça düşünebilme
  → Sürdürülebilirlik: Bir parçayı değiştirmek diğerlerini ETKİLEMEMELİ
  → Test edilebilirlik: Parçaları izole test etme
  → Yeniden kullanım: Parçaları başka yerlerde kullanma

Modülerlik ölçütleri:
  1. Cohesion (Bağdaşıklık)
  2. Coupling (Bağlanma)
  3. Connascence (Birlikte Değişim)
```

### Cohesion (Bağdaşıklık) 🧲

```
"Bir modül içindeki elemanlar ne kadar İLGİLİ?"

YÜKSEK Cohesion = İYİ ✅
  → Modüldeki her şey BİRBİRİYLE İLGİLİ
  → UserService: createUser, findUser, updateUser, deleteUser
  → Hepsi "user" ile ilgili — UYUMLU!

DÜŞÜK Cohesion = KÖTÜ ❌
  → Modüldeki şeyler BİRBİRİYLE İLGİSİZ
  → HelperService: sendEmail, calculateTax, formatDate, resizeImage
  → Birbirleriyle ALAKASI YOK — "çöp çekmecesi" modülü!

Cohesion Tipleri (iyiden kötüye):
  1. Functional   → Tek bir işlevi gerçekleştirmek için birlikte çalışır ✅✅✅
  2. Sequential   → Bir fonksiyonun çıktısı diğerinin girdisi ✅✅
  3. Communicational → Aynı veriyi kullanır ✅
  4. Procedural   → Belirli sırayla çalışır 😐
  5. Temporal     → Aynı zamanda çalışır 😐
  6. Logical      → Kategorik olarak ilgili ama fonksiyonel bağ yok ❌
  7. Coincidental → Hiçbir ilgi yok, tesadüfen aynı modülde ❌❌❌

HEDEF: Functional cohesion!
```

### Coupling (Bağlanma) 🔗

```
"Modüller birbirlerine ne kadar BAĞIMLI?"

DÜŞÜK Coupling = İYİ ✅
  → Bir modülü değiştirmek diğerlerini ETKİLEMEZ
  → PaymentService değişti → OrderService ETKİLENMEDİ ✅

YÜKSEK Coupling = KÖTÜ ❌
  → Bir modülü değiştirmek zincirleme etki yaratır
  → PaymentService değişti → OrderService → NotificationService → ... 💥

İdeal: "Yüksek cohesion, düşük coupling"
  → İçeride SIKICA bağlı (cohesion)
  → Dışarıya GEVŞEK bağlı (coupling)
```

### Connascence (Birlikte Değişim)

```
İki bileşen arasındaki BAĞIMLILIK ŞEKLİ:

Statik Connascence (kaynak kodda):
  CoN (Name)      → İsim değişirse diğeri de değişmeli
  CoT (Type)      → Tip değişirse diğeri de değişmeli
  CoM (Meaning)   → "1 = admin, 2 = user" — anlam paylaşımı
  CoP (Position)  → Parametre sırası önemli
  CoA (Algorithm) → Aynı algoritmayı kullanmak zorunda (hash fonksiyonu gibi)

Dinamik Connascence (çalışma zamanında):
  CoE (Execution) → Çalışma sırası önemli
  CoT (Timing)    → Zamanlama önemli (race condition!)
  CoV (Values)    → Birlikte değişmesi gereken değerler (DB transaction)
  CoI (Identity)  → Aynı nesneyi referans etmek zorunda

KURAL:
  1. Dinamik connascence'ı AZALT (zor debug)
  2. Statik connascence'ı TERCİH ET (IDE anlar, compile-time hata)
  3. Connascence'ı modül İÇİNE çek (dışa sızmamalı)
```

---

## 4. 📊 Mimari Karakteristikler (ilities)

### "-ilities" Nedir?

```
Sistem NE yapar? → Fonksiyonel gereksinimler
  "Kullanıcı giriş yapabilmeli"
  "Sipariş oluşturabilmeli"

Sistem NASIL yapmalı? → Mimari Karakteristikler (Non-functional)
  "1000 kullanıcı aynı anda giriş yapabilmeli" → Scalability
  "Giriş 200ms'den uzun sürmemeli" → Performance
  "%99.99 uptime" → Availability
  "Bir servis çökerse sistem çalışmaya devam etmeli" → Fault Tolerance

MİMAR bunlarla ilgilenir!
Geliştirici: "Giriş yapabilmeli" ← fonksiyon yazma
Mimar: "1000 kişi aynı anda giriş yapabilmeli" ← sistem tasarımı
```

### Temel Karakteristikler Kataloğu

```
┌─────────────────────────────────────────────────────────────────────┐
│ KATEGORİ           │ KARAKTERİSTİK        │ AÇIKLAMA               │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Operasyonel         │ Availability         │ Çalışma süresi (%99.9) │
│                     │ Performance          │ Yanıt süresi (latency)  │
│                     │ Scalability          │ Yük artışına dayanma    │
│                     │ Elasticity           │ Ani yük artışına adapte │
│                     │ Reliability          │ Hatasız çalışma         │
│                     │ Recoverability       │ Hatadan kurtulma hızı   │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Yapısal             │ Modularity           │ Parçalara ayrılabilirlik│
│                     │ Extensibility        │ Yeni özellik ekleme     │
│                     │ Maintainability      │ Bakım ve güncelleme     │
│                     │ Deployability        │ Deploy kolaylığı        │
│                     │ Testability          │ Test edilebilirlik      │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Cross-Cutting       │ Security             │ Güvenlik                │
│                     │ Observability        │ İzlenebilirlik          │
│                     │ Interoperability     │ Sistemler arası uyum    │
│                     │ Accessibility        │ Erişilebilirlik         │
│                     │ Agility              │ Hızlı değişim yeteneği  │
└─────────────────────┴──────────────────────┴────────────────────────┘
```

### Trade-off Gerçeği: Hepsini Seçemezsin!

```
KURAL: Mimari karakteristik SAYISINI MİNİMİZE ET!

Neden?
  → Her karakteristik MALİYET ekler (karmaşıklık, zaman, para)
  → Bazıları birbiriyle ÇELİŞİR!

Çelişki örnekleri:

  Performance ←→ Security
    Şifreleme performansı düşürür

  Scalability ←→ Simplicity
    Ölçeklenme mekanizmaları karmaşıklık ekler

  Availability ←→ Cost
    %99.99 → PAHALIIIII 💸

  Flexibility ←→ Performance
    Soyutlama katmanları = ekstra maliyet

KURAL: En fazla 3-7 kritik karakteristik seç!
  "Hepsini" istersen HİÇBİRİNİ iyi yapamazsın.

  ┌─────────────────────────────────────────┐
  │         "Hızlı, ucuz, kaliteli.         │
  │          İkisini seç."                  │
  │              — Anonim                   │
  └─────────────────────────────────────────┘
```

---

## 5. 🔍 Karakteristikleri Belirleme

### Nereden Gelir?

```
Mimari karakteristikler 3 kaynaktan gelir:

1. DOMAIN endişelerinden  →  İş bağlamı
2. GEREKSİNİMLERDEN       →  Açıkça belirtilen
3. ÖRTülü bilgiden         →  Belirtilmese de gerekli

Örnek: Online eğitim platformu
  Domain: "Sınav zamanlarında çok yük oluyor" → Elasticity
  Gereksinim: "Aynı anda 10K öğrenci sınava girebilmeli" → Scalability
  Örtülü: "Sınav sonuçları DOĞRU olmalı" → Data Integrity (kimse söylemedi ama ŞART!)
```

### Domain Endişesi → Karakteristik Eşleştirme

```
┌─────────────────────────┬──────────────────────────────────┐
│ Domain Endişesi          │ Mimari Karakteristik              │
├─────────────────────────┼──────────────────────────────────┤
│ "Müşteri kaybetmeyelim"  │ Availability, Fault Tolerance    │
│ "Hızlı büyüyoruz"       │ Scalability, Elasticity          │
│ "Yasal uyumluluk"        │ Security, Auditability           │
│ "Birleşme/satın alma"    │ Interoperability, Extensibility  │
│ "Pazar zamanı kritik"    │ Agility, Deployability           │
│ "Bütçe kısıtlı"         │ Simplicity, Feasibility          │
│ "Küresel kullanıcılar"   │ Performance, Internationalization│
│ "Kısa süreli kampanyalar"│ Elasticity, Scalability          │
└─────────────────────────┴──────────────────────────────────┘

UYARI: Her endişe birden fazla karakteristiğe MAP olabilir!
Mimar, HANGİSİNİN daha kritik olduğunu KARAR VERIR.
```

---

## 6. 📏 Karakteristikleri Ölçme

### Fitness Functions 🏋️

```
"Mimari karakteristiklerin TESTLER gibi ÖLÇÜLEBILIR olması gerekir!"

Fitness Function = Mimari kararlarımızın doğruluğunu 
                   ÖLÇEN otomatik test/metrik

Örnekler:

  Performans fitness function:
    → "Her API endpoint 200ms'nin altında yanıt vermeli"
    → CI/CD'de load test ile kontrol

  Modülerlik fitness function:
    → "Hiçbir modül X'ten fazla import etmemeli"
    → Lint kuralı ile kontrol

  Bağımlılık fitness function:
    → "domain/ katmanı infrastructure/'a ASLA import etmemeli"
    → ArchUnit/dependency-cruiser ile kontrol
```

```javascript
// Dependency fitness function örneği (dependency-cruiser config)
// .dependency-cruiser.js

module.exports = {
  forbidden: [
    {
      name: 'domain-cannot-import-infrastructure',
      comment: 'Domain katmanı altyapıya bağımlı olamaz (Clean Architecture)',
      severity: 'error',
      from: { path: '^src/domain' },
      to: { path: '^src/infrastructure' },
    },
    {
      name: 'no-circular-dependencies',
      comment: 'Döngüsel bağımlılık yasak',
      severity: 'error',
      from: {},
      to: { circular: true },
    },
  ],
};

// CI'da otomatik çalışır → mimari bozulursa build KIRILIR! 🛡️
```

```javascript
// Performans fitness function (integration test)
test('sipariş oluşturma 200ms altında olmalı', async () => {
  const start = Date.now();

  await request(app)
    .post('/orders')
    .send({ userId: 'user-1', items: [{ productId: 'p1', quantity: 1 }] });

  const elapsed = Date.now() - start;
  expect(elapsed).toBeLessThan(200); // 200ms limiti ✅
});
```

### Governance Mekanizmaları

```
Fitness function'lar nasıl uygulanır?

1. CI/CD Pipeline'da (Otomatik) ⚙️
   → Dependency check, load test, lint kuralları
   → Build kırılır → merge ENGELLENIR

2. Code Review'da (Yarı Otomatik) 👀
   → Mimar PR'ı inceler
   → "Bu değişiklik performansı etkiler mi?"

3. Architecture Decision Records — ADR (Manuel) 📝
   → Mimari kararları BELGELEME
   → "Neden X yerine Y seçtik?"
   → ileride BAKIP anlayabilme
```

---

## 7. 📦 Bileşen Tabanlı Düşünce

### Bileşen Nedir?

```
Bileşen = Fiziksel olarak paketlenmiş MODÜL

  Java: JAR dosyası
  Node.js: npm paketi veya klasör modülü
  .NET: Assembly

Bileşen, mimari ile sınıf arasındaki katmandır:
  Mimari → Bileşenler → Sınıflar/Fonksiyonlar

Mimar bileşenlerle düşünür:
  "Sipariş bileşeni hangi diğer bileşenlere bağımlı?"
  "Ödeme bileşenini bağımsız deploy edebilir miyiz?"
```

### Top-Down vs Bottom-Up Bileşen Tespiti

```
TOP-DOWN (Yukarıdan):
  1. Domain'e bak → Alt domain'leri belirle
  2. Her alt domain = bir bileşen adayı
  3. Bileşenler arası ilişkileri çiz
  4. Detaylandır

  "Sigorta sistemi" →
    Poliçe Yönetimi,
    Hasar Yönetimi,
    Müşteri Yönetimi,
    Ödeme Yönetimi

BOTTOM-UP (Aşağıdan):
  1. Mevcut koda bak
  2. İlişkili sınıfları grupla
  3. Gruplardan bileşenler oluştur
  4. Gereksiz bağımlılıkları kes

HER İKİSİ DE KULLANILIR:
  Sıfırdan → Top-Down
  Mevcut sistem → Bottom-Up (refactoring)
```

### Entity Trap ⚠️

```
TUZAK: Bileşenleri entity'lere göre oluşturma!

  ❌ Entity-based components:
    UserComponent
    OrderComponent
    ProductComponent
    PaymentComponent

  Bunlar CRUD container olur sadece!
  İŞ AKIŞLARI bileşenler arasına DAĞILIR.
  "Sipariş oluşturma" → Order + Product + Payment + User = 4 bileşen birden!

  ✅ Workflow-based components:
    CreateOrderWorkflow
    ProcessPaymentWorkflow
    CustomerOnboarding
    InventoryManagement

  İş akışı bir bileşende KAPALI kalır.
  Daha az bileşen arası iletişim = daha düşük coupling!

Bu, DDD'deki Bounded Context'e benzer.
→ "İş kapasitesi" bazında düşün, "veri varlığı" bazında DEĞİL!
```

---

## 8. 🏛️ Mimari Stiller — Temeller

### Monolithik vs Dağıtık

```
TÜM mimari stiller 2 ana gruba ayrılır:

MONOLITHIK (Tek Birim):
  → Tüm kod tek bir deploy birimi
  → Layered, Pipeline, Microkernel
  → Basit, ucuz, ama ölçeklenmesi zor

DAĞITIK (Distributed):
  → Kod farklı servislere/node'lara ayrılmış
  → SOA, Event-Driven, Microservices, Space-Based
  → Ölçeklenebilir, ama KARMAŞIK

"Dağıtık sistem kullanma, MECBUR kalmadıkça!"
→ Dağıtık = her şey DAHA ZOR
```

### Dağıtık Sistemlerin 8 Yanılgısı 🎭

```
Peter Deutsch + James Gosling'in meşhur listesi:

1. "Ağ GÜVENİLİRDİR"
   → HAYIR! Paketler kaybolur, timeout olur, bağlantı kopar.
   → Circuit breaker, retry, fallback GEREKİR!

2. "Gecikme SIFIRDIR"
   → HAYIR! Fonksiyon çağrısı: nanosaniye. HTTP çağrısı: MİLİSANİYE!
   → 10 servis × 50ms = 500ms! Zincirleme gecikme BÜYÜR.

3. "Bant genişliği SONSUZ"
   → HAYIR! Büyük payload'lar ağı tıkar.
   → Pagination, compression, protobuf vs JSON karar ver.

4. "Ağ GÜVENLİDİR"
   → HAYIR! Her servis sınırı = potansiyel saldırı yüzeyi.
   → mTLS, auth token, network policy GEREKİR.

5. "Topoloji DEĞİŞMEZ"
   → HAYIR! Sunucular eklenir/kaldırılır, IP değişir.
   → Service discovery (Consul, K8s DNS) GEREKİR.

6. "TEK yönetici var"
   → HAYIR! Farklı takımlar farklı servisleri yönetir.
   → Standartlar, governance, kontratlar GEREKİR.

7. "Taşıma maliyeti SIFIR"
   → HAYIR! Serialization/deserialization CPU tüketir.
   → JSON vs Protobuf vs Avro trade-off!

8. "Ağ HOMOJENDİR"
   → HAYIR! Farklı network donanımları, farklı davranışlar.
   → Test ve izleme ŞART.

Bu 8 yanılgıyı BİLMEDEN microservices yapma!
Her biri bir MİMARİ karar GEREKTİRİR.
```

---

## 9. 🎂 Layered Architecture

### En Yaygın Stil

```
┌──────────────────────────────────┐
│        Presentation              │  UI / API
├──────────────────────────────────┤
│        Business Logic            │  İş kuralları
├──────────────────────────────────┤
│        Persistence               │  Veritabanı erişimi
├──────────────────────────────────┤
│        Database                  │  Veritabanı
└──────────────────────────────────┘

Her katman sadece ALTINDAKİ katmanla konuşur.
Basit, herkesçe bilinen, hızlı başlanır.
```

### Sinkhole Anti-Pattern 🕳️

```
Bir request katmanlardan geçiyor ama HİÇBİR katman
gerçek bir iş YAPMIYOR — sadece aşağı geçiriyor!

  Request → Controller → Service → Repository → DB
  Controller: req.body'yi service'e VER
  Service: aynısını repository'ye VER
  Repository: DB'den al, GERI VER

  → 🕳️ Sinkhole! Orta katmanlar sadece "pass-through"!
  → Eğer request'lerin %80'inden fazlası sinkhole ise →
    YANLIŞ mimari seçmişsindir!

UYARI: %20-30 sinkhole NORMAL! Her request iş mantığı gerektirmez.
  Sorun: %80+ sinkhole = gereksiz katman karmaşıklığı
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Deployability       │ ⭐      │  → Tüm sistemi deploy etmek ZORUNLU
│ Testability         │ ⭐⭐    │  → Katmanlar test edilebilir AMA izolasyon zor
│ Scalability         │ ⭐      │  → Tüm katmanlar birlikte ölçeklenir
│ Performance         │ ⭐⭐    │  → Katmanlar arası overhead
│ Fault Tolerance     │ ⭐      │  → Bir katman çökerse HER ŞEY çöker
│ Overall Cost        │ ⭐⭐⭐⭐⭐│  → Ucuz! Basit!
│ Simplicity          │ ⭐⭐⭐⭐⭐│  → En basit mimari
└─────────────────────┴─────────┘

Ne zaman kullan?
  ✅ Küçük/orta projeler, tek takım
  ✅ Hızlı başlamak gerektiğinde
  ❌ Yüksek ölçeklenme gerektiğinde
  ❌ Bağımsız deploy gerektiğinde
```

---

## 10. 🔧 Pipeline Architecture

### Unix Pipes Felsefesi

```
Unix: ls | grep ".js" | sort | head -5

Her adım:
  → Girdi alır → İşler → Çıktı verir
  → Sonraki adıma bağımlı DEĞİL
  → Bağımsız test edilebilir

Pipeline Architecture = Aynı mantık, yazılımda!

  Filter → Filter → Filter → Filter
    │         │         │         │
    ↓         ↓         ↓         ↓
  [Pipe]   [Pipe]   [Pipe]   [Pipe]
```

```javascript
// Pipeline Architecture örneği: Sipariş işleme

// Filtreler (her biri bağımsız, tek sorumluluk)
const validateOrder = (order) => {
  if (!order.items.length) throw new Error('Boş sipariş');
  return order;
};

const calculateTotals = (order) => ({
  ...order,
  subtotal: order.items.reduce((s, i) => s + i.price * i.quantity, 0),
});

const applyDiscounts = (order) => ({
  ...order,
  total: order.subtotal > 1000 ? order.subtotal * 0.95 : order.subtotal,
});

const addTax = (order) => ({
  ...order,
  totalWithTax: order.total * 1.18,
});

// Pipeline (compose)
const processOrder = pipe(
  validateOrder,
  calculateTotals,
  applyDiscounts,
  addTax,
);

// pipe utility
function pipe(...fns) {
  return (input) => fns.reduce((result, fn) => fn(result), input);
}

const result = processOrder({ items: [{ price: 500, quantity: 3 }] });
// Her adım TEST EDİLEBİLİR, bağımsız, tek sorumluluk! ✅
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Simplicity          │ ⭐⭐⭐⭐⭐│  → Çok basit konsept
│ Testability         │ ⭐⭐⭐⭐⭐│  → Her filtre izole test edilir
│ Modularity          │ ⭐⭐⭐⭐  │  → Filtreler bağımsız
│ Scalability         │ ⭐      │  → Monolithik, ölçeklenmesi zor
│ Fault Tolerance     │ ⭐      │  → Tek process
└─────────────────────┴─────────┘

Ne zaman kullan?
  ✅ ETL, veri dönüştürme, rapor oluşturma
  ✅ Compiler/interpreter pipeline'ları
  ❌ Karmaşık iş mantığı
  ❌ Yüksek ölçeklenme
```

---

## 11. 🔌 Microkernel Architecture

### Plugin Mimarisi

```
┌────────────────────────────────────────┐
│              CORE SYSTEM               │
│    (minimal, kararlı, nadiren değişir) │
│                                        │
│    ┌──────┐  ┌──────┐  ┌──────┐       │
│    │Plugin│  │Plugin│  │Plugin│       │
│    │  A   │  │  B   │  │  C   │       │
│    └──────┘  └──────┘  └──────┘       │
└────────────────────────────────────────┘

Core: Temel iş mantığı (değişmez)
Plugin'ler: Özelleştirmeler (bağımsız eklenir/kaldırılır)

Gerçek dünya örnekleri:
  → VS Code: Core editor + extensions (plugin!)
  → Eclipse, IntelliJ
  → Chrome: Browser + extensions
  → Webpack: Core + loaders + plugins
```

```javascript
// Microkernel örneği: Vergi hesaplama motoru

// CORE — sabit, kararlı
class TaxEngine {
  #plugins = new Map();

  registerPlugin(countryCode, plugin) {
    this.#plugins.set(countryCode, plugin);
  }

  calculateTax(order, countryCode) {
    const plugin = this.#plugins.get(countryCode);
    if (!plugin) throw new Error(`${countryCode} için vergi plugin'i bulunamadı`);
    return plugin.calculate(order);
  }
}

// PLUGIN'LER — bağımsız, eklenip çıkarılabilir
class TurkeyTaxPlugin {
  calculate(order) {
    return { kdv: order.total * 0.20, otv: 0 }; // %20 KDV
  }
}

class GermanyTaxPlugin {
  calculate(order) {
    return { mwst: order.total * 0.19 }; // %19 MwSt
  }
}

class USATaxPlugin {
  calculate(order) {
    const stateTax = this.#getStateTaxRate(order.state);
    return { salesTax: order.total * stateTax };
  }
}

// Kullanım
const engine = new TaxEngine();
engine.registerPlugin('TR', new TurkeyTaxPlugin());
engine.registerPlugin('DE', new GermanyTaxPlugin());
engine.registerPlugin('US', new USATaxPlugin());

// Yeni ülke? Yeni plugin yaz, core'a DOKUNMA! ✅ (OCP)
engine.registerPlugin('FR', new FranceTaxPlugin());
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Extensibility       │ ⭐⭐⭐⭐⭐│  → Plugin ekle, core değiştirme!
│ Testability         │ ⭐⭐⭐⭐⭐│  → Plugin'ler izole test edilir
│ Deployability       │ ⭐⭐⭐   │  → Plugin bağımsız deploy edilebilir
│ Simplicity          │ ⭐⭐⭐⭐  │  → Konsept basit
│ Scalability         │ ⭐⭐    │  → Monolithik core
│ Fault Tolerance     │ ⭐⭐    │  → Plugin çökerse etkisi sınırlı
└─────────────────────┴─────────┘
```

---

## 12. 🏢 Service-Based Architecture

### Microservices'in Pragmatik Kuzeni

```
"Microservices çok karmaşık! Monolith çok sıkışık!
 Ortası yok mu?" → SBA! 🎯

  Service-Based Architecture (SBA):
    → 4-12 arası "büyük" servis (domain service)
    → Ortak bir veritabanı PAYLAŞILIR (genellikle)
    → Microservices kadar granüler DEĞİL
    → Monolith kadar sıkışık DEĞİL

  ┌───────────────────────────────────────┐
  │            User Interface             │
  ├────────┬────────┬────────┬────────────┤
  │ Sipariş│ Ödeme  │ Envanter│ Müşteri   │
  │ Servisi│ Servisi│ Servisi │ Servisi   │
  ├────────┴────────┴────────┴────────────┤
  │           Ortak Veritabanı             │
  └───────────────────────────────────────┘

  vs Microservices:
  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │Sipariş │ │ Ödeme  │ │Envanter│ │Müşteri │
  │ Svc    │ │ Svc    │ │ Svc    │ │ Svc    │
  │  DB    │ │  DB    │ │  DB    │ │  DB    │
  └────────┘ └────────┘ └────────┘ └────────┘
  Her servisin KENDİ DB'si var!
```

### SBA vs Microservices Trade-off

```
┌──────────────────┬──────────────────┬──────────────────┐
│                  │ Service-Based     │ Microservices    │
├──────────────────┼──────────────────┼──────────────────┤
│ Servis sayısı    │ 4-12              │ 10-100+          │
│ Servis boyutu    │ Büyük (domain)    │ Küçük (fonksiyon)│
│ Veritabanı       │ Genellikle ortak  │ Her servisin kendi│
│ Karmaşıklık      │ Orta              │ Yüksek           │
│ İletişim         │ Basit (REST)      │ Karmaşık (saga)  │
│ Deploy           │ Servis bazında    │ Servis bazında   │
│ Transaction      │ ACID mümkün!      │ Saga gerekli     │
│ Maliyet          │ Düşük-Orta        │ Yüksek           │
│ Ekip boyutu      │ Küçük-orta        │ Büyük            │
└──────────────────┴──────────────────┴──────────────────┘

MESAJ: Çoğu şirket için SBA YETERLİ! 
Microservices'e "hype" yüzünden değil, GERÇEK ihtiyaç varsa geç.
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Deployability       │ ⭐⭐⭐⭐  │  → Servis bazında deploy
│ Testability         │ ⭐⭐⭐⭐  │  → Servis izole test edilir
│ Scalability         │ ⭐⭐⭐   │  → Servis bazında ölçekleme
│ Fault Tolerance     │ ⭐⭐⭐⭐  │  → Bir servis çökse diğerleri yaşar
│ Simplicity          │ ⭐⭐⭐   │  → Microservices'ten basit
│ Overall Cost        │ ⭐⭐⭐⭐  │  → Microservices'ten ucuz
└─────────────────────┴─────────┘
```

---

## 13. ⚡ Event-Driven Architecture

### İki Topoloji

```
EDA iki temel topolojiye sahip:

1. BROKER Topolojisi (Koreografi)
   → Merkezi orkestratör YOK
   → Event'ler yayınlanır, ilgilenen dinler
   → Her servis kendi kararını verir
   → Loosely coupled AMA akışı takip etmek ZOR

2. MEDIATOR Topolojisi (Orkestrasyon)
   → Merkezi bir mediator event akışını YÖNETİR
   → "Sipariş oluşturuldu → stok kontrol → ödeme al → kargola"
   → Akışı takip etmek KOLAY AMA single point of failure
```

### Broker Topolojisi (Koreografi) 💃

```
Olay: "Sipariş Oluşturuldu"

  [Order Service] → publishes → "order.created"
                                      │
                    ┌─────────────────┼─────────────────┐
                    ↓                 ↓                 ↓
              [Stok Service]    [Ödeme Service]   [Bildirim Svc]
              "stok.reserved"   "payment.done"    "email.sent"
                    │
                    ↓
              [Kargo Service]
              "shipment.created"

  HER servis:
    1. Event'i DİNLER
    2. İŞİNİ yapar
    3. Yeni event YAYINLAR
    4. Diğer servisleri BİLMEZ

  ✅ Çok loosely coupled
  ✅ Yeni servis eklemek kolay (sadece event'i dinle)
  ❌ Akış nereden nereye gidiyor? DEBUG ZOR!
  ❌ Hata durumunda ne olur? Compensation mantığı KARMAŞIK!
```

### Mediator Topolojisi (Orkestrasyon) 🎼

```
  [Order Service] → "order.created" → [Mediator]
                                          │
                                          ├→ [Stok Service]: "stok kontrol et"
                                          │      ↓ "stok tamam"
                                          ├→ [Ödeme Service]: "ödeme al"
                                          │      ↓ "ödeme tamam"
                                          ├→ [Kargo Service]: "kargola"
                                          │      ↓ "kargolama tamam"
                                          └→ [Bildirim Svc]: "müşteriye haber ver"

  Mediator TÜM akışı bilir ve yönetir.

  ✅ Akış net, takip edilebilir
  ✅ Hata yönetimi merkezi
  ❌ Mediator = single point of failure
  ❌ Servisler mediator'a bağlı (tighter coupling)
```

### Async vs Request-Reply

```
ASENKRON (fire-and-forget):
  Servis A → Event → Queue → Servis B
  A beklemez, devam eder. B ne zaman işlerse işler.
  ✅ Performans (A bloklanmaz)
  ❌ "İşlem tamam mı?" sorusunun cevabı YOK (hemen)

REQUEST-REPLY (Async ama cevap bekle):
  Servis A → Request → Queue → Servis B → Reply → Queue → Servis A
  A bekler AMA async queue üzerinden. Timeout gerekli!
  ✅ Cevapla ilgilenebilirsin
  ❌ Daha karmaşık, timeout yönetimi

SENKRON (HTTP):
  Servis A → HTTP → Servis B → HTTP Response → Servis A
  A bloklanır, bekler.
  ✅ Basit, bilinen pattern
  ❌ Tight temporal coupling (B çöktüyse A da çöker!)
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Scalability         │ ⭐⭐⭐⭐⭐│  → Event queue ile yük dengeleme
│ Performance         │ ⭐⭐⭐⭐⭐│  → Async, non-blocking
│ Fault Tolerance     │ ⭐⭐⭐⭐⭐│  → Queue buffer, retry
│ Evolvability        │ ⭐⭐⭐⭐⭐│  → Yeni consumer ekle, producer'a dokunma
│ Simplicity          │ ⭐      │  → Async düşünce ZORDUR!
│ Testability         │ ⭐⭐    │  → Async test etmek zor
│ Overall Cost        │ ⭐⭐    │  → Message broker altyapısı gerekir
└─────────────────────┴─────────┘

Ne zaman kullan?
  ✅ Yüksek ölçeklenme ve performans
  ✅ Loosely coupled servisler
  ✅ Eventual consistency kabul edilebilir
  ❌ Basit CRUD
  ❌ Strong consistency şart
```

---

## 14. 🌌 Space-Based Architecture

### Elastik Ölçeklenme

```
Sorun: Veritabanı DARBOĞAZ!
  10K istek/saniye → App server OK → DB ÇÖKTÜ! 💥

Çözüm: Veritabanını denklemden ÇIKAR (kısmen)!

Space-Based Architecture:
  → Veriyi IN-MEMORY tut (her instance'ta)
  → Instance'lar arası REPLIKASYON
  → Veritabanı sadece YEDEK (async yazılır)
  → Sınırsız instance eklenebilir!

  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │Processing│  │Processing│  │Processing│
  │  Unit    │  │  Unit    │  │  Unit    │
  │ ┌──────┐ │  │ ┌──────┐ │  │ ┌──────┐ │
  │ │In-Mem│ │  │ │In-Mem│ │  │ │In-Mem│ │
  │ │ Grid │◄├──├─┤ Grid │◄├──├─┤ Grid │ │
  │ └──────┘ │  │ └──────┘ │  │ └──────┘ │
  └────┬─────┘  └────┬─────┘  └────┬─────┘
       │              │              │
       └──────────────┼──────────────┘
                      │ (async write)
                ┌─────┴─────┐
                │ Database  │ (backup only)
                └───────────┘
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Scalability         │ ⭐⭐⭐⭐⭐│  → Instance ekle, kapasiteyi artır
│ Elasticity          │ ⭐⭐⭐⭐⭐│  → Ani yüke anında uyum
│ Performance         │ ⭐⭐⭐⭐⭐│  → In-memory = çok hızlı
│ Simplicity          │ ⭐      │  → EN karmaşık mimari!
│ Testability         │ ⭐      │  → Grid replikasyonu test etmek çok zor
│ Overall Cost        │ ⭐      │  → Bellek ve altyapı = PAHALI 💰
└─────────────────────┴─────────┘

Ne zaman kullan?
  ✅ Çok yüksek hacimli, ani yük (bilet satışı, flash sale)
  ✅ Düşük latency şart
  ❌ Çoğu proje için FAZLA!
```

---

## 15. 🔬 Microservices Architecture

### Temel İlkeler

```
Microservice mimarisinin TEMEL ilkeleri:

1. SINGLE PURPOSE (Tek Amaç)
   → Her servis TEK bir iş yapar
   → "Sipariş servisi" sadece sipariş yönetir

2. BAĞIMSIZ DEPLOY
   → Her servis BAĞIMSIZ deploy edilir
   → Servis A deploy edilirken B ETKİLENMEZ

3. VERİ İZOLASYONU
   → Her servis KENDİ veritabanına sahip
   → Başka servisin DB'sine DOĞRUDAN erişim YASAK!

4. BOUNDED CONTEXT (DDD)
   → Her servis bir domain bağlamını TEMSİL eder
   → "Sipariş" ve "Envanter" farklı bağlamlar

5. BAĞIMSIZ TAKIMLAR
   → Bir servis = bir takım (idealde)
   → Conway's Law: "Sistem, onu üreten organizasyonun
      iletişim yapısını yansıtır"
```

### Granülerlik — Ne Kadar Küçük?

```
Her şeyin trade-off olduğunu hatırla!

ÇOK KÜÇÜK servisler:
  ❌ Çok fazla network call
  ❌ Transaction yönetimi çok karmaşık
  ❌ Veri tutarlılığı problemi
  ❌ Operational overhead (deploy, monitor, debug)

ÇOK BÜYÜK servisler:
  ❌ Bağımsız deploy avantajı kaybolur
  ❌ Monolith'e geri dönüş
  ❌ Farklı takımlar aynı serviste çalışır → çakışma

DOĞRU boyut nasıl bulunur?
  1. İş kapası (business capability) bazında ayır
  2. Ekip bazında ayır (2-pizza rule: 1 servis = 1 pizza team)
  3. "Bu servisi 2 haftada yeniden yazabilir miyim?" testi
  4. Veri bağımlılığına bak: çok fazla join → muhtemelen aynı servis

Sam Newman: "Monolith ile başla, sınırları anladıktan sonra ayır."
```

### İletişim Stilleri

```
SENKRON:
  REST / gRPC
  → Basit, anlaşılır
  → Temporal coupling: "B çöktüyse A çalışamaz!"
  → Zincir: A → B → C → D (her biri bekler → yavaş!)

ASENKRON:
  Message Queue (RabbitMQ, Kafka)
  → Loose coupling: "B çökse bile A çalışır, mesaj kuyrukta bekler"
  → Karmaşıklık: eventual consistency, idempotency, ordering

KOREOGRAFI vs ORKESTRASYON:
  Koreografi: Her servis ne yapacağını BİLİR (event-driven)
  Orkestrasyon: Merkezi bir servis (saga orchestrator) YÖNETIR

SAĞ SEÇ:
  Basit akış + 2-3 servis → Senkron REST
  Karmaşık akış + 5+ servis → Asenkron + Saga
  Yüksek throughput → Asenkron + Event streaming (Kafka)
```

### Saga Pattern 📜

```
Dağıtık transaction nasıl yönetilir?

Monolith:  BEGIN → INSERT order → INSERT payment → COMMIT ✅

Microservice: DB'ler FARKLI. ACID transaction YOKTUR!

Saga: Compensating transactions (telafi işlemleri)

  1. Order Service: Sipariş oluştur → "order.created"
  2. Payment Service: Ödeme al → "payment.completed"
  3. Inventory Service: Stok azalt → "stock.reserved"
  4. Shipping Service: Kargo oluştur → "shipment.created"

  HATA DURUMUNDA (3. adımda stok yok!):
  ← Payment Service: Ödemeyi İADE ET (compensate)
  ← Order Service: Siparişi İPTAL ET (compensate)

  HER ADIMIN bir "geri alma" adımı OLMALI!
  → Bu karmaşık! AMA dağıtık sistemde ZORUNLU.
```

### Sidecar ve Service Mesh 🛡️

```
Cross-cutting concern'ler her serviste tekrar?
  → Logging, tracing, auth, rate limiting, circuit breaker

Sidecar Pattern:
  Her servisin yanına bir "sidecar" proxy koy.
  Sidecar cross-cutting concern'leri YÖNETIR.

  ┌──────────────────┐     ┌──────────────────┐
  │  Order Service   │     │  Payment Service │
  │                  │     │                  │
  │  ┌────────────┐  │     │  ┌────────────┐  │
  │  │  Sidecar   │  │────→│  │  Sidecar   │  │
  │  │  (Envoy)   │  │     │  │  (Envoy)   │  │
  │  └────────────┘  │     │  └────────────┘  │
  └──────────────────┘     └──────────────────┘

Service Mesh (Istio, Linkerd):
  = Tüm sidecar'ları MERKEZI olarak yöneten sistem
  → mTLS, traffic management, observability OTOMATIK
```

### Puan Kartı

```
┌─────────────────────┬─────────┐
│ Karakteristik        │ Puan    │
├─────────────────────┼─────────┤
│ Deployability       │ ⭐⭐⭐⭐⭐│  → Bağımsız deploy — EN İYİ!
│ Scalability         │ ⭐⭐⭐⭐⭐│  → Servis bazında ölçekleme
│ Fault Tolerance     │ ⭐⭐⭐⭐⭐│  → Bir servis çökerse diğerleri yaşar
│ Evolvability        │ ⭐⭐⭐⭐⭐│  → Servis bazında teknoloji seçimi
│ Testability         │ ⭐⭐⭐   │  → Integration test ZORDUR
│ Simplicity          │ ⭐      │  → EN karmaşık mimari (Space-Based ile)
│ Overall Cost        │ ⭐      │  → EN PAHALI mimari
│ Performance         │ ⭐⭐    │  → Network overhead
└─────────────────────┴─────────┘

Ne zaman kullan?
  ✅ Büyük organizasyon, çok takım
  ✅ Hızlı, bağımsız deploy zorunlu
  ✅ Farklı ölçeklenme ihtiyaçları
  ❌ Küçük ekip (< 10 kişi genellikle monolith YETERLİ!)
  ❌ Startup / MVP (hız önemli, karmaşıklık değil)
```

---

## 16. 📋 Mimari Kararlar

### Anti-Pattern'lar

```
1. "Covering Your Assets" Anti-Pattern 🫣
   → Mimar karar VERMEKTEN KAÇINIR
   → "İkisi de olabilir, siz karar verin"
   → Neden kötü: Mimarın işi KARAR VERMEK!

2. "Groundhog Day" Anti-Pattern 🔄
   → Aynı karar tekrar tekrar TARTIŞILIR
   → Neden: Karar belgelenmemiş veya gerekçe açıklanmamış
   → Çözüm: ADR! (Architecture Decision Record)

3. "Email-Driven Architecture" Anti-Pattern 📧
   → Mimari kararlar email'lerde kaybolur
   → "3 ay önce bir e-posta'da konuşmuştuk..."
   → Çözüm: ADR + wiki + version control!
```

### Architecture Decision Records (ADR) 📝

```
Her mimari karar bir ADR ile BELGELENMELİ:

# ADR-001: Servisler Arası İletişim Protokolü

## Durum
Kabul Edildi (2024-03-15)

## Bağlam
Sipariş ve ödeme servisleri arasında iletişim gerekiyor.
Günde ~10K sipariş bekleniyor. Eventual consistency kabul edilebilir.

## Karar
Asenkron mesajlaşma (RabbitMQ) kullanılacak.

## Gerekçe
Seçenekler değerlendirildi:
| Seçenek      | Avantaj              | Dezavantaj                |
|--------------| --------------------|--------------------------|
| REST (sync)  | Basit, hızlı geliştirme | Temporal coupling, cascade failure |
| gRPC (sync)  | Hızlı, type-safe    | Aynı coupling sorunları   |
| RabbitMQ     | Loose coupling, retry | Karmaşıklık, eventual cons. |
| Kafka        | Event sourcing, replay | Overkill (10K/gün yeterli)|

RabbitMQ seçildi çünkü:
- Eventual consistency kabul edilebilir (siparişler)
- Ödeme servisi çökse bile siparişler kuyrukta beklenir
- 10K/gün hacmi için Kafka gereksiz karmaşıklık ekler

## Sonuçlar
- Mesaj formatı JSON Schema ile tanımlanacak
- Dead letter queue hata yönetimi için kurulacak
- Idempotency key ile tekrarlanan mesajlar engellenecek

## Notlar
Bu karar 100K/gün hacmine ulaşıldığında yeniden değerlendirilecek.
```

---

## 17. ⚠️ Mimari Risk Analizi

### Risk Matrisi

```
Risk değerlendirmesi 2 boyutlu:

          ETKİ
          │  Yüksek │  🟡       │  🔴
          │  Orta   │  🟢       │  🟡
          │  Düşük  │  🟢       │  🟢
          └─────────┴───────────┴─────────
                    Düşük         Yüksek
                    OLASILIK

🔴 Yüksek etki + Yüksek olasılık = ACİL HAREKet!
🟡 Yüksek etki + Düşük olasılık = İZLE ve PLANLA
🟡 Düşük etki + Yüksek olasılık = AZALt
🟢 Düşük etki + Düşük olasılık = KABUL et
```

### Risk Storming 🌪️

```
Ekip aktivitesi: Mimari riskleri TOPLU olarak belirle

1. BİREYSEL: Herkes mimari diyagramı inceler, risk gördüğü yere
   renkli yapışkan not yapıştırır (🔴🟡🟢)

2. TOPLU: Tüm notlar görünür. Aynı yere çok not → yüksek risk!

3. TARTIŞMA: Her risk tartışılır:
   → "Veritabanı single point of failure" (🔴 herkes görmüş!)
   → "Cache tutarsızlığı" (🟡 birkaç kişi görmüş)
   → "Log formatı tutarsız" (🟢 bir kişi görmüş)

4. AKSIYON: Her risk için eylem planı:
   → 🔴 DB: Read replica ekle + failover kur
   → 🟡 Cache: TTL standardize et + invalidation stratejisi
   → 🟢 Log: Sonraki sprint'te log formatı standartlaştır

"Bir mimar tek başına tüm riskleri GÖREMEZ.
 Ekip bir bakışta daha fazlasını görür." 👁️👁️👁️👁️
```

---

## 18. 📊 Diyagramlar ve Sunum

### C4 Modeli

```
Simon Brown'un C4 Modeli — 4 seviyeli diyagram:

Level 1: SYSTEM CONTEXT
  → Sistemin dış dünyayla (kullanıcılar, diğer sistemler) ilişkisi
  → "Kuş bakışı" — herkes anlayabilir

Level 2: CONTAINER
  → Sistemin büyük yapı taşları (API, web app, DB, message broker)
  → "Hangi teknolojiler, nasıl konuşuyor?"

Level 3: COMPONENT
  → Bir container'ın iç yapısı (modüller, sınıflar)
  → Geliştiriciler için

Level 4: CODE
  → Sınıf diyagramları (genellikle GEREKSİZ — IDE'den bakılır)

KURAL:
  → Her seviye için HEDEF KİTLE farklı
  → Yöneticiler → Level 1-2
  → Geliştiriciler → Level 2-3
  → Level 4 genellikle YAPMA (hızla eskir)
```

### Sunum İpuçları

```
Mimar aynı zamanda İLETİŞİMCİDİR!

1. Hedef kitlseyi tanı:
   → CTO'ya: Maliyet, risk, timeline
   → Geliştirilere: Teknik detay, trade-off
   → Ürün yöneticisine: İş etkisi, hız

2. Diyagramda TUTARLILIK:
   → Aynı renk = aynı anlam (her yerde)
   → Ok yönü = veri akışı mı? Bağımlılık mı? AÇIKLA!
   → Legend (gösterge) UNUTMA!

3. İfadenin önemini belirle:
   → "Microservices YAPABİLİRİZ" (seçenek)
   → "Microservices YAPMALIYIZ" (tavsiye)
   → "Microservices YAPACAĞIZ" (karar)
   → Kelimeler İYİ SEÇ!
```

---

## 19. 👥 Ekip ve Liderlik

### Kontrol Spektrumu

```
Mimar, ekip üzerinde NE KADAR kontrol uygulamalı?

  ←──────────────────────────────────────────→
  BARRIKATLAR      REHBERLIK          SERBESTLİK
  (çok kontrol)    (dengeli)          (az kontrol)

  ❌ Barrikatlar:
    "Sadece X kütüphanesini kullanabilirsiniz!"
    "Her PR'a ben onay vereceğim!"
    → Ekip demotive olur, bottleneck oluşur

  ❌ Tam Serbesti:
    "Ne isterseniz yapın!"
    → Kaos, tutarsız kararlar, teknik borç

  ✅ Rehberlik:
    "Bu 3 framework'ten birini seçebilirsiniz, gerekçenizi ADR'ye yazın."
    "Cross-cutting concern'ler için şu standartları takip edin."
    "Servis sınırlarını şu prensiplerle çizin."

  EKIP DENEYİMİNE GÖRE AYARLA:
    Junior ekip → Daha fazla kontrol (rehberlik sık)
    Senior ekip → Daha fazla serbesti (sadece guardrail'ler)
```

### Conway's Law 🏢

```
"Sistemi tasarlayan organizasyonlar, kendi iletişim
 yapılarının kopyasını üreten tasarımlar üretmeye
 mecburdur." — Melvin Conway, 1968

Pratik anlam:
  3 takım varsa → 3 servisten oluşan sistem üretirler
  10 takım varsa → 10 servislik mimari ortaya çıkar

INVERSE CONWAY MANEUVER:
  İSTEDİĞİN mimariyi belirle → EKİPLERİ buna göre ORGANIZE ET!

  İstediğin: 4 microservice
  → 4 takım oluştur, her biri bir servisten sorumlu
  → Takım yapısı mimariyi DESTEKLER (zorlukla değil, doğal olarak)
```

### Elastic Leadership

```
Ekibin olgunluğuna göre liderlik STİLİ değiş:

FORMING (Oluşum):
  → Ekip yeni, kurallar belirsiz
  → Mimar: DIRECTIVE ol. Kararları SEN ver.

STORMING (Fırtına):
  → Ekip tartışıyor, ego çatışmaları
  → Mimar: KOLAYLAŞTIRICI ol. Tartışmaları yönlendir.

NORMING (Normleşme):
  → Ekip uyum sağlıyor, standartlar oturuyor
  → Mimar: DANIŞMAN ol. Sorulara cevap ver.

PERFORMING (Performans):
  → Ekip kendi kararlarını verebiliyor
  → Mimar: DELEGE ET. Stratejiye odaklan.
```

---

## 20. � Büyük Şirketlerde Mimari Kararlar

### Netflix — Event-Driven + Microservices Hibrit

```
Netflix'in mimarisi kitaptaki "Event-Driven" + "Microservices" birleşimi:
  → 1000+ microservice (her biri bağımsız deploy)
  → Service mesh: Zuul (API Gateway) + Eureka (Service Discovery)
  → Event-driven: Kafka ile asenkron iletişim

Fitness Functions (kitaptaki kavram) Netflix'te:
  → Chaos Monkey: Fault tolerance fitness function
  → Canary deployment: Her release %1 trafikle test edilir
  → Circuit breaker (Hystrix): Cascade failure koruması

Architecture Quantum:
  → Her microservice = 1 quantum
  → Bağımsız deploy edilebilir
  → Kendi DB'si var (shared-nothing)
```

### Spotify — Service-Based → Microservices Evrimi

```
Spotify modeli kitaptaki "evolvability" kavramını gösterir:
  → Başlangıçta monolith
  → Sonra service-based (ekip başına servis)
  → Sonra microservices (domain başına servis)

"Squad" yapısı = Inverse Conway Maneuver:
  → Organizasyonu mimariyi TAKIP EDECEK şekilde kur
  → Kitapta bunu "organizasyonel mimari" olarak görürsünüz
```

### Amazon — Two-Pizza Teams + SOA

```
2002'de Jeff Bezos'un "API Mandate":
  → Tüm ekipler SERVİS arayüzü ile iletişim kuracak
  → Doğrudan DB erişimi YASAK
  → Bu kural AWS'nin doğuşuna yol açtı

Kitaptaki "coupling characteristics" burada:
  → Stamp coupling: Ekipler JSON contract ile konuşur
  → Hiçbir ekip başkasının iç yapısını bilmez
  → Conway's Law'ın EN güzel örneği
```

---

## 21. 🤖 Yapay Zeka Çağında Yazılım Mimarisi

### AI Mimari Kararları Verebilir mi?

```
Kitaptaki en kritik kavram: "Everything is a TRADE-OFF"
  → AI trade-off ANALİZİ yapabilir ama KARAR veremez
  → Neden? Context bilgisi eksik (ekip yetkinliği, bütçe, politik durum)

AI'ın GÜÇLERİ:
  ✅ Architecture fitness function önerme
  ✅ Coupling analizi (static analysis gibi)
  ✅ Pattern eşleştirme ("Bu yapı X pattern'a benziyor")
  ✅ Trade-off matris oluşturma

AI'ın ZAYIFLIKLARI:
  ❌ "Bu ekip microservices yönetebilir mi?" sorusunu cevaplayamaz
  ❌ Politik/organizasyonel trade-off'ları bilmez
  ❌ "İlk mimariyi BASİT seç, sonra evrilsin" ← bu SEZG gerektiri
```

### AI ile Mimari Değerlendirme Promptları

```
ARCHITECTURE DECISION RECORD:
  "Bu senaryoyu analiz et ve Architecture Decision Record (ADR) oluştur:
   - Context: [mevcut sistem açıklaması]
   - Seçenekler: Layered vs Microservices vs Event-Driven
   - Her seçenek için fitness function tanımla
   - Trade-off analizi: scalability vs simplicity vs cost
   - Karar ve gerekçe
   
   Richards & Ford'un Fundamentals of SA kitabındaki
   architecture characteristics listesini kullan."

MODULARITY ANALİZİ:
  "Bu kod tabanının modülerlik metriklerini analiz et:
   - Afferent coupling (Ca): Kaç modül bu modüle bağımlı?
   - Efferent coupling (Ce): Bu modül kaç modüle bağımlı?
   - Instability (I = Ce / (Ca+Ce)): Değişime açıklık
   - Abstractness (A): Soyut sınıf oranı
   Richards'ın 'zone of pain' ve 'zone of uselessness' kavramlarını kullan."

CONNASCENCE ANALİZİ:
  "Bu iki modül arasındaki connascence türünü belirle:
   - Static mi Dynamic mi?
   - Name, Type, Meaning, Position, Algorithm?
   - Strength'i azaltmak için ne yapılabilir?
   - Locality'si ne? (aynı sınıf, aynı paket, farklı servis)"
```

### Kitabın AI Çağındaki Önemi

```
Richards & Ford'un kitabı AI çağında DAHA değerli çünkü:

  1. AI çok hızlı kod üretir → YAPI kararları daha kritik
     → Yanlış mimaride çok kod üretmek = DAHA büyük sorun

  2. AI microservice dünyasında yeni riskler yaratır:
     → AI her servisi bağımsız üretebilir
     → AMA servisler arası CONTRACT uyumu?
     → Architecture Quantum kavramı burada devreye girer

  3. Fitness functions AI ile otomatikleştirilebilir:
     → "Bu deploy performans SLA'ını karşılıyor mu?"
     → AI fitness function'ı çalıştırır ve RAPORLAR
```

### Topluluk Görüşleri

```
Mark Richards (kitabın yazarı, 2023):
  "Mimarinin %50'si TEKNİK, %50'si İNSAN meselesi.
   Hangi pattern'ı seçeceğin kadar, ekibinin bunu
   uygulayabilme kapasitesi ÖNEMLİ."

Neal Ford (diğer yazar):
  "First Law of Software Architecture:
   Everything in software architecture is a trade-off.
   If you think you found something that isn't, 
   you just haven't found the trade-off YET."

Reddit r/softwarearchitecture:
  "Bu kitap interviewer'ların GERÇEKTEN sorduğu konuları kapsıyor.
   DDIA + bu kitap = System Design Interview'a hazırsın."

Sam Newman (Building Microservices yazarı):
  "Richards & Ford mimarideki trade-off düşüncesini çok iyi anlatır.
   Ama microservices için ayrıca derinleşmen gerek."
```

---

## 22. �🎬 Son Sözler

### Mimari Stil Karşılaştırma Tablosu 🏆

```
┌────────────────┬─────┬──────┬──────┬──────┬─────┬──────┬───────┐
│                │Scale│Deploy│Fault │Simple│Cost │Test  │Evolve │
├────────────────┼─────┼──────┼──────┼──────┼─────┼──────┼───────┤
│ Layered        │ ⭐  │ ⭐   │ ⭐   │⭐⭐⭐⭐⭐│⭐⭐⭐⭐⭐│ ⭐⭐  │ ⭐    │
│ Pipeline       │ ⭐  │ ⭐⭐  │ ⭐   │⭐⭐⭐⭐⭐│⭐⭐⭐⭐⭐│⭐⭐⭐⭐⭐│ ⭐⭐⭐ │
│ Microkernel    │ ⭐⭐ │ ⭐⭐⭐ │ ⭐⭐  │⭐⭐⭐⭐ │⭐⭐⭐⭐ │⭐⭐⭐⭐⭐│ ⭐⭐⭐ │
│ Service-Based  │⭐⭐⭐ │⭐⭐⭐⭐ │⭐⭐⭐⭐ │ ⭐⭐⭐ │⭐⭐⭐⭐ │ ⭐⭐⭐⭐│ ⭐⭐⭐ │
│ Event-Driven   │⭐⭐⭐⭐⭐│⭐⭐⭐ │⭐⭐⭐⭐⭐│ ⭐   │ ⭐⭐  │ ⭐⭐  │⭐⭐⭐⭐⭐│
│ Space-Based    │⭐⭐⭐⭐⭐│⭐⭐⭐ │⭐⭐⭐ │ ⭐   │ ⭐   │ ⭐   │ ⭐⭐  │
│ Microservices  │⭐⭐⭐⭐⭐│⭐⭐⭐⭐⭐│⭐⭐⭐⭐⭐│ ⭐   │ ⭐   │ ⭐⭐⭐ │⭐⭐⭐⭐⭐│
└────────────────┴─────┴──────┴──────┴──────┴─────┴──────┴───────┘

"En iyi" mimari YOK! Sadece durumuna en UYGUN olan var.
```

### 7 Altın Kural 🏆

| # | Kural | Açıklama |
|---|---|---|
| 1 | **Her şey trade-off** | "Avantajsız" çözüm bulamıyorsan yeterince analiz etmemişsindir |
| 2 | **NEDEN > NASIL** | Kararın gerekçesini YAZ (ADR) |
| 3 | **Genişlik > Derinlik** | Bir mimar olarak birçok teknolojiyi BİLMEN gerekir |
| 4 | **En az 3-7 karakteristik** | Hepsini istersen hiçbirini iyi yapamazsın |
| 5 | **Fitness function** | Mimari kararlarını OTOMATİK test et |
| 6 | **Conway's Law** | Ekip yapısı = sistem yapısı. BİLİNÇLİ organize et |
| 7 | **Evrilme > Tahmin** | "Doğru" mimariyi ilk günden bilmek İMKANSIZ, evril! |

### Önceki Kitaplarla Bağlantı 🔗

```
📗 Grokking Algorithms → Veri yapıları = bileşen iç yapısı
📕 Clean Code → Temiz KOD = temiz MİMARİNİN temeli
📘 Pragmatic Programmer → DRY, Orthogonality → Modülerlik prensipleri
📙 Missing README → Kariyer büyümesi: Developer → Mimar yolu
📗 Philosophy of Software Design → Deep modules = mimari bileşenler
📘 Design Patterns → Pattern → Bileşen iç tasarımı
📕 DDIA → Veri katmanı mimari kararları (replication, partitioning)
📙 Unit Testing → Testability mimari karakteristik
📗 Refactoring → Mimari evrilme = kademeli refactoring
🏛️ Clean Architecture → DIP, boundaries → bu kitaptaki tüm stillerde geçerli
🏗️ Fundamentals of SA → NASIL karar verilir? Trade-off düşünme ÇERÇEVESI

Bu kitap "doğru mimari nedir?" sorusuna yanıt vermez.
"Doğru mimari NASIL seçilir?" sorusuna yanıt verir!

Clean Architecture: "Bağımlılık kuralına UY" (tek doğru cevap)
Fundamentals:       "Seçeneklerin şunlar. Trade-off'ları değerlendir." (karar çerçevesi)
→ İkisi birbirini TAMAMLAR ✅
```

### Faz 3 İlerleme Durumu 📊

```
FAZ 3 — Mimari & Ölçek (12-18 ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Clean Architecture              ✅
  2. Fundamentals of Software Arch   ✅  ← BURADASIN
  3. Building Microservices          ⬜
  4. The Phoenix Project             ⬜
  5. System Design Interview Vol 1   ⬜
```

---

> **"Mimarlık, doğru cevapları bulmak değil,
> doğru SORULARI sormaktır.
> 'Hangi mimariyi seçmeliyim?' yerine
> 'Hangi karakteristikler BU PROJE için kritik?'
> 'Hangi trade-off'ları KABUL EDEBİLİRİZ?'
> 'Bu karar GERİ ALINABİLİR mi?'
> soruları önemlidir.
> Çünkü yazılım mimarisinde en pahalı şey
> YANLIŞ kararlar değil — GERİ ALINAMAZ kararlarıdır."**
> — Richards & Ford'un ruhu
