# 🔧 Refactoring — Improving the Design of Existing Code — Türkçe Kapsamlı Rehber

> **"Refactoring, kodun dışarıdan gözlemlenen davranışını DEĞİŞTİRMEDEN
> iç yapısını iyileştirme disiplinidir."**
> — Martin Fowler

Bu kitap, mevcut kodu **güvenle** iyileştirmenin sistematik kataloğudur.
70+ refactoring tekniğini adım adım anlatır. Refactoring'i bir sanat değil,
bir **zanaat** haline getirir: küçük, güvenli, test edilebilir adımlarla.

---

## 📖 İçindekiler

1. [Refactoring Nedir?](#1--refactoring-nedir)
2. [Neden Refactoring?](#2--neden-refactoring)
3. [Ne Zaman Refactoring Yapmalı?](#3--ne-zaman-refactoring-yapmalı)
4. [Code Smells — Kötü Kokular](#4--code-smells--kötü-kokular)
5. [Temel Refactoring Teknikleri](#5--temel-refactoring-teknikleri)
6. [Kapsülleme Refactoring'leri](#6--kapsülleme-refactoringleri)
7. [Feature Taşıma Refactoring'leri](#7--feature-taşıma-refactoringleri)
8. [Veri Organizasyonu](#8--veri-organizasyonu)
9. [Koşullu Mantığı Sadeleştirme](#9--koşullu-mantığı-sadeleştirme)
10. [API Refactoring'leri](#10--api-refactoringleri)
11. [Kalıtım ile İlgili Refactoring'ler](#11--kalıtım-ile-i̇lgili-refactoringler)
12. [Büyük Refactoring'ler](#12--büyük-refactoringler)
13. [Refactoring ve Performans](#13--refactoring-ve-performans)
14. [Refactoring İş Akışı](#14--refactoring-i̇ş-akışı)
15. [Büyük Şirketlerde Refactoring](#15--büyük-şirketlerde-refactoring)
16. [Yapay Zeka Çağında Refactoring](#16--yapay-zeka-çağında-refactoring)
17. [Son Sözler](#17--son-sözler)

---

## 1. 🔄 Refactoring Nedir?

### İki Şapka Metaforu 🎩🎩

Fowler, Kent Beck'ten alıntıladığı iki şapka metaforuyla yazılım geliştirmeyi anlatır:

```
ŞAPKA 1: Feature Ekleme 🎩
  → Yeni davranış ekliyorsun
  → Testler EKLENIR (yeni davranış için)
  → Mevcut testler DEĞİŞMEMELİ

ŞAPKA 2: Refactoring 🎩
  → Davranış DEĞİŞMİYOR
  → Yapı iyileşiyor
  → Mevcut testler GEÇMEYE devam etmeli
  → Yeni test EKLENMEZ (davranış aynı çünkü)

KURAL: Aynı anda TEK şapka tak!
  ❌ "Feature eklerken kodu da düzelteyim" → iki şapka birden → KAOS!
  ✅ Refactor et → commit → feature ekle → commit → refactor et → commit
```

### Refactoring ≠ Yeniden Yazma (Rewrite)

```
REFACTORING:                          REWRITE:
  Küçük adımlar ✅                     Büyük patlama ❌
  Her adımda testler geçer ✅          Testler haftalarca kırık ❌
  Sürekli çalışan sistem ✅            "2 hafta sonra hazır" ❌
  Risk düşük ✅                        Risk yüksek ❌
  Günlük yapılabilir ✅                Proje planı gerekir ❌

Rewrite gerekeceği TEK durum:
  → Kod O KADAR kötü ki, adım adım iyileştiremiyorsun
  → Bu çok NADİR olmalı! Çoğu zaman refactoring YETERLİ.
```

### Refactoring'in Tanımı (Kesin) 📖

```
İsim olarak:
  "Kodun dışarıdan gözlemlenen davranışını değiştirmeden
   iç yapısını iyileştiren bir dönüşüm."

Fiil olarak:
  "Bir dizi refactoring uygulayarak, gözlemlenen davranışı
   değiştirmeden kodu yeniden yapılandırmak."

Kritik kelime: "GÖZLEMLENEN DAVRANIŞ DEĞİŞMEZ"
  → Performans değişebilir (daha hızlı veya yavaş olabilir)
  → İç yapı değişir (başka fonksiyonlar, başka sınıflar)
  → AMA dışarıdan bakan biri aynı sonucu görür
```

---

## 2. 💡 Neden Refactoring?

### 1. Kodu Anlamayı Kolaylaştırır 📖

```javascript
// ÖNCE: "Bu ne yapıyor?" — 3 dakika düşünme
function calc(a, b, t) {
  if (t === 1) return a * b * 0.15;
  if (t === 2) return a * b * 0.12;
  if (t === 3) return a * b * 0.08 + (a > 100 ? 50 : 0);
  return 0;
}

// SONRA: "Anlaşıldı!" — 3 saniye
function calculateInsurancePremium(vehicleValue, driverAge, coverageType) {
  switch (coverageType) {
    case CoverageType.FULL:
      return vehicleValue * driverAge * 0.15;
    case CoverageType.STANDARD:
      return vehicleValue * driverAge * 0.12;
    case CoverageType.BASIC: {
      const basePremium = vehicleValue * driverAge * 0.08;
      const highValueSurcharge = vehicleValue > 100_000 ? 50 : 0;
      return basePremium + highValueSurcharge;
    }
    default:
      return 0;
  }
}
```

### 2. Bug Bulmayı Kolaylaştırır 🐛

```
Karmaşık kod = Bug'lar gizlenir
Temiz kod = Bug'lar görünür olur

"Refactoring yapmasam bu bug'ı ASLA bulamazdım!"
  — Çoğu deneyimli geliştiricinin ortak deneyimi

Kent Beck: "Ben harika bir programcı değilim.
Sadece harika alışkanlıkları olan iyi bir programcıyım."
```

### 3. Geliştirme Hızını Artırır ⚡

```
Paradoks: "Refactoring yapmak zaman kaybı değil mi?"

Kısa vadede:    Feature gecikmesi (saatler)
Uzun vadede:    Feature hızlanması (GÜNLER/HAFTALAR kazanılır!)

Design Stamina Hypothesis (Fowler):

  Kalite
    │
    │        İyi iç tasarım
    │       ╱───────────────   (hız sabit veya artar)
    │     ╱
    │   ╱
    │  ╱╲ Kötü iç tasarım
    │ ╱  ╲
    │╱    ╲──────────────   (hız sürekli düşer)
    └────────────────────→ Zaman

  Kesişme noktası genellikle HAFTALAR içinde!
  Yani birkaç hafta sonra bile refactoring kendini ÖDER.
```

### 4. Tasarımı İyileştirir 🏗️

```
Refactoring olmadan:
  Kod çürür → "Patch üzerine patch" → Spaghetti
  Her yeni özellik ESKİSİNDEN DAHA ZOR eklenir

Refactoring ile:
  Kod evrilir → "Sürekli iyileşme" → Temiz mimari
  Her yeni özellik ÖNCEKİ KADAR KOLAY eklenir
```

---

## 3. ⏰ Ne Zaman Refactoring Yapmalı?

### Üçün Kuralı (Rule of Three) 3️⃣

> **"Bir şeyi üçüncü kez yaptığında, refactor et."**

```
1. kez: Sadece yap.
2. kez: "Hmm, benzerini görmüştüm ama neyse, yap."
3. kez: "Tamam, bu PATTERN oluştu. REFACTOR ET!" 🔧
```

### Hazırlık Refactoring'i (Preparatory) 🏗️

> **"Feature eklemeden ÖNCE kodu hazırla."**

```javascript
// Feature: "İndirim kuponu desteği ekle"
// Ama mevcut kod buna hazır DEĞİL...

// ADIM 1: Önce refactor (şapka 1: refactoring)
// Eski kodu "kupon eklenebilir" hale getir
// commit: "refactor: extract discount calculation"

// ADIM 2: Sonra feature (şapka 2: feature)
// Temizlenmiş koda kuponu ekle
// commit: "feat: add coupon discount support"

// Jessica Kerr: "Bir feature'ı şu anki yapıya eklemek zorsa,
// önce yapıyı feature'ı eklemeyi KOLAYLAŞTIRACAK şekilde değiştir,
// sonra feature'ı ekle."
```

### Anlama Refactoring'i (Comprehension) 🧠

```
Kodu okuyor ve ANLAMIYORSUN.
→ Anladıkça refactor et!
→ "aa, bu değişken aslında şu anlama geliyor" → RENAME!
→ "Bu 3 satır aslında bir KAVRAM" → EXTRACT FUNCTION!
→ Kodun sana ANLATTIKLARINI, koda GERİ YANSIT.

Fowler: "Kodu her okuduğumda, onu BİRAZ DAHA İYİ bırakırım."
```

### Çöp Toplama Refactoring'i (Litter-Pickup) 🗑️

```
Başka bir iş yaparken "kötü kokan" kod gördün:
  → Hemen düzelt (küçükse)
  → Not al (büyükse — sonra ayrı bir PR'da)

Boy Scout Rule (İzci Kuralı):
"Kamp alanını bulduğundan DAHA TEMİZ bırak."
→ Bir dosyaya dokunduysan, dosyayı biraz DAHA İYİ bırak.
```

### Ne Zaman Refactoring YAPMA ❌

```
1. Koda DOKUNMUYORSAN → Refactor etme
   → Çalışıyor, kimse değiştirmiyor → bırak

2. Sıfırdan yazmak DAHA KOLAY ise → Rewrite
   → Nadiren! Ama bazen gerçekten en iyi yol

3. Deadline çok YAKINSA → Şimdi değil
   → AMA deadline'dan sonra YAP!
   → "Deadline bitti, şimdi temizleme zamanı"

4. Kodun TEST'i YOKSA → Önce test yaz 🧪
   → Refactoring testSİZ yapılmaz!
   → Characterization test: "Mevcut davranışı kilitle"
```

---

## 4. 👃 Code Smells — Kötü Kokular

Fowler ve Kent Beck'in belirlediği 24 "code smell." Her koku, belirli refactoring tekniklerini işaret eder.

### Smell 1: Mysterious Name (Gizemli İsim) 🔮

```javascript
// ❌ KOKU: İsimden ne yaptığı anlaşılmıyor
function calc(x, y, z) { ... }
const d = new Date() - startDate;
const temp = users.filter(u => u.a && u.s > 3);

// ✅ TEMİZ: İsim her şeyi anlatıyor
function calculateMonthlyPremium(age, income, riskFactor) { ... }
const elapsedTimeMs = new Date() - startDate;
const activeExperiencedUsers = users.filter(u => u.isActive && u.yearsOfService > 3);
```

**Refactoring:** Rename Variable, Rename Function, Rename Field

### Smell 2: Duplicated Code (Tekrarlanan Kod) 📋📋

```javascript
// ❌ KOKU: Aynı mantık 2+ yerde
function getAdminReport() {
  const users = db.query('SELECT * FROM users WHERE role = "admin"');
  const total = users.reduce((sum, u) => sum + u.salary, 0);
  const avg = total / users.length;
  return { users, total, average: avg };
}

function getManagerReport() {
  const users = db.query('SELECT * FROM users WHERE role = "manager"');
  const total = users.reduce((sum, u) => sum + u.salary, 0);
  const avg = total / users.length;
  return { users, total, average: avg };
}

// ✅ TEMİZ: Ortak mantık çıkarıldı
function getRoleReport(role) {
  const users = db.query(`SELECT * FROM users WHERE role = $1`, [role]);
  const total = users.reduce((sum, u) => sum + u.salary, 0);
  const average = total / users.length;
  return { users, total, average };
}
```

**Refactoring:** Extract Function, Slide Statements, Pull Up Method

### Smell 3: Long Function (Uzun Fonksiyon) 📜

```javascript
// ❌ KOKU: 100+ satırlık fonksiyon
async function processOrder(orderData) {
  // Validasyon (20 satır)
  if (!orderData.items) throw new Error('...');
  // ... 18 satır daha

  // Stok kontrolü (15 satır)
  for (const item of orderData.items) {
    // ... 13 satır
  }

  // Fiyat hesaplama (25 satır)
  let total = 0;
  // ... 23 satır

  // Ödeme işleme (20 satır)
  // ... 18 satır

  // Bildirim gönderme (15 satır)
  // ... 13 satır

  // Loglama (10 satır)
  // ... 8 satır
}

// ✅ TEMİZ: Her bölüm kendi fonksiyonunda
async function processOrder(orderData) {
  validateOrder(orderData);
  await checkStockAvailability(orderData.items);
  const total = calculateTotal(orderData);
  await processPayment(orderData.userId, total);
  await sendOrderConfirmation(orderData);
  logOrderProcessed(orderData);
}
```

**Refactoring:** Extract Function, Replace Temp with Query, Decompose Conditional

> **Fowler:** "Bir fonksiyonu ne kadar uzun olduğuna göre değil, NE YAPTIĞI ile NASIL YAPTIĞI arasındaki mesafeye göre değerlendir. Bir yorum yazmak istiyorsan, bunun yerine fonksiyon çıkar — yorumun fonksiyon adı olsun."

### Smell 4: Long Parameter List (Uzun Parametre Listesi) 📋

```javascript
// ❌ KOKU: Çok fazla parametre
function createUser(firstName, lastName, email, phone,
  street, city, zipCode, country,
  birthDate, gender, preferredLanguage) {
  // ...
}

// ✅ TEMİZ: Parametreleri nesneye grupla
function createUser({ personalInfo, address, preferences }) {
  // ...
}

createUser({
  personalInfo: { firstName: 'Ali', lastName: 'Yılmaz', email: 'ali@mail.com' },
  address: { city: 'İstanbul', zipCode: '34000' },
  preferences: { language: 'tr' }
});
```

**Refactoring:** Introduce Parameter Object, Preserve Whole Object, Replace Parameter with Query

### Smell 5: Global Data (Global Veri) 🌍

```javascript
// ❌ KOKU: Global değişken — HER YERDEN değiştirilebilir
let currentUser = null;
let appConfig = {};

// Herhangi bir yerden:
currentUser = { name: 'Hacker' }; // 😱 Kim değiştirdi? Nereden? Debug KABUSTUR!

// ✅ TEMİZ: Kapsüllenmiş erişim
class SessionManager {
  #currentUser = null;

  setUser(user) {
    if (!user?.id) throw new Error('Geçersiz kullanıcı');
    this.#currentUser = Object.freeze(user);
    this.#logSessionChange(user);
  }

  getUser() {
    return this.#currentUser;
  }
}
```

**Refactoring:** Encapsulate Variable

### Smell 6: Mutable Data (Değiştirilebilir Veri) 🔓

```javascript
// ❌ KOKU: Veri her yerden değişiyor
const order = { items: [], total: 0, status: 'draft' };
order.items.push({ name: 'Laptop', price: 10000 });
order.total = 10000;
// Başka bir yerde...
order.total = -5; // Kimse fark etmedi! 💥

// ✅ TEMİZ: Değiştirmek için metotlar kullan
class Order {
  #items = [];
  #status = 'draft';

  addItem(item) {
    if (this.#status !== 'draft') throw new Error('Sipariş kilitli');
    this.#items.push(Object.freeze(item));
  }

  get total() {
    return this.#items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  }

  get items() {
    return [...this.#items]; // Kopya döndür, orijinali koru!
  }
}
```

**Refactoring:** Encapsulate Variable, Split Variable, Replace Derived Variable with Query

### Smell 7: Divergent Change (Iraksak Değişim) 🔀

```
Bir sınıf, FARKLI nedenlerle sürekli DEĞİŞİYOR:
  → Yeni veritabanı → Bu sınıfı değiştir
  → Yeni iş kuralı → Bu sınıfı değiştir
  → Yeni API formatı → Bu sınıfı değiştir
  = Bu sınıf TOO MANY reasons to change! (SRP ihlali)

Çözüm: Farklı değişim nedenlerini FARKLI sınıflara ayır
```

**Refactoring:** Split Phase, Move Function, Extract Class

### Smell 8: Shotgun Surgery (Saçma Ameliyatı) 💥

```
Tek bir değişiklik yapınca BİRÇOK sınıfı değiştirmen gerekiyor:
  → Yeni alan ekle → 5 dosyayı değiştir
  → Format değiştir → 8 dosyayı değiştir

Divergent Change'in tersi:
  Divergent: 1 sınıf, çok neden
  Shotgun:   1 neden, çok sınıf

Çözüm: İlgili kodu TEK bir yere topla
```

**Refactoring:** Move Function, Move Field, Combine Functions into Class, Inline Function

### Smell 9: Feature Envy (Özellik Kıskançlığı) 👀

```javascript
// ❌ KOKU: Bu fonksiyon başka sınıfın verisini çok fazla kullanıyor
function calculateShippingCost(order) {
  const baseWeight = order.items.reduce((w, i) => w + i.weight, 0);
  const destination = order.address.city;
  const zone = order.address.country === 'TR' ? 'domestic' : 'international';
  const distance = getDistance(order.address.zipCode);
  // order.address'i çok fazla kullanıyoruz! Address'e "kıskanç bakıyoruz"!
}

// ✅ TEMİZ: Fonksiyonu verinin OLDUĞU yere taşı
class Address {
  getShippingZone() {
    return this.country === 'TR' ? 'domestic' : 'international';
  }

  getDistance() {
    return distanceCalculator.fromZipCode(this.zipCode);
  }
}
```

**Refactoring:** Move Function, Extract Function

### Smell 10: Data Clumps (Veri Kümeleri) 📦

```javascript
// ❌ KOKU: Aynı parametreler her yerde birlikte geçiyor
function plotPoint(x, y, z) { ... }
function distanceBetween(x1, y1, z1, x2, y2, z2) { ... }
function translatePoint(x, y, z, dx, dy, dz) { ... }

// x, y, z her zaman birlikte → BUNLAR BİR NESNE!

// ✅ TEMİZ: Nesne oluştur
class Point3D {
  constructor(x, y, z) { this.x = x; this.y = y; this.z = z; }

  distanceTo(other) {
    return Math.sqrt(
      (this.x - other.x) ** 2 +
      (this.y - other.y) ** 2 +
      (this.z - other.z) ** 2
    );
  }

  translate(dx, dy, dz) {
    return new Point3D(this.x + dx, this.y + dy, this.z + dz);
  }
}
```

**Refactoring:** Introduce Parameter Object, Extract Class, Preserve Whole Object

### Smell 11: Primitive Obsession (İlkel Takıntı) 🔢

```javascript
// ❌ KOKU: Her şey string/number — domain kavramları kayıp
function createUser(name, email, phone, currency, amount) {
  if (!email.includes('@')) throw new Error('Geçersiz email');
  if (amount < 0) throw new Error('Negatif tutar');
  if (!['TRY', 'USD', 'EUR'].includes(currency)) throw new Error('Geçersiz para birimi');
  // Validasyon HER YERDE tekrar ediliyor!
}

// ✅ TEMİZ: Domain nesneleri oluştur (Value Objects)
class Email {
  #value;
  constructor(value) {
    if (!value.includes('@')) throw new Error('Geçersiz email');
    this.#value = value.toLowerCase();
  }
  toString() { return this.#value; }
}

class Money {
  #amount;
  #currency;
  constructor(amount, currency) {
    if (amount < 0) throw new Error('Negatif tutar');
    if (!['TRY', 'USD', 'EUR'].includes(currency)) throw new Error('Geçersiz para birimi');
    this.#amount = amount;
    this.#currency = currency;
  }
  add(other) {
    if (this.#currency !== other.currency) throw new Error('Farklı para birimleri');
    return new Money(this.#amount + other.amount, this.#currency);
  }
}

// Validasyon TEK YERDE, nesne oluşturulurken yapılıyor ✅
const email = new Email('ali@mail.com'); // Geçersizse hemen hata!
const price = new Money(100, 'TRY');
```

**Refactoring:** Replace Primitive with Object, Replace Type Code with Subclasses

### Smell 12: Repeated Switches / Conditional Complexity 🔀

```javascript
// ❌ KOKU: Aynı switch/if-else birçok yerde tekrar
function calculatePay(employee) {
  switch (employee.type) {
    case 'engineer': return employee.salary;
    case 'manager': return employee.salary + employee.bonus;
    case 'intern': return employee.salary * 0.5;
  }
}

function getTitle(employee) {
  switch (employee.type) {
    case 'engineer': return 'Yazılım Mühendisi';
    case 'manager': return 'Yönetici';
    case 'intern': return 'Stajyer';
  }
}

// Her yeni çalışan tipi = TÜM switch'leri güncelle! 😩

// ✅ TEMİZ: Polimorfizm kullan
class Engineer {
  calculatePay() { return this.salary; }
  getTitle() { return 'Yazılım Mühendisi'; }
}

class Manager {
  calculatePay() { return this.salary + this.bonus; }
  getTitle() { return 'Yönetici'; }
}

// Yeni tip ekle → Yeni sınıf yaz, mevcut koda DOKUNMA! ✅
```

**Refactoring:** Replace Conditional with Polymorphism, Replace Type Code with Subclasses

### Diğer Önemli Kokular (Kısa)

| Koku | Açıklama | Refactoring |
|---|---|---|
| **Lazy Element** | İşe yaramayan sınıf/fonksiyon | Inline Function/Class |
| **Speculative Generality** | "İleride lazım olur" kodu | YAGNI! Sil. |
| **Dead Code** | Asla çalışmayan kod | Sil! |
| **Middle Man** | Sadece delege eden sınıf | Inline, Remove Middle Man |
| **Insider Trading** | İki modül çok fazla bilgi paylaşıyor | Move Function, Hide Delegate |
| **Large Class** | Çok fazla sorumluluk | Extract Class, Extract Superclass |
| **Comments** | Kötü kodu açıklamak için yorum | Kodu iyileştir, yorum gereksiz kalır |
| **Refused Bequest** | Alt sınıf üst sınıfın özelliklerini kullanmıyor | Replace Inheritance with Delegation |

---

## 5. 🛠️ Temel Refactoring Teknikleri

### Extract Function (Fonksiyon Çıkar) ⭐

**En sık kullanılan refactoring!**

```javascript
// ÖNCE:
function printOwing(invoice) {
  printBanner();

  let outstanding = 0;
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // Print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
  console.log(`due: ${invoice.dueDate.toLocaleDateString()}`);
}

// SONRA:
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
  console.log(`due: ${invoice.dueDate.toLocaleDateString()}`);
}
```

**Ne zaman çıkar?**
> "Eğer bir kod bloğuna YORUM yazma ihtiyacı hissediyorsan, onu bir fonksiyon olarak çıkar ve yorumu FONKSİYON ADI yap."

```javascript
// Yorum yerine fonksiyon adı:
// ❌ // Check if user is eligible for discount
if (user.age > 18 && user.orders.length > 5 && !user.isBanned) { ... }

// ✅
if (isEligibleForDiscount(user)) { ... }

function isEligibleForDiscount(user) {
  return user.age > 18 && user.orders.length > 5 && !user.isBanned;
}
```

### Inline Function (Fonksiyon Satır İçi Yap) 🔙

Extract Function'ın tersi. Fonksiyon gereksizse:

```javascript
// ÖNCE: Fonksiyon, gövdesinden daha karmaşık DEĞİL
function moreThanFiveOrders(customer) {
  return customer.orders.length > 5;
}
function isGoldCustomer(customer) {
  return moreThanFiveOrders(customer);
}

// SONRA: Inline et, gereksiz dolaylama kaldır
function isGoldCustomer(customer) {
  return customer.orders.length > 5;
}
```

### Extract Variable (Değişken Çıkar) 📝

```javascript
// ÖNCE: Karmaşık ifade
function price(order) {
  return order.quantity * order.itemPrice -
    Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
    Math.min(order.quantity * order.itemPrice * 0.1, 100);
}

// SONRA: Açıklayıcı değişkenler
function price(order) {
  const basePrice = order.quantity * order.itemPrice;
  const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
  const shipping = Math.min(basePrice * 0.1, 100);
  return basePrice - quantityDiscount + shipping;
}
```

### Inline Variable (Değişken Satır İçi Yap) 🔙

```javascript
// ÖNCE: Değişken ifadeden daha açıklayıcı DEĞİL
const basePrice = order.basePrice;
return basePrice > 1000;

// SONRA:
return order.basePrice > 1000;
```

### Rename Variable / Function / Field (Yeniden Adlandır) 📛

```javascript
// ÖNCE:
const a = height * width;
function ck(u) { return u.s > 3; }

// SONRA:
const area = height * width;
function isExperiencedUser(user) { return user.yearsOfService > 3; }
```

> **Fowler:** "İyi isimlendirme, temiz kodun temelidir. İsimlere ne kadar çok zaman harcarsan, kodu o kadar az okumanız gerekir."

### Change Function Declaration (Fonksiyon İmzasını Değiştir) ✍️

```javascript
// ÖNCE: Parametre eksik/fazla/yanlış isimli
function circum(radius) { ... }

// SONRA:
function circumference(radius) { ... }

// Adım adım (migrate):
// 1. Yeni adla fonksiyon oluştur, eski fonksiyon yeniyi çağırsın
// 2. Tüm çağıranları yeni fonksiyona yönlendir
// 3. Eski fonksiyonu sil
```

---

## 6. 🔒 Kapsülleme Refactoring'leri

### Encapsulate Variable (Değişkeni Kapsülle) 🔐

```javascript
// ÖNCE: Global erişilebilir veri
let defaultOwner = { firstName: 'Martin', lastName: 'Fowler' };

// Herhangi bir yerden:
defaultOwner.firstName = 'Hacker'; // 😱 Kontrolsüz değişiklik!

// SONRA: Getter/setter ile koruma
let _defaultOwner = { firstName: 'Martin', lastName: 'Fowler' };

function getDefaultOwner() {
  return { ..._defaultOwner }; // KOPYA döndür! Orijinali korur.
}

function setDefaultOwner(owner) {
  _defaultOwner = { ...owner }; // Validasyon eklenebilir
}
```

### Encapsulate Record (Kaydı Kapsülle) 📦

```javascript
// ÖNCE: Ham nesne — yapısı kontrolsüz
const organization = { name: 'Acme Corp', country: 'TR' };
organization.name = ''; // Boş isim? Kimse kontrol etmiyor!

// SONRA: Sınıf ile kapsülle
class Organization {
  #name;
  #country;

  constructor(data) {
    this.#name = data.name;
    this.#country = data.country;
  }

  get name() { return this.#name; }
  set name(value) {
    if (!value?.trim()) throw new Error('İsim boş olamaz!');
    this.#name = value.trim();
  }

  get country() { return this.#country; }
}
```

### Encapsulate Collection (Koleksiyonu Kapsülle) 📚

```javascript
// ❌ KOKU: İç koleksiyon dışarıya sızıyor
class Course {
  get students() { return this.#students; } // Orijinal diziyi döndürüyor!
}

const course = new Course();
course.students.push(evilStudent); // 😱 Sınıf habersiz, doğrulama yok!

// ✅ TEMİZ: Koleksiyonu koru
class Course {
  #students = [];

  get students() { return [...this.#students]; } // KOPYA döndür!

  addStudent(student) {
    if (this.#students.length >= 30) throw new Error('Sınıf dolu!');
    if (this.#students.find(s => s.id === student.id)) throw new Error('Zaten kayıtlı!');
    this.#students.push(student);
  }

  removeStudent(studentId) {
    this.#students = this.#students.filter(s => s.id !== studentId);
  }
}
```

---

## 7. 🚚 Feature Taşıma Refactoring'leri

### Move Function (Fonksiyonu Taşı) 📦→📦

```javascript
// ÖNCE: trackSummary hesaplaması Account'ta, ama daha çok GPS verisi kullanıyor
class Account {
  calculateDistance(points) {
    let total = 0;
    for (let i = 1; i < points.length; i++) {
      total += haversine(points[i-1], points[i]); // GPS hesabı!
    }
    return total;
  }
}

// SONRA: GPS ile ilgili fonksiyon GPS modülüne taşındı
class GPSTracker {
  calculateDistance(points) {
    let total = 0;
    for (let i = 1; i < points.length; i++) {
      total += haversine(points[i-1], points[i]);
    }
    return total;
  }
}
// Feature Envy kokusunu giderdik! ✅
```

### Slide Statements (İfadeleri Kaydır) ↕️

```javascript
// ÖNCE: İlgili satırlar dağınık
const pricingPlan = retrievePricingPlan();
const order = retreiveOrder();
let charge;
const chargePerUnit = pricingPlan.unit;

// SONRA: İlgili satırları bir araya getir
const pricingPlan = retrievePricingPlan();
const chargePerUnit = pricingPlan.unit; // pricingPlan ile ilgili → yanına kaydır

const order = retreiveOrder();
let charge;
```

### Split Loop (Döngüyü Böl) ✂️

```javascript
// ÖNCE: Tek döngüde birden fazla iş
let youngest = Infinity;
let totalSalary = 0;
for (const person of people) {
  if (person.age < youngest) youngest = person.age;
  totalSalary += person.salary;
}

// SONRA: Her döngü TEK iş yapar
const youngest = Math.min(...people.map(p => p.age));
const totalSalary = people.reduce((sum, p) => sum + p.salary, 0);

// "Ama iki kez döngü dönüyorsun! Performans!" diye düşünme.
// 1. Çoğu durumda fark YOK (N küçük)
// 2. Okunabilirlik > mikro-optimizasyon
// 3. Profiler sorunu gösterirse O ZAMAN birleştir
```

### Replace Loop with Pipeline (Döngüyü Pipeline'la Değiştir) 🔗

```javascript
// ÖNCE: Klasik for döngüsü
const result = [];
for (const person of people) {
  if (person.age >= 18) {
    if (person.city === 'İstanbul') {
      result.push(person.name.toUpperCase());
    }
  }
}
result.sort();

// SONRA: Pipeline (fonksiyonel zincir)
const result = people
  .filter(p => p.age >= 18)
  .filter(p => p.city === 'İstanbul')
  .map(p => p.name.toUpperCase())
  .sort();

// Her adım NE yaptığını söylüyor:
// filter → filter → map → sort
// Akış SOL'dan SAĞA okunur, döngü analizine GEREK YOK ✅
```

---

## 8. 📊 Veri Organizasyonu

### Replace Temp with Query (Geçici Değişkeni Sorgu ile Değiştir) 🔄

```javascript
// ÖNCE: Geçici değişken
function calculateTotal(order) {
  const basePrice = order.quantity * order.itemPrice;
  if (basePrice > 1000) return basePrice * 0.95;
  return basePrice * 0.98;
}

// SONRA: Sorgu (fonksiyon çağrısı)
function calculateTotal(order) {
  if (basePrice(order) > 1000) return basePrice(order) * 0.95;
  return basePrice(order) * 0.98;
}

function basePrice(order) {
  return order.quantity * order.itemPrice;
}

// Neden? basePrice artık başka yerlerden de KULLANILABILIR!
// Geçici değişken sadece O fonksiyonda yaşar → sınırlı
```

### Split Variable (Değişkeni Böl) ✂️

```javascript
// ❌ KOKU: Bir değişken birden fazla AMAÇ için kullanılıyor
let temp = 2 * (height + width);  // temp = çevre
console.log(`Çevre: ${temp}`);
temp = height * width;             // temp artık ALAN?! 🤯
console.log(`Alan: ${temp}`);

// ✅ TEMİZ: Her amaç için ayrı değişken
const perimeter = 2 * (height + width);
console.log(`Çevre: ${perimeter}`);
const area = height * width;
console.log(`Alan: ${area}`);
```

### Replace Magic Number with Symbolic Constant (Sihirli Sayıyı Sabitle Değiştir) 🔢→📛

```javascript
// ❌ KOKU: 0.08 ne? 86400 ne? 30 ne?
if (amount * 0.08 > 1000) { ... }
setTimeout(cleanup, 86400000);
if (retries > 30) throw new Error('Failed');

// ✅ TEMİZ: Sabitlere isim ver
const TAX_RATE = 0.08;
const ONE_DAY_MS = 24 * 60 * 60 * 1000;
const MAX_RETRY_COUNT = 30;

if (amount * TAX_RATE > 1000) { ... }
setTimeout(cleanup, ONE_DAY_MS);
if (retries > MAX_RETRY_COUNT) throw new Error('Failed');
```

---

## 9. 🔀 Koşullu Mantığı Sadeleştirme

### Decompose Conditional (Koşulu Parçala) 🧩

```javascript
// ÖNCE: Karmaşık koşul
if (date.isBefore(plan.summerStart) || date.isAfter(plan.summerEnd)) {
  charge = quantity * plan.winterRate + plan.winterServiceCharge;
} else {
  charge = quantity * plan.summerRate;
}

// SONRA: Koşulları anlamlı fonksiyonlara çıkar
if (isSummer(date, plan)) {
  charge = summerCharge(quantity, plan);
} else {
  charge = winterCharge(quantity, plan);
}

function isSummer(date, plan) {
  return !date.isBefore(plan.summerStart) && !date.isAfter(plan.summerEnd);
}

function summerCharge(quantity, plan) {
  return quantity * plan.summerRate;
}

function winterCharge(quantity, plan) {
  return quantity * plan.winterRate + plan.winterServiceCharge;
}
```

### Consolidate Conditional (Koşulları Birleştir) 🤝

```javascript
// ÖNCE: Aynı sonuca götüren farklı koşullar
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;

// SONRA: TEK koşulda birleştir
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2
    || employee.monthsDisabled > 12
    || employee.isPartTime;
}
```

### Replace Nested Conditional with Guard Clauses (İç İçe Koşulları Koruma İfadeleriyle Değiştir) 🛡️

```javascript
// ❌ KOKU: İç içe if — "arrow code" / "hadouken code"
function getPayAmount(employee) {
  let result;
  if (employee.isSeparated) {
    result = { amount: 0, reason: 'separated' };
  } else {
    if (employee.isRetired) {
      result = { amount: 0, reason: 'retired' };
    } else {
      // Normal hesaplama... 20 satır derinlikte
      result = calculateNormalPay(employee);
    }
  }
  return result;
}

// ✅ TEMİZ: Guard clause'lar ile düzleştir
function getPayAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reason: 'separated' };
  if (employee.isRetired)   return { amount: 0, reason: 'retired' };

  return calculateNormalPay(employee);
}
// DÜMDÜZ! İstisnaları erken ele al, normal akış en altta. ✅
```

### Replace Conditional with Polymorphism (Koşulu Polimorfizmle Değiştir) 🎭

```javascript
// ÖNCE: Tip bazlı switch → her yeni tip = her switch'i güncelle
function calculateArea(shape) {
  switch (shape.type) {
    case 'circle':    return Math.PI * shape.radius ** 2;
    case 'rectangle': return shape.width * shape.height;
    case 'triangle':  return 0.5 * shape.base * shape.height;
  }
}

// SONRA: Her şekil kendi hesabını biliyor
class Circle {
  constructor(radius) { this.radius = radius; }
  calculateArea() { return Math.PI * this.radius ** 2; }
}

class Rectangle {
  constructor(width, height) { this.width = width; this.height = height; }
  calculateArea() { return this.width * this.height; }
}

class Triangle {
  constructor(base, height) { this.base = base; this.height = height; }
  calculateArea() { return 0.5 * this.base * this.height; }
}

// Yeni şekil? Yeni sınıf. Mevcut koda DOKUNMA! ✅ (Open/Closed Principle)
```

### Introduce Special Case / Null Object (Özel Durum Nesnesi) 🎯

```javascript
// ❌ KOKU: Her yerde null kontrolü
function getCustomerName(site) {
  const customer = site.customer;
  if (customer === null) return 'Misafir';
  return customer.name;
}

function getCustomerPlan(site) {
  const customer = site.customer;
  if (customer === null) return 'basic';
  return customer.plan;
}

// "customer === null" check her yerde tekrar ediyor! 😩

// ✅ TEMİZ: Null Object (Special Case)
class UnknownCustomer {
  get name() { return 'Misafir'; }
  get plan() { return 'basic'; }
  get isUnknown() { return true; }
}

// site.customer artık ASLA null değil, ya gerçek müşteri ya UnknownCustomer
function getCustomerName(site) {
  return site.customer.name; // null check YOK! ✅
}

function getCustomerPlan(site) {
  return site.customer.plan; // null check YOK! ✅
}
```

### Introduce Assertion (Doğrulama Ekle) ✅

```javascript
// ÖNCE: Varsayımlar gizli
function calculateDiscount(price, discountRate) {
  return price * (1 - discountRate); // discountRate 0-1 arası olmalı... mı?
}

// SONRA: Varsayımları AÇIK yap
function calculateDiscount(price, discountRate) {
  console.assert(price >= 0, 'Fiyat negatif olamaz');
  console.assert(discountRate >= 0 && discountRate <= 1, 'İndirim 0-1 arası olmalı');
  return price * (1 - discountRate);
}
```

---

## 10. 🔌 API Refactoring'leri

### Separate Query from Modifier (Sorguyu Değiştiriciden Ayır) 🔍✏️

```javascript
// ❌ KOKU: Fonksiyon hem veri döndürüyor HEM de yan etkisi var
function getTotalAndSendAlert(orders) {
  const total = orders.reduce((sum, o) => sum + o.amount, 0);
  if (total > 10000) sendAlert('Yüksek harcama!'); // Yan etki!
  return total; // Sorgu
}
// Bu fonksiyonu çağırmak GÜVENLİ Mİ? Her çağırdığında alert gider mi?

// ✅ TEMİZ: Ayır!
function getTotal(orders) {
  return orders.reduce((sum, o) => sum + o.amount, 0); // SORU: sadece veri döner
}

function sendHighSpendingAlert(orders) {
  if (getTotal(orders) > 10000) sendAlert('Yüksek harcama!'); // KOMUT: yan etki
}

// CQS (Command-Query Separation): Sorgu = veri döndür, Komut = değişiklik yap. İkisini KARIŞTIRMA!
```

### Replace Parameter with Query (Parametreyi Sorguyla değiştir) 🔄

```javascript
// ÖNCE: Gereksiz parametre — çağıran hesaplıyor, çağrılan da hesaplayabilir
function finalPrice(basePrice, discountLevel) {
  return basePrice * (1 - discountByLevel(discountLevel));
}
// Çağıran: finalPrice(basePrice, customer.discountLevel)

// SONRA: Parametreyi kaldır, fonksiyon kendi hesaplasın
function finalPrice(basePrice, customer) {
  const discountLevel = customer.discountLevel; // Kendi sorsun!
  return basePrice * (1 - discountByLevel(discountLevel));
}
```

### Remove Flag Argument (Bayrak Parametresini Kaldır) 🚩

```javascript
// ❌ KOKU: Boolean parametre — hangi davranışı seçtiği AÇIK DEĞİL
function setDimension(name, value, isMetric) {
  if (isMetric) { /* ... */ }
  else { /* ... */ }
}
setDimension('height', 180, true);  // true ne demek? 🤷
setDimension('height', 6, false);   // false ne demek? 🤷

// ✅ TEMİZ: Ayrı fonksiyonlar
function setDimensionInCm(name, value) { /* ... */ }
function setDimensionInFeet(name, value) { /* ... */ }

setDimensionInCm('height', 180);    // Açık ve net! ✅
setDimensionInFeet('height', 6);    // Açık ve net! ✅
```

---

## 11. 🧬 Kalıtım ile İlgili Refactoring'ler

### Pull Up Method / Field (Metodu/Alanı Yukarı Çek) ⬆️

```javascript
// ÖNCE: Aynı metod iki alt sınıfta tekrar
class Employee {
  get name() { return this.#name; }
}
class Engineer extends Employee {
  getAnnualCost() { return this.monthlySalary * 12; } // Tekrar!
}
class Manager extends Employee {
  getAnnualCost() { return this.monthlySalary * 12; } // Tekrar!
}

// SONRA: Üst sınıfa çek
class Employee {
  get name() { return this.#name; }
  getAnnualCost() { return this.monthlySalary * 12; } // TEK YER ✅
}
```

### Push Down Method / Field (Metodu/Alanı Aşağı İt) ⬇️

```javascript
// ÖNCE: Üst sınıftaki metod sadece BİR alt sınıf tarafından kullanılıyor
class Employee {
  getManagerBonus() { return this.salary * 0.1; } // Sadece Manager kullanıyor!
}

// SONRA: Sadece kullanan alt sınıfa taşı
class Manager extends Employee {
  getManagerBonus() { return this.salary * 0.1; } // Sadece burada ✅
}
```

### Replace Inheritance with Delegation (Kalıtımı Delegasyonla Değiştir) 🔄

```javascript
// ❌ KOKU: Stack, List'i extend ediyor ama List'in tüm metodlarını İSTEMİYOR
class Stack extends List {
  push(item) { this.add(item); }
  pop() { return this.removeLast(); }
  // AMA! stack.get(3) çağrılabilir → Stack semantiği BOZULDU! 😱
  // Stack LIFO olmalı, ama List tüm metodlarını açıyor
}

// ✅ TEMİZ: Delegasyon (HAS-A)
class Stack {
  #storage = new List();

  push(item) { this.#storage.add(item); }
  pop() { return this.#storage.removeLast(); }
  peek() { return this.#storage.getLast(); }
  get size() { return this.#storage.length; }

  // get(3) YOK! Sadece Stack operasyonları mevcut ✅
}
```

---

## 12. 🏔️ Büyük Refactoring'ler

Bazen küçük adımlar yetmez, mimari düzeyinde refactoring gerekir:

### Strangler Fig Pattern 🌿

Büyük bir sistemi **kademeli olarak** yenisiyle değiştir:

```
[ESKİ SİSTEM] ← Tüm trafik

Adım 1: Yeni feature YENİ sistemde yaz
[ESKİ SİSTEM] ← Çoğu trafik
[YENİ SİSTEM] ← Birkaç endpoint

Adım 2: Eski endpoint'leri TEK TEK yeniye taşı
[ESKİ SİSTEM] ← Az trafik
[YENİ SİSTEM] ← Çoğu trafik

Adım 3: Eski sistemi KAPAT
[YENİ SİSTEM] ← Tüm trafik ✅

→ Risk az, kademeli, geri alınabilir!
→ "Big bang rewrite" yerine HER ZAMAN bunu tercih et
```

### Branch by Abstraction 🌿🔀

Büyük bir iç bileşeni değiştirmek için:

```javascript
// ADIM 1: Mevcut koda bir soyutlama katmanı ekle (interface)
class NotificationSender {
  send(userId, message) { throw new Error('Implement me'); }
}

// ADIM 2: Mevcut implementasyonu bu interface'e uyarla
class LegacyEmailNotification extends NotificationSender {
  send(userId, message) {
    legacyEmailSystem.fire(userId, message); // Eski sistem
  }
}

// ADIM 3: Yeni implementasyonu yaz
class PushNotification extends NotificationSender {
  send(userId, message) {
    firebase.sendPushNotification(userId, message); // Yeni sistem
  }
}

// ADIM 4: Feature flag ile geçiş yap
function getNotificationSender() {
  if (featureFlags.isEnabled('push-notifications')) {
    return new PushNotification();    // Yeni
  }
  return new LegacyEmailNotification(); // Eski
}

// ADIM 5: Yeni sistem stabil olunca → eski kodu SİL
```

---

## 13. ⚡ Refactoring ve Performans

### Fowler'ın Yaklaşımı 🏎️

> **"Önce TEMİZ yaz, sonra ÖLÇÜM yap, sorun varsa OPTİMİZE et."**

```
90/10 Kuralı:
  Kodun %90'ı performans açısından ÖNEMSİZ.
  Kodun %10'u zamanın %90'ını tüketir.

Premature optimization:
  ❌ "Bu döngü yavaş olabilir, optimizasyon yapalım"
     → Belki o döngü milisaniye bile sürmüyor!

Doğru yaklaşım:
  1. Temiz, okunabilir kod yaz ✅
  2. Profiler ile ÖLÇ → "Darboğaz nerede?" 🎯
  3. Darboğazı optimize et
  4. Tekrar ölç → "İyileşme var mı?"
  5. Yoksa geri al! (Refactoring güvenli geri alınır)

Cleaner code = Easier optimization!
  → Temiz kod, darboğazı BULMAYAMI kolaylaştırır
  → Temiz kod, darboğazı DÜZELTMEYİ kolaylaştırır
```

```javascript
// KÖTÜ: Okunmaz "hızlı" kod
function f(d) {
  let r=0,i=d.length;while(i--)r+=d[i].p*d[i].q;return r;
}
// Belki gerçekten hızlı AMA:
// → Bug varsa bulamazsın
// → Optimize etmen gerekirse neyi optimize edeceğini anlayamazsın

// İYİ: Temiz, sonra profiler ile kontrol
function calculateOrderTotal(items) {
  return items.reduce((total, item) => total + item.price * item.quantity, 0);
}
// → Bug anında görünür
// → Profiler "bu fonksiyon yavaş" derse → hedefli optimize et
```

---

## 14. 🔄 Refactoring İş Akışı

### Adım Adım Güvenli Refactoring 🪜

```
1. TESTLERİN GEÇTIĞINDEN EMIN OL (yeşil çubuk) ✅
   → Testlerin yoksa? ÖNCE characterization test yaz!

2. KÜÇÜK BİR ADIM AT 👣
   → Rename, extract function, inline variable...
   → TEK bir değişiklik!

3. TESTLERİ ÇALIŞTIR ✅
   → Hâlâ geçiyor mu?
   → Evet → 4. adıma
   → Hayır → 2. adımı GERİ AL (undo), tekrar dene

4. COMMIT ET 💾
   → Her başarılı adımı commit et
   → "Küçük, güvenli adım" = "küçük, güvenli commit"

5. 2'YE DÖN 🔄
   → Bir sonraki küçük adımı at

ASLA:
  ❌ 30 dosyayı aynı anda değiştirme
  ❌ Testler kırıkken devam etme
  ❌ Refactoring ve feature eklemeyi karıştırma
```

### Refactoring Commit Stratejisi 📝

```
GÜN 1: Feature ekle
  commit: "feat: add coupon validation"

GÜN 1: Baktın ki alan adları kötü
  commit: "refactor: rename 'val' to 'discountRate' in CouponService"

GÜN 1: Uzun fonksiyon gördün
  commit: "refactor: extract calculateCouponDiscount from processOrder"

GÜN 2: Feature'a devam
  commit: "feat: apply coupon to cart total"

→ Refactoring commit'leri AYRI!
→ Code review'da kolayca anlaşılır
→ Sorun çıkarsa tek tek geri alınabilir
```

### Characterization Test (Mevcut Davranışı Kilitle) 🔒

Testlerin yokken refactoring yapmak tehlikelidir. Önce **mevcut davranışı kilitle:**

```javascript
// Kodu anlamıyorsun ama çalışıyor. Ne yaparsın?
// → "Ne döndürüyor?" sorusunu sor ve KAYDET!

// Legacy fonksiyon (anlaşılmaz)
function mysteryCalc(a, b, c) {
  return ((a * 3.14 + b) / c) * (c > 10 ? 1.5 : 1);
}

// Characterization test: Mevcut davranışı KILITLE
test('mysteryCalc — mevcut davranışı koruma', () => {
  expect(mysteryCalc(10, 5, 20)).toBe(((10 * 3.14 + 5) / 20) * 1.5); // Snapshot
  expect(mysteryCalc(10, 5, 5)).toBe(((10 * 3.14 + 5) / 5) * 1);
  expect(mysteryCalc(0, 0, 1)).toBe(0);
});

// Şimdi güvenle refactor edebilirsin!
// Her adımda testleri çalıştır → aynı sonuçlar, güvendesin ✅
```

---

## 15. � Büyük Şirketlerde Refactoring

### Google — Large-Scale Changes (LSC)

```
Google'da tek bir refactoring 10,000+ dosyayı etkileyebilir:

  → Rosie: Google'ın otomatik refactoring aracı
  → Bir API imzası değişti → tüm kullananlar güncellenecek
  → İnsan kontrol eder, araç uygular
  → Trunk-based development: Hepsi tek branch'te

Ders: Refactoring'i küçük tutmak LUXURY değil,
       Google ölçeğinde HAYATTA KALMA ŞARTI.
```

### Martin Fowler'ın ThoughtWorks Deneyimi

```
ThoughtWorks (Fowler'ın şirketi) müşterilerine refactoring öğretir:

  → Strangler Fig Pattern: Eski sistemi parça parça sar
  → Branch by Abstraction: Eski kodu soyutlama arkasına al
  → Her ikisi de Fowler'ın kitabındaki PRENSİPLERDEN doğar
  → Ama kitaptaki fonksiyon-düzeyi refactoring ile
    mimari refactoring FARKLI ÖLÇEKLERDİR
```

### Spotify — Refactoring + Autonomy

```
Her squad kendi microservice'inden sorumlu:
  → "Kendi kodunu kendi temizle" kültürü
  → Ama ORTAK kütüphaneler refactor edilince?
  → Consumer-Driven Contract Tests ile güvenli geçiş

Ders: Refactoring sadece TEKNİK değil, ORGANİZASYONEL.
       Conway's Law: Kod yapısı = organizasyon yapısı.
```

### Getir'de Refactoring

```
Hızlı büyüyen startup'larda refactoring genelde "sonra yaparız":
  → Tech Debt birikir, velocity DÜŞER
  → "Hız için kaliteyi feda ettik" → sonra hızı KALİTESİZLİK feda eder

Fowler'ın cevabı:
  → Refactoring İÇİN izin isteme
  → Feature geliştirirken refactor et ("İki Şapka")
  → "Bu sprint'te refactoring yapacağım" deme
  → "Bu feature'ı yaparken kodu da iyileştireceğim" de
```

---

## 16. 🤖 Yapay Zeka Çağında Refactoring

### AI Refactoring Yapabilir mi?

2024'te AI araçları (Copilot, Cursor, ChatGPT) refactoring konusunda **en güçlü** oldukları alandalar. Neden?

```
Refactoring = Davranış DEĞİŞMEDEN yapıyı değiştir
AI = Pattern tanıma konusunda mükemmel

Bu ikisi ÇOK uyumlu:
  ✅ Rename Variable/Function → AI mükemmel
  ✅ Extract Function → AI iyi (bağlamı anlıyor)
  ✅ Inline Variable → AI mükemmel
  ✅ Replace Temp with Query → AI iyi
  ✅ Code smell tespiti → AI oldukça iyi

  ⚠️ Move Function (hangi sınıfa?) → AI bazen yanılır
  ⚠️ Replace Conditional with Polymorphism → AI context kaybeder
  ❌ Mimari kararlar → AI bilgi yetersiz (domain bilmiyor)
```

### AI ile Güvenli Refactoring Prompts

```
EXTRACT FUNCTION:
  "Bu fonksiyondaki [satır X-Y] arasındaki kodu 
   ayrı bir fonksiyona çıkar. Fonksiyon adı davranışı 
   açıklasın. Parametre sayısını minimum tut. 
   Side effect olmamalı — pure function olsun mümkünse."

REPLACE CONDITIONAL:
  "Bu switch/if-else zincirini Strategy pattern ile 
   değiştir. Her case bir strateji sınıfı/fonksiyonu olsun.
   Factory fonksiyonu ile doğru stratejiyi seç.
   Mevcut davranışı DEĞİŞTİRME."

SMELL TESPİTİ:
  "Bu dosyayı Fowler'ın code smell listesine göre analiz et:
   - Long Method var mı?
   - Feature Envy var mı? (bir objenin verilerini çok kullanan)
   - Data Clumps var mı? (hep beraber gezen parametreler)
   - Divergent Change var mı? (bir sınıf birden fazla nedenden değişiyor)
   Her smell için hangi refactoring'i önerirsin?"

LEGACY KOD:
  "Bu fonksiyonun ne yaptığını açıkla, sonra 
   characterization test yaz (mevcut davranışı kilitle).
   Fowler'ın 'Preserve Whole Object' ve 
   'Replace Parameter with Query' refactoring'lerini
   uygulayarak iyileştir. Her adımda testlerin geçtiğinden emin ol."
```

### AI'ın Refactoring'de Zayıf Noktaları

```
1. KÜÇÜK ADIM prensibi:
   → AI büyük değişiklikler yapmak ister
   → Fowler: "Her seferinde BİR refactoring"
   → AI'a de ki: "Sadece BU bir adımı yap, başka değişiklik yapma"

2. TEST kontrolü:
   → AI testleri çalıştırmadan devam eder
   → Fowler: "Her adımdan sonra test çalıştır"
   → AI'a de ki: "Bu refactoring sonrası hangi testler kırılabilir?"

3. DOMAIN bilgisi:
   → AI kodu temizler ama domain kavramını anlamayabilir
   → "calculateInvoice" → AI: "compute" veya "process" der
   → Ama DOMAIN'de "invoice" ve "calculate" kritik terimlerdir
   → Ubiquitous Language'ı boz!
```

### Topluluk Görüşleri

```
Kent Beck (@KentBeck):
  "for each desired change, make the change easy 
   (warning: this may be hard), then make the easy change."
  → Refactoring'in amacı: Değişimi KOLAY yapmak

Sandi Metz:
  "Duplication is far cheaper than the wrong abstraction.
   Prefer duplication over the wrong abstraction."
  → Yanlış soyutlamayı refactor etmek, duplicate kodu 
    refactor etmekten ÇOK daha zor

Reddit r/programming'de sık tekrarlanan:
  "Fowler'ın kitabı bir REFERANS KİTAP. Baştan sona okuma,
   kod kokusu hissettiğinde aç, o refactoring'i uygula."

Martin Fowler'ın kendisi (2023 blog):
  "Refactoring bir aktivite değil, bir ALIŞKANLIK olmalı.
   'Refactoring sprint'i' = refactoring yapMIYORSUN demek."
```

---

## 17. �🎬 Son Sözler

### Fowler'ın Altın Kuralları 🏆

| # | İlke | Bir Cümlede |
|---|---|---|
| 1 | **İki şapka** | Refactoring ve feature eklemeyi AYIR |
| 2 | **Küçük adımlar** | Her adımda testler geçmeli |
| 3 | **Code smells rehber** | Koku → refactoring tekniği → uygula |
| 4 | **Testler şart** | Testsiz refactoring = ip olmadan cambazlık |
| 5 | **Sürekli yap** | Büyük "refactoring sprintleri" değil, günlük alışkanlık |
| 6 | **Performans sonra** | Önce temiz, sonra ölç, sonra optimize et |
| 7 | **Strangler Fig** | Büyük değişiklik = kademeli geçiş |
| 8 | **İzci kuralı** | Bulduğundan daha temiz bırak |
| 9 | **Üçün kuralı** | 3. tekrarda refactor et |
| 10 | **Yorum → fonksiyon** | Yorum yazmak istiyorsan, fonksiyon çıkar |

### Refactoring Katalog Özet Haritası 🗺️

```
KOKU gördüğünde → HANGİ TEKNİĞİ uygula?

Gizemli isim        → Rename
Tekrarlanan kod     → Extract Function, Pull Up Method
Uzun fonksiyon      → Extract Function, Replace Temp with Query
Uzun parametre      → Introduce Parameter Object
Global veri         → Encapsulate Variable
Değiştirilebilir veri → Encapsulate Variable, Split Variable
Feature Envy        → Move Function
Veri kümeleri       → Introduce Parameter Object, Extract Class
İlkel takıntı       → Replace Primitive with Object
Tekrarlanan switch  → Replace Conditional with Polymorphism
İç içe koşullar     → Guard Clauses
Ölü kod             → SİL!
Yorum               → Extract Function (yorum → fonksiyon adı)
Middle Man          → Inline, Remove Middle Man
```

### Tüm Kitapların Birbirine Bağlanması 🔗

```
Bu 9 kitap nasıl birbirine bağlanıyor:

📗 Grokking Algorithms
    → TEMELLERİ öğrendin

📕 Clean Code
    → "İyi kod nasıl YAZILIR?" öğrendin
    → Fowler: "Clean Code'un kurallarından bazıları aşırı dogmatik
       ama temel prensipleri değerli"

📘 Pragmatic Programmer
    → "İyi mühendis nasıl DÜŞÜNÜR?" öğrendin
    → İzci kuralı, DRY, ortogonallik bu kitapta da var

📙 The Missing README
    → "İyi mühendis nasıl ÇALIŞIR?" öğrendin
    → Refactoring'i PR sürecine dahil etmeyi buradan biliyorsun

📗 A Philosophy of Software Design
    → "Karmaşıklık nasıl azaltılır?" öğrendin
    → Refactoring'in NEDEN gerekli olduğunu derinlemesine anladın
    → Derin modüller = extract + encapsulate

📘 Head First Design Patterns
    → "Bilinen çözümler neler?" öğrendin
    → Refactoring'in HEDEFİNİ biliyorsun: kodu pattern'lara yaklaştır

📕 DDIA
    → "Veriler nasıl yönetilir?" öğrendin
    → Büyük ölçekte refactoring = schema evrimi + migration

📙 Unit Testing (Khorikov)
    → "Testler nasıl YAZILIR?" öğrendin
    → Refactoring'in KALKANININI oluşturdun

📗 Refactoring (Fowler)
    → "Mevcut kodu nasıl GÜVENle iyileştiririm?" öğrendin
    → Tüm önceki bilgileri PRATİĞE döktün
    → TAMAMLAYICI PARÇA ✅
```

### Öğrenme Yolculuğu — FAZ 1 + FAZ 2 TAMAMLANDI! 🎉🎉🎉

```
FAZ 1 ✅
  📗 Grokking Algorithms          ✅
  📕 Clean Code                   ✅
  📘 The Pragmatic Programmer     ✅
  📙 The Missing README           ✅

FAZ 2 ✅
  📗 A Philosophy of Software Design ✅
  📘 Head First Design Patterns     ✅
  📕 Designing Data-Intensive Apps  ✅
  📙 Unit Testing (Khorikov)        ✅
  📗 Refactoring (Fowler)          ✅  ← BURADASIN

FAZ 3 (İleri Seviye):
  📕 System Design Interview        → Sistem tasarımı pratikleri
  📘 Building Microservices          → Dağıtık mimari
  📕 Domain-Driven Design            → Karmaşık domain modelleme
  📙 Release It!                     → Production mühendisliği
  📗 Staff Engineer                  → Teknik liderlik
```

---

> **"Refactoring bir LÜKs değildir.
> Profesyonel yazılım geliştirmenin OLMAZSA OLMAZ parçasıdır.
> Nasıl bir cerrah ameliyattan sonra aletlerini TEMİZLİYORSA,
> bir yazılımcı da kodunu düzenli olarak TEMİZLEMELİDİR.
> Küçük adımlar, büyük testler, sürekli iyileşme.
> Bu bir sprint değil, bir MARATON'dur.
> Ve bu maratonda en önemli kural:
> Bulduğundan daha temiz bırak."** 🏕️
>
> — Bu rehberin özü: **"Davranışı değiştirmeden yapıyı iyileştir.
> Küçük adımlarla, testlerle korunarak, her gün biraz daha iyi."**
