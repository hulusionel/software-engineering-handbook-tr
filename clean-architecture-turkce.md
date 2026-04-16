# 🏛️ Clean Architecture — Türkçe Kapsamlı Rehber

> **"Mimari, bir sistemin ŞEKLİDİR.
> Bu şekil, sistemi geliştirme maliyetini belirler.
> İyi mimari = düşük maliyet, uzun ömür.
> Kötü mimari = artan maliyet, kısa ömür."**
> — Robert C. Martin (Uncle Bob)

Bu kitap, yazılım mimarisinin **evrensel prensiplerini** anlatır.
Hangi dili, framework'ü veya teknolojiy kullanırsan kullan — bu kurallar geçerlidir.
İşte mesaj: **"Detayları ertele, politikaları koru, bağımlılıkları içe doğru yönlendir."**

---

## 📖 İçindekiler

1. [Tasarım ve Mimari Nedir?](#1--tasarım-ve-mimari-nedir)
2. [İki Değer Hikayesi](#2--i̇ki-değer-hikayesi)
3. [Programlama Paradigmaları](#3--programlama-paradigmaları)
4. [SOLID Prensipleri](#4--solid-prensipleri)
5. [Bileşen (Component) Prensipleri](#5--bileşen-component-prensipleri)
6. [Bileşen Bağlanma (Coupling) Prensipleri](#6--bileşen-bağlanma-coupling-prensipleri)
7. [Clean Architecture Nedir?](#7--clean-architecture-nedir)
8. [Bağımlılık Kuralı](#8--bağımlılık-kuralı-dependency-rule)
9. [Humble Object Pattern](#9--humble-object-pattern)
10. [Sınırlar (Boundaries)](#10--sınırlar-boundaries)
11. [Screaming Architecture](#11--screaming-architecture)
12. [Detaylar (Database, Web, Framework)](#12--detaylar)
13. [Gerçek Dünya Uygulaması](#13--gerçek-dünya-uygulaması)
14. [Clean Architecture vs Diğer Mimariler](#14--clean-architecture-vs-diğer-mimariler)
15. [Büyük Şirketlerde Clean Architecture](#15--büyük-şirketlerde-clean-architecture)
16. [Yapay Zeka Çağında Clean Architecture](#16--yapay-zeka-çağında-clean-architecture)
17. [Son Sözler](#17--son-sözler)

---

## 1. 🏗️ Tasarım ve Mimari Nedir?

### Tasarım = Mimari (Uncle Bob'a Göre)

```
Geleneksel ayrım:
  Mimari  = Üst düzey kararlar (katmanlar, modüller, iletişim)
  Tasarım = Alt düzey kararlar (sınıflar, fonksiyonlar, değişkenler)

Uncle Bob: "Bu ayrım YAPAY ve YANILTICI."

Gerçek:
  Mimari ve tasarım aynı şeyin farklı zoom seviyelerindeki görünümleridir.

  🔭 Uzaktan bakınca → "Mimari" diyorsun
  🔬 Yakınlaşınca → "Tasarım" diyorsun
  AMA hepsi AYNI yapının parçası!

  Alt düzey kararlar üst düzeyi destekler.
  Üst düzey kararlar alt düzeyi şekillendirir.
  Birini ihmal edersen DİĞERİ de çöker!
```

### Mimarinin Amacı

```
Mimarinin amacı NE DEĞİLDİR:
  ❌ "Sistemi çalıştırmak"
  → Çoğu kötü mimari de ÇALIŞIR! Sorun bu değil.

Mimarinin GERÇEK amacı:
  ✅ "Sistemi geliştirmeyi, deploy etmeyi, işletmeyi ve
     bakımını yapmayı KOLAY ve UCUZ tutmak."

İyi mimari = Zaman geçtikçe özellik ekleme hızı DÜŞMeZ
Kötü mimari = Her özellik BİR ÖNCEKİNDEN DAHA PAHALI

                 maliyet
                    │
  Kötü mimari:      │  ╱
                    │ ╱
                    │╱     "Her sprint daha AĞIR!"
                    ├─────────────→ zaman
                    │
  İyi mimari:       │──────────
                    │          "Sürdürülebilir hız"
                    └─────────────→ zaman
```

### Davranış ve Yapı — İki Değer

Her yazılım sistemi iki tür değer sunar:

```
1. DAVRANIŞ (Behavior):
   → Sistem ne YAPAR? Gereksinimleri karşılıyor mu?
   → Stakeholder'lar bunu ister: "Sipariş alabilmeli!"

2. YAPI (Structure / Architecture):
   → Sistem ne kadar kolay DEĞİŞTİRİLEBİLİR?
   → "Software" kelimesindeki "soft" = YUMUŞAK, değiştirilebilir!
   → Yazılımın ASIL değeri bu!

Paradoks:
  Paydaşlar DAVRANIŞ ister (feature, feature, feature!)
  AMA yazılımın uzun vadeli değeri YAPI'dadır.
```

---

## 2. ⚖️ İki Değer Hikayesi

### Eisenhower Matrisi

```
Uncle Bob, Eisenhower'dan alıntı yapar:

"Önemli olan nadiren acildir. Acil olan nadiren önemlidir."

              ACİL          ACİL DEĞİL
            ┌──────────────┬──────────────┐
  ÖNEMLİ   │ 1. Yap!      │ 2. Planla    │
            │ (kriz)       │ (MİMARİ!)    │
            ├──────────────┼──────────────┤
  ÖNEMLİ   │ 3. Delege et │ 4. Eleme!    │
  DEĞİL    │ (feature?)   │ (zaman kaybı)│
            └──────────────┴──────────────┘

Yanlış olan:
  Yöneticiler: "Bu feature ACİL!" → kutu 1'e koyarlar
  AMA gerçekte bu acil ama ÖNEMLİ DEĞİL (kutu 3)

  Mimari ise ÖNEMLİ ama ACİL GÖRÜNMüyor (kutu 2)
  → Sürekli ertelenir
  → Ta ki sistem ÇÜRÜYENE kadar → artık kutu 1!

GOREVİMİZ:
  Mimari'nin ÖNEMLİ olduğunu savunmak.
  "Feature bu sprint'te lazım!" baskısına rağmen
  yapısal kaliteyi KORUMAK.

  "Geliştirici olarak SEN sistemin yapısından sorumlusun.
   Bu senin SAVAŞIN."
```

### Eğer Yapıyı İhmal Edersen...

```
Sprint 1:  Feature → 2 gün    ✅ "Çok hızlıyız!"
Sprint 5:  Feature → 1 hafta  😐 "Biraz yavaşladık"
Sprint 15: Feature → 3 hafta  😰 "Neden bu kadar yavaş?"
Sprint 30: Feature → 2 ay     🔥 "Sistemi yeniden yazalım!"

→ "Yeniden yazalım!" = mimarinin İFLASI!
→ Yeniden yazma genellikle aynı hatalara düşer. KÖTÜ DÖNGÜ!

Çözüm: Yapıya SÜREKLI yatırım yap.
  Refactoring = günlük bakım
  Clean Architecture = uzun vadeli strateji
```

---

## 3. 🔧 Programlama Paradigmaları

Uncle Bob, 3 paradigmanın mimariyle ilişkisini anlatır:

### Yapısal Programlama (Structured) 🧱

```
Dijkstra, 1968: "goto zararlıdır!"

goto OLMADAN:
  → sequence (sıralı), selection (if/else), iteration (loop)
  → Bu 3 yapı ile HER algoritma yazılabilir (Böhm-Jacopini teoremi)

Mimariyle ilişki:
  Yapısal programlama bize FALSIFIABILiTY (yanlışlanabilirlik) verdi.
  → Programı küçük, test edilebilir parçalara bölme
  → Fonksiyonel ayrıştırma (functional decomposition)
  → Dijkstra: "Testler bug'ın VARLIĞINI kanıtlar, YOKLUĞUNU değil"
  → Tıpkı bilimde: Teori yanlışLANABİLİR olmalı (Popper)

"Yapısal programlama, goto'yu YASAKLAYARAK
 doğrudan kontrol transferini DİSİPLİN altına aldı."
```

### Nesne Yönelimli Programlama (OOP) 🎯

```
OOP'nin GERÇEK gücü nedir?

Uncle Bob'a göre:
  Kapsülleme: C'de DAHA İYİYDİ! (header file = mükemmel gizleme)
              OOP aslında kapsüllemeyi ZAYIFLATTI (public/protected/private kaos!)
  Kalıtım: C'de elle yapılabilirdi ama RAHATSIZDI (struct iç içe gömme)
  Polimorfizm: C'de function pointer ile VARDI ama TEHLİKELİYDİ

  ✅ OOP'nin asıl katkısı: Polimorfizmi GÜVENLİ ve KOLAY yaptı
  ✅ Bu da DEPENDENCY INVERSION'u pratik hale getirdi!

Polimorfizm sayesinde DEPENDENCY INVERSION yapılabilir:

  ESKİ DÜNYA (polimorfizm öncesi):
    High-Level → Low-Level
    İş kuralı → Veritabanı
    Kontrol akışı === Bağımlılık yönü
    ↓ her şey aynı yöne akar ↓

  YENİ DÜNYA (polimorfizm ile):
    High-Level → [Interface] ← Low-Level
    İş kuralı → [Port] ← Veritabanı adaptörü

    Kontrol akışı:  Business → Database  (sağa doğru)
    Bağımlılık:     Business ← Database  (sola doğru, TERS!)
    → BAĞIMLILIK TERSİNE ÇEVRİLDİ!

BU Clean Architecture'ın TEMELİDİR.

"OOP, dolaylı kontrol transferini (function pointer) DİSİPLİN altına aldı."
```

### Fonksiyonel Programlama (FP) 🔄

```
Fonksiyonel programlama: "Değişkenler DEĞİŞMEZ (immutable)!"

Değişebilir (mutable) veri neden tehlikeli?
  → Race condition
  → Deadlock
  → Concurrent güncelleme sorunları

İmmutability:
  → Her değişiklik YENİ bir kopya oluşturur
  → Yan etki (side effect) yok veya kontrol altında
  → Concurrent programlama GÜVENLİ

Mimariyle ilişki:
  Event Sourcing = tüm değişiklikleri GEÇMİŞ TENSE olarak sakla
  → "Bakiye 500₺ oldu" DEĞİL
  → "100₺ yatırıldı", "200₺ yatırıldı", "50₺ çekildi", "250₺ yatırıldı"
  → Tüm olaylar IMMUTABLE → hesap durumu = olayların toplamı

"FP, atamayı (assignment) DİSİPLİN altına aldı."
```

### Özet: 3 Paradigma, 3 Disiplin

```
┌──────────────┬──────────────────────┬──────────────────────────────┐
│ Paradigma     │ Disiplin Altına Alınan │ Mimari Etkisi              │
├──────────────┼──────────────────────┼──────────────────────────────┤
│ Structured   │ goto (doğrudan atlama) │ Fonksiyonel ayrıştırma      │
│ OOP          │ Function pointer      │ Dependency Inversion!        │
│ FP           │ Assignment (atama)    │ Immutability, Event Sourcing │
└──────────────┴──────────────────────┴──────────────────────────────┘

3 paradigma 1958-1968 arasında keşfedildi.
O zamandan beri YENİ paradigma YOK.
Her paradigma bir şeyi YASAKLAR (ekleme değil, ÇIKARMA).
```

---

## 4. ⭐ SOLID Prensipleri

Uncle Bob'un (ve başkalarının) ortaya koyduğu 5 prensip. **Modül/sınıf seviyesinde** tasarım rehberi.

### S — Single Responsibility Principle (Tek Sorumluluk) 📦

```
YANLIŞ ANLAMA: "Bir sınıf tek bir şey yapmalı"
  → Bu fonksiyonlar için geçerli, sınıflar için DEĞİL!

DOĞRU ANLAM: "Bir sınıfın değişmesi için TEK BİR NEDEN olmalı."
  → Daha doğrusu: "Bir sınıf TEK BİR AKTÖRE karşı sorumlu olmalı."

Aktör = Değişiklik talep eden kişi/grup
```

```javascript
// ❌ SRP İHLALİ: 3 farklı aktör, 1 sınıf
class Employee {
  calculatePay() { ... }      // Muhasebe departmanı ister (CFO)
  reportHours() { ... }       // İK departmanı ister (COO)
  save() { ... }              // DBA / Teknik ekip ister (CTO)
}

// CFO: "Fazla mesai hesaplaması değişmeli"
// → calculatePay değişir
// → AMA reportHours da aynı helper'ı kullanıyordu → İK raporu BOZULDU! 💥

// ✅ SRP: Her aktör için ayrı sınıf
class PayCalculator {
  calculatePay(employee) { ... }  // CFO'nun sorumluluğu
}

class HourReporter {
  reportHours(employee) { ... }   // COO'nun sorumluluğu
}

class EmployeeRepository {
  save(employee) { ... }          // CTO'nun sorumluluğu
}

// Bir aktörün değişiklik talebi diğerlerini ETKİLEMEZ ✅
```

**Hikaye:** Düşün ki bir restoranda garson hem sipariş alıyor, hem yemek pişiriyor, hem de kasa yapıyor. Müşteri "menü değişsin" der → garson değiştirir → AMA kasa fiyatları da bozulur! Her işi ayrı kişiye ver. 🍽️👨‍🍳💰

### O — Open/Closed Principle (Açık/Kapalı) 🚪

```
"Yazılım varlıkları genişlemeye AÇIK, değişikliğe KAPALI olmalı."

→ Yeni davranış eklenebilmeli (AÇIK)
→ Mevcut koda DOKUNMADAN (KAPALI)

Nasıl? SOYUTLAMA + POLİMORFİZM
```

```javascript
// ❌ OCP İHLALİ: Yeni rapor türü = mevcut kodu değiştir
function generateReport(type, data) {
  if (type === 'pdf') {
    // PDF oluştur...
  } else if (type === 'excel') {
    // Excel oluştur...
  } else if (type === 'csv') {
    // CSV oluştur... (her yeni format = if ekle!)
  }
}

// ✅ OCP: Yeni format = yeni sınıf, mevcut koda DOKUNMA
class ReportGenerator {
  constructor(formatter) {
    this.formatter = formatter; // Soyutlamaya bağımlı
  }
  generate(data) {
    return this.formatter.format(data); // Polimorfizm!
  }
}

class PdfFormatter {
  format(data) { /* PDF logic */ }
}
class ExcelFormatter {
  format(data) { /* Excel logic */ }
}
// Yeni: WordFormatter → yeni sınıf yaz, ReportGenerator'a DOKUNMA! ✅
```

**Mimari düzeyde OCP:**

```
Finansal rapor sistemi:

  [Controller] → [Use Case] → [Presenter]
                    ↑
                 [Gateway]

Yeni rapor hedefi (ekran → printer)?
  → Yeni Presenter yaz
  → Use Case'e DOKUNMA!

Yeni veri kaynağı (SQL → NoSQL)?
  → Yeni Gateway yaz
  → Use Case'e DOKUNMA!

Use Case (iş kuralı) = DEĞİŞMEYEN merkez
Çevre = değiştirilebilen DETAYLAR
→ Bu Clean Architecture'ın ÖZÜ!
```

### L — Liskov Substitution Principle (Liskov Yerine Koyma) 🔄

```
Barbara Liskov, 1988:

"Alt sınıf, üst sınıfın yerine geçebilmeli.
 Kullanan kod FARK ETMEMELİ."

Basitçe: "Bir kuş uçabiliyorsa, penguen kuş OLAMAZ."
(Çünkü penguen uçamaz → kuş yerine koyamazsın)
```

```javascript
// ❌ LSP İHLALİ: Klasik Rectangle-Square problemi
class Rectangle {
  setWidth(w) { this.width = w; }
  setHeight(h) { this.height = h; }
  getArea() { return this.width * this.height; }
}

class Square extends Rectangle {
  setWidth(w) { this.width = w; this.height = w; } // İkisini birden değiştir!
  setHeight(h) { this.width = h; this.height = h; }
}

// Kullanan kod:
function testArea(rect) {
  rect.setWidth(5);
  rect.setHeight(4);
  console.assert(rect.getArea() === 20); // Rectangle: ✅ 20, Square: ❌ 16!
}
// Square, Rectangle'ın yerine GEÇEMİYOR → LSP ihlali!

// ✅ LSP: Ortak davranışı interface ile tanımla
class Shape {
  getArea() { throw new Error('Implement me'); }
}

class Rectangle extends Shape {
  constructor(w, h) { super(); this.width = w; this.height = h; }
  getArea() { return this.width * this.height; }
}

class Square extends Shape {
  constructor(side) { super(); this.side = side; }
  getArea() { return this.side * this.side; }
}
```

**Mimariyle ilişki:**

```
LSP sadece sınıflar için DEĞİL, mimari sınırlar için de geçerli!

Taxi dispatch sistemi:
  URI: /driver/{driverId}/pickupAddress/{address}

  Acme şirketi: /driver/Bob/pickupAddress/23-Elm-St
  Purplecar:    /driver/Bob/pickupAddress/23-Elm-St  → aynı format ✅
  BestDriver:   /driver/Bob/pickupAddress/23%20Elm%20St  → farklı! ❌ LSP ihlali!

  → Bir adaptör katmanı gerekir (if/else ile şirkete göre format)
  → Mimari düzeyde LSP ihlali = ek karmaşıklık
```

### I — Interface Segregation Principle (Arayüz Ayırma) ✂️

```
"İstemcileri kullanmadıkları metodlara bağımlı olmaya ZORLAMA."

→ Şişman interface yerine küçük, odaklı interface'ler
→ Her istemci SADECE ihtiyaç duyduğu metodları görsün
```

```javascript
// ❌ ISP İHLALİ: Şişman interface — bazı istemciler bazı metodları kullanmaz
class MultiFunctionPrinter {
  print() { ... }
  scan() { ... }
  fax() { ... }
  staple() { ... }
}

// Sadece yazdırmak isteyen istemci: scan(), fax(), staple() ile de uğraşmak ZORUNDA!

// ✅ ISP: Arayüzleri ayır
// printer.js
class Printer {
  print() { ... }
}

// scanner.js
class Scanner {
  scan() { ... }
}

// MultiFunctionMachine sadece ihtiyaç duyulursa COMPOSE et:
class MultiFunctionMachine {
  constructor(printer, scanner, faxer) {
    this.printer = printer;
    this.scanner = scanner;
    this.faxer = faxer;
  }
}
```

**Mimari düzeyde ISP:**

```
Sistem S → Framework F → Database D

S, F'nin sadece 3 fonksiyonunu kullanıyor.
AMA F, D'nin tamamına bağımlı.
D'de herhangi bir değişiklik → F yeniden deploy → S yeniden deploy!

Çözüm:
  S → [Küçük Interface] → F → D
  S SADECE küçük interface'i görür
  D değişse bile, küçük interface değişmediyse S ETKİLENMEZ ✅
```

### D — Dependency Inversion Principle (Bağımlılık Tersine Çevirme) 🔄

**Clean Architecture'ın EN ÖNEMLİ prensibi!**

```
"Üst düzey modüller, alt düzey modüllere BAĞIMLI OLMAMALI.
 İkisi de SOYUTLAMALARA bağımlı olmalı."

"Soyutlamalar detaylara bağımlı olmamalı.
 Detaylar soyutlamalara bağımlı olmalı."
```

```javascript
// ❌ DIP İHLALİ: İş kuralı doğrudan veritabanına bağımlı
const mysql = require('mysql'); // ← DETAY!

class OrderService {
  async createOrder(orderData) {
    const connection = mysql.createConnection({ host: 'localhost' }); // 💥 MySQL'e YAPISÇI!
    await connection.query('INSERT INTO orders ...', orderData);
    // OrderService, MySQL'i biliyor → değiştirmek İMKANSIZ
  }
}

// ✅ DIP: İş kuralı soyutlamaya bağımlı, detay soyutlamayı UYGULAR
// --- port (soyutlama) ---
class OrderRepository {
  async save(order) { throw new Error('Implement me'); }
  async findById(id) { throw new Error('Implement me'); }
}

// --- iş kuralı (üst düzey) ---
class OrderService {
  constructor(orderRepository) { // Soyutlamaya bağımlı ✅
    this.orderRepo = orderRepository;
  }
  async createOrder(orderData) {
    const order = new Order(orderData);
    await this.orderRepo.save(order); // Hangi DB? BİLMİYOR! ✅
    return order;
  }
}

// --- adapter (alt düzey detay) ---
class MySQLOrderRepository extends OrderRepository {
  async save(order) {
    await this.connection.query('INSERT INTO orders ...', order);
  }
}

class MongoOrderRepository extends OrderRepository {
  async save(order) {
    await this.collection.insertOne(order);
  }
}

// Bağımlılık yönü:
//   OrderService → OrderRepository (soyutlama) ← MySQLOrderRepository
//   İŞ KURALI → [SOYUTLAMA] ← DETAY
//   Yön TERSİNE çevrildi! 🔄
```

**Gerçek dünya analojisi:** 🔌

```
Priz standardı (interface):
  Türkiye'de priz 220V, tip F.

Cihaz (üst düzey modül):
  Laptop şarj cihazı → prize TAKILIR
  Laptop priz tipini BİLMEK ZORUNDA DEĞİL

Priz (alt düzey detay):
  Duvardaki kablo → priz STANDARDINA uyar

DEĞİŞİKLİK:
  Elektrik şirketi kablolamayı değiştirdi → Priz standardı aynı → Laptop ETKİLENMEDİ ✅
  Yeni laptop aldım → Aynı prize takılır → Altyapı ETKİLENMEDİ ✅

= DEPENDENCY INVERSION PRATİKTE!
```

### SOLID Özet Tablosu

| Prensip | Bir Cümlede | Mimari Etkisi |
|---|---|---|
| **S**RP | Tek aktör, tek sorumluluk | Modülleri aktörlere göre ayır |
| **O**CP | Genişlemeye açık, değişikliğe kapalı | Soyutlama katmanları |
| **L**SP | Yerine koyulabilirlik | Arayüz kontratlarına uy |
| **I**SP | Küçük, odaklı arayüzler | Gereksiz bağımlılıkları kes |
| **D**IP | Soyutlamaya bağlan, detaya değil | **Clean Architecture'ın TEMELİ** |

---

## 5. 📦 Bileşen (Component) Prensipleri

Sınıfları **bileşenlere (component/package/module)** nasıl gruplamalı?

### REP — Reuse/Release Equivalence Principle

```
"Yeniden kullanımın (reuse) birimi = yayınlamanın (release) birimi"

→ Bileşen olarak PAKETLENEN şey, RELease edilebilir olmalı
→ Versiyon numarası olmalı (semver: 1.2.3)
→ CHANGELOG olmalı
→ Kullanıcı ne aldığını BİLMELİ

Pratik etki:
  Bir npm paketindeki sınıflar ANLAMSALCA ilişkili olmalı.
  "auth-utils" paketi → auth ile ilgili her şey
  "random-stuff" paketi → ❌ ne olduğu belli değil
```

### CCP — Common Closure Principle (SRP'nin Bileşen Versiyonu)

```
"Aynı nedenle, aynı zamanda değişen sınıfları AYNI bileşende topla."
"Farklı nedenlerle değişen sınıfları FARKLI bileşenlere ayır."

= SRP ama sınıf yerine BILEŞEN seviyesinde.

Neden?
  → Bir değişiklik geldiğinde TEK bileşeni değiştirmek yeterli olmalı
  → 10 bileşeni aynı anda değiştirmek = SHOTGUN SURGERY!

Pratik:
  Order ile ilgili TÜM sınıflar → order-module/
  Ödeme ile ilgili TÜM sınıflar → payment-module/
  Bir ödeme değişikliği = sadece payment-module'e dokunursun ✅
```

### CRP — Common Reuse Principle (ISP'nin Bileşen Versiyonu)

```
"Birlikte kullanılmayan sınıfları AYNI bileşende tutma."

→ Bileşen A'dan sadece 1 sınıf kullanıyorsan,
  tüm A'ya bağımlısın demek!
  A'daki KULLANMADIĞIN sınıf değişirse → SEN de etkilenirsin!

Pratik:
  ❌ "utils" paketi → her şey içinde → her değişiklik herkesi etkiler
  ✅ "date-utils", "string-utils", "http-utils" → ayrı paketler
     Sadece ihtiyacın olanı al ✅
```

### Üç Prensip Arasındaki Gerilim

```
         REP ←────────→ CCP
          ↑               │
          │               │
          └───── CRP ─────┘

REP+CCP: "İlgili şeyleri bir arada tut" → BÜYÜK bileşenler
CRP:     "İlgisiz şeyleri ayır" → KÜÇÜK bileşenler
→ Bu bir DENGE! Mükemmel çözüm yok.

Projenin erken döneminde → CCP ağırlıklı (hız, kolaylık)
Proje olgunlaşınca      → CRP ağırlıklı (bağımsızlık, yeniden kullanım)
```

---

## 6. 🔗 Bileşen Bağlanma (Coupling) Prensipleri

Bileşenler arası **bağımlılık** kuralları:

### ADP — Acyclic Dependencies Principle (Döngüsüz Bağımlılık) 🔄❌

```
"Bileşen bağımlılık grafiğinde DÖNGÜ OLMAMALI."

✅ İyi:
  A → B → C → D (tek yönlü, ağaç şeklinde)

❌ Kötü:
  A → B → C → A  (DÖNGÜ!)
  "A değişti" → B'yi tekrar build et → C'yi tekrar build et → A'yı tekrar build et → ∞

Döngüyü kırma yolları:
  1. Dependency Inversion: A → [Interface] ← C
  2. Yeni bileşen çıkar: A → X ← C (ortak parçaları X'e al)
```

### SDP — Stable Dependencies Principle (Kararlı Bağımlılık) ⚓

```
"Bağımlılıklar KARARLI olan yöne doğru olmalı."

Kararlılık (Stability):
  = Değiştirmesi ZOR olan → kararlı
  = Birçok şey BANA bağımlı → değiştirmem zor → kararlıyım

  Instability = (çıkan bağımlılık) / (giren + çıkan bağımlılık)
  I = 0 → çok kararlı (hiç dışarıya bağımlı değil, ama çoğu şey BANA bağımlı)
  I = 1 → çok kararsız (hiçbir şey bana bağımlı değil, ama ben çoğu şeye bağımlıyım)

Kural:
  Kararsız bileşen → Kararlı bileşene bağımlı olmalı ✅
  Kararlı bileşen → Kararsız bileşene bağımlı olmamalı ❌

Neden?
  Kararlı bir bileşen kararsız bir şeye bağımlıysa,
  kararsız bileşen DEĞİŞTİĞİNDE kararlı olan da etkilenir!
  → Kararlılık KAYBOLUR!
```

### SAP — Stable Abstractions Principle (Kararlı Soyutlamalar) 🎯

```
"Kararlı bir bileşen, soyut da olmalı."

Neden?
  Kararlı = değiştirmesi zor
  AMA değişikliğe KAPALI olursa esnek olamaz!
  Çözüm: SOYUT yap → soyutlama genişlemeye AÇIK (OCP!)

  Kararlı + Somut = 💀 "Zone of Pain" (değiştirilemez AMA değişmesi gereken)
  Kararsız + Soyut = 🤷 "Zone of Uselessness" (hiç kullanılmayan soyutlama)
  Kararlı + Soyut = ✅ İDEAL (interface'ler, abstract sınıflar)
  Kararsız + Somut = ✅ İDEAL (detay implementasyonları)

Ana Dizi (Main Sequence):
  ┌──────────┐
  │ Soyut    │  ✅ Kararlı + Soyut
  │          │     (interfaces)
  │          │
  │   Ana    │  ← Dengeli bileşenler
  │  Dizi    │
  │          │
  │          │  ✅ Kararsız + Somut
  │ Somut    │     (implementasyonlar)
  └──────────┘
  Kararlı ←→ Kararsız

  "Ana diziye yakın ol, köşelerden uzak dur!"
```

---

## 7. 🎯 Clean Architecture Nedir?

Uncle Bob'un tüm mimari bilgisinin **ÖZETİ:**

### Konsantrik Daireler 🎯

```
            ╔══════════════════════════════════════════╗
            ║        Frameworks & Drivers              ║
            ║   ╔══════════════════════════════╗       ║
            ║   ║    Interface Adapters         ║       ║
            ║   ║   ╔══════════════════╗       ║       ║
            ║   ║   ║  Application     ║       ║       ║
            ║   ║   ║  Business Rules  ║       ║       ║
            ║   ║   ║  ╔══════════╗   ║       ║       ║
            ║   ║   ║  ║Enterprise║   ║       ║       ║
            ║   ║   ║  ║Business  ║   ║       ║       ║
            ║   ║   ║  ║Rules     ║   ║       ║       ║
            ║   ║   ║  ║(Entities)║   ║       ║       ║
            ║   ║   ║  ╚══════════╝   ║       ║       ║
            ║   ║   ╚══════════════════╝       ║       ║
            ║   ╚══════════════════════════════╝       ║
            ╚══════════════════════════════════════════╝

İÇTEN DIŞA DOĞRU:

1. 🟡 ENTITIES (Enterprise Business Rules)
   → Domain nesneleri, iş kurallarının en saf hali
   → Hiçbir şeye bağımlı DEĞİL

2. 🟠 USE CASES (Application Business Rules)
   → "Sipariş oluştur", "Kullanıcı giriş yap"
   → Entity'leri KULLANAN uygulama akışları
   → SADECE entity'lere bağımlı

3. 🔵 INTERFACE ADAPTERS
   → Controller, Presenter, Gateway
   → Dış dünya formatı ↔ İç format dönüşümü
   → Use case'lere bağımlı

4. 🟣 FRAMEWORKS & DRIVERS
   → Express, React, PostgreSQL, Redis, RabbitMQ
   → EN DIŞ katman, EN AZ kod
   → Her şeye bağımlı olabilir AMA hiçbir şey BUNA bağımlı değil
```

### Her Katman Ne İçerir?

```javascript
// ==========================================
// 🟡 KATMAN 1: ENTITIES (Domain)
// ==========================================
// Hiçbir framework, kütüphane, altyapı bilmez!
// Saf JavaScript/TypeScript sınıfları.

class Order {
  #items = [];
  #status = 'draft';

  addItem(product, quantity) {
    if (this.#status !== 'draft') {
      throw new Error('Sadece taslak siparişe ürün eklenebilir');
    }
    if (quantity <= 0) {
      throw new Error('Miktar pozitif olmalı');
    }
    this.#items.push({ product, quantity, price: product.price * quantity });
  }

  get total() {
    return this.#items.reduce((sum, item) => sum + item.price, 0);
  }

  confirm() {
    if (this.#items.length === 0) {
      throw new Error('Boş sipariş onaylanamaz');
    }
    this.#status = 'confirmed';
  }
}

// Bu sınıf:
// ❌ Express bilmez
// ❌ PostgreSQL bilmez
// ❌ Redis bilmez
// ✅ Sadece İŞ KURALLARINI bilir

// ==========================================
// 🟠 KATMAN 2: USE CASES
// ==========================================
// Entity'leri kullanarak uygulama akışını yönetir.
// Soyut port'lara (interface) bağımlıdır.

class CreateOrderUseCase {
  constructor({ orderRepository, productRepository, eventPublisher }) {
    this.orderRepo = orderRepository;       // SOYUTLAMA (port)
    this.productRepo = productRepository;   // SOYUTLAMA (port)
    this.eventPublisher = eventPublisher;    // SOYUTLAMA (port)
  }

  async execute({ userId, items }) {
    const order = new Order(userId);       // Entity kullan

    for (const { productId, quantity } of items) {
      const product = await this.productRepo.findById(productId);
      if (!product) throw new Error(`Ürün bulunamadı: ${productId}`);
      order.addItem(product, quantity);     // İş kuralı entity'de!
    }

    order.confirm();                        // İş kuralı entity'de!
    await this.orderRepo.save(order);
    await this.eventPublisher.publish('order.created', { orderId: order.id });

    return order;
  }
}

// Bu sınıf:
// ❌ Express bilmez (HTTP? ne HTTP?)
// ❌ PostgreSQL bilmez (SQL? ne SQL?)
// ❌ RabbitMQ bilmez
// ✅ Sadece PORT'ları bilir (orderRepository, eventPublisher)

// ==========================================
// 🔵 KATMAN 3: INTERFACE ADAPTERS
// ==========================================
// Dış dünya ile iç dünya arasında DÖNÜŞÜM yapar.

// --- Controller (HTTP → Use Case) ---
class OrderController {
  constructor(createOrderUseCase) {
    this.createOrder = createOrderUseCase;
  }

  async handleCreateOrder(req, res) {
    try {
      const { userId, items } = req.body;                // HTTP formatı → iç format
      const order = await this.createOrder.execute({ userId, items });
      res.status(201).json({                             // İç format → HTTP formatı
        id: order.id,
        total: order.total,
        status: order.status,
      });
    } catch (error) {
      res.status(400).json({ error: error.message });
    }
  }
}

// --- Repository (Use Case Port → Database) ---
class PostgresOrderRepository {
  constructor(pool) {
    this.pool = pool;
  }

  async save(order) {
    await this.pool.query(
      'INSERT INTO orders (id, user_id, total, status) VALUES ($1, $2, $3, $4)',
      [order.id, order.userId, order.total, order.status]
    );
    // SQL detayı BURADA, Use Case'de DEĞİL!
  }

  async findById(id) {
    const { rows } = await this.pool.query('SELECT * FROM orders WHERE id = $1', [id]);
    return rows[0] ? this.#toDomain(rows[0]) : null;
  }

  #toDomain(row) {
    // DB formatı → Entity formatı dönüşümü
    return new Order({ id: row.id, userId: row.user_id /* ... */ });
  }
}

// --- Event Publisher ---
class RabbitMQEventPublisher {
  async publish(eventName, data) {
    await this.channel.publish('orders', eventName, Buffer.from(JSON.stringify(data)));
    // RabbitMQ detayı BURADA!
  }
}

// ==========================================
// 🟣 KATMAN 4: FRAMEWORKS & DRIVERS
// ==========================================
// Minimum "yapıştırıcı" (glue) kod.

// --- Express setup (main/composition root) ---
const express = require('express');
const { Pool } = require('pg');

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

// Bağımlılıkları OLUŞTUR ve ENJEKTE ET:
const orderRepo = new PostgresOrderRepository(pool);
const productRepo = new PostgresProductRepository(pool);
const eventPublisher = new RabbitMQEventPublisher(channel);
const createOrderUseCase = new CreateOrderUseCase({ orderRepo, productRepo, eventPublisher });
const orderController = new OrderController(createOrderUseCase);

// Route'ları bağla:
const app = express();
app.post('/orders', (req, res) => orderController.handleCreateOrder(req, res));

// Bu dosya:
// → TÜM bağımlılıkları bilir (çünkü oluşturuyor)
// → AMA en AZ mantık içerir (sadece kabloları bağlar)
// → "Composition Root" veya "Main Component"
```

---

## 8. 👑 Bağımlılık Kuralı (Dependency Rule)

**Clean Architecture'ın TEK ve EN ÖNEMLİ kuralı:**

```
╔═══════════════════════════════════════════════════════╗
║  Kaynak kod bağımlılıkları HER ZAMAN                 ║
║  İÇE DOĞRU olmalıdır.                                ║
║                                                       ║
║  Dış katman → İç katmana bağımlı olabilir ✅          ║
║  İç katman → Dış katmana bağımlı OLAMAZ ❌            ║
║                                                       ║
║  İç katman, dış katmanın VARLIĞINDAN BİLE             ║
║  HABERDAR OLMAMALI!                                   ║
╚═══════════════════════════════════════════════════════╝

"İç katman = POLİTİKA (iş kuralları)"
"Dış katman = DETAY (framework, DB, UI)"

Politika detaylara bağımlı OLMAMALI.
Detaylar politikaya bağımlı OLMALI.
```

### Katmanlar Arası Veri Geçişi

```
HTTP Request → Controller → Use Case → Entity → Use Case → Controller → HTTP Response

AMA!
Her katman geçişinde VERİ FORMATI değişmeli:

  HTTP Request body (JSON)
      ↓ parse
  Input DTO (CreateOrderInput)
      ↓ use case
  Entity (Order)
      ↓ use case dönüşü
  Output DTO (CreateOrderOutput)
      ↓ serialize
  HTTP Response body (JSON)

NEDEN?
  → Entity'yi doğrudan HTTP response olarak dönme!
  → Entity değişirse API da değişir → tight coupling!
  → DTO'lar katmanları AYIRIR (decoupling)
```

```javascript
// ❌ KÖTÜ: Entity doğrudan response olarak dönüyor
app.post('/orders', async (req, res) => {
  const order = await createOrder.execute(req.body);
  res.json(order); // Entity'nin TÜM iç alanları dışarıya sızıyor! 💥
});

// ✅ İYİ: DTO ile dönüşüm
app.post('/orders', async (req, res) => {
  const input = { userId: req.body.userId, items: req.body.items }; // Input DTO
  const order = await createOrder.execute(input);
  res.json({  // Output DTO — sadece dışarının görmesi gerekenleri
    id: order.id,
    total: order.total,
    createdAt: order.createdAt,
  });
});
```

---

## 9. 🙇 Humble Object Pattern

Zor test edilen şeyleri kolay test edilen şeylerden **AYIR.**

```
Sorun:
  UI, veritabanı, ağ bağlantısı → test etmesi ZOR
  İş mantığı → test etmesi KOLAY

Çözüm:
  ZOR kısımdan mantığı ÇIKAR,
  ZOR kısım "humble" (alçakgönüllü, aptal) kalsın:
  sadece veriyi ilet, karar VERME!

Örnek: Presenter Pattern

  ❌ KÖTÜ: View kararlar veriyor
  View: "Eğer bakiye negatifse kırmızı yap ve (xxx) formatında göster"
  → View'ı test etmek ZOR (UI render etmen lazım)

  ✅ İYİ: Presenter karar veriyor, View sadece gösteriyor
  Presenter: {
    balance: "-₺1,500",
    balanceColor: "red",
    showWarning: true,
    warningMessage: "Bakiyeniz ekside!"
  }
  View: "Presenter ne derse onu göster" (test etmeye GEREK YOK, aptal!)
  Presenter: test etmesi KOLAY (saf fonksiyon, UI yok)
```

```javascript
// Presenter (kolay test edilir — saf fonksiyon)
function presentOrder(order) {
  return {
    id: order.id,
    totalFormatted: `₺${order.total.toLocaleString('tr-TR')}`,
    statusLabel: order.status === 'confirmed' ? '✅ Onaylandı' : '⏳ Bekliyor',
    statusColor: order.status === 'confirmed' ? 'green' : 'orange',
    itemCount: `${order.items.length} ürün`,
  };
}

// Test (saf fonksiyon, mock yok, UI yok)
test('confirmed order shows green', () => {
  const viewModel = presentOrder({ id: 1, total: 1500, status: 'confirmed', items: [1, 2] });
  expect(viewModel.statusColor).toBe('green');
  expect(viewModel.totalFormatted).toBe('₺1.500');
});

// View (humble — sadece göster, test etmeye gerek yok)
function OrderView({ order }) {
  const vm = presentOrder(order);
  return `<div style="color: ${vm.statusColor}">${vm.statusLabel} — ${vm.totalFormatted}</div>`;
}
```

**Humble Object örnekleri mimaride:**

```
Database Gateway:
  Humble = SQL sorgularını çalıştıran kısım (test etmesi zor)
  Akıllı = Hangi sorguyu çalıştıracağına karar veren kısım (Use Case)

Service Boundary:
  Humble = HTTP request/response parse eden kısım (Controller)
  Akıllı = İş kurallarını çalıştıran kısım (Use Case)

Event Listener:
  Humble = Event'i alıp parse eden kısım
  Akıllı = Event'e nasıl tepki vereceğine karar veren kısım (Handler)
```

---

## 10. 🧱 Sınırlar (Boundaries)

### Sınır Nedir?

```
Sınır = İki bileşen/katman arasındaki AYRIM çizgisi.

Sınır neden önemli?
  → DETAYLARI iş kurallarından AYIRIR
  → Değişikliğin yayılmasını ENGELLER
  → "Kararları ertelemeyi" mümkün kılar

Uncle Bob: "İyi mimari, KARARLARI ERTELEMENİ sağlar."
  → Veritabanını ilk gün seçmek ZORUNDA DEĞİLSİN
  → Web framework'ü ilk gün seçmek ZORUNDA DEĞİLSİN
  → Bunlar DETAY. Detaylar sonra belirlenir.
```

### Sınır Türleri

```
En basitinden en karmaşığına:

1. KAYNAK DOSYASI SEVİYESİ
   → import/require ile çizilir
   → Aynı process, aynı adres alanı
   → Maliyet: ÇOK DÜŞÜK
   → Örnek: src/domain/ ↔ src/infra/

2. BİLEŞEN (COMPONENT) SEVİYESİ
   → Ayrı npm paketleri / JAR'lar
   → Aynı process, farklı deploy birimleri
   → Maliyet: DÜŞÜK
   → Örnek: @company/order-domain ↔ @company/order-infra

3. PROCESS SEVİYESİ
   → Farklı process'ler, aynı makine
   → IPC, socket, pipe ile iletişim
   → Maliyet: ORTA

4. SERVİS SEVİYESİ
   → Farklı makineler, ağ üzerinden
   → HTTP, gRPC, message queue
   → Maliyet: YÜKSEK (latency, failure, serialization)
   → Microservices!

KURAL:
  İhtiyacından FAZLA sınır çizme!
  Monolith'le başla, sınırları MODÜL düzeyinde çiz.
  Microservice'e GERÇEKTEN ihtiyaç duyduğunda geç.

  "Sınırlar zaman içinde EVRİLMELİ, önceden TAHMİN EDİLMEMELİ."
```

### Sınır Çizerken DIP Nasıl Çalışır?

```
     Business Rules              Database
    ┌─────────────┐            ┌───────────┐
    │             │            │           │
    │ Use Case   ─┼── uses ──→│ Interface │ ← SOYUTLAMA
    │             │            │ (Port)    │
    └─────────────┘            └─────┬─────┘
                                     │ implements
                                ┌────┴────┐
                                │ Postgres │ ← DETAY
                                │ Adapter  │
                                └──────────┘

  Bağımlılık yönü: Use Case → Interface ← Adapter
  İş kuralı PostgreSQL'i BİLMEZ. Interface bilir mi? HAYIR!
  Interface sadece "save(order)" der, NASIL yapıldığını bilmez.
  → Adapter değişebilir (Postgres → Mongo → file → in-memory)
  → Use Case DEĞİŞMEZ. ✅
```

---

## 11. 🏠 Screaming Architecture

### Mimari Ne Hakkında BAĞIRMALI?

```
Bir binanın planına baktığında NE gördüğünü anlarsın:
  → "Bu bir kütüphane" (bunu raf düzeni, okuma odası gösterir)
  → "Bu bir hastane" (bunu muayene odaları gösterir)
  → "Bu bir ev" (bunu yatak odası, mutfak gösterir)

Peki yazılımın klasör yapısına baktığında?

  ❌ KÖTÜ (Framework bağırıyor):
    src/
      controllers/
      models/
      views/
      routes/
      middleware/
      helpers/
      utils/

  → "Bu bir Express.js projesi!" (veya Rails, Spring, vb.)
  → Ama NE YAPIYOR? Sipariş mi? Banka mı? Oyun mu? BELLİ DEĞİL!

  ✅ İYİ (Domain bağırıyor):
    src/
      orders/
        create-order.use-case.js
        order.entity.js
        order.repository.port.js
      payments/
        process-payment.use-case.js
        payment.entity.js
      shipping/
        calculate-shipping.use-case.js
        shipment.entity.js
      shared/
        ...

  → "Bu bir E-TİCARET sistemi!" 🛒
  → Framework ne? Önemli DEĞİL. DETAY.
```

```javascript
// ❌ Framework-First yapı:
// src/controllers/orderController.js
// src/models/Order.js
// src/routes/orderRoutes.js
// → "Express projesi" bağırıyor, domain kayıp

// ✅ Domain-First yapı:
// src/orders/domain/order.entity.js
// src/orders/application/create-order.use-case.js
// src/orders/infrastructure/postgres-order.repository.js
// src/orders/presentation/order.controller.js
// → "Sipariş yönetimi" bağırıyor, framework gizli ✅
```

> **Uncle Bob:** "Mimarinize baktığınızda 'Rails!' veya 'Express!' değil, 'Sağlık Sistemi!' veya 'Muhasebe Sistemi!' görmelisiniz."

---

## 12. 🔩 Detaylar

### Veritabanı Bir DETAYDIR 🗄️

```
"Veritabanı mimari DEĞİLDİR. Bir DETAYDIR."

Şok edici mi? Düşün:

  İş kuralı: "Sipariş 1000₺'yi geçerse %5 indirim uygula"
  → Bu kural PostgreSQL'e mi bağlı? MongoDB'ye mi? Redis'e mi?
  → HAYIR! Bu kural veritabanından BAĞIMSIZ.

  Veritabanı sadece VERİYİ NASIL SAKLADIĞINDIR.
  → SQL, NoSQL, file system, in-memory... hepsi DETAY!

  İş kuralların veritabanını bilmemeli:
    Order.applyDiscount() → SQL yazmaz!
    OrderRepository.save() → SQL yazar ama bu DETAY katmanında!

Pratik sonuç:
  Test'te: In-memory repository kullan (PostgreSQL'i ayağa kaldırma!)
  Dev'de: SQLite veya Docker Postgres
  Prod'da: Managed PostgreSQL
  → Use Case kodu hiç DEĞİŞMEZ!
```

### Web Bir DETAYDIR 🌐

```
"Web bir delivery mechanism'dir. Mimari DEĞİLDİR."

İş kuralları WEB'i bilmemeli:
  → HTTP status kodları? Use Case'in işi DEĞİL.
  → JSON formatting? Use Case'in işi DEĞİL.
  → Cookie, session, header? Use Case'in işi DEĞİL.

Bugün WEB, yarın:
  → CLI tool
  → gRPC servisi
  → Cron job
  → Message queue consumer
  → Hepsi AYNI Use Case'i kullanır! ✅

Bunu mümkün kılan: Use Case'in HTTP'den HABERDAR OLMAMASI.
```

```javascript
// Use Case — delivery mechanism bilmez
class CreateOrderUseCase {
  async execute(input) {
    // HTTP? gRPC? CLI? BİLMİYOR! Sadece input/output.
    const order = new Order(input.userId);
    // ...
    return { orderId: order.id, total: order.total };
  }
}

// HTTP adapter
app.post('/orders', async (req, res) => {
  const result = await createOrder.execute(req.body);
  res.status(201).json(result); // HTTP detayı BURADA
});

// CLI adapter
program.command('create-order').action(async (options) => {
  const result = await createOrder.execute(options);
  console.log(`Sipariş oluşturuldu: ${result.orderId}`); // CLI detayı BURADA
});

// gRPC adapter
grpcServer.addService(OrderService, {
  createOrder: async (call, callback) => {
    const result = await createOrder.execute(call.request);
    callback(null, result); // gRPC detayı BURADA
  }
});

// AYNI Use Case, 3 FARKLI delivery mechanism ✅
```

### Framework Bir DETAYDIR 📦

```
"Framework'ler çok kullanışlıdır AMA evlenmek zorunda DEĞİLSİN."

Framework'le evlenmek:
  ❌ Tüm kodu framework convention'larına göre yazma
  ❌ Entity'leri framework decorator/annotation'larıyla donatma
  ❌ Framework'ün kalıtım yapısını domain'e taşıma

Framework'ü detay olarak tutmak:
  ✅ Framework'ü EN DIŞ katmanda kullan
  ✅ İş kurallarını framework'ten BAĞIMSIZ yaz
  ✅ Framework değişirse (Express → Fastify) sadece dış katmanı değiştir

Analoji: 🏠🪟
  Framework = pencere
  İş kuralı = ev

  Pencere değiştiğinde EVİ YIKMA!
  Pencereyi DEĞİŞTİR, ev aynı kalsın.

  AMA eğer evin duvarları pencereye BAĞIMLIYSA →
  pencere değişince duvar da çöker! 💥
  → İşte framework'e sıkı bağlanmanın maliyeti!
```

```javascript
// ❌ KÖTÜ: Entity framework'e bağımlı
// (Express/Mongoose tarzı — entity ve DB modeli iç içe)
const mongoose = require('mongoose'); // Framework detayı!

const orderSchema = new mongoose.Schema({
  userId: String,
  items: [{ productId: String, quantity: Number }],
  total: Number,
});

orderSchema.methods.applyDiscount = function () {
  if (this.total > 1000) this.total *= 0.95;
};

const Order = mongoose.model('Order', orderSchema);
// → İş kuralı (applyDiscount) Mongoose'a BAĞIMLI!
// → Mongoose değişirse iş kuralı da DEĞİŞİR!

// ✅ İYİ: Entity framework'ten bağımsız
// domain/order.entity.js — SIFIR import!
class Order {
  #total;
  constructor({ userId, items }) {
    this.userId = userId;
    this.items = items;
    this.#total = items.reduce((sum, i) => sum + i.price * i.quantity, 0);
  }

  applyDiscount() {
    if (this.#total > 1000) this.#total *= 0.95;
  }

  get total() { return this.#total; }
}

// infrastructure/mongoose-order.repository.js — Framework BURADA
const mongoose = require('mongoose');
const orderSchema = new mongoose.Schema({ /* ... */ });
const OrderModel = mongoose.model('Order', orderSchema);

class MongooseOrderRepository {
  async save(order) {
    await OrderModel.create({
      userId: order.userId,
      items: order.items,
      total: order.total,
    });
  }
}
// → Mongoose değişirse sadece BU dosya değişir, entity ETKİLENMEZ ✅
```

---

## 13. 🏗️ Gerçek Dünya Uygulaması

### Klasör Yapısı (Node.js Örneği)

```
src/
  ├── domain/                      🟡 ENTITIES
  │   ├── order/
  │   │   ├── order.entity.js         İş kuralları
  │   │   ├── order-item.value-object.js
  │   │   └── order.errors.js         Domain hataları
  │   └── user/
  │       └── user.entity.js
  │
  ├── application/                 🟠 USE CASES
  │   ├── order/
  │   │   ├── create-order.use-case.js
  │   │   ├── cancel-order.use-case.js
  │   │   └── ports/                  SOYUTLAMALAR (interface'ler)
  │   │       ├── order.repository.port.js
  │   │       └── payment.gateway.port.js
  │   └── user/
  │       └── register-user.use-case.js
  │
  ├── infrastructure/              🔵 ADAPTERS + 🟣 FRAMEWORKS
  │   ├── persistence/
  │   │   ├── postgres-order.repository.js
  │   │   └── postgres-user.repository.js
  │   ├── external-services/
  │   │   ├── stripe-payment.gateway.js
  │   │   └── sendgrid-email.service.js
  │   ├── messaging/
  │   │   └── rabbitmq-event.publisher.js
  │   └── http/
  │       ├── server.js               Express setup
  │       ├── routes/
  │       │   ├── order.routes.js
  │       │   └── user.routes.js
  │       └── controllers/
  │           ├── order.controller.js
  │           └── user.controller.js
  │
  └── main.js                     🟣 COMPOSITION ROOT
                                    Tüm bağımlılıkları oluştur ve bağla
```

### Composition Root (main.js)

```javascript
// main.js — HER ŞEYİ bilir, AMA hiçbir şey BUNU bilmez
const express = require('express');
const { Pool } = require('pg');

// Infrastructure
const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const orderRepo = new PostgresOrderRepository(pool);
const userRepo = new PostgresUserRepository(pool);
const paymentGateway = new StripePaymentGateway(process.env.STRIPE_KEY);
const emailService = new SendGridEmailService(process.env.SENDGRID_KEY);
const eventPublisher = new RabbitMQEventPublisher(process.env.RABBITMQ_URL);

// Use Cases
const createOrder = new CreateOrderUseCase({
  orderRepository: orderRepo,
  paymentGateway,
  eventPublisher,
});
const cancelOrder = new CancelOrderUseCase({ orderRepository: orderRepo });
const registerUser = new RegisterUserUseCase({
  userRepository: userRepo,
  emailService,
});

// Controllers
const orderController = new OrderController({ createOrder, cancelOrder });
const userController = new UserController({ registerUser });

// Express (Framework — EN DIŞ)
const app = express();
app.use(express.json());
app.post('/orders', (req, res) => orderController.create(req, res));
app.delete('/orders/:id', (req, res) => orderController.cancel(req, res));
app.post('/users', (req, res) => userController.register(req, res));

app.listen(3000);
```

### Test Stratejisi

```javascript
// ============================================
// Use Case Testi — Hızlı, izole, güvenilir
// ============================================
// Infrastructure yerine IN-MEMORY implementasyon kullan!

class InMemoryOrderRepository {
  #orders = new Map();

  async save(order) {
    this.#orders.set(order.id, order);
  }

  async findById(id) {
    return this.#orders.get(id) || null;
  }

  // Test helper
  getAll() { return [...this.#orders.values()]; }
}

class FakePaymentGateway {
  #shouldFail = false;

  simulateFailure() { this.#shouldFail = true; }

  async charge(amount) {
    if (this.#shouldFail) throw new Error('Payment failed');
    return { transactionId: 'fake-tx-123' };
  }
}

class SpyEventPublisher {
  #events = [];

  async publish(eventName, data) {
    this.#events.push({ eventName, data });
  }

  getPublishedEvents() { return this.#events; }
}

// TEST
describe('CreateOrderUseCase', () => {
  let useCase;
  let orderRepo;
  let paymentGateway;
  let eventPublisher;

  beforeEach(() => {
    orderRepo = new InMemoryOrderRepository();
    paymentGateway = new FakePaymentGateway();
    eventPublisher = new SpyEventPublisher();

    useCase = new CreateOrderUseCase({
      orderRepository: orderRepo,
      paymentGateway,
      eventPublisher,
    });
  });

  test('sipariş oluşturulduğunda event yayınlanır', async () => {
    // Arrange
    const input = { userId: 'user-1', items: [{ productId: 'p1', quantity: 2 }] };

    // Act
    const result = await useCase.execute(input);

    // Assert
    expect(result.orderId).toBeDefined();
    const events = eventPublisher.getPublishedEvents();
    expect(events).toHaveLength(1);
    expect(events[0].eventName).toBe('order.created');
  });

  test('ödeme başarısız olursa sipariş oluşturulmaz', async () => {
    paymentGateway.simulateFailure();

    const input = { userId: 'user-1', items: [{ productId: 'p1', quantity: 1 }] };

    await expect(useCase.execute(input)).rejects.toThrow('Payment failed');
    expect(orderRepo.getAll()).toHaveLength(0); // Sipariş kaydedilmedi!
  });
});

// → PostgreSQL yok! RabbitMQ yok! Network yok!
// → Milisaniyede koşar! ⚡
// → Güvenilir! (Dış bağımlılık yok)
```

---

## 14. 🔬 Clean Architecture vs Diğer Mimariler

### Benzer Mimariler Ailesi

```
Clean Architecture aslında TEK değil, bir AİLENİN parçası:

1. Hexagonal Architecture (Ports & Adapters) — Alistair Cockburn (2005)
   → "Uygulama bir altıgen. Port'lar ve adapter'lar ile dış dünyaya bağlanır."

2. Onion Architecture — Jeffrey Palermo (2008)
   → "Domain merkezde, altyapı dışarıda. Soğan gibi katmanlar."

3. Clean Architecture — Robert C. Martin (2012)
   → "Konsantrik daireler, bağımlılık kuralı, SOLID."

HEPSİ AYNI ŞEYİ SÖYLÜYOR:
  → İş kuralları MERKEZde
  → Altyapı DIŞARIDA
  → Bağımlılıklar İÇE DOĞRU
  → Detaylar ERTELENEBİLİR
```

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Hexagonal:    Port ←→ Adapter ←→ Dış Dünya             │
│                                                         │
│  Onion:        Domain → App → Infra (katmanlar)         │
│                                                         │
│  Clean:        Entity → UseCase → Adapter → Framework   │
│                                                         │
│  FARK: Terminoloji ve görselleştirme                    │
│  ORTAK: Bağımlılık yönü, domain izolasyonu              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Clean Architecture Ne Zaman FAZLA?

```
✅ KULLAN:
  → Uzun ömürlü, büyüyen projeler
  → Birden fazla delivery mechanism (API + CLI + Queue)
  → Karmaşık domain mantığı
  → Ekip > 3 kişi
  → Veritabanı/framework değişebilir

❌ FAZLA OLUR:
  → Prototip / MVP / hackathon
  → CRUD-ağırlıklı, az mantık
  → Tek delivery mechanism, tek DB, hiç değişmeyecek
  → Solo geliştirici, kısa ömürlü proje

PRAGMATIK YAKLAŞIM:
  → MVC ile başla, domain mantığı büyüdükçe katmanları AYIR
  → "Yeterli" mimari uygula, "mükemmel" mimari arama
  → Refactoring ile EVRİL (büyük patlama yerine kademeli geçiş)
```

### Kritik Bakış: Uncle Bob'a İtirazlar

```
Uncle Bob'un bazı iddiaları tartışmalıdır:

1. "Veritabanı bir detaydır"
   İtiraz: ORM/SQL/NoSQL seçimi domain modellemeyi ETKİLER.
   Cevap: Detay olma ≠ önemsiz. Detay = değiştirilebilir olmalı.

2. "Framework'lerle evlenme"
   İtiraz: Spring/Express projenin HER YERİNDE.
   Cevap: İş kurallarını framework'ten izole et.
          Controller'lar framework'le evli olabilir, Use Case'ler HAYIR.

3. "Çok fazla soyutlama"
   İtiraz: Basit CRUD için 4 katman gereksiz.
   Cevap: Doğru! Pragmatik ol. Katman sayısını domain karmaşıklığına göre ayarla.

4. "Test öncelikli OOP"
   İtiraz: Fonksiyonel dillerde farklı yaklaşımlar var.
   Cevap: İlkeler (bağımlılık yönü, izolasyon) paradigmadan bağımsız geçerli.
```

---

## 15. � Büyük Şirketlerde Clean Architecture

### Netflix — Hexagonal Architecture

```
Netflix backend servisleri Hexagonal Architecture kullanır:
  → Domain layer: İş kuralları (öneri algoritması, içerik yönetimi)
  → Port/Adapter: gRPC, REST, Kafka consumer → hepsi ADAPTER
  → Domain ASLA framework'e bağımlı değil

Sonuç: Netflix veritabanını Cassandra'dan CockroachDB'ye 
       geçirmiş — domain katmanında TEK SATIR değişmemiş.
       Clean Architecture'ın GÜCÜ bu.
```

### Amazon — Strict Dependency Rule

```
Amazon'da "dependency rule" SERTTİR:
  → İç katman dış katmanı IMPORT edemez
  → Bunu static analysis tool'ları ile ENFORCElar
  → ArchUnit (Java) veya eslint kuralları ile

"İki pizza kuralı" + Clean Architecture:
  → Her microservice küçük ekip, kendi domain'i
  → Ama İÇ yapı da temiz olmalı
  → Microservice ≠ spaghetti kodun küçük versiyonu
```

### Uber — Domain Layer Enforcement

```
Uber'in yaklaşımı Uncle Bob'a çok yakın:
  → "Domain entities hiçbir framework import'u yapamaz"
  → Code review'da #1 kural
  → Neden? Framework değiştiğinde (Express→Fastify gibi)
    domain kodunu DEĞİŞTİRMEK zorunda kalmamak

Getir'de aynı prensip:
  → Service katmanı Fastify bilmesin
  → Controller → Service → Repository
  → Repository interface kullan, implementasyonu dışarıda tut
```

---

## 16. 🤖 Yapay Zeka Çağında Clean Architecture

### AI Kodu ve Mimari Katmanlar

```
AI kodlama araçları (Copilot, Cursor) genelde:
  ❌ Her şeyi TEK dosyaya koyar
  ❌ Framework kodu ile iş kuralını KARIŞTIR
  ❌ Veritabanı sorgusunu controller'a gömer
  
Bu, Uncle Bob'un kitabındaki HER kuralı ihlal eder!

Çözüm: AI'a mimari sınırları SÖYLE:
```

### Mimari-Uyumlu AI Promptları

```
KATMANLI MİMARİ:
  "Bu feature'ı Clean Architecture prensiplerine göre implemente et.
   4 katman kullan:
   - Entity (saf iş kuralları, hiç import yok)
   - Use Case (uygulama iş kuralları, entity'lere bağımlı)
   - Interface Adapter (controller, presenter, gateway)
   - Framework/Driver (Express route, DB query)
   
   Dependency Rule: İç katmanlar dışı BİLMEMELİ.
   Framework import'u sadece en dış katmanda olsun."

SOLID KONTROL:
  "Bu kodu SOLID prensiplerine göre değerlendir:
   - SRP: Bu sınıf kaç farklı AKTÖRE hizmet veriyor?
   - OCP: Yeni davranış eklemek için mevcut kodu değiştirmek gerekiyor mu?
   - LSP: Alt sınıflar üst sınıfın yerine güvenle geçebilir mi?
   - ISP: İstemciler kullanmadıkları metotlara mı bağımlı?
   - DIP: Somut sınıf mı, soyut arayüz mü kullanılıyor?"

BOUNDARY ANALİZİ:
  "Bu projede mimari sınırları analiz et:
   - Hangi modüller birbirine DOĞRUDAN bağımlı?
   - Bağımlılık yönü DOĞRU mu? (dıştan içe mi akıyor?)
   - Hangi noktalar framework kilidi oluşturuyor?"
```

### AI Çağında Clean Architecture Neden DAHA ÖNEMLİ?

```
Paradoks: AI daha çok kod üretecek → mimari DAHA ÖNEMLİ

  1. AI çok hızlı KOD üretir ama MİMARİ kararları BILMEZ
     → İnsan mimariyi belirler, AI implemente eder
     
  2. AI-generated kod TEKRAR EDİLEBİLİR olmalı
     → Clean Architecture = değiştirilebilir yapı
     → AI'ın yanlış ürettiğini DEĞİŞTİRMEK kolay olmalı

  3. AI-projelerde en büyük sorun: ENTANGLEMENT
     → ML pipeline + business logic + data access İÇ İÇE
     → Google'ın "Machine Learning: The High-Interest Credit Card" makalesi
     → Clean Architecture: ML modeli = Detail, Domain = Stable
```

### Topluluk Görüşleri

```
Uncle Bob (2023 interview):
  "Clean Architecture'ın kuralları hiç değişmedi.
   Framework'ler gelir gider, bağımlılık yönü kalır."

Simon Brown (C4 Model yaratıcısı):
  "Uncle Bob'un dediği doğru ama PRATİKTE çok katmanlı mimari 
   overengineering olabiliyor. Package by Component daha pragmatik."
  → Kitabın "The Missing Chapter"ı tam bunu tartışır!

Reddit r/softwarearchitecture:
  "Clean Architecture kitabı SOLID bölümlerinde mükemmel ama
   pratik örneklerde zayıf. Alistair Cockburn'ın Hexagonal 
   Architecture makalesi ile birlikte oku."

Mark Richards (Fund. of SA yazarı):
  "Uncle Bob SOLID'i iyi anlatır, ama mimari stilleri (event-driven,
   microservices, space-based) için yeterli DEĞİL. İkisini birleştir."
```

---

## 17. �🎬 Son Sözler

### Clean Architecture Akıl Haritası 🧠

```
                    Clean Architecture
                          │
            ┌─────────────┼─────────────┐
            │             │             │
        PRENSİPLER     KATMANLAR      DETAYLAR
            │             │             │
        ┌───┴───┐    ┌────┴────┐   ┌───┴────┐
        │ SOLID │    │ Entity  │   │ DB     │
        │ DIP   │    │ UseCase │   │ Web    │
        │ SRP   │    │ Adapter │   │ Framework│
        │ OCP   │    │ Driver  │   │ UI     │
        └───────┘    └─────────┘   └────────┘

  Bağımlılık Kuralı: DETAYLAR → KATMANLAR → PRENSİPLER
  (Dıştan içe, asla tersi!)
```

### 10 Altın Kural 🏆

| # | Kural | Açıklama |
|---|---|---|
| 1 | **Dependency Rule** | Bağımlılıklar her zaman İÇE doğru |
| 2 | **Entity'ler saftır** | Framework, DB, HTTP bilmez |
| 3 | **Use Case'ler orkestra** | Entity'leri koordine eder, detay bilmez |
| 4 | **Port'lar sözleşme** | Interface = iç ve dış arasındaki KONTRAT |
| 5 | **Adapter'lar dönüştürücü** | Dış formatı iç formata çevirir |
| 6 | **DB detaydır** | Use Case SQL yazmaz |
| 7 | **Web detaydır** | Use Case HTTP bilmez |
| 8 | **Framework detaydır** | İş kuralı Express/Fastify bilmez |
| 9 | **Testler yönlendirsin** | Test edilemiyorsa mimari YANLIŞ |
| 10 | **Pragmatik ol** | "Yeterli" mimari > "mükemmel" mimari |

### Önceki Kitaplarla Bağlantı 🔗

```
📗 Grokking Algorithms → Temel algoritmalar
📕 Clean Code → KOD seviyesinde temizlik
📘 Pragmatic Programmer → MÜHENDİSLİK zihniyeti (DRY, Orthogonality)
📙 Missing README → KARİYER ve ÇALIŞMA pratikleri
📗 Philosophy of Software Design → COMPLEXITY yönetimi
📘 Design Patterns → BİLİNEN çözümler (Pattern → Polimorfizm → DIP)
📕 DDIA → VERİ yönetimi (DB gerçekten detay mı? Kleppmann detayı ANLATIR)
📙 Unit Testing → TEST disiplini (Khorikov: "implementation detail test etme!")
📗 Refactoring → Mevcut kodu güvenle İYİLEŞTİR
🏛️ Clean Architecture → HEPSİNİ bir araya getiren MİMARİ çerçeve!

Clean Architecture, önceki 9 kitabın bilgisini
mimari düzeyde BÜTÜNLEŞTIRIR:

  → Clean Code'un isimlendirme kuralları → Entity'lerde
  → Pragmatic Programmer'ın DRY'sı → Use Case izolasyonu
  → Design Patterns'ın polimorfizmi → DIP uygulaması
  → DDIA'nın veritabanı bilgisi → Repository pattern'ı
  → Khorikov'un test stratejisi → Hexagonal test yaklaşımı
  → Fowler'ın refactoring'i → Kademeli mimari geçiş
```

### Faz 3 İlerleme Durumu 📊

```
FAZ 3 — Mimari & Ölçek (12-18 ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Clean Architecture            ✅  ← BURADASIN
  2. Fundamentals of Software Arch ⬜
  3. Building Microservices        ⬜
  4. The Phoenix Project           ⬜
  5. System Design Interview Vol 1 ⬜
```

---

> **"Mimarinin amacı sistemi ÇALIŞTIRMAK değildir.
> Çoğu kötü mimari de çalışır.
> Mimarinin amacı, sistemi geliştirmeyi, deploy etmeyi
> ve bakımını yapmayı ÖMÜR BOYU ucuz tutmaktır.
> Bunu başarmanın yolu: politikaları detaylardan AYIRMAK
> ve bağımlılıkları her zaman detaylardan politikaya doğru yönlendirmektir.
> Bu tek bir cümleyle özetlenebilir:
> 'İş kuralları hiçbir şeye, her şey iş kurallarına bağımlı olmalı.'"**
> — Robert C. Martin
