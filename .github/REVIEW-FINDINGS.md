# 📋 Handbook Review Bulguları — Takip Dosyası

> **Oluşturulma**: 2026-05-03
> **Son Güncelleme**: 2026-09-04
> **Toplam Bulgu**: 100 madde (+ 22 yeni: 20 kırık anchor, CI otomasyonu, ek kırık karakter)
> **Durum**: ⬜ = Bekliyor | ✅ = Düzeltildi | ⏭️ = Atlandı (bilinçli karar)
>
> **2026-09-04 revizyonu**: Yüksek (Y1–Y4) ve seçili Düşük (D1, D2.1, D4) öncelikli maddeler tamamlandı.
> Ayrıca K1'de "düzeltildi" işaretli olmasına rağmen **8 içerik dosyasında hâlâ mevcut olan kırık `🏢`/`🎬` emojileri** giderildi (bkz. K5) ve
> orijinal denetimde kaçırılan **20 kırık başlık (anchor) linki** ile bir **CI kalite kapısı** eklendi (bkz. YENİ bölümü).

---

## 🔴 KRİTİK (Öncelik 1) — Yapısal Bütünlüğü Bozan Sorunlar

### K1. Kırık Emoji Karakterleri — pratik/ (8 dosya)

Unicode replacement character (`�`) başlıklarda ve footer'larda görünüyor. Anchor linkleri bozabilir.

- [x] K1.1 `pratik/latency-numbers-ve-kapasite-matematigi.md` — satır ~420: `## ⚠️ Kapasite Planlama Anti-Pattern'leri`
- [x] K1.2 `pratik/latency-numbers-ve-kapasite-matematigi.md` — satır ~463: `## 📚 İleri Okuma`
- [x] K1.3 `pratik/postmortem-arsivi.md` — satır ~487: `## ⚠️ Postmortem Anti-Pattern'leri`
- [x] K1.4 `pratik/postmortem-arsivi.md` — satır ~500: `## 📚 İleri Okuma`
- [x] K1.5 `pratik/postmortem-arsivi.md` — satır ~509: Footer: `[📚 Sözlük]`, `[📋 Postmortem]`
- [x] K1.6 `pratik/guvenlik-derinlemesine.md` — satır ~660: `## ⚠️ Güvenlik Anti-Pattern'leri`
- [x] K1.7 `pratik/guvenlik-derinlemesine.md` — satır ~675: `## 📚 İleri Okuma`
- [x] K1.8 `pratik/modern-teknoloji-radari.md` — satır ~386: `## ⚠️ Teknoloji Seçim Anti-Pattern'leri`
- [x] K1.9 `pratik/modern-teknoloji-radari.md` — satır ~400: `## 📚 İleri Okuma`
- [x] K1.10 `pratik/staff-yazma-kulturu.md` — satır ~466: Footer: `[📚 Sözlük]`, `[📐 Şablonlar]`
- [x] K1.11 `pratik/karar-cercevesi-matrisleri.md` — satır ~525: Footer: `[📚 Sözlük]`, `[📐 ADR]`
- [x] K1.12 `pratik/api-tasarim-derinligi.md` — satır ~640: Footer: `[📚 Sözlük]`, `[📐 ADR]`

### K2. Kırık Emoji Karakterleri — kariyer-kultur/ (2 dosya)

- [x] K2.1 `kariyer-kultur/staff-engineers-path-turkce.md` — Bölüm 16 başlığı: `## 16. 🏢` ✅
- [x] K2.2 `kariyer-kultur/staff-engineers-path-turkce.md` — Bölüm 18 başlığı: `## 18. 🎬` ✅
- [x] K2.3 `kariyer-kultur/the-phoenix-project-turkce.md` — Bölüm 19 başlığı: `## 19. 🏢` ✅
- [x] K2.4 `kariyer-kultur/the-phoenix-project-turkce.md` — Bölüm 21 başlığı: `## 21. 🎬` ✅

### K3. Kırık Emoji Karakterleri — veri-sistemler/ (1 dosya)

- [x] K3.1 `veri-sistemler/grokking-algorithms-turkce.md` — satır ~383: `## 4. � Diziler vs Bağlı Listeler`
- [x] K3.2 `veri-sistemler/grokking-algorithms-turkce.md` — satır ~484: `## 5. �🗂️ Selection Sort`

### K4. Bölüm Numaralandırma Hatası — grokking-algorithms

- [x] K4.1 `veri-sistemler/grokking-algorithms-turkce.md` — Bölüm 5 iki kez kullanılmış (Selection Sort ve Recursion aynı numara). İçindekiler ile gövde uyumsuz.
- [x] K4.2 `veri-sistemler/grokking-algorithms-turkce.md` — İçindekiler'deki anchor link'ler bölüm numaraları ile eşleşmiyor.

### K5. Kırık Emoji Karakterleri — mimari-tasarim/, kod-kalitesi/, veri-sistemler/ (KAÇIRILMIŞTI)

> K1 "düzeltildi" işaretliydi ancak **8 dosyada `## N. 🏢 Büyük Şirketlerde…` ve `## N. 🎬 Son Sözler` başlıklarındaki emojiler hâlâ `�` idi.** 2026-09-04'te giderildi (15 karakter). Bunlar başlıkta olduğu için anchor bütünlüğünü de riske atıyordu.

- [x] K5.1 `mimari-tasarim/clean-architecture-turkce.md` (2), `ddd-turkce.md` (2), `system-design-interview-turkce.md` (2), `fundamentals-of-software-architecture-turkce.md` (2), `software-architecture-hard-parts-turkce.md` (2), `building-microservices-turkce.md` (1)
- [x] K5.2 `kod-kalitesi/refactoring-turkce.md` (2)
- [x] K5.3 `veri-sistemler/thinking-in-systems-turkce.md` (2)

---

## 🟡 YÜKSEK (Öncelik 2) — İçerik Tutarlılığı ve Önemli Eksikler

### Y1. Yol Haritasına Çapraz Referans Eksikliği

- [x] Y1.1 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — Projedeki 40+ dokümana hiçbir çapraz referans yok. Her kitap önerisinin yanına ilgili rehber linki eklenmeli.
- [x] Y1.2 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — `pratik/` klasörüne yönlendirme yok.
- [x] Y1.3 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — `ileri-duzey-rehberler/` referansı yok.
- [x] Y1.4 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — `templates/` referansı yok.
- [x] Y1.5 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — Güvenlik bölümü yok (11 bölümün hiçbirinde).

### Y2. Glossary ile Terim Tutarsızlıkları

- [x] Y2.1 **Cohesion**: Glossary → "Bağlaşıklık". Dosyalarda → "Bağdaşıklık". Tutarsız.
- [x] Y2.2 **Coupling**: Glossary → "Bağlılık". Dosyalarda → "Bağlanma", "Bağımlılık" karışık.
- [x] Y2.3 **Aggregate**: Glossary → "Bütünleyen / Agregat". DDD dosyasında → "Küme". Tutarsız.
- [x] Y2.4 **Consensus**: Glossary → "Uzlaşı / Konsensüs". DDIA'da → "Uzlaşma". Tutarsız.

### Y3. Dosyalar Arası Tekrarlarda Çapraz Referans Eksikliği

- [x] Y3.1 **Saga Pattern** — `mimari-tasarim/` (3 dosya) + `ileri-duzey-rehberler/` (2 dosya) = 5 yerde anlatılıyor, aralarında çapraz referans yok.
- [x] Y3.2 **Circuit Breaker** — `building-microservices`, `senior-roadmap`, `advanced-backend` = 3 yerde, çapraz referans yok.
- [x] Y3.3 **Connection Pooling** — `senior-roadmap`, `advanced-backend` = 2 yerde tekrar, çapraz referans yok.

### Y4. PRFAQ Şablonu Eksik

- [x] Y4.1 `templates/README.md` — PRFAQ şablonu "TBD" olarak işaretli ama dosya oluşturulmamış.

---

## 🟠 ORTA (Öncelik 3) — Typo'lar ve Yazım Hataları

### T1. mimari-tasarim/ Typo'ları

- [x] T1.1 `mimari-tasarim/clean-architecture-turkce.md` — satır ~80: `GOREVİMİZ` → `GÖREVİMİZ`
- [x] T1.2 `mimari-tasarim/clean-architecture-turkce.md` — satır ~110: `DÜŞMeZ` → `DÜŞMEZ`
- [x] T1.3 `mimari-tasarim/clean-architecture-turkce.md` — satır ~153: `FALSIFIABILiTY` → `FALSIFIABILITY`
- [x] T1.4 `mimari-tasarim/clean-architecture-turkce.md` — satır ~166: `GÖRÜNMüyor` → `GÖRÜNMÜYOR`
- [x] T1.5 `mimari-tasarim/clean-architecture-turkce.md` — satır ~1862: `ANLAMADIYISANIZ` → `ANLAMADIYORSANIZ`
- [x] T1.6 `mimari-tasarim/fundamentals-of-software-architecture-turkce.md` — satır ~1299: `hedef kitlseyi` → `hedef kitlesini`
- [x] T1.7 `mimari-tasarim/fundamentals-of-software-architecture-turkce.md` — satır ~1314: `SEZG gerektiri` → `SEZGİ gerektirir`
- [x] T1.8 `mimari-tasarim/software-architecture-hard-parts-turkce.md` — satır ~42: `yönetecağiz` → `yöneteceğiz`
- [x] T1.9 `mimari-tasarim/software-architecture-hard-parts-turkce.md` — satır ~44: `olmazmıydı` → `olmaz mıydı`
- [x] T1.10 `mimari-tasarim/software-architecture-hard-parts-turkce.md` — satır ~903: `KOMPANZAsyon` → `KOMPANZASYON`
- [x] T1.11 `mimari-tasarim/software-architecture-hard-parts-turkce.md` — satır ~1024: `SERVİS İLETIŞIMINDE` → `SERVİS İLETİŞİMİNDE`
- [x] T1.12 `mimari-tasarim/building-microservices-turkce.md` — satır ~1185: `KOLAYLAŞTTIRIR` → `KOLAYLAŞTIRIR`
- [x] T1.13 `mimari-tasarim/building-microservices-turkce.md` — satır ~1195: `KAZANDTIRIR` → `KAZANDIRIR`
- [x] T1.14 `mimari-tasarim/building-microservices-turkce.md` — satır ~1544: `HER metrriğe` → `HER metriğe`
- [x] T1.15 `mimari-tasarim/building-microservices-turkce.md` — satır ~1861: `ANLAMADIYISANIZ` → `ANLAMADIYORSANIZ`

### T2. kod-kalitesi/ Typo'ları

- [x] T2.1 `kod-kalitesi/refactoring-turkce.md` — satır ~915: `retreiveOrder()` → `retrieveOrder()`
- [x] T2.2 `kod-kalitesi/refactoring-turkce.md` — satır ~1391: `BULMAYAMI` → `BULMAYI MI`
- [x] T2.3 `kod-kalitesi/unit-testing-turkce.md` — satır ~1527: `diş bağımlılık` → `dış bağımlılık`
- [x] T2.4 `kod-kalitesi/philosophy-of-software-design-turkce.md` — satır ~900: `İDAREE EDİLEBİLİR` → `İDARE EDİLEBİLİR`
- [x] T2.5 `kod-kalitesi/head-first-design-patterns-turkce.md` — satır ~877: `Ali'a` → `Ali'ye`

### T3. veri-sistemler/ Typo'ları

- [x] T3.1 `veri-sistemler/ddia-turkce.md` — satır ~1572: `KAYBOLDUl` → `KAYBOLDU`
- [x] T3.2 `veri-sistemler/grokking-algorithms-turkce.md` — satır ~830: `kontolEdildi` → `kontrolEdildi`
- [x] T3.3 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~225: `YAZILIM ANALOJISİ` → `YAZILIM ANALOJİSİ`
- [x] T3.4 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~233: `Consumer çökerdİ!` → `Consumer çökerdi!`
- [x] T3.5 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~316: `termosatatı` → `termostatı`
- [x] T3.6 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~642: `GEÇGEÇtespit` → `GEÇ tespit`
- [x] T3.7 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~685: `DEĞİŞMEdEN` → `DEĞİŞMEDEN`
- [x] T3.8 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~943: `VERiMLİLİK` → `VERİMLİLİK`
- [x] T3.9 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~1013: `DOMaINI` → `DOMAIN'İ`
- [x] T3.10 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~1017: `LİDERLIĞÎ` → `LİDERLİĞİ`
- [x] T3.11 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~1505: `FARBİKADA` → `FABRİKADA`
- [x] T3.12 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~1533: `YAPAMIyorsun` → `YAPAMIYORSUN`
- [x] T3.13 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~1547: `bilMIYORUM` → `BİLMİYORUM`
- [x] T3.14 `veri-sistemler/thinking-in-systems-turkce.md` — satır ~1446: `ÇIKARIlAMAZ` → `ÇIKARILAMAZ`

### T4. kariyer-kultur/ Typo'ları

- [x] T4.1 `kariyer-kultur/staff-engineers-path-turkce.md` — `UZMANICISI` → `UZMANCISI` ✅
- [x] T4.2 `kariyer-kultur/staff-engineers-path-turkce.md` — `Engellereri` → `Engelleri` ✅
- [x] T4.3 `kariyer-kultur/staff-engineers-path-turkce.md` — `YAPACACAKSIN` → `YAPACAKSIN` ✅
- [x] T4.4 `kariyer-kultur/staff-engineers-path-turkce.md` — `KALDRACI` → `KALDIRACI` ✅
- [x] T4.5 `kariyer-kultur/staff-engineers-path-turkce.md` — `EKSTrA` → `EKSTRA` ✅
- [x] T4.6 `kariyer-kultur/staff-engineers-path-turkce.md` — `DERINLESTIRIR` → `DERİNLEŞTİRİR` ✅
- [x] T4.7 `kariyer-kultur/staff-engineers-path-turkce.md` — `BİLMELİDIR` → `BİLMELİDİR` ✅
- [x] T4.8 `kariyer-kultur/staff-engineers-path-turkce.md` — `İLETIŞİM` → `İLETİŞİM` ✅
- [x] T4.9 `kariyer-kultur/staff-engineers-path-turkce.md` — `ŞEKILLENDIRIRSIN` → `ŞEKİLLENDİRİRSİN` ✅
- [x] T4.10 `kariyer-kultur/pragmatic-programmer-turkce.md` — `toplulukklara` → `topluluklara` ✅
- [x] T4.11 `kariyer-kultur/pragmatic-programmer-turkce.md` — `hassasiyet derecesin` → `hassasiyet derecesini` ✅
- [x] T4.12 `kariyer-kultur/pragmatic-programmer-turkce.md` — `özgürleştirrir` → `özgürleştirir` ✅
- [x] T4.13 `kariyer-kultur/pragmatic-programmer-turkce.md` — `Hedeffin` → `Hedefin` ⏭️ (dosyada bulunamadı)
- [x] T4.14 `kariyer-kultur/the-missing-readme-turkce.md` — `TUTARSI!` → `TUTARSIZ!` ✅
- [x] T4.15 `kariyer-kultur/the-missing-readme-turkce.md` — `YETERLidir` → `YETERLİDİR` ✅
- [x] T4.16 `kariyer-kultur/the-phoenix-project-turkce.md` — `DEĞİŞİNKLİK` → `DEĞİŞİKLİK` ✅
- [x] T4.17 `kariyer-kultur/the-phoenix-project-turkce.md` — `ENGELLMEZ` → `ENGELLEMEZ` ✅

### T5. pratik/ Typo'ları

- [x] T5.1 `pratik/performance-engineering.md` — satır ~89: `görüğü` → `gördüğü`

### T6. templates/ Typo'ları

- [x] T6.1 `templates/adr-sablon.md` — `dedi diyen ADR` → `diyen ADR` (fazla "dedi" kelimesi)
- [x] T6.2 `templates/rfc-design-doc-sablon.md` — Bölüm 7: `kararsalama` → `kararlaştırma` (var olmayan sözcük)

### T7. yol-haritasi/ Typo'ları

- [x] T7.1 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — satır ~16: `kodunuzun` → `kodunun` (sen/siz tutarsızlığı)

---

## 🔵 DÜŞÜK (Öncelik 4) — Estetik ve İyileştirme Önerileri

### D1. ALL-CAPS Türkçe Karakter Tutarlılığı

- [x] D1.1 Proje genelinde ALL-CAPS vurgu stilinde `I` yerine `İ`, `i` yerine `İ` hataları toplu düzeltilmeli
- [x] D1.2 Özellikle `kariyer-kultur/staff-engineers-path-turkce.md` yoğun (9 adet)
- [x] D1.3 `mimari-tasarim/software-architecture-hard-parts-turkce.md` — `İLETIŞIMINDE` → `İLETİŞİMİNDE`

### D2. README İyileştirmeleri

- [x] D2.1 `yol-haritasi/README.md` — Çok minimal. Hedef kitle ve kullanım rehberi eklenmeli.
- [ ] D2.2 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — Tablo sütun isimleri bölümler arası tutarsız ("Neden Önemli", "Özet", "Açıklama", "Odak" karışık).

### D3. Dosya Boyutu Optimizasyonu

- [ ] D3.1 `ileri-duzey-rehberler/senior-backend-developer-roadmap.md` (~5200 satır) — Alt dosyalara bölünme düşünülebilir.
- [ ] D3.2 `ileri-duzey-rehberler/advanced-backend-engineering.md` (~4500 satır) — Alt dosyalara bölünme düşünülebilir.

### D4. İngilizce Terim Parantez İçi Açıklama

- [x] D4.1 `templates/adr-sablon.md` — `opinion` kelimesi Türkçe karşılığı olmadan kullanılmış → `görüş (opinion)`
- [x] D4.2 `yol-haritasi/yazilim-muhendisligi-yol-haritasi.md` — `mindset'i` → `zihniyet (mindset)`

### D5. İçerik Eksiklikleri (Nice-to-Have)

- [x] D5.1 `mimari-tasarim/fundamentals-of-software-architecture-turkce.md` — SOA stili atlanmış
- [x] D5.2 `mimari-tasarim/ddd-turkce.md` — Specification Pattern, Large-Scale Structure eksik
- [x] D5.3 `mimari-tasarim/software-architecture-hard-parts-turkce.md` — Sysops Squad Saga case study atlanmış
- [x] D5.4 `kod-kalitesi/clean-code-turkce.md` — Successive Refinement case study atlanmış
- [x] D5.5 `kod-kalitesi/refactoring-turkce.md` — Video mağazası step-by-step örneği atlanmış
- [x] D5.6 `kod-kalitesi/head-first-design-patterns-turkce.md` — MVC compound pattern eksik
- [x] D5.7 `veri-sistemler/thinking-in-systems-turkce.md` — Archetype 5-8 eksik
- [x] D5.8 `veri-sistemler/ddia-turkce.md` — Linearizability vs Serializability ayrımı yetersiz
- [x] D5.9 `ileri-duzey-rehberler/senior-backend-developer-roadmap.md` — Node.js odağı başlıkta belirtilmiyor
- [x] D5.10 `ileri-duzey-rehberler/senior-backend-developer-roadmap.md` — Testing bölümü eksik
- [x] D5.11 `ileri-duzey-rehberler/advanced-backend-engineering.md` — Event Sourcing derinliği yetersiz

### D6. İleri Düzey Dosyalar Arası Tekrar Azaltma

- [x] D6.1 Saga Pattern tekrarı: İki dosya arasında birinden diğerine referans verilmeli
- [x] D6.2 Circuit Breaker tekrarı: Aynı şekilde çapraz referans eklenmeli
- [x] D6.3 Connection Pooling tekrarı: Aynı şekilde çapraz referans eklenmeli

---

## 🆕 YENİ — Orijinal Denetimde Kaçırılan Bulgular (2026-09-04)

### YZ1. Kırık Başlık (Anchor) Linkleri — 20 adet

> İçindekiler tablolarındaki bazı anchor'lar, GitHub'ın slug algoritmasıyla üretilen gerçek başlık anchor'larıyla eşleşmiyordu. Üç neden: (a) İ→`i̇` birleşik nokta farkı, (b) emoji başlıktan gelen baştaki tirenin TOC'ta eksik olması, (c) Türkçe karakterlerin ASCII'ye indirgenmesi veya başlıktan bir kelimenin (ör. "Falcon", "Leverage Points") anchor'da eksik kalması. Hepsi başlık metninden hesaplanan doğru slug ile düzeltildi.

- [x] YZ1.1 `pratik/postmortem-arsivi.md` — 6 anchor (ASCII-fold + eksik "Falcon"): `baglanti→bağlantı`, `cıkardı→çıkardı`, `ic-bagımlılık→i̇ç-bağımlılık`, `gunluğun…calıstırması→günlüğün…çalıştırması`, `+falcon`, `musteri→müşteri`
- [x] YZ1.2 `pratik/mimari-elestiri.md`, `staff-soft-skills.md`, `operasyonel-derinlik.md`, `domain-mimarileri.md` — `İleri Okuma`/`Kontrol Listesi` başlıklarında emoji-tire + İ farkı
- [x] YZ1.3 `pratik/karar-cercevesi-matrisleri.md`, `networking-derinlemesine.md`, `hukuk-uyumluluk-etik.md`, `staff-yazma-kulturu.md` — İ→`i̇` anchor farkı
- [x] YZ1.4 `veri-sistemler/thinking-in-systems-turkce.md` — anchor'da eksik parantez içi İngilizce (`-leverage-points`, `-bounded-rationality`)
- [x] YZ1.5 `ileri-duzey-rehberler/*-roadmap.md` & `advanced-backend-engineering.md` — `#giriş → #-giriş` (emoji başlık)

### YZ2. CI Kalite Kapısı Eklendi

> Repo, denetim standartlarını *tarif ediyordu* ama otomatik *çalıştırmıyordu*. Artık her push/PR'da çalışan bir kapı var.

- [x] YZ2.1 `.github/scripts/check_links.py` — stdlib-only; `�` (U+FFFD) taraması + kırık dosya linki + GitHub uyumlu anchor doğrulaması
- [x] YZ2.2 `.github/workflows/quality.yml` — bloklayan link/karakter denetimi + bilgilendirici markdownlint
- [x] YZ2.3 `.markdownlint-cli2.jsonc` — gürültülü kurallar kapatılmış makul yapılandırma

---

## 🟢 D5 — İçerik Eksiklikleri (2026-09-04'te TAMAMLANDI)

Tümü ilgili kitaba sadık, mevcut pedagojik stille, yeniden numaralandırma yapmadan (`###` alt-başlık) eklendi; CI anchor doğrulamasından geçti.

- [x] D5.1 fundamentals — Orchestration-Driven **SOA** stili (neden terk edildi) eklendi
- [x] D5.2 ddd — **Specification Pattern** (Supple Design) + **Large-Scale Structure** (4 kalıp) eklendi
- [x] D5.3 hard-parts — **8 Transaksiyonel Saga deseni** matrisi + **Sysops Squad** vakası eklendi
- [x] D5.4 clean-code — **Successive Refinement** (Uncle Bob'un Args örneği) eklendi
- [x] D5.5 refactoring — **Video mağazası** adım-adım açılış örneği eklendi
- [x] D5.6 head-first — **MVC bileşik deseni** (Observer+Strategy+Composite) eklendi
- [x] D5.7 thinking-in-systems — **Archetype 5–8** (Shifting the Burden, Escalation, Tragedy of the Commons, Growth & Underinvestment) eklendi
- [x] D5.8 ddia — **Linearizability ≠ Serializability** ayrımı + strict serializability kutusu eklendi
- [x] D5.9 senior-roadmap — Node.js/TypeScript odağı Giriş'te belirtildi + test rehberlerine çapraz referans
- [x] D5.10 senior-roadmap — Testing, mevcut "Testing Strategies" alt-bölümü + deep test rehberlerine (unit-testing, test-stratejileri) çapraz referansla ele alındı
- [x] D5.11 advanced-backend — **Event Sourcing derinlemesine** (snapshot, projection, schema evolution, GDPR/crypto-shredding) eklendi

---

## 🟢 Ek Tamamlananlar (2026-09-04, PR2)

- [x] **D2.2** — Yol haritası "Kitap" tablolarının açıklama sütunu "Açıklama"ya standartlaştırıldı.
- [x] **Y3.1** — Saga Pattern çapraz referansları: building-microservices ↔ hard-parts ↔ advanced-backend arası "Ayrıca bkz." eklendi.

## 🆕 KAPSAM DIŞI YENİ BÖLÜM — Yapay Zeka Çağında Mühendislik (PR2)

> Orijinal denetimde yoktu; kullanıcı talebiyle eklenen yeni üst kategori (`yapay-zeka-cagi/`, ~1000 satır). Niş, uygulayıcı odaklı agent mühendisliği.

- [x] AI1 `yapay-zeka-cagi/agentic-muhendislik.md` — token ekonomisi, context mühendisliği, agentic loop, tool/skill, MCP, compaction, AI ile kodlama
- [x] AI2 `yapay-zeka-cagi/otonom-ve-oz-gelisen-sistemler.md` — çoklu-agent, otonom/gece agent'leri, öz-gelişen sistemler, guardrail, eval
- [x] AI3 `yapay-zeka-cagi/dunyada-ai-kullanimi.md` — benimseme, üretim mimarileri, ekonomi, yönetişim
- [x] AI4 `yapay-zeka-cagi/README.md` + kök README kategori girişi

## ⏭️ Kalan Tek Ertelenen (Tartışma Gerektirir)

- **D3.1–D3.2** — 11.5K / 4.3K satırlık dosyaların alt dosyalara bölünmesi. **Öneri: yapılmasın** — mevcut dosyaların iyi TOC'u var, ve bölme (a) inbound anchor linklerini kırar (aralarındaki Saga çapraz referansları dahil), (b) dış linkleri bozar, (c) içerik doğruluğuna değer katmaz. Kullanıcı ısrar ederse dikkatli, anchor-koruyan bir bölme yapılabilir.

---

## 📊 İlerleme Özeti

| Öncelik | Toplam | Düzeltildi | Bekliyor | Ertelendi |
|---------|:------:|:----------:|:--------:|:-------:|
| 🔴 Kritik | 21 | 21 | 0 | 0 |
| 🟡 Yüksek | 13 | 13 | 0 | 0 |
| 🟠 Orta (Typo) | 50 | 50 | 0 | 0 |
| 🔵 Düşük | 23 | 21 | 0 | 2 |
| 🆕 Yeni (YZ) | 8 | 8 | 0 | 0 |
| 🤖 AI Bölümü (yeni kapsam) | 4 | 4 | 0 | 0 |
| **Toplam** | **119** | **117** | **0** | **2** |

> Kalan 2 madde yalnızca **D3.1–D3.2** (dosya bölme); önerimiz yapılmaması yönünde (yukarıda gerekçe). İçerik doğruluğu, yapısal bütünlük veya içerik tamlığı ile ilgili **bekleyen bir sorun yoktur**.
