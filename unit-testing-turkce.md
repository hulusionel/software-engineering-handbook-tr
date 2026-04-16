# 🧪 Unit Testing — Principles, Practices, and Patterns — Türkçe Kapsamlı Rehber

> **"İyi testler yazmak, iyi kod yazmak kadar ZOR bir beceridir.
> Ama çoğu geliştirici testleri 'yazılması gereken bir angarya' olarak görür.
> Bu kitap, testlerin bir VARLIK mı yoksa YÜKÜMLÜLÜK mü olduğunu sorgulatır."**
> — Vladimir Khorikov

Bu kitap, "test yaz" demekle kalmaz — **hangi** testleri, **neden**, **nasıl** yazacağını
ve en önemlisi **hangi testleri YAZMAMAN** gerektiğini öğretir.

---

## 📖 İçindekiler

1. [Test Yazmanın Amacı](#1--test-yazmanın-amacı)
2. [İyi Testin 4 Sütunu](#2--i̇yi-testin-4-sütunu)
3. [Test Piramidi ve Oranlar](#3--test-piramidi-ve-oranlar)
4. [Kod Kategorileri ve Test Stratejisi](#4--kod-kategorileri-ve-test-stratejisi)
5. [Mock'lar, Stub'lar ve Test Doubles](#5--mocklar-stublar-ve-test-doubles)
6. [Mock'u Ne Zaman Kullan, Ne Zaman Kullanma](#6--mocku-ne-zaman-kullan-ne-zaman-kullanma)
7. [Üç Test Stili](#7--üç-test-stili)
8. [Refactoring ve Testler](#8--refactoring-ve-testler)
9. [Integration Test Stratejisi](#9--integration-test-stratejisi)
10. [Anti-Pattern'lar](#10--anti-patternlar)
11. [Test Best Practices](#11--test-best-practices)
12. [Code Coverage Metrikleri](#12--code-coverage-metrikleri--sayılar-yalan-söyler)
13. [Büyük Şirketlerde Test Kültürü](#13--büyük-şirketlerde-test-kültürü)
14. [Yapay Zeka Çağında Unit Testing](#14--yapay-zeka-çağında-unit-testing)
15. [Son Sözler](#15--son-sözler)

---

## 1. 🎯 Test Yazmanın Amacı

### Neden Test Yazıyoruz?

Çoğu kişi: "Bug bulmak için." ❌ — Bu tam doğru değil.

> **"Testlerin asıl amacı, projenin sürdürülebilir büyümesini sağlamaktır."**

```
Testsiz proje:

Hız
  │  🚀
  │ ╱╲
  │╱  ╲
  │    ╲
  │     ╲───────── (hız sürekli düşer)
  │              ╲
  └──────────────────→ Zaman

Başta hızlısın! Ama kod büyüdükçe:
  - "Bu değişiklik neyi bozar?" → BİLEMEZSİN
  - Her değişiklik korku → yavaşlık
  - Regresyon bug'ları → sürekli yangın söndürme 🔥

İyi testlerle proje:

Hız
  │            ╱──── (hız sabit veya artar)
  │          ╱
  │        ╱
  │      ╱
  │    ╱
  │  ╱  (başta biraz yavaş — test yazma maliyeti)
  └──────────────────→ Zaman

Başta yavaşsın AMA:
  - Refactoring güvenle yapılır ✅
  - Regresyon anında yakalanır ✅
  - Yeni feature ekleme hızı ARTARAK devam eder ✅
```

### ANCAK: Kötü testler HİÇ testten DAHA KÖTÜDÜR! ⚠️

```
Kötü testlerle proje:

Hız
  │
  │
  │  ╱╲
  │ ╱  ╲
  │╱    ╲
  │      ╲──────── (kötü testler yük olur!)
  │            ╲
  └──────────────────→ Zaman

Neden?
  - Her refactoring'de düzinelerce test KIRILIR (false positive)
  - Testleri düzeltmek, kodu düzeltmekten UZUN sürer
  - Ekip testleri "kapatmaya" veya "skip" etmeye başlar
  - Sonuç: Test var ama güven vermiyor = YÜKÜMLÜLÜK

Hedef: AZ ama DEĞERLİ test > ÇOK ama DEĞERSIZ test
```

### Test Süit = Bir Varlık mı, Yükümlülük mü?

Her test bir MALİYETTİR:
1. **Yazma maliyeti:** İlk yazma süresi
2. **Bakım maliyeti:** Kod değiştiğinde testi güncelleme
3. **Çalışma maliyeti:** CI/CD'de bekleme süresi
4. **Okuma maliyeti:** Başkasının testi anlaması

> **"Bir test, yarattığı DEĞER > getirdiği MALİYET ise kalmalı. Yoksa SİL."**

---

## 2. 🏛️ İyi Testin 4 Sütunu

Khorikov'un en önemli katkısı: İyi bir testi değerlendirmek için **4 kriter**.

### Sütun 1: Regression'a Karşı Koruma 🛡️

> "Bir bug üretildiğinde, test onu YAKALAR MI?"

```javascript
// ✅ İYI: Gerçek iş mantığını test eder → regresyon yakalar
test('indirim kuponu uygulayınca toplam düşmeli', () => {
  const cart = new Cart();
  cart.addItem({ name: 'Laptop', price: 10000 });
  cart.applyCoupon({ code: 'YENI20', discount: 0.20 });

  expect(cart.total).toBe(8000);
  // Biri formülü bozarsa → TEST KIRILIR → regresyon yakalandı! ✅
});

// ❌ KÖTÜ: Trivial testi — regresyon riski sıfır
test('boş cart toplam 0 olmalı', () => {
  const cart = new Cart();
  expect(cart.total).toBe(0);
  // Bu hiç kırılmaz. Kırılırsa zaten çok büyük bir sorun var.
  // DEĞER üretmiyor.
});
```

**Kural:** Teste kattığın kod ne kadar FAZLA ve ne kadar KARMAŞİK ise, regresyon koruma değeri o kadar yüksek.

### Sütun 2: Refactoring'e Dayanıklılık 🔧

> "Kodun DAVRANIŞI değişmeden iç yapısı değiştiğinde, test KIRILMAMALI."

Bu sütun **en çok ihmal edilen** ve **en kritik** olandır!

```javascript
// ❌ KIRILGAN TEST: İç yapıya bağımlı (implementation detail)
test('kullanıcı oluşturma — veritabanı çağrısını kontrol et', () => {
  const mockDb = jest.fn();
  const service = new UserService(mockDb);

  service.createUser('Ali', 'ali@mail.com');

  // İÇ YAPIYI test ediyor:
  expect(mockDb).toHaveBeenCalledWith(
    'INSERT INTO users (name, email) VALUES ($1, $2)',
    ['Ali', 'ali@mail.com']
  );
  // SQL sorgusunu değiştirsen (ama davranış aynı kalsa) → TEST KIRILIR!
  // Tablo adını rename etsen → TEST KIRILIR!
  // ORM'e geçsen → TEST KIRILIR!
  // Davranış AYNI ama test KIRILDI = FALSE POSITIVE 🚨
});

// ✅ DAYANIKLI TEST: Davranışa bağımlı (observable behavior)
test('kullanıcı oluşturma — kullanıcı kaydedilmeli', async () => {
  const service = new UserService(realDb); // Gerçek DB (test DB)

  await service.createUser('Ali', 'ali@mail.com');

  const user = await realDb.findUserByEmail('ali@mail.com');
  expect(user).not.toBeNull();
  expect(user.name).toBe('Ali');
  // SQL değişse de, ORM'e geçse de, tablo adı değişse de
  // → Kullanıcı KAYDEDILDI MI? Evet! Test GEÇER! ✅
});
```

### False Positive vs False Negative ⚖️

```
False Positive (Yanlış Alarm):
  Kod DOĞRU çalışıyor → test KIRILDI
  → Refactoring'de oluşur
  → Güven kaybı: "Aa yine kırılmış, geç skip'le" 😒
  → EN TEHLİKELİSİ!

False Negative (Kaçırma):
  Kod HATALI → test GEÇTI
  → Bug kaçırdın!
  → Ama en azından test yazmadan da olacaktı

Hedef: AZ false positive + AZ false negative
  → Davranışı test et, implementasyonu DEĞİL!
```

### Sütun 3: Hızlı Geri Bildirim ⚡

> "Test ne kadar hızlı çalışırsa, o kadar sık çalıştırılır."

```
Unit test:     ~1ms      → Her kayıtta çalıştır ✅
Integration:   ~100ms    → Her commit'te çalıştır ✅
E2E:           ~10s      → Her PR'da çalıştır
UI E2E:        ~30s-1dk  → Günde 1-2 kez

10.000 unit test × 1ms = 10 saniye → HER ZAMAN çalıştır ✅
100 integration × 100ms = 10 saniye → HER ZAMAN çalıştır ✅
50 E2E × 30s = 25 dakika → PR'da çalıştır ⚠️
```

### Sütun 4: Bakım Kolaylığı 🧹

> "Testi anlamak ve değiştirmek ne kadar kolay?"

```javascript
// ❌ BAKIMI ZOR: Ne test ediliyor anlamak 3 dakika sürüyor
test('test case 47', () => {
  const x = createObj(1, true, null, 'a', [3, 4], { z: 1 });
  const y = process(x, 2, false);
  setupMock('svc', { ret: [{ a: 1, b: 2 }] });
  const r = doStuff(y, getMock('svc'));
  expect(r.v).toBe(42);
  expect(r.s).toBe('done');
  expect(r.f).toEqual([1, 2, 3]);
  // x ne? y ne? r ne? 42 nereden geldi? 🤷
});

// ✅ BAKIMI KOLAY: Okuyan anında anlar
test('premium kullanıcı 100₺ üzeri alışverişte %15 indirim almalı', () => {
  // Arrange (Hazırla)
  const premiumUser = createPremiumUser();
  const cart = createCartWithTotal(150);

  // Act (Çalıştır)
  const discount = calculateDiscount(premiumUser, cart);

  // Assert (Doğrula)
  expect(discount).toBe(22.5); // 150 × 0.15 = 22.5₺
});
```

### 4 Sütunun Trade-off'u 📊

> **"4 sütunun tamamını maksimize etmek İMKANSIZ!"**

```
                        Regresyon   Refactoring   Hızlı    Bakım
                        Koruma      Dayanıklılık  Geri B.  Kolaylığı
┌──────────────────────┼───────────┼─────────────┼────────┼─────────┐
│ Unit Test            │    ⚠️     │     ✅      │   ✅   │   ✅    │
│ (küçük birim)        │ az kod    │  impl gizli │ hızlı  │ basit   │
├──────────────────────┼───────────┼─────────────┼────────┼─────────┤
│ Integration Test     │    ✅     │     ✅      │   ⚠️   │   ⚠️    │
│ (bileşenler birlikte)│ çok kod   │  davranış   │ yavaş  │ setup   │
├──────────────────────┼───────────┼─────────────┼────────┼─────────┤
│ E2E Test             │    ✅✅   │     ✅      │   ❌   │   ❌    │
│ (tüm sistem)         │ en çok    │  davranış   │ çok    │ karmaşık│
│                      │ kod       │             │ yavaş  │         │
└──────────────────────┴───────────┴─────────────┴────────┴─────────┘

→ TEK bir test türü yeterli DEĞİL
→ Doğru KARIŞIMı bul (Test Piramidi)
```

---

## 3. 🔺 Test Piramidi ve Oranlar

### Klasik Test Piramidi

```
         ╱╲
        ╱  ╲         E2E Tests
       ╱ E2E╲        → Az sayıda (5-10%)
      ╱──────╲       → Yavaş, pahalı, kırılgan
     ╱        ╲      → Kritik iş akışları
    ╱Integration╲    
   ╱────────────╲    Integration Tests
  ╱              ╲   → Orta sayıda (20-30%)
 ╱   Unit Tests   ╲  → Dış sistemlerle etkileşim
╱──────────────────╲ 
                      Unit Tests
                      → Çok sayıda (60-70%)
                      → Hızlı, ucuz, odaklı
                      → İş mantığı (domain logic)
```

### Khorikov'un Piramidi: Biraz Farklı!

Khorikov, "her şeyi unit test et" demez. **Değerli olan yeri test et:**

```
Piramid yerine daha doğru model:

  Domain Logic (iş mantığı) → UNIT TEST (çok)
  Controller/Orchestration  → INTEGRATION TEST (orta)
  Altyapı (DB, API, file)   → INTEGRATION TEST (az)
  Trivial kod (getter/setter) → TEST YAZMA! ❌

"Karmaşık iş mantığı" = Unit test cennetidir
"Koordinasyon kodu" = Integration test alanıdır
"Trivial kod" = Test yazmaya DEĞMEZ
```

---

## 4. 📦 Kod Kategorileri ve Test Stratejisi

### Khorikov'un 2×2 Matrisi — KİTABIN KALBİ! ⭐

Her kod parçasını iki eksende değerlendir:

```
                    Karmaşıklık / Domain Önemi
                    DÜŞÜK          │         YÜKSEK
              ┌────────────────────┼────────────────────┐
              │                    │                    │
   ÇOK        │  Overcomplicated   │    Domain Model    │
   Bağımlılık  │  Controller        │    & Algorithms    │
   (dış sistem)│                    │                    │
              │  🔴 REFACTOR ET!   │  🔴 OLAMAZ!        │
              │  Bu kod problematic │  Karmaşık + çok    │
              │                    │  bağımlılık = kaos  │
              ├────────────────────┼────────────────────┤
              │                    │                    │
   AZ         │  Trivial Code      │  Domain Model      │
   Bağımlılık  │                    │  & Algorithms      │
              │                    │                    │
              │  ⬜ TEST YAZMA     │  ✅ UNIT TEST!     │
              │  Getter, setter,   │  İş mantığı,       │
              │  constructor       │  hesaplamalar       │
              └────────────────────┴────────────────────┘
```

#### Sol Alt: Trivial Code → TEST YAZMA ❌

```javascript
// Getter, setter, basit constructor → Test yazmaya DEĞMEZ
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  get displayName() {
    return this.name;
  }
}

// ❌ Bu testi yazma!
test('user name should be set', () => {
  const user = new User('Ali', 'ali@mail.com');
  expect(user.name).toBe('Ali');  // DUH! Constructor'da set ettik zaten 🤦
});
```

#### Sağ Alt: Domain Model → UNIT TEST ✅✅✅

```javascript
// Karmaşık iş mantığı, az bağımlılık → UNIT TEST CENNETİ!
class PricingEngine {
  calculateDiscount(user, cart) {
    let discount = 0;

    // Üyelik indirimi
    if (user.membership === 'premium') {
      discount += 0.10;
    } else if (user.membership === 'gold') {
      discount += 0.15;
    }

    // Miktar indirimi
    if (cart.totalItems > 10) {
      discount += 0.05;
    }

    // Kampanya indirimi
    if (cart.hasCoupon) {
      discount += cart.coupon.discountRate;
    }

    // Maksimum indirim sınırı
    return Math.min(discount, 0.30); // Max %30
  }
}

// ✅ BU testi yaz! Çok değerli:
test('gold üyelik + 10+ ürün + kupon = max %30 indirim', () => {
  const user = { membership: 'gold' };
  const cart = {
    totalItems: 15,
    hasCoupon: true,
    coupon: { discountRate: 0.15 }
  };

  const engine = new PricingEngine();
  const discount = engine.calculateDiscount(user, cart);

  expect(discount).toBe(0.30); // 0.15 + 0.05 + 0.15 = 0.35 → cap 0.30
});

test('premium üyelik, kuponsuz, az ürün = %10 indirim', () => {
  const user = { membership: 'premium' };
  const cart = { totalItems: 3, hasCoupon: false };

  const engine = new PricingEngine();
  const discount = engine.calculateDiscount(user, cart);

  expect(discount).toBe(0.10);
});
```

#### Sol Üst: Overcomplicated Controller → REFACTOR ET! 🔴

```javascript
// ❌ SORUNLU: Hem karmaşık mantık HEM de dış bağımlılık → TEST EDILEMEZ!
class OrderController {
  async createOrder(req, res) {
    // Dış bağımlılık: DB
    const user = await db.users.findById(req.userId);

    // İş mantığı (controller'da OLMAMALI!)
    let total = 0;
    for (const item of req.items) {
      const product = await db.products.findById(item.productId);
      if (product.stock < item.quantity) {
        return res.status(400).json({ error: 'Stok yetersiz' });
      }
      total += product.price * item.quantity;
    }
    if (user.membership === 'premium') total *= 0.9;

    // Dış bağımlılık: Ödeme servisi
    const payment = await paymentService.charge(user, total);

    // Dış bağımlılık: DB
    const order = await db.orders.insert({ userId: user.id, total, items: req.items });

    // Dış bağımlılık: Email servisi
    await emailService.sendConfirmation(user.email, order);

    res.json(order);
  }
}
// Bu kodu test etmek için: DB mock, payment mock, email mock...
// Her şeyi mock'layınca test ANLAMSIZ olur!
```

```javascript
// ✅ REFACTORED: İş mantığını AYİR, controller'ı SİMPLİFY et

// Domain Model (pure function — dış bağımlılık YOK)
class OrderCalculator {
  calculate(items, products, membership) {
    // Stok kontrolü
    for (const item of items) {
      const product = products.find(p => p.id === item.productId);
      if (!product || product.stock < item.quantity) {
        return { success: false, error: `Stok yetersiz: ${item.productId}` };
      }
    }

    // Toplam hesaplama
    let total = items.reduce((sum, item) => {
      const product = products.find(p => p.id === item.productId);
      return sum + product.price * item.quantity;
    }, 0);

    // Üyelik indirimi
    if (membership === 'premium') total *= 0.9;

    return { success: true, total };
  }
}

// Controller (thin — sadece orkestrasyon, iş mantığı YOK)
class OrderController {
  async createOrder(req, res) {
    const user = await db.users.findById(req.userId);
    const products = await db.products.findByIds(req.items.map(i => i.productId));

    // İş mantığını DELEGE ET
    const calculator = new OrderCalculator();
    const result = calculator.calculate(req.items, products, user.membership);

    if (!result.success) {
      return res.status(400).json({ error: result.error });
    }

    const payment = await paymentService.charge(user, result.total);
    const order = await db.orders.insert({ userId: user.id, total: result.total });
    await emailService.sendConfirmation(user.email, order);

    res.json(order);
  }
}

// Şimdi OrderCalculator'ı UNIT TEST ile test edebilirsin!
// Mock YOK, DB YOK, hızlı, güvenilir! ✅✅✅
test('premium üye %10 indirim almalı', () => {
  const calc = new OrderCalculator();
  const items = [{ productId: 'p1', quantity: 2 }];
  const products = [{ id: 'p1', price: 100, stock: 10 }];

  const result = calc.calculate(items, products, 'premium');

  expect(result.success).toBe(true);
  expect(result.total).toBe(180); // 200 * 0.9
});

// Controller'ı ise INTEGRATION TEST ile test et (gerçek DB ile)
```

#### Sağ Üst: Domain + Çok Bağımlılık → OLAMAZ! 🔴🔴

Eğer domain mantığın çok bağımlılık gerektiriyorsa, mimari bir sorun var:

```
ÇÖZÜM: Humble Object Pattern
  → Dış bağımlılıkları "alçakgönüllü" (humble) bir objeye taşı
  → İş mantığını PURE bir objeye taşı
  → İkisini birbirinden ayır

Controller (Humble Object):
  → DB'den oku, servisleri çağır
  → İş kararları ALMAZ
  → Test: Integration test

Domain Model (Pure):
  → Hesapla, karar ver, doğrula
  → Dış dünyayı BİLMEZ
  → Test: Unit test
```

---

## 5. 🎭 Mock'lar, Stub'lar ve Test Doubles

### Terminoloji

```
Test Double: Gerçek bağımlılık yerine kullanılan HER ŞEY

5 Tür Test Double:

1. DUMMY: Sadece parametre doldurmak için, hiç kullanılmaz
   → new Service(dummyLogger)  // Logger hiç çağrılmayacak

2. STUB: Sabit cevap döner, doğrulanmaz
   → stub.getUser = () => ({ name: 'Ali' })  // Her zaman Ali döner

3. SPY: Gerçek metodu çağırır ama çağrıları KAYIT eder
   → realService.send(data)  // Gerçekten gönderir + kaydeder

4. MOCK: Beklenen çağrıları tanımlar ve DOĞRULAR
   → expect(mock.save).toHaveBeenCalledWith('Ali')

5. FAKE: Basitleştirilmiş çalışan implementasyon
   → FakeDatabase: Bellekte Map ile çalışan sahte DB
```

### Khorikov'un Basitleştirmesi

```
Khorikov sadece 2 kategori kullanır:

MOCK (komut) → Dış dünyaya ETKİ yapan çağrılar
  → Email gönder, DB'ye yaz, API çağır
  → "Bu metod ÇAĞRİLDI MI?" diye doğrularsın
  → Interaction verification

STUB (sorgu) → Dış dünyadan VERİ alan çağrılar
  → DB'den oku, config'den al, API'den getir
  → "Bu cevabı DÖNDER" diye ayarlarsın
  → State verification
  → ASLA doğrulama (assert) YAPMA!
```

```javascript
// STUB: Veri döner, doğrulanmaz
const userRepository = {
  findById: jest.fn().mockReturnValue({ id: 1, name: 'Ali', balance: 1000 })
  //        ↑ STUB: Sabit veri döner
};

// MOCK: Çağrı doğrulanır
const emailService = {
  sendEmail: jest.fn()
  //         ↑ MOCK: Çağrıldı mı diye kontrol edeceğiz
};

test('para transferi başarılı olduğunda email gönderilmeli', async () => {
  const service = new TransferService(userRepository, emailService);

  await service.transfer('user-1', 'user-2', 100);

  // STUB doğrulanmaz: findById çağrıldı mı diye KONTROL ETME!
  // ❌ expect(userRepository.findById).toHaveBeenCalled(); → YAPMA!

  // MOCK doğrulanır: Email gönderildi MI?
  expect(emailService.sendEmail).toHaveBeenCalledWith(
    expect.objectContaining({ subject: 'Transfer Başarılı' })
  ); // ✅ Bu doğru!
});
```

### ⚠️ Stub'ları Assert Etme! (Overspecification)

```javascript
// ❌ OVERSPECIFICATION: Stub'ı assert etme!
test('kullanıcı siparişlerini getir', async () => {
  const orderRepo = {
    findByUserId: jest.fn().mockReturnValue([{ id: 1, total: 100 }])
  };

  const orders = await orderService.getUserOrders('user-1');

  // ❌ YANLIŞ: "findByUserId çağrıldı mı?" diye sorma!
  expect(orderRepo.findByUserId).toHaveBeenCalledWith('user-1');
  // Bu bir STUBtur, çağrılıp çağrılmadığı senin TESTİNİ ilgilendirmez!
  // IMPLEMENTATION DETAIL! Yarın cache'e geçsen → test KIRILIR!

  // ✅ DOĞRU: SONUCU kontrol et
  expect(orders).toHaveLength(1);
  expect(orders[0].total).toBe(100);
});
```

---

## 6. 🎯 Mock'u Ne Zaman Kullan, Ne Zaman Kullanma

### Khorikov'un Altın Kuralı ⭐

> **"Mock sadece İŞLEM SINIRLARINDA (process boundaries) kullan.
> Sistem İÇİNDEKİ bağımlılıkları ASLA mock'lama!"**

```
Uygulaman:
┌─────────────────────────────────────────────┐
│                                             │
│  Controller → Service → Domain → Repository │
│                                             │
│  Bu sınıfları birbirine mock'lama! ❌       │
│  Bunlar SİSTEMİN İÇİ!                      │
│                                             │
└──────────────────┬──────────────────────────┘
                   │ İŞLEM SINIRI (process boundary)
                   ↓
┌──────────────────────────────────────────────┐
│  DIŞ SİSTEMLER:                              │
│  → Veritabanı    → Email servisi             │
│  → 3rd party API → Mesaj kuyruğu             │
│  SADECE BUNLARI mock'la (gerektiğinde) ✅    │
└──────────────────────────────────────────────┘
```

### İç Bağımlılık vs Dış Bağımlılık

```
İÇ BAĞIMLILIK (Managed dependency):
  → Sadece SENİN uygulaman erişir
  → Veritabanı (sadece senin uygulamanın DB'si)
  → Dosya sistemi (uygulama klasörü)
  → Mock'laMa! Gerçeğini kullan (test DB)!

DIŞ BAĞIMLILIK (Unmanaged dependency):
  → Dış dünya ile ETKİLEŞİM
  → Email servisi (dışarıya email gider)
  → 3rd party API (başka şirketin servisi)
  → Mesaj kuyruğu (başka servisler okur)
  → Mock'la! ✅ (Gerçeğini test'te kullanmak tehlikeli/pahalı)

Neden bu ayrım ÖNEMLİ?
  → Managed (iç) bağımlılığı mock'larsan → refactoring'i KIRIYORSUN!
     (DB sorgusunu değiştirdin ama davranış AYNI → test KIRILMAMALI!)
  → Unmanaged (dış) bağımlılığı mock'lamazsan → testler YAVAŞ/GERÇEK email gİDER!
```

```javascript
// İÇ bağımlılık: Veritabanı → MOCK'LAMA, gerçek test DB kullan!
test('kullanıcı oluşturulmalı', async () => {
  // ✅ Gerçek test DB (in-memory SQLite veya test container)
  const userService = new UserService(testDb);

  await userService.createUser('Ali', 'ali@mail.com');

  // Gerçek DB'den doğrula
  const user = await testDb.users.findByEmail('ali@mail.com');
  expect(user.name).toBe('Ali');
});

// DIŞ bağımlılık: Email servisi → MOCK'LA!
test('sipariş tamamlandığında email gönderilmeli', async () => {
  const emailMock = { send: jest.fn() }; // ✅ Mock
  const orderService = new OrderService(testDb, emailMock);

  await orderService.completeOrder('order-123');

  expect(emailMock.send).toHaveBeenCalledWith(
    expect.objectContaining({
      to: 'ali@mail.com',
      subject: 'Siparişiniz Tamamlandı'
    })
  );
});
```

### Neden DB'yi Mock'lamamalı?

```
DB mock'larsan:
  → "INSERT çağrıldı mı?" diye doğrularsın → İmplementation detail!
  → Yarın SQL'den ORM'e geçsen → TÜM testler kırılır
  → Gerçek DB davranışı test edilmez (constraint, index, transaction)
  → Sahte bir güvenlik hissi: "Test geçti AMA DB'de çalışmıyor" 😱

DB'yi gerçek kullanırsan:
  → Gerçek INSERT, gerçek SELECT
  → Constraint'ler test edilir
  → Transaction davranışı test edilir
  → Biraz yavaş AMA gerçek
  → Docker + test container = hızlı ve izole ✅
```

---

## 7. 📝 Üç Test Stili

### Stil 1: Output-Based Testing (Çıktı Bazlı) — EN İYİ! ⭐

```javascript
// PURE FUNCTION: Girdi → Çıktı, yan etkisi YOK
function calculateShippingCost(weight, distance, isExpress) {
  const baseCost = weight * 0.5;
  const distanceCost = distance * 0.1;
  const expressFee = isExpress ? 20 : 0;
  return baseCost + distanceCost + expressFee;
}

// TEST: Sadece ÇIKTIYI kontrol et
test('express kargo 20₺ ek ücret', () => {
  const cost = calculateShippingCost(10, 100, true);
  expect(cost).toBe(10 * 0.5 + 100 * 0.1 + 20); // 35₺
});

test('normal kargo ek ücret yok', () => {
  const cost = calculateShippingCost(10, 100, false);
  expect(cost).toBe(10 * 0.5 + 100 * 0.1); // 15₺
});

// NEDEN EN İYİ?
// ✅ Mock yok → Bakımı kolay
// ✅ Refactoring'e dayanıklı → İç yapı gizli
// ✅ Hızlı → Dış bağımlılık yok
// ✅ Okunabilir → Girdi/çıktı açık
```

### Stil 2: State-Based Testing (Durum Bazlı) — İYİ

```javascript
// Nesnenin DURUMUNU kontrol et (yan etkisi var ama gözlemlenebilir)
test('sepete ürün eklenince toplam güncellenmeli', () => {
  const cart = new ShoppingCart();

  cart.addItem({ name: 'Laptop', price: 10000, quantity: 1 });
  cart.addItem({ name: 'Mouse', price: 200, quantity: 2 });

  // DURUMU kontrol et
  expect(cart.itemCount).toBe(2);
  expect(cart.total).toBe(10400); // 10000 + 200*2
});

// İYİ ama:
// ⚠️ Bazen setup fazla olabiliyor
// ⚠️ Gözlemlenebilir durum çok büyükse assertion'lar uzuyor
```

### Stil 3: Communication-Based Testing (İletişim Bazlı) — DİKKATLİ KULLAN

```javascript
// Dış sisteme yapılan ÇAĞRIYI kontrol et (mock kullanır)
test('sipariş iptalinde ödeme iade edilmeli', async () => {
  const paymentGateway = { refund: jest.fn().mockResolvedValue(true) };
  const orderService = new OrderService(testDb, paymentGateway);

  await orderService.cancelOrder('order-123');

  // İLETİŞİMİ kontrol et: refund çağrıldı mı, doğru parametrelerle mi?
  expect(paymentGateway.refund).toHaveBeenCalledWith({
    orderId: 'order-123',
    amount: 500,
    reason: 'customer_cancellation'
  });
});

// DİKKAT:
// ⚠️ Sadece dış bağımlılıklar için kullan
// ⚠️ İç bağımlılıkları bu stille test ETME
// ⚠️ Aşırı kullanım → kırılgan testler
```

### Stil Tercih Sırası

```
1. Output-Based  ✅✅✅  (mümkünse HER ZAMAN bunu tercih et)
2. State-Based   ✅✅    (output mümkün değilse)
3. Communication ⚠️     (sadece dış bağımlılıklar için)

Daha fazla output-based test yazmak için:
→ Functional architecture kullan
→ İş mantığını PURE fonksiyonlara taşı
→ Yan etkileri (DB, API) kenara it (controller'a)
```

---

## 8. 🔄 Refactoring ve Testler

### Observable Behavior vs Implementation Detail

Bu ayrım, **tüm kitabın temel eksenidir:**

```
Observable Behavior (Gözlemlenebilir Davranış):
  → Client'ın (çağıran kodun) GÖREBİLDİĞİ sonuçlar
  → Dönüş değeri
  → Durum değişikliği (dışarıdan erişilebilir)
  → Dış sistemlere yapılan çağrılar (email, API)

  → BUNU test et! ✅

Implementation Detail (Uygulama Detayı):
  → İşin NASIL yapıldığı
  → Hangi fonksiyon çağrıldı
  → Hangi SQL sorgusu kullanıldı
  → Ara değişkenler, private metodlar

  → BUNU test ETME! ❌
```

```javascript
// ❌ Implementation detail test ediyor
test('kullanıcı oluştur', () => {
  const service = new UserService();
  const spy = jest.spyOn(service, '_hashPassword');  // Private metod!

  service.createUser('Ali', '123456');

  expect(spy).toHaveBeenCalledWith('123456');  // NASIL yaptığını test ediyor
  expect(spy).toHaveReturnedWith(expect.any(String));
  // Yarın hash algoritmasını değiştirsen → test KIRILIR
  // Ama davranış AYNI: şifre güvenli şekilde kaydedildi!
});

// ✅ Observable behavior test ediyor
test('kullanıcı şifresi düz metin olarak saklanmamalı', async () => {
  const service = new UserService(testDb);

  await service.createUser('Ali', '123456');

  const user = await testDb.users.findByName('Ali');
  expect(user.password).not.toBe('123456');    // Düz metin değil ✅
  expect(user.password.length).toBeGreaterThan(20); // Hash uzunluğu ✅
  // NASIL hash'lediği önemli değil, SONUCu test edildi!
});
```

### Kırılgan Testlerden Kaçınma Rehberi

```
Test kırılmasının 2 nedeni:

1. DOĞRU KIRILMA (gerçek bug) ✅
   → Davranış değişti, test bunu yakaladı
   → İstediğimiz şey!

2. YANLIŞ KIRILMA (false positive) ❌
   → Refactoring yaptın, davranış AYNI, ama test kırıldı
   → Implementation detail'e bağımlı test

YANLIŞ KIRILMAYI AZALTMAK İÇİN:

  □ Private metotları test ETME
  □ Stub'ları assert ETME
  □ İç fonksiyon çağrılarını doğrulama
  □ Belirli SQL/sorgu stringlerini bekleme
  □ Metot çağırma sırasını doğrulama (gerekli değilse)

YERINE:

  ✅ Sadece public API'ı (interface) test et
  ✅ Dönüş değerini veya son durumu assert et
  ✅ Dış etkiyi assert et (email gitti mi?)
  ✅ Davranışı tanımlayan testler yaz
```

---

## 9. 🔗 Integration Test Stratejisi

### Integration Test Ne Zaman?

```
Unit test: İş mantığı, domain logic, hesaplamalar
Integration test: Dış dünya ile etkileşim

Controller/Orchestration kodunu integration test ile test et:
  → Gerçek veritabanı bağlantısı
  → Gerçek HTTP çağrıları (test server)
  → Mock'lanmış dış servisler (email, 3rd party API)
```

### En İyi Pratikler

```javascript
// INTEGRATION TEST: Gerçek DB + Mock dış servis
describe('OrderController Integration', () => {
  let testDb;
  let emailMock;
  let app;

  beforeAll(async () => {
    testDb = await createTestDatabase(); // Docker container veya in-memory
    emailMock = { send: jest.fn() };
    app = createApp({ db: testDb, emailService: emailMock });
  });

  beforeEach(async () => {
    await testDb.clean(); // Her testten önce DB'yi temizle
    emailMock.send.mockClear();
  });

  afterAll(async () => {
    await testDb.destroy();
  });

  test('başarılı sipariş oluşturma', async () => {
    // Arrange: Test verisini gerçek DB'ye yaz
    const user = await testDb.users.insert({ name: 'Ali', email: 'ali@test.com', membership: 'premium' });
    const product = await testDb.products.insert({ name: 'Laptop', price: 10000, stock: 5 });

    // Act: Gerçek HTTP isteği
    const response = await request(app)
      .post('/orders')
      .send({ userId: user.id, items: [{ productId: product.id, quantity: 1 }] })
      .expect(201);

    // Assert: Sonucu kontrol et
    expect(response.body.total).toBe(9000); // Premium %10 indirim

    // Assert: DB'deki durumu kontrol et
    const order = await testDb.orders.findById(response.body.id);
    expect(order).not.toBeNull();
    expect(order.total).toBe(9000);

    // Assert: Stok azaldı mı?
    const updatedProduct = await testDb.products.findById(product.id);
    expect(updatedProduct.stock).toBe(4);

    // Assert: Email gönderildi mi? (mock)
    expect(emailMock.send).toHaveBeenCalledWith(
      expect.objectContaining({ to: 'ali@test.com' })
    );
  });

  test('stok yetersizse 400 dönmeli', async () => {
    const user = await testDb.users.insert({ name: 'Ayşe' });
    const product = await testDb.products.insert({ name: 'Phone', price: 5000, stock: 0 });

    const response = await request(app)
      .post('/orders')
      .send({ userId: user.id, items: [{ productId: product.id, quantity: 1 }] })
      .expect(400);

    expect(response.body.error).toContain('Stok yetersiz');

    // Email gönderilMEMELİ
    expect(emailMock.send).not.toHaveBeenCalled();
  });
});
```

### Integration Test Miktarı

```
Unit test:         İş mantığının her edge case'i
Integration test:  Her "mutlu yol" (happy path) + kritik hata senaryoları

Bir controller için tipik integration test sayısı:
  → 1 happy path (başarılı akış)
  → 2-3 hata senaryosu (validasyon hatası, yetki hatası, not found)
  → Toplam 3-5 test

DAHA FAZLASI gereksiz: Integration test yavaş ve pahalı!
Edge case'leri unit test'te test et.
```

---

## 10. 🚫 Anti-Pattern'lar

### Anti-Pattern 1: Private Metot Testi ❌

```javascript
// ❌ Private metodu test etme
class UserService {
  #validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  createUser(name, email) {
    if (!this.#validateEmail(email)) {
      throw new ValidationError('Geçersiz email');
    }
    // ...
  }
}

// ❌ YANLIŞ: Private metodu doğrudan test etme
test('validateEmail geçerli email doğrulamalı', () => {
  const service = new UserService();
  expect(service._validateEmail('ali@mail.com')).toBe(true);  // ERIŞEMEZSIN!
});

// ✅ DOĞRU: Public metod üzerinden test et
test('geçersiz email ile kullanıcı oluşturulamaz', () => {
  const service = new UserService();
  expect(() => service.createUser('Ali', 'gecersiz')).toThrow('Geçersiz email');
});

test('geçerli email ile kullanıcı oluşturulabilir', () => {
  const service = new UserService();
  expect(() => service.createUser('Ali', 'ali@mail.com')).not.toThrow();
});

// Private metod public interface üzerinden test edildi! ✅
// Yarın regex değişse → createUser hâlâ aynı davranıyorsa → test GEÇER!
```

### Anti-Pattern 2: Aşırı Mock Kullanımı ❌

```javascript
// ❌ LONDON SCHOOL AŞIRILIĞI: Her şeyi mock'la
test('sipariş oluştur', async () => {
  const userRepo = { findById: jest.fn().mockResolvedValue({ id: 1, name: 'Ali' }) };
  const productRepo = { findById: jest.fn().mockResolvedValue({ id: 1, price: 100 }) };
  const orderRepo = { save: jest.fn() };
  const paymentService = { charge: jest.fn().mockResolvedValue(true) };
  const emailService = { send: jest.fn() };
  const logger = { info: jest.fn() };
  const cache = { set: jest.fn() };

  const service = new OrderService(userRepo, productRepo, orderRepo, paymentService, emailService, logger, cache);
  await service.createOrder(1, [{ productId: 1, quantity: 1 }]);

  expect(userRepo.findById).toHaveBeenCalledWith(1);
  expect(productRepo.findById).toHaveBeenCalledWith(1);
  expect(orderRepo.save).toHaveBeenCalled();
  expect(paymentService.charge).toHaveBeenCalled();
  expect(emailService.send).toHaveBeenCalled();
  expect(logger.info).toHaveBeenCalled();
  expect(cache.set).toHaveBeenCalled();

  // 7 mock, 7 assertion → Implementation detail'in birebir kopyası!
  // BU TEST KODU AYNASIDIR, kodu KORUMUYOR!
  // Herhangi bir iç değişiklikte → TEST KIRILIR!
});
```

### Anti-Pattern 3: Test İçinde Kontrol Akışı ❌

```javascript
// ❌ Test içinde if, for, try-catch kullanma
test('tüm kullanıcılar aktif olmalı', () => {
  const users = getUsersFromDB();

  for (const user of users) {
    if (user.role !== 'admin') {
      expect(user.isActive).toBe(true);
    }
  }
  // Kaç kullanıcı test edildi? Belki 0! (tümü admin ise → test boş geçer)
});

// ✅ Testlerini belirleyici (deterministic) yap
test('normal kullanıcılar aktif olmalı', () => {
  const users = [
    { name: 'Ali', role: 'user', isActive: true },
    { name: 'Ayşe', role: 'user', isActive: true },
  ];

  const normalUsers = users.filter(u => u.role !== 'admin');
  expect(normalUsers.length).toBeGreaterThan(0); // Boş olmadığından emin ol!
  normalUsers.forEach(u => expect(u.isActive).toBe(true));
});
```

### Anti-Pattern 4: God Test ❌

```javascript
// ❌ Tek testte çok şey test etme (God Test)
test('kullanıcı sistemi çalışmalı', async () => {
  // 50 satır setup
  // kullanıcı oluştur
  // email doğrula
  // giriş yap
  // profil güncelle
  // şifre değiştir
  // sipariş ver
  // sipariş iptal et
  // hesabı sil
  // 30 assertion

  // Bu test kırıldığında: NERESİ KIRILDI? Hangisi hatalı? 🤷
});

// ✅ Her test TEK bir davranışı test etmeli
test('yeni kullanıcı email doğrulaması gerektirir', () => { ... });
test('doğrulanmış kullanıcı giriş yapabilir', () => { ... });
test('kullanıcı şifresini değiştirebilir', () => { ... });
```

---

## 11. 📋 Test Best Practices

### AAA Pattern (Arrange-Act-Assert) 📐

```javascript
test('premium kullanıcı kargo ücreti ödemez', () => {
  // ARRANGE: Test verilerini hazırla
  const user = createUser({ membership: 'premium' });
  const cart = createCart({ total: 500, weight: 5 });

  // ACT: Test edilen davranışı çalıştır (TEK satır!)
  const shippingCost = calculateShipping(user, cart);

  // ASSERT: Sonucu doğrula
  expect(shippingCost).toBe(0);
});

// Kurallar:
// → Arrange: Uzun olabilir (helper fonksiyonlar kullan)
// → Act: TEK SATIR olmalı! Birden fazlaysa testi böl.
// → Assert: 1-3 assertion ideal. Hepsi AYNI davranışla ilgili olmalı.
// → Hiç yorum yazma — test adı yeterince açıklayıcı olmalı.
```

### Test İsimlendirme 📛

```javascript
// ❌ KÖTÜ: Ne test edildiği belli değil
test('test_1', () => { ... });
test('calculateDiscount works', () => { ... });
test('should return correct value', () => { ... });

// ✅ İYİ: Davranışı tam olarak açıklar
test('expired coupon should not apply discount', () => { ... });
test('premium user gets free shipping on orders above 200₺', () => { ... });
test('out of stock product cannot be added to cart', () => { ... });

// FORMAT: [durum] + [eylem] + [beklenen sonuç]
// "expired coupon" + "apply discount" + "should not"
```

### Test Verileri ve Object Mother / Builder 🏗️

```javascript
// ❌ Her testte veri tekrarı
test('test 1', () => {
  const user = { id: 1, name: 'Ali', email: 'ali@mail.com', membership: 'premium',
    createdAt: new Date(), isActive: true, balance: 1000 };
  // ...
});

test('test 2', () => {
  const user = { id: 2, name: 'Ayşe', email: 'ayse@mail.com', membership: 'standard',
    createdAt: new Date(), isActive: true, balance: 500 };
  // ...
});

// ✅ Test Data Builder: Sadece ÖNEMLİ alanları belirt
function createUser(overrides = {}) {
  return {
    id: overrides.id ?? 1,
    name: overrides.name ?? 'Test User',
    email: overrides.email ?? 'test@mail.com',
    membership: overrides.membership ?? 'standard',
    createdAt: overrides.createdAt ?? new Date(),
    isActive: overrides.isActive ?? true,
    balance: overrides.balance ?? 0,
    ...overrides,
  };
}

test('premium kullanıcı %10 indirim alır', () => {
  const user = createUser({ membership: 'premium' });
  // Sadece ÖNEMLİ alan belirtildi, geri kalanı default ✅
  // Test okuyucu: "Aa, membership önemli burada, geri kalanı önemsiz"
});

test('bakiyesi yetersiz kullanıcı sipariş veremez', () => {
  const user = createUser({ balance: 10 });
  const cart = createCart({ total: 500 });
  // Okuyucu anında anlar: "bakiye < total → hata"
});
```

### Test Bağımsızlığı 🔒

```javascript
// ❌ Testler birbirine bağımlı
let userId;

test('kullanıcı oluştur', async () => {
  const user = await createUser('Ali');
  userId = user.id;  // Sonraki test buna bağımlı!
});

test('kullanıcıyı güncelle', async () => {
  await updateUser(userId, { name: 'Ali Can' });  // userId önceki testten!
  // İlk test fail olursa? → Bu test de fail! 💥
  // Testleri farklı sırada çalıştırırsan? → BOZULUR! 💥
});

// ✅ Testler bağımsız, kendi verilerini oluşturur
test('kullanıcıyı güncelle', async () => {
  // Arrange: KENDİ verisini oluştur
  const user = await createUser('Ali');

  // Act
  await updateUser(user.id, { name: 'Ali Can' });

  // Assert
  const updated = await findUser(user.id);
  expect(updated.name).toBe('Ali Can');
});
```

---

## 12. 📊 Code Coverage Metrikleri — Sayılar Yalan Söyler

### Coverage Yüksek = Kaliteli Test? ❌

Khorikov bu konuda çok net: **code coverage iyi test yazıldığının KANITI değildir.** Kötü test yazıldığının mazereti olarak kullanılır.

```javascript
// %100 coverage ama SIFIR değer:
function sum(a, b) {
  return a + b;
}

test('sum works', () => {
  sum(1, 2); // assert YOK! Sonucu kontrol etmiyor.
  // Coverage tool: "Bu satır çalıştı" → %100 ✅
  // Gerçek: HİÇBİR ŞEY doğrulanmadı → %0 güven
});
```

### Coverage Metrikleri Tablosu

| Metrik | Ne Ölçer | Yalan Söyler mi? |
|--------|----------|-------------------|
| **Line Coverage** | Çalıştırılan satır yüzdesi | ✅ Evet — assert olmadan bile artar |
| **Branch Coverage** | if/else dallarını gezme | ✅ Evet — aynı sorun |
| **Mutation Testing** | Kodu değiştir, test kırılır mı? | ❌ En dürüst metrik ama YAVAŞ |

### Mutation Testing — Gerçek Kalite Ölçüsü

```
Mutation testing şöyle çalışır:

  1. Kodunda "return a + b" var
  2. Tool bunu "return a - b" yapar (mutant)
  3. Testlerin HÂLÂ geçiyorsa → testlerin ZAYIF (mutant hayatta kaldı!)
  4. Testlerin fail oluyorsa → testlerin GÜÇLÜ (mutant öldürüldü! ✅)

Tool: Stryker (JavaScript/TypeScript için)
  → npx stryker run
  → Mutation score: %85 → %15 mutant hayatta kaldı = eksik test var
```

### Büyük Şirketlerde Coverage Yaklaşımı

```
Google:
  → %60 "kabul edilebilir", %75 "tavsiye edilen", %90 "örnek"
  → AMA: Coverage hedefi ZORUNLU değil
  → Mutation testing aktif kullanılıyor (internal tool)

Microsoft:
  → Windows ekibi: Coverage metriği yok, "BUG BULMA" metriği var
  → "Test yazdıktan sonra kaç bug production'a ulaştı?" → ASIL metrik

Getir:
  → Sonarqube'da %80 minimum gate var
  → Ama önemli olan: DAVRANIŞI test ediyor musun?
  → Coverage %90 ama hep implementation detail test ediliyorsa → DEĞERSIZ
```

### Doğru Yaklaşım

```
Coverage'ı TABAN olarak kullan, HEDEF olarak değil:

  ❌ "Coverage %90'a çıkarmalıyız" → Getter testleri yazılır
  ✅ "Coverage %60'ın altına DÜŞMEMELI" → Minimum kalite çıtası
  ✅ "Yeni feature'da coverage %80+" → Yeni kod için makul hedef
  ✅ "Mutation score %85+" → Gerçek kalite ölçümü (CI'da yavaş ama değerli)
```

---

## 13. 🏢 Büyük Şirketlerde Test Kültürü

### Google — Testing on the Toilet (TotT)

Google'da tuvalet kabinlerinin iç kapısına test ipuçları asılır. Evet, **gerçekten**. "Testing on the Toilet" programı 2006'dan beri aktif. Her hafta yeni bir test ipucu yayınlanır.

```
Google'ın Test Piramidi (gerçek rakamlar):
  → %80 Unit Test (küçük, hızlı, izole)
  → %15 Integration Test (birkaç modül birlikte)
  → %5 End-to-End Test (tam sistem, yavaş)

Google'ın kuralı: "Flaky test = DISABLED test"
  → Eğer bir test bazen geçiyor, bazen kılıyorsa → KAPAT
  → %1 flaky rate bile binlerce test'te her gün yüzlerce false alarm
```

### Netflix — Chaos Engineering + Test

```
Netflix sadece unit test yazmaz, production'ı TEST EDER:
  → Chaos Monkey: Rastgele sunucu öldürür
  → Testi GERÇEKLİK ile birleştirir

AMA unit test olmadan chaos engineering DE işe yaramaz:
  → "20 sunucu öldü, servis ayakta" → Güzel
  → "Ama order hesaplaması yanlış" → Unit test eksik
```

### Spotify — Microservice Test Stratejisi

```
Spotify'ın yaklaşımı Khorikov'a çok yakın:
  → Consumer-Driven Contract Tests (Pact)
  → Her microservice kendi "sözleşmesini" yayınlar
  → Downstream servis: "Ben senden bu format'ta veri bekliyorum"
  → Upstream servis: "Tamam, bu sözleşmeye uyuyorum"
  → Bu MANAGED/UNMANAGED ayrımının microservice versiyonu
```

---

## 14. 🤖 Yapay Zeka Çağında Unit Testing

### AI Test Yazmada İyi mi?

2024'te GitHub Copilot, ChatGPT ve benzeri araçlar test yazma konusunda **iyi ama tehlikeli** hale geldi. Neden tehlikeli?

```
AI'ın test yazma eğilimi:

  ❌ Implementation detail'e bağlı testler yazar
    → "Bu fonksiyon iç'te map() kullanıyor, onu test edeyim"
    → Khorikov: YANLIŞ! Davranışı test et!

  ❌ Mock'ları gereğinden fazla kullanır
    → Her dependency'yi mock'lar (London School)
    → Khorikov: Sadece dış bağımlılıkları mock'la!

  ❌ Coverage obsesyonu yaratır
    → "Her satırı cover edeyim" → Getter/setter testleri
    → Khorikov: Değersiz testi yazma!

  ✅ AMA: AAA pattern'ını güzel uygular
  ✅ AMA: Edge case'leri hatırlatır
  ✅ AMA: Test isim konvansiyonları güzel
```

### Khorikov Prensiplerine Uygun AI Promptları

```
KÖTÜ PROMPT:
  "Bu fonksiyon için test yaz"
  → AI her implementation detail'i test eder

İYİ PROMPT:
  "Bu fonksiyonun DAVRANIŞ testlerini yaz. 
   Implementation detail'e (hangi metot çağrılıyor, 
   iç değişken ne) bağlı olmasın. 
   Sadece dışarıdan görülebilir sonuçları assert et.
   AAA pattern kullan. 
   Mock sadece dış bağımlılıklar (email, 3rd party API) için olsun.
   Veritabanı gibi iç bağımlılıklar için gerçek test instance kullan."
```

```
DETAYLI PROMPT:
  "Bu servis için test yaz. Vladimir Khorikov'un 
   Unit Testing kitabındaki 4 sütun kriterini uygula:
   1. Regression koruması: Gerçek business logic'i test et
   2. Refactoring dayanıklılığı: Private'ları çağırma
   3. Hızlı feedback: Mock'ları minimumda tut
   4. Bakım kolaylığı: Test başına tek davranış
   
   Coverage için getter/setter testi YAZMA.
   Stub'ları assert ETME.
   Test isimleri 'should_expectedBehavior_when_condition' formatında olsun."
```

### AI ile Test Review

```
AI'a mevcut testlerini REVIEW ettirmek, yenisini yazdırmaktan değerli:

PROMPT:
  "Bu test dosyasını Khorikov'un kriterlerine göre değerlendir:
   - Hangi testler implementation detail'e bağımlı?
   - Hangi stub'lar gereksiz yere assert ediliyor?
   - Hangi mock'lar aslında iç bağımlılık (DB, file) için kullanılmış?
   - 4 sütun analizi yap: her test için (regression, refactoring 
     resistance, speed, maintainability) puanla"
```

### Topluluk Görüşleri

```
Kent Beck (TDD'nin mucidi):
  "AI ile TDD yapmak ilginç: AI'a test yazdırmak yerine,
   SEN testi yaz, AI kodu yazsın. Red-Green-Refactor hâlâ geçerli."

Martin Fowler:
  "Test piramidinin şekli değişebilir ama TEMELİ aynı:
   Hızlı feedback veren, az kırılgan testler her zaman kazanır."

J.B. Rainsberger (@jbrains):
  "Integration test'ler bir TUZAK. 
   Yeterince yazmıyorsun çünkü yavaş.
   Yazınca da çok kırılgan oluyorlar.
   Çözüm: Contract test + unit test."

Reddit r/programming:
  "Khorikov'un kitabı okuduktan sonra test yazma şeklim tamamen değişti.
   Artık mock sayısını değil, test'in REFACTORING'e dayanıp 
   dayanmadığını ölçüyorum." — en çok upvote alan yorum
```

---

## 15. 🎬 Son Sözler

### Bu Kitabın Altın Kuralları 🏆

| # | İlke | Bir Cümlede |
|---|---|---|
| 1 | **Testlerin amacı sürdürülebilir büyüme** | Bug bulma değil, güvenle değiştirme |
| 2 | **4 sütunu dengele** | Regresyon, refactoring dayanıklılığı, hız, bakım |
| 3 | **Implementation değil behavior test et** | Private metot, SQL sorgusu = DOĞRULAMA! |
| 4 | **2×2 matrisi kullan** | Domain → unit test, Controller → integration test |
| 5 | **Mock'u sınırda kullan** | Sadece dış bağımlılıklar için |
| 6 | **Stub'ları assert etme** | Stub = veri sağlar, Mock = doğrulanır |
| 7 | **Output-based tercih et** | Pure function > state > communication |
| 8 | **Kötü test, hiç testten kötü** | Değer < maliyet → SİL |
| 9 | **AAA pattern** | Arrange → Act (tek satır!) → Assert |
| 10 | **Her test bağımsız** | Sıra, diğer testler önemsiz olmalı |

### Khorikov vs Diğer Yaklaşımlar

```
LONDON SCHOOL (Mockist):
  → Her bağımlılığı mock'la
  → Her sınıfı izole test et
  → Khorikov: "Çok kırılgan, implementation detail'e bağlı!"

DETROIT SCHOOL (Classicist):
  → Mock'lardan kaçın
  → Birimleri birlikte test et
  → Khorikov buna DAHA YAKIN ama tam bu da değil

KHORİKOV YAKLAŞIMI:
  → Domain logic → unit test (mock'suz)
  → Controller → integration test (gerçek DB, mock dış servisler)
  → Trivial kod → test yazma
  → Her zaman DAVRANIŞI test et
```

### Test Yazma Kontrol Listesi ✅

```
Yeni test yazmadan önce sor:

  □ Bu test hangi DAVRANIŞI doğruluyor?
  □ Bu davranış değişmeden iç yapı değişirse test KIRILIR MI?
    → Evet ise: Testi değiştir, implementation detail'den kurtul
  □ Bu test gerçekten DEĞER üretiyor mu?
    → Getter/setter testi mi? → YAZMA
  □ Mock kullandıysan: Bu bir diş bağımlılık mı?
    → İç bağımlılık mock'ladıysan → Kaldır, gerçeğini kullan
  □ Stub'ları assert ettin mi?
    → Evet ise → Kaldır, sadece mock'ları assert et
  □ Test adı davranışı açıklıyor mu?
    → 'test1' → 'expired coupon should not apply discount'
```

### Öğrenme Yolculuğu 🛤️

```
📗 Grokking Algorithms            → Algoritma temeli ✅
📕 Clean Code                     → Kod kalitesi ✅
📘 The Pragmatic Programmer       → Mühendislik zihniyeti ✅
📙 The Missing README             → Kariyer temeli ✅
📗 A Philosophy of Software Design → Tasarım felsefesi ✅
📘 Head First Design Patterns     → Pattern'lar ✅
📕 Designing Data-Intensive Apps  → Dağıtık sistem temeli ✅
📙 Unit Testing (Khorikov)        → Test stratejisi ✅  ← BURADASIN

Sıradaki (Faz 2 sonu):
📗 Refactoring (Fowler)           → Referans kitap
```

---

> **"Testler bir güvenlik ağıdır, kalkan değil.
> Her testini yazmadan önce sor:
> 'Bu test kırıldığında, gerçekten bir bug olduğunu MU gösterir,
> yoksa sadece kodu DEĞİŞTİRDİĞİMİ mi?'
> Birincisi değerlidir, ikincisi yüktür.
> İyi test yazmak, hangi testleri YAZMAYACAĞINI bilmekle başlar."** 🧪
>
> — Bu rehberin özü: **"Az ama değerli test > Çok ama değersiz test.
> Davranışı test et, implementasyonu değil."**
