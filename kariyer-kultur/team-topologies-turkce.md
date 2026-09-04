# 🧩 Team Topologies — Türkçe Kapsamlı Rehber

> **"Yazılım mimarinizi takım yapınız belirler. O hâlde önce takımları tasarlayın."**
> — Matthew Skelton & Manuel Pais, *Team Topologies* (2019)

Bu rehber, modern organizasyon tasarımının en etkili kitabını Türkçe olarak anlatır. Kitabın çekirdeği devrimci bir fikirdir: **Takım yapısı bir İK meselesi değil, bir mimari karardır.** İyi yazılım, doğru sınırlara bölünmüş, bilişsel yükü yönetilebilir takımlardan çıkar.

---

## 📖 İçindekiler

1. [Conway Yasası ve Ters Manevra](#1--conway-yasası-ve-ters-manevra)
2. [Bilişsel Yük: Merkezî Kısıt](#2--bilişsel-yük-merkezî-kısıt)
3. [Dört Temel Takım Tipi](#3--dört-temel-takım-tipi)
4. [Üç Etkileşim Modu](#4--üç-etkileşim-modu)
5. [Kırılma Düzlemleri (Fracture Planes)](#5--kırılma-düzlemleri-fracture-planes)
6. [Team API ve İnce Platform](#6--team-api-ve-i̇nce-platform)
7. [Organizasyonu Evrimleştirmek](#7--organizasyonu-evrimleştirmek)
8. [Büyük Şirketlerde Team Topologies](#8--büyük-şirketlerde-team-topologies)
9. [Son Sözler](#9--son-sözler)

---

## 1. 🔄 Conway Yasası ve Ters Manevra

```
CONWAY YASASI (1968):
  "Bir sistem tasarlayan organizasyon, kaçınılmaz olarak kendi
   İLETİŞİM YAPISININ bir kopyası olan bir tasarım üretir."

  → 4 ekip bir derleyici yazarsa → 4 geçişli (4-pass) bir derleyici çıkar.
  → Mimariyi zorlamadan önce, takım iletişim yapısına bak — mimarin O olacak.
```

Kitabın anahtar fikri **Ters Conway Manevrası**:

```
GELENEKSEL (yanlış):        TERS CONWAY (doğru):
  Önce mimariyi tasarla        Önce İSTEDİĞİN mimariyi belirle
  Sonra takımları ona zorla    Sonra takımları O mimariyi ÜRETECEK şekilde kur
  → Takım yapısı direnç        → Takım yapısı hedef mimariyi DOĞAL üretir
    gösterir, mimari bozulur
```

> **Staff dersi:** "Neden mikroservislerimiz hâlâ birbirine sıkı bağlı?" sorusunun cevabı genelde koddan çok **organizasyon şemasındadır.** Gevşek bağlı mimari istiyorsan, gevşek bağlı, bağımsız takımlar kur. Bkz. [Building Microservices](../mimari-tasarim/building-microservices-turkce.md) ve [Fundamentals of Software Architecture](../mimari-tasarim/fundamentals-of-software-architecture-turkce.md).

---

## 2. 🧠 Bilişsel Yük: Merkezî Kısıt

Kitabın en özgün katkısı: **takımın taşıyabileceği bilişsel yük sınırlıdır** ve yazılımı buna göre bölmelisin.

```
BİLİŞSEL YÜK ÜÇ TÜRDÜR (psikolojiden ödünç):
  1. INTRINSIC (özsel)    → Problemin doğasındaki zorluk (algoritma, domain).
                            İYİ: eğitim/işe alımla azaltılır.
  2. EXTRANEOUS (dışsal)  → Ortamın gereksiz yükü (kırılgan deploy, kötü araç,
                            karışık config). KÖTÜ: platform ile YOK EDİLMELİ.
  3. GERMANE (verimli)    → Öğrenmeye/değer üretmeye giden yük (iş kuralları).
                            İSTENEN: takımın enerjisi BURAYA gitmeli.

HEDEF: Extraneous'u sıfırla (platform), Intrinsic'i yönet (uzmanlaşma),
       Germane'e alan aç (asıl değer).
```

```
"TAKIM-BOYUTU YAZILIM" (team-sized software):
  → Bir yazılım parçası, bir takımın bilişsel kapasitesini AŞMAMALI.
  → Aşıyorsa: takım sürekli yangın söndürür, değişim yavaşlar, tükenmişlik.
  → Çözüm: yazılımı takımın taşıyabileceği parçalara böl (yük ekle DEĞİL,
    SORUMLULUĞU böl).
```

> **Temel ölçüt:** "Bu takıma kaç sistem verebiliriz?" sorusunun cevabı kafa sayısı değil, **bilişsel yük**tür. Aşırı yüklü bir takıma developer eklemek çoğu zaman yükü artırır (iletişim maliyeti), azaltmaz.

---

## 3. 👥 Dört Temel Takım Tipi

Kitap, bir organizasyondaki tüm takımların **yalnızca dört tipe** indirgenmesini önerir. Bu sadeleştirme güçlüdür: "her takım tuhaf ve özeldir" kaosunu bitirir.

```
1. STREAM-ALIGNED (akış-hizalı) — ⭐ ANA TAKIM
   → Bir iş akışına (ürün, kullanıcı segmenti, domain) uçtan uca sahip.
   → Fikirden üretime kadar bağımsız teslim eder. Diğerleri BUNU DESTEKLER.
   → Organizasyonun ÇOĞUNLUĞU bu tip olmalı.

2. PLATFORM — akış-hizalı takımların hızını artıran iç ürün
   → Ortak altyapı/hizmetleri "self-service" olarak sunar (CI/CD, gözlem, veri).
   → Amaç: stream-aligned takımların EXTRANEOUS bilişsel yükünü YOK etmek.
   → Platform bir "self-service ürün"dür, bir bilet kuyruğu DEĞİL.

3. ENABLING (etkinleştirici) — geçici koçluk/uzmanlık
   → Belirli bir yeteneği (test otomasyonu, güvenlik, cloud) stream-aligned
     takımlara ÖĞRETİR, sonra çekilir. Kalıcı bağımlılık YARATMAZ.

4. COMPLICATED-SUBSYSTEM (karmaşık alt sistem) — derin uzmanlık gerektiren parça
   → Video codec, gerçek-zamanlı fiyatlama, ML modeli gibi, herkesin
     öğrenemeyeceği kadar derin bir parçaya sahip uzman takım.
   → İSTİSNADIR; gerçekten gerektiğinde kurulur (her karmaşık şey buraya değil!).
```

```
┌──────────────────────────────────────────────────────────┐
│  ENABLING ──öğretir──►  STREAM-ALIGNED  ◄──hizmet── PLATFORM│
│  (geçici koçluk)        (uçtan uca sahip)   (self-service)  │
│                              ▲                             │
│                              │ hizmet                      │
│                     COMPLICATED-SUBSYSTEM                  │
│                     (derin uzmanlık)                       │
└──────────────────────────────────────────────────────────┘
```

> **Staff dersi:** En sık hata, her şeyi "component team" (teknik katman takımı: frontend takımı, DB takımı) yapmaktır → her özellik 5 takımı koordine eder → teslimat felç olur. Team Topologies'in reçetesi: **stream-aligned takımları güçlendir, gerisini onları destekleyecek şekilde kur.**

---

## 4. 🤝 Üç Etkileşim Modu

Takımların *nasıl* etkileştiği, *ne* oldukları kadar önemlidir. Kitap üç mod tanımlar — ve her etkileşimin **bilinçli seçilmesini** ister.

```
1. COLLABORATION (işbirliği) — birlikte, yoğun çalışma
   → İki takım bir süre iç içe çalışır (keşif, yeni alan).
   → GÜÇLÜ ama PAHALI: bilişsel yükü artırır, sınırları bulanıklaştırır.
   → GEÇİCİ olmalı; kalıcı collaboration = bulanık sorumluluk.

2. X-AS-A-SERVICE (hizmet olarak) — net API üzerinden tüket
   → Bir takım diğerinin sunduğunu "self-service" tüketir (platform gibi).
   → DÜŞÜK bilişsel yük, NET sınır → ölçeklenen varsayılan mod.

3. FACILITATING (kolaylaştırma) — koçluk/engel kaldırma
   → Enabling takımın modu: öğret, engeli kaldır, sonra çekil.
```

```
EVRİM KALIBI:
  Yeni/belirsiz alan → COLLABORATION (birlikte keşfet) →
  olgunlaşınca → X-AS-A-SERVICE (net API'ye dönüştür) →
  → böylece bilişsel yük düşer, ekipler bağımsızlaşır.
```

---

## 5. 🪓 Kırılma Düzlemleri (Fracture Planes)

"Yazılımı nereden böleyim?" sorusuna kitabın cevabı: **doğal kırılma düzlemleri boyunca** — kaya gibi, zorlanınca doğal çatlaklardan.

```
İYİ KIRILMA DÜZLEMLERİ:
  • Business domain / bounded context (EN GÜÇLÜ — bkz. DDD)
  • Değişim hızı (hızlı değişen ↔ nadir değişen ayrı takımlarda)
  • Risk / uyumluluk (regüle edilen kısım ayrı)
  • Kullanıcı personası / coğrafya
  • Performans izolasyonu (yüksek yük ayrı)

KÖTÜ KIRILMA (kaçın):
  ✗ Teknik katman (frontend/backend/DB takımları) → her özellik hepsini gezer
  ✗ Rastgele/tarihsel (Conway'in kazası)
```

> Domain sınırları, en dayanıklı kırılma düzlemidir çünkü iş ihtiyacıyla hizalıdır. Bu yüzden Team Topologies + [Domain-Driven Design](../mimari-tasarim/ddd-turkce.md) birlikte okunur: bounded context'ler doğal takım sınırlarıdır.

---

## 6. 🔌 Team API ve İnce Platform

```
TEAM API — bir takımın "arayüzü":
  → Kod (versiyonlanmış servis/kütüphane), dokümanlar, çalışma pratikleri,
    iletişim kanalları, SLA'lar. "Bizimle nasıl çalışılır?"
  → İyi Team API = düşük iletişim sürtünmesi + net sorumluluk.
```

```
THINNEST VIABLE PLATFORM (TVP) — en ince uygulanabilir platform:
  → Platform, "mümkün olan en KÜÇÜK" olmalı — bir wiki sayfası bile olabilir.
  → Aşırı mühendislik yapılmış dev platform, kendisi bir bilişsel yük olur.
  → Kural: platform, stream-aligned takımların hızını GERÇEKTEN artırdığı
    kadar büyür — bir gram fazlası israftır.
```

> **Staff dersi:** Platform ekipleri en çok "self-service ürün" yerine "merkezî bilet kuyruğu" olmaya kayarak başarısız olur. Platform, kullananların onu **sevdiği ve gönüllü seçtiği** ölçüde başarılıdır — zorunlu tutulan değil.

---

## 7. 🌱 Organizasyonu Evrimleştirmek

```
ORGANİZASYON CANLIDIR — sabit değil, ADAPTİF olmalı:
  • Takım yapısı, ürün/teknoloji olgunlaştıkça DEĞİŞMELİ.
  • "Sensing organization": sinyalleri (bilişsel yük, teslimat hızı,
    bağımlılık darboğazları) okuyup topolojiyi ayarlar.
  • Tetikleyiciler: bir takım sürekli yavaşlıyorsa, çok fazla bağımlılık
    varsa, tek bir sistem bir takımı boğuyorsa → topolojiyi yeniden düşün.
```

> Bu, [Thinking in Systems](../veri-sistemler/thinking-in-systems-turkce.md)'in organizasyona uygulanmasıdır: geri bildirim döngüleri, gecikmeler, kaldıraç noktaları. Organizasyon bir sistemdir; onu bir sistem gibi tasarla ve evrimleştir.

---

## 8. 🏢 Büyük Şirketlerde Team Topologies

```
GERÇEK DÜNYA:
  • Amazon "two-pizza teams": küçük, bağımsız, uçtan uca sahip (stream-aligned).
  • Spotify modeli (squad/tribe/guild): popülerleşti ama Team Topologies daha
    NET bir dil verir; "squad" belirsizken 4 tip + 3 mod ölçülebilir.
  • Platform mühendisliği akımı (2020'ler): "internal developer platform (IDP)"
    doğrudan Team Topologies'in platform-takımı fikrinin ürünüdür.
  • Bulut ekipleri: DevOps'un "you build it, you run it" ideali ancak
    stream-aligned takım + güçlü platform ile ölçeklenir.
```

```
YAYGIN HATALAR:
  ✗ Etiketleri değiştirip yapıyı korumak ("artık squad diyoruz" ama hâlâ
    teknik-katman takımları).
  ✗ Platformu zorunlu bilet kuyruğu yapmak (self-service değil).
  ✗ Her karmaşık şeyi "complicated-subsystem" ilan edip uzman siloları yaratmak.
  ✗ Kalıcı collaboration → kimsenin net sahibi olmadığı gri alanlar.
```

---

## 9. 🎬 Son Sözler

```
TEAM TOPOLOGIES — 6 ALTIN KURAL:
  1. Takım yapısı bir mimari karardır (Conway). Mimarini takımlarınla tasarla.
  2. Bilişsel yük merkezî kısıttır — yazılımı takımın taşıyabileceği kadar böl.
  3. Dört tip yeter: stream-aligned (çoğunluk) + platform + enabling + complicated.
  4. Üç etkileşim modunu BİLİNÇLİ seç; collaboration geçici, X-as-a-Service kalıcı.
  5. Domain sınırları en iyi kırılma düzlemidir (DDD ile birlikte oku).
  6. Platform "en ince uygulanabilir" olmalı ve bir SELF-SERVICE ürün gibi sevilmeli.
```

> **Kitabın son mesajı:** Hızlı akış (fast flow) istiyorsan, önce **takımları** doğru kur; mimari, kalite ve hız bunun bir sonucudur. Organizasyon, ürettiğin yazılımın ilk taslağıdır.

---

## 📚 İleri Okuma

- Skelton & Pais — *Team Topologies* (2019) — kitabın kendisi (teamtopologies.com)
- Conway 1968 — *How Do Committees Invent?* (orijinal makale)
- Nicole Forsgren et al. — **Accelerate** ([bu repodaki rehber](accelerate-turkce.md)) — hızlı akışın veriyle kanıtı
- Bu repo: [Building Microservices](../mimari-tasarim/building-microservices-turkce.md) · [DDD](../mimari-tasarim/ddd-turkce.md) · [Thinking in Systems](../veri-sistemler/thinking-in-systems-turkce.md) · [The Staff Engineer's Path](staff-engineers-path-turkce.md)

---

> [⬅️ Kariyer & Kültür](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
