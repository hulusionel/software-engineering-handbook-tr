# 💥 Release It! — Türkçe Kapsamlı Rehber

> **"Yazılım tasarımını 'çalışıyor mu?' değil, 'saat 03:00'te üretimde çökerken hayatta kalıyor mu?' diye düşün."**
> — Michael Nygard, *Release It! Design and Deploy Production-Ready Software* (2nd ed.)

Bu rehber, Michael Nygard'ın backend dayanıklılığı üzerine klasikleşmiş kitabını Türkçe olarak, hikâyeler ve üretim gerçekleriyle anlatır. Kitabın çekirdeği tek bir fikirdir: **Yazılım bir demo için değil, yıllarca ayakta kalacak bir üretim sistemi için tasarlanır.** Circuit breaker, bulkhead ve backpressure gibi bugün herkesin kullandığı kavramların çoğu bu kitapta popülerleşti.

---

## 📖 İçindekiler

1. [Açılış Felaketi: Bir Uçağı Yere İndiren Bug](#1--açılış-felaketi-bir-uçağı-yere-i̇ndiren-bug)
2. [Neden "Çalışıyor" Yetmez?](#2--neden-çalışıyor-yetmez)
3. [Kararlılık Anti-Pattern'leri](#3--kararlılık-anti-patternleri)
4. [Kararlılık Pattern'leri](#4--kararlılık-patternleri)
5. [Kapasite ve Ölçek](#5--kapasite-ve-ölçek)
6. [Üretime Dağıtım İçin Tasarım](#6--üretime-dağıtım-i̇çin-tasarım)
7. [Şeffaflık: Loglama, Metrik, İzleme](#7--şeffaflık-loglama-metrik-i̇zleme)
8. [Evrimsel Mimari ve Adaptasyon](#8--evrimsel-mimari-ve-adaptasyon)
9. [Büyük Şirketlerde Release It!](#9--büyük-şirketlerde-release-it)
10. [Son Sözler](#10--son-sözler)

---

## 1. ✈️ Açılış Felaketi: Bir Uçağı Yere İndiren Bug

Kitap efsanevi bir hikâyeyle başlar. Bir havayolunun uçuş operasyon sistemi, gecenin köründe **tamamen** durur — check-in kioskları donar, kapı ekranları kararır. Milyonlarca dolar ve binlerce yolcu etkilenir.

```
KÖK NEDEN ZİNCİRİ (tek bir küçük kusurun kaskadı):
  1. Bir veritabanı bağlantısı sessizce koptu (firewall boştaki bağlantıyı düşürdü).
  2. Uygulama bu ÖLÜ bağlantıyı connection pool'a geri koydu.
  3. Bir sonraki istek ölü bağlantıyı aldı → SQLException.
  4. Hata yakalandı AMA bağlantı pool'a İADE EDİLMEDİ (kaynak sızıntısı!).
  5. Her istek bir bağlantı daha sızdırdı → pool tükendi.
  6. Yeni istekler pool'dan bağlantı beklerken SONSUZA KİLİTLENDİ.
  7. Tüm thread'ler bloklandı → uygulama "ayakta" ama HİÇBİR ŞEY yapmıyor.
  8. Aynı kod tüm sunucularda → HEPSİ aynı anda çöktü.
```

> **Nygard'ın dersi:** Sistem "hata" vermedi — kimse `throw` görmedi. Tek bir kütüphanenin tek bir kenar durumu, katman katman büyüyüp koca sistemi yere serdi. **Kararlılık, mutlu yolu değil; sürprizleri hayatta kalmayı tasarlamaktır.**

---

## 2. 🎯 Neden "Çalışıyor" Yetmez?

```
GELİŞTİRME ZİHNİYETİ          ÜRETİM ZİHNİYETİ
  "Testler geçiyor" ✅          "Bağımlılık 5 sn yanıt vermezse ne olur?"
  "Demo çalıştı" ✅             "Trafik 10× olursa? Disk dolarsa?"
  "Happy path tamam" ✅         "Bir node çökerken diğerleri ne yapar?"
  → Tek makine, temiz veri      → 7/24, kısmi hata, düşman girdi, yıllarca
```

Nygard iki kavramı ayırır:

| Kavram | Tanım |
|---|---|
| **Longevity (uzun ömür)** | Sistem haftalarca/aylarca kesintisiz ayakta kalabiliyor mu? (Bellek sızıntısı, log şişmesi, kaynak tükenmesi = zamanla ölüm) |
| **Resilience (dayanıklılık)** | Bir bileşen çökerken sistem *bir bütün olarak* hayatta kalıyor mu, yoksa çöküş yayılıyor mu? |

> **Temel ilke:** Her entegrasyon noktası, her uzak çağrı **bir gün başarısız olacak** — yavaşça, garip biçimde, en kötü anda. Soru "olur mu?" değil, "olduğunda ne olacak?"dır.

---

## 3. 🕳️ Kararlılık Anti-Pattern'leri

Bunlar çöküşü *yaratan* ve *yayan* kalıplardır. Nygard'ın en değerli katkısı bunları isimlendirmesidir — isimlendirebildiğin tehlikeyi önleyebilirsin.

### Integration Points (Entegrasyon Noktaları) — "Bir numaralı katil"

```
Her dış çağrı (DB, API, cache, kuyruk) bir RİSKTİR:
  → Yavaş yanıt (en tehlikelisi — hata'dan beter, çünkü thread'i tutar)
  → Hiç yanıt vermeme (timeout yoksa SONSUZA bekler)
  → Bozuk/beklenmedik yanıt
  → Bağlantının sessizce kopması
SAVUNMA: Timeout + Circuit Breaker + Bulkhead (bkz. bölüm 4)
```

### Cascading Failures (Kaskad Hatalar)

```
Bir servisin çöküşü, onu çağıran servisi de çökertir → o da bir üstünü →
  domino etkisi. Çöküş, sistem SINIRLARINI aşarak yayılır.
  Integration Point çöküşü → çağıran thread'ler bloklanır → çağıran çöker →
  ZİNCİR REAKSİYON. SAVUNMA: Circuit Breaker (yayılmayı KESER).
```

### Blocked Threads (Bloklanan Thread'ler)

```
En yaygın "ayakta ama ölü" nedeni:
  → Thread'ler bir kaynağı (bağlantı, kilit) sonsuza bekler → havuz tükenir →
    yeni iş kabul edilemez. Uygulama süreç olarak yaşıyor, işlevsel olarak ÖLÜ.
  → Açılış hikâyesindeki tam senaryo budur.
SAVUNMA: Timeout HER yerde; sınırsız bekleme YASAK.
```

### Slow Responses (Yavaş Yanıtlar) — hata'dan beter

```
Hızlı hata > yavaş yanıt. Yavaş yanıt:
  → Çağıranın thread'ini/kaynağını uzun süre tutar → kaynak tükenir →
    yavaşlık YUKARI doğru yayılır (senin yavaşlığın çağıranını çökertir).
SAVUNMA: Fail Fast; makul timeout; aşırı yükte iş reddet (Shed Load).
```

### Diğer kritik anti-pattern'ler

| Anti-Pattern | Ne yapar |
|---|---|
| **Chain Reactions** | Bir node çökünce yükü diğerlerine biner → onlar da çöker (yatay yayılım) |
| **Users** | Kullanıcılar öngörülemez: yavaş, kötü niyetli, aniden kalabalık; her biri kaynak tüketir |
| **Unbalanced Capacities** | A servisi B'den çok daha güçlü → B'yi ezer (kapasite dengesizliği) |
| **Dogpile / Thundering Herd** | Hepsi aynı anda (restart, cache expiry, cron) → ani yük darbesi |
| **Self-Denial Attack** | Kendi kampanyan/anonsun trafik patlaması yaratır (kendi kendine DDoS) |
| **Unbounded Result Sets** | "LIMIT'siz sorgu" — normalde 10 satır, bir gün 10M satır → bellek patlar |
| **Scaling Effects** | Küçükte çalışan (nokta-nokta bağlantı) büyükte patlar (N² ilişki) |

> **Staff dersi:** Bu anti-pattern'lerin çoğu tek başına zararsız görünür; tehlike **kombinasyonlarında** ve **ölçekte**dir. [Anti-Pattern Kataloğu](../pratik/anti-pattern-katalogu.md) ve [Postmortem Arşivi](../pratik/postmortem-arsivi.md) bunların gerçek dünyadaki örnekleriyle doludur.

---

## 4. 🛡️ Kararlılık Pattern'leri

Anti-pattern'lere karşı Nygard'ın savunma cephanesi. Bugünkü "resilience engineering"in temeli.

### Timeout (Zaman Aşımı)

```
KURAL: Ağ üzerinden yapılan HİÇBİR çağrı sonsuz beklemesin.
  → Her uzak çağrıya makul timeout koy. Timeout yoksa, uzak sistemin
    yavaşlığı SENİN kaynaklarını tüketir (Blocked Threads).
  → Bağlantı timeout'u + okuma timeout'u AYRI ayarlanır.
```

### Circuit Breaker (Devre Kesici) — kitabın en ünlü katkısı

```
Elektrik devre kesici gibi: sürekli başarısız olan bir bağımlılığa çağrıyı
DURDUR, böylece kaskadı ve boşa beklemeyi engelle.

  ┌─────────┐  hata eşiği aşıldı   ┌────────┐  timeout sonrası  ┌──────────┐
  │ CLOSED  │────────────────────→ │  OPEN  │ ─────────────────→│ HALF-OPEN│
  │(normal) │                      │(çağrı  │                   │(1 deneme)│
  │ çağrı✓  │←─────────────────────│ YOK,   │←──────────────────│ başarısız│
  └─────────┘  deneme başarılı     │hızlı ✗)│   deneme başarılı  └──────────┘
                                   └────────┘
  • CLOSED: çağrılar geçer; hatalar sayılır.
  • OPEN: eşik aşıldı → çağrı YAPILMAZ, anında hata (fail fast) → bağımlılığa
    nefes aldır, çağıranı boşa bekletme.
  • HALF-OPEN: bir süre sonra tek deneme; başarılıysa CLOSED, değilse tekrar OPEN.
```

> Not: Bu repoda circuit breaker'ın kod uygulaması için bkz. [Advanced Backend Engineering](../ileri-duzey-rehberler/advanced-backend-engineering.md#resilience-patterns) ve [Building Microservices](building-microservices-turkce.md).

### Bulkhead (Bölme Duvarı)

```
Geminin su geçirmez bölmeleri gibi: bir bölme su alsa da gemi batmaz.
  → Kaynakları BÖL: her bağımlılık/kiracı için ayrı thread pool / bağlantı havuzu.
  → Bir bağımlılık çökse, YALNIZCA onun bölmesi tükenir; gerisi ayakta kalır.
  Örnek: Ödeme servisi yavaşlasa bile, arama/gözat akışı kendi havuzunda çalışır.
```

### Steady State (Kararlı Durum)

```
Sistem insan müdahalesi olmadan sonsuza çalışabilmeli:
  → Log rotasyonu (disk dolmasın), veri temizleme (tablo şişmesin),
    cache eviction, geçici dosya temizliği.
  → "Fiber Optik" kuralı: her mekanizma bir şey BİRİKTİRİYORSA, onu
    TEMİZLEYEN bir mekanizma da olmalı.
```

### Diğer kritik pattern'ler

| Pattern | Ne yapar |
|---|---|
| **Fail Fast** | Başarısız olacaksan HIZLI ol; kaynağı tutup yavaşça ölme |
| **Let It Crash** | Bozuk durumu onarmaya çalışma; bileşeni temiz durumla yeniden başlat (Erlang felsefesi) |
| **Handshaking** | Sunucu doluysa istemciye "yavaşla" sinyali ver (kabul etmeden önce anlaş) |
| **Back Pressure** | Alıcı yetişemiyorsa göndereni YAVAŞLAT (sınırlı kuyruk + blokla) → çöküş yerine yavaşlama |
| **Shed Load** | Aşırı yükte bazı istekleri baştan REDDET (503) → tümünü çökertmektense bir kısmını kurtar |
| **Governor** | Otomatik/yıkıcı eylemleri yavaşlat (ör. otomatik ölçek küçültme hız sınırı) |

> **Staff dersi:** Back Pressure ve Shed Load aynı gerçeğin iki yüzüdür: **sınırsız kabul, garantili çöküştür.** Bir sistem kapasitesinin üstünde iş kabul etmeyi reddetmeyi öğrenmeli — "hayır" demek bir dayanıklılık özelliğidir. Bkz. [Eşzamanlılık Primitifleri — backpressure](../pratik/eszamanlilik-primitifleri.md).

---

## 5. 📈 Kapasite ve Ölçek

```
KAPASİTE = sistemin kabul edilebilir performansla taşıyabildiği yük.
  → "Performans" (tek istek hızı) ≠ "Throughput" (birim zamanda iş) ≠ "Kapasite".
  → Darboğaz TEK bir kaynaktır (CPU, bellek, DB bağlantısı, IO) — onu bul.

NYGARD'IN KAPASİTE ANTI-PATTERN'LERİ:
  • Resource pool'ları çağrı başına yeniden kurma (bağlantıyı reuse et!)
  • Aşırı JSON/veri serileştirme (gereksiz alanlar)
  • AJAX/aşırı chatty istemci (N+1 ağ çağrısı)
  • Cache'i yanlış kullanma (düşük hit oranı, bellek şişmesi)
```

> Sayısal kapasite matematiği (Little's Law, utilization eğrisi, p99) için bu repoda derin bir kaynak var: [Latency Numaraları & Kapasite Matematiği](../pratik/latency-numbers-ve-kapasite-matematigi.md).

---

## 6. 🚀 Üretime Dağıtım İçin Tasarım

Nygard, kodun *deploy edilebilir* ve *işletilebilir* olmasının tasarım kararı olduğunu vurgular.

```
SIFIR-KESİNTİ DAĞITIM İÇİN:
  • Versiyonlanmış, GERİYE UYUMLU API'ler (eski ve yeni aynı anda yaşayabilmeli).
  • DB şema göçü, koddan AYRI ve geriye uyumlu (expand/contract deseni:
    önce ekle → çift yaz → geri doldur → eskiyi kaldır).
  • Config'i koddan AYIR; ortamlar arası fark yalnızca config olsun.
  • Feature flag: dağıtımı (deploy) yayından (release) AYIR.

SIFIRDAN AYAĞA KALKMA (recovery-oriented):
  • Sistem herhangi bir anda güvenle yeniden başlatılabilmeli.
  • Başlatma sırası bağımlılıklara TAKILMAMALI (bağımlılık yoksa da ayağa kalk,
    circuit breaker OPEN başla).
```

> Dağıtım stratejileri (blue-green, canary, expand/contract) için bkz. [Build, Release & Supply Chain](../pratik/build-release-supply-chain.md).

---

## 7. 🔍 Şeffaflık: Loglama, Metrik, İzleme

```
"Göremediğin sistemi işletemezsin."
  • LOG: yapılandırılmış (JSON), korelasyon ID'li, doğru seviyede. Log bir
    ürün özelliğidir — 03:00'te seni sen kurtaracak olan şeydir.
  • METRİK: iş + teknik (istek/sn, hata oranı, p99, kaynak doygunluğu).
  • İZLEME (tracing): dağıtık çağrının uçtan uca yolu.
  • ADAPTASYON: sistem, gözlemlenen davranışa göre kendini ayarlayabilmeli
    (autoscale, adaptif timeout).
```

> Bu, modern **observability**'nin habercisidir. Derinlik için: [Performance Engineering — USE/RED/Four Golden Signals](../pratik/performance-engineering.md) ve [SRE Pratiği](../pratik/sre-pratigi.md).

---

## 8. 🧬 Evrimsel Mimari ve Adaptasyon

```
Sistem CANLIDIR — dağıtıldıktan sonra öğrenmeye devam eder:
  • Gevşek bağ (loose coupling) → parçalar bağımsız evrilir.
  • Asenkron/mesajlaşma → zamansal bağımsızlık, dayanıklılık.
  • "Postel yasası": gönderirken katı, alırken hoşgörülü ol.
  • Sürüm birlikte yaşaması (versioning) → büyük-patlama göçü yok.
```

> **Staff dersi:** Nygard'ın nihai mesajı: kararlılık bir kerelik bir özellik değil, **sürekli bir tasarım disiplinidir.** Sistem büyüdükçe yeni kırılganlıklar doğar; postmortem'lerden öğren, savunmaları güçlendir.

---

## 9. 🏢 Büyük Şirketlerde Release It!

```
GERÇEK DÜNYA UYGULAMASI:
  • Netflix Hystrix (ve sonrası resilience4j): circuit breaker + bulkhead'i
    kütüphane hâline getirdi — Nygard'ın pattern'lerinin doğrudan mirası.
  • AWS/Google: her servis timeout + retry (jitter'lı exponential backoff) +
    circuit breaker + load shedding varsayar.
  • Chaos Engineering (Netflix Chaos Monkey): bu pattern'lerin GERÇEKTEN
    çalıştığını üretimde kanıtlamak için kasıtlı hata enjeksiyonu.
  • Service mesh (Istio/Linkerd): timeout, retry, circuit breaking'i altyapı
    katmanına taşıdı — uygulama koduna dokunmadan.
```

```
YAYGIN HATALAR (bugün bile):
  ✗ Retry'a jitter/backoff koymamak → retry storm (kendi kendine DDoS).
  ✗ Circuit breaker'ı fallback olmadan koymak → yine de kötü kullanıcı deneyimi.
  ✗ Timeout'ları katmanlar arası TUTARSIZ ayarlamak (dış timeout < iç timeout
    olmalı, yoksa boşuna bekleme).
  ✗ Bulkhead'siz paylaşılan tek havuz → bir bağımlılık hepsini çökertir.
```

---

## 10. 🎬 Son Sözler

```
RELEASE IT! — 7 ALTIN KURAL:
  1. Her entegrasyon noktası bir gün başarısız olacak — buna GÖRE tasarla.
  2. Timeout HER yerde; sınırsız bekleme = garantili çöküş.
  3. Circuit Breaker ile çöküşün YAYILMASINI kes.
  4. Bulkhead ile kaynakları böl; bir bölme batsa gemi yüzsün.
  5. Yavaş yanıt hatadan beterdir — Fail Fast, Shed Load, Back Pressure.
  6. Steady State: biriken her şeyin bir temizleyicisi olsun.
  7. Şeffaflık (log/metrik/trace) bir ürün özelliğidir — 03:00'te seni kurtarır.
```

> **Nygard'ın son sözü:** "Yazılımınız bir demoda değil, üretimde yaşar — düşman bir dünyada, yıllarca, siz uyurken. Onu **hayatta kalmak** için tasarlayın."

---

## 📚 İleri Okuma

- Michael Nygard — *Release It!* (2nd ed., 2018) — kitabın kendisi
- Netflix — *Hystrix* / *resilience4j* dokümantasyonu (pattern'lerin kod hâli)
- Google SRE Book — *Handling Overload*, *Addressing Cascading Failures* bölümleri
- Bu repo: [Anti-Pattern Kataloğu](../pratik/anti-pattern-katalogu.md) · [Dağıtık Sistemler Derinlemesine](../pratik/dagitik-sistemler-derinlemesine.md) · [Eşzamanlılık Primitifleri](../pratik/eszamanlilik-primitifleri.md) · [SRE Pratiği](../pratik/sre-pratigi.md) · [Postmortem Arşivi](../pratik/postmortem-arsivi.md)

---

> [⬅️ Mimari & Tasarım](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
