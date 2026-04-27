# 🔵 Domain-Driven Design (DDD) — Türkçe Kapsamlı Rehber

> **"Yazılım, modellediği domain kadar karmaşık olmalıdır — daha fazla değil."**
> — Eric Evans

Bu kitap yazılım mühendisliğinin "kutsal kitabı"dır — "The Blue Book" olarak bilinir.
2003'te yazılmıştır ama bugün microservices, event-driven architecture ve
modern yazılım tasarımının TEMELİNİ oluşturur. 💎

**UYARI:** Bu kitap ZORDUR. İlk okumada %30'unu anlaman normal.
Ama anladığın her kavram, mühendislik kariyerini KALICI olarak dönüştürür.

---

## 📖 İçindekiler

1. [DDD Nedir ve Neden Önemlidir?](#1--ddd-nedir-ve-neden-önemlidir)
2. [Ubiquitous Language (Ortak Dil)](#2--ubiquitous-language-ortak-dil)
3. [Model-Driven Design](#3--model-driven-design)
4. [Entity (Varlık)](#4--entity-varlık)
5. [Value Object (Değer Nesnesi)](#5--value-object-değer-nesnesi)
6. [Aggregate (Küme)](#6--aggregate-küme)
7. [Repository (Depo)](#7--repository-depo)
8. [Service (Servis)](#8--service-servis)
9. [Factory (Fabrika)](#9--factory-fabrika)
10. [Domain Event (Alan Olayı)](#10--domain-event-alan-olayı)
11. [Module (Modül)](#11--module-modül)
12. [Bounded Context (Sınırlı Bağlam)](#12--bounded-context-sınırlı-bağlam)
13. [Context Map (Bağlam Haritası)](#13--context-map-bağlam-haritası)
14. [Anti-Corruption Layer (ACL)](#14--anti-corruption-layer-acl)
15. [Strategic Design](#15--strategic-design)
16. [Supple Design (Esnek Tasarım)](#16--supple-design-esnek-tasarım)
17. [Event Storming](#17--event-storming)
18. [CQRS ve Event Sourcing](#18--cqrs-ve-event-sourcing)
19. [DDD ve Microservices](#19--ddd-ve-microservices)
20. [Gerçek Hayata Uyarlama](#20--gerçek-hayata-uyarlama)
21. [Büyük Şirketlerde DDD](#21--büyük-şirketlerde-ddd)
22. [Yapay Zeka Çağında DDD](#22--yapay-zeka-çağında-ddd)
23. [Son Sözler](#23--son-sözler)

---

## 1. 🌍 DDD Nedir ve Neden Önemlidir?

### Temel Sorun

```
Yazılım projeleri neden BAŞARISIZ olur?

❌ "Teknik olarak mükemmel ama yanlış şeyi yapan" yazılımlar
❌ Geliştiriciler ve iş uzmanları FARKLI dil konuşuyor
❌ Kod, iş kurallarını YANSITMIYOR
❌ Karmaşıklık KONTROL EDİLEMİYOR

Senaryo:
  İş uzmanı: "Siparişi ASKIYA alalım."
  Geliştirici: "Order.status = 'inactive' mi yapayım?"
  İş uzmanı: "Hayır, askıya almak farklı! Stok geri dönmeli, 
              ödeme iade beklemeli, kargo durdurulmalı..."
  Geliştirici: "Aaa, ben sadece status değiştiriyordum..." 😅

→ SORUN: Geliştirici domain'i (iş alanını) ANLAMIYOR!
→ ÇÖZÜM: Domain-Driven Design! 💡
```

### DDD'nin Temel Fikri

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║   "En karmaşık yazılım, TEKNİK karmaşıklıktan değil,     ║
║    DOMAIN karmaşıklığından gelir."                         ║
║                                                            ║
║   Teknik zorluk: "Redis cluster nasıl kurulur?"            ║
║   → Çözümü Google'dan bulursun.                            ║
║                                                            ║
║   Domain zorluğu: "Kargo iade süreci sırasında             ║
║   siparişin finansal durumu ne olmalı?"                     ║
║   → Çözümü Google'dan BULAMAZSIN.                          ║
║   → İŞ UZMANLARLA konuşman lazım!                          ║
║                                                            ║
║   DDD = Domain bilgisini kodun MERKEZİNE koy!             ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

### DDD'nin İki Seviyesi

```
STRATEGIC DDD (Büyük resim) 🗺️
  → Bounded Context'ler: Sistemin SINIRLARI nerede?
  → Context Map: Context'ler arası ilişkiler
  → Hangi takım hangi domain'den sorumlu?
  → "NEYİ modelliyoruz?" sorusu

TACTICAL DDD (Detay) 🔧
  → Entity, Value Object, Aggregate, Repository, Service
  → Domain Event, Factory
  → Kodu NASIL yapılandırıyoruz?
  → "NASIL modelliyoruz?" sorusu

SIRALAMA:
  İlk STRATEGIC → sonra TACTICAL!
  → Önce SINIRLARINI çiz → sonra İÇİNİ doldur!
  → Çoğu takım TAKTİK'ten başlıyor → HATA! 🚫
  → "İlk Entity ve Repository yapalım" → sınırlar belirsiz → kaos!
```

---

## 2. 🗣️ Ubiquitous Language (Ortak Dil)

### DDD'nin EN ÖNEMLİ Kavramı

```
"Ubiquitous" = HER YERDE BULUNAN

Geliştirici, iş uzmanı, ürün yöneticisi, test uzmanı...
HERKES AYNI kelimelerle AYNI anlama gelen şeylerden bahsetmeli!

❌ KÖTÜ DURUM:
  İş uzmanı: "Müşteri", "Üye", "Kullanıcı" → HEPSİ AYNI ŞEYI mi kastediyor?
  Geliştirici: Kodda "User" class'ı var → ama "Müşteri" mi "Üye" mi?
  DBA: Tabloda "accounts" → Bu "User" mı?
  → HERKES FARKLI ŞEY ANLIYOR! 😱

✅ İYİ DURUM:
  Takım kararı: "Biz buna 'Üye' diyoruz. 
  Üye = kayıt olmuş ve en az bir sipariş vermiş kişi."
  
  → İş uzmanı: "Üye" diyor
  → Kodda: class Member { ... } (User değil! Account değil! MEMBER!)
  → DB'de: tablo adı "members"
  → API'de: POST /members
  → Dökümanda: "Üyelik Sistemi"
  → HERKES AYNI DİL! ✅
```

### Ortak Dil Nasıl Oluşturulur?

```
ADIM 1: İŞ UZMANLARLA KONUŞ (çok konuş!)
  → "Bu süreç nasıl işliyor?"
  → İş uzmanının kullandığı KELİMELERİ DINLE
  → Teknik jargon KULLANMA!

ADIM 2: SÖZLÜK OLUŞTUR (Glossary)
  ┌──────────────────────────────────────────────────────┐
  │ Terim      │ Tanım                                   │
  ├────────────┼─────────────────────────────────────────┤
  │ Üye        │ Kayıt olmuş ve sipariş vermiş kişi      │
  │ Ziyaretçi  │ Kayıt olmamış site kullanıcısı          │
  │ Sipariş    │ Üyenin oluşturduğu satın alma talebi    │
  │ Kargo      │ Siparişin fiziksel teslimat süreci      │
  │ İade       │ Üyenin ürünü geri göndermesi            │
  │ Askıya Alma│ Siparişin geçici olarak durdurulması    │
  └────────────┴─────────────────────────────────────────┘

ADIM 3: KODDA KULLAN
  → Sözlükteki her terim = kodda bir class/method adı
  → class Member (User değil!)
  → class Order (Purchase değil!)
  → order.suspend() (order.setStatus('inactive') DEĞİL!)

ADIM 4: SÜREKLİ REFİNE ET
  → "Biz buna 'askıya alma' diyoruz ama aslında 2 farklı durum var:
     geçici askı ve kalıcı askı."
  → Tamam! → TemporarySuspension ve PermanentSuspension!
  → Dil EVRİLİR → kod da evrilir! ♻️
```

```javascript
// ❌ KÖTÜ: Geliştirici kendi dilini uydurmuş
class UserAccount {
  deactivate() {
    this.status = 'inactive';
    // stok ne olacak? iade ne olacak? BELLI DEĞIL!
  }
}

// ✅ İYI: Ubiquitous Language kullanılmış
class Order {
  suspend() {
    // "Askıya alma" = İş uzmanının tanımladığı süreç
    this.status = OrderStatus.SUSPENDED;
    this.releaseReservedStock();         // Stoku serbest bırak
    this.initiatePaymentHold();          // Ödeme holdda
    this.notifyShippingToHalt();         // Kargoyu durdur
    this.recordSuspensionReason();       // Nedenini kaydet
    this.emit(new OrderSuspended(this)); // Domain event!
  }
}

// → Kodu okuyan İŞ UZMANI bile anlayabilir!
// → "Evet, askıya alma tam da bunu yapmalı!" ✅
```

---

## 3. 🎨 Model-Driven Design

### Model Nedir?

```
MODEL = Gerçekliğin basitleştirilmiş temsili

Gerçek dünya ÇOK karmaşık → HER ŞEYİ modelleyemezsin
→ ÖNEMLI olan kısımları modelle, gerisini ATLA!

HARITA metaforu: 🗺️
  → Türkiye haritası: Tüm binaları gösterir mi? HAYIR!
  → Tüm binaları gösteren harita = gerçek dünya kadar karmaşık = İŞE YARAMAZ!
  → İyi harita: AMACA göre detay seviyesi

  Yol haritası: Yollar + şehirler (bina yok)
  Topografik harita: Yükseklik + arazi (yol yok)
  → Her harita BELİRLİ bir amaca HİZMET eder

  Yazılım modeli de böyle:
  → "Sipariş" modeli: fiyat, ürünler, durum, teslimat → İŞ İÇİN ÖNEMLİ olanlar
  → Siparişin kağıt rengi? Yazı fontu? → İŞ İÇİN ÖNEMSİZ → MODELLEME!
```

### Model = Kod

```
DDD'nin DEVRİMCİ fikri:

GELENeksel:
  İş uzmanı → Analiz dokümanı → Geliştirici → KOD
  → Doküman ve kodun BAĞLANTISI kopar!
  → Doküman güncellenir ama kod güncellenmez (veya tersi)
  → 3 ay sonra: doküman bir şey söylüyor, kod başka bir şey yapıyor 😱

DDD:
  İş uzmanı + Geliştirici → BİRLİKTE model oluşturur → KOD = MODEL!
  → Kod, modelin TA KENDİSİDİR. Ayrı doküman gerekmiyor!
  → Model değişirse → kod değişir
  → Kod değişirse → model değişir
  → İKİSİ HER ZAMAN SENKRON! ✅

  "Kod anlaşılmıyorsa, model yanlıştır."
  "Model iş uzmanına açıklayamıyorsan, model eksiktir."
```

---

## 4. 🆔 Entity (Varlık)

### Tanım

```
ENTITY = KİMLİĞİ (identity) olan nesne

İki entity AYNI özelliklere sahip olsa bile FARKLIDIR!
Çünkü KİMLİKLERİ farklı.

ÖRNEK: İnsanlar
  → Ali Yılmaz, doğum: 1990, İstanbul
  → Ali Yılmaz, doğum: 1990, İstanbul
  → AYNI KİŞİ Mİ? → TC kimlik numarasına BAK!
  → TC: 123 ≠ TC: 456 → FARKLI kişiler!
  → İsimleri, doğum yılları, şehirleri aynı AMA kimlikleri FARKLI!

ÖRNEK: Sipariş
  → Sipariş #1001: 3 ürün, 150 TL
  → Sipariş #1002: 3 ürün, 150 TL
  → AYNI SİPARİŞ Mİ? HAYIR!
  → ID'leri farklı → farklı siparişler!
  → Sipariş bir ENTITY'dir.
```

### Entity Kuralları

```
1. KİMLİK (ID) → Yaratıldığında atanır, ASLA değişmez
2. Yaşam döngüsü var → oluşturulur, değişir, silinir
3. Eşitlik = ID eşitliği (özellik eşitliği değil!)
4. DEĞİŞEBİLİR (mutable) — durumu zaman içinde değişir
```

```javascript
// Entity örneği
class Order {
  #id;        // kimlik → değişmez!
  #memberId;
  #items;
  #status;
  #createdAt;

  constructor(id, memberId) {
    this.#id = id;
    this.#memberId = memberId;
    this.#items = [];
    this.#status = OrderStatus.DRAFT;
    this.#createdAt = new Date();
  }

  get id() { return this.#id; }

  addItem(product, quantity) {
    if (this.#status !== OrderStatus.DRAFT) {
      throw new Error('Sadece taslak siparişe ürün eklenebilir!');
    }
    // İş kuralı BURADA, entity İÇİNDE! ✅
    const item = new OrderItem(product, quantity);
    this.#items.push(item);
  }

  confirm() {
    if (this.#items.length === 0) {
      throw new Error('Boş sipariş onaylanamaz!'); // İş kuralı!
    }
    this.#status = OrderStatus.CONFIRMED;
  }

  // Entity eşitliği = ID eşitliği!
  equals(other) {
    if (!(other instanceof Order)) return false;
    return this.#id === other.id;
  }
}

// İki sipariş AYNI ürünlere sahip olsa bile
// ID'leri farklıysa → FARKLI sipariş!
const order1 = new Order('ord-001', 'member-1');
const order2 = new Order('ord-002', 'member-1');
order1.equals(order2); // false! (farklı ID)
```

---

## 5. 💎 Value Object (Değer Nesnesi)

### Tanım

```
VALUE OBJECT = Kimliği OLMAYAN, sadece DEĞERİYLE tanımlanan nesne

İki value object AYNI değerlere sahipse → AYNIDIR!
Kimlik YOK → sadece değer!

ÖRNEK: Para 💰
  → 100 TL banknot (seri no: ABC123)
  → 100 TL banknot (seri no: XYZ789)
  → Seri numaraları farklı AMA değerleri AYNI
  → Kasiyere ödemede: "Hangi 100 TL?" diye sormaz!
  → 100 TL = 100 TL → AYNI DEĞER!

ÖRNEK: Renk 🎨
  → RGB(255, 0, 0) ve RGB(255, 0, 0) → AYNIDIR! İkisi de KırmızI!
  → "Bu kırmızı MU, yoksa ŞU kırmızı mı?" → aynı!

ÖRNEK: Adres 📍
  → "İstanbul, Kadıköy, Moda Cad. No:5" 
  → Bu adres KİM'in değil, NERE'nin bilgisi
  → İki farklı kişinin adresi AYNI olabilir → sorun yok!
```

### Value Object Kuralları

```
1. KİMLİK YOK → kimliğe göre karşılaştırma yok
2. DEĞİŞMEZ (Immutable!) → oluşturulduktan sonra DEĞİŞTİRİLEMEZ!
   → Değiştirmek istiyorsan → YENİ bir value object OLUŞTUR!
3. EŞİTLİK = TÜM özelliklerin eşitliği
4. Yan etkisiz (side-effect free)
5. KENDI KENDİNİ DOĞRULAR (self-validating)
```

```javascript
// ❌ KÖTÜ: Para'yı primitive olarak temsil etmek
class Order {
  constructor() {
    this.price = 100;    // 100 ne? TL? USD? Euro? BİLİNMEZ!
    this.currency = 'TRY'; // Ayrı alan → unutulabilir, tutarsız olabilir!
  }
}

// ✅ İYI: Para bir VALUE OBJECT
class Money {
  #amount;
  #currency;

  constructor(amount, currency) {
    if (amount < 0) throw new Error('Tutar negatif olamaz!');
    if (!['TRY', 'USD', 'EUR'].includes(currency)) {
      throw new Error(`Geçersiz para birimi: ${currency}`);
    }
    this.#amount = amount;
    this.#currency = currency;
    Object.freeze(this); // IMMUTABLE! 🔒
  }

  get amount() { return this.#amount; }
  get currency() { return this.#currency; }

  add(other) {
    if (this.#currency !== other.currency) {
      throw new Error('Farklı para birimleri toplanamaz!');
      // 100 TL + 50 USD = ??? → İŞ KURALI!
    }
    return new Money(this.#amount + other.amount, this.#currency);
    // → YENİ nesne! Mevcut DEĞİŞMEZ! ✅
  }

  multiply(factor) {
    return new Money(this.#amount * factor, this.#currency);
  }

  equals(other) {
    if (!(other instanceof Money)) return false;
    return this.#amount === other.amount && 
           this.#currency === other.currency;
  }

  toString() {
    return `${this.#amount} ${this.#currency}`;
  }
}

// Kullanım:
const price = new Money(100, 'TRY');
const tax = new Money(18, 'TRY');
const total = price.add(tax); // new Money(118, 'TRY') → YENİ nesne!

price.amount; // hâlâ 100! → immutable! ✅
total.amount; // 118

// Eşitlik: değere göre!
const a = new Money(100, 'TRY');
const b = new Money(100, 'TRY');
a.equals(b); // true! → Aynı DEĞER = Aynı nesne! ✅
```

### Adres Value Object

```javascript
class Address {
  #city;
  #district;
  #street;
  #zipCode;

  constructor(city, district, street, zipCode) {
    if (!city || !district) throw new Error('Şehir ve ilçe zorunlu!');
    this.#city = city;
    this.#district = district;
    this.#street = street;
    this.#zipCode = zipCode;
    Object.freeze(this);
  }

  get city() { return this.#city; }
  get district() { return this.#district; }
  get street() { return this.#street; }
  get zipCode() { return this.#zipCode; }

  // Taşındı mı? → Yeni adres OLUŞTUR! (eski DEĞİŞMEZ)
  withCity(newCity) {
    return new Address(newCity, this.#district, this.#street, this.#zipCode);
  }

  equals(other) {
    if (!(other instanceof Address)) return false;
    return this.#city === other.city &&
           this.#district === other.district &&
           this.#street === other.street &&
           this.#zipCode === other.zipCode;
  }
}
```

### Entity vs Value Object Karar Ağacı

```
KİMLİK ÖNEMLİ Mİ?
  │
  ├── EVET → ENTITY
  │   → Sipariş, Müşteri, Ürün, Hesap
  │   → "Bu SİPARİŞ hangisi?" sorusu anlamlı
  │   → ID ile takip edilir, yaşam döngüsü var
  │
  └── HAYIR → VALUE OBJECT
      → Para, Adres, Tarih Aralığı, Email, Renk
      → "Bu 100 TL'nin hangisi?" sorusu ANLAMSIZ
      → Değer eşitse aynıdır, immutable

  💡 PRATIK KURAL: "Mümkün olan her şeyi VALUE OBJECT yap!"
  → Value Object DAHA basit (immutable, side-effect free)
  → Entity DAHA karmaşık (yaşam döngüsü, identity yönetimi)
  → Entity sayısını MINIMIZE et!
```

---

## 6. 🧩 Aggregate (Küme)

### DDD'nin EN ZOR ama EN ÖNEMLİ Kavramı

```
AGGREGATE = Bir bütün olarak ele alınan entity ve value object kümesi

PROBLEM:
  Sipariş → SiparişKalemleri → Ürün → Kategori → ...
  → Her şey her şeyle bağlantılı → SPAGETTI! 🍝
  → "Siparişi silersem, ürünü de siler miyim?" → BELİRSİZ!
  → "İki istek aynı anda sipariş kalemini değiştirirse?" → KAOS!

ÇÖZÜM: SINIRLARI ÇİZ!
  → Aggregate = BİR BÜTÜN olarak yönetilen küme
  → Aggregate ROOT = Dışarıdan erişim NOKTASI (tek giriş!)
  → Aggregate içi = dış dünyadan GİZLİ

  ┌─────────────── Aggregate Sınırı ──────────────────┐
  │                                                     │
  │   [Order] ← Aggregate Root (TEK giriş noktası!)    │
  │      │                                              │
  │      ├── OrderItem (Value Object / Entity)          │
  │      ├── OrderItem                                  │
  │      ├── ShippingAddress (Value Object)              │
  │      └── PaymentInfo (Value Object)                  │
  │                                                     │
  └─────────────────────────────────────────────────────┘

  → Dış dünya SADECE Order ile konuşur!
  → OrderItem'a doğrudan erişim YASAK!
  → "order.addItem()" → OK ✅
  → "orderItem.setQuantity(5)" → YASAK! ❌ (order üzerinden yap!)
```

### Aggregate Kuralları (KRİTİK!)

```
KURAL 1: AGGREGATE ROOT dışarıdan TEK ERİŞİM noktasıdır 🚪
  → Dış dünya sadece root'un public metodlarını çağırır
  → İç nesnelere DİREKT referans DIŞARI VERİLMEZ!

KURAL 2: AGGREGATE İÇİ TUTARLILIK tek işlemde (transaction) sağlanır 🔒
  → Bir aggregate'in tüm değişiklikleri TEK transaction'da!
  → "Order onaylandı VE stok düştü" → AYNI aggregate değilse → FARKLI transaction!

KURAL 3: AGGREGATE'LER ARASI referans SADECE ID ile! 🔗
  → Order.memberId = "member-123" ✅ (ID referans)
  → Order.member = memberObject ❌ (doğrudan nesne referansı YASAK!)
  → Neden? → Aggregate sınırını BOZAR, birlikte yükleme ZORUNLULUĞU doğurur

KURAL 4: AGGREGATE KÜÇÜK TUTULMALI! 📦
  → Büyük aggregate = büyük transaction = yavaş = çakışma!
  → "Şüpheye düştüğünde, DAHA KÜÇÜK aggregate yap!"
```

```javascript
// Aggregate Root: Order
class Order {
  #id;
  #memberId;      // Başka aggregate'e ID ile referans! ✅
  #items;         // Aggregate İÇİ → dışarı verilmez!
  #shippingAddress; // Value Object
  #status;

  constructor(id, memberId, shippingAddress) {
    this.#id = id;
    this.#memberId = memberId;
    this.#items = [];
    this.#shippingAddress = shippingAddress;
    this.#status = OrderStatus.DRAFT;
  }

  // Dış dünya SADECE bu metodları çağırabilir
  addItem(productId, productName, price, quantity) {
    if (this.#status !== OrderStatus.DRAFT) {
      throw new Error('Onaylanmış siparişe ürün eklenemez!');
    }
    if (quantity <= 0) {
      throw new Error('Miktar pozitif olmalı!');
    }

    // Aynı üründen varsa güncelle
    const existing = this.#items.find(i => i.productId === productId);
    if (existing) {
      existing.increaseQuantity(quantity);
    } else {
      this.#items.push(new OrderItem(productId, productName, price, quantity));
    }
  }

  removeItem(productId) {
    if (this.#status !== OrderStatus.DRAFT) {
      throw new Error('Onaylanmış siparişten ürün çıkarılamaz!');
    }
    this.#items = this.#items.filter(i => i.productId !== productId);
  }

  confirm() {
    if (this.#items.length === 0) {
      throw new Error('Boş sipariş onaylanamaz!');
    }
    if (!this.#shippingAddress) {
      throw new Error('Teslimat adresi gerekli!');
    }
    this.#status = OrderStatus.CONFIRMED;
    // Domain Event yayınla!
    return new OrderConfirmed(this.#id, this.#memberId, this.totalAmount);
  }

  get totalAmount() {
    return this.#items.reduce(
      (sum, item) => sum.add(item.subtotal),
      new Money(0, 'TRY')
    );
  }

  // İTEMLERİN KOPYAsını ver → orijinale dokunulamasın!
  get items() {
    return [...this.#items]; // defensive copy! 🛡️
  }
}

// Aggregate İÇİ Entity
class OrderItem {
  #productId;
  #productName;
  #unitPrice;
  #quantity;

  constructor(productId, productName, unitPrice, quantity) {
    this.#productId = productId;
    this.#productName = productName;
    this.#unitPrice = unitPrice;
    this.#quantity = quantity;
  }

  get productId() { return this.#productId; }

  get subtotal() {
    return this.#unitPrice.multiply(this.#quantity);
  }

  increaseQuantity(amount) {
    this.#quantity += amount;
  }
}
```

### Aggregate Boyut Kararı

```
SORU: Sipariş + Siparişin ödeme bilgisi → AYNI aggregate mi?

DÜŞÜN:
  → Sipariş onaylandığında ödeme de AYNI ANDA mı yapılmalı?
  → Yoksa ödeme ayrı bir süreç mi?

  E-ticaret:
  → Sipariş oluştur → Ödeme AYRI bir adım (3D Secure, banka onayı)
  → Order Aggregate ≠ Payment Aggregate
  → Order.confirm() → OrderConfirmed event → Payment servisi DİNLER

  Restoran POS:
  → Sipariş ver → ANINDA öde (kasada)
  → Order + Payment = AYNI aggregate OLABİLİR (tek transaction)

  BAĞLAMA BAĞLI! (Context-dependent)
  → Bu kararı İŞ UZMANIYLA beraber al!

GENEL KURAL:
  ┌──────────────────────────────────────────────────┐
  │ "Bir aggregate'i DAHA KÜÇÜK yapmanın bir yolunu  │
  │  bulabiliyorsan, YAP!"                           │
  │                                                  │
  │  Büyük aggregate:                                │
  │  → Yavaş yükleme (çok veri)                     │
  │  → Çok çakışma (çok kişi aynı anda)             │
  │  → Zor ölçekleme                                 │
  │                                                  │
  │  Küçük aggregate:                                │
  │  → Hızlı, az çakışma, kolay ölçekleme           │
  │  → AMA eventual consistency gerekebilir          │
  └──────────────────────────────────────────────────┘
```

---

## 7. 📦 Repository (Depo)

### Tanım

```
REPOSITORY = Aggregate'leri saklamak ve almak için SOYUTLAMA katmanı

"Domain katmanı VERİTABANINI BİLMEMELİ!"
→ Domain: "Siparişi kaydet" → NASIL kaydettiğini bilmiyorum ve BİLMEM GEREKMEZ!
→ Repository: "Tamam, ben PostgreSQL'e yazarım" (veya MongoDB'ye, veya bellekte tutarım test için)

METAFOR: Kütüphane 📚
  → "Bana DDD kitabını ver" → Kütüphaneci raflarda ARAR → bulur → verir
  → Sen rafları, katalog sistemini, Dewey Decimal'ı BİLMEZSİN!
  → Sadece "kitabı ver" dersin!

  Repository = Kütüphaneci! 📖
```

```javascript
// Repository INTERFACE (domain katmanında tanımlanır)
class OrderRepository {
  async findById(orderId) {
    throw new Error('Not implemented');
  }

  async save(order) {
    throw new Error('Not implemented');
  }

  async findByMemberId(memberId) {
    throw new Error('Not implemented');
  }
}

// Repository IMPLEMENTATION (infrastructure katmanında)
class PostgresOrderRepository extends OrderRepository {
  #db;

  constructor(dbConnection) {
    super();
    this.#db = dbConnection;
  }

  async findById(orderId) {
    const row = await this.#db.query(
      'SELECT * FROM orders WHERE id = $1', [orderId]
    );
    if (!row) return null;

    const items = await this.#db.query(
      'SELECT * FROM order_items WHERE order_id = $1', [orderId]
    );

    // DB satırlarından → Domain nesnesine dönüştür (hydration)
    return this.#toDomain(row, items);
  }

  async save(order) {
    // Domain nesnesinden → DB satırlarına dönüştür (dehydration)
    await this.#db.query(
      `INSERT INTO orders (id, member_id, status, shipping_address)
       VALUES ($1, $2, $3, $4)
       ON CONFLICT (id) DO UPDATE SET status = $3`,
      [order.id, order.memberId, order.status, order.shippingAddress]
    );
    // Items da kaydet...
  }

  #toDomain(row, items) {
    const order = new Order(row.id, row.member_id, /* ... */);
    // ... items ekle, durumu set et
    return order;
  }
}

// Test için IN-MEMORY implementation
class InMemoryOrderRepository extends OrderRepository {
  #orders = new Map();

  async findById(orderId) {
    return this.#orders.get(orderId) || null;
  }

  async save(order) {
    this.#orders.set(order.id, order);
  }
}

// → Domain kodu AYNI, altyapı DEĞİŞEBİLİR!
// → Test: InMemoryOrderRepository → DB'siz, hızlı test! ✅
// → Production: PostgresOrderRepository → gerçek DB ✅
```

### Repository Kuralları

```
1. HER AGGREGATE ROOT için BİR repository
   → OrderRepository ✅
   → OrderItemRepository ❌ (OrderItem aggregate root DEĞİL!)
   → Aggregate bütün olarak yüklenir ve kaydedilir

2. Repository DAİMA bütün aggregate'i döner
   → findById → Order + tüm OrderItem'ları + ShippingAddress → HEPSİ!
   → Kısmi yükleme YOK (aggregate BÜTÜNDÜR!)

3. Repository sadece COLLECTION semantiği sunar
   → Ekleme, bulma, silme → koleksiyon gibi!
   → İÇİNDE ne olduğu (SQL, MongoDB, dosya) → domain bilmez!

4. Karmaşık sorgular → AYRI QUERY SERVİSİ
   → "Son 7 günde 1000 TL üzeri siparişler?" → Raporlama sorgusu
   → Repository'nin işi DEĞİL! → ReadModel / Query Service kullan (CQRS!)
```

---

## 8. ⚙️ Service (Servis)

### Tanım

```
DOMAIN SERVICE = Hiçbir entity veya value object'e AİT OLMAYAN
                 domain mantığı

PROBLEM:
  → Havale işlemi: A hesabından B hesabına para transferi
  → Bu mantık KİME ait?
  → A hesabına mı? → A.transfer(B, amount) → garip!
  → B hesabına mı? → B.receive(A, amount) → garip!
  → İkisine de AİT DEĞİL! → DOMAIN SERVICE!
```

```javascript
// ❌ ZORLANMIŞ: Transfer mantığı hesaba konulmuş
class Account {
  transferTo(targetAccount, amount) {
    this.withdraw(amount);
    targetAccount.deposit(amount);
    // → Account başka bir Account'u bilmek ZORUNDA MI?
    // → Single Responsibility ihlali!
  }
}

// ✅ İYI: Domain Service
class TransferService {
  async execute(sourceAccountId, targetAccountId, amount) {
    const source = await this.accountRepo.findById(sourceAccountId);
    const target = await this.accountRepo.findById(targetAccountId);

    if (!source || !target) {
      throw new Error('Hesap bulunamadı!');
    }

    // İŞ KURALLARI:
    if (source.balance.isLessThan(amount)) {
      throw new InsufficientFundsError();
    }
    if (source.isBlocked || target.isBlocked) {
      throw new BlockedAccountError();
    }

    source.withdraw(amount);  // Entity kendi mantığını çalıştırır
    target.deposit(amount);   // Entity kendi mantığını çalıştırır

    await this.accountRepo.save(source);
    await this.accountRepo.save(target);

    return new TransferCompleted(sourceAccountId, targetAccountId, amount);
  }
}
```

### Servis Türleri

```
1. DOMAIN SERVICE (Domain katmanı)
   → İş kuralları, birden fazla aggregate'i kapsayan mantık
   → TransferService, PricingService, ShippingCalculator
   → STATELESS! (kendi durumu yok)
   → Ubiquitous Language'den gelir

2. APPLICATION SERVICE (Uygulama katmanı)
   → Use case orkestrasyon
   → Transaction yönetimi, yetkilendirme, event yayınlama
   → Domain mantığı İÇERMEZ!
   → "Sipariş onayla" use case'ini koordine eder

3. INFRASTRUCTURE SERVICE (Altyapı katmanı)
   → E-posta gönderme, mesaj kuyruğu, dosya sistemi
   → Teknik kaygılar, domain ile İLGİSİZ

AYRIM ÖNEMLİ:
  ❌ Application Service'e iş kuralı KOYMA!
  ❌ Domain Service'e transaction/auth KOYMA!
  ✅ Her servis kendi katmanının sorumluluğunda!
```

```javascript
// APPLICATION SERVICE (orkestrasyon, domain mantığı YOK!)
class ConfirmOrderUseCase {
  #orderRepo;
  #eventBus;
  #authService;

  constructor(orderRepo, eventBus, authService) {
    this.#orderRepo = orderRepo;
    this.#eventBus = eventBus;
    this.#authService = authService;
  }

  async execute(orderId, userId) {
    // 1. Yetkilendirme (infrastructure concern)
    await this.#authService.ensureCanConfirmOrder(userId);

    // 2. Aggregate'i yükle
    const order = await this.#orderRepo.findById(orderId);
    if (!order) throw new OrderNotFoundError(orderId);

    // 3. Domain mantığını ÇAĞIR (kendisi domain bilmez!)
    const event = order.confirm(); // İş kuralları Entity İÇİNDE! ✅

    // 4. Kaydet
    await this.#orderRepo.save(order);

    // 5. Event yayınla
    await this.#eventBus.publish(event);
  }
}
```

---

## 9. 🏭 Factory (Fabrika)

### Tanım

```
FACTORY = Karmaşık nesnelerin OLUŞTURULMA mantığını ayır

SORUN: Aggregate oluşturmak KARMAŞIKsa → constructor şişer!

  new Order(id, memberId, items, shippingAddress, billingAddress,
            couponCode, loyaltyPoints, giftWrapping, note, ...);
  // → 15 parametre! Constructor KABUS! 😱

ÇÖZÜM: Factory!
```

```javascript
// Factory — karmaşık oluşturmayı yönetir
class OrderFactory {
  #idGenerator;
  #memberRepo;
  #productRepo;

  constructor(idGenerator, memberRepo, productRepo) {
    this.#idGenerator = idGenerator;
    this.#memberRepo = memberRepo;
    this.#productRepo = productRepo;
  }

  async createOrder(memberId, cartItems, shippingAddressData) {
    // 1. Üyeyi doğrula
    const member = await this.#memberRepo.findById(memberId);
    if (!member) throw new MemberNotFoundError(memberId);
    if (member.isBlocked) throw new BlockedMemberError(memberId);

    // 2. ID üret
    const orderId = this.#idGenerator.generate();

    // 3. Adres value object oluştur
    const shippingAddress = new Address(
      shippingAddressData.city,
      shippingAddressData.district,
      shippingAddressData.street,
      shippingAddressData.zipCode
    );

    // 4. Siparişi oluştur
    const order = new Order(orderId, memberId, shippingAddress);

    // 5. Ürünleri ekle ve fiyatları doğrula
    for (const cartItem of cartItems) {
      const product = await this.#productRepo.findById(cartItem.productId);
      if (!product) throw new ProductNotFoundError(cartItem.productId);
      if (!product.isAvailable) throw new ProductUnavailableError(product.name);

      order.addItem(
        product.id,
        product.name,
        product.currentPrice, // Güncel fiyat!
        cartItem.quantity
      );
    }

    return order;
  }
}

// Kullanım:
const orderFactory = new OrderFactory(idGen, memberRepo, productRepo);
const order = await orderFactory.createOrder('member-1', cartItems, addressData);
// → Tüm karmaşık oluşturma mantığı TEK yerde! ✅
```

---

## 10. 📡 Domain Event (Alan Olayı)

### Tanım

```
DOMAIN EVENT = Domain'de gerçekleşen ÖNEMLİ bir olay

"Bir şey OLDU" → Geçmiş zaman!
→ OrderConfirmed (Sipariş onaylandı)
→ PaymentReceived (Ödeme alındı)
→ MemberRegistered (Üye kaydoldu)
→ ProductPriceChanged (Ürün fiyatı değişti)

NEDEN ÖNEMLİ?
  → Aggregate'ler arası İLETIŞIM
  → Eventual consistency sağlama
  → Audit trail (iz bırakma)
  → Diğer bounded context'leri bilgilendirme
```

```javascript
// Domain Event tanımı
class OrderConfirmed {
  constructor(orderId, memberId, totalAmount, confirmedAt) {
    this.eventType = 'OrderConfirmed';
    this.orderId = orderId;
    this.memberId = memberId;
    this.totalAmount = totalAmount;
    this.confirmedAt = confirmedAt || new Date();
    this.eventId = generateUUID(); // Her event benzersiz!
    Object.freeze(this); // Event IMMUTABLE! ✅
  }
}

// Event'i kim dinler?
// → Stok servisi: "Sipariş onaylandı → stoku DÜŞÜR!"
// → Ödeme servisi: "Sipariş onaylandı → ödeme BAŞLAT!"
// → Bildirim servisi: "Sipariş onaylandı → e-posta GÖNDER!"
// → Analitik: "Sipariş onaylandı → metriği GÜNCELLE!"

// Event handler
class StockReservationHandler {
  #productRepo;

  constructor(productRepo) {
    this.#productRepo = productRepo;
  }

  async handle(event) {
    if (event.eventType !== 'OrderConfirmed') return;

    // Stok azaltma mantığı
    for (const item of event.items) {
      const product = await this.#productRepo.findById(item.productId);
      product.reserveStock(item.quantity);
      await this.#productRepo.save(product);
    }
  }
}
```

### Event'lerin Gücü

```
BEZ AGGREGATE SİPARİŞ AKIŞI:

  ┌─────────┐  OrderConfirmed  ┌──────────┐  PaymentReceived  ┌─────────┐
  │ Order   │─────────────────→│ Payment  │──────────────────→│ Shipping│
  │ Context │                  │ Context  │                   │ Context │
  └─────────┘                  └──────────┘                   └─────────┘

  Her context kendi aggregate'ini yönetir
  İletişim: EVENT ile! (doğrudan çağrı değil!)
  → Loosely coupled! Bir context diğerinin İÇ YAPISINI bilmez!

  Order: "Ben onaylandım!" (OrderConfirmed event)
  Payment: "Tamam, ödemeyi alayım" (event'i dinler)
  Payment: "Ödeme alındı!" (PaymentReceived event)
  Shipping: "Tamam, kargoyu başlatayım" (event'i dinler)

  → Her context BAĞIMSIZ!
  → Payment çöktüğünde → Order ETKİLENMEZ!
  → Event kuyrukte BEKLEr → Payment ayağa kalkınca İŞLER! ✅
```

---

## 11. 📂 Module (Modül)

### Modül = Kavramsal Gruplama

```
MODÜLler = İlişkili kavramları GRUPLA

İyi modül yapısı:

src/
  domain/
    order/                    ← Order Modülü
      Order.js                (Aggregate Root)
      OrderItem.js            (Entity)
      OrderStatus.js          (Value Object / Enum)
      OrderRepository.js      (Repository Interface)
      OrderConfirmed.js       (Domain Event)
      OrderFactory.js         (Factory)
      ShippingAddress.js      (Value Object)
    
    member/                   ← Member Modülü
      Member.js
      MemberRepository.js
      Email.js                (Value Object)
      MemberRegistered.js     (Domain Event)
    
    product/                  ← Product Modülü
      Product.js
      ProductRepository.js
      Money.js                (Value Object — paylaşılan)
      ProductPriceChanged.js

  application/
    usecases/
      ConfirmOrderUseCase.js
      RegisterMemberUseCase.js
    
  infrastructure/
    persistence/
      PostgresOrderRepository.js
      PostgresMemberRepository.js
    messaging/
      RabbitMQEventBus.js

→ Modüller Ubiquitous Language'den gelir!
→ "order", "member", "product" → İŞ TERİMLERİ!
→ "utils", "helpers", "managers" → TEKNİK TERİMLER → KÖTÜ! ❌
```

---

## 12. 🏰 Bounded Context (Sınırlı Bağlam)

### DDD'nin STRATEJİK Kalbi

```
BOUNDED CONTEXT = Belirli bir modelin GEÇERLİ olduğu SINIR

PROBLEM: "Müşteri" nedir?
  → Satış: "Müşteri = satın alan kişi, kredi limiti, satın alma geçmişi"
  → Kargo: "Müşteri = teslimat yapılacak kişi, adres, telefon"
  → Muhasebe: "Müşteri = fatura kesilen kişi, vergi no, cari hesap"
  → Destek: "Müşteri = şikayet eden kişi, bilet geçmişi, SLA"

  AYNI KELİME → FARKLI ANLAMLAR → FARKLI BAĞLAMLAR!

  Tek bir "Customer" class'ı HEPSİNİ kapsamaya çalışırsa:
  → 50+ alan, 200+ metod → GOD OBJECT! 💀
  → Satış değişikliği kargo testlerini KIRIYOR!
  → Herkes birbirinin ayağına BASIYOR!

ÇÖZÜM: Her bağlamın KENDİ "Müşteri" tanımı olsun!

  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
  │ Satış Context    │  │ Kargo Context   │  │ Muhasebe Context│
  │                 │  │                 │  │                 │
  │ Customer:       │  │ Recipient:      │  │ Debtor:         │
  │ - name          │  │ - name          │  │ - companyName   │
  │ - creditLimit   │  │ - address       │  │ - taxId         │
  │ - purchaseHx    │  │ - phone         │  │ - balance       │
  │ - preferences   │  │ - deliveryNotes │  │ - invoices      │
  └─────────────────┘  └─────────────────┘  └─────────────────┘

  → FARKLI isimler! (Customer ≠ Recipient ≠ Debtor)
  → FARKLI alanlar!
  → FARKLI modeller!
  → Her biri kendi bağlamında TUTARLI ve BASİT!
```

### Bounded Context = Microservice?

```
KISA CEVAP: Genellikle EVET, ama her zaman değil!

  Bounded Context → mantıksal sınır (KAVRAMSAL)
  Microservice → fiziksel sınır (TEKNİK)

  İYİ BAŞLANGIÇ:
  → 1 Bounded Context = 1 Microservice
  → Her context kendi veritabanına sahip
  → Her context bağımsız deploy edilebilir
  → Context sınırları = takım sınırları (Conway's Law!)

  AMA:
  → Yeni sistemde: 1 monolith içinde birden fazla context OLABİLİR
  → Olgunlaşınca: Context'leri microservice'e AYIR
  → Monolith First yaklaşımı! (Building Microservices'ten hatırlarsın!)

  SIRA:
  1. Bounded Context'leri BELİRLE (strategic design)
  2. Context'ler arası ilişkileri HARİTALA
  3. Monolith'te ayrı modüller olarak KODLA
  4. Gerektiğinde microservice'e AYIR
  → ASLA "her entity'yi microservice yapalım!" YAPMA! ❌
```

---

## 13. 🗺️ Context Map (Bağlam Haritası)

### Context'ler Arası İlişkiler

```
Context'ler İZOLE değil → birbirleriyle İLETIŞİR!
Context Map = bu ilişkilerin HARİTASI

İLIŞKI PATTERNLERİ:

1. SHARED KERNEL (Paylaşılan Çekirdek) 🤝
   → İki context AYNI modeli paylaşıyor
   → Dikkat: Değişiklik İKİSİNİ de etkiler!
   → Küçük tut! Yalnızca GERÇEKTEN paylaşılması gereken kısım!

   ┌────────┐  paylaşılan  ┌────────┐
   │ Ctx A  │──── kod ─────│ Ctx B  │
   └────────┘              └────────┘

2. CUSTOMER-SUPPLIER (Müşteri-Tedarikçi) 🏪
   → Upstream (tedarikçi) → API sağlar
   → Downstream (müşteri) → API'yi kullanır
   → Downstream'in ihtiyaçları upstream'in yol haritasını ETKİLER

   [Upstream: Ürün Ctx] →→→ [Downstream: Sipariş Ctx]
   "İhtiyacını söyle, API'yi GÜNCELLERİM"

3. CONFORMIST (Uyumcu) 😔
   → Upstream DEĞİŞTİRMEZ → Downstream UYMAK ZORUNDA!
   → Genelde 3. parti API'ler (Stripe, Twilio)
   → "Api böyle, BEĞENMİYORSAN KULLANMA!"

4. ANTI-CORRUPTION LAYER (ACL) 🛡️
   → Downstream kendini upstream'in modelinden KORUR
   → Çeviri katmanı ekler (en önemli pattern!)

5. OPEN HOST SERVICE + PUBLISHED LANGUAGE 📖
   → Upstream herkese açık, iyi tanımlanmış API sunar
   → REST API + Swagger/OpenAPI → Published Language!

6. SEPARATE WAYS (Ayrı Yollar) 🔀
   → İki context HİÇ iletişim kurmuyor
   → Her biri bağımsız → en basit! ✅
   → "İletişim maliyeti > faydası" ise → ayır!

7. PARTNERSHIP (Ortaklık) 🤜🤛
   → İki takım BİRLİKTE evrilir
   → Senkronize değişiklik yapıyorlar
   → Güçlü koordinasyon gerekli
```

### Bir Şirketin Context Map'i

```
┌─────────────────────────────────────────────────────────┐
│                     CONTEXT MAP                          │
│                                                         │
│  ┌─────────┐   C/S    ┌──────────┐   C/S   ┌────────┐ │
│  │ Product │ ───────→ │  Order   │ ──────→ │ Ship.  │ │
│  │ Catalog │          │ Mgmt     │         │ & Del. │ │
│  └─────────┘          └─────┬────┘         └────────┘ │
│                              │                         │
│                       Domain Event                     │
│                              │                         │
│                        ┌─────▼────┐                    │
│                        │ Payment  │                    │
│                        └─────┬────┘                    │
│                              │                         │
│                         ACL  │                         │
│                              │                         │
│                        ┌─────▼────┐                    │
│                        │ Stripe   │  (3rd party)       │
│                        │ (Conform)│                    │
│                        └──────────┘                    │
│                                                         │
│  ┌──────────┐  Separate Ways  ┌──────────┐            │
│  │ CRM      │                 │ Analytics│            │
│  │          │                 │          │            │
│  └──────────┘                 └──────────┘            │
│                                                         │
│  C/S = Customer-Supplier                               │
│  ACL = Anti-Corruption Layer                           │
└─────────────────────────────────────────────────────────┘
```

---

## 14. 🛡️ Anti-Corruption Layer (ACL)

### En Önemli Entegrasyon Pattern'ı

```
SORUN:
  → 3. parti API veya legacy sistem kullanıyorsun
  → Onların modeli SENİN modeline UYMUYOR
  → Onların değişiklikleri SENİN kodunu BOZUYOR

ÖRNEK: Ödeme sistemi
  Stripe API: { "amount": 1000, "currency": "usd" }  ← cent cinsinden!
  Senin modelin: new Money(10, 'USD')                  ← dolar cinsinden!

  Stripe değişiklik yaptı → SENİN domain kodun BOZULDU! 💀

ÇÖZÜM: ACL = Çeviri katmanı!
```

```javascript
// ❌ KÖTÜ: Domain kodu doğrudan Stripe'a bağımlı
class OrderService {
  async processPayment(order) {
    // Domain kodu Stripe'ın API yapısını BİLİYOR → BAĞIMLILIK!
    const result = await stripe.charges.create({
      amount: order.totalAmount.amount * 100, // cent'e çevir!
      currency: order.totalAmount.currency.toLowerCase(),
      source: order.paymentToken,
    });
    
    if (result.status === 'succeeded') { // Stripe'a özgü durum!
      order.markAsPaid();
    }
  }
}
// → Stripe API değişirse → domain kodu KIRILIR!
// → Test etmek ZOR (Stripe mock'lamak lazım!)

// ✅ İYI: Anti-Corruption Layer ile
// 1. Domain'in kendi ödeme INTERFACE'ı
class PaymentGateway {
  async charge(amount, paymentMethod) {
    throw new Error('Not implemented');
  }
}

class PaymentResult {
  #success;
  #transactionId;
  #failureReason;

  constructor(success, transactionId, failureReason = null) {
    this.#success = success;
    this.#transactionId = transactionId;
    this.#failureReason = failureReason;
    Object.freeze(this);
  }

  get isSuccessful() { return this.#success; }
  get transactionId() { return this.#transactionId; }
  get failureReason() { return this.#failureReason; }
}

// 2. ACL: Stripe'ı DOMAIN modeline çevir
class StripePaymentGateway extends PaymentGateway {
  #stripeClient;

  constructor(stripeClient) {
    super();
    this.#stripeClient = stripeClient;
  }

  async charge(amount, paymentMethod) {
    try {
      const result = await this.#stripeClient.charges.create({
        amount: amount.amount * 100,  // Çeviri BURADA! Domain bilmez!
        currency: amount.currency.toLowerCase(),
        source: paymentMethod.token,
      });

      // Stripe sonucunu → Domain sonucuna çevir
      return new PaymentResult(
        result.status === 'succeeded',
        result.id,
        result.failure_message
      );
    } catch (error) {
      return new PaymentResult(false, null, error.message);
    }
  }
}

// 3. Domain kodu TEMİZ kalır!
class OrderService {
  #paymentGateway; // Interface'e bağımlı, Stripe'a DEĞİL!

  async processPayment(order) {
    const result = await this.#paymentGateway.charge(
      order.totalAmount,
      order.paymentMethod
    );

    if (result.isSuccessful) {
      order.markAsPaid(result.transactionId);
    } else {
      order.markPaymentFailed(result.failureReason);
    }
  }
}

// → Stripe → PayPal'a geçmek istersen?
// → Sadece PayPalPaymentGateway yaz!
// → Domain kodu HİÇ DEĞİŞMEZ! ✅
```

---

## 15. 🎯 Strategic Design

### Core, Supporting, Generic Domain

```
HER İŞ 3 tür domain'den oluşur:

1. CORE DOMAIN (Çekirdek Alan) 💎
   → İşin REKABET AVANTAJI
   → "Bu olmazsa iş BATARIN!" kısmı
   → En iyi mühendisler BURADA çalışmalı!
   → Kendi geliştir, DIŞ KAYNAK KULLANMA!

   Örnekler:
   → Getir: Teslimat optimizasyonu, sipariş deneyimi
   → Netflix: Öneri algoritması, streaming altyapısı
   → Google: Arama algoritması

2. SUPPORTING DOMAIN (Destekleyici Alan) 🔧
   → Core'u DESTEKLER ama rakiplerden AYIRMAZ
   → Özel geliştirme gerekebilir (off-the-shelf olmaz)
   → Ama core kadar YATIRIM gerektirmez

   Örnekler:
   → Getir: Kurye yönetimi, menü yönetimi
   → Netflix: İçerik yönetimi
   → Google: Reklam yönetimi

3. GENERIC DOMAIN (Genel Alan) 📦
   → Sektörde STANDART olan çözümler
   → Off-the-shelf ürün AL veya dış kaynak kullan!
   → Kendin yazmak ZAMAN KAYBI!

   Örnekler:
   → Ödeme: Stripe, iyzico kullan → kendin YAZMA!
   → Kimlik doğrulama: Auth0, Keycloak kullan
   → E-posta: SendGrid, SES kullan
   → Muhasebe: Logo, Parasut kullan

ALTIN KURAL:
  "Core domain'e EN İYİ mühendisleri koy.
   Generic domain'i SATIN AL.
   Supporting domain'i YETER düzeyde geliştir."
```

### Distillation (Damıtma)

```
Core domain'i SAFLAŞTIR → gereksiz karmaşıklığı ÇIKAR!

"Altından ayrıştır, taşları AT!"

ADIMLAR:
  1. Domain'deki TÜM kavramları listele
  2. Hangisi CORE? → Rekabet avantajı mı?
  3. Core OLMAYANLAR → Supporting veya Generic'e TAŞI
  4. Core'u sürekli refine et → DAHA SADE, DAHA GÜÇLÜ

DOMAIN VISION STATEMENT:
  → 1 paragraf: "Bu domain NE yapıyor ve NEDEN önemli?"
  → Herkes bunu OKUYABİLMELİ ve ANLAMALI

  Örnek:
  "Sipariş yönetimi sistemi, üyelerin ürün seçiminden teslimatına
   kadar olan satın alma sürecini yönetir. Fiyatlandırma, kampanya
   uygulaması ve stok kontrolü ile entegre çalışarak kesintisiz
   bir alışveriş deneyimi sunar. Rekabet avantajımız: anlık
   fiyat optimizasyonu ve kişiselleştirilmiş kampanya önerisi."
```

---

## 16. 🧬 Supple Design (Esnek Tasarım)

### Intention-Revealing Interfaces

```
İNTERFACE metod adı, NE yapıldığını AÇIKÇA anlatmalı!

❌ process(data)    → NE işliyor? BELLİ DEĞİL!
❌ handle(event)    → NASIL handle ediyor? BELLİ DEĞİL!
❌ doStuff()        → ... 😤

✅ confirmOrder()                → Siparişi ONAYLIYOR
✅ calculateShippingCost()       → Kargo ÜCRETİNİ HESAPLIYOR
✅ reserveStock(productId, qty)  → Stok AYIRIYOR
✅ applyDiscountCoupon(code)     → İndirim kuponu UYGULUYOR

"Metod adını oku → KODU OKUMADAN ne yaptığını BİL!"
```

### Side-Effect-Free Functions

```
Sorgu metodları DEĞİŞİKLİK YAPMAMALI!

❌ KÖTÜ:
order.calculateTotal()  // hesaplıyor VE DB'ye YAZIYOR!
                        // → yan etki! sürpriz! 💀

✅ İYI:
order.calculateTotal()  // SADECE hesaplıyor, bir şey DEĞİŞTİRMİYOR
order.confirm()         // değişiklik yapıyor → ADI BELLİ!

CQS (Command Query Separation):
  → QUERY: Veri döner, durum DEĞİŞTİRMEZ
  → COMMAND: Durum değiştirir, veri DÖNMEZ (veya minimal)

  order.totalAmount     → QUERY (okuma, yan etki yok)
  order.confirm()       → COMMAND (yazma, durum değişir)
  → İkisini KARISTIRMA!
```

### Assertions & Invariants

```
INVARIANT = Her zaman DOGRU olması gereken kural

Sipariş invariant'ları:
  → Sipariş toplamı NEGATIF olamaz!
  → Sipariş en az 1 ürün İÇERMELİ (onaylanmışsa)!
  → Kargo adresi BOŞ olamaz (onaylanmışsa)!

Bu kurallar AGGREGATE İÇİNDE KORUNUR:

class Order {
  confirm() {
    // Invariant kontrolleri
    this.#assertNotEmpty();
    this.#assertHasShippingAddress();
    this.#assertTotalIsPositive();
    
    this.#status = OrderStatus.CONFIRMED;
  }

  #assertNotEmpty() {
    if (this.#items.length === 0) {
      throw new InvariantViolation('Sipariş boş olamaz!');
    }
  }

  #assertHasShippingAddress() {
    if (!this.#shippingAddress) {
      throw new InvariantViolation('Kargo adresi gerekli!');
    }
  }
}

// Aggregate invariant'ları koruyan KALE'dir! 🏰
// Dış dünya ne yaparsa yapsın, invariant'lar HEP GEÇERLİ!
```

---

## 17. 🎯 Event Storming

### Domain Keşif Atölyesi

```
EVENT STORMING = Alberto Brandolini'nin icadı
→ Büyük bir duvar + turuncu post-it'ler + İŞ UZMANLARI + geliştiriciler
→ Domain'i keşfetmenin EN ETKİLİ yolu! 🎯

NASIL YAPILIR?

ADIM 1: DOMAIN EVENT'LERİ YAZAR (Turuncu post-it) 🟧
  → "Geçmişte ne OLDU?"
  → SiparişOluşturuldu, ÖdemeAlındı, KargoGönderildi, İadeYapıldı
  → Herkes AYNI ANDA yapıştırır → kaotik ama verimli!
  → Kronolojik sırada → soldan sağa zaman akışı

  ──────────────────── ZAMAN ──────────────────→
  [Üye         [Ürün        [Sipariş     [Ödeme      [Kargo
   Kaydoldu]    Sepete       Oluşturuldu]  Alındı]     Gönderildi]
                Eklendi]

ADIM 2: COMMAND'LER ekle (Mavi post-it) 🟦
  → "Bu event'i kim/ne TETİKLEDİ?"
  → SiparişiOnayla → SiparişOnaylandı
  → ÖdemeyiAl → ÖdemeAlındı

ADIM 3: AGGREGATE'LER ekle (Sarı post-it) 🟨
  → "Bu command hangi aggregate'e gidiyor?"
  → SiparişiOnayla → [Sipariş] → SiparişOnaylandı

ADIM 4: BOUNDED CONTEXT'LER çiz 🔲
  → İlişkili event + command + aggregate kümelerini DAIRE içine al
  → Her daire = potansiyel Bounded Context!

SONUÇ: Duvarın üzerinde TÜM domain görünür! 🗺️
  → Herkes AYNI RESMİ görüyor
  → Ubiquitous Language doğal olarak OLUŞUYOR
  → Context sınırları BELİRGİNLEŞİYOR
  → İş uzmanları ve geliştiriciler BIRLIKTE keşfediyor! ✅
```

---

## 18. 📊 CQRS ve Event Sourcing

### CQRS (Command Query Responsibility Segregation)

```
CQRS = OKUMA ve YAZMA modellerini AYIR!

GELENeksel:
  ┌──────────┐
  │ AYNI     │ ← Yazma (INSERT/UPDATE)
  │ MODEL    │ ← Okuma (SELECT)
  └──────────┘
  → Karmaşık JOIN'ler, yavaş sorgular
  → Yazma optimizasyonu okumayı BOZAR (veya tersi)

CQRS:
  ┌──────────┐                 ┌──────────┐
  │ YAZMA    │  ─── event ───→ │ OKUMA    │
  │ MODELİ   │                 │ MODELİ   │
  │ (Command)│                 │ (Query)  │
  └──────────┘                 └──────────┘
  Normalize DB                 Denormalize / cache
  İş kuralları                 Hızlı sorgular
  Aggregate'ler                Flat view'lar

NEDEN?
  → Okuma ve yazma İHTİYAÇLARI farklı!
  → Yazma: Tutarlılık, iş kuralları, validation
  → Okuma: Hız, esnek sorgular, JOIN'siz flat veri

  E-ticaret: Sipariş yazma 500/sn, okuma 50,000/sn
  → Farklı ölçekleme! Okuma modelini CACHE + denormalize! ✅
```

### Event Sourcing

```
EVENT SOURCING = Durumu KAYDETMEK yerine, OLAYLARI kaydet!

GELENeksel: Mevcut durumu DB'ye yaz (snapshot)
  orders: { id: 1, status: 'shipped', total: 150 }
  → "Geçmiş ne oldu?" → BİLİNMEZ! Sadece şimdiki durum var!

Event Sourcing: OLAYLARI kaydet, durumu olaylardan HESAPLA
  events:
    1. OrderCreated { orderId: 1, memberId: 5 }
    2. ItemAdded { orderId: 1, productId: 10, qty: 2 }
    3. ItemAdded { orderId: 1, productId: 20, qty: 1 }
    4. OrderConfirmed { orderId: 1 }
    5. PaymentReceived { orderId: 1, amount: 150 }
    6. OrderShipped { orderId: 1, trackingNo: 'TR123' }

  → Mevcut durum = tüm event'leri BAŞTAN OYNAT (replay!)
  → "3. adımda sipariş nasıldı?" → İlk 3 event'i oynat → O ANDAKİ durumu bil!
  → TAM AUDİT LOG! Hiçbir bilgi KAYBOLMAZ!
  → Zaman yolculuğu YAPABİLİRSİN! ⏰

DİKKAT:
  → Event store BÜYÜR → snapshot'lar ile optimize et
  → Event schema'sı DEĞİŞİRSE → event upcasting gerekir
  → KARMAŞIK! Her sistem için GEREKMEZ!
  → Kullan: Finansal sistemler, audit gerektiren sistemler, karmaşık domain
  → Kullanma: Basit CRUD uygulamalar
```

---

## 19. 🔬 DDD ve Microservices

### DDD Microservices'in TEMELİDİR

```
Microservices SINIRlarını NASIL çizersin?

❌ KÖTÜ SINIRLAR (Teknik bölme):
  → User Service, Order Service, Database Service, Notification Service
  → Her service'in "neden ayrı olduğu" BELLİ DEĞİL
  → Dağıtık monolith! (en kötüsü!)

✅ İYI SINIRLAR (Domain bölme = Bounded Context!):
  → Sipariş Yönetimi Context → Order Service
  → Ödeme Context → Payment Service
  → Kargo Context → Shipping Service
  → Ürün Kataloğu Context → Product Service
  → Her service kendi BOUNDED CONTEXT'i!

KURALLAR:
  1. 1 Bounded Context ≥ 1 Microservice
     (1 context = N service OLABİLİR ama 1 service ≠ N context!)

  2. Her service kendi VERİTABANINA sahip
     → Context'ler arası JOIN YOK! (Database per service)

  3. İletişim: Domain Event ile (asenkron) veya API ile (senkron)
     → Asenkron TERCIH ET! Daha loose coupling!

  4. Aggregate sınırları = API sınırları
     → Bir aggregate response'da → BİR API call ile tamamlanmalı!
```

### DDD Katmanlı Mimari

```
┌──────────────────────────────────────┐
│         PRESENTATION LAYER          │
│  (REST API, GraphQL, gRPC)           │
│  → Route, DTO, Serialization         │
├──────────────────────────────────────┤
│         APPLICATION LAYER            │
│  (Use Cases, Orchestration)          │
│  → ConfirmOrderUseCase               │
│  → Transaction, Authorization        │
│  → Domain mantığı YOK!               │
├──────────────────────────────────────┤
│         DOMAIN LAYER 💎              │
│  (Entity, VO, Aggregate, Service)    │
│  → İŞ KURALLARININ KALBİ            │
│  → Hiçbir şeye BAĞIMLI DEĞİL!       │
│  → Framework bilmez, DB bilmez!      │
├──────────────────────────────────────┤
│         INFRASTRUCTURE LAYER         │
│  (Repository impl, Messaging,       │
│   External APIs, DB)                 │
│  → Teknik detaylar                   │
└──────────────────────────────────────┘

BAĞIMLILIK YÖNÜ (DIP — Dependency Inversion):
  Presentation → Application → Domain ← Infrastructure
                                  ↑           │
                                  └───────────┘
  → Domain MERKEZDE ve HİÇBİR ŞEYE BAĞIMLI DEĞİL!
  → Infrastructure domain'e bağımlı (tersi değil!)
  → Clean Architecture ile BİREBİR örtüşür! 🏛️
```

---

## 20. 🌍 Gerçek Hayata Uyarlama

### DDD Ne Zaman Kullanılmalı?

```
✅ KULLAN:
  → Karmaşık iş kuralları (e-ticaret, finans, sigorta, sağlık)
  → Domain uzmanlarıyla çalışıyorsun
  → Uzun ömürlü proje (yıllarca sürecek)
  → Takım büyük (5+ geliştirici)
  → Microservices mimarisi planlıyorsun

❌ KULLANMA (overkill):
  → Basit CRUD (blog, to-do list)
  → Prototip / MVP
  → Tek kişilik proje
  → İş kuralları basit ("kaydet, listele, sil")
  → KISS! → Karmaşıklık gerektirmeyen yere karmaşıklık EKLEME!

"DDD'yi HER YERDE kullanmak,
 tabak yıkamak için yangın söndürücü kullanmak gibidir." 🧯🍽️

DOĞRU YAKLAŞIM:
  → CORE DOMAIN'DE → TAM DDD (Aggregate, Event, Repository...)
  → SUPPORTING'TE → HAFİF DDD (Ubiquitous Language, Bounded Context)
  → GENERIC'TE → CRUD YETERLİ veya hazır çözüm kullan!
```

### Adım Adım Başla

```
"Yarından itibaren tüm kodu DDD ile yazacağız!" → BAŞARISIZ!

ADIM 1: Ubiquitous Language OLUŞTUR (bugün başla!)
  → İş uzmanlarıyla konuş
  → Terimleri BELGELE
  → Kodda İŞ terimleri kullan (User → Member/Customer/Guest)

ADIM 2: Bounded Context KESfET
  → Sistemdeki farklı BAĞLAMLARI belirle
  → Her bağlamın kendi modeli olsun
  → Context Map çiz

ADIM 3: Entity vs Value Object AYIR
  → "Bu nesnenin KİMLİGI önemli mi?"
  → Value Object'leri IMMUTABLE yap
  → İş kurallarını nesnelerin İÇİNE koy (Anemic Domain Model'den KURTUL!)

ADIM 4: Aggregate SINIRLARINI çiz
  → Transaction sınırları = Aggregate sınırları
  → Küçük tut!
  → Aggregate'ler arası → ID referans + domain event

ADIM 5: Repository ve Application Service EKLE
  → Persistence'ı SOYUTLA
  → Use case'leri Application Service'e TAŞI
  → Domain mantığını domain katmanında TUT

ADIM 6: Event-Driven iletişim EKLE
  → Aggregate'ler arası → domain event
  → Context'ler arası → integration event + message queue
```

### Anti-Pattern: Anemic Domain Model

```
EN YAYGIN DDD HATASI!

ANEMIC DOMAIN MODEL = Entity'ler sadece data tutuyor, iş kuralları DIŞARIDA!

❌ ANEMİK (KÖTÜ):
class Order {
  constructor() {
    this.id = null;
    this.status = null;
    this.items = [];
    this.total = 0;
  }
  // Sadece getter/setter! İŞ KURALI YOK!
}

class OrderService {
  confirmOrder(order) {
    if (order.items.length === 0) throw new Error('Boş!');
    if (!order.shippingAddress) throw new Error('Adres!');
    order.status = 'confirmed'; // Dışarıdan DEĞİŞTİRİYOR!
    order.total = order.items.reduce((s, i) => s + i.price * i.qty, 0);
    // TÜM mantık SERVİSTE! Entity boş kutu! 📦
  }
}
// → Order bir "veri çantası" → Entity olmanın ANLAMINI KAYBETMIŞ!
// → "Transaction Script" pattern'ı → DDD DEĞİL!

✅ RICH DOMAIN MODEL (İYI):
class Order {
  confirm() {
    // İş kuralları BENİM İÇİMDE! 💪
    if (this.#items.length === 0) throw new Error('Boş sipariş!');
    if (!this.#shippingAddress) throw new Error('Adres gerekli!');
    this.#status = OrderStatus.CONFIRMED;
    return new OrderConfirmed(this.#id, this.totalAmount);
  }
  // Entity KENDİ iş kurallarını BİLİR ve UYGULAR!
}
```

---

## 21. � Büyük Şirketlerde DDD

### Amazon — Bounded Context = Microservice

```
Amazon'ın "two-pizza team" yapısı DDD'nin ideal uygulaması:

  → Her ekip 1 Bounded Context sahiplenir
  → Bounded Context = Microservice sınırı
  → Ubiquitous Language ekip İÇİNDE geçerli
  → Ekipler arası: Published Language (API contract)

Jeff Bezos'un API Mandate:
  → "Ekipler SADECE servis arayüzü ile konuşacak"
  → Bu DDD'nin Context Map'indeki "Published Language" pattern'ı
  → Shared kernel YASAK → Open Host Service ile konuş
```

### Netflix — Event-Driven DDD

```
Netflix'in recommendation engine'i Event Sourcing kullanır:
  → UserWatchedEvent → model güncelle
  → UserRatedEvent → preference güncelle
  → Domain Event'ler Kafka ile akar

DDD + Microservices'teki en büyük hata:
  → Anemic Domain Model (iş kuralını SERVİS'e koymak)
  → Netflix bu tuzağa düşmemek için "Rich Domain Model" enforce eder
  → Entity iş kuralını BİLMELİ, service sadece ORKESTRASyon yapmalı
```

### Getir'de DDD Uygulanabilirliği

```
E-ticaret ve teslimat domain'i DDD için İDEAL:

  Sipariş Bağlamı (Order Context):
    → Order (Aggregate Root)
    → OrderItem (Entity)
    → Address (Value Object)
    → OrderPlaced, OrderDelivered (Domain Events)

  Teslimat Bağlamı (Delivery Context):
    → Delivery (Aggregate Root)
    → Route (Value Object)
    → CourierAssigned (Domain Event)

  İKİ bağlam arasında:
    → OrderPlaced event → Delivery context'e akar
    → Published Language: Event schema (JSON contract)
    → Farklı Ubiquitous Language: 
      Order context'te "sipariş", Delivery context'te "gönderi"
```

---

## 22. 🤖 Yapay Zeka Çağında DDD

### AI Domain Modellemede Yardımcı Olabilir mi?

```
DDD'nin kalbi: Domain uzmanıyla mühendis arasında DİYALOG
AI burada NASIL yardım eder?

  ✅ Event Storming kolaylaştırıcı:
     → "Bu domain'deki olayları çıkar" → ilk taslak
     → AMA: Domain uzmanı ONAYLAMALI

  ✅ Ubiquitous Language sözlüğü:
     → "Bu kod tabanındaki domain terimlerini bul ve sözlük oluştur"
     → Tutarsız kullanımları tespit et

  ✅ Aggregate sınır analizi:
     → "Bu entity'lerin hangisi birlikte DEĞİŞMELİ?"
     → Transactional consistency sınırlarını öner

  ❌ Strategic Design kararları:
     → "Bu iki ekip arasında Partnership mı, Customer-Supplier mı olmalı?"
     → Bu İNSAN ilişkisi — AI cevaplayamaz

  ❌ Ubiquitous Language OLUŞTURMA:
     → Dil domain uzmanıyla konuşarak KEŞFEDILIR
     → AI mevcut dili ANALİZ eder ama yeni dil YARATMAZ
```

### DDD-Uyumlu AI Promptları

```
AGGREGATE TASARIMİ:
  "Bu business domain'i analiz et ve Aggregate'ları tanımla.
   Eric Evans'ın kurallarını uygula:
   - Her Aggregate bir Root Entity'ye sahip olsun
   - Aggregate DIŞINDA referans: SADECE ID ile
   - Transactional boundary: Aggregate = 1 transaction
   - Invariant'lar (iş kuralları) Aggregate İÇİNDE enforce edilsin
   Domain: [domain açıklaması]"

VALUE OBJECT vs ENTITY:
  "Bu kavramların hangisi Value Object, hangisi Entity?
   Evans'ın kriterleri:
   - Identity önemli mi? → Entity
   - Sadece değerleri mi önemli? → Value Object
   - Immutable olabilir mi? → Value Object
   Kavramlar: [liste]"

CONTEXT MAP:
  "Bu microservice'ler arasındaki ilişkileri DDD Context Map
   pattern'larına göre sınıflandır:
   - Shared Kernel: Ortak model paylaşımı (TEHLİKELİ)
   - Customer-Supplier: Bir taraf diğerine hizmet verir
   - Conformist: Downstream upstream'e UYAR
   - Anti-Corruption Layer: Downstream kendini KORUR
   - Open Host Service: Published Language ile konuşur
   Servisler: [liste]"
```

### Topluluk Görüşleri

```
Eric Evans (DDD'nin yaratıcısı, 2023):
  "DDD'yi yazdığımda microservices YOKTU.
   Ama Bounded Context kavramı microservices için
   BİÇİLMİŞ KAFTAN oldu. Bu tesadüf değil —
   iyi soyutlamalar teknoloji değişse de geçerli kalır."

Vaughn Vernon (Implementing DDD yazarı):
  "Evans'ın kitabı STRATEJİK design'da mükemmel.
   Ama TAKTİK pattern'lar için benim kitabıma da bak.
   Özellikle Aggregate tasarım kuralları."

Alberto Brandolini (Event Storming yaratıcısı):
  "DDD'nin en zor kısmı KOD değil, İNSANLAR.
   Domain uzmanını ODADAYA al, beraber model et.
   Event Storming bunu KOLAYLAŞTIRIR."

Reddit r/softwaredevelopment:
  "DDD kitabını 3 kere okudum. İlk seferde HİÇ anlamadım.
   İkinci seferde 'stratejik kısım önemli, taktik kısım overrated' dedim.  
   Üçüncü okumada taktik kısmın da NE KADAR derin olduğunu gördüm.
   Evans'ın kitabını ACELE okuma."
```

---

## 23. �🎬 Son Sözler

### DDD Özet Kartı

```
┌──────────────────────────────────────────────────────────────┐
│                    DDD CHEAT SHEET                            │
├──────────────────────────────────────────────────────────────┤
│ STRATEGIC:                                                    │
│  → Ubiquitous Language: Herkes aynı dili konuşsun!           │
│  → Bounded Context: Modelin geçerli olduğu sınır            │
│  → Context Map: Context'ler arası ilişki haritası            │
│  → Core/Supporting/Generic: Yatırımı doğru yere yap!        │
│                                                              │
│ TACTICAL:                                                    │
│  → Entity: Kimliği olan, değişebilir nesne                  │
│  → Value Object: Kimliksiz, immutable, değerle tanımlı      │
│  → Aggregate: Tutarlılık sınırı, Root üzerinden erişim      │
│  → Repository: Aggregate persistence soyutlaması            │
│  → Domain Service: Hiçbir entity'ye ait olmayan iş kuralı   │
│  → Domain Event: "Bir şey oldu!" → bağlam arası iletişim   │
│  → Factory: Karmaşık nesne oluşturma                        │
│                                                              │
│ PRENSİPLER:                                                  │
│  → Model = Kod (ayrı doküman değil!)                        │
│  → İş kuralları domain'de (anemic model YASAK!)             │
│  → Aggregate küçük tut → eventual consistency kabul et      │
│  → ACL ile dış bağımlılıklardan KORUN                       │
│  → Core domain'e EN İYİ ekibi koy                           │
└──────────────────────────────────────────────────────────────┘
```

### Tüm Kitaplarla Bağlantı 🔗

```
📗 Grokking Algorithms → Algoritma bilgisi → modelleme kararları
📕 Clean Code → Temiz kod → Intention-Revealing Interface, iyi isimlendirme
📘 Pragmatic Programmer → DRY, ortogonalite → Bounded Context, tek sorumluluk
📙 Missing README → Takım çalışması → Ubiquitous Language, iş uzmanlarıyla iletişim
📗 Philosophy of Software Design → Deep modules → Aggregate, Repository soyutlaması
📘 Design Patterns → Factory, Observer → DDD Factory, Domain Event
📕 DDIA → Eventual consistency, replication → Aggregate arası tutarlılık
📙 Unit Testing → Entity ve VO testi → Domain logic testi!
📗 Refactoring → Anemic → Rich Model dönüşümü
🏛️ Clean Architecture → Dependency Rule → Domain katmanı bağımsız!
🏗️ Fundamentals of SA → Mimari stiller → Context = Microservice
🔬 Building Microservices → Bounded Context = Service sınırı!
🔥 Phoenix Project → Değer akışı → Value Stream = Domain Event akışı
🏗️ System Design → Ölçekleme → DDD ile doğru bölünmüş sistem iyi ölçeklenir
🔵 Domain-Driven Design → TÜM bunların FELSEFE ve MODEL temelidir!

DDD bir ARAÇ DEĞİLDİR.
DDD bir DÜŞÜNME BİÇIMIDİR.
"Sorunu ANLA, doğru MODELLE, kodda YAŞAT." 💎
```

### Faz 4 İlerleme Durumu 📊

```
FAZ 4 — Ustalık (18+ ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Domain-Driven Design          ✅  ← BURADASIN
  2. Software Arch: The Hard Parts ⬜
  3. The Staff Engineer's Path     ⬜
  4. Thinking in Systems           ⬜
```

---

> **"Yazılımın en zor kısmı KODLAMAK değildir.
> En zor kısım NEYİ kodlayacağını ANLAMAKTIR.
>
> İş uzmanları PROBLEMI bilir.
> Geliştiriciler ÇÖZÜMÜ bilir.
> DDD ikisini BİRLEŞTİRİR.
>
> Ubiquitous Language ile AYNI DİLİ konuş.
> Bounded Context ile SINIRLARINI çiz.
> Aggregate ile TUTARLILIĞINI koru.
> Domain Event ile AKIŞINI yönet.
>
> Ve her zaman hatırla:
> Kod, modelin kendisidir.
> Model, gerçekliğin anlamlandırılmış halidir.
> Hızlı ama yanlış modelden,
> yavaş ama doğru model HER ZAMAN iyidir.
>
> Çünkü yanlış model üzerine kurulan hız,
> eninde sonunda seni DURDURUR."** 🔵
