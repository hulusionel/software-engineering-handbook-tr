# 📖 The Missing README — Türkçe Kapsamlı Rehber

> **"Okulda öğretilmeyen ama işte hayatta kalman için bilmen gereken her şey."**
> — Chris Riccomini & Dmitriy Ryaboy

Bu kitap, bir yazılım mühendisinin **teknik beceriler dışında** bilmesi gereken her şeyi anlatır:
nasıl çalışılır, nasıl iletişim kurulur, nasıl büyünür, nasıl hayatta kalınır.

---

## 📖 İçindekiler

1. [İlk Gününden İtibaren (Getting Started)](#1--i̇lk-gününden-i̇tibaren)
2. [Bilinçli Yetkinlik Kazanmak](#2--bilinçli-yetkinlik-kazanmak)
3. [Kod Yazmak (Üretime Hazır Kod)](#3--kod-yazmak-üretime-hazır-kod)
4. [Yazılım Tasarımı](#4--yazılım-tasarımı)
5. [Kodu Doğru Yönetmek](#5--kodu-doğru-yönetmek)
6. [Test Yazmak](#6--test-yazmak)
7. [Kod İnceleme (Code Review)](#7--kod-i̇nceleme-code-review)
8. [Yazılımı Teslim Etmek (Delivery)](#8--yazılımı-teslim-etmek-delivery)
9. [On-Call ve Incident Yönetimi](#9--on-call-ve-incident-yönetimi)
10. [Teknik Tasarım Süreçleri](#10--teknik-tasarım-süreçleri)
11. [Kariyer Yönetimi](#11--kariyer-yönetimi)
12. [Kendini ve Başkalarını Yönetmek](#12--kendini-ve-başkalarını-yönetmek)
13. [Son Sözler](#13--son-sözler)

---

## 1. 🚀 İlk Gününden İtibaren

### Hikaye: Yeni Okul 🏫

İlk iş gününü düşün. Yeni bir okula transfer olmuş öğrenci gibisin:
- Kimseyi tanımıyorsun 😟
- Tuvaletlerin nerede olduğunu bilmiyorsun 🚻
- Herkes birbirini tanıyor, sen dışarıdan bakıyorsun 👀
- "Acaba burada da mı böyle yapılıyor?" diye her şeyi sorguluyorsun 🤔

**Bu NORMAL.** Herkes bunu yaşadı. Ve iyi haber: İlk 3 ayda çoğu şeyi çözersin.

### İlk 90 Gün Planı 📅

```
Hafta 1-2: GÖZLEMLE
├── Takımını tanı (herkesin adını ve rolünü öğren)
├── Geliştirme ortamını kur (README'yi takip et)
├── Codebase'i gezin (ana dosyalar, mimari)
├── Mevcut dokümantasyonu oku
└── Küçük bir "good first issue" al ve çöz

Hafta 3-4: SOR
├── Mentor/buddy'ni belirle
├── Onboarding dokümanı eksikse, kendin yazarak öğren
├── Takımın ritüellerini anla (standup, retro, planning)
├── Mimariyi whiteboard'da birinin anlatmasını iste
└── İlk küçük PR'ını aç

Ay 2-3: KATKILAR
├── Daha büyük görevler al
├── Code review yapmaya başla (öğrenmenin en iyi yolu!)
├── Teknik borcu (technical debt) not al
├── Takım toplantılarında sorular sor
└── İlk bağımsız feature'ını geliştir
```

### Soru Sormayı Öğren 🙋

> **"Aptalca soru yoktur, ama sormamak aptallıktır."**

Ama NASIL sorduğun önemli:

```
❌ KÖTÜ SORU:
"Bu çalışmıyor, yardım eder misin?"
→ Ne çalışmıyor? Ne denedin? Hata mesajı ne?

✅ İYİ SORU:
"User servisi çağrıldığında 401 hatası alıyorum.
Token'ı kontrol ettim, geçerli görünüyor.
Postman'de aynı token ile çalışıyor.
Header'da Bearer prefix'i eksik olabilir mi?"
→ Ne yaptığını, ne beklediğini, ne olduğunu ve ne denediğini söyledin!
```

#### Soru Sorma Şablonu 📋

```
1. Ne yapmaya çalışıyorum?
2. Ne olmasını bekliyordum?
3. Ne oldu? (Hata mesajı, screenshot)
4. Ne denedim? (En az 2-3 girişim)
5. Tahminim ne? (Kök neden ne olabilir?)
```

> **30 dakika kuralı:** Bir soruna 30 dakika uğraştıysan ve ilerleyemiyorsan, SOR. Daha fazla beklemek zaman kaybı. Daha az beklemek tembelliktir.

### Mentor İlişkisi 🧑‍🏫

| Senin Sorumluluğun | Mentorun Sorumluluğu |
|---|---|
| Toplantılara hazırlıklı gel | Zaman ayır, düzenli görüş |
| Somut sorular sor | Yön göster, bağlam ver |
| Feedback'i savunmaya geçmeden dinle | Yapıcı feedback ver |
| Öğrendiklerini uygula | İlerlemeyi takip et |
| İnisiyatif al, bekleme | Fırsatlar tanı, güçlendirme |

> **İpucu:** Mentorun yoksa, KENDİN bul. Takımda kod kalitesine önem veren, sabırlı birine yaklaş ve "Bana mentor olur musun?" de. İnsanlar genellikle memnuniyetle kabul eder.

### Yeni Başlayanın Gizli Süper Gücü 🦸

**Taze göz (Fresh eyes)!** Herkesin normal kabul ettiği garip şeyleri SEN fark edersin:

```
"Neden deploy 3 saat sürüyor?" → Herkes alışmış, ama bu anormal!
"Neden bu config el ile güncelleniyor?" → Otomatik olabilir!
"README'de X adımı eksik" → Onboarding dokümanını iyileştir!

Gördüğün sorunları NOT AL. Çözmek için acele etme, ama kaydet.
3 ay sonra bazılarını çözme fırsatın olacak.
```

---

## 2. 🎓 Bilinçli Yetkinlik Kazanmak

### Dreyfus Modeli: Yetkinlik Seviyeleri 📊

```
Seviye 1: 🟢 ÇAYLAK (Novice)
  "Tarif ver, adım adım uygulayayım"
  → Kurallara sıkı sıkıya bağlı
  → Bağlamı hesaba katamaz
  → "Bu SONAR kuralı hata veriyor, ne yapmalıyım?"

Seviye 2: 🔵 İLERİ BAŞLANGIÇ (Advanced Beginner)
  "Bazı kalıpları tanıyorum"
  → Benzer durumları fark eder
  → Hâlâ büyük resmi göremez
  → "Bu pattern Repository'e benziyor"

Seviye 3: 🟡 YETKİN (Competent)
  "Planlayabilir, önceliklendirebilirim"
  → Problem çözme yeteneği gelişmiş
  → Büyük resmi görmeye başlar
  → "Bu özelliği şu sırayla yapalım, şu riskler var"

Seviye 4: 🟠 USTA (Proficient)
  "Bağlamı anlıyorum, prensipleri uyguluyorum"
  → Kuralların NEDEN olduğunu bilir
  → Kuralları ne zaman esnetmek gerektiğini bilir
  → "Bu durumda DRY'ı ihlal etmemiz daha doğru çünkü..."

Seviye 5: 🔴 UZMAN (Expert)
  "Sezgisel olarak doğru kararı veririm"
  → Kurallar otomatikleşmiş
  → Yeni paradigmalar oluşturabilir
  → "Bu problemi daha önce görmemiştim ama doğru yaklaşım şu olmalı"
```

> **Önemli:** Her konuda farklı seviyelerde olabilirsin. JavaScript'te "Usta" olabilirsin ama Kubernetes'te "Çaylak".

### Nasıl Seviye Atlanır? 🚀

#### 1. Kasıtlı Pratik (Deliberate Practice) 🎯

```
❌ Sadece iş yapmak = Pratik DEĞİL
   (10 yıl aynı işi yapmak ≠ 10 yıllık deneyim)

✅ Kasıtlı pratik = Zayıf yönlerini bilerek çalışmak
   - Rahatsız olduğun konulara yönel
   - Feedback al
   - Tekrarla
```

| Yöntem | Açıklama |
|---|---|
| **Side project** | Tüm kararları sen veriyorsun, en hızlı öğrenme |
| **Açık kaynak katkı** | Başka insanların kodunu oku, kendi koduna feedback al |
| **Kod kataları** | Küçük egzersizler (exercism.io, codewars.com) |
| **Kitap/Makale** | Teori bilgisi |
| **Eşli programlama** | Birinden canlı olarak öğren |
| **Konferans konuşması/Blog yazısı** | Öğretmek en iyi öğrenmektir |

#### 2. T-Shaped Mühendis Ol 📐

```
   Geniş bilgi (birçok konuda yüzeysel)
   ┌──────────────────────────────┐
   │  FE  │  BE  │ DevOps │  DB  │
   │      │      │        │      │
   └──┬───┴──────┴────────┴──────┘
      │
      │  Derin uzmanlık
      │  (bir konuda derin)
      │
      │  Backend
      │  Node.js
      │  Distributed Systems
      │  API Design
      │
      ▼
```

> Bir konuda DERİN ol (uzmanlık alanın) ama diğer konularda da konuşabilecek kadar GENİŞ ol.

#### 3. Öğrenme Döngüsü 🔄

```
           ┌──→ ÖĞren ──→ UYGULA ──┐
           │                         │
           │                         ▼
        TEKRARLA              FEEDBACK AL
           │                         │
           │                         │
           └──── DÜŞÜN ←────────────┘
```

**En kritik adım: FEEDBACK.** Feedback olmadan öğrenme olmaz.
- **Kod review** = kodun hakkında feedback
- **1:1 toplantılar** = performansın hakkında feedback
- **Retrospektif** = sürecin hakkında feedback
- **Monitoring/Alerting** = sisteminiz hakkında feedback

---

## 3. 💻 Kod Yazmak (Üretime Hazır Kod)

### "Çalışan Kod" vs "Üretime Hazır Kod" 🏭

```
Çalışan Kod:                    Üretime Hazır Kod:
✅ Doğru sonucu veriyor         ✅ Doğru sonucu veriyor
                                ✅ Hataları zarif yönetiyor
                                ✅ Logları anlamlı
                                ✅ Metrikleri izlenebilir
                                ✅ Test edilmiş
                                ✅ Güvenli
                                ✅ Performansı ölçülmüş
                                ✅ Geri alınabilir (rollback)
                                ✅ Dokümante edilmiş
                                ✅ Ölçeklenebilir
```

> **Okulda:** "Çalışıyor mu? Tamam, A al."
> **İşte:** "Çalışıyor mu? Bu sadece başlangıç."

### Defansif Programlama 🛡️

```javascript
// ❌ İyimser programlama: "Her şey yolunda gidecek!"
async function getUser(id) {
  const response = await fetch(`/api/users/${id}`);
  const user = await response.json();
  return user.name.toUpperCase();
}

// ✅ Defansif programlama: "Her şey ters gidebilir!"
async function getUser(id) {
  if (!id) {
    throw new ValidationError('User ID gerekli');
  }

  let response;
  try {
    response = await fetch(`/api/users/${id}`);
  } catch (error) {
    throw new ServiceError(`User servisi erişilemez: ${error.message}`);
  }

  if (!response.ok) {
    if (response.status === 404) {
      throw new NotFoundError(`Kullanıcı bulunamadı: ${id}`);
    }
    throw new ServiceError(`User servisi hata döndü: ${response.status}`);
  }

  const user = await response.json();

  if (!user?.name) {
    logger.warn('Kullanıcının adı boş', { userId: id });
    return 'Bilinmeyen';
  }

  return user.name.toUpperCase();
}
```

### Logging: Geleceğe Mektup Yazmak 📝

Log, gelecekte bir hatayı araştıran birine (muhtemelen sana!) bıraktığın izlerdir.

```javascript
// ❌ KÖTÜ LOGLAR
console.log('buraya geldi');          // Nereye geldi?
console.log('hata');                   // Ne hatası?
console.log(user);                     // Bu obje ne? Neden loglanıyor?
console.log('girdi', data);            // Hassas veri mi var içinde?

// ✅ İYİ LOGLAR
logger.info('Sipariş oluşturma başladı', {
  userId: order.userId,
  itemCount: order.items.length,
  totalAmount: order.total
});

logger.error('Ödeme başarısız', {
  orderId: order.id,
  userId: order.userId,
  errorCode: paymentResult.code,
  errorMessage: paymentResult.message,
  // ❌ Kart numarası, CVV gibi hassas bilgi ASLA loglanma!
});

logger.warn('Stok azaldı', {
  productId: product.id,
  remainingStock: product.stock,
  threshold: MIN_STOCK_ALERT
});
```

#### Log Seviyeleri 📊

| Seviye | Ne Zaman Kullanılır | Örnek |
|---|---|---|
| **ERROR** | Bir şey KIRILDI, müdahale gerek | DB bağlantısı koptu, ödeme başarısız |
| **WARN** | Şüpheli ama kırık değil | Rate limit'e yaklaşıldı, cache miss oranı yüksek |
| **INFO** | Normal ama önemli işlemler | Kullanıcı girişi, sipariş oluşturma, deploy |
| **DEBUG** | Geliştirme sırasında detay | Fonksiyon parametreleri, ara adımlar |

> **Kural:** Production loglarını okuyarak sistemin ne yaptığını **hikaye gibi** anlayabilmen lazım.

### Yapılandırma Yönetimi ⚙️

```javascript
// ❌ KÖTÜ: Hardcoded değerler
const TIMEOUT = 5000;
const MAX_RETRIES = 3;
const API_URL = 'https://api.production.com';
const DB_PASSWORD = 'supersecret123';  // 🚨 ASLA!

// ✅ İYİ: Ortam değişkenlerinden
const config = {
  timeout: parseInt(process.env.TIMEOUT) || 5000,
  maxRetries: parseInt(process.env.MAX_RETRIES) || 3,
  apiUrl: process.env.API_URL || 'http://localhost:3000',
  dbPassword: process.env.DB_PASSWORD,  // Vault/secret manager'dan
};

// Uygulama başlarken validasyon
function validateConfig(config) {
  const required = ['apiUrl', 'dbPassword'];
  const missing = required.filter(key => !config[key]);

  if (missing.length > 0) {
    throw new Error(`Eksik yapılandırma: ${missing.join(', ')}`);
  }
}
```

### Metrikler: Bilmediğini Bilemezsin 📈

```javascript
// İş metrikleri (Business metrics)
metrics.increment('orders.created');
metrics.histogram('order.total_amount', order.total);
metrics.gauge('active_users.count', activeUsers);

// Teknik metrikler (Technical metrics)
const startTime = Date.now();
const result = await processOrder(order);
metrics.histogram('order.processing_duration_ms', Date.now() - startTime);

metrics.increment('http.requests', { method: 'POST', path: '/orders', status: 201 });
metrics.increment('db.queries', { operation: 'INSERT', table: 'orders' });
```

> **"Ölçemediğin şeyi iyileştiremezsin."** — Peter Drucker

---

## 4. 🏛️ Yazılım Tasarımı

### Karmaşıklık İki Türdür 🧩

#### 1. Essential Complexity (Zorunlu Karmaşıklık)
İş kuralının kendisinden gelen karmaşıklık. Kaçınılmaz.

```
"Vergi hesaplama" zor bir iştir çünkü:
- Her ülkenin farklı vergi kuralı var
- Ürün kategorisine göre vergi oranı değişir
- İndirimler vergiye nasıl uygulanır?
Bu karmaşıklık İŞİN KENDİSİNDEN gelir, koddan değil.
```

#### 2. Accidental Complexity (Yanlışlıkla Eklenen Karmaşıklık)
Kötü tasarım, yanlış araç seçimi, gereksiz soyutlamalardan gelen karmaşıklık. Kaçınılabilir!

```javascript
// ❌ Accidental complexity: Basit bir işi karmaşıklaştırmak
class UserNameFormatterFactory {
  static createFormatter(type) {
    switch(type) {
      case 'upper': return new UpperCaseFormatter();
      case 'lower': return new LowerCaseFormatter();
      default: return new DefaultFormatter();
    }
  }
}

class UpperCaseFormatter {
  format(name) { return name.toUpperCase(); }
}
// ... 50 satır daha kod

// ✅ Yeterli: Basit bir fonksiyon
function formatUserName(name, style = 'upper') {
  return style === 'upper' ? name.toUpperCase() : name.toLowerCase();
}
```

> **Hedeffin:** Zorunlu karmaşıklığı yönet, yanlışlıkla eklenen karmaşıklığı yok et.

### YAGNI — You Aren't Gonna Need It 🚫

> **"İhtiyacın olmayacak. Yapma."**

```javascript
// ❌ "İleride lazım olur" sendromu
class UserService {
  getUser(id) { ... }
  getUserByEmail(email) { ... }
  getUserByPhone(phone) { ... }          // Hiç kullanılmadı
  getUserBySSN(ssn) { ... }              // Hiç kullanılmadı
  getUserByFingerprint(fp) { ... }       // Hiç kullanılmadı
  getUserByRetinaScan(scan) { ... }      // Bu ne?? 😂
  getUsersByBloodType(type) { ... }      // NASA mı burası?
}

// ✅ Sadece ŞUAN ihtiyacın olanı yaz
class UserService {
  getUser(id) { ... }
  getUserByEmail(email) { ... }
  // İhtiyaç olduğunda ekleriz. KISS!
}
```

> **İstatistik:** "İleride lazım olur" diye yazılan kodun **%60-80'i** asla kullanılmaz.
> Bu da demek oluyor ki zamanının çoğunu **gereksiz kod yazmakla** geçiriyorsun! 💸

### KISS — Keep It Simple, Stupid 💋

```javascript
// ❌ Karmaşık: "Look ma, how clever I am!"
const isEven = n => !(n & 1) ? (() => true)() : (() => false)();

// ✅ Basit: Herkes anlıyor
const isEven = n => n % 2 === 0;

// ❌ "Akıllı" çözüm
const getInitials = name =>
  name.split(/\s+/).reduce((acc, word) =>
    acc + word.charAt(0).toUpperCase(), '');

// ✅ Okunabilir çözüm
function getInitials(fullName) {
  const words = fullName.split(' ');
  return words
    .map(word => word[0].toUpperCase())
    .join('');
}
```

> **"Herkesin anlayacağı kodu yaz, sadece dahilerin anlayacağı kodu değil."**

### Soyutlama Seviyeleri 🪆

```
Ne kadar soyut?

Çok somut: SQL sorgusu yazıyorsun
  ↓
Biraz soyut: Repository fonksiyonu çağırıyorsun
  ↓
Daha soyut: Service fonksiyonu çağırıyorsun
  ↓
  Çok soyut: "Kullanıcıyı getir" diyorsun

Her seviyede SADEce o seviyenin detaylarıyla ilgilenmelisin.
```

```javascript
// Her seviye kendi soyutlamasında kalıyor:

// Controller seviyesi (yüksek soyutlama)
async function handleGetUser(req, res) {
  const user = await userService.getById(req.params.id);
  res.json(user);
}

// Service seviyesi (orta soyutlama)
async function getById(id) {
  const user = await userRepository.findById(id);
  if (!user) throw new NotFoundError('Kullanıcı bulunamadı');
  return sanitizeUser(user);
}

// Repository seviyesi (düşük soyutlama)
async function findById(id) {
  const result = await db.query('SELECT * FROM users WHERE id = $1', [id]);
  return result.rows[0] || null;
}
```

### API Tasarımı: Diğer Geliştiriciler Senin Müşterin 🤝

```javascript
// ❌ KÖTÜ API: Kullanıcı ne yapacağını bilemiyor
POST /api/do?action=getUser&id=5
POST /api/do?action=deleteUser&id=5
// Her şey POST, action parametresine göre farklı iş... RESTful değil!

// ✅ İYİ API: RESTful, sezgisel, tutarlı
GET    /api/users        → Tüm kullanıcıları listele
GET    /api/users/5      → ID=5 kullanıcıyı getir
POST   /api/users        → Yeni kullanıcı oluştur
PUT    /api/users/5      → Kullanıcıyı güncelle
DELETE /api/users/5      → Kullanıcıyı sil

// Tutarlı hata formatı
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "Kullanıcı bulunamadı",
    "details": { "userId": 5 }
  }
}

// Tutarlı başarı formatı
{
  "data": { "id": 5, "name": "Ali" },
  "meta": { "requestId": "abc-123" }
}
```

---

## 5. 🌿 Kodu Doğru Yönetmek

### Git Branching Stratejisi 🌳

```
main (production)
 │
 ├── feature/user-authentication
 │     ├── commit: "feat: add login endpoint"
 │     ├── commit: "feat: add JWT token generation"
 │     ├── commit: "test: add login integration tests"
 │     └── → PR → Code Review → Merge to main
 │
 ├── fix/order-duplicate-bug
 │     ├── commit: "fix: prevent duplicate orders on retry"
 │     └── → PR → Code Review → Merge to main
 │
 └── chore/update-dependencies
       └── → PR → Merge
```

### İyi Commit Pratikleri 📝

#### Atomik Commitler

Her commit **TEK BİR mantıksal değişiklik** içermeli:

```bash
# ❌ KÖTÜ: Dev commit — ne yaptığını anlamak imkansız
git commit -m "various fixes and new features"

# ✅ İYİ: Atomik commitler
git commit -m "feat: add email validation to user registration"
git commit -m "fix: handle null address in order summary"
git commit -m "refactor: extract payment logic to PaymentService"
git commit -m "docs: add API documentation for /orders endpoint"
git commit -m "test: add edge case tests for discount calculation"
```

#### Conventional Commits Formatı 📋

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

| Type | Ne Zaman |
|---|---|
| `feat` | Yeni özellik |
| `fix` | Bug düzeltme |
| `docs` | Sadece dokümantasyon |
| `style` | Formatlama (boşluk, virgül, noktalı virgül) |
| `refactor` | Kod yapısı değişikliği (davranış değişmiyor) |
| `test` | Test ekleme/düzeltme |
| `chore` | Build, CI, bağımlılık güncelleme |
| `perf` | Performans iyileştirme |

```bash
# Örnekler:
git commit -m "feat(auth): add two-factor authentication support"
git commit -m "fix(orders): prevent negative quantities in cart"
git commit -m "refactor(users): extract validation to shared module"
git commit -m "perf(search): add database index for email lookup"
```

### PR (Pull Request) Açma Sanatı 🎨

```markdown
## PR Şablonu

### Ne yaptım? (What)
Kullanıcı kaydında email doğrulama eklendi.

### Neden yaptım? (Why)
Fake email'lerle yapılan kayıtlar spam sorununa yol açıyordu. (JIRA-1234)

### Nasıl yaptım? (How)
- Kayıt sırasında doğrulama emaili gönderiliyor
- 24 saat içinde doğrulanmayan hesaplar pasife alınıyor
- Mevcut kullanıcılar etkilenmiyor

### Test
- [x] Unit testler eklendi
- [x] Integration testi eklendi
- [x] Manuel test yapıldı (staging)

### Screenshots (varsa)
[Ekran görüntüleri]

### Notlar
- Rate limiting henüz eklenmedi, ayrı PR'da gelecek
- Migration dosyası var, deploy sırasında dikkat!
```

#### PR Boyutu 📏

```
PR Boyutu    →  Review Kalitesi
─────────────────────────────────
50 satır     →  "Her satırı inceledim" 🔍
200 satır    →  "Detaylı baktım" 👀
500 satır    →  "Hızlı göz gezdirdim" 👁️
1000+ satır  →  "LGTM 🙄" (gerçekte bakmadım)
```

> **İdeal PR: 200-400 satır.** Daha büyükse BÖL!

---

## 6. 🧪 Test Yazmak

### Test Piramidi 🔺

```
        ╱  ╲
       ╱ E2E ╲            Yavaş, pahalı, az sayıda
      ╱────────╲
     ╱Integration╲        Orta hız, orta maliyet
    ╱──────────────╲
   ╱   Unit Tests   ╲     Hızlı, ucuz, çok sayıda
  ╱══════════════════╲
```

| Test Türü | Ne Test Eder | Hız | Sayı |
|---|---|---|---|
| **Unit** | Tek bir fonksiyon/modül | ⚡ Anında | Yüzlerce |
| **Integration** | Modüller arası etkileşim | 🚗 Saniyeler | Onlarca |
| **E2E** | Tüm sistem uçtan uca | 🐢 Dakikalar | Birkaç |

### Ne Zaman Test Yazılır? ⏰

```
✅ Her zaman test yaz:
  - Yeni özellik geliştirirken
  - Bug düzeltirken (önce bug'ı yakalayan testi yaz!)
  - Refactoring yapmadan ÖNCE

❌ Bu durumlarda test atlayabilirsin (tartışmalı!):
  - Prototipler (ama prototip production'a taşınmamalı!)
  - Trivial getter/setter'lar
  - Third-party kütüphane wrapper'ları (kendi learning test'ini yaz)
```

### Test Adlandırma 📛

```javascript
// ❌ KÖTÜ: Ne test ettiği belli değil
test('test1', () => { ... });
test('order test', () => { ... });
test('should work', () => { ... });

// ✅ İYİ: given_when_then veya should_when formatı
test('should return 404 when user does not exist', () => { ... });
test('should apply 20% discount when user is premium member', () => { ... });
test('should throw ValidationError when email is empty', () => { ... });

// ✅ describe bloklarıyla organize et
describe('OrderService', () => {
  describe('createOrder', () => {
    test('should create order with valid items', () => { ... });
    test('should throw error when cart is empty', () => { ... });
    test('should apply coupon discount', () => { ... });
  });

  describe('cancelOrder', () => {
    test('should refund payment when order is cancelled', () => { ... });
    test('should not allow cancellation after shipping', () => { ... });
  });
});
```

### Fixture ve Factory Pattern 🏭

```javascript
// ❌ KÖTÜ: Her testte verileri tekrar tekrar oluşturma
test('test 1', () => {
  const user = { id: 1, name: 'Ali', email: 'ali@test.com', role: 'admin', age: 28, ... };
  // ...
});

test('test 2', () => {
  const user = { id: 2, name: 'Ayşe', email: 'ayse@test.com', role: 'user', age: 25, ... };
  // ...
});

// ✅ İYİ: Factory fonksiyonu
function createTestUser(overrides = {}) {
  return {
    id: Math.random().toString(36).substr(2, 9),
    name: 'Test User',
    email: 'test@example.com',
    role: 'user',
    age: 25,
    status: 'active',
    ...overrides  // İstediğin alanı ezebilirsin
  };
}

test('admin kullanıcı tüm raporları görebilmeli', () => {
  const admin = createTestUser({ role: 'admin' });
  // Sadece önemli farkı belirttin, geri kalan varsayılan
});

test('pasif kullanıcı giriş yapamamalı', () => {
  const inactiveUser = createTestUser({ status: 'inactive' });
  // ...
});
```

### Flaky Testler (Güvenilmez Testler) 🎰

Bazen geçen, bazen kalan testler = **ekibin en büyük düşmanı!**

```
Flaky test nedenleri ve çözümleri:

1. ⏰ Zamana bağımlılık
   ❌ expect(createdAt).toBe(new Date())
   ✅ expect(createdAt).toBeInstanceOf(Date)

2. 🎲 Sıra bağımlılığı
   ❌ Test A'nın çıktısına Test B bağımlı
   ✅ Her test kendi verisini oluştursun (isolated)

3. 🌐 Ağ bağımlılığı
   ❌ Gerçek API'yi çağırma
   ✅ Mock/stub kullan

4. 🔀 Yarış durumu (race condition)
   ❌ setTimeout ile bekleme
   ✅ Async/await ile doğru bekleme

5. 🗂️ Paylaşılan state
   ❌ Global değişken kullanma
   ✅ beforeEach'te temiz state oluştur
```

> **Kural:** Flaky test gördüğün an YA DÜZELT ya da SİL. "Bazen kalıyor" diye ignore etmek, test suite'ine olan güveni yok eder.

---

## 7. 👁️ Kod İnceleme (Code Review)

### Neden Code Review? 🤔

```
Code Review faydaları:
├── 🐛 Bug yakalama (gözden kaçanlar)
├── 📚 Bilgi paylaşımı (bus factor azaltma)
├── 📏 Tutarlılık (takım standartları)
├── 🧠 Öğrenme (başkasının kodu = yeni perspektif)
└── 🤝 Takım sahipliği ("Bu kodu herkes biliyor")
```

> **Bus Factor:** "Kaç kişi otobüsle ezilirse proje durur?" Bu sayıyı artırmak için code review şart!

### Code Review Yapan Kişi İçin (Reviewer) 🔍

#### Ne Kontrol Edilmeli?

```
Kontrol Listesi:

🎯 Doğruluk
  □ Kod doğru şeyi yapıyor mu?
  □ Edge case'ler düşünülmüş mü?
  □ Hata durumları yönetiliyor mu?

📐 Tasarım
  □ Doğru soyutlama seviyesinde mi?
  □ SOLID prensiplerine uygun mu?
  □ Gereksiz karmaşıklık var mı?

🧹 Temizlik
  □ İsimlendirmeler anlaşılır mı?
  □ DRY ihlali var mı?
  □ Dead code var mı?

🧪 Test
  □ Testler var mı?
  □ Doğru şeyleri test ediyor mu?
  □ Edge case'ler test edilmiş mi?

🔒 Güvenlik
  □ SQL injection riski?
  □ Hassas veri loglanıyor mu?
  □ Authentication/Authorization kontrolleri var mı?

📊 Performans
  □ N+1 query sorunu var mı?
  □ Gereksiz DB çağrısı var mı?
  □ Büyük veri setlerinde ne olur?
```

#### Nasıl Yorum Yapılmalı? 💬

```
❌ KÖTÜ YORUM:
"Bu yanlış."
"Böyle yapılmaz."
"Neden böyle yazdın?"

✅ İYİ YORUM:
"Bu yaklaşım yerine X pattern kullanmayı düşünür müsün?
 Çünkü [neden]. İşte bir örnek: [link/snippet]"

"Burada bir edge case kaçmış olabilir: userId null gelirse ne olur?
 Belki şöyle bir guard ekleyebiliriz: [öneri]"

"Güzel yaklaşım! 👍 Bir küçük öneri: Bu fonksiyonu
 daha okunabilir yapmak için early return kullanılabilir."
```

#### Yorum Etiketleme Sistemi 🏷️

```
[blocking]  → Bu düzeltilmeden merge edilemez
[nit]       → Nitpick: Küçük öneri, zorunlu değil
[question]  → Anlama amaçlı soru, belki bir şeyi kaçırıyorum
[suggestion]→ Alternatif yaklaşım önerisi
[praise]    → Bunu çok beğendim! 🎉

Örnek:
"[nit] Burada const yerine let kullanılmış ama değer değişmiyor."
"[blocking] Bu endpoint authentication middleware'i kullanmıyor, güvenlik açığı."
"[praise] Bu utility fonksiyonu çok temiz, harika iş! 👏"
```

### Code Review Alan Kişi İçin (Author) 📤

```
1. PR'ı açmadan ÖNCE kendi kodunu gözden geçir
2. PR açıklamasını detaylı yaz
3. Büyük PR'ı küçük parçalara böl
4. Review yorumlarını kişisel alma! 🙏
5. Yorumlara yapıcı şekilde yanıt ver
6. Anlaşamadığınız konularda yüz yüze konuş
```

> **Altın kural:** Code review KODU eleştirir, KİŞİYİ DEĞİL.
> "Senin kodun kötü" ❌ → "Bu kodun şu kısmı iyileştirilebilir" ✅

---

## 8. 🚀 Yazılımı Teslim Etmek (Delivery)

### CI/CD Pipeline 🏭

```
Commit → Build → Test → Analyze → Deploy (Staging) → Test → Deploy (Prod)
          │       │       │            │                │          │
          │       │       │            │                │          │
        compile  unit   lint/sonar   otomatik        e2e/smoke  canary/
        bundle   integ  security     deploy          manual     blue-green
```

### Deployment Stratejileri 🎯

#### 1. Rolling Deploy (Yuvarlanan Dağıtım)

```
Sunucu 1: [v1] → [v2] ✅
Sunucu 2: [v1] → [v2] ✅    Her sunucu sırayla güncellenir
Sunucu 3: [v1] → [v2] ✅
```

#### 2. Blue-Green Deploy

```
                 Kullanıcılar
                      │
Load Balancer ───────┼───────
                      │
Blue  (v1) ← aktif    │    Green (v2) ← hazırlanıyor
                      │
                   Switch!
                      │
Blue  (v1) ← yedek    │    Green (v2) ← artık aktif ✅
```

#### 3. Canary Deploy (Kanarya Dağıtımı) 🐦

```
%95 trafik → v1 (eski, güvenli)
%5  trafik → v2 (yeni, deneniyor)

Metrikler iyi mi?
  Evet → %10... %25... %50... %100 → v2'ye geç ✅
  Hayır → Geri al! 🔙 Sadece %5 etkilendi.
```

#### 4. Feature Flags 🚩

```javascript
// Özelliği koda deploy et ama AÇMA
if (featureFlags.isEnabled('new-checkout-flow', user)) {
  return newCheckoutFlow(order);
} else {
  return legacyCheckoutFlow(order);
}

// Avantajlar:
// - Deploy ve release bağımsız! 
// - PM istediği zaman özelliği açıp kapabilir
// - A/B test yapabilirsin
// - Sorun olursa flag'i kapat, rollback'e gerek yok
```

### Rollback Planı Olmalı 🔙

> **"Her deploy'un bir rollback planı olmalıdır. Plan yoksa deploy yapma."**

```
Deploy checklist:
  □ Rollback adımları tanımlandı mı?
  □ DB migration geri alınabilir mi?
  □ Monitoring/alerting ayarlandı mı?
  □ Smoke test hazır mı?
  □ İletişim planı var mı? (Slack kanalı, ilgili kişiler)
  □ Deploy saati uygun mu? (Cuma 17:00'da deploy YAPMA! 😱)
```

---

## 9. 🚨 On-Call ve Incident Yönetimi

### Hikaye: Gece 3'te Telefon Çalıyor 📱

```
🔔 PagerDuty: "ALERT: Orders API - Error Rate > 50%"
⏰ Saat: 03:17
😴 Sen: *Uyuyor*
📱 *ZIRRRR*

Bu an için HAZIRLIKLI olmalısın!
```

### On-Call Nedir? 📟

On-call = Belirli bir süre boyunca (genellikle 1 hafta) sistem sorunlarına müdahale etmeye hazır olmak.

```
On-Call Rotasyonu:
Hafta 1: Ali     (Primary) / Ayşe (Secondary)
Hafta 2: Mehmet  (Primary) / Ali  (Secondary)
Hafta 3: Ayşe   (Primary) / Mehmet (Secondary)
Hafta 4: Ali     (Primary) / Ayşe (Secondary)
...
```

### Incident Seviyeleri 🚦

| Seviye | Tanım | Örnek | Müdahale |
|---|---|---|---|
| **SEV1** 🔴 | Tüm sistem çökmüş | Hiçbir kullanıcı sipariş veremiyor | Anında, tüm ekip |
| **SEV2** 🟠 | Ana özellik bozuk | Ödeme sistemi çalışmıyor | 30 dk içinde, on-call + takım |
| **SEV3** 🟡 | Kısmi etki | Bazı kullanıcılar yavaşlık yaşıyor | 4 saat içinde, on-call |
| **SEV4** 🟢 | Minimal etki | Dashboard'da bir grafik kırık | Sonraki iş günü |

### Incident Response (Olay Müdahalesi) 🏥

```
INCIDENT TIMELINE:

1. 🔔 ALGILA (Detect)
   Alert geldi veya müşteri bildirdi
   → Kendi monitoring'in yakalamalı, müşteriden duymak KÖTÜ!

2. 📢 BİLDİR (Communicate)
   #incident kanalına yaz:
   "🚨 SEV2 - Orders API yüksek hata oranı. Araştırıyorum."

3. 🔍 ARAŞTIR (Investigate)
   - Dashboard'lara bak (Grafana, Datadog, vb.)
   - Logları kontrol et
   - Son deploy ne zamandı?
   - Ne değişti? (config, trafik spike, dependency)

4. 🛠️ MÜDAHALE ET (Mitigate)
   → Hızlı çözüm bul:
     - Rollback
     - Config değişikliği
     - Etkilenen servisi restart et
     - Trafik yönlendirme değiştir
   → ŞİMDİ problemi ÇÖZ, kök nedeni SONRA araştır!

5. 📝 SONRASI (Post-mortem)
   → Olay bitince dökümanla (blameless!)
```

### Postmortem (Olay Sonrası Rapor) 📄

> **BLAMELESS = Suçsuz.** Postmortem'in amacı suçlu bulmak DEĞİL, sistemin nasıl iyileştirileceğini bulmaktır!

```markdown
## Postmortem: Orders API Çökmesi - 15 Nisan 2026

### Özet
15 Nisan 03:17-04:45 arasında Orders API %60 hata oranı yaşadı.
~2.500 sipariş etkilendi.

### Zaman Çizelgesi
- 03:17 — Alert tetiklendi
- 03:22 — On-call engineer müdahaleye başladı
- 03:35 — Son deploy'un soruna yol açtığı tespit edildi
- 03:42 — Rollback başlatıldı
- 04:45 — Sistem normal seviyeye döndü

### Kök Neden
Deploy edilen kodda, büyük siparişlerde timeout değerinin yetersiz
kalması nedeniyle database bağlantı havuzu tükendi.

### Etki
- 2.500 kullanıcı sipariş veremedi
- Tahmini gelir kaybı: ~XX TL

### Öğrenilen Dersler
- ✅ İyi giden: Alert 5 dakikada tetiklendi, hızlı rollback
- ❌ İyileştirilecek: Load test yapılmamıştı, staging'de yakalanmalıydı

### Aksiyon Maddeleri
- [ ] @ali — Deploy öncesi load test zorunlu olacak (Ticket: JIRA-5678)
- [ ] @ayse — DB connection pool monitoring eklenmeli (Ticket: JIRA-5679)
- [ ] @mehmet — Timeout config'i environment variable olacak (Ticket: JIRA-5680)
```

> **"Postmortem yazmamak, aynı hatayı tekrar yapmayı garanti etmektir."**

### On-Call Sağlıklı Yaşam Rehberi 🧘

```
✅ Yapılması gerekenler:
  - Runbook hazırla (bilinen sorunlar ve çözümleri)
  - Alert'leri düzenli gözden geçir (çok mu? gereksiz olanı kapat)
  - On-call arkadaşını tanı (secondary'i bilgilendir)
  - Telefonu yanından ayırma (ama panikleme de!)

❌ Yapılmaması gerekenler:
  - Her alert'i production incident olarak görme
  - Tek başına kahraman olmaya çalışma (yardım iste!)
  - Postmortem'i atlama ("Düzeldi ya, tamam" ❌)
  - Cuma akşamı deploy yapma 😅
```

---

## 10. 📝 Teknik Tasarım Süreçleri

### Design Document / RFC / ADR 📐

Büyük bir değişiklik yapmadan önce **yazarak düşün!**

#### ADR — Architecture Decision Record 🏛️

```markdown
# ADR-001: Event Queue Olarak Kafka Kullanımı

## Durum
Kabul Edildi (2026-03-15)

## Bağlam
Siparişler ve bildirimler arasındaki senkron HTTP çağrıları,
yüksek yükte cascade failure'a yol açıyor.

## Karar
Servisler arası asenkron iletişim için Apache Kafka kullanılacak.

## Alternatifler
1. **RabbitMQ** — Daha basit ama ölçeklenebilirlik sınırlı
2. **AWS SQS** — Cloud-native ama vendor lock-in
3. **Redis Streams** — Zaten kullandığımız Redis üzerinde ama durability endişesi

## Sonuçlar
- ✅ Servisler decouple olur, cascade failure önlenir
- ✅ Event replay ile hata kurtarma kolaylaşır
- ❌ Operasyonel karmaşıklık artar (Kafka cluster yönetimi)
- ❌ Eventual consistency ile başa çıkmak gerekir
```

#### Ne Zaman Doküman Yazılmalı?

```
Her zaman doküman yaz:
├── Yeni bir servis/modül tasarlıyorsan
├── Veritabanı şeması değişiyorsa
├── Yeni bir external dependency ekliyorsan
├── API kontratı değişiyorsa
├── Performans kritik çalışma yapıyorsan
└── "Bu kararı neden aldık?" sorusuna gelecekte cevap verilmeli ise

Doküman yazma:
├── Küçük bug fix
├── Refactoring (tasarımı değişmiyorsa)
└── Config değişikliği
```

### Teknik Tasarım Dokümanı Şablonu 📄

```markdown
# Tasarım: [Özellik Adı]

## Amaç
Bu doküman, [X problemi] için önerilen çözümü anlatır.

## Motivasyon / Problem
- Şu an X sorunu var
- Bu, kullanıcıları Y şekilde etkiliyor
- Aylık Z TL maliyet çıkartıyor

## Önerilen Çözüm
[Mimari diyagram]
[Ana bileşenler ve sorumlulukları]
[Veri akışı]
[API kontratları]

## Alternatifler
1. [Alternatif 1] — Neden seçilmedi
2. [Alternatif 2] — Neden seçilmedi

## Riskler ve Azaltma Planları
- Risk 1: [Açıklama] → Azaltma: [Plan]

## İş Planı
- Faz 1: [Şu adımlar] (2 hafta)
- Faz 2: [Şu adımlar] (1 hafta)

## Açık Sorular
- [ ] X bileşeni Y'yi destekliyor mu?
```

---

## 11. 📈 Kariyer Yönetimi

### Mühendislik Seviyeleri (Kariyer Merdiveni) 🪜

```
                                ┌──────────────┐
                               │ Distinguished │ Çok nadir
                               │   Engineer    │
                               └──────┬───────┘
                          ┌───────────┴───────────┐
                         │    Principal Engineer   │ Şirket çapında etki
                         └───────────┬────────────┘
                    ┌────────────────┴────────────────┐
                   │         Staff Engineer            │ Org çapında etki
                   └────────────────┬─────────────────┘
              ┌─────────────────────┴─────────────────────┐
             │              Senior Engineer                │ Takım çapı
             └─────────────────────┬──────────────────────┘
        ┌──────────────────────────┴──────────────────────────┐
       │                    Mid-Level Engineer                  │
       └──────────────────────────┬───────────────────────────┘
  ┌───────────────────────────────┴───────────────────────────────┐
 │                        Junior Engineer                          │ 🫵 Başlangıç
 └─────────────────────────────────────────────────────────────────┘
```

### Her Seviyeden Beklentiler 📋

#### Junior Engineer (0-2 yıl)

```
✅ Beklenen:
  - Tanımlanmış görevleri tamamlamak
  - Sorular sormak
  - Mentorluktan faydalanmak
  - Kod kalitesi standartlarını öğrenmek
  - Test yazmak
  - Code review'dan öğrenmek

❌ Beklenmeyen:
  - Mimari kararlar
  - Bağımsız büyük projeler
  - Başkalarına mentorluk
```

#### Mid-Level Engineer (2-5 yıl)

```
✅ Beklenen:
  - Bağımsız çalışabilmek
  - Belirsiz gereksinimleri netleştirmek
  - Birden fazla yaklaşımı değerlendirmek
  - Başka mühendislere yardım etmek
  - Kod kalitesi standartlarını yükseltmek
  - Teknik borcu tanımlamak ve azaltmak
```

#### Senior Engineer (5+ yıl)

```
✅ Beklenen:
  - Belirsiz problemleri çözmek
  - Takımı teknik olarak yönlendirmek
  - Mimari kararlar almak
  - Mentorluk yapmak
  - Cross-team işbirliği
  - Teknik karar dokümanları yazmak (ADR, RFC)
  - Proje planlama ve tahmin
  - On-call liderliği
```

### 1:1 Toplantıları Etkili Kullanmak 🗣️

1:1 = Yöneticinle birebir düzenli toplantı. **SENİN toplantın**, hazırlıklı gel!

```
1:1 Gündemi (her toplantıya hazırla):

📌 Bu hafta neler yaptım?
  - Tamamladığım işler
  - Karşılaştığım zorluklar

❓ Yardıma ihtiyacım olan konular
  - Teknik: "X servisi hakkında bilgi lazım"
  - Organizasyonel: "Y takımıyla koordinasyon gerekiyor"
  - Kariyer: "Mentorluk fırsatı arıyorum"

🎯 Kariyer hedeflerim
  - Kısa vade (3 ay): "Bu çeyrek X'i öğrenmek istiyorum"
  - Orta vade (1 yıl): "Senior'a terfi için ne yapmam gerekiyor?"

💡 Feedback istediğim konular
  - "Son PR'ımdaki tasarım hakkında ne düşünüyorsun?"
  - "Toplantılardaki iletişimim nasıl?"
```

> **Hatırla:** Yöneticin senin **kariyer sponsorun**. Ama senin adına kariyer planı yapmaz. O plan **senin işin.**

### Terfi Nasıl Alınır? 🏆

```
❌ Terfi ALMAK:
"2 yıl oldu, terfi hakkım var" → Terfi zamana göre DEĞİL!

✅ Terfi KAZANMAK:
Bir üst seviyenin işini zatten YAPIYORSAN, terfi gelir.

Strateji:
1. Bir üst seviyeden ne beklendiğini yöneticinle konuş
2. O beklentileri karşılayan görevler al
3. Yaptıklarını GÖRÜNÜR yap (dokümanla, sunumlarda paylaş)
4. Sponsorun (yöneticin) farkında olsun
5. Terfi zamanı geldiğinde kanıtlar hazır olsun
```

### IC vs Management Track 🔀

```
         ┌─ IC Track ──────────────────────────────┐
         │ Junior → Mid → Senior → Staff → Principal │
         │ Daha derin teknik uzmanlık                │
         └──────────────────────────────────────────┘

         ┌─ Management Track ──────────────────────┐
         │ Tech Lead → EM → Director → VP → CTO     │
         │ İnsan yönetimi, strateji, organizasyon    │
         └──────────────────────────────────────────┘

Sen hangisini istiyorsun?

IC: "Teknik derinliği seviyorum, insanları yönetmek beni
     yormak yerine kod yazmak istiyorum"

Management: "İnsanları geliştirmek, strateji belirlemek,
            organizasyonu şekillendirmek istiyorum"

Her ikisi de EŞIT DEĞERDEDİR! Birisi diğerinden "üst" değildir.
```

---

## 12. 🧘 Kendini ve Başkalarını Yönetmek

### Imposter Syndrome (Sahtekar Sendromu) 🎭

> **"Herkes benden daha iyi biliyor. Bir gün gerçeği fark edecekler."**

```
İstatistik: Yazılım mühendislerinin %70'i imposter sendromu yaşıyor.

Gerçek:
- Senior bile her gün bir şey öğreniyor
- Stack Overflow herkesin en yakın arkadaşı (senior dahil!)
- "Bilmiyorum" demek profesyonelliktir, zayıflık değil
- Herkes başlangıçta kötüydü

İlacı:
1. Öğrendiklerini kaydet → Geriye bak, ne kadar geliştiğini gör
2. Başkalarına yardım et → Sen de biliyorsun, kanıtla
3. Konuş → Başkaları da aynı şeyi hissediyor, paylaş
4. Mükemmeliyetçiliği bırak → "Yeterince iyi" YETERLidir
```

### Dunning-Kruger Etkisi 📉📈

```
Güven
  │
  │  🏔️ "Her şeyi
  │      biliyorum!"         ⭐ Gerçek
  │      (Bilmiyorsun)      ustalık
  │        │                   │
  │        │                 ╱
  │        │               ╱
  │        │    🕳️       ╱
  │         ╲  "Hiçbir  ╱
  │          ╲  şeyi  ╱
  │           ╲bilmi-╱
  │            ╲yorum"
  │             ╲  ╱
  └──────────────────────→ Bilgi

Yeni öğrendin → Her şeyi bildiğini sanıyorsun (tehlikeli!)
Biraz daha öğrendin → Bilmediğinin farkına vardın (acı ama sağlıklı)
Çok öğrendin → Gerçek özgüven geldi (informed confidence)
```

### Zaman Yönetimi ⏰

#### Maker's Schedule vs Manager's Schedule 📅

```
Manager'ın günü:            Maker'ın (Developer) günü:
09:00 ☐ Toplantı            09:00 ┐
09:30 ☐ Toplantı                   │
10:00 ☐ 1:1                        │ ODAKLI ÇALIŞMA BLOĞU
10:30 ☐ Email                      │ (kesintisiz 3 saat)
11:00 ☐ Toplantı                   │
11:30 ☐ Toplantı            12:00 ┘
12:00 ☐ Öğle yemeği         12:00 ☐ Öğle yemeği
13:00 ☐ Toplantı            13:00 ☐ Standup (15 dk)
13:30 ☐ Toplantı            13:15 ┐
14:00 ☐ 1:1                        │ ODAKLI ÇALIŞMA BLOĞU
14:30 ☐ Email                      │ (kesintisiz 3 saat)
15:00 ☐ Toplantı                   │
                             16:15 ┘
                             16:15 ☐ Code review, email, Slack
```

> **Her toplantı bir developer'ın 30 dakikasını değil, TÜM ODAKLILI çalışma bloğunu bozar!**

#### Pomodoro Tekniği 🍅

```
25 dk ODAKLI ÇALIŞMA 🔴 → 5 dk MOLA ⚪ → 25 dk 🔴 → 5 dk ⚪
→ 25 dk 🔴 → 5 dk ⚪ → 25 dk 🔴 → 15 dk UZUN MOLA 🟢

Kurallar:
- 25 dk boyunca Slack KAPALI, telefon SESSIZE
- Biri soru sorarsa: "10 dk sonra bakayım"
- Acil değilse: kesme!
```

### Sağlıklı Çalışma Alışkanlıkları 💚

```
✅ Yapılması gerekenler:
  - Düzenli molalar ver (göz, sırt, bilek)
  - İş-yaşam dengesi koru (kapağı kapat, evde iş yapma)
  - "Hayır" demeyi öğren ("Bu sprint'e sığmaz, sonraki sprint'e alalım")
  - Egzersiz yap (yürüyüş bile yeter)
  - Uyku düzenini koru (kötü uyku = kötü kod!)

❌ Yapılmaması gerekenler:
  - Hero culture: "Ben gece 3'e kadar çalışıp yetiştirdim!" → TUTARSI!
  - Burnout belirtilerini görmezden gelme
  - Sürekli acil moddda çalışma
  - "Bu benim değil" deme ama "Her şey benim" de deme
```

### İletişim Sanatı 🗣️

#### Teknik Konuları Teknik Olmayan Kişilere Anlatmak 🌉

```
❌ PM'e:
"gRPC endpoint'te protobuf serialization'da backward
compatibility problemi var, rolling update sırasında
field number'lar çakışıyor"

✅ PM'e:
"Yeni güncellemeyi canlıya aldığımızda, eski ve yeni versiyon
arasında iletişim sorunu olabilir. Bu, 5-10 dakikalık kesintiye
yol açabilir. Bunu önlemek için 2 günlük ek çalışma gerekiyor."

Teknik detayı SAKLAMA, ama dinleyicinin anlayacağı dile ÇEVİR:
- Etkiyi söyle (kaç kullanıcı etkilenir?)
- Süreyi söyle (ne kadar sürer?)
- Alternatif sun (ne yapabiliriz?)
```

#### Toplantılarda Etkili Olma 💬

```
Toplantı ÖNCE:
  □ Gündem var mı? Yoksa iste!
  □ "Bu toplantı email/Slack ile çözülebilir mi?"
  □ Hazırlığını yap (gerekli datayı topla)

Toplantı SIRASINDA:
  □ Not al (sonra unutursun)
  □ Konuşmaya katkı yap (sessiz kalma)
  □ Konu dışına çıkıldığında "Bunu ayrı konuşalım" de
  □ Toplantı saatini geçirme

Toplantı SONRA:
  □ Aksiyonları kaydet (kim, ne, ne zaman)
  □ İlgili kişilere özeti paylaş
```

---

### 🤖 Yapay Zeka Çağında "The Missing README"

```
Bu kitap "okulda öğretilmeyenler" hakkında.
Artık bir şey daha var ki okulda öğretilmiyor:
→ AI ARAÇLARIYLA ÇALIŞMAK!

1. ONBOARDING HIZLANIYOR ⭐
   → Yeni projeye giriş: "Bu codebase ne yapıyor?" → AI'a sor!
   → AMA: AI halüsine edebilir → her zaman KODDLA DOĞRULA!
   → AI = hızlı başlangıç ama KOR KÖRÜNE güvenme!

2. CODE REVIEW DEĞİŞİYOR
   → AI-generated kodu REVIEW etmek yeni beceri!
   → "Bu kodu Copilot yazdı" → her satırı ANLA!
   → "AI yazdı diye doğrudur" → EN TEHLİKELİ varsayım!

3. TESTLER DEĞİŞİYOR
   → AI test üretebilir AMA genellikle implementation detail test eder
   → SEN davranış (behavior) testi istemelisin!
   → AI-generated testi OKUMASANIZ eklemeyin!

4. TEKNİK BORÇ RISKI ARTIYOR
   → AI ile kod üretmek ÇOK HIZLI → "ne kadar çok o kadar iyi" tuzagı!
   → Hızlı üretim = hızlı borç birikimi
   → YAVAŞLA ve DÜŞÜN: "Bu kodu ANLADIM MI?" → sonra merge et!
```

## 13. 🎬 Son Sözler

### Bu Kitabın Altın Kuralları 🏆

| # | Kural | Bir Cümlede |
|---|---|---|
| 1 | **İlk günden katkı yap** | Korkma, küçük başla, sor |
| 2 | **Kasıtlı olarak öğren** | Sadece iş yapmak yetmez, zayıf yönlerini çalış |
| 3 | **Üretim kalitesinde yaz** | "Çalışıyor" yetmez: logla, izle, test et |
| 4 | **Basit tut** | YAGNI, KISS — karmaşıklıkla savaş |
| 5 | **Git'i doğru kullan** | Atomik commit, iyi mesaj, küçük PR |
| 6 | **Test yaz** | Piramit: çok unit, orta integration, az E2E |
| 7 | **Review yap ve al** | Kodu eleştir, kişiyi değil |
| 8 | **Güvenli deploy et** | CI/CD, canary, feature flag, rollback planı |
| 9 | **Incident'a hazır ol** | Runbook, postmortem, blameless kültür |
| 10 | **Kararları dokula** | ADR, RFC, tasarım dokümanı |
| 11 | **Kariyerini yönet** | Seviye beklentileri, 1:1, görünürlük |
| 12 | **Kendine iyi bak** | İletişim, zaman yönetimi, work-life balance |

### Şu An Neredesin, Nereye Gidiyorsun? 🗺️

```
📗 Grokking Algorithms     → Algoritma temeli ✅
📕 Clean Code              → Kod kalitesi ✅
📘 The Pragmatic Programmer → Mühendislik zihniyeti ✅
📙 The Missing README      → Kariyer temeli ✅  ← BURADASIN

🎓 FAZ 1 TAMAMLANDI! 🎉

Sıradaki (Faz 2):
📗 A Philosophy of Software Design → Daha derin tasarım düşüncesi
📘 Head First Design Patterns      → Pattern'lar
📕 Designing Data-Intensive Apps   → Dağıtık sistem temeli
📙 Unit Testing (Khorikov)         → Test stratejisi
📗 Refactoring (Fowler)            → Referans kitap
```

---

> **"Kimse 'tam hazır' olarak doğmuyor.
> Herkes bir gün yeni başlayan olarak kapıdan giriyor.
> Fark, girişten sonra ne yaptığındadır."**
>
> İlk gününde soru sormaktan çekinme.
> Yüzüncü gününde başkalarına yol göster.
> Bininci gününde sistemi şekillendir.
>
> **Bu maraton. Ve sen çoktan koşmaya başladın.** 🏃‍♂️💨
