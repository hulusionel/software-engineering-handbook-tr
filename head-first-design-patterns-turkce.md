# 🎨 Head First Design Patterns — Türkçe Kapsamlı Rehber

> **"Tecrübeli geliştiriciler aynı problemleri tekrar tekrar çözmez.
> Daha önce işe yarayan çözümleri TEKRAR KULLANIR.
> Bu çözümlere 'Design Patterns' denir."**
> — Gang of Four (GoF)

Bu kitap, GoF'un 23 pattern'ını **hikayeler, görselleştirmeler ve pratik örneklerle**
anlaşılır hale getirir. Ağır akademik dili bırakır, "neden" sorusuna odaklanır.

---

## 📖 İçindekiler

1. [Design Pattern Nedir?](#1--design-pattern-nedir)
2. [OOP Temel İlkeleri](#2--oop-temel-i̇lkeleri)
3. [Strategy Pattern](#3--strategy-pattern)
4. [Observer Pattern](#4--observer-pattern)
5. [Decorator Pattern](#5--decorator-pattern)
6. [Factory Pattern (Simple, Method, Abstract)](#6--factory-pattern)
7. [Singleton Pattern](#7--singleton-pattern)
8. [Command Pattern](#8--command-pattern)
9. [Adapter Pattern](#9--adapter-pattern)
10. [Facade Pattern](#10--facade-pattern)
11. [Template Method Pattern](#11--template-method-pattern)
12. [Iterator Pattern](#12--iterator-pattern)
13. [Composite Pattern](#13--composite-pattern)
14. [State Pattern](#14--state-pattern)
15. [Proxy Pattern](#15--proxy-pattern)
16. [Builder Pattern (Bonus)](#16--builder-pattern-bonus)
17. [Hangi Pattern'ı Ne Zaman Kullanmalı?](#17--hangi-patternı-ne-zaman-kullanmalı)
18. [Anti-Pattern'lar](#18--anti-patternlar)
19. [Son Sözler](#19--son-sözler)

---

## 1. 🧩 Design Pattern Nedir?

### Hikaye: Usta Marangoz 🪵

Bir marangoz düşün. Her yeni mobilya yaptığında sıfırdan "birleştirme tekniği" icat etmez. **Zıvanalı birleştirme**, **kuyruklu geçme**, **kavela birleştirme** gibi yüzlerce yıllık denenmiş teknikleri kullanır.

Design Pattern'lar da yazılımın **zıvanalı birleştirme**leridir:
- Sıfırdan icat etmezsin
- Denenmiş ve kanıtlanmış çözümlerdir
- Diğer ustalarla aynı dili konuşmanı sağlar

### Pattern ≠ Kopyala-Yapıştır Kod 📋

```
Pattern bir ŞABLON değil, bir FİKİRDİR.

Tarif kitabındaki "kek tarifi" gibi düşünme.
Daha çok "tatlıyı yumuşak yapmak için yağ ve şekeri önce çırp" gibi
bir PRENSİP olarak düşün. Bu prensibi kurabiyede de, pastada da,
kekte de uygularsın — ama her seferinde farklı şekilde.
```

### Pattern'ların Üç Kategorisi 📂

| Kategori | Ne Yapar? | Pattern'lar |
|---|---|---|
| **Creational** (Yaratımsal) | Nesneleri NASIL oluşturacağını belirler | Factory, Singleton, Builder |
| **Structural** (Yapısal) | Nesneleri NASIL birleştireceğini belirler | Adapter, Decorator, Facade, Composite, Proxy |
| **Behavioral** (Davranışsal) | Nesnelerin NASIL iletişim kuracağını belirler | Strategy, Observer, Command, State, Template Method, Iterator |

---

## 2. 🏗️ OOP Temel İlkeleri

Pattern'ları anlamadan önce, temeldeki ilkeleri bilmen lazım. Bunlar pattern'ların **neden** bu şekilde tasarlandığını açıklar.

### 4 Temel OOP İlkesi

#### 1. Abstraction (Soyutlama) 🎭

```javascript
// Gerçek dünya: "Araba" deyince motorun piston hareketini düşünmezsin
// Yazılım: Bir nesnenin detaylarını gizleyip, sadece önemli kısmını göster

// Soyutlama: "Ödeme yapmak" = tek bir kavram
class PaymentProcessor {
  async pay(amount) { } // NASIL ödeme yapılacağı gizli
}
```

#### 2. Encapsulation (Kapsülleme) 🔐

```javascript
// Veriler ve davranışlar bir arada, dışarıdan koruma altında
class BankAccount {
  #balance = 0;  // Dışarıdan doğrudan erişilemez

  deposit(amount) {
    if (amount <= 0) throw new Error('Geçersiz miktar');
    this.#balance += amount;
  }

  get balance() {
    return this.#balance;  // Sadece okuma, yazma yok
  }
}

const account = new BankAccount();
account.deposit(100);
// account.#balance = -1000;  ← HATA! Dışarıdan değiştiremezsin ✅
```

#### 3. Inheritance (Kalıtım) 🧬

```javascript
// Ortak özellikleri paylaşma
class Animal {
  eat() { console.log('Nom nom'); }
}

class Dog extends Animal {
  bark() { console.log('Hav hav!'); }
}

const dog = new Dog();
dog.eat();  // Animal'dan miras → "Nom nom"
dog.bark(); // Dog'a özgü → "Hav hav!"
```

#### 4. Polymorphism (Çok Biçimlilik) 🎭🎭

```javascript
// Aynı interface, farklı davranışlar
class CreditCardPayment {
  pay(amount) { console.log(`💳 Kredi kartından ${amount}₺ çekildi`); }
}

class CryptoPayment {
  pay(amount) { console.log(`₿ Kripto ile ${amount}₺ ödendi`); }
}

// Çağıran kodun ödeme TİPİNİ bilmesine gerek yok!
function checkout(paymentMethod, amount) {
  paymentMethod.pay(amount); // Hangisi olursa olsun aynı şekilde çağır
}

checkout(new CreditCardPayment(), 100); // 💳 Kredi kartından 100₺ çekildi
checkout(new CryptoPayment(), 100);     // ₿ Kripto ile 100₺ ödendi
```

### SOLID ile Bağlantı 🔗

Pattern'lar genellikle şu SOLID ilkelerini uygular:

| İlke | Kısaltma | Bir Cümlede |
|---|---|---|
| **Single Responsibility** | SRP | Bir sınıf TEK bir nedenden değişmeli |
| **Open/Closed** | OCP | Genişlemeye AÇIK, değişikliğe KAPALI |
| **Liskov Substitution** | LSP | Alt sınıf, üst sınıfın yerine geçebilmeli |
| **Interface Segregation** | ISP | Kullanmadığın interface'e bağımlı olma |
| **Dependency Inversion** | DIP | Somut sınıfa değil, soyutlamaya bağımlı ol |

---

## 3. 🦆 Strategy Pattern

### Hikaye: SimUDuck Oyunu 🎮🦆

Bir ördek simülasyonu yapıyorsun. Ördekler yüzebilir ve vaklayabilir:

```javascript
// İlk tasarım: Basit kalıtım
class Duck {
  quack() { console.log('Vak vak!'); }
  swim() { console.log('Yüzüyorum!'); }
  display() { /* alt sınıf çizer */ }
}

class MallardDuck extends Duck {
  display() { console.log('Yeşil başlı ördek'); }
}

class RedheadDuck extends Duck {
  display() { console.log('Kızıl başlı ördek'); }
}
```

**Problem:** Patron diyor ki "Ördekler UÇSUN!" 🚀

```javascript
// Naif çözüm: Duck'a fly() ekle
class Duck {
  quack() { console.log('Vak vak!'); }
  swim() { console.log('Yüzüyorum!'); }
  fly() { console.log('Uçuyorum!'); }  // ← Yeni
}

// AMA! 😱
class RubberDuck extends Duck {
  // Plastik ördek uçamaz!
  // Plastik ördek vaklamaz, cıyaklar!
  quack() { console.log('Cıyak cıyak!'); }
  fly() { /* BOŞ — ama neden uçma özelliği olan bir şeyin fly metodu var? */ }
}

class DecoyDuck extends Duck {
  // Tahta ördek: uçamaz, vaklayamaz, yüzemez!
  quack() { } // boş
  fly() { }   // boş
  swim() { }  // boş
  // Bu sınıf neden Duck'tan miras alıyor?! 😩
}
```

**Kalıtım burada ÇALIŞMIYOR!** Her yeni ördek tipinde potansiyel olarak her metodu override etmen gerekiyor.

### Çözüm: Strategy Pattern 🎯

> **"Değişen kısmı, değişmeyen kısımdan AYIR."**
> **"Kalıtım yerine BİLEŞİM (composition) kullan."**

```javascript
// ADIM 1: Değişen davranışları ayrı "strateji" olarak tanımla

// Uçma stratejileri
class FlyWithWings {
  fly() { console.log('Kanatlarımla uçuyorum! 🦅'); }
}

class FlyNoWay {
  fly() { console.log('Uçamıyorum 😢'); }
}

class FlyWithRocket {
  fly() { console.log('ROKETLE UÇUYORUM! 🚀🔥'); }
}

// Vaklama stratejileri
class QuackBehavior {
  quack() { console.log('Vak vak! 🦆'); }
}

class Squeak {
  quack() { console.log('Cıyak cıyak! 🧸'); }
}

class MuteQuack {
  quack() { console.log('... (sessizlik) 🤫'); }
}
```

```javascript
// ADIM 2: Duck sınıfı davranışları İÇİNDE DEĞİL, referans olarak TUTAR

class Duck {
  constructor(flyBehavior, quackBehavior) {
    this.flyBehavior = flyBehavior;
    this.quackBehavior = quackBehavior;
  }

  performFly() {
    this.flyBehavior.fly(); // Davranışı DELEGE et
  }

  performQuack() {
    this.quackBehavior.quack(); // Davranışı DELEGE et
  }

  swim() {
    console.log('Yüzüyorum! 🏊');
  }

  // ✨ ÇALIŞMA ZAMANINDA davranış DEĞİŞTİREBİLİRSİN!
  setFlyBehavior(newFlyBehavior) {
    this.flyBehavior = newFlyBehavior;
  }
}
```

```javascript
// ADIM 3: Ördekleri oluştur

class MallardDuck extends Duck {
  constructor() {
    super(new FlyWithWings(), new QuackBehavior());
  }

  display() { console.log('Yeşil başlı ördek 🟢'); }
}

class RubberDuck extends Duck {
  constructor() {
    super(new FlyNoWay(), new Squeak());
  }

  display() { console.log('Sarı plastik ördek 🟡'); }
}

// KULLANIM:
const mallard = new MallardDuck();
mallard.performFly();   // "Kanatlarımla uçuyorum! 🦅"
mallard.performQuack(); // "Vak vak! 🦆"

const rubber = new RubberDuck();
rubber.performFly();    // "Uçamıyorum 😢"
rubber.performQuack();  // "Cıyak cıyak! 🧸"

// ✨ Plastik ördeğe roket takayım!
rubber.setFlyBehavior(new FlyWithRocket());
rubber.performFly();    // "ROKETLE UÇUYORUM! 🚀🔥"
```

### Gerçek Dünya Kullanımı 🌍

```javascript
// Ödeme stratejileri
class CreditCardStrategy {
  pay(amount) {
    console.log(`💳 Kredi kartı ile ${amount}₺ ödendi`);
    // Kredi kartı validasyonu, 3D Secure, vs.
  }
}

class BankTransferStrategy {
  pay(amount) {
    console.log(`🏦 Havale ile ${amount}₺ gönderildi`);
    // IBAN kontrolü, EFT/Havale işlemi
  }
}

class CryptoStrategy {
  pay(amount) {
    console.log(`₿ Kripto ile ${amount}₺ değerinde ödeme yapıldı`);
    // Wallet adresi, blockchain onay
  }
}

class PaymentService {
  constructor(strategy) {
    this.strategy = strategy;
  }

  setStrategy(strategy) {
    this.strategy = strategy; // Çalışma zamanında değiştir!
  }

  checkout(amount) {
    this.strategy.pay(amount);
  }
}

// Kullanım: Kullanıcı ödeme yöntemini seçer
const payment = new PaymentService(new CreditCardStrategy());
payment.checkout(500); // 💳 Kredi kartı ile 500₺ ödendi

// Kullanıcı fikir değiştirdi
payment.setStrategy(new BankTransferStrategy());
payment.checkout(500); // 🏦 Havale ile 500₺ gönderildi
```

### 🧠 Prensip #1: Program to an Interface, Not an Implementation

```
❌ "Bu nesne MallardDuck'tır ve FlyWithWings yapabilir"
   → Somut (concrete) tipe bağımlısın

✅ "Bu nesne bir Duck'tır ve fly yapabilir"
   → Soyutlamaya (interface/abstract) bağımlısın
   → İçeride ne olduğu seni ilgilendirmez
```

### 🧠 Prensip #2: Favor Composition Over Inheritance

```
❌ Kalıtım: "Ördek bir FlyingAnimal'dır" (IS-A)
   → Katı, değiştirmesi zor

✅ Bileşim: "Ördek bir FlyBehavior'A SAHİPTİR" (HAS-A)
   → Esnek, çalışma zamanında değiştirilebilir
```

---

## 4. 👁️ Observer Pattern

### Hikaye: Hava Durumu İstasyonu 🌤️

Bir hava durumu istasyonun var. Sıcaklık, nem, basınç ölçüyor. Bu verileri **birden fazla ekranda** göstermen lazım: güncel durum ekranı, istatistik ekranı, tahmin ekranı.

```javascript
// ❌ KÖTÜ: Veri değiştiğinde elle her ekranı güncelle
class WeatherStation {
  setMeasurements(temp, humidity, pressure) {
    this.temp = temp;
    this.humidity = humidity;
    this.pressure = pressure;

    // YENİ EKRAN EKLEYECEKSEN BURADA DEĞİŞİKLİK YAPMAN LAZIM!
    currentDisplay.update(temp, humidity, pressure);
    statisticsDisplay.update(temp, humidity, pressure);
    forecastDisplay.update(temp, humidity, pressure);
    // mobileDisplay.update(...) ← Yeni ekran? Burayı değiştir!
    // webDisplay.update(...)    ← Bir tane daha? Yine burayı değiştir!
  }
}
// Open/Closed Principle'ı İHLAL EDİYOR!
// Her yeni ekran için WeatherStation'ı DEĞİŞTİRMEN lazım.
```

### Çözüm: Observer Pattern 📡

> **"Bir nesne (Subject) durum değiştirdiğinde, ona BAĞLİ tüm nesneler (Observer) OTOMATİK olarak haberdar edilir."**

Gazete aboneliği gibi düşün:
- **Gazete şirketi** (Subject): Haber üretir
- **Aboneler** (Observer): Haberleri otomatik alır
- Yeni abone eklenmesi gazete şirketini ETKİLEMEZ
- Abone istediği zaman aboneliğini iptal edebilir

```javascript
// Subject (Yayıncı): Hava Durumu İstasyonu
class WeatherStation {
  #observers = [];
  #temperature;
  #humidity;
  #pressure;

  // Abone ol
  subscribe(observer) {
    this.#observers.push(observer);
    console.log(`📡 Yeni abone eklendi. Toplam: ${this.#observers.length}`);
  }

  // Abonelikten çık
  unsubscribe(observer) {
    this.#observers = this.#observers.filter(obs => obs !== observer);
    console.log(`📡 Abone çıkarıldı. Kalan: ${this.#observers.length}`);
  }

  // Tüm aboneleri bilgilendir
  #notify() {
    for (const observer of this.#observers) {
      observer.update({
        temperature: this.#temperature,
        humidity: this.#humidity,
        pressure: this.#pressure,
      });
    }
  }

  // Yeni ölçüm geldiğinde
  setMeasurements(temperature, humidity, pressure) {
    this.#temperature = temperature;
    this.#humidity = humidity;
    this.#pressure = pressure;
    this.#notify(); // Tüm abonelere OTOMATİK bildir! 🔔
  }
}
```

```javascript
// Observer'lar (Aboneler): Ekranlar
class CurrentConditionsDisplay {
  update({ temperature, humidity }) {
    console.log(`🌡️ Güncel Durum: ${temperature}°C, Nem: %${humidity}`);
  }
}

class StatisticsDisplay {
  #temperatures = [];

  update({ temperature }) {
    this.#temperatures.push(temperature);
    const avg = this.#temperatures.reduce((a, b) => a + b, 0) / this.#temperatures.length;
    const max = Math.max(...this.#temperatures);
    const min = Math.min(...this.#temperatures);
    console.log(`📊 İstatistik: Ort=${avg.toFixed(1)}°C, Max=${max}°C, Min=${min}°C`);
  }
}

class ForecastDisplay {
  #lastPressure = 0;

  update({ pressure }) {
    if (pressure > this.#lastPressure) {
      console.log('☀️ Tahmin: Hava düzelecek!');
    } else if (pressure < this.#lastPressure) {
      console.log('🌧️ Tahmin: Yağmur bekleniyor!');
    } else {
      console.log('🌤️ Tahmin: Değişiklik yok');
    }
    this.#lastPressure = pressure;
  }
}
```

```javascript
// KULLANIM:
const station = new WeatherStation();

const currentDisplay = new CurrentConditionsDisplay();
const statsDisplay = new StatisticsDisplay();
const forecastDisplay = new ForecastDisplay();

station.subscribe(currentDisplay);
station.subscribe(statsDisplay);
station.subscribe(forecastDisplay);

station.setMeasurements(25, 65, 1013);
// 🌡️ Güncel Durum: 25°C, Nem: %65
// 📊 İstatistik: Ort=25.0°C, Max=25°C, Min=25°C
// ☀️ Tahmin: Hava düzelecek!

station.setMeasurements(28, 70, 1010);
// 🌡️ Güncel Durum: 28°C, Nem: %70
// 📊 İstatistik: Ort=26.5°C, Max=28°C, Min=25°C
// 🌧️ Tahmin: Yağmur bekleniyor!

// Yeni ekran ekle — WeatherStation'ı DEĞİŞTİRMEYE GEREK YOK!
class MobileNotification {
  update({ temperature }) {
    if (temperature > 35) {
      console.log('📱 Sıcak hava uyarısı!');
    }
  }
}

station.subscribe(new MobileNotification()); // Sadece abone ol, bitti! ✅
```

### JavaScript'te Yerleşik Observer: EventEmitter 📢

```javascript
const EventEmitter = require('events');

class OrderService extends EventEmitter {
  async createOrder(orderData) {
    const order = await db.orders.insert(orderData);

    // Observer'ları bilgilendir
    this.emit('orderCreated', order);

    return order;
  }
}

const orderService = new OrderService();

// Observer'lar (dinleyiciler) abone olur
orderService.on('orderCreated', (order) => {
  emailService.sendConfirmation(order);
});

orderService.on('orderCreated', (order) => {
  inventoryService.reserveItems(order);
});

orderService.on('orderCreated', (order) => {
  analyticsService.trackPurchase(order);
});

// Yeni bir dinleyici eklemek → OrderService'i DEĞİŞTİRMEZ! ✅
```

### 🧠 Prensip #3: Loose Coupling (Gevşek Bağlantı)

```
Subject ve Observer birbirini minimum düzeyde tanır:

Subject bilir: "Dinleyicilerim var ve update() metodları var"
Subject BİLMEZ: "Kim dinliyor, ne yapıyorlar"

Observer bilir: "Bir Subject'e abone oldum"
Observer BİLMEZ: "Başka kim abone, Subject nasıl çalışıyor"

→ İkisi BAĞİMSIZ değişebilir!
```

---

## 5. 🎁 Decorator Pattern

### Hikaye: Starbuzz Coffee ☕

Bir kahve dükkanı programı yapıyorsun. Kahve + eklentiler (süt, mocha, vaniyla, karamel...):

```javascript
// ❌ Kalıtımla: HER KOMBİNASYON İÇİN AYRI SINIF!
class Coffee { cost() { return 10; } }
class CoffeeWithMilk extends Coffee { cost() { return 12; } }
class CoffeeWithMocha extends Coffee { cost() { return 14; } }
class CoffeeWithMilkAndMocha extends Coffee { cost() { return 16; } }
class CoffeeWithMilkAndMochaAndVanilla extends Coffee { cost() { return 19; } }
class CoffeeWithMilkAndCaramel extends Coffee { cost() { return 17; } }
// ... 😱 Kombinasyon PATLAMASI! 3 eklenti = 2³ = 8 sınıf!
// 10 eklenti = 2¹⁰ = 1024 SINIF!
```

### Çözüm: Decorator Pattern 🎀

> **"Nesnelere çalışma zamanında yeni sorumluluklar ekle.
> Kalıtıma alternatif, esnek bir genişleme mekanizması."**

Hediye paketi gibi düşün: 🎁
- Hediyeyi (kahve) al
- Bir kâğıda sar (süt ekle)
- Üstüne kurdele koy (mocha ekle)
- Yıldız ekle (vaniyla ekle)
- Her katman öncekini SARAR, yeni özellik ekler

```javascript
// Temel bileşen: Kahve
class Espresso {
  cost() { return 10; }
  description() { return 'Espresso'; }
}

class HouseBlend {
  cost() { return 8; }
  description() { return 'House Blend'; }
}

// Decorator'lar: Eklentiler
class MilkDecorator {
  constructor(beverage) {
    this.beverage = beverage; // Sardığı nesneyi tut
  }

  cost() {
    return this.beverage.cost() + 2; // Öncekinin fiyatı + süt
  }

  description() {
    return this.beverage.description() + ', Süt';
  }
}

class MochaDecorator {
  constructor(beverage) {
    this.beverage = beverage;
  }

  cost() {
    return this.beverage.cost() + 4;
  }

  description() {
    return this.beverage.description() + ', Mocha';
  }
}

class VanillaDecorator {
  constructor(beverage) {
    this.beverage = beverage;
  }

  cost() {
    return this.beverage.cost() + 3;
  }

  description() {
    return this.beverage.description() + ', Vanilya';
  }
}
```

```javascript
// KULLANIM: Katman katman SAR!
let beverage = new Espresso();
console.log(`${beverage.description()}: ${beverage.cost()}₺`);
// Espresso: 10₺

beverage = new MilkDecorator(beverage);     // Süt ekle
console.log(`${beverage.description()}: ${beverage.cost()}₺`);
// Espresso, Süt: 12₺

beverage = new MochaDecorator(beverage);    // Mocha ekle
console.log(`${beverage.description()}: ${beverage.cost()}₺`);
// Espresso, Süt, Mocha: 16₺

beverage = new VanillaDecorator(beverage);  // Vanilya ekle
console.log(`${beverage.description()}: ${beverage.cost()}₺`);
// Espresso, Süt, Mocha, Vanilya: 19₺

// ÇİFT MOCHA?
beverage = new MochaDecorator(beverage);    // Bir mocha daha!
console.log(`${beverage.description()}: ${beverage.cost()}₺`);
// Espresso, Süt, Mocha, Vanilya, Mocha: 23₺
```

### Gerçek Dünya: Middleware Pipeline 🔗

Express.js middleware'leri aslında Decorator Pattern'dır!

```javascript
// Her middleware, request/response'u "sarar" ve yeni özellik ekler

// Temel handler
function handleRequest(req, res) {
  res.json({ message: 'Merhaba!' });
}

// Decorator 1: Loglama ekle
function withLogging(handler) {
  return (req, res) => {
    console.log(`📝 ${req.method} ${req.url}`);
    handler(req, res);
  };
}

// Decorator 2: Auth kontrolü ekle
function withAuth(handler) {
  return (req, res) => {
    if (!req.headers.authorization) {
      return res.status(401).json({ error: 'Yetkisiz' });
    }
    handler(req, res);
  };
}

// Decorator 3: Rate limiting ekle
function withRateLimit(handler, maxRequests = 100) {
  const counts = new Map();
  return (req, res) => {
    const ip = req.ip;
    const current = counts.get(ip) || 0;
    if (current >= maxRequests) {
      return res.status(429).json({ error: 'Çok fazla istek' });
    }
    counts.set(ip, current + 1);
    handler(req, res);
  };
}

// Katman katman sar:
const securedHandler = withRateLimit(withAuth(withLogging(handleRequest)));
// İstek akışı: RateLimit → Auth → Logging → Handler

// Express'te bu şu şekilde:
app.get('/api/data', rateLimit, authenticate, logRequest, handleRequest);
```

### 🧠 Prensip #4: Open/Closed Principle

```
Sınıflar GENİŞLEMEYE açık, DEĞİŞİKLİĞE kapalı olmalı.

❌ Yeni eklenti = mevcut sınıfı değiştir
✅ Yeni eklenti = yeni Decorator sınıfı ekle (mevcut kod değişmez)
```

---

## 6. 🏭 Factory Pattern

### Üç Çeşit Factory Var!

#### 1. Simple Factory (Basit Fabrika)

```javascript
// ❌ Client doğrudan nesne oluşturuyor — problem!
function orderPizza(type) {
  let pizza;

  // Bu kısım HER ZAMAN DEĞİŞİYOR: yeni pizza? burayı değiştir!
  if (type === 'cheese') pizza = new CheesePizza();
  else if (type === 'pepperoni') pizza = new PepperoniPizza();
  else if (type === 'veggie') pizza = new VeggiePizza();
  // else if (type === 'hawaiian') pizza = new HawaiianPizza(); ← Yeni!
  // else if (type === 'bbq') pizza = new BBQPizza();            ← Yine yeni!

  pizza.prepare();
  pizza.bake();
  pizza.cut();
  return pizza;
}
```

```javascript
// ✅ Simple Factory: Oluşturma mantığını ayır
class PizzaFactory {
  createPizza(type) {
    switch (type) {
      case 'cheese':    return new CheesePizza();
      case 'pepperoni': return new PepperoniPizza();
      case 'veggie':    return new VeggiePizza();
      default: throw new Error(`Bilinmeyen pizza: ${type}`);
    }
  }
}

function orderPizza(type) {
  const factory = new PizzaFactory();
  const pizza = factory.createPizza(type);  // Oluşturma DELEGEDİ

  pizza.prepare();
  pizza.bake();
  pizza.cut();
  return pizza;
}
// Yeni pizza? Sadece PizzaFactory'i değiştir. orderPizza'ya dokunma! ✅
```

#### 2. Factory Method Pattern 🏭

> **"Alt sınıflara, hangi nesnenin oluşturulacağına karar verme yetkisi ver."**

```javascript
// Farklı şehirlerin farklı pizza stilleri var!
class PizzaStore {
  orderPizza(type) {
    const pizza = this.createPizza(type); // ALT SINIF karar verir!

    pizza.prepare();
    pizza.bake();
    pizza.cut();
    pizza.box();
    return pizza;
  }

  // Factory Method — Alt sınıf OVERRIDE eder
  createPizza(type) {
    throw new Error('Alt sınıf bu metodu implement etmeli!');
  }
}

class IstanbulPizzaStore extends PizzaStore {
  createPizza(type) {
    switch (type) {
      case 'cheese':    return new IstanbulCheesePizza();    // İnce hamur, beyaz peynir
      case 'pepperoni': return new IstanbulPepperoniPizza(); // Sucuk!
      case 'veggie':    return new IstanbulVeggiePizza();    // Kekikli
      default: throw new Error(`Bilinmeyen: ${type}`);
    }
  }
}

class ItalianPizzaStore extends PizzaStore {
  createPizza(type) {
    switch (type) {
      case 'cheese':    return new ItalianCheesePizza();     // Kalın hamur, mozzarella
      case 'pepperoni': return new ItalianPepperoniPizza();  // Gerçek pepperoni
      case 'veggie':    return new ItalianVeggiePizza();     // Pesto soslu
      default: throw new Error(`Bilinmeyen: ${type}`);
    }
  }
}

// Kullanım:
const istanbulStore = new IstanbulPizzaStore();
const pizza = istanbulStore.orderPizza('pepperoni');
// → Sucuklu, ince hamurlu İstanbul usulü pizza! 🍕
```

#### 3. Abstract Factory Pattern 🏭🏭

> **"Birbiriyle ilişkili nesne AİLELERİ oluştur."**

```javascript
// Bir pizza için malzeme AİLESİ lazım: hamur + sos + peynir + et
class IstanbulIngredientFactory {
  createDough()   { return new ThinCrustDough(); }     // İnce hamur
  createSauce()   { return new TomatoSauce(); }        // Domates sos
  createCheese()  { return new WhiteCheese(); }        // Beyaz peynir
  createMeat()    { return new Sucuk(); }              // Sucuk!
}

class ItalianIngredientFactory {
  createDough()   { return new ThickCrustDough(); }    // Kalın hamur
  createSauce()   { return new MarinaraSauce(); }      // Marinara sos
  createCheese()  { return new Mozzarella(); }         // Mozzarella
  createMeat()    { return new Pepperoni(); }          // Pepperoni
}

class CheesePizza {
  constructor(ingredientFactory) {
    this.factory = ingredientFactory;
  }

  prepare() {
    this.dough = this.factory.createDough();
    this.sauce = this.factory.createSauce();
    this.cheese = this.factory.createCheese();
    console.log(`Hazırlanıyor: ${this.dough.name} + ${this.sauce.name} + ${this.cheese.name}`);
  }
}

// İstanbul peynirli pizza: İnce hamur + Domates sos + Beyaz peynir ✅
// İtalyan peynirli pizza:  Kalın hamur + Marinara sos + Mozzarella ✅
// AYNI sınıf, FARKLI malzemeler — factory sayesinde!
```

### Gerçek Dünya: Veritabanı Bağlantıları 🗄️

```javascript
class DatabaseFactory {
  static create(config) {
    switch (config.type) {
      case 'postgresql':
        return new PostgresClient(config);
      case 'mongodb':
        return new MongoClient(config);
      case 'redis':
        return new RedisClient(config);
      default:
        throw new Error(`Desteklenmeyen DB: ${config.type}`);
    }
  }
}

// Kullanım: Client hangi DB olduğunu bilmek zorunda değil!
const db = DatabaseFactory.create({ type: 'postgresql', host: 'localhost' });
await db.query('SELECT * FROM users');

// Test ortamında SQLite kullan:
const testDb = DatabaseFactory.create({ type: 'sqlite', path: ':memory:' });
```

### 🧠 Prensip #5: Dependency Inversion

```
❌ Üst seviye modüller, alt seviye modüllere bağımlı
   PizzaStore → CheesePizza, PepperoniPizza (somut sınıflar)

✅ Her iki seviye de SOYUTLAMALARA bağımlı
   PizzaStore → Pizza (interface)
   CheesePizza → Pizza (interface)
```

---

## 7. 🔮 Singleton Pattern

### Tek Bir Nesne, Her Yerde Aynı 1️⃣

> **"Bir sınıftan SADECE TEK BİR NESNE oluşturulmasını garanti et."**

Gerçek dünya örnekleri: Veritabanı bağlantı havuzu, yapılandırma nesnesi, logger.

```javascript
// ❌ Singleton olmadan: Her seferinde yeni bağlantı!
const db1 = new DatabaseConnection(); // Bağlantı 1
const db2 = new DatabaseConnection(); // Bağlantı 2
const db3 = new DatabaseConnection(); // Bağlantı 3
// 100 modül = 100 bağlantı! Veritabanı çöker! 💥

// ✅ Singleton: Her zaman aynı nesne
class Database {
  static #instance = null;

  static getInstance() {
    if (!Database.#instance) {
      Database.#instance = new Database();
      console.log('🔌 Veritabanı bağlantısı oluşturuldu');
    }
    return Database.#instance;
  }

  constructor() {
    if (Database.#instance) {
      throw new Error('new Database() kullanma! Database.getInstance() kullan.');
    }
    this.connection = this.#connect();
  }

  #connect() { /* ... bağlantı */ }

  query(sql) { /* ... sorgu */ }
}

const db1 = Database.getInstance(); // 🔌 Veritabanı bağlantısı oluşturuldu
const db2 = Database.getInstance(); // (sessizlik — aynı nesne döner)
console.log(db1 === db2); // true ✅ Aynı nesne!
```

### Node.js'te Doğal Singleton: module.exports 📦

```javascript
// Node.js modülleri zaten singleton'dır!
// İlk require'da çalışır, sonraki require'lar cache'ten döner.

// config.js
console.log('Config yükleniyor...');
module.exports = {
  port: process.env.PORT || 3000,
  dbUrl: process.env.DB_URL || 'localhost',
};

// a.js
const config = require('./config');  // "Config yükleniyor..." (İLK SEFERINDE)

// b.js
const config = require('./config');  // (sessizlik — cache'ten gelir)

// a.js ve b.js AYNI config nesnesini kullanıyor! Doğal singleton! ✅
```

### ⚠️ Singleton Uyarıları

```
Singleton, en ÇOK KÖTÜYE KULLANILAN pattern'dır!

Sorunları:
  1. Global state → Test edilmesi ZOR
  2. Bağımlılıkları GİZLER (kod okurken görmezsin)
  3. Single Responsibility ihlali (hem "iş yap" hem "tekliği garanti et")

Kullan: DB bağlantı havuzu, configuration, logger
KULLANMA: İş mantığı sınıfları, servisler, controller'lar

Alternatif: Dependency Injection (DI) kullan!
  Singleton yerine → "Tek nesne oluştur, her yere AKTAR"
```

---

## 8. 📋 Command Pattern

### Hikaye: Akıllı Ev Kumandası 🏠

Evdeki cihazları kontrol eden bir kumanda tasarlıyorsun. Her düğme farklı bir cihazı kontrol edebilmeli:

```javascript
// ❌ OLMAZ: Her düğme için hardcoded mantık
class RemoteControl {
  pressButton(slot) {
    if (slot === 0) light.turnOn();
    else if (slot === 1) fan.setSpeed('high');
    else if (slot === 2) stereo.setCD(); stereo.setVolume(11); stereo.on();
    // Yeni cihaz = burayı değiştir! 😩
  }
}
```

### Çözüm: Command Pattern ⌨️

> **"Bir isteği NESNE olarak sarmalayarak, istekleri parametre olarak geçir,
> sıraya koy, logla veya GERİ AL."**

```javascript
// KOMUT interface'i: Her komut execute() ve undo() yapabilir
// Komutlar
class LightOnCommand {
  constructor(light) {
    this.light = light;
  }
  execute() { this.light.turnOn(); }
  undo()    { this.light.turnOff(); }
}

class LightOffCommand {
  constructor(light) {
    this.light = light;
  }
  execute() { this.light.turnOff(); }
  undo()    { this.light.turnOn(); }
}

class FanHighCommand {
  constructor(fan) {
    this.fan = fan;
    this.prevSpeed = null;
  }
  execute() {
    this.prevSpeed = this.fan.getSpeed();
    this.fan.setSpeed('high');
  }
  undo() {
    this.fan.setSpeed(this.prevSpeed); // Önceki hıza geri dön!
  }
}

class StereoPlayCommand {
  constructor(stereo) { this.stereo = stereo; }
  execute() {
    this.stereo.on();
    this.stereo.setCD();
    this.stereo.setVolume(11);
  }
  undo() {
    this.stereo.off();
  }
}
```

```javascript
// Kumanda: Komutları slotlara ata
class RemoteControl {
  #slots = [];
  #history = []; // GERİ ALMA geçmişi ↩️

  setCommand(slot, command) {
    this.#slots[slot] = command;
  }

  pressButton(slot) {
    const command = this.#slots[slot];
    if (command) {
      command.execute();
      this.#history.push(command);
    }
  }

  pressUndo() {
    const command = this.#history.pop();
    if (command) {
      command.undo();
      console.log('↩️ Geri alındı!');
    }
  }
}
```

```javascript
// KULLANIM:
const livingRoomLight = { turnOn: () => console.log('💡 Salon ışığı AÇIK'), turnOff: () => console.log('💡 Salon ışığı KAPALI') };
const fan = { speed: 'off', getSpeed() { return this.speed; }, setSpeed(s) { this.speed = s; console.log(`🌀 Fan: ${s}`); } };

const remote = new RemoteControl();
remote.setCommand(0, new LightOnCommand(livingRoomLight));
remote.setCommand(1, new FanHighCommand(fan));

remote.pressButton(0); // 💡 Salon ışığı AÇIK
remote.pressButton(1); // 🌀 Fan: high

remote.pressUndo();    // ↩️ Geri alındı! → 🌀 Fan: off
remote.pressUndo();    // ↩️ Geri alındı! → 💡 Salon ışığı KAPALI
```

### Gerçek Dünya: Undo/Redo, İş Kuyrukları 📦

```javascript
// Metin editörü: Undo/Redo
class InsertTextCommand {
  constructor(editor, text, position) {
    this.editor = editor;
    this.text = text;
    this.position = position;
  }

  execute() {
    this.editor.insertAt(this.position, this.text);
  }

  undo() {
    this.editor.deleteAt(this.position, this.text.length);
  }
}

// İş kuyruğu: Komutları sıraya koy, sırayla çalıştır
class JobQueue {
  #queue = [];

  addJob(command) {
    this.#queue.push(command);
  }

  async processAll() {
    while (this.#queue.length > 0) {
      const command = this.#queue.shift();
      await command.execute();
    }
  }
}
```

---

## 9. 🔌 Adapter Pattern

### Hikaye: Avrupa Prizi 🔌

Türkiye'den aldığın şarj aleti Amerika'da prize uymuyor. Ne yaparsın? **Adaptör** alırsın! Adaptör, prizin şeklini değiştirir ama elektriğin kendisi aynıdır.

```javascript
// Mevcut sistem: Türk ödeme sistemi (eski API)
class TurkishPaymentSystem {
  odemeYap(miktar, parabirimi) {
    console.log(`${miktar} ${parabirimi} ödeme yapıldı (TR sistemi)`);
    return { basarili: true, islemNo: 'TR-' + Date.now() };
  }

  odemedurumSorgula(islemNo) {
    return { durum: 'tamamlandi', islemNo };
  }
}

// Yeni sistem: Uluslararası ödeme interface'i (yeni API)
// Tüm yeni kodlar BU interface'i bekliyor:
// processPayment(amount, currency) → { success, transactionId }
// getStatus(transactionId) → { status, transactionId }
```

```javascript
// ❌ KÖTÜ ÇÖZÜM: Eski sistemi değiştir
// Riskli! Çalışan kodu bozmak tehlikeli.
// Eski sistemi kullanan başka yerler de var!

// ✅ ADAPTER: Eski sistemi yeni interface'e uyarla
class TurkishPaymentAdapter {
  constructor() {
    this.turkishSystem = new TurkishPaymentSystem();
  }

  processPayment(amount, currency) {
    // Yeni interface → Eski sisteme çevir
    const result = this.turkishSystem.odemeYap(amount, currency);
    // Eski yanıtı → Yeni formata çevir
    return {
      success: result.basarili,
      transactionId: result.islemNo,
    };
  }

  getStatus(transactionId) {
    const result = this.turkishSystem.odemedurumSorgula(transactionId);
    return {
      status: result.durum === 'tamamlandi' ? 'completed' : 'pending',
      transactionId: result.islemNo,
    };
  }
}

// KULLANIM: Yeni kod eski sistemi bilmiyor bile!
const paymentProcessor = new TurkishPaymentAdapter();
const result = paymentProcessor.processPayment(100, 'TRY');
// { success: true, transactionId: 'TR-1713020400000' }
```

### Gerçek Dünya: API Entegrasyonları 🌐

```javascript
// Farklı SMS provider'ları → Tek interface
class TwilioAdapter {
  constructor(twilioClient) { this.client = twilioClient; }

  async sendSMS(to, message) {
    const result = await this.client.messages.create({
      body: message, to, from: '+1234567890'
    });
    return { id: result.sid, status: result.status };
  }
}

class NetGSMAdapter {
  constructor(netgsmClient) { this.client = netgsmClient; }

  async sendSMS(to, message) {
    const result = await this.client.smsGonder({
      numara: to, mesaj: message, baslik: 'SIRKET'
    });
    return { id: result.islemId, status: result.durum === '0' ? 'sent' : 'failed' };
  }
}

// KULLANIM: Hangisi olduğu önemli değil!
async function sendVerificationCode(smsProvider, phone, code) {
  await smsProvider.sendSMS(phone, `Doğrulama kodunuz: ${code}`);
}

sendVerificationCode(new TwilioAdapter(twilioClient), '+905551234567', '123456');
sendVerificationCode(new NetGSMAdapter(netgsmClient), '+905551234567', '123456');
```

---

## 10. 🏨 Facade Pattern

### Hikaye: Otel Resepsiyonu 🛎️

Bir otele gittiğinde odanı almak için şunları yapman gerekmez:
- Temizlik ekibini ara → "Oda 301'i temizle"
- Teknik servisi ara → "Oda 301'in klimasını aç"
- Mutfağı ara → "Oda 301 minibar dolsun"
- Güvenliği ara → "Oda 301'e kart bası ver"

Sadece **resepsiyona** gidersin: "Oda istiyorum." Resepsiyon HER ŞEYİ halleder.

```javascript
// Karmaşık alt sistemler:
class RoomService {
  cleanRoom(room) { console.log(`🧹 Oda ${room} temizlendi`); }
}

class ACSystem {
  setTemperature(room, temp) { console.log(`❄️ Oda ${room}: ${temp}°C`); }
}

class KeyCardSystem {
  issueCard(room, guest) {
    console.log(`🔑 Oda ${room} için ${guest}'a kart verildi`);
    return { room, guest, cardId: 'CARD-' + Date.now() };
  }
  revokeCard(cardId) { console.log(`🔑 Kart ${cardId} iptal edildi`); }
}

class BillingSystem {
  createInvoice(guest, room, nights) {
    const total = nights * 500;
    console.log(`💰 ${guest}: ${nights} gece, ${total}₺`);
    return { guest, total };
  }
}

class MinibarService {
  stockMinibar(room) { console.log(`🍫 Oda ${room} minibar dolduruldu`); }
}
```

```javascript
// ❌ Facade olmadan: Client TÜM alt sistemleri bilmek zorunda
function checkIn(guest, room, nights) {
  const roomService = new RoomService();
  const ac = new ACSystem();
  const keyCard = new KeyCardSystem();
  const billing = new BillingSystem();
  const minibar = new MinibarService();

  roomService.cleanRoom(room);
  ac.setTemperature(room, 22);
  minibar.stockMinibar(room);
  const card = keyCard.issueCard(room, guest);
  billing.createInvoice(guest, room, nights);
  return card;
}
// Client 5 alt sistemi biliyor, 5 sınıf oluşturuyor. KARMAŞIK!
```

```javascript
// ✅ FACADE: Tek bir basit interface
class HotelFacade {
  constructor() {
    this.roomService = new RoomService();
    this.ac = new ACSystem();
    this.keyCard = new KeyCardSystem();
    this.billing = new BillingSystem();
    this.minibar = new MinibarService();
  }

  checkIn(guest, room, nights) {
    console.log(`\n🏨 Check-in: ${guest}, Oda ${room}\n${'─'.repeat(35)}`);
    this.roomService.cleanRoom(room);
    this.ac.setTemperature(room, 22);
    this.minibar.stockMinibar(room);
    const card = this.keyCard.issueCard(room, guest);
    this.billing.createInvoice(guest, room, nights);
    console.log('─'.repeat(35));
    console.log('✅ Check-in tamamlandı!\n');
    return card;
  }

  checkOut(guest, cardId) {
    console.log(`\n🏨 Check-out: ${guest}\n${'─'.repeat(35)}`);
    this.keyCard.revokeCard(cardId);
    console.log('✅ Check-out tamamlandı!\n');
  }
}

// KULLANIM: Client sadece facade'ı bilir!
const hotel = new HotelFacade();
const card = hotel.checkIn('Ali', 301, 3);
// 🏨 Check-in: Ali, Oda 301
// 🧹 Oda 301 temizlendi
// ❄️ Oda 301: 22°C
// 🍫 Oda 301 minibar dolduruldu
// 🔑 Oda 301 için Ali'a kart verildi
// 💰 Ali: 3 gece, 1500₺
// ✅ Check-in tamamlandı!
```

### Adapter vs Facade Farkı ⚖️

```
Adapter:  BİR interface'i BAŞKA BİR interface'e dönüştürür
          Amaç: Uyumsuz sistemleri uyumlu hale getirmek

Facade:   KARMAŞIK bir sisteme BASİT bir interface sağlar
          Amaç: Kullanımı kolaylaştırmak
```

---

## 11. 📐 Template Method Pattern

### Hikaye: Çay ve Kahve 🍵☕

Çay ve kahve hazırlama süreci neredeyse aynı:

```
Kahve:                    Çay:
1. Suyu kaynat            1. Suyu kaynat        ← AYNI
2. Kahveyi demle          2. Çay poşetini demle ← FARKLI
3. Bardağa dök            3. Bardağa dök        ← AYNI
4. Süt ve şeker ekle      4. Limon ekle          ← FARKLI
```

> **"Algoritmanın iskeletini tanımla, bazı adımları alt sınıflara bırak."**

```javascript
// Template (Şablon): Ortak akış
class HotBeverage {
  // TEMPLATE METHOD: Algoritmayı tanımlar, adımları sıralar
  // Alt sınıflar bunu DEĞİŞTİREMEZ
  prepare() {
    this.boilWater();
    this.brew();          // Alt sınıf belirler
    this.pourInCup();
    this.addCondiments(); // Alt sınıf belirler
  }

  boilWater() {
    console.log('🔥 Su kaynıyor...');
  }

  pourInCup() {
    console.log('☕ Bardağa dökülüyor...');
  }

  // Alt sınıflar BUNU override eder:
  brew() {
    throw new Error('Alt sınıf implement etmeli!');
  }

  addCondiments() {
    throw new Error('Alt sınıf implement etmeli!');
  }
}
```

```javascript
class Coffee extends HotBeverage {
  brew() {
    console.log('☕ Kahve demleniyor (French press)...');
  }

  addCondiments() {
    console.log('🥛 Süt ve şeker ekleniyor...');
  }
}

class Tea extends HotBeverage {
  brew() {
    console.log('🍵 Çay poşeti demleniyor...');
  }

  addCondiments() {
    console.log('🍋 Limon ekleniyor...');
  }
}

// KULLANIM:
new Coffee().prepare();
// 🔥 Su kaynıyor...
// ☕ Kahve demleniyor (French press)...
// ☕ Bardağa dökülüyor...
// 🥛 Süt ve şeker ekleniyor...

new Tea().prepare();
// 🔥 Su kaynıyor...
// 🍵 Çay poşeti demleniyor...
// ☕ Bardağa dökülüyor...
// 🍋 Limon ekleniyor...
```

### Hook Methods (Kanca Metotları) 🪝

Alt sınıfların İSTERSE override edeceği opsiyonel adımlar:

```javascript
class HotBeverage {
  prepare() {
    this.boilWater();
    this.brew();
    this.pourInCup();
    if (this.customerWantsCondiments()) {  // HOOK! 🪝
      this.addCondiments();
    }
  }

  // Hook: Varsayılan evet, alt sınıf değiştirebilir
  customerWantsCondiments() {
    return true;
  }
}

class BlackCoffee extends HotBeverage {
  brew() { console.log('☕ Sade kahve demleniyor...'); }
  addCondiments() { console.log('Bir şey eklenmedi'); }

  customerWantsCondiments() {
    return false; // Sade! Hiçbir şey ekleme!
  }
}
```

### Gerçek Dünya: Veri İşleme Pipeline 📊

```javascript
class DataProcessor {
  // Template method
  async process(source) {
    const rawData = await this.extract(source);
    const cleanData = this.transform(rawData);
    const result = await this.load(cleanData);
    if (this.shouldNotify()) {
      await this.notify(result);
    }
    return result;
  }

  // Alt sınıflar override eder
  async extract(source) { throw new Error('Implement et!'); }
  transform(data) { throw new Error('Implement et!'); }
  async load(data) { throw new Error('Implement et!'); }

  // Hook
  shouldNotify() { return false; }
  async notify(result) { }
}

class CSVtoDBProcessor extends DataProcessor {
  async extract(filePath) {
    return fs.readFileSync(filePath, 'utf-8').split('\n').map(line => line.split(','));
  }

  transform(rows) {
    return rows.map(([name, email, age]) => ({ name, email, age: parseInt(age) }));
  }

  async load(users) {
    return db.users.insertMany(users);
  }

  shouldNotify() { return true; }
  async notify(result) {
    console.log(`📧 ${result.insertedCount} kullanıcı eklendi`);
  }
}
```

### Strategy vs Template Method ⚖️

```
Strategy Pattern:
  → Bileşim (HAS-A) kullanır
  → ALGORİTMANIN TAMAMI değiştirilir
  → Çalışma zamanında değiştirilebilir

Template Method:
  → Kalıtım (IS-A) kullanır
  → Algoritmanın BAZI ADIMLARI değiştirilir
  → Derleme zamanında belirlenir (class tanımında)
```

---

## 12. 🔁 Iterator Pattern

### Hikaye: İki Farklı Menü 📋

İki restoran birleşti. Biri menüyü Array'de, diğeri Object'te tutuyor:

```javascript
// Restoran A: Array kullanıyor
const breakfastMenu = [
  { name: 'Menemen', price: 45 },
  { name: 'Simit', price: 10 },
  { name: 'Çay', price: 5 },
];

// Restoran B: Object kullanıyor
const dinnerMenu = {
  kofte: { name: 'Köfte', price: 80 },
  pilav: { name: 'Pilav', price: 40 },
  ayran: { name: 'Ayran', price: 15 },
};
```

```javascript
// ❌ Client farklı veri yapılarını BİLMEK zorunda
function printMenu() {
  // Array için
  for (let i = 0; i < breakfastMenu.length; i++) {
    console.log(breakfastMenu[i].name);
  }
  // Object için — FARKLI döngü!
  for (const key of Object.keys(dinnerMenu)) {
    console.log(dinnerMenu[key].name);
  }
}
// Her yeni menü türü için yeni döngü yazman lazım!
```

```javascript
// ✅ Iterator Pattern: Ortak dolaşma mekanizması
class ArrayMenuIterator {
  #items;
  #position = 0;

  constructor(items) { this.#items = items; }

  hasNext() { return this.#position < this.#items.length; }
  next()    { return this.#items[this.#position++]; }
}

class ObjectMenuIterator {
  #keys;
  #values;
  #position = 0;

  constructor(obj) {
    this.#keys = Object.keys(obj);
    this.#values = Object.values(obj);
  }

  hasNext() { return this.#position < this.#keys.length; }
  next()    { return this.#values[this.#position++]; }
}

// Client artık veri yapısını bilmiyor!
function printMenu(iterator) {
  while (iterator.hasNext()) {
    const item = iterator.next();
    console.log(`${item.name}: ${item.price}₺`);
  }
}

printMenu(new ArrayMenuIterator(breakfastMenu));
printMenu(new ObjectMenuIterator(dinnerMenu));
```

### JavaScript'te Yerleşik: Symbol.iterator ✨

JavaScript'te iterator pattern DİLE GÖMÜLÜdür:

```javascript
// for...of → Symbol.iterator'ı otomatik çağırır!
for (const item of breakfastMenu) {
  console.log(item.name); // Array zaten iterable ✅
}

// Kendi sınıfını iterable yap:
class Menu {
  #items = [];

  addItem(item) { this.#items.push(item); }

  // Symbol.iterator tanımla → for...of ile dolaş!
  [Symbol.iterator]() {
    let index = 0;
    const items = this.#items;
    return {
      next() {
        if (index < items.length) {
          return { value: items[index++], done: false };
        }
        return { done: true };
      }
    };
  }
}

const menu = new Menu();
menu.addItem({ name: 'Menemen', price: 45 });
menu.addItem({ name: 'Simit', price: 10 });

for (const item of menu) {
  console.log(`${item.name}: ${item.price}₺`);
}

// Spread operatörü de çalışır!
const allItems = [...menu];
```

---

## 13. 🌳 Composite Pattern

### Hikaye: Dosya Sistemi 📁

Dosya ve klasörler bir ağaç yapısı oluşturur. Bir klasörün içinde dosyalar VE başka klasörler olabilir:

```
📁 Projeler/
├── 📄 readme.md (50 KB)
├── 📁 src/
│   ├── 📄 index.js (10 KB)
│   ├── 📄 utils.js (8 KB)
│   └── 📁 controllers/
│       ├── 📄 user.js (15 KB)
│       └── 📄 auth.js (12 KB)
└── 📁 docs/
    └── 📄 api.md (20 KB)
```

**Toplam boyut?** Her dosya + her klasörün içindeki dosyalar... Ama bunu BASİT yapmanın yolu:

> **"Tekil nesneyi (yaprak) ve nesne grubunu (dal) AYNI ŞEKİLDE işle."**

```javascript
// Ortak interface: Hem dosya hem klasör "getSize()" yapabilir

class File {
  constructor(name, size) {
    this.name = name;
    this.size = size;
  }

  getSize() {
    return this.size;
  }

  print(indent = '') {
    console.log(`${indent}📄 ${this.name} (${this.size} KB)`);
  }
}

class Folder {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  add(child) {
    this.children.push(child);
    return this; // Fluent API
  }

  getSize() {
    // Tüm çocukların boyutlarını topla (rekürsif!)
    return this.children.reduce((total, child) => total + child.getSize(), 0);
  }

  print(indent = '') {
    console.log(`${indent}📁 ${this.name}/ (${this.getSize()} KB)`);
    for (const child of this.children) {
      child.print(indent + '  ');
    }
  }
}
```

```javascript
// Ağacı oluştur:
const project = new Folder('Projeler')
  .add(new File('readme.md', 50))
  .add(
    new Folder('src')
      .add(new File('index.js', 10))
      .add(new File('utils.js', 8))
      .add(
        new Folder('controllers')
          .add(new File('user.js', 15))
          .add(new File('auth.js', 12))
      )
  )
  .add(
    new Folder('docs')
      .add(new File('api.md', 20))
  );

project.print();
// 📁 Projeler/ (115 KB)
//   📄 readme.md (50 KB)
//   📁 src/ (45 KB)
//     📄 index.js (10 KB)
//     📄 utils.js (8 KB)
//     📁 controllers/ (27 KB)
//       📄 user.js (15 KB)
//       📄 auth.js (12 KB)
//   📁 docs/ (20 KB)
//     📄 api.md (20 KB)

console.log(`Toplam: ${project.getSize()} KB`); // Toplam: 115 KB
```

### Gerçek Dünya: UI Bileşenleri, Organizasyon Yapıları 🏢

```javascript
// Organizasyon: Departmanlar ve çalışanlar
class Employee {
  constructor(name, salary) {
    this.name = name;
    this.salary = salary;
  }
  getTotalSalary() { return this.salary; }
}

class Department {
  constructor(name) {
    this.name = name;
    this.members = []; // Employee veya alt Department olabilir!
  }
  add(member) { this.members.push(member); }
  getTotalSalary() {
    return this.members.reduce((total, m) => total + m.getTotalSalary(), 0);
  }
}

const engineering = new Department('Mühendislik');
engineering.add(new Employee('Ali', 30000));
engineering.add(new Employee('Ayşe', 35000));

const frontend = new Department('Frontend');
frontend.add(new Employee('Mehmet', 28000));
engineering.add(frontend); // Alt departman

console.log(engineering.getTotalSalary()); // 93000 (rekürsif toplam)
```

---

## 14. 🚦 State Pattern

### Hikaye: Şeker Makinesi 🍬

Bir otomat makinesi düşün. Farklı DURUMLARI var: bozuk para bekliyor, ürün seçimi, ürünü veriyor, satıldı...

```javascript
// ❌ IF-ELSE CEHENNEMI: Her metotta durum kontrolü
class GumballMachine {
  // state = 'NO_COIN' | 'HAS_COIN' | 'SOLD' | 'SOLD_OUT'
  state = 'NO_COIN';
  count = 5;

  insertCoin() {
    if (this.state === 'NO_COIN') {
      this.state = 'HAS_COIN';
      console.log('💰 Para atıldı');
    } else if (this.state === 'HAS_COIN') {
      console.log('⚠️ Zaten para var');
    } else if (this.state === 'SOLD') {
      console.log('⚠️ Ürün çıkıyor, bekleyin');
    } else if (this.state === 'SOLD_OUT') {
      console.log('❌ Ürün tükendi');
    }
  }

  turnCrank() {
    if (this.state === 'NO_COIN') {
      console.log('⚠️ Önce para atın');
    } else if (this.state === 'HAS_COIN') {
      this.state = 'SOLD';
      console.log('🔄 Kol çevrildi');
      this.dispense();
    } else if (this.state === 'SOLD') {
      console.log('⚠️ Zaten çevrildi');
    } else if (this.state === 'SOLD_OUT') {
      console.log('❌ Ürün tükendi');
    }
  }

  // ... HER yeni durum eklediğinde TÜM metotlara yeni if-else ekle!
  // 😱 "WINNER" durumu ekle → 4 metod × 5 durum = 20 koşul!
}
```

### Çözüm: State Pattern 🚦

> **"Nesnenin davranışını, iç durumuna göre değiştir.
> Nesne sanki sınıfını değiştirmiş gibi davransın."**

```javascript
// Her durum bir SINIF
class NoCoinState {
  constructor(machine) { this.machine = machine; }

  insertCoin() {
    console.log('💰 Para atıldı');
    this.machine.setState(this.machine.hasCoinState);
  }

  turnCrank() {
    console.log('⚠️ Önce para atın');
  }

  dispense() {
    console.log('⚠️ Önce para atın');
  }
}

class HasCoinState {
  constructor(machine) { this.machine = machine; }

  insertCoin() {
    console.log('⚠️ Zaten para var');
  }

  turnCrank() {
    console.log('🔄 Kol çevrildi');
    this.machine.setState(this.machine.soldState);
    this.machine.dispense();
  }

  dispense() {
    console.log('⚠️ Henüz kol çevrilmedi');
  }
}

class SoldState {
  constructor(machine) { this.machine = machine; }

  insertCoin() { console.log('⚠️ Ürün çıkıyor, bekleyin'); }
  turnCrank()  { console.log('⚠️ Zaten çevrildi'); }

  dispense() {
    this.machine.releaseGumball();
    if (this.machine.count > 0) {
      this.machine.setState(this.machine.noCoinState);
    } else {
      console.log('❌ Ürün tükendi!');
      this.machine.setState(this.machine.soldOutState);
    }
  }
}

class SoldOutState {
  constructor(machine) { this.machine = machine; }

  insertCoin() { console.log('❌ Ürün tükendi, para atılamaz'); }
  turnCrank()  { console.log('❌ Ürün tükendi'); }
  dispense()   { console.log('❌ Ürün tükendi'); }
}
```

```javascript
// Makine: Durum yönetimi
class GumballMachine {
  constructor(count) {
    this.noCoinState = new NoCoinState(this);
    this.hasCoinState = new HasCoinState(this);
    this.soldState = new SoldState(this);
    this.soldOutState = new SoldOutState(this);

    this.count = count;
    this.state = count > 0 ? this.noCoinState : this.soldOutState;
  }

  setState(state) { this.state = state; }

  insertCoin()  { this.state.insertCoin(); }   // Delege!
  turnCrank()   { this.state.turnCrank(); }     // Delege!
  dispense()    { this.state.dispense(); }      // Delege!

  releaseGumball() {
    if (this.count > 0) {
      this.count--;
      console.log(`🍬 Ürün çıktı! (Kalan: ${this.count})`);
    }
  }
}

// KULLANIM:
const machine = new GumballMachine(3);
machine.insertCoin(); // 💰 Para atıldı
machine.turnCrank();  // 🔄 Kol çevrildi → 🍬 Ürün çıktı! (Kalan: 2)
machine.turnCrank();  // ⚠️ Önce para atın

// YENİ DURUM EKLEMEK KOLAY: WinnerState sınıfı yaz, bitti!
// Mevcut kodları DEĞİŞTİRMEYE neredeyse GEREK YOK! ✅
```

### Strategy vs State ⚖️

```
Aynı yapı, farklı NİYET:

Strategy: Client stratejiyi BİLEREK seçer
  → "Kredi kartıyla öde" (kullanıcı bilinçli seçer)

State: Durum İÇ MANTIKLA değişir
  → "Para atıldı → otomatik olarak HasCoinState'e geç"
  → Client durum değişikliğini kontrol etmez
```

---

## 15. 🛡️ Proxy Pattern

### Tanım 📋

> **"Bir nesneye erişimi kontrol etmek için BİR VEKİL (proxy) koy."**

Gerçek dünya: Avukat (client ile mahkeme arasında vekil), sekreter (patron ile ziyaretçiler arasında vekil).

### Proxy Türleri

#### 1. Sanal Proxy (Lazy Loading) 💤

```javascript
// ❌ Pahalı nesneyi hemen oluştur (belki hiç kullanmayacaksın!)
class HeavyImage {
  constructor(url) {
    this.url = url;
    this.data = this.downloadFromServer(url); // 5 saniye sürüyor! 😓
  }

  downloadFromServer(url) {
    console.log(`⏳ ${url} indiriliyor... (5 saniye)`);
    // ... ağır indirme işlemi
    return '📸 Büyük resim verisi';
  }

  display() {
    console.log(`Gösteriliyor: ${this.data}`);
  }
}

// ✅ Sanal Proxy: Gerçekten İHTİYAÇ olduğunda indir
class ImageProxy {
  constructor(url) {
    this.url = url;
    this.realImage = null; // Henüz yok!
  }

  display() {
    if (!this.realImage) {
      console.log('⏳ Resim ilk kez yükleniyor...');
      this.realImage = new HeavyImage(this.url);
    }
    this.realImage.display();
  }
}

const img = new ImageProxy('https://example.com/huge-photo.jpg');
// ... (hiçbir indirme olmadı!)
img.display(); // ŞİMDİ indir ve göster
img.display(); // Cache'ten, tekrar INDİRME!
```

#### 2. Koruma Proxy (Access Control) 🔒

```javascript
class BankAccount {
  #balance;
  #owner;

  constructor(owner, balance) {
    this.#owner = owner;
    this.#balance = balance;
  }

  withdraw(amount) {
    this.#balance -= amount;
    console.log(`💸 ${amount}₺ çekildi. Kalan: ${this.#balance}₺`);
  }

  getBalance() { return this.#balance; }
  getOwner()   { return this.#owner; }
}

// Koruma Proxy: Yetki kontrolü
class BankAccountProxy {
  constructor(realAccount, currentUser) {
    this.realAccount = realAccount;
    this.currentUser = currentUser;
  }

  withdraw(amount) {
    if (this.currentUser !== this.realAccount.getOwner()) {
      console.log('🚫 Yetkiniz yok! Hesap sahibi değilsiniz.');
      return;
    }
    if (amount > 5000) {
      console.log('⚠️ 5000₺ üzeri çekim için müdür onayı gerekli');
      return;
    }
    this.realAccount.withdraw(amount);
  }

  getBalance() {
    if (this.currentUser !== this.realAccount.getOwner()) {
      console.log('🚫 Bakiye bilgisi gizli');
      return null;
    }
    return this.realAccount.getBalance();
  }
}

const aliAccount = new BankAccount('Ali', 10000);
const proxy = new BankAccountProxy(aliAccount, 'Mehmet');
proxy.withdraw(100); // 🚫 Yetkiniz yok! Hesap sahibi değilsiniz.
proxy.getBalance();  // 🚫 Bakiye bilgisi gizli
```

#### 3. Cache Proxy 🗃️

```javascript
class ApiClient {
  async getUser(id) {
    console.log(`🌐 API çağrısı: /users/${id}`);
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  }
}

class CachingProxy {
  constructor(realClient, ttl = 60000) {
    this.client = realClient;
    this.cache = new Map();
    this.ttl = ttl;
  }

  async getUser(id) {
    const cached = this.cache.get(id);
    if (cached && Date.now() - cached.timestamp < this.ttl) {
      console.log(`⚡ Cache'ten: /users/${id}`);
      return cached.data;
    }

    const data = await this.client.getUser(id);
    this.cache.set(id, { data, timestamp: Date.now() });
    return data;
  }
}

const api = new CachingProxy(new ApiClient());
await api.getUser(1); // 🌐 API çağrısı: /users/1
await api.getUser(1); // ⚡ Cache'ten: /users/1 (API çağrısı yok!)
```

### JavaScript'te Yerleşik Proxy 🪞

JavaScript'in `Proxy` nesnesi bu pattern'ı DİL SEVİYESİNDE destekler:

```javascript
const user = { name: 'Ali', age: 25, _password: 'secret123' };

const protectedUser = new Proxy(user, {
  get(target, prop) {
    if (prop.startsWith('_')) {
      throw new Error(`🚫 "${prop}" alanı gizli!`);
    }
    console.log(`📖 ${prop} okundu`);
    return target[prop];
  },

  set(target, prop, value) {
    if (prop === 'age' && (value < 0 || value > 150)) {
      throw new Error('⚠️ Geçersiz yaş!');
    }
    console.log(`✏️ ${prop} = ${value}`);
    target[prop] = value;
    return true;
  }
});

protectedUser.name;       // 📖 name okundu → "Ali"
protectedUser.age = 30;   // ✏️ age = 30
protectedUser._password;  // 💥 Error: 🚫 "_password" alanı gizli!
protectedUser.age = -5;   // 💥 Error: ⚠️ Geçersiz yaş!
```

---

## 16. 🔨 Builder Pattern (Bonus)

GoF'ta var ama Head First'te yer almıyor. Yine de çok kullanışlı:

> **"Karmaşık nesneleri ADIM ADIM oluştur."**

```javascript
// ❌ Çok parametreli constructor: Hangisi ne?
const query = new HTTPRequest(
  'GET',              // method
  '/api/users',       // path
  { 'Accept': 'application/json' },  // headers
  null,               // body
  5000,               // timeout
  3,                  // retryCount
  true,               // followRedirects
  'bearer xyz',       // auth
  null,               // proxy
  true,               // keepAlive
);
// 10 parametre 😵 Sıralarını ezberlemen lazım!
```

```javascript
// ✅ Builder: Adım adım, okunabilir şekilde oluştur
class RequestBuilder {
  #config = {};

  method(method)     { this.#config.method = method; return this; }
  url(url)           { this.#config.url = url; return this; }
  header(key, value) {
    this.#config.headers = this.#config.headers || {};
    this.#config.headers[key] = value;
    return this;
  }
  body(body)         { this.#config.body = body; return this; }
  timeout(ms)        { this.#config.timeout = ms; return this; }
  retry(count)       { this.#config.retryCount = count; return this; }
  auth(token)        { this.#config.auth = `Bearer ${token}`; return this; }

  build() {
    // Validasyon
    if (!this.#config.method) throw new Error('Method gerekli!');
    if (!this.#config.url) throw new Error('URL gerekli!');
    return { ...this.#config };
  }
}

// KULLANIM: Okunabilir, zincirleme çağrılar
const request = new RequestBuilder()
  .method('GET')
  .url('/api/users')
  .header('Accept', 'application/json')
  .timeout(5000)
  .retry(3)
  .auth('xyz-token')
  .build();

// Her adım ne yaptığını ANLATIYOR! Parametre sırası önemli DEĞİL!
```

---

## 17. 🗺️ Hangi Pattern'ı Ne Zaman Kullanmalı?

### Karar Ağacı 🌳

```
"Nesne OLUŞTURMA ile ilgili bir sorunum var"
  → Karmaşık nesne, çok parametre? → BUILDER
  → Nesne tipi çalışma zamanında belirleniyor? → FACTORY
  → Tek instance gerekli? → SINGLETON (dikkatli!)

"Nesne YAPISI ile ilgili bir sorunum var"
  → Uyumsuz interface'leri bağlamam lazım? → ADAPTER
  → Karmaşık bir sisteme basit erişim? → FACADE
  → Nesnelere dinamik özellik eklemek? → DECORATOR
  → Ağaç yapısı (parça-bütün ilişkisi)? → COMPOSITE
  → Nesneye erişimi kontrol etmek? → PROXY

"Nesne DAVRANIŞI ile ilgili bir sorunum var"
  → Algoritma ailesinden birini seçmek? → STRATEGY
  → Durum değişince davranış değişsin? → STATE
  → "Bir şey olduğunda haberi olsun" mekanizması? → OBSERVER
  → İşlem geri alınabilsin (undo)? → COMMAND
  → Algoritma adımlarının bir kısmı değişsin? → TEMPLATE METHOD
  → Koleksiyonları tiple bağımsız dolaşmak? → ITERATOR
```

### Hızlı Referans Tablosu 📊

| Pattern | Problem | Çözüm | Gerçek Dünya |
|---|---|---|---|
| **Strategy** | Birden fazla algoritma/davranış | Bileşim ile değiştirilebilir strateji | Ödeme yöntemleri, sıralama |
| **Observer** | 1→N olay bildirimi | Subject-Observer ilişkisi | EventEmitter, Webhook |
| **Decorator** | Dinamik özellik ekleme | Nesneyi sararak genişletme | Middleware, stream'ler |
| **Factory** | Nesne oluşturma karmaşıklığı | Oluşturmayı ayır | DB bağlantısı, parser |
| **Singleton** | Tek instance | Static instance kontrolü | Config, Logger, Pool |
| **Command** | İşlem kuyruklama / geri alma | İşlemi nesne olarak kapsülle | Undo/Redo, Job queue |
| **Adapter** | Uyumsuz interface | Dönüştürücü katman | API entegrasyonu |
| **Facade** | Karmaşık alt sistem | Basit interface | SDK, wrapper |
| **Template** | Algoritma iskeleti | Sabit adımlar + değişken adımlar | ETL pipeline |
| **State** | Duruma göre davranış | Her durum bir sınıf | Sipariş durumu, oyun |
| **Composite** | Ağaç yapısı | Yaprak ve dal aynı interface | Dosya sistemi, UI |
| **Proxy** | Erişim kontrolü | Vekil nesne | Cache, auth, lazy load |
| **Builder** | Karmaşık nesne oluşturma | Adım adım inşa | Query builder, config |

---

## 18. 🚫 Anti-Pattern'lar

### Pattern KÖTÜYE kullanılırsa...

#### 1. Pattern Mania 🤒

```javascript
// ❌ Her yere pattern sıkıştırma hastalığı
// Sadece "Hello World" yazdırmak için:
class HelloWorldFactory {
  create() { return new HelloWorldBuilder().build(); }
}

class HelloWorldBuilder {
  build() {
    return new HelloWorldProxy(new HelloWorldDecorator(new HelloWorld()));
  }
}

// 😱 4 sınıf, sadece bir string yazdırmak için!

// ✅ BASIT TUT
console.log('Hello, World!');
```

#### 2. Yanlış Pattern Seçimi 🎯

```
Problem: "İki sınıfın uyumsuz interface'i var"
✅ Doğru: Adapter
❌ Yanlış: Her şeyi Decorator'la sarmak

Problem: "Farklı ortamlarda farklı davranış"
✅ Doğru: Strategy veya Factory
❌ Yanlış: Singleton ile global state tutmak
```

#### 3. God Object (Tanrı Nesnesi) 🌩️

Pattern'ların tam tersi: Her şeyi tek bir sınıfta toplamak.

```javascript
// ❌ GOD OBJECT: Her şeyi yapan sınıf
class Application {
  connectDB() { ... }
  handleHTTP() { ... }
  sendEmail() { ... }
  processPayment() { ... }
  generateReport() { ... }
  manageSessions() { ... }
  validateInput() { ... }
  renderUI() { ... }
  // ... 2000 satır, 50 metod

  // Bu sınıf DEĞİŞMEK için 50 farklı nedeni var!
  // SRP: Single Responsibility = TEK neden!
}
```

---

## 19. 🎬 Son Sözler

### Pattern Öğrenmenin Evreleri 📈

```
Evre 1 — Bilmiyorum 🤷
  "Pattern? O ne?"

Evre 2 — Öğreniyorum 📚
  "Strategy Pattern'ı kullanmalıyım!"

Evre 3 — Aşırı Kullanım 🤒
  "HER YERE PATTERN! Factory + Singleton + Observer!"

Evre 4 — Olgunluk ✨ (HEDEF!)
  "Bu problemi en basit şekilde nasıl çözerim?
   Hmm, burada bir Strategy mantıklı olur.
   Ama şurada YAGNI, basit tut."
```

### 🤖 Yapay Zeka Çağında Design Patterns

```
AI araçları (LangChain, OpenAI SDK, LlamaIndex) pattern'larla DOLU:

🎯 STRATEGY → Model seçimi
   → LLM provider'ı değiştirmek (GPT → Claude → Gemini)
   → Her provider farklı strategy, aynı interface!
   → LangChain'de BaseLLM interface'i = Strategy Pattern!

👀 OBSERVER → Model monitoring
   → Training sırasında loss değişince callback'ler tetiklenir
   → Webhook event sistemleri → Observer Pattern!

🎨 DECORATOR → Middleware zinciri
   → LLM çağrısına: loglama, rate-limiting, caching, retry
   → Her biri bir Decorator → fonksiyonalite SARIYOR!

🏭 FACTORY → Provider-agnostic client
   → createLLMClient("openai") vs createLLMClient("anthropic")
   → Hangi provider olursa olsun aynı INTERFACE → Factory Pattern!

🛡️ PROXY → Rate-limiting, caching
   → OpenAI API'yi doğrudan çağırma → Proxy arkasından çağır
   → Cache Proxy: aynı prompt → cached yanıt (para tasarrufu!)
   → Rate-limit Proxy: saniyede max 10 istek

PROMPT ÖRNEĞİ:
  "Bu kodu refactor et, Strategy Pattern kullanarak 
   farklı AI provider'ları destekle.
   OpenAI, Anthropic ve Google Gemini için 
   ortak bir interface oluştur.
   Factory Method ile provider seçimini konfigürasyona bağla."
```

### Pattern'lar Bir ARAÇ, Amaç DEĞİL 🔧

```
❌ "Bu kodda hangi pattern'ı kullanabilirim?"
   → Pattern'ı çözüm arayan bir problem yapıyorsun

✅ "Bu problemin en temiz çözümü ne?"
   → Cevap bazen bir pattern, bazen basit bir if-else
```

### Bu Kitaptan Öğrendiğin Prensipler 🏆

| # | Prensip | Açıklama |
|---|---|---|
| 1 | **Değişeni, değişmeyenden ayır** | Değişen kısmı kapsülle |
| 2 | **Interface'e programla** | Somut sınıfa değil |
| 3 | **Kalıtım yerine bileşim** | HAS-A > IS-A |
| 4 | **Loose coupling** | Bağımlılıkları minimize et |
| 5 | **Open/Closed** | Genişlemeye açık, değişikliğe kapalı |
| 6 | **Dependency Inversion** | Soyutlamaya bağımlı ol |
| 7 | **En az bilgi (Law of Demeter)** | Yabancılarla konuşma |
| 8 | **Hollywood Principle** | "Bizi arama, biz seni ararız" |
| 9 | **Tek sorumluluk** | Her sınıfın TEK değişme nedeni |

### Öğrenme Yolculuğu 🛤️

```
📗 Grokking Algorithms          → Algoritma temeli ✅
📕 Clean Code                   → Kod kalitesi ✅
📘 The Pragmatic Programmer     → Mühendislik zihniyeti ✅
📙 The Missing README           → Kariyer temeli ✅
📗 A Philosophy of Software Design → Tasarım felsefesi ✅
📘 Head First Design Patterns   → Pattern'lar ✅  ← BURADASIN

Sıradaki (Faz 2 devam):
📕 Designing Data-Intensive Apps → Dağıtık sistem temeli
📙 Unit Testing (Khorikov)       → Test stratejisi
📗 Refactoring (Fowler)          → Referans kitap
```

---

> **"Pattern'lar bilgeliğin DNA'sıdır.
> Binlerce mühendis aynı problemlerle karşılaştı, çözümler buldu,
> bu çözümler denenip elenerek bugünkü haline geldi.
> Sen bu birikimi öğrendiğinde, her yeni problem aslında
> daha önce çözülmüş bir problemin varyasyonudur."** 🧬
>
> — Bu rehberin özü: **"Her pattern bir prensip öğretir. Pattern'ı değil, prensibi öğren."**
