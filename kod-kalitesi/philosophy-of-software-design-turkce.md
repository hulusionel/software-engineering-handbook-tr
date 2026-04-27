# 🧠 A Philosophy of Software Design — Türkçe Kapsamlı Rehber

> **"Yazılım tasarımının en büyük amacı karmaşıklığı azaltmaktır."**
> — John Ousterhout (Stanford CS 190 Dersi)

Bu kitap, Clean Code'dan daha **derin** ve daha **az dogmatik** bir yaklaşımla
yazılım tasarımının felsefesini anlatır. Kurallar değil, **düşünce biçimi** öğretir.

---

## 📖 İçindekiler

1. [Bu Kitap Neden Önemli?](#1--bu-kitap-neden-önemli)
2. [Karmaşıklığın Doğası](#2--karmaşıklığın-doğası)
3. [Stratejik vs Taktiksel Programlama](#3--stratejik-vs-taktiksel-programlama)
4. [Modüller Derin Olmalı](#4--modüller-derin-olmalı)
5. [Bilgi Sızıntısı ve Bilgi Gizleme](#5--bilgi-sızıntısı-ve-bilgi-gizleme)
6. [Genel Amaçlı Modüller](#6--genel-amaçlı-modüller)
7. [Katmanlar Arası Soyutlama](#7--katmanlar-arası-soyutlama)
8. [Karmaşıklığı Aşağı Çek](#8--karmaşıklığı-aşağı-çek)
9. [Bir Arada mı, Ayrı mı?](#9--bir-arada-mı-ayrı-mı)
10. [Hata Yönetimi Felsefesi](#10--hata-yönetimi-felsefesi)
11. [Tasarımda İki Kez Düşün](#11--tasarımda-i̇ki-kez-düşün)
12. [Neden Yorum Yazmak ÖNEMLİDİR](#12--neden-yorum-yazmak-önemli̇di̇r)
13. [İsimlendirme](#13--i̇simlendirme)
14. [Mevcut Kodu Değiştirmek](#14--mevcut-kodu-değiştirmek)
15. [Performans ve Tasarım](#15--performans-ve-tasarım)
16. [Trendler ve Dikkat Edilmesi Gerekenler](#16--trendler-ve-dikkat-edilmesi-gerekenler)
17. [Son Sözler](#17--son-sözler)

---

## 1. 🌟 Bu Kitap Neden Önemli?

### Clean Code'dan Farkı ⚖️

| | Clean Code | A Philosophy of Software Design |
|---|---|---|
| **Yaklaşım** | Kurallar: "Fonksiyon 5 satır olsun" | Felsefe: "Karmaşıklığı azalt" |
| **Yorum** | "Yorum kötüdür, kodu düzelt" | "İyi yorum çok değerlidir!" |
| **Fonksiyon boyutu** | Küçük küçük küçük | "Çok küçük = çok fazla parça = karmaşıklık" |
| **Sınıf boyutu** | Her zaman küçük | "Bazen büyük sınıf daha basittir" |
| **Odak** | Kod seviyesi temizlik | Sistem seviyesi tasarım |

> **İkisi de değerli!** Ama bu kitap daha **olgun** ve **nüanslı** bir bakış açısı sunar. Clean Code "ne yapma" der, bu kitap **"nasıl düşün"** der.

### Stanford CS 190 📚

Bu kitap, John Ousterhout'un Stanford'da verdiği CS 190 dersinin ürünüdür. Öğrenciler gerçek projeler yaparak tasarım prensiplerini öğrenir, her iterasyonda kodlarını gözden geçirip iyileştirirler.

---

## 2. 🌀 Karmaşıklığın Doğası

### Karmaşıklık Nedir? 🤯

> **Karmaşıklık = Bir sistemi anlamayı ve değiştirmeyi ZORLAŞTIRAN her şey.**

Karmaşıklık bir düşman gibidir: görünmez bir şekilde birikir, bir gün fark ettiğinde zaten çok geç olmuştur.

### Karmaşıklığın Üç Belirtisi 🔍

#### 1. Değişiklik Büyümesi (Change Amplification) 📢

Basit bir değişiklik için birçok yeri değiştirmen gerekiyor.

```javascript
// ❌ KARMAŞIK: Renk değiştirmek için 15 dosyayı değiştir
// header.js
const headerStyle = { backgroundColor: '#3498db' };
// sidebar.js
const sidebarStyle = { backgroundColor: '#3498db' };
// footer.js
const footerStyle = { backgroundColor: '#3498db' };
// button.js
const buttonStyle = { backgroundColor: '#3498db' };
// ... 11 dosya daha

// Tasarımcı: "Rengi #2980b9 yapalım" → 15 DOSYA DEĞİŞTİR! 😩

// ✅ BASİT: Tek bir yerde değiştir
// theme.js
const theme = {
  primaryColor: '#3498db',  // Sadece burayı değiştir!
};

// header.js
const headerStyle = { backgroundColor: theme.primaryColor };
// sidebar.js
const sidebarStyle = { backgroundColor: theme.primaryColor };
```

#### 2. Bilişsel Yük (Cognitive Load) 🧠

Bir görevi tamamlamak için geliştiricinin **kafasında tutması gereken bilgi** miktarı.

```javascript
// ❌ YÜKSEK BİLİŞSEL YÜK
// Bu fonksiyonu anlamak için bilmen gerekenler:
// 1. statusCode'ların anlamları (1=active, 2=inactive, 3=suspended, 4=...)
// 2. roleId'lerin anlamları (100=admin, 200=user, 300=...)
// 3. permissionBitmask nasıl çalışıyor (0x01=read, 0x02=write, 0x04=...)
// 4. createdAt neden Unix timestamp (saniye mi, milisaniye mi?)
function canAccess(user, resource) {
  return user.s === 1
    && user.r >= 100
    && (user.p & resource.requiredP) === resource.requiredP
    && (Date.now() / 1000 - user.c) < 86400 * 365;
}

// ✅ DÜŞÜK BİLİŞSEL YÜK
// Bu fonksiyonu anlamak için özel bilgi gerekmez
function canAccess(user, resource) {
  return user.isActive()
    && user.isAdmin()
    && user.hasPermissions(resource.requiredPermissions)
    && !user.isExpired();
}
```

> **Karmaşıklığı ölçmenin en iyi yolu:** "Yeni bir mühendis bu kodu ne kadar zamanda anlar?"

#### 3. Bilinmeyenler-Bilinmeyenler (Unknown Unknowns) ❓❓

En tehlikeli karmaşıklık türü: **Bilmediğini bilmediğin şeyler.**

```javascript
// ❌ UNKNOWN UNKNOWN: Tehlikeli sürpriz
function deleteUser(userId) {
  await db.users.delete(userId);
  // 😱 BİLMEDİĞİN ŞEY: Bu kullanıcının siparişleri de var!
  // Siparişler orphan kalıyor!
  // CRM'deki kayıtlar tutarsız hale geliyor!
  // Payment provider'daki subscription hâlâ aktif!
}

// ✅ KNOWN: Tüm bağımlılıklar açık
function deleteUser(userId) {
  const user = await getUser(userId);
  await cancelAllSubscriptions(userId);     // Abonelikleri iptal et
  await archiveOrders(userId);              // Siparişleri arşivle
  await notifyCRM(userId, 'DELETED');       // CRM'i bilgilendir
  await db.users.softDelete(userId);        // Kullanıcıyı sil (soft delete)
  await auditLog.record('USER_DELETED', { userId });  // Kayıt tut
}
```

> **"Bir değişiklik yaparken 'başka neyi etkiler?' sorusunun cevabını BİLEMİYORSAN, karmaşıklık çok yüksek."**

### Karmaşıklık Kademeli Olarak Birikir 📈

Karmaşıklık tek bir büyük hatayla gelmez. **Yüzlerce küçük kararla** birikir:

```
Gün 1:    "Şimdilik hardcoded bırakayım" → +1 🪨
Gün 5:    "Burada hızlıca bir hack yapalım" → +1 🪨
Gün 12:   "Test sonra yazarım" → +1 🪨
Gün 20:   "Bu fonksiyon biraz uzun ama neyse" → +1 🪨
Gün 35:   "İsimlendirmeyi sonra düzeltirim" → +1 🪨
...
Gün 365:  "BU KODU KİMSE ANLAYAMIYOR!" → 🏔️ (yüzlerce taş birikmiş!)
```

> **Her küçük karar önemli.** Karmaşıklık sıfıra indirilemez ama **kontrol altında** tutulabilir. Bu kitabın tamamı bunun nasıl yapılacağını anlatır.

### Karmaşıklığın Formülü 📐

$$C = \sum_{p} c_p \times t_p$$

- $C$ = Toplam karmaşıklık
- $c_p$ = Her parçanın karmaşıklığı
- $t_p$ = O parçayla ne kadar sık çalışılıyor (zaman ağırlığı)

**Bu formül ne diyor?**
Karmaşık ama **nadiren dokunulan** kod, basit ama **sürekli değiştirilen** koddan daha az sorunludur!

```
Senaryo A: Çok karmaşık ama yılda 1 kez dokunulan modül → Kabul edilebilir
Senaryo B: Biraz karmaşık ama günde 5 kez dokunulan modül → ACİL DÜZELT! 🚨
```

---

## 3. ⚔️ Stratejik vs Taktiksel Programlama

### Hikaye: İki Mühendis 👷

**Taktiksel Ayşe:** "Bir an önce çalışsın, deadline var!"
```
Sprint 1: ✅ Feature tamamlandı (hızlı, ama kodu biraz dağınık)
Sprint 2: ✅ Feature tamamlandı (biraz daha dağınık, ama yetişti)
Sprint 3: ⚠️ Feature tamamlandı (ama 2 bug çıktı, çünkü eski kod karışık)
Sprint 4: 🐛 Bug fixler + Feature (feature yarım kaldı)
Sprint 5: 🔥 "Temelden yazmamız lazım" (her şey kaos)
```

**Stratejik Ali:** "İyi bir tasarım yapayım, biraz daha sürer ama sağlam olur."
```
Sprint 1: ✅ Feature tamamlandı (biraz daha uzun sürdü ama temiz)
Sprint 2: ✅ Feature tamamlandı (kolay, çünkü altyapı sağlam)
Sprint 3: ✅ Feature tamamlandı (daha da hızlı, sistem büyüyor ama karmaşıklaşmıyor)
Sprint 4: ✅ Feature tamamlandı + refactoring (sürekli iyileşme)
Sprint 5: ✅ Feature tamamlandı (rakip hâlâ sprint 3'te!) 🚀
```

### Taktiksel Programlama ❌

```
Hedef: "Çalışsın yeter"
Yaklaşım: "En hızlı yol neyse o"
Sonuç: Teknik borç birikir → Hız AZALIR

    Hız
     │     Taktiksel
     │    ╱╲
     │   ╱  ╲
     │  ╱    ╲
     │ ╱      ╲─────────  (hız sürekli düşer)
     │╱                ╲
     └──────────────────→ Zaman
```

### Stratejik Programlama ✅

```
Hedef: "Harika bir tasarım"
Yaklaşım: "Biraz yavaş başla, sonra hızlan"
Sonuç: Temiz altyapı → Hız ARTAR

    Hız
     │              Stratejik
     │              ╱────────── (hız sürekli artar veya sabit)
     │            ╱
     │          ╱
     │        ╱
     │      ╱
     │    ╱
     │  ╱
     └──────────────────→ Zaman
```

### %10-20 Yatırım Kuralı 💰

> **"Her görev için zamanının %10-20'sini tasarım ve iyileştirmeye ayır."**

Bu demek DEĞİL:
- ❌ 2 hafta hiçbir şey teslim etme, sadece refactor yap
- ❌ Her şeyi mükemmel yap

Bu demek:
- ✅ Yeni feature yazarken, dokunduğun yeri biraz iyileştir
- ✅ Mevcut kodu daha temiz yapacak küçük değişiklikler ekle
- ✅ İsimleri düzelt, gereksiz karmaşıklığı basitleştir
- ✅ Yorum ekle, test ekle

```
5 günlük görev:
├── 4 gün: Feature geliştirme
└── 1 gün: Tasarım iyileştirme, test, dokümantasyon

Uzun vadede bu 1 günlük yatırım, yüzlerce gün kazandırır!
```

---

## 4. 🏊 Modüller Derin Olmalı

### Kitabın EN ÖNEMLİ Kavramı! ⭐

Bu bölüm, kitabın kalbidir. Clean Code'un "küçük fonksiyonlar" dogmasına alternatif bir bakış açısı sunar.

### Modülün İki Yüzü

Her modülün (fonksiyon, sınıf, servis) iki yüzü vardır:

1. **Interface (Arayüz):** Dışarıdan görünen kısım — ne YAPTIĞI
2. **Implementation (Uygulama):** İçerideki detaylar — NASIL yaptığı

```
┌─────────────────────────────┐
│         INTERFACE            │  ← Kullanıcının gördüğü
│  (Fonksiyon adı, parametreler, │
│   dönüş tipi, davranış sözü)  │
├═════════════════════════════┤
│                              │
│                              │
│       IMPLEMENTATION         │  ← Kullanıcının bilmesine
│   (İç mantık, algoritmalar,  │     GEREK OLMAYAN detaylar
│    veri yapıları, optimizasyon)│
│                              │
│                              │
└─────────────────────────────┘
```

### Derin Modül vs Sığ Modül 🏊 vs 🏖️

#### Derin Modül = İYİ ✅

**Basit interface, güçlü işlevsellik.** Az şey sor, çok iş yap.

```
Basit interface (küçük)
┌───────────────┐
│   read(file)  │    ← Sadece dosya adını ver
├═══════════════┤
│               │
│  Dosya sistemi│
│  Buffer yönet │
│  Encoding     │    ← Arkada tonlarca karmaşıklığı GİZLER
│  Cache        │
│  Hata yönetimi│
│  Lock yönetimi│
│               │
└───────────────┘
```

**Gerçek dünya örneği: Unix dosya I/O**

```javascript
// DERİN MODÜL: Unix file system
const data = fs.readFileSync('/path/to/file', 'utf-8');

// Bu tek satırın arkasında neler oluyor?
// 1. Dosya yolu çözümleme (path resolution)
// 2. İzin kontrolü (permission check)
// 3. Disk bloklarını bulma (inode lookup)
// 4. Bellek ayırma (buffer allocation)
// 5. DMA transferi (disk → memory)
// 6. Encoding dönüşümü (bytes → utf-8)
// 7. Cache yönetimi (page cache)
// 8. Hata yönetimi (dosya yok, izin yok, disk bozuk...)
// 9. Lock yönetimi (concurrent access)

// Tüm bu karmaşıklığı TEK BİR FONKSİYON gizliyor!
// Interface: readFileSync(path, encoding) → string
// 2 parametre, 1 dönüş. BASİT! ✅
```

#### Sığ Modül = KÖTÜ ❌

**Karmaşık interface, az işlevsellik.** Çok şey sor, az iş yap.

```
Karmaşık interface (büyük)
┌────────────────────────────────────┐
│ create(host, port, protocol,        │
│   timeout, retryCount, retryDelay,  │  ← Kullanıcı çok şey BİLMEK zorunda
│   certPath, keepAlive, maxSockets,  │
│   encoding, auth, proxy)            │
├════════════════════════════════════┤
│  connect()                          │  ← Arkada az iş yapıyor
└────────────────────────────────────┘
```

```javascript
// ❌ SIĞ MODÜL: Interface'i implementation'dan bile karmaşık!
class TextProcessor {
  addText(text) {
    this.buffer += text;
  }

  getLength() {
    return this.buffer.length;
  }

  clear() {
    this.buffer = '';
  }

  getText() {
    return this.buffer;
  }
}
// Bu sınıf string'in zaten yaptığını yapıyor!
// Kullanıcıya SIFIR değer katıyor.
// Sadece "sınıf yazmış olmak" için var.
```

### Sığ Modül Hastalığı: Classitis 🤒

> **Classitis:** "Her şey bir sınıf olmalı" dogmasının yarattığı hastalık.

```java
// ❌ CLASSİTİS: Java'dan kötü bir örnek
// Bir dosyayı okumak için KAÇ SINIF lazım?
FileInputStream fileStream = new FileInputStream("data.txt");
BufferedInputStream bufferedStream = new BufferedInputStream(fileStream);
ObjectInputStream objectStream = new ObjectInputStream(bufferedStream);

// 3 sınıf, 3 satır — sadece bir dosya okumak için! 😩
// Her sınıf SIĞ (az iş yapıyor) ve kullanıcıya yük bindiriyor.

// ✅ DERİN MODÜL: Node.js yaklaşımı
const data = fs.readFileSync('data.txt', 'utf-8');
// 1 satır. Bitti. ✅
```

### Derin Modül Tasarlama Rehberi 📐

```
İyi modülün 3 özelliği:

1. BASİT INTERFACE
   → Az parametre
   → Kolay anlaşılır isim
   → Kullanıcının bilmesi gereken minimum bilgi

2. GÜÇLÜ İŞLEVSELLİK
   → Karmaşıklığı İÇERİDE gizler
   → Kullanıcının düşünmesi gereken şeyleri azaltır
   → "Benim yerime sen düşün" der

3. SOYUTLAMA
   → Implementation detayları DIŞARİDA görünmez
   → İçerideki değişiklikler dışarıyı ETKİLEMEZ
```

```javascript
// ✅ DERİN MODÜL ÖRNEĞI: Bir HTTP client
// Kullanıcı sadece şunu yapar:
const users = await api.get('/users');

// Arkada neler oluyor (kullanıcı bilmiyor ve BİLMESİ GEREKMEYEN):
// - Base URL ekleme
// - Authentication header ekleme
// - JSON serialization/deserialization
// - Timeout yönetimi
// - Retry mantığı (exponential backoff)
// - Circuit breaker
// - Request/Response logging
// - Error normalization
// - Cache kontrolü
```

### Clean Code ile Çelişki mi? 🤔

Clean Code: "Fonksiyonlar 5 satır olsun!"
Ousterhout: "Bu SIĞ modüller üretir!"

```javascript
// Clean Code yaklaşımı (aşırıya kaçarsa):
function processOrder(order) {
  validateOrder(order);
  calculateTotal(order);
  applyDiscount(order);
  saveToDB(order);
  sendEmail(order);
}

function validateOrder(order) { validateItems(order); validateUser(order); }
function validateItems(order) { checkItemStock(order); checkItemPrice(order); }
function checkItemStock(order) { /* 2 satır */ }
function checkItemPrice(order) { /* 2 satır */ }
// ... 15 fonksiyon, her biri 2-3 satır

// Sorun: İş akışını anlamak için 15 fonksiyonu takip etmen lazım!
// Her fonksiyon SO SIĞDIR ki tek başına anlamı yok.
// Kodu "anlamak" için kafanda 15 parçayı birleştirmen gerekiyor.
```

```javascript
// Ousterhout yaklaşımı:
function processOrder(order) {
  // Validasyon
  if (!order.items?.length) throw new ValidationError('Sepet boş');
  for (const item of order.items) {
    const stock = await inventory.getStock(item.id);
    if (stock < item.quantity) {
      throw new ValidationError(`${item.name} stokta yok`);
    }
  }

  // Hesaplama
  let total = order.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  if (order.coupon) {
    total *= (1 - order.coupon.discount);
  }

  // Kayıt ve bildirim
  const savedOrder = await db.orders.insert({ ...order, total });
  await emailService.sendConfirmation(savedOrder);

  return savedOrder;
}

// 30 satır AMA her şey TEK YERDE. Akışı anlamak için
// başka yere gitmeye gerek yok. Okunabilir, takip edilebilir.
```

> **Denge noktası:** Ne 200 satırlık canavar fonksiyon, ne de 2 satırlık 50 tane anlamsız fonksiyon. **Her fonksiyon anlamlı bir soyutlama sunmalı.**

---

## 5. 🔒 Bilgi Sızıntısı ve Bilgi Gizleme

### Bilgi Gizleme (Information Hiding) = En Temel Prensip 🏗️

> **"Bir modülün implementation detayları, diğer modüllerden GİZLENMELİDİR."**

Bu, David Parnas'ın 1972'deki ünlü makalesinden gelen bir kavram ve yazılım tasarımının TEMELİDİR.

```javascript
// ✅ BİLGİ GİZLEME: Dış dünya "nasıl" bilmiyor
class PasswordHasher {
  hash(plainPassword) {
    // İçeride bcrypt, argon2, scrypt... ne kullanıldığı GİZLİ
    return bcrypt.hashSync(plainPassword, 12);
  }

  verify(plainPassword, hashedPassword) {
    return bcrypt.compareSync(plainPassword, hashedPassword);
  }
}

// Yarın bcrypt'ten argon2'ye geçiş:
// → SADECE bu sınıf değişir
// → Dışarıdaki hiçbir kod etkilenmez ✅
```

### Bilgi Sızıntısı (Information Leakage) = Ana Tehlike 💧

Bilgi sızıntısı, bir modülün implementation detaylarının dışarıya **sızması**dır.

```javascript
// ❌ BİLGİ SIZINTISI: Dış dünya veritabanı yapısını biliyor
app.get('/users/:id', async (req, res) => {
  // SQL sorgusunun yapısı, tablo adları, sütun adları
  // hepsi CONTROLLER'da görünüyor → BİLGİ SIZINTISI!
  const result = await db.query(
    `SELECT u.first_name, u.last_name, u.email_addr,
            a.street_name, a.city_name, a.zip_code
     FROM app_users u
     LEFT JOIN user_addresses a ON u.user_id = a.user_id
     WHERE u.user_id = $1 AND u.is_deleted = false`,
    [req.params.id]
  );
  res.json(result.rows[0]);
});

// Tablo adı değişirse? → Controller değişmeli
// Sütun adı değişirse? → Controller değişmeli
// Soft delete mantığı değişirse? → Controller değişmeli
// DB'den başka bir DB'ye geçersen? → Controller değişmeli
// 😱 Her şey birbirine bağlı!
```

```javascript
// ✅ BİLGİ GİZLEME: Controller veritabanını bilmiyor
app.get('/users/:id', async (req, res) => {
  const user = await userService.getById(req.params.id);
  if (!user) throw new NotFoundError();
  res.json(user);
});

// userService.js
async function getById(id) {
  return userRepository.findById(id);
}

// userRepository.js  ← SQL BİLGİSİ SADECE BURADA
async function findById(id) {
  const result = await db.query(
    `SELECT ... FROM app_users WHERE user_id = $1 AND is_deleted = false`,
    [id]
  );
  return mapToUser(result.rows[0]);
}
```

### Bilgi Sızıntısının Türleri 💧💧💧

#### 1. Temporal Decomposition (Zamansal Ayrıştırma)

Kodu **ne zaman çalıştığına** göre ayırmak, genellikle bilgi sızıntısına yol açar:

```javascript
// ❌ ZAMANSAL AYRIŞTIRMA: Dosya formatı bilgisi İKİ yere sızmış
// readFile.js — "Okuma zamanında" çalışır
function readConfig(path) {
  const content = fs.readFileSync(path, 'utf-8');
  const lines = content.split('\n');
  const config = {};
  for (const line of lines) {
    const [key, value] = line.split('=');  // Format bilgisi: key=value
    config[key.trim()] = value.trim();
  }
  return config;
}

// writeFile.js — "Yazma zamanında" çalışır
function writeConfig(path, config) {
  const lines = Object.entries(config)
    .map(([key, value]) => `${key}=${value}`);  // Aynı format bilgisi tekrar!
  fs.writeFileSync(path, lines.join('\n'));
}

// FORMAT BİLGİSİ (key=value, newline separator) İKİ DOSYAYA SIZMIŞ!
// Format değişirse? İKİ dosyayı da değiştir!
```

```javascript
// ✅ DOĞRU: Format bilgisi TEK YERDE
class ConfigFile {
  #path;
  #separator = '=';
  #lineBreak = '\n';

  constructor(path) {
    this.#path = path;
  }

  read() {
    const content = fs.readFileSync(this.#path, 'utf-8');
    const config = {};
    for (const line of content.split(this.#lineBreak)) {
      const [key, value] = line.split(this.#separator);
      config[key.trim()] = value.trim();
    }
    return config;
  }

  write(config) {
    const content = Object.entries(config)
      .map(([k, v]) => `${k}${this.#separator}${v}`)
      .join(this.#lineBreak);
    fs.writeFileSync(this.#path, content);
  }
}
// Format bilgisi TEK SINIFTA. Değişirse TEK YERİ değiştir. ✅
```

#### 2. Interface Üzerinden Sızıntı

```javascript
// ❌ Interface üzerinden sızıntı: Çağıran, B-tree olduğunu BİLMEK zorunda
class BTreeIndex {
  insertNode(key, value, leafLevel) { ... }
  rebalanceAfterInsert(node) { ... }
  splitNode(node) { ... }
}
// Kullanıcı B-tree'nin iç yapısını bilmek zorunda!

// ✅ Soyutlanmış interface: Kullanıcı veri yapısını bilmiyor
class Index {
  put(key, value) { ... }
  get(key) { ... }
  delete(key) { ... }
}
// B-tree mi, Hash map mi, LSM tree mi? Kullanıcıyı İLGİLENDİRMEZ!
```

### 🧠 Akılda Kalası Kontrol Sorusu

Bir modül tasarlarken kendine sor:

> **"Bu modülü kullanan kişi, içeride NE olduğunu bilmek zorunda mı?"**
> - Evet → İnformation leakage var! Düzelt! 🔧
> - Hayır → Güzel, bilgi iyi gizlenmiş ✅

---

## 6. 🌍 Genel Amaçlı Modüller

### Somewhat General-Purpose 🎯

> **"Bugünün ihtiyacını karşıla, ama yarının ihtiyacını da KOLAYLAŞTIR."**

YAGNI (ihtiyacın olmayacak) ile overengineering arasında bir denge noktası var. Ousterhout buna **"somewhat general-purpose"** (bir miktar genel amaçlı) diyor.

```javascript
// ❌ ÇOK SPESIFIK: Sadece bugünün ihtiyacını karşılıyor
function sendWelcomeEmailToNewUser(user) {
  const subject = 'Hoş geldiniz!';
  const body = `Merhaba ${user.name}, aramıza hoş geldiniz!`;
  smtp.send(user.email, subject, body);
}

// Yarın "şifre sıfırlama emaili" lazım olunca? → Yeni fonksiyon yaz
// Yarın "sipariş onay emaili" lazım olunca? → Yine yeni fonksiyon yaz
// Her seferinde SMTP detaylarını tekrarla... 😩
```

```javascript
// ❌ ÇOK GENEL: İhtiyaç olmayan karmaşıklık
class UniversalCommunicationPlatform {
  send(channel, template, variables, options = {}) {
    // Email, SMS, Push, WhatsApp, Telegram, pigeon mail...
    // Template engine, retry, queue, scheduling, A/B testing...
    // 500 satır kod, henüz sadece 1 email gönderiyorsun!
  }
}

// YAGNI! Henüz SMS bile kullanmıyorsun!
```

```javascript
// ✅ BİR MİKTAR GENEL AMAÇLI: Bugünü çözer, yarını kolaylaştırır
class EmailSender {
  async send({ to, subject, body, html = null }) {
    // SMTP detayları gizli
    // Format (text/html) esnek
    // Kime, ne gönderilecek: parametrik
    return smtp.send({ to, subject, text: body, html });
  }
}

// Kullanım: Her tür email için kullanılabilir
await emailSender.send({
  to: user.email,
  subject: 'Hoş geldiniz!',
  body: `Merhaba ${user.name}!`
});

await emailSender.send({
  to: user.email,
  subject: 'Şifre sıfırlama',
  body: `Kodunuz: ${code}`
});
```

### Genel Amaçlı mı, Özel Amaçlı mı? Karar Rehberi 🤔

Kendine şu soruları sor:

```
1. "Bu interface'i bugünkü kullanımımın detaylarını bilmeden
    tasarlayabilir miyim?"
   → Evet ise, doğru soyutlama seviyesindesin ✅

2. "Bu fonksiyon bugünkü kullanım senaryosuna özgü terimler
    içeriyor mu?"
   → İçeriyorsa, çok spesifik → Genelleştir

3. "Bu genel yapıyı şu an kullanmadığım senaryolar için
    mi inşa ediyorum?"
   → Evet ise, YAGNI → Sadeleştir
```

**Zor soru: Metin editörü geliştiriyorsun. Bir "selection" modülü tasarlıyorsun.**

```javascript
// ❌ ÇOK SPESİFİK — Sadece "karakter seçimi" için çalışır
function selectCharacters(startIndex, endIndex) { ... }

// ❌ ÇOK GENEL — "Herhangi bir veri setinden seçim" (gereksiz)
function selectFromDataset(dataset, dimensions, selectionAlgorithm, ...) { ... }

// ✅ BİR MİKTAR GENEL — Karakter, kelime, satır, blok seçimi
class Selection {
  constructor(anchor, extent) {
    this.anchor = anchor;  // Seçim başlangıç pozisyonu
    this.extent = extent;  // Seçim bitiş pozisyonu
  }

  contains(position) { ... }
  getText(document) { ... }
  expand(unit) { ... }  // unit: 'char', 'word', 'line'
}
// Bugün sadece karakter seçimi kullanıyorsun AMA
// yapı kelime/satır seçimini de KOLAYLAŞTIRIR
```

---

## 7. 🪜 Katmanlar Arası Soyutlama

### Pass-Through Methods = Kırmızı Bayrak 🚩

Bir fonksiyon/metod, aldığı parametreleri aynen bir alt katmana iletiyorsa ve **kendisi hiçbir iş yapmıyorsa**, bu bir **pass-through method**dir ve genellikle gereksizdir.

```javascript
// ❌ PASS-THROUGH: Bu katman sıfır değer katıyor
class UserController {
  getUser(id) {
    return this.userService.getUser(id);  // Sadece iletme
  }
}

class UserService {
  getUser(id) {
    return this.userRepository.getUser(id);  // Sadece iletme
  }
}

class UserRepository {
  getUser(id) {
    return db.query('SELECT * FROM users WHERE id = $1', [id]);  // Gerçek iş
  }
}

// 3 katman, ama sadece 1'i iş yapıyor!
// UserController ve UserService boş birer kabuk.
```

**Çözüm seçenekleri:**

```javascript
// ÇÖZÜM 1: Katmanı kaldır (basit durumlarda)
class UserController {
  getUser(id) {
    return db.query('SELECT * FROM users WHERE id = $1', [id]);
  }
}
// 1 katman sildik. Daha basit! ✅
// Ama dikkat: Büyük projelerde business logic eklenecekse katman gerekli

// ÇÖZÜM 2: Katmana gerçek sorumluluk ver
class UserService {
  async getUser(id) {
    const user = await this.userRepository.findById(id);

    if (!user) throw new NotFoundError();   // İş kuralı
    if (user.isBanned) throw new ForbiddenError(); // İş kuralı

    const enrichedUser = await this.enrichWithProfile(user); // Zenginleştirme
    return this.sanitize(enrichedUser);     // Hassas verileri temizle
  }
}
// Artık BU katman gerçek İŞ yapıyor ✅
```

### Pass-Through Variables = Başka Bir Kırmızı Bayrak 🚩

Bir değişken, birçok katmandan geçip sadece en altta kullanılıyorsa:

```javascript
// ❌ PASS-THROUGH VARIABLE: requestId 4 katmandan geçiyor
function handleRequest(requestId, data) {
  processOrder(requestId, data);
}

function processOrder(requestId, data) {
  validateOrder(requestId, data);
}

function validateOrder(requestId, data) {
  logValidation(requestId, data);
}

function logValidation(requestId, data) {
  logger.info(`Validating`, { requestId });  // Sadece burada kullanılıyor!
}
```

```javascript
// ✅ ÇÖZÜM: Context nesnesi veya AsyncLocalStorage kullan
const { AsyncLocalStorage } = require('async_hooks');
const requestContext = new AsyncLocalStorage();

// Middleware'de context başlat
app.use((req, res, next) => {
  requestContext.run({ requestId: req.id }, next);
});

// Her yerde context'e eriş (parametre geçmeye gerek yok!)
function logValidation(data) {
  const { requestId } = requestContext.getStore();
  logger.info('Validating', { requestId });
}
```

### Her Katman Yeni Bir Soyutlama Sunmalı 📊

```
✅ İYİ KATMANLAMA:

Controller:  HTTP → İş nesnesi dönüşümü (request → domain)
Service:     İş kuralları, akış kontrolü, orkestrasyon
Repository:  Veri erişimi, SQL, cache
Database:    Fiziksel depolama

Her katman FARKLI bir dilde konuşuyor!
Controller: HTTP terimleri (req, res, status)
Service:    İş terimleri (order, payment, discount)
Repository: Veri terimleri (query, insert, index)
```

```
❌ KÖTÜ KATMANLAMA:

Controller:  user.name → user.name (aynen ilet)
Service:     user.name → user.name (aynen ilet)
Repository:  user.name → user.name (aynen ilet)
Database:    user.name

3 katman ama hepsi AYNI DİLDE konuşuyor!
Soyutlama yok, sadece bürokrasi var.
```

---

## 8. ⬇️ Karmaşıklığı Aşağı Çek

### Pull Complexity Downward 📥

> **"Bir modül basit bir interface sunmak için içeride karmaşık olabilir. Bu İYİDİR."**

Felsefe: Karmaşıklığı **kullanıcıdan (caller)** al, **uygulayıcının (implementer)** içine göm.

**Neden?** Bir modül 1 kez yazılır ama N kez kullanılır. Karmaşıklığı modülün içine koymak, N kullanıcıyı basitleştirir.

```
Kullanıcı sayısı = N (çok), Uygulayıcı = 1

Karmaşıklık kullanıcıda ise:  N kişi × karmaşıklık = ÇOK KÖTÜ
Karmaşıklık uygulayıcıda ise: 1 kişi × karmaşıklık = İDAREE EDİLEBİLİR
```

```javascript
// ❌ Karmaşıklık KULLANICIDA: Kullanıcı retry, timeout, error handling yapıyor
async function getUser(id) {
  let attempts = 0;
  while (attempts < 3) {
    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 5000);

      const response = await fetch(`/api/users/${id}`, {
        signal: controller.signal,
        headers: { 'Authorization': `Bearer ${getToken()}` }
      });

      clearTimeout(timeout);

      if (!response.ok) {
        if (response.status === 429) {
          await sleep(Math.pow(2, attempts) * 1000);
          attempts++;
          continue;
        }
        throw new Error(`HTTP ${response.status}`);
      }

      return response.json();
    } catch (error) {
      attempts++;
      if (attempts >= 3) throw error;
      await sleep(1000);
    }
  }
}

// HER API çağrısında bu 30 satır tekrarlanacak! 😱
```

```javascript
// ✅ Karmaşıklık MODÜLÜN İÇİNDE: Kullanıcı sadece 1 satır yazıyor
const user = await api.get('/users/123');

// api.js — Karmaşıklık burada GİZLİ:
class ApiClient {
  async get(path) {
    return this.#request('GET', path);
  }

  async #request(method, path, body = null) {
    for (let attempt = 0; attempt < this.#maxRetries; attempt++) {
      try {
        const response = await this.#fetchWithTimeout(method, path, body);

        if (response.status === 429) {
          await this.#waitForRateLimit(attempt);
          continue;
        }

        if (!response.ok) {
          throw this.#createError(response);
        }

        return response.json();
      } catch (error) {
        if (attempt === this.#maxRetries - 1) throw error;
        await this.#sleep(this.#getBackoffTime(attempt));
      }
    }
  }

  // ... timeout, auth, retry, error handling tüm karmaşıklık burada
}

// Kullanıcı BUNLARI BİLMEK ZORUNDA DEĞİL!
// const user = await api.get('/users/123');  → Bitti! ✅
```

### Ama Dikkat: Her Zaman Aşağı Çekme! ⚠️

Eğer karmaşıklık modülün kullanım bağlamına özgüyse, onu modülün içine çekmek **yanlış** olur:

```javascript
// ❌ Karmaşıklığı yanlış yere çekme
class ApiClient {
  async getUser(id) {
    const user = await this.get(`/users/${id}`);
    // ❌ İş kuralı API client'ın içine sızmış!
    if (user.age < 18) {
      throw new Error('Kullanıcı 18 yaşından küçük');
    }
    return user;
  }
}

// ✅ İş kuralı kendi katmanında
class UserService {
  async getAdultUser(id) {
    const user = await this.api.get(`/users/${id}`);
    if (user.age < 18) {
      throw new BusinessError('Kullanıcı 18 yaşından küçük');
    }
    return user;
  }
}
```

---

## 9. 🧩 Bir Arada mı, Ayrı mı?

### Ne Zaman Birleştir? Ne Zaman Ayır? 🤔

Bu, yazılım tasarımının **en zor sorularından** biridir.

#### Birleştir (Bring Together) Eğer: 🤝

```
1. Bilgi paylaşıyorlarsa
   → Aynı veri formatını okuyup yazıyorlarsa → BİRLEŞTİR

2. Interface basitleşiyorsa
   → İki modülü birleştirmek daha basit bir API sunuyorsa → BİRLEŞTİR

3. Tekrarı azaltıyorsa
   → DRY ihlali varsa → BİRLEŞTİR

4. Birlikte kullanılıyorlarsa
   → Her zaman yan yana çağrılıyorlarsa → BİRLEŞTİR
```

```javascript
// Birlikte kullanılan fonksiyonları BİRLEŞTİR
// ❌ Her zaman ikisi de çağrılıyor
const user = await fetchUser(id);
const profile = await fetchProfile(id);
const merged = mergeUserAndProfile(user, profile);

// ✅ Tek fonksiyon
const user = await getUserWithProfile(id);
```

#### Ayır (Separate) Eğer: ✂️

```
1. Genel amaçlı bir mekanizma varsa
   → Logging, caching, authentication → AYIR (middleware olarak)

2. Bağımsız olarak değişebilirler
   → UI ve iş kuralları → AYIR

3. Biri olmadan diğeri kullanılabiliyor
   → Email gönderme ve sipariş oluşturma → AYIR

4. Farklı soyutlama seviyeleri
   → HTTP handling ve business logic → AYIR
```

### 🔴 Kırmızı Bayraklar: Yanlış Ayrılmış Kod

```javascript
// 🚩 Conjoined Methods: Birini anlamak için diğerini okuman lazım
function validateInput(data) {
  if (!data.type) return;
  // type kontrolü burada başlıyor...
  if (data.type === 'premium') {
    data._premiumFlag = true;  // 🚩 Diğer fonksiyon bunu bekliyor!
  }
}

function processInput(data) {
  if (data._premiumFlag) {  // 🚩 validateInput'un detayını BİLMEN lazım!
    applyPremiumDiscount(data);
  }
}

// İki fonksiyon aslında TEK bir iş yapıyor ama yapay olarak bölünmüş.
// Birini anlamak için diğerini de okuman ZORUNLU.
// → BİRLEŞTİR veya bilgi sızıntısını düzelt!
```

---

## 10. ⚡ Hata Yönetimi Felsefesi

### Ousterhout'un Radikal Görüşü 💥

> **"Exception'lar karmaşıklığın en büyük kaynaklarından biridir. Bunları AZALTMANIN yollarını bul."**

Bu, çoğu kitabın söylediğinin **tam tersi**! Ama mantığını dinle:

### Hata Sayısını Azaltma Stratejileri

#### 1. Hatayı Tanımından Çıkar (Define Errors Out of Existence) 🪄

```javascript
// ❌ Gereksiz hata: "Zaten silinmiş bir şeyi silmek" neden hata olsun?
function deleteUser(id) {
  const user = db.find(id);
  if (!user) {
    throw new NotFoundError('Kullanıcı bulunamadı');
    // Çağıran: try-catch yazmalı, "bulunamadı" durumunu yönetmeli
    // Peki çağıran zaten silmek istiyordu? Silindi zaten! Problem ne?
  }
  db.delete(id);
}

// ✅ Hatayı tanımdan çıkar: "Sil" = "Var olmamasını sağla"
function deleteUser(id) {
  db.deleteIfExists(id);  // Yoksa hiçbir şey yapmaz, hata FİRLATMAZ
  // İdempotent! Kaç kez çağırırsan çağır, sonuç aynı: kullanıcı yok. ✅
}
```

```javascript
// ❌ Gereksiz hata: String'in alt stringini alırken sınır dışı hata
"hello".substring(0, 100);
// Java'da: StringIndexOutOfBoundsException 💥
// JavaScript'te: "hello" (sessizce kırpar) ✅

// JavaScript'in yaklaşımı Ousterhout'a göre DAHA İYİ!
// Çünkü çağıranın string uzunluğunu bilmesine GEREK KALMIYOR.
```

> **Fikir:** Bir metod, "normal cevap" üretebiliyorsa hata fırlatmasın. Hata, sadece **gerçekten kurtarılamaz** durumlarda olsun.

#### 2. Exception Maskeleme (Exception Masking) 🎭

Düşük seviyeli kodu o hatayı **kendisi çözsün**, üste fırlatmasın.

```javascript
// ❌ Her hatayı üste fırlat
class NetworkClient {
  async send(data) {
    const response = await fetch(url, { body: data });
    if (!response.ok) throw new NetworkError(response.status);
    return response.json();
  }
}
// Çağıranın HER SEFERINDE hata yönetmesi lazım

// ✅ Hatayı içeride maskele
class NetworkClient {
  async send(data) {
    for (let i = 0; i < 3; i++) {
      try {
        const response = await fetch(url, { body: data });
        if (response.ok) return response.json();

        if (response.status === 503) {
          await this.sleep(1000 * (i + 1)); // Retry
          continue;
        }
      } catch (networkError) {
        if (i < 2) continue; // Ağ hatası, tekrar dene
      }
    }
    throw new NetworkError('3 denemeden sonra başarısız');
  }
}
// Geçici hatalar İÇERİDE çözülüyor.
// Sadece KALICI hatalar üste fırlatılıyor. ✅
```

#### 3. Exception Birleştirme (Exception Aggregation) 📦

Birçok yerde aynı tür hatayı yönetmek yerine, TEK YERDE yönet.

```javascript
// ❌ Her endpoint'te ayrı ayrı hata yönetimi
app.get('/users/:id', async (req, res) => {
  try {
    const user = await userService.getById(req.params.id);
    res.json(user);
  } catch (error) {
    if (error instanceof NotFoundError) res.status(404).json({ error: error.message });
    else if (error instanceof ValidationError) res.status(400).json({ error: error.message });
    else res.status(500).json({ error: 'Internal error' });
  }
});

app.get('/orders/:id', async (req, res) => {
  try {
    const order = await orderService.getById(req.params.id);
    res.json(order);
  } catch (error) {
    // AYNI hata yönetimi TEKRAR! 😩
    if (error instanceof NotFoundError) res.status(404).json({ error: error.message });
    else if (error instanceof ValidationError) res.status(400).json({ error: error.message });
    else res.status(500).json({ error: 'Internal error' });
  }
});

// ✅ TEK YERDE hata yönetimi (error handling middleware)
app.get('/users/:id', async (req, res) => {
  const user = await userService.getById(req.params.id); // Hata fırlatabilir
  res.json(user);
});

app.get('/orders/:id', async (req, res) => {
  const order = await orderService.getById(req.params.id); // Hata fırlatabilir
  res.json(order);
});

// Tüm hatalar TEK YERDE yakalanır:
app.use((error, req, res, next) => {
  if (error instanceof NotFoundError) return res.status(404).json({ error: error.message });
  if (error instanceof ValidationError) return res.status(400).json({ error: error.message });
  logger.error(error);
  res.status(500).json({ error: 'Internal error' });
});
```

### 🧠 Akılda Kalası Özet

> **"Hata fırlatmak BEDAVA değildir. Her exception, sisteme karmaşıklık ekler."**
> - Mümkünse hatayı **tanımdan çıkar** (idempotent davranış)
> - Mümkünse hatayı **içeride çöz** (maskeleme)
> - Kaçınılmaz hataları **tek yerde yönet** (birleştirme)

---

## 11. 🔄 Tasarımda İki Kez Düşün

### Design it Twice ✌️

> **"Her tasarım kararında EN AZ İKİ farklı yaklaşım düşün."**

Bu, overengineering DEĞİL. Bu, **daha iyi kararlar vermek**.

```
Görev: Kullanıcı bildirimleri sistemi

Yaklaşım A: Polling
  → Client her 5 saniyede sunucuya sorar
  + Basit implementasyon
  - Gereksiz trafik, gecikme

Yaklaşım B: WebSocket
  → Gerçek zamanlı, sunucu push eder
  + Anlık bildirim
  - Bağlantı yönetimi karmaşık

Yaklaşım C: Server-Sent Events (SSE)
  → Sunucudan tek yönlü akış
  + WebSocket'tan basit, polling'den verimli
  - Sadece sunucu → client iletişimi

KARŞILAŞTIR:
┌─────────┬──────────┬──────────┬──────────┐
│         │ Polling  │WebSocket │   SSE    │
├─────────┼──────────┼──────────┼──────────┤
│ Basitlik│   ✅✅    │    ⚠️    │    ✅    │
│ Gerçek  │   ❌     │   ✅✅    │    ✅    │
│ zamanlı │          │          │          │
│ Ölçekle │   ❌     │    ⚠️    │    ✅    │
│ nebilir │          │          │          │
└─────────┴──────────┴──────────┴──────────┘

→ Bu senaryoda SSE en iyi denge! (Basit + gerçek zamanlı)
```

### Neden İki Kez?

1. **İlk fikrin nadiren en iyi fikirdir**
2. Karşılaştırma yapmadan bir yaklaşımın iyi mi kötü mü olduğunu bilemezsin
3. **Trade-off'ları** ancak alternatifler olduğunda görebilirsin
4. Bazen iki yaklaşımın **kükreyişimi** en iyi çözümü verir

> **Her büyük tasarım kararında:** "Bunu başka nasıl yapabilirim?" diye sor. En az 2 seçenek düşün, karşılaştır, sonra seç.

---

## 12. 📝 Neden Yorum Yazmak ÖNEMLİDİR

### Clean Code ile En Büyük Çelişki! 🔥

Clean Code: "İyi kod yoruma ihtiyaç duymaz."
Ousterhout: **"Bu tehlikeli bir yanılgıdır!"**

### Ousterhout'un Argümanı 🎯

```
Kod ne YAPTIĞINI söyler.
Yorum NEDEN yapıldığını söyler.

Bu iki bilgi FARKLIDIR ve biri diğerinin yerini ALAMAZ!
```

```javascript
// Kod
if (retryCount > 3) {
  await sleep(30000);
}

// Bu kodu okuyunca ne anlıyorsun?
// "3 denemeden sonra 30 saniye bekle"
// Ama NEDEN? Bilmiyorsun!

// Yorum ile:
// Rate limiting API'sı 3 başarısız denemeden sonra 30 saniyelik
// cooldown periyodu uyguluyor. Bu süre API dokümantasyonunda belirtilmiş.
// Ref: https://api.example.com/docs/rate-limiting
if (retryCount > 3) {
  await sleep(30000);
}

// Şimdi NEDEN 30 saniye olduğunu, NEDEN 3 deneme olduğunu BİLİYORSUN.
// Bu bilgi koddan ÇIKARILAMAZ!
```

### Yorum Türleri 📋

#### 1. Interface Yorumları (EN ÖNEMLİ!) 📘

Bir fonksiyon/sınıf/modülün **ne yaptığını** ve **nasıl kullanılacağını** anlatan yorum.

```javascript
/**
 * Verilen kullanıcı için uygulanabilir en yüksek indirimi hesaplar.
 *
 * İndirim önceliği: Kupon > Üyelik > Kampanya
 * Birden fazla indirim uygulanmaz, en yüksek olan seçilir.
 *
 * @param {string} userId — İndirim hesaplanacak kullanıcının ID'si
 * @param {Array<CartItem>} items — Sepetteki ürünler
 * @returns {number} İndirim oranı (0-1 arası, örn: 0.2 = %20)
 * @throws {NotFoundError} Kullanıcı bulunamazsa
 *
 * @example
 * const discount = await calculateBestDiscount('user-123', cartItems);
 * const finalPrice = totalPrice * (1 - discount);
 */
async function calculateBestDiscount(userId, items) { ... }
```

> **Yorum olmadan** bu fonksiyonu doğru kullanmak için implementation'ı okumanız lazım. Bu çok **zaman kaybı!**

#### 2. Implementation Yorumları (Ne ve Neden!) 🔍

Kodun içindeki karmaşık mantığı açıklayan yorumlar.

```javascript
async function rebalancePartitions(shards) {
  // Shard'ları yük durumuna göre yeniden dengele.
  // Greedy algoritma: En yüklü shard'dan en boş shard'a eleman taşı.
  //
  // Neden tam optimal değil: NP-hard olan bin packing probleminin
  // yaklaşık çözümü. Tam optimal çözüm 100+ shard'da dakikalar sürer,
  // bu yaklaşım milisaniyede sonuç verir ve pratikte %95+ optimal.
  //
  // Alternatif olarak consistent hashing düşünüldü ama mevcut
  // altyapımızla uyumlu değildi (bkz: ADR-042).

  const sorted = shards.sort((a, b) => b.load - a.load);
  // ... implementasyon
}
```

#### 3. Cross-Module Yorumları 🔗

Farklı modüller arasındaki bağımlılıkları açıklayan yorumlar.

```javascript
// ⚠️ DİKKAT: Bu alan değiştirilirse, aşağıdaki yerlerin de güncellenmesi gerekir:
// - src/services/billing.js → calculateInvoice() fonksiyonu
// - src/migrations/20240315_add_tax_rate.js → migration
// - docs/api/pricing.md → API dokümantasyonu
const TAX_RATE = 0.18;
```

### Kötü Yorumlar Hâlâ Kötü ❌

Ousterhout de her yorumu savunmuyor! Kötü yorum türleri:

```javascript
// ❌ Kodu tekrarlayan yorum
i++; // i'yi artır

// ❌ Belirsiz yorum
// Bazı şeyleri burada yapıyoruz

// ❌ Güncelliğini yitirmiş yorum (en tehlikeli!)
// Kullanıcının yaşını kontrol eder
function checkEmail(user) { ... } // 😱 Yalan söylüyor!
```

### Yorum Yazma Kontrol Listesi ✅

```
Yorum yaz eğer:
  □ Tasarım kararının NEDEN'ini açıklıyorsa
  □ Bir sınıf/fonksiyon/modülün interface'ini tanımlıyorsa
  □ Bilinen bir sınırlama veya TODO varsa
  □ Şaşırtıcı bir davranış varsa
  □ Performans kararının gerekçesi varsa
  □ Cross-module bağımlılık varsa

Yorum yazma eğer:
  □ Kodu tekrarlıyorsa (i++ → i'yi artır)
  □ Kötü isimlendirmenin bahanesi ise
  □ Güncel kalmayacağından eminsen
```

### Yorum = Tasarım Aracı 🛠️

Ousterhout'un harika bir önerisi:

> **"Kodu yazmadan ÖNCE yorum yaz."**

```javascript
// ADIM 1: Önce yorumlarla tasarla
/**
 * Sepetteki ürünlerin toplam fiyatını hesaplar.
 * İndirimler uygulanır, kargo ücreti eklenir.
 * 200 TL üzeri siparişlerde kargo ücretsiz.
 */
function calculateCartTotal(items, coupon) {
  // TODO: Ürün fiyatlarını topla

  // TODO: Kupon varsa indirimi uygula

  // TODO: Kargo ücretini hesapla (200 TL üzeri ücretsiz)

  // TODO: Toplam = ürünler + kargo - indirim
}

// ADIM 2: Şimdi kodu yaz
// Yorum sana bir roadmap, bir plan verdi!
// Kodu yazarken yorumları gerçek açıklamalarla güncelle.
```

> Bu yaklaşım, **test-first** gibi bir **comment-first** metodolojisi. Önce ne yapacağını düşün (yorum yaz), sonra yap (kod yaz).

---

## 13. 📛 İsimlendirme

### Ousterhout'un İsimlendirme Felsefesi

Clean Code ile büyük oranda aynı fikirde ama birkaç ek perspektif var:

#### İsimler Belirsizlik Yaratmamalı

```javascript
// ❌ BELİRSİZ: "count" neyin count'u?
function count() { ... }

// Bağlama göre farklı anlamlar:
// count(users) → Kaç kullanıcı var?
// count(query) → Kaç sonuç var?
// count(clicks) → Kaç tıklama var?

// ✅ AÇIK: Ne sayıldığı belli
function countActiveUsers() { ... }
function countSearchResults(query) { ... }
function countPageClicks(pageId) { ... }
```

#### İsimler Tutarlı Olmalı

> **"Her zaman aynı şey için aynı kelimeyi kullan."**

```javascript
// ❌ TUTARSIZ: Aynı kavram, farklı kelimeler
function getUser() { ... }
function fetchOrder() { ... }
function retrieveProduct() { ... }
function loadCustomer() { ... }
function findInvoice() { ... }
// GET? FETCH? RETRIEVE? LOAD? FIND? 🤯

// ✅ TUTARLI: Takım sözlüğü belirle
// "Veritabanından tek kayıt getirme" = findById
// "Veritabanından liste getirme" = findAll / findBy
// "Dış servisten veri çekme" = fetch
function findUserById() { ... }
function findOrderById() { ... }
function findAllProducts() { ... }
function fetchExternalPricing() { ... }
```

#### İsim Uzunluğu ≈ Scope Büyüklüğü

```javascript
// Küçük scope → kısa isim OK
items.map(x => x.price);  // x yeterli, 1 satırlık scope

// Büyük scope → uzun, açıklayıcı isim ŞART
class OrderProcessingService {  // Geniş scope, açık isim
  async processNewOrder(orderData) { ... }
}

// Ama abartma!
class AbstractSingletonProxyFactoryBean { ... }  // 😵 Bu ne?
```

---

## 14. 🔧 Mevcut Kodu Değiştirmek

### Stratejik Yaklaşım 📐

> **"Mevcut koda dokunduğunda, onu biraz DAHA İYİ bırak."**

Ama "daha iyi" ne demek? Ousterhout'un stratejisi:

```
Bir bug fix veya feature eklerken:

1. DEĞİŞİKLİĞİ YAP — Asıl görevini tamamla

2. ETRAFINA BAK — Bu modülde:
   → Daha iyi bir isim olabilir mi?
   → Gereksiz bir yorum var mı?
   → Bilgi sızıntısı var mı?
   → Interface basitleştirilebilir mi?

3. KÜÇÜK İYİLEŞTİRMELER YAP — Ama sadece dokunduğun bölgede
   → Refactoring'i asıl değişiklikle aynı PR'a KOY
   → "Ayrı PR'da yaparım" deme, YAPMAYACAKSIN! 😅

4. BÜYÜK SORUNLARI NOT AL — Büyük refactoring gerekiyorsa
   → Ticket oluştur, plana al
   → Ama o ticket'ı da bir gün yap!
```

### Tasarım Tutarlılığını Koru ⚖️

```
Mevcut pattern varsa, ONA UY!

Projede Repository pattern kullanılıyorsa:
  → Yeni entity için de Repository yaz
  → "Ben doğrudan DB çağırırım" deme!

Projede error middleware varsa:
  → Her endpoint'te try-catch YAZMA
  → Error middleware'i kullan

Tutarsızlık, karmaşıklığın en büyük kaynağıdır!
Bir mühendis iki farklı pattern görünce:
"Hangisi doğru? Neden farklı?" → Bilişsel yük! 🧠💥
```

---

## 15. ⚡ Performans ve Tasarım

### Ousterhout'un Yaklaşımı 🏎️

> **"Performansı TASARIM aşamasında düşün, ama optimizasyonu ÖLÇÜM sonrası yap."**

#### Tasarım Seviyesinde (Erken) ✅

```
Bu kararlar sonradan değiştirilmesi ÇOK ZOR:
- Veritabanı seçimi (SQL vs NoSQL)
- Senkron vs asenkron mimari
- Monolith vs microservices
- Cache stratejisi
- Veri modeli

Bu kararları erken ve doğru ver.
```

#### Kod Seviyesinde (Geç) ✅

```
Bu kararlar sonradan değiştirilebilir:
- Hangi sort algoritması?
- HashMap mi, TreeMap mi?
- Loop içinde optimizasyon

ÖNCE ÖLÇÜM YAP, sonra optimize et!
```

#### Critical Path (Kritik Yol)

> **"Kodun %90'ı performans açısından önemsizdir. %10'unu bul ve orayı optimize et."**

```javascript
// Profiling yapmadan optimize etme!
// "Bu fonksiyon yavaş olabilir" DEĞİL → "Bu fonksiyon 500ms sürüyor" → ÖLÇÜM!

console.time('processOrder');
await processOrder(order);
console.timeEnd('processOrder');
// processOrder: 432ms ← İşte veri!

// Şimdi hangisi yavaş?
console.time('validate');
await validateOrder(order);
console.timeEnd('validate');
// validate: 12ms ← sorun burada değil

console.time('payment');
await chargePayment(order);
console.timeEnd('payment');
// payment: 380ms ← SORUN BURADA! 🎯
```

---

## 16. 📌 Trendler ve Dikkat Edilmesi Gerekenler

### Ousterhout'un Uyarıları ⚠️

Yazılım dünyasında bazı trendler faydalıdır ama **aşırıya kaçarılmamalıdır:**

| Trend | Faydası | Aşırıya Kaçarsa |
|---|---|---|
| **Küçük sınıflar / fonksiyonlar** | Okunabilirlik | Sığ modüller, classitis |
| **Test Driven Development** | Kalite | Testler tasarımı yönlendirmemeli |
| **Agile** | Esneklik | "Tasarım yapmayalım" bahanesi olmamalı |
| **Design Patterns** | Ortak dil | Her yere pattern sıkıştırmak |
| **Getters/Setters** | Kapsülleme | Gereksiz boilerplate |
| **Inheritance** | Yeniden kullanım | Derin inheritance ağaçları |

### Özellikle TDD Hakkında 🧪

> Ousterhout TDD karşıtı değil ama şunu söylüyor:

```
TDD şunu söylüyor: "Test yaz, kodu yaz, refactor et"
Ousterhout şunu ekliyor: "Ama önce TASARIMI düşün!"

❌ TDD dogması: Test → En basit kod → Refactor → Test → ...
   "Tasarım testlerden ÇIKAR!"

✅ Ousterhout: Tasarımı DÜŞÜN → Yorum yaz → Test yaz → Kod yaz → İyileştir
   "Tasarım BİLİNÇLİ bir süreçtir, tesadüfen çıkmaz!"
```

---

## 17. 🎬 Son Sözler

### Bu Kitabın Altın Kuralları 🏆

| # | İlke | Bir Cümlede |
|---|---|---|
| 1 | **Karmaşıklık düşmandır** | Her karar karmaşıklığı artırır mı azaltır mı, bunu sor |
| 2 | **Stratejik programla** | %10-20 zamanını tasarım yatırımına ayır |
| 3 | **Derin modüller yaz** | Basit interface, güçlü implementasyon |
| 4 | **Bilgiyi gizle** | Implementation detayları dışarıya sızmasın |
| 5 | **Somewhat general-purpose** | Bugünü çöz, yarını kolaylaştır |
| 6 | **Pass-through'dan kaçın** | Her katman gerçek değer katmalı |
| 7 | **Karmaşıklığı aşağı çek** | Kullanıcıyı basitleştir, modülü karmaşıklaştır |
| 8 | **Hataları azalt** | Mümkünse tanımdan çıkar, içeride çöz |
| 9 | **İki kez tasarla** | Her kararda en az 2 alternatif düşün |
| 10 | **Yorumlar değerlidir** | Neden ve ne bilgisini yorumla |
| 11 | **İsimlendirme tutarlılığı** | Aynı kavram = aynı kelime, her yerde |
| 12 | **Kademeli iyileştir** | Her dokunuşta kodu biraz daha iyi bırak |

### Clean Code vs A Philosophy of Software Design 📊

```
Clean Code okuyan:
  "Fonksiyonlar 5 satır olmalı! Yorum kötü! Sınıflar küçük!"

Philosophy okuyan:
  "Karmaşıklığı nerede azaltabilirim?
   Bu modül yeterince derin mi?
   Bu yorum gerçekten yardımcı mı?
   Bu karar bilgi sızıntısına yol açıyor mu?"

İKİSİNİ DE oku. Clean Code kuralları öğretir,
Philosophy DÜŞÜNMEYI öğretir. 🧠
```

### Öğrenme Yolculuğu 🛤️

```
📗 Grokking Algorithms          → Algoritma temeli ✅
📕 Clean Code                   → Kod kalitesi ✅
📘 The Pragmatic Programmer     → Mühendislik zihniyeti ✅
📙 The Missing README           → Kariyer temeli ✅
📗 A Philosophy of Software Design → Tasarım felsefesi ✅  ← BURADASIN

Sıradaki (Faz 2 devam):
📘 Head First Design Patterns   → Pattern'lar
📕 Designing Data-Intensive Apps → Dağıtık sistem temeli
📙 Unit Testing (Khorikov)       → Test stratejisi
📗 Refactoring (Fowler)          → Referans kitap
```

---

> **"Yazılım tasarımı bir SANAT değil, bir ZANAATtır.
> Sanatı doğuştan taşırsın, zanaatı ise PRATİKLE öğrenirsin.
> Her gün biraz daha iyi tasarla, biraz daha az karmaşıklık üret.
> Ve unutma: İyi tasarımın en büyük ödülü,
> GELECEKTE o koda döndüğünde gülümsemektir."** 😊

### 🤖 Yapay Zeka Çağında Bu Felsefe

```
Ousterhout'un temel tezi: "Karmaşıklık yavaş yavaş birikir."

AI ile bu birikim HIZLANIYOR:

1. AI = TAKTİK PROGRAMLAMA MAKİNESİ!
   → AI kod üretir, çalışır, yoldaş!
   → AMA: AI stratejik TASARIM yapmaz!
   → Ousterhout: "Taktik tornado" tehlikesi → AI bunu 10x YAPAR!
   → SEN stratejik düşünmezsen AI taktik borç üretir!

2. "DERİN MODÜLLER" AI ile DAHA ÖNEMLİ
   → AI genellikle sığ modüller üretir (küçük fonksiyonlar, çok parametre)
   → SEN bunları derin modüllere dönüştürmelisin!
   → Prompt: "Bu 5 fonksiyonu tek bir derin modüle birleştir,
     basit interface ile sarmal, detayları gizle."

3. BİLGİ SIZINTISI → AI EN ÇOK BUNU YAPAR!
   → AI kodu üretirken implementation detayını HER YERE yaydırır
   → "Bir yerde değiştirdiğinde her yeri değiştirmen gerekir" → FELAKET!
   → Ousterhout'un bilgi gizleme prensibi → AI çıktısını KONTROL ET!

4. "HATALI TANIMLARI DÜZELT" → AI API TASARIMINDA
   → AI'ın yazdığı API çok fazla hata durumu döndürebilir
   → Ousterhout: "Hatayı tanımdan çıkar" → API'yi BASİTLEŞTİR!

Özetle: AI KOD yazar, SEN TASARIM yaparsın.
Bu kitabın önemi AI çağında ARTMIŞTIR, azalmamıştır!
```

> — Bu rehberin özü: **"Karmaşıklığı azalt. Her şey bunun etrafında döner."**
