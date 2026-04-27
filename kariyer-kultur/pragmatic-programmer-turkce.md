# 🛠️ The Pragmatic Programmer — Türkçe Kapsamlı Rehber

> **"Pragmatik"** = Teorik mükemmellik yerine, **pratik sonuçlara** odaklanan.
> Bu kitap, yazılım mühendisliğinde "doğru mühendis" olmanın felsefesini anlatır.

> **"Kariyerinin en önemli yatırımı sensin."**
> — Andy Hunt & Dave Thomas

---

## 📖 İçindekiler

1. [Pragmatik Felsefe](#1--pragmatik-felsefe)
2. [Pragmatik Yaklaşım](#2--pragmatik-yaklaşım)
3. [Temel Araçlar](#3--temel-araçlar)
4. [Pragmatik Paranoya](#4--pragmatik-paranoya)
5. [Bükülebilir Kod (Bend or Break)](#5--bükülebilir-kod-bend-or-break)
6. [Eşzamanlılık (Concurrency)](#6--eşzamanlılık-concurrency)
7. [Kodlarken (While You Are Coding)](#7--kodlarken-while-you-are-coding)
8. [Projeden Önce](#8--projeden-önce)
9. [Pragmatik Projeler](#9--pragmatik-projeler)
10. [Son Sözler](#10--son-sözler)

---

## 1. 🧠 Pragmatik Felsefe

### 1.1 Senin Hayatın, Senin Sorumluluğun 🪞

#### Hikaye: Kırık Pencere 🏚️

Bir mahallede tertemiz bir bina var. Bir gün birisi bir pencereyi kırar. Kimse tamir etmez. Birkaç hafta sonra başka pencereler de kırılır. Sonra duvarlar grafiti ile kaplanır. 6 ay sonra bina terk edilmiş harabeye döner.

Bu, kriminolojideki **"Kırık Pencere Teorisi"** (Broken Window Theory).

> **Yazılımda kırık pencere =** düzeltilmemiş kötü tasarım, yanlış karar, kirli kod.

Takımda biri "Zaten burası karışık, ben de öyle yazayım" dediğinde, çürüme başlar. 🪟💥

```
Bir kırık pencere     →  "Neyse, zaten kötü"
                      →  İkinci kırık pencere
                      →  "Herkes böyle yapıyor"
                      →  Her yer kırık
                      →  "Sıfırdan yazalım" 😩
```

**Pragmatik mühendis ne yapar?**
- Kırık pencere gördüğünde ya **hemen tamir eder** ya da en azından **tahta ile kapatır** (TODO + ticket)
- Kodun genelini temiz tutarak, başkalarının da temiz tutmasını teşvik eder
- "Zaten kötü" bahanesine izin vermez

#### Karşıt Hikaye: Taş Çorba 🍲

Üç asker köye gelir, aç ve yorgun. Köylülerden yiyecek istemeye çalışırlar ama herkes "Yok" der. Askerler bir kazan su kaynatır, içine büyük bir taş koyar.

Köylü: "Ne yapıyorsunuz?"
Askerler: "Taş çorbası! Çok lezzetli ama biraz havuç olsa daha iyi olurdu..."
Köylü: "Bende havuç var!" 🥕

Başka biri patates getirir, başka biri soğan... Sonunda herkes katkı yapar ve ortaya harika bir çorba çıkar! 🍲

> **Taş Çorba = Değişimi başlatan katalizör olmak.**

Büyük bir proje önerisi yapmak yerine, **küçük bir prototip** yap. İnsanlar çalışan bir şey gördüğünde katkı yapmaya başlar.

```
"Şuna izin verin, buna bütçe ayırın..."  → Kimse ilgilenmez 😴
"Bakın şunu yaptım, bir de şu olsa..."   → Herkes ilgilenir! 🤩
```

### 1.2 Yeterince İyi Yazılım 🎯

Mükemmellik düşmanıdır iyinin (**"Perfect is the enemy of good"**).

#### Piksel Piksel Resim Analojisi 🎨

Bir tabloyu düşün. Ressam ne zaman durur?

- Her fırça darbesiyle biraz daha iyi olur
- Ama bir noktadan sonra **daha fazla çalışmak tabloyu bozmaya başlar** (overworking)
- Usta ressam, "yeterince iyi" olduğunu bilir ve durur

```javascript
// ❌ Overengineering: 5 dakikalık iş için 3 günlük mimari
class AbstractUserValidatorFactoryProviderStrategy {
  createValidatorForUserTypeByContextWithOptions(type, ctx, opts) {
    // 200 satır...
  }
}

// ✅ Yeterince iyi: İhtiyacı karşılar, anlaşılır, genişletilebilir
function validateUser(user) {
  if (!user.email) throw new Error('Email gerekli');
  if (!user.name) throw new Error('İsim gerekli');
  return true;
}
```

> **Yeterince iyi ≠ özensiz.** Kullanıcının ihtiyacını karşılayan, sürdürülebilir, profesyonel kod demek.

### 1.3 Bilgi Portföyün 📈

Bilgin = finansal portföy gibi yönetilmeli.

| Yatırım İlkesi | Bilgi Karşılığı |
|---|---|
| **Düzenli yatırım yap** | Her yıl en az 1 yeni dil/teknoloji öğren |
| **Çeşitlendir** | Sadece backend değil, frontend, DevOps, mobil de öğren |
| **Riski yönet** | Tutucu (Java) + riskli (yeni çıkan dil) karışımı |
| **Ucuzken al, pahalıyken sat** | Yeni bir teknoloji popüler olmadan öğren |
| **Gözden geçir ve dengele** | Bilgi eskir, portföyünü güncelle |

#### Somut Hedefler 🎯

- ✅ Her yıl en az bir yeni programlama dili öğren
- ✅ Her ay bir teknik kitap oku
- ✅ Teknik olmayan kitaplar da oku (insan psikolojisi, iletişim)
- ✅ Kurslar al, konferanslara katıl
- ✅ Yerel kullanıcı gruplarına ve toplulukklara katıl
- ✅ Farklı ortamları dene (Windows kullanıyorsan Linux'u dene, vb.)
- ✅ Akımın dışında kal — mainstream'den farklı şeyler de öğren

#### Eleştirel Düşünce 🧐

Her okuduğuna körü körüne inanma! Sorular sor:

- **"Neden?"** → Bu neden böyle?
- **"Kimin için?"** → Bu bilgi kime yarıyor?
- **"Bağlam nedir?"** → Bu hangi koşulda geçerli?
- **"Ne zaman ve nerede işe yarar?"** → Her yerde mi, yoksa belirli durumlarda mı?
- **"Arkasında para var mı?"** → Bir şirket bunu satmaya mı çalışıyor?

> **"Sana bir teknolojinin harika olduğunu söyleyen kişi, o teknolojiyi mi satıyor?"** 🤔

### 1.4 İletişim 🗣️

Harika bir fikrin var ama anlatamıyorsan, **yokmuş gibidir.**

| İlke | Açıklama |
|---|---|
| **Dinleyiciyi tanı** | CEO'ya teknik detay anlatma, geliştiriciye iş stratejisi anlama |
| **Ne söylemek istediğini bil** | Konuşmadan/yazmadan önce ana mesajını netleştir |
| **Zamanı seç** | "Deployment sırasında refactoring önerme" 😅 |
| **Bir stil seç** | Bazıları görsel ister, bazıları data ister |
| **Güzel görünmesini sağla** | README, dokümantasyon, sunum — formatlama önemli |
| **Dinleyiciyi dahil et** | Soru sor, feedback al, monolog yapma |
| **Dinle** | İnsanları dinle, belki onlar da sana bir şey öğretir |
| **Geri dön** | "Mail atayım, cevap veririm" dediysen VER! |

> **E-posta ve Slack kuralı:** Mesajını göndermeden önce bir kez daha oku. "Ben bunu alsam ne düşünürdüm?" diye sor kendine.

---

## 2. 🎯 Pragmatik Yaklaşım

### 2.1 DRY — Don't Repeat Yourself 🔁

> **"Her bilgi parçası, sistem içinde tek bir yerde, tek bir otoriteye sahip, kesin bir temsile sahip olmalıdır."**

Bu, Clean Code'daki DRY'den **çok daha geniş** bir kavram!

#### DRY Sadece Kod Tekrarı Değil! ⚠️

```
DRY'ın kapsadığı alanlar:
├── Kod tekrarı (en bariz)
├── Dokümantasyon tekrarı
├── Veri tekrarı
├── API tekrarı
└── Bilgi tekrarı (en önemlisi)
```

#### Kod Tekrarı 💻

```javascript
// ❌ DRY İhlali: Aynı validasyon mantığı iki yerde
function createUser(data) {
  if (!data.email || !data.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
    throw new Error('Geçersiz email');
  }
  // ... oluştur
}

function updateUser(data) {
  if (!data.email || !data.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
    throw new Error('Geçersiz email');
  }
  // ... güncelle
}

// ✅ DRY: Tek bir doğruluk kaynağı
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function validateEmail(email) {
  if (!email || !email.match(EMAIL_REGEX)) {
    throw new Error('Geçersiz email');
  }
}

function createUser(data) {
  validateEmail(data.email);
  // ... oluştur
}

function updateUser(data) {
  validateEmail(data.email);
  // ... güncelle
}
```

#### Dokümantasyon Tekrarı 📝

```javascript
// ❌ DRY İhlali: Yorum kodu tekrarlıyor
/**
 * Kullanıcının yaşını döndürür.
 * @param {Object} user - Kullanıcı objesi
 * @returns {number} - Kullanıcının yaşı
 */
function getUserAge(user) {
  return user.age;
}
// Yorum, kodun zaten söylediğini tekrarlıyor!

// ✅ Yorum gereksiz, fonksiyon adı yeterli
function getUserAge(user) {
  return user.age;
}
```

#### Veri Tekrarı 🗄️

```javascript
// ❌ DRY İhlali: Yaş hem saklanıyor hem hesaplanıyor
class User {
  constructor(name, birthDate) {
    this.name = name;
    this.birthDate = birthDate;
    this.age = this.calculateAge(); // 🚨 birthDate değişirse age eski kalır!
  }
}

// ✅ DRY: Yaş her zaman hesaplanır (türetilmiş veri)
class User {
  constructor(name, birthDate) {
    this.name = name;
    this.birthDate = birthDate;
  }

  get age() {
    return Math.floor(
      (Date.now() - this.birthDate.getTime()) / (365.25 * 24 * 60 * 60 * 1000)
    );
  }
}
```

#### ⚠️ Tüm Tekrarlar Kötü Değil!

Bazen **kasıtlı tekrar** doğru çözümdür:

```javascript
// Bu DRY ihlali DEĞİL! İki farklı bağlamda farklı nedenlerle benzer kod.
// Çünkü ileride bağımsız olarak değişebilirler.

// API validasyonu (kullanıcı girdisi)
function validateApiRequest(req) {
  if (!req.body.email) throw new BadRequestError('Email required');
}

// Domain validasyonu (iş kuralı)
function validateBusinessRule(user) {
  if (!user.email) throw new DomainError('User must have email');
}
// İkisi de email kontrol ediyor AMA farklı nedenlerle!
// API kuralları değişebilir, iş kuralları değişmeyebilir veya tam tersi.
```

### 2.2 Ortogonallik (Orthogonality) 📐

#### Hikaye: Helikopter Kumandası 🚁

Helikopterin 4 kumanda kolu var ve hepsi birbirine bağlı:
- Bir kolu çekince helikopter yukarı çıkar AMA aynı zamanda sola kayar
- Sola kaymayı düzeltmek için başka bir kol çekmen lazım
- O kol da başka bir şeyi etkiler...
- Sonuç: **Basit bir hareket için 4 kolu aynı anda ayarlaman lazım!** 😰

Bu ortogonal OLMAYAN bir tasarım.

> **Ortogonal = Bir bileşeni değiştirmek, diğerlerini ETKİLEMEZ.**

```
Ortogonal SİSTEM:             Ortogonal OLMAYAN SİSTEM:
┌─────┐  ┌─────┐  ┌─────┐    ┌─────────────────────────┐
│  A  │  │  B  │  │  C  │    │   A ←→ B ←→ C ←→ D      │
│     │  │     │  │     │    │   ↕         ↕   ↕       │
│     │  │     │  │     │    │   E ←→ F ←→ G           │
└─────┘  └─────┘  └─────┘    └─────────────────────────┘
A değişince B ve C             A değişince B,C,D,E,F,G
ETKİLENMEZ ✅                  HEPSİ ETKİLENİR ❌
```

#### Ortogonal Kod Örneği

```javascript
// ❌ ORTOGONALLİK DÜŞÜK: Veritabanı değişikliği UI'ı etkiler
function getUserProfile(userId) {
  const result = db.query(`SELECT * FROM users WHERE id = ${userId}`);
  return `<div class="profile">
    <h1>${result.rows[0].first_name} ${result.rows[0].last_name}</h1>
    <p>${result.rows[0].email_address}</p>
  </div>`;
}
// DB sütun adı değişirse? → Bu fonksiyon patlar
// HTML yapısı değişirse? → Bu fonksiyon değişmeli
// İki bağımsız değişiklik aynı yeri etkiliyor! ❌
```

```javascript
// ✅ ORTOGONALLİK YÜKSEK: Her katman bağımsız
// Veri erişim katmanı
function findUserById(userId) {
  const result = db.query('SELECT * FROM users WHERE id = $1', [userId]);
  return {
    name: `${result.rows[0].first_name} ${result.rows[0].last_name}`,
    email: result.rows[0].email_address
  };
}

// Sunum katmanı
function renderProfile(user) {
  return `<div class="profile">
    <h1>${user.name}</h1>
    <p>${user.email}</p>
  </div>`;
}

// DB değişirse → sadece findUserById değişir
// HTML değişirse → sadece renderProfile değişir ✅
```

#### Ortogonallik Test Sorusu 🧪

> **"X bileşenini değiştirdiğimde, kaç tane başka dosyaya dokunmam gerekiyor?"**
> Cevap 1 ise → ortogonal ✅
> Cevap 5+ ise → ortogonal değil! ❌

### 2.3 Geri Dönülebilirlik (Reversibility) ↩️

> **"Hiçbir karar son karar değildir."**

Bugün verdiğin her teknoloji kararını yarın geri almak ihtiyacın olabilir:
- PostgreSQL'den MongoDB'ye geçiş
- REST'ten GraphQL'e geçiş
- AWS'den GCP'ye geçiş
- Monolith'ten microservices'e geçiş

```javascript
// ❌ GERİ DÖNÜLEMEZ: PostgreSQL her yere yayılmış
async function getUser(id) {
  return pool.query('SELECT * FROM users WHERE id = $1', [id]);
}

async function createOrder(data) {
  return pool.query('INSERT INTO orders (user_id, total) VALUES ($1, $2)', [data.userId, data.total]);
}
// 50 dosyada doğrudan PostgreSQL query... MongoDB'ye geçiş? Ay sürer!

// ✅ GERİ DÖNÜLEBİLİR: Repository pattern ile soyutla
class UserRepository {
  async findById(id) { ... }     // PostgreSQL implementasyonu
  async create(data) { ... }
}

// MongoDB'ye geçiş? Sadece Repository'nin iç implementasyonunu değiştir!
// 50 dosya yerine 1 dosya! ✅
```

> **Başparmak kuralı:** "Bu kararı değiştirmem gerekirse ne kadar acır?" Çok acıyorsa, arkasına bir soyutlama katmanı koy.

### 2.4 İzleyici Mermi (Tracer Bullets) 🔫

#### Hikaye: Karanlıkta Nişan Almak 🌙

Gece savaşında hedefi göremezsin. İki seçeneğin var:

1. **Karanlıkta hesap yapıp tek atış:** Rüzgarı, mesafeyi, açıyı hesapla → Tek kurşun at → Iskaladın mı bilmezsin 😬
2. **İzleyici mermi (tracer bullet):** Parlayan özel mermiler kullan. Merminin nereye gittiğini GÖRÜRSÜN. Iskalıyorsan anında düzelt.

Yazılımda:

| Yaklaşım | Analoji | Sonuç |
|---|---|---|
| **Büyük tasarım + uzun geliştirme + büyük dağıtım** | Karanlıkta hesap | 6 ay sonra "yanlış şeyi yapmışız" riski |
| **İzleyici mermi: Minimum ama çalışan uçtan uca sistem** | Parlayan mermi | Hemen feedback, hemen düzeltme |

#### Tracer Bullet Geliştirme 🎯

```
Geleneksel yaklaşım:
1. Tüm gereksinimleri topla (2 ay)
2. Tüm sistemi tasarla (1 ay)
3. Tüm kodu yaz (3 ay)
4. Tüm testleri yap (1 ay)
5. Dağıt (1 hafta)
6. "Müşteri bunu istememiş!" 😱 (7 ay boşa gitmiş)

Tracer bullet yaklaşımı:
1. En kritik özelliği belirle
2. Onu uçtan uca (UI → API → DB) en basit şekilde çalıştır (1-2 hafta)
3. Müşteriye göster → Feedback al
4. Bir sonraki özelliğe geç
5. Her iterasyonda çalışan bir sistemin var! ✅
```

```
Tracer Bullet:
UI ─────→ API ─────→ Service ─────→ DB
  basit     basit       basit        basit
  ama ÇALIŞAN! ✅

Sonra her katmanı zenginleştirirsin:
UI ─────→ API ─────→ Service ─────→ DB
  güzel     validasyonlu  tam logic    optimize
```

#### Tracer Bullet vs Prototip 🤔

| | Tracer Bullet | Prototip |
|---|---|---|
| **Amaç** | İskelet ama PRODUCTION kodu | Deney, öğrenme |
| **Kod kalitesi** | Temiz, sürdürülebilir | Hızlı, kirli, atılacak |
| **Sonrası** | Üstüne inşa edilir | ÇÖPE ATILIR |

> Prototip = Deneme tahtası (atılır) 🗑️
> Tracer bullet = Binanın çelik iskeleti (üstüne katlar eklenir) 🏗️

### 2.5 Tahmin (Estimating) 📊

#### Hikaye: "Ne Kadar Sürer?" Sorusu ⏰

PM sana soruyor: "Bu özellik ne kadar sürer?"

```
Yanlış cevap: "2 hafta" (hiç düşünmeden, göz kararı)
Doğru yaklaşım: "Bir bakmam lazım, yarına döneyim"
```

#### Tahmin Hassasiyeti 🎯

Tahminin **hassasiyet derecesin** duruma göre ayarla:

| Tahmin | Müşterinin Algısı |
|---|---|
| "Yaklaşık 6 ay" | 5-7 ay olabilir |
| "150 iş günü" | Tam 150 gün beklenir! |
| "3 hafta 2 gün" | Çok kesin — 1 gün gecikmeye tolerans yok! |

> **İpucu:** Belirsizlik yüksekse **büyük birim** kullan. Kesinlik yüksekse **küçük birim**.

| Süre | Kullan |
|---|---|
| 1-15 gün | Gün |
| 3-6 hafta | Hafta |
| 2-6 ay | Ay |
| 6+ ay | "Kesin söyleyemem, bölelim" |

#### PERT Tahmini 📐

Üç tahmin yap ve ortala:

- **O** = Optimistic (iyimser) — Her şey yolunda giderse
- **M** = Most likely (büyük ihtimalle) — Gerçekçi
- **P** = Pessimistic (kötümser) — Her şey ters giderse

$$Tahmin = \frac{O + 4M + P}{6}$$

```
Örnek: Yeni API endpoint geliştirme

O = 2 gün (basit, bildiğim teknoloji)
M = 5 gün (testler, review, küçük sorunlar)
P = 12 gün (beklenmedik entegrasyon sorunları)

Tahmin = (2 + 4×5 + 12) / 6 = 34/6 ≈ 5.7 gün → "Yaklaşık 1 hafta"
```

#### En İyi Tahmin Yöntemi: Geçmiş Deneyim 📚

```
1. İstenen şeyi anla
2. Daha önce benzer bir şey yaptın mı?
3. Alt görevlere böl
4. Her alt görevi tahmin et
5. Topla
6. Bir miktar buffer ekle (genellikle %20-30)
7. "Yaklaşık X" olarak ilet
```

> **"Tahmini iyileştirmenin en iyi yolu, önceki tahminlerinin ne kadar tuttuğunu takip etmektir."**
> Her sprint sonunda: "5 gün demiştim, 8 gün sürdü. Neden?" →  Öğren, bir sonraki tahmin daha iyi olur.

---

## 3. 🧰 Temel Araçlar

### 3.1 Düz Metin Gücü (Power of Plain Text) 📄

> **"Bilgiyi düz metin olarak sakla."**

Binary formatlar (Word, Excel, proprietary DB) sorunludur:
- 10 yıl sonra okunamazlar
- Araçlar arasında taşınamazlar
- Versiyon kontrolüne girmezler

```
❌ Binary: .docx, .xlsx, .psd, custom binary format
✅ Düz metin: .json, .yaml, .csv, .md, .sql, .env
```

```yaml
# ✅ Düz metin yapılandırma - Herkes okuyabilir, git diff yapılabilir
database:
  host: localhost
  port: 5432
  name: myapp_production
  pool_size: 10

cache:
  type: redis
  host: localhost
  port: 6379
  ttl: 3600
```

> Düz metin, **insurance policy** (sigorta poliçesi) gibidir. Belki yarın bugünkü aracı kullanamazsın, ama düz metni her zaman okuyabilirsin.

### 3.2 Shell Oyunları 🐚

> **"GUI sınırlar, Shell özgürleştirrir."**

GUI (grafiksel arayüz) ile yapabileceklerin sınırlıdır. Komut satırı ise **sınırsız kombinasyon** sunar.

```bash
# Son 24 saatte değişen JavaScript dosyalarını bul
find . -name "*.js" -mtime -1

# Kodda "TODO" yazan yerleri bul, dosya adı ve satır numarasıyla
grep -rn "TODO" src/

# En çok değişen 10 dosya (en problemli dosyalar bunlar!)
git log --pretty=format: --name-only | sort | uniq -c | sort -rg | head -10

# Tüm console.log'ları sil
find src/ -name "*.js" -exec sed -i '' '/console\.log/d' {} +

# API yanıt süresini test et
time curl -s https://api.example.com/users > /dev/null

# JSON çıktıyı güzelleştir
cat data.json | python3 -m json.tool

# Birden fazla komutu pipe ile bağla
cat access.log | grep "500" | awk '{print $7}' | sort | uniq -c | sort -rn | head
# → En çok 500 hatası veren endpoint'ler!
```

> **Her gün 5 dakikanı yeni bir komut öğrenmeye ayır.** 1 yıl sonra komut satırı ninjiası olursun! 🥷

### 3.3 Versiyon Kontrolü (Version Control) 📚

> **"Her şeyi versiyon kontrolüne al. Her. Şeyi."**

Sadece kodu değil:
- ✅ Kod
- ✅ Yapılandırma dosyaları
- ✅ Altyapı tanımları (Terraform, Kubernetes manifests)
- ✅ Dokümantasyon
- ✅ Test verileri
- ✅ Build betikleri
- ✅ Veritabanı migration'ları

```
❌ Versiyon kontrolünde OLMAMASI gerekenler:
- Şifreler, API anahtarları (bunlar için .env + vault kullan)
- Build çıktıları (node_modules, dist/)
- IDE-specific dosyalar (.idea/, .vscode/ — tartışmalı)
- Büyük binary dosyalar (videolar, vb.)
```

#### İyi Commit Mesajları 📝

```bash
# ❌ KÖTÜ
git commit -m "fix"
git commit -m "update"
git commit -m "asdfg"
git commit -m "WIP"

# ✅ İYİ: Ne, neden ve nasıl
git commit -m "fix: prevent duplicate order creation on retry

When a payment timeout occurs, the client retries the request.
Without idempotency check, this creates duplicate orders.
Added orderId-based idempotency key to prevent duplicates.

Closes #1234"
```

### 3.4 Hata Ayıklama (Debugging) 🐛

> **"Hata ayıklarken panik yapma. DÜŞÜN."**

#### Debugging Psikolojisi 🧠

```
❌ "Bu imkansız!"        → İmkansız değil, anlamamışsın
❌ "Compiler hatalı!"    → %99.9 senin kodun hatalı
❌ "Dün çalışıyordu!"    → Dün ile bugün arasında ne değişti?
❌ "Benim bilgisayarımda
    çalışıyor!"           → Ortam farkını bul
```

#### Debugging Stratejileri 🔍

**1. Yeniden Üret (Reproduce)**
Hatayı **güvenilir şekilde** tekrarlayamazsın = düzeltemezsin.

```javascript
// Hatayı yeniden üreten bir test yaz!
test('bakiye negatife düşmemeli (bug #1234)', () => {
  const account = new Account(100);
  account.withdraw(150);
  expect(account.balance).toBeGreaterThanOrEqual(0); // 🔴 FAIL → Bug'ı yakaladık!
});
```

**2. Rubber Duck Debugging 🦆**
Bir lastik ördeğe (veya herhangi birine) **sorunu baştan anlatmak.** Anlatırken genellikle sorunun cevabını kendin bulursun!

```
"Bakk ördek, şimdi burda kullanıcı oluşturuyor,
sonra şifresini hashliyor, sonra... Dur bir dakika. 
Hashlemeden ÖNCE kaydediyorum! İşte bug burada!" 🎉🦆
```

**3. İkiye Bölme (Binary Search Debugging)**
```
Hata oluşuyor.
Kodun ortasına bir log koy.
Log'a kadar mı sorun, sonrası mı?
  → Sorunlu yarıyı belirle
  → O yarının ortasına log koy
  → Tekrarla
  → Suçlu satırı buldun! 🎯
```

**4. git bisect**
```bash
# Git'in binary search'ü! Hangi commit bug'ı getirdi?
git bisect start
git bisect bad          # Şu anki commit hatalı
git bisect good v1.0    # v1.0'da çalışıyordu
# Git seni commit'ler arasında gezdirir, sen "good/bad" dersin
# Suçlu commit'i bulur! 🕵️
```

**5. Varsayımlarını Sorgula**
Hata bulamıyorsan, **emin olduğun şeylerden birinde** yanılıyorsundur!

```javascript
// "Bu fonksiyon kesin doğru değer döndürüyor" → Emin misin? Log at!
const user = await getUser(id);
console.log('User:', JSON.stringify(user, null, 2)); // 😱 null dönüyormuş!
```

> **"Debugging, bir dedektif romanı okumak gibidir — ama katil SENSİN."** 🔍😄

### 3.5 Metin İşleme (Text Manipulation) ✂️

Pragmatik programcılar **metin işleme araçlarını** bilir:

| Araç | Ne İşe Yarar |
|---|---|
| `sed` | Stream editor — metin değiştirme |
| `awk` | Sütunlu veri işleme |
| `jq` | JSON işleme |
| `regex` | Desen eşleme |
| `sort`, `uniq`, `wc` | Sayma, sıralama, tekilleştirme |

```bash
# package.json'dan dependency sayısını öğren
cat package.json | jq '.dependencies | length'

# Tüm dosyalarda "var " ifadesini "const " ile değiştir
find src/ -name "*.js" -exec sed -i '' 's/var /const /g' {} +

# En uzun 5 dosyayı bul (satır sayısına göre)
find src/ -name "*.js" -exec wc -l {} + | sort -rn | head -5

# Git log'dan katkıda bulunan geliştiricileri ve commit sayılarını göster
git shortlog -sn --no-merges
```

---

## 4. 😱 Pragmatik Paranoya

### 4.1 Sözleşme ile Tasarım (Design by Contract — DBC) 📜

#### Hikaye: Restoran Sözleşmesi 🍽️

Bir restorana gittiğinde **yazılı olmayan bir sözleşme** var:

- **Senin sorumluluğun (Precondition):** Para getir, giyinik gel, menüden sipariş ver
- **Restoranın sorumluluğu (Postcondition):** Sipariş ettiğin yemeği, yenilebilir kalitede getirmek
- **Değişmez (Invariant):** Restoran açık olduğu sürece mutfak çalışır

```javascript
// Design by Contract örneği
function withdraw(account, amount) {
  // PRECONDITION — Çağıranın sorumluluğu
  if (amount <= 0) throw new Error('Tutar pozitif olmalı');
  if (amount > account.balance) throw new Error('Yetersiz bakiye');

  // İŞLEM
  account.balance -= amount;

  // POSTCONDITION — Fonksiyonun garantisi
  if (account.balance < 0) throw new Error('INVARIANT İHLALİ: Bakiye negatif!');
  // Bu satır asla çalışmamalı — çalışırsa kodda ciddi bug var!

  return account.balance;
}
```

### 4.2 Erken Çök (Crash Early) 💥

> **"Ölü programlar yalan söylemez."**

Hata olduğunda sessizce devam etmek, **çok daha büyük hatalar**a yol açar.

```javascript
// ❌ KÖTÜ: Hatayı yut, devam et
function readConfig(path) {
  try {
    return JSON.parse(fs.readFileSync(path, 'utf-8'));
  } catch (error) {
    return {};  // 😱 Config dosyası yokmuş gibi devam et!
    // Uygulama çalışır ama YANLIŞ ayarlarla! Çok daha tehlikeli!
  }
}

// ✅ İYİ: Hata varsa HEMEN dur ve söyle
function readConfig(path) {
  try {
    return JSON.parse(fs.readFileSync(path, 'utf-8'));
  } catch (error) {
    throw new Error(
      `Kritik: Config dosyası okunamadı: ${path}. ` +
      `Uygulama başlatılamaz. Hata: ${error.message}`
    );
    // Uygulama BAŞLAMAZ. Sorunu HEMEN fark edersin.
  }
}
```

> **Analoji:** Arabanın motor ışığı yandığında iki seçenek:
> - ❌ Işığın üstüne bant yap, sürmeye devam et → Motor yanar 🔥
> - ✅ Dur, servise götür → Motor kurtulur ✅

### 4.3 Assertive Programming (İddialı Programlama) 💪

> **"Eğer olamaz diyorsan, KONTROL ET."**

```javascript
// "Bu dizi asla boş olmaz" → Emin misin?
function processItems(items) {
  // ✅ Assert ile kontrol et
  console.assert(items.length > 0, 'items dizisi boş olamaz!');
  console.assert(
    items.every(item => item.price >= 0),
    'Tüm fiyatlar pozitif olmalı!'
  );

  // Artık güvenle devam edebilirsin
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

```javascript
// Daha güçlü bir assert helper
function assert(condition, message) {
  if (!condition) {
    throw new Error(`Assertion Failed: ${message}`);
  }
}

function divide(a, b) {
  assert(b !== 0, 'Sıfıra bölme hatası');
  assert(typeof a === 'number', 'a bir sayı olmalı');
  assert(typeof b === 'number', 'b bir sayı olmalı');
  return a / b;
}
```

> **Assert'ler production'da kalmalı mı?** Tartışmalı, ama pragmatik yaklaşım: **Performans etkisi yoksa kalsın!** Hataları erken yakalamak her zaman iyidir.

### 4.4 Kaynakları Dengele (Resource Balancing) ⚖️

> **"Başlatan bitirmeli. Açan kapatmalı. Ayıran geri vermeli."**

```javascript
// ❌ KÖTÜ: Kaynak açılıyor ama her durumda kapatılmıyor
async function processFile(path) {
  const file = await fs.open(path, 'r');
  const data = await file.readFile('utf-8');
  const result = JSON.parse(data);      // 💥 Bu satır hata fırlatırsa?
  await file.close();                     // ← ÇALIŞMAZ! Dosya açık kalır! 😱
  return result;
}

// ✅ İYİ: try-finally ile kaynak temizliği garanti
async function processFile(path) {
  const file = await fs.open(path, 'r');
  try {
    const data = await file.readFile('utf-8');
    return JSON.parse(data);
  } finally {
    await file.close();  // ← Hata olsa bile ÇALIŞIR! ✅
  }
}

// ✅ DAHA İYİ: with deseni (bazı dillerde)
// Node.js'te henüz tam yok ama benzer pattern:
async function processFile(path) {
  const data = await fs.readFile(path, 'utf-8'); // Otomatik aç-oku-kapat
  return JSON.parse(data);
}
```

**İç içe kaynaklar:**
Açma sırası: A → B → C
Kapama sırası: C → B → A (ters sıra, yığın gibi!)

```javascript
// ✅ İYİ: LIFO (Last In, First Out) sırasında kapat
async function transfer() {
  const sourceDb = await connectDb('source');     // 1. aç
  const targetDb = await connectDb('target');     // 2. aç

  try {
    await doTransfer(sourceDb, targetDb);
  } finally {
    await targetDb.close();    // 2. kapat (son açılan ilk kapanır)
    await sourceDb.close();    // 1. kapat
  }
}
```

### 4.5 Farlarını Aşma (Don't Outrun Your Headlights) 🔦

> **"Farlarının gördüğünden daha ilerisini tahmin etmeye çalışma."**

Gece karanlık bir yolda araba kullanıyorsun. Farların sadece 100 metre ilerisini aydınlatıyor. 200 metre ileride ne var? BİLMİYORSUN! Ve bilmen de gerekmiyor — sadece farlarının gördüğü alana ODAKLAN!

```
Yazılımda aynı prensip:

❌ "3 yıl sonrası için mimari tasarlayalım!" 
   → 3 yıl sonra ne olacağını BİLMİYORSUN!
   → Teknoloji değişir, gereksinimler değişir, takım değişir!

✅ "Şimdi bildiğimizle EN İYİ kararı alalım, 
    değiştirmeyi KOLAY tutalım!"
   → Geri dönülebilirlik + küçük adımlar!

PRATİK KURALLAR:
  → Gelecekte "belki lazım olur" diye kod yazma → YAGNI!
  → Her adımda sonraki adımı görebilir ol → küçük iterasyonlar!
  → Tahmin edemediğin şeyleri ESNEK bırak → soyutlama katmanı!
  → "1 adım ileri bak, 10 adım ileriyi HAYAL ETME" 🔦
```

Ayrıca dışarıdan gelen hiçbir veriye güvenme — **her zaman doğrula:**

```javascript
// ❌ KÖTÜ: Kullanıcının gönderdiği veriye güvenme
app.post('/transfer', (req, res) => {
  const { fromAccount, toAccount, amount } = req.body;
  transferMoney(fromAccount, toAccount, amount);
  // Ya kullanıcı amount: -1000 gönderirse? Ters transfer! 😱
});

// ✅ İYİ: Her şeyi doğrula
app.post('/transfer', authenticate, (req, res) => {
  const { toAccount, amount } = req.body;
  const fromAccount = req.user.accountId; // Kendi hesabını oturumdan al
  
  if (!Number.isFinite(amount) || amount <= 0) {
    throw new ValidationError('Geçersiz tutar');
  }
  if (amount > MAX_TRANSFER_LIMIT) {
    throw new ValidationError('Transfer limiti aşıldı');
  }
  
  transferMoney(fromAccount, toAccount, amount);
});
```

---

## 5. 🌊 Bükülebilir Kod (Bend or Break)

### 5.1 Bağlantıyı Azalt (Decoupling) 🔗

> **"Az bağlantılı kod, değiştirilmesi kolay koddur."**

#### Tell, Don't Ask (Söyle, Sorma) 📢

```javascript
// ❌ ASK (Sorma): Veriyi al, kararı kendin ver
function applyDiscount(customer, order) {
  if (customer.loyaltyPoints > 1000) {     // Müşterinin verisini SORUYORSUN
    if (customer.membershipType === 'gold') {  // Daha fazla SORUYORSUN
      order.total *= 0.8;                   // Kararı SEN veriyorsun
    } else {
      order.total *= 0.9;
    }
  }
}

// ✅ TELL (Söyle): O işi yapması gereken nesneye SÖYle
function applyDiscount(customer, order) {
  const discount = customer.getDiscount();  // Müşteriye "indirimini ver" de
  order.applyDiscount(discount);            // Siparişe "indirimi uygula" de
}

class Customer {
  getDiscount() {
    if (this.loyaltyPoints > 1000) {
      return this.membershipType === 'gold' ? 0.2 : 0.1;
    }
    return 0;
  }
}
```

#### Law of Demeter (Demeter Yasası) — Sadece Bir Nokta! 🔴

```javascript
// ❌ Tren kazası — her nokta bir bağımlılık
order.getCustomer().getAddress().getCity().getZipCode();

// ✅ Tek nokta
order.getDeliveryZipCode();
```

### 5.2 Olaylarla Programlama (Events & Reactive) ⚡

Bileşenler arasında **doğrudan çağrı yerine olay (event)** kullan.

#### Pub/Sub (Yayınla/Abone Ol) Pattern

```javascript
// ❌ SIKICA BAĞLI: OrderService doğrudan herkesi çağırıyor
class OrderService {
  async createOrder(data) {
    const order = await this.saveOrder(data);
    await this.emailService.sendConfirmation(order);   // Bağımlılık!
    await this.inventoryService.reduceStock(order);     // Bağımlılık!
    await this.analyticsService.trackPurchase(order);   // Bağımlılık!
    await this.loyaltyService.addPoints(order);         // Bağımlılık!
    // Yeni servis eklersen? Bu dosyayı değiştirmen lazım! 😩
  }
}
```

```javascript
// ✅ GEVŞEk BAĞLI: Event yayınla, kim dinlerse dinlesin
class OrderService {
  async createOrder(data) {
    const order = await this.saveOrder(data);
    eventBus.emit('order.created', order); // Tek satır! 🎉
  }
}

// Her servis kendi ilgilendiği olayı dinler
eventBus.on('order.created', (order) => emailService.sendConfirmation(order));
eventBus.on('order.created', (order) => inventoryService.reduceStock(order));
eventBus.on('order.created', (order) => analyticsService.trackPurchase(order));
eventBus.on('order.created', (order) => loyaltyService.addPoints(order));

// Yeni servis? OrderService'e DOKUNMADAN ekle!
eventBus.on('order.created', (order) => newService.doSomething(order)); ✅
```

### 5.3 Dönüşüm Programlama (Transform Programming) 🔄

> **"Programlama = veriyi bir formdan diğerine dönüştürmek."**

Nesne içindeki state'i değiştirmek yerine, veriyi **pipeline** boyunca DÖNÜŞTÜR.

```javascript
// ❌ State-based: Nesneyi mutate ediyorsun
function processOrder(order) {
  order.validated = true;
  order.total = calculateTotal(order.items);
  order.tax = order.total * 0.18;
  order.grandTotal = order.total + order.tax;
  order.status = 'processed';
  return order;
}

// ✅ Pipeline: Her adım yeni bir değer üretir
const processOrder = (rawOrder) =>
  [rawOrder]
    .map(validate)
    .map(calculateTotal)
    .map(addTax)
    .map(markAsProcessed)[0];

// Veya daha okunabilir:
function processOrder(rawOrder) {
  const validated = validate(rawOrder);
  const withTotal = calculateTotal(validated);
  const withTax = addTax(withTotal);
  const processed = markAsProcessed(withTax);
  return processed;
}

// Her fonksiyon saf (pure): input → output, yan etki yok!
function addTax(order) {
  return {
    ...order,
    tax: order.total * 0.18,
    grandTotal: order.total * 1.18
  };
}
```

> **Pipeline düşüncesi:** data → f1 → f2 → f3 → f4 → result
> Unix pipe'ları gibi: `cat file | grep "error" | sort | uniq -c`

### 5.4 Yapılandırma (Configuration) ⚙️

> **"Detayları kodun dışında tut."**

Değişebilecek her şeyi **yapılandırma** olarak dışarı al:

```javascript
// ❌ KÖTÜ: Ayarlar kodun içinde hardcoded
const MAX_RETRY = 3;
const API_URL = 'https://api.production.com';
const CACHE_TTL = 3600;
const RATE_LIMIT = 100;

// ✅ İYİ: Ayarlar dışarıda, ortam değişkenlerinde
// config.js
module.exports = {
  maxRetry: parseInt(process.env.MAX_RETRY) || 3,
  apiUrl: process.env.API_URL || 'http://localhost:3000',
  cacheTtl: parseInt(process.env.CACHE_TTL) || 3600,
  rateLimit: parseInt(process.env.RATE_LIMIT) || 100,
};
```

Yapılandırılması gereken şeyler:
- 🔧 Veritabanı bağlantıları
- 🔧 API URL'leri ve anahtarları
- 🔧 Timeout süreleri
- 🔧 Log seviyeleri
- 🔧 Feature flag'ler
- 🔧 Rate limit'ler
- 🔧 Email ayarları

---

## 6. ⚡ Eşzamanlılık (Concurrency)

### 6.1 Temporal Coupling'i Kır ⏰

**Temporal coupling** = İşlerin belirli bir sırada yapılması zorunluluğu.

```javascript
// ❌ Temporal coupling: A, B, C sırayla olmalı
async function init() {
  await loadConfig();        // 1. önce config
  await connectDatabase();   // 2. sonra DB
  await startServer();       // 3. en son server
}
// Config ve DB bağlantısı aslında bağımsız! Neden sırayla?

// ✅ Bağımsız işleri paralel yap
async function init() {
  const [config, db] = await Promise.all([
    loadConfig(),           // Paralel!
    connectDatabase()       // Paralel!
  ]);
  await startServer(config, db); // Bu ikisine bağlı, sıralı
}
```

### 6.2 Paylaşılan State = Sorun! 🚨

```javascript
// ❌ TEHLİKELİ: Paylaşılan mutable state
let requestCount = 0;

app.use((req, res, next) => {
  requestCount++; // 🚨 Eşzamanlı isteklerde yarış durumu!
  next();
});

// ✅ GÜVENLİ: Atomik operasyonlar kullan
// Redis ile:
app.use(async (req, res, next) => {
  await redis.incr('request_count'); // Atomik! ✅
  next();
});
```

### 6.3 Actor Model 🎭

Her "aktör" bağımsız çalışır, mesajlaşarak iletişim kurar.

```javascript
// Kavramsal Actor modeli
class OrderActor {
  async handleMessage(message) {
    switch (message.type) {
      case 'CREATE_ORDER':
        const order = await this.createOrder(message.data);
        paymentActor.send({ type: 'CHARGE', order });
        break;
      case 'ORDER_PAID':
        await this.updateStatus(message.orderId, 'paid');
        shippingActor.send({ type: 'SHIP', orderId: message.orderId });
        break;
    }
  }
}
```

> Aktörler birbirinin state'ine **asla** doğrudan erişmez. Sadece **mesaj** gönderir. Bu sayede yarış durumu olmaz!

---

## 7. ✍️ Kodlarken (While You Are Coding)

### 7.1 Sürüngen Beyin Programlaması 🦎

> **"İçgüdülerine güven, ama doğrula."**

Bazen bir şeyin yanlış olduğunu **hissedersin** ama parmağını koyamazsın.

```
Durum: Bir kodu yazıyorsun, her şey "doğru" görünüyor ama içinde bir huzursuzluk var.

❌ Yanlış: "Neyse, çalışıyor, geçelim"
✅ Doğru: "Dur. Bu huzursuzluk neden? Bir şeyi mi kaçırıyorum?"
```

İçgüdün seni uyarıyorsa:
1. **Dur.** Yazmaya devam etme.
2. **Kendine sor:** "Bu neden rahatsız ediyor?"
3. **Prototip yap:** Belirsizliği çözmek için küçük bir deney yap.
4. **Yürüyüşe çık:** Bazen ekrandan uzaklaşmak cevabı getirir 🚶

### 7.2 Tesadüfe Göre Programlama 🎲

> **"Kodun çalışması = kodun doğru olması DEĞİLDİR!"**

#### Hikaye: Mayın Tarlası 💣

Bir mayın tarlasında yürüyorsun. 10 adım attın, patlamadı. Bu, güvenli bir yolda olduğun anlamına mı gelir? **HAYIR!** Sadece şanslısın.

```javascript
// ❌ "Çalışıyor" ama tesadüfen çalışıyor
function getFirstUser() {
  const users = db.query('SELECT * FROM users');
  return users[0]; // "İlk kullanıcı hep Ali oluyor" → TESADÜF!
  // Veritabanı sıralama garantisi vermez!
  // Bir gün farklı bir kullanıcı dönecek ve her şey patlayacak 💥
}

// ✅ Kasıtlı olarak doğru
function getFirstRegisteredUser() {
  const users = db.query('SELECT * FROM users ORDER BY created_at ASC LIMIT 1');
  return users[0]; // Açıkça "en eski kullanıcı" diyorsun
}
```

**Tesadüfi programlamanın belirtileri:**
- "Neden çalıştığını bilmiyorum ama çalışıyor" 🚩
- "Bu satırı kaldırınca patlıyor ama neden olduğunu bilmiyorum" 🚩
- "Stack Overflow'dan kopyaladım" 🚩
- "Sırası önemli ama hangi sırda olacağını bilmiyorum" 🚩

> **Kasıtlı programla:** Her satırını NEDEN yazdığını bilmelisin.

### 7.3 Algoritma Hızı (Algorithm Speed) ⏱️

Big O'yu hatırla (Grokking Algorithms'ten!) ve kararlarında kullan:

```javascript
// Gerçek dünya kararı: 10.000 kullanıcıda admin olanları bul

// Yaklaşım 1: Her sorgu için tüm listeyi tara — O(n)
function isAdmin(userId, allUsers) {
  return allUsers.find(u => u.id === userId)?.role === 'admin';
}
// 10.000 kullanıcı × 1.000 sorgu/sn = 10.000.000 işlem/sn 😰

// Yaklaşım 2: Set/Map ile — O(1)
const adminSet = new Set(allUsers.filter(u => u.role === 'admin').map(u => u.id));
function isAdmin(userId) {
  return adminSet.has(userId);
}
// 1.000 sorgu/sn = 1.000 işlem/sn 😎
```

### 7.4 Refactoring 🔄

> **"Refactoring = Dış davranışı değiştirmeden iç yapıyı iyileştirmek."**

#### Ne Zaman Refactor Edilmeli?

- **DRY ihlali:** Aynı kodu 2. kez kopyalıyorsan → Dur, refactor yap
- **Ortogonal olmayan tasarım:** Bir değişiklik 5 dosyayı etkiliyorsa
- **Eskimiş bilgi:** İş kuralları değişmiş ama kod eski
- **Performans:** Ölçüm sonrasında yavaş noktayı optimize et
- **"Bana kötü kokuyor":** İçgüdün bir şeyin yanlış olduğunu söylüyorsa

#### Refactoring Kuralları

```
1. ✅ Test olmadan refactoring YAPMA (önce test yaz!)
2. ✅ Küçük adımlarla ilerle
3. ✅ Her adımda testleri çalıştır
4. ❌ Refactoring ile yeni özellik eklemeyi KARIŞTIRMA
5. ❌ "Büyük refactoring" planları yapma — küçük ve sürekli yap
```

### 7.5 Test ile Kodlama 🧪

> **"Test, bulduğumuz hataları değil, KODUN ne yapması gerektiğini gösterir."**

**Test-first düşüncesi:**

```javascript
// ÖNCE testi düşün:
// "Kullanıcı 100 TL'lik ürünü sepete ekleyince, sepet toplamı 100 TL olmalı"

test('ürün sepete eklenince toplam güncellenmeli', () => {
  const cart = new ShoppingCart();
  cart.addItem({ name: 'Kitap', price: 100 });
  expect(cart.getTotal()).toBe(100);
});

// SONRA kodu yaz:
class ShoppingCart {
  #items = [];

  addItem(item) {
    this.#items.push(item);
  }

  getTotal() {
    return this.#items.reduce((sum, item) => sum + item.price, 0);
  }
}
```

> **Test düşünmek = tasarım düşünmek.** Test yazmak seni daha iyi API tasarımı yapmaya zorlar.

### 7.6 İsimlendirme 📛

> **"Bilgisayar biliminde iki zor şey var: cache invalidation ve isimlendirme."**
> — Phil Karlton

Pragmatic Programmer'a göre isimlendirme kuralları:

1. **Kültürü yansıt:** Takımın kullandığı terimleri kullan
2. **Tutarlı ol:** `get`/`fetch`/`retrieve`/`find` — birini seç, her yerde kullan
3. **İsmi değiştirmekten korkma:** Kötü isim keşfedince HEMEN düzelt
4. **Proje sözlüğü oluştur:** Ubiquitous Language (DDD'den)

```javascript
// ❌ Tutarsız isimlendirme
getUserById();
fetchOrder();
retrieveProduct();
findCustomer();
// get? fetch? retrieve? find? HANGİSİ?!

// ✅ Tutarlı isimlendirme
getUser();
getOrder();
getProduct();
getCustomer();
// Hep "get" — beyin yormaz!
```

---

## 8. 📋 Projeden Önce

### 8.1 Gereksinim Çukuru (Requirements Pit) 🕳️

> **"Gereksinimler toplanmaz, kazılır. Yüzeyde gördüğün, buzbuğun tepesidir."**

#### Hikaye: Otomatik Kapı 🚪

Müşteri: "Kapı otomatik açılsın."

Kolay, değil mi? Dur bakalım:

```
- Kapı ne zaman açılsın? Birisi yaklaşınca? Ne kadar yaklaşınca?
- Kedi yaklaşırsa da açılsın mı?
- Aynı anda iki kişi gelirse?
- Kapı açıkken biri çıkmaya çalışırsa?
- Yangın alarmında ne olacak?
- Elektrik kesilirse?
- Kış aylarında rüzgar eserse sürekli açık mı kalsın?
```

**Bir cümlelik gereksinim, 20 soruya dönüştü!** 🤯

> **Gereksinim, bir şeyin ne yapması gerektiğini ifade eder — NASIL yapılacağını değil.**

#### Gereksinim Keşif Teknikleri 🔍

```
1. "Neden?" sor — Asıl ihtiyacı bul
   Müşteri: "Login sayfasına captcha ekle"
   Sen: "Neden?" 
   Müşteri: "Bot saldırıları oluyor"
   Sen: "Rate limiting + IP blocking daha iyi olabilir" 💡

2. Kullanıcı gibi düşün — O anı yaşa
   "Ben kullanıcı olsam ne yapmak isterdim?"

3. Prototip göster — Soyut tartışmak yerine somut göster
   "Böyle bir şey mi istiyorsunuz?" 

4. Glossary (Sözlük) oluştur — Herkes aynı şeyi mi kastediyor?
   "Kullanıcı" = Kayıtlı kullanıcı mı? Ziyaretçi mi? Admin mi?
```

### 8.2 İmkansız Bulmacaları Çözmek 🧩

Bir problemi çözemediğini hissediyorsan, muhtemelen **yanlış soruyu** soruyorsundur.

> **"Kutuyu düşünme: Kutunun sınırlarını BUL."**

```
"Bu widget'ı real-time güncelleyemiyorum"
  → Gerçekten real-time mi olmalı? 5 saniyelik gecikme kabul edilebilir mi?

"Bu 1 milyon kaydı sıralayamıyorum"
  → Hepsini sıralamak zorunda mısın? İlk 100'ü göstersen yeter mi?

"Bu API çok yavaş"
  → API'yi hızlandırmak yerine cache'lemek yeterli mi?
```

**Kısıtlamaları sorgula:**
- Bu kısıtlama gerçek mi, yoksa varsayım mı?
- Kısıtlamayı kaldıracak daha basit bir yol var mı?
- Farklı bir bakış açısıyla problemi yeniden tanımlayabilir misin?

### 8.3 Birlikte Çalışmak 🤝

> **"Eşli programlama (pair programming) veya mob programming dene."**

```
Tek başına çalışma:
🧑‍💻 → Kafanda takılır → Saatler geçer → Hâlâ takılı

Eşli programlama:
🧑‍💻🧑‍💻 → "Hmm, şöyle olsa?" → "Aslında şunu deneyelim" → 15 dk'da çözüm!
```

Eşli programlama her zaman uygun değil ama özellikle şu durumlarda çok faydalı:
- Karmaşık bir problemi çözerken
- Yeni bir takım üyesini onboarding yaparken
- Kritik bir mimari kararı verirken
- Sıkıştığını hissettiğinde

### 8.4 Çevikliğin Özü (The Essence of Agility) 🏃

> **"Agile bir süreç değil, bir DEĞERLER sistemidir."**

```
❌ Agile sahte:
- "Sprint yapıyoruz" ama gereksinimler hiç değişmiyor
- "Stand-up yapıyoruz" ama 45 dakika sürüyor
- "Agile'ız" ama 6 aylık waterfall planı var
- Jira board'da 200 ticket var ama kimse bakmıyor

✅ Gerçek Agile:
- Kısa iterasyonlarla çalışan yazılım üret
- Feedback al, planı değiştir
- Değişime direnme, kucakla
- Bireylere ve etkileşimlere değer ver
```

Agile'ın özü **tek bir cümle:**

> **"Ne yapacağını tam bilmediğin bir ortamda, küçük adımlarla ilerle ve sürekli feedback al."**

---

## 9. 🏗️ Pragmatik Projeler

### 9.1 Pragmatik Takımlar 👥

Bireysel pragmatik prensiplerin tümü **takım seviyesinde** de geçerli:

| Birey | Takım |
|---|---|
| Kırık pencereyi tamir et | Takım düzeyinde kod kalite standartları belirle |
| Bilgi portföyüne yatırım yap | Tech talk'lar, kitap kulüpleri, knowledge sharing |
| İletişim kur | Sprint retrospektifi, ADR'ler, RFC'ler |
| DRY | Paylaşılan kütüphaneler, ortak araçlar |
| Ortogonallik | Microservices, takım bağımsızlığı |

### 9.2 Onu Adlandırabiliyorsan, Otomatikleştir! 🤖

> **"Manuel yapman gereken her tekrarlayan iş, bir robot adayıdır."**

| Manuel İş | Otomatik Çözüm |
|---|---|
| "PR'a bakayım, lint doğru mu" | CI/CD'de otomatik lint |
| "Build edip test edeyim" | CI pipeline |
| "Staging'e deploy edeyim" | Otomatik deployment |
| "Veritabanı migration yapayım" | Migration araçları |
| "Yeni proje oluşturayım" | Template/scaffolding |
| "Dependency güncelle" | Renovate/Dependabot |
| "Test coverage raporla" | CI'da otomatik coverage report |

```yaml
# CI/CD Pipeline örneği (GitHub Actions / Bitbucket Pipelines)
# ✅ İnsan müdahalesine gerek yok!
steps:
  - lint          # Kod kalitesi
  - test          # Testler
  - security-scan # Güvenlik taraması
  - build         # Build
  - deploy-staging # Staging'e deploy
  - smoke-test    # Canlı test
  - deploy-prod   # Production'a deploy (onay sonrası)
```

> **Kural:** Bir işi 2. kez manuel yapıyorsan, 3. kez otomatikleştir.

### 9.3 Kullanıcıları Mutlu Et 😊

> **"Yazılım geliştirmenin amacı kullanıcıları mutlu etmektir."**

Teknik mükemmellik, kullanıcı mutlu değilse anlamsızdır:

```
❌ "Harika bir microservices mimarisi yaptık!"
   → Ama kullanıcılar sipariş veremiyor 😢

✅ "Basit bir monolith ama kullanıcılar 2 saniyede sipariş veriyor!"
   → Kullanıcılar mutlu! 😊

Soru hep şu olmalı: "Bu benim kullanıcıma nasıl fayda sağlıyor?"
```

### 9.4 Gurur ve Önyargı 🏆

> **"İmzanı atabilirsin. Kodun senin eserin, gurur duy."**

```
Eski zanaatkarlar eserlerini imzalardı.
Bir mobilya ustası yaptığı sandalyenin altına ismini kazırdı.
Çünkü o sandalyeyle gurur duyardı.

Sen de kodunla gurur duy.
Ama gururun seni körleştirmesin!

✅ "Bu kodu ben yazdım, arkasındayım" — GURUR
❌ "Bu kodda hata olamaz çünkü ben yazdım" — ÖNYARGI
```

---

## 10. 🎬 Son Sözler

### Kitabın Tüm İpuçları (Tips) — Özet Tablosu 📋

| # | Tip | Açıklama |
|---|---|---|
| 1 | **Zanaatınla ilgilen** | İşini ciddiye al |
| 2 | **Düşün! İşin hakkında düşün** | Otopilotta kodlama |
| 3 | **Değişimi katalize et** | Taş çorba yap |
| 4 | **Büyük resmi hatırla** | Kaynar su kurbağası olma |
| 5 | **Yeterince iyi yazılım yap** | Mükemmel, iyinin düşmanı |
| 6 | **Bilgi portföyüne yatırım yap** | Her yıl yeni şeyler öğren |
| 7 | **Eleştirel düşün** | Her kaynağı sorgula |
| 8 | **Kırık pencere bırakma** | İlk kötü kodu tolere etme |
| 9 | **DRY** | Her bilgi tek yerde |
| 10 | **Ortogonallik** | Bağımsız bileşenler |
| 11 | **Geri dönülebilirlik** | Kararları geri almak kolay olsun |
| 12 | **İzleyici mermiler** | Uçtan uca basit ama çalışan kod |
| 13 | **Prototiple** | Belirsizlikleri deney ile çöz |
| 14 | **Alanın diline yaklaş** | DSL ve Ubiquitous Language |
| 15 | **Tahmin et** | PERT, geçmiş deneyim |
| 16 | **Düz metin gücü** | Binary formatlardan kaçın |
| 17 | **Shell'i kullan** | GUI'den bağımsız ol |
| 18 | **Editörünü öğren** | Kısayollar, makrolar |
| 19 | **Versiyon kontrolü** | Her şeyi versiyonla |
| 20 | **Hata ayıklama: Panik yapma** | Düşün, adım adım izle |
| 21 | **Sözleşme ile tasarla** | Pre/post condition, invariant |
| 22 | **Erken çök** | Sessiz hata, gizli felaket |
| 23 | **Assert kullan** | "İmkansız" dediğin şeyi doğrula |
| 24 | **Kaynakları dengele** | Açan kapatmalı |
| 25 | **Tell, Don't Ask** | Vermeyi söyle, veriyi sorma |
| 26 | **Olaylara yanıt ver** | Event-driven tasarım |
| 27 | **Dönüşüm pipeline'ları** | State yerine transform |
| 28 | **Yapılandırmayı dışa al** | Hardcoded değer yasak |
| 29 | **Tesadüfe programlama** | Neden çalıştığını BİL |
| 30 | **Refactor et** | Küçük, sürekli, testli |
| 31 | **Test-first düşün** | Test = tasarım aracı |
| 32 | **İsimlendirmeye özen göster** | İsim = dokümantasyon |
| 33 | **Otomatikleştir** | Manuel iş = hata kaynağı |
| 34 | **Kullanıcıyı mutlu et** | Asıl amaç bu |
| 35 | **İmzanı at, gurur duy** | Ama önyargıya kapılma |

### 🤖 Yapay Zeka Çağında Pragmatik Mühendis

```
Pragmatik Programmer'ın İPUÇLARI AI çağında DAHA DA ÖNEMLİ!

1. "TESADÜFE PROGRAMLAMA" (Tip 29) → AI ile AMPLIFIED!
   → AI kodu üretiyor → çalışıyor → AMA neden çalıştığını BİLMİYORSUN!
   → En tehlikeli senaryo: "Copilot yazdı, test geçti, deploy ettim"
   → Pragmatik mühendis: "Neden çalıştığını ANLA, sonra KULLAN!" ✅

2. "DRY" → AI aynı kodu her seferinde biraz FARKLI üretir!
   → 3 yerde benzer ama farklı validation kodu → DRY ihlali!
   → Pragmatik mühendis: AI çıktısını BIRLEŞTIR ve SOYUTLA!

3. "IZLEYICI MERMILER" → AI ile hızlı prototip!
   → "Bana bir REST API iskeleti oluştur" → tracer bullet!
   → Hemen çalışan bir uç-uca akış → sonra KALITE ekle!

4. "RUBBER DUCK DEBUGGING" → AI artık ördek!
   → "Şu sorunu ChatGPT'ye ANLAT" → anlatırken çözümü 
     genellikle KENDİN bulursun!
   → Ama dikkat: AI her zaman doğru söyleMEZ → DOĞRULA!

GERÇEK DÜNYADAN ÖRNEKLER:

NETFLIX → Geri Dönülebilirlik (Reversibility)
  → Her feature, feature flag arkasında → anında kapatılabilir!
  → "Chaos Engineering" = pragmatik paranoyanın EN uç hali!
  → "Bir şeyleri bilerek KIRMAK → ne kadar dayanıklı olduğunu görmek"

SPOTIFY → Ortogonallik
  → Squad modeli: her takım bağımsız → birbirinden ortogonal!
  → Bir squad'ın değişikliği diğerlerini ETKILEMEZ!

AMAZON → "Two Pizza Teams" + DRY
  → 2 pizzanın doyurabileceği kadar küçük takımlar
  → API-First: her takım servisini API ile SUNAR → ortogonal!
```

### Bu Kitap Sana Ne Kazandırır? 🎁

```
ÖNCE:                              SONRA:
"Kod çalışıyor, yeter"           → "Kod temiz, test edilmiş, sürdürülebilir"
"Her şeyi ben yaparım"           → "Otomatikleştir, delege et, işbirliği yap"
"Bu teknoloji her yerde kullanılır, → "Bu BİZİM problemimize uygun mu?"
  biz de kullanalım"
"Hata oldu, panik!"              → "Sakin ol, yeniden üret, düşün, çöz"
"Dün çalışıyordu"                → "Ne değişti? git bisect!"
"Tam bilmiyorum ama idare eder"  → "Neden çalıştığını bilmeliyim"
"Gereksinimler belli, başlayalım" → "Gerçekten anladığımızdan emin olalım"
```

### Öğrenme Yolculuğu 🛤️

```
📗 Grokking Algorithms   → Algoritma temeli ✅
📕 Clean Code            → Kod kalitesi ✅
📘 The Pragmatic Programmer → Mühendislik zihniyeti ✅  ← BURADASİN
📙 The Missing README    → Kariyer temeli (sıradaki!)
🌐 teachyourselfcs.com   → CS boşluklarını doldur
```

---

> **"İşe bir taşla başla. Sonra havuç ekle. Sonra patates. Sonra et.
> Ve bir baktığında, ortada harika bir çorba var."** 🍲
>
> İlk adımı at. Küçük başla. Pragmatik ol.
> **Mükemmel değil, YETERINCE İYİ ve SÜREKLI İYİLEŞEN bir mühendis ol.** 🚀
