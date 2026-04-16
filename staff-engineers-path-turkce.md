# 🧭 The Staff Engineer's Path — Türkçe Kapsamlı Rehber

> **"Staff engineer olmak, daha zor problemler ÇÖZMEK değil.
> Doğru problemlerin ÇÖZÜLMESİNİ sağlamaktır."**
> — Tanya Reilly

Bu kitap KOD yazmayı ÖĞRETmez. Kod yazmayı zaten BİLİYORSUN.
Bu kitap, **Senior'dan sonra NE yapacağını** öğretir.
IC (Individual Contributor) yolunda ilerlemek isteyenler için
yöneticilik DIŞINDA bir kariyer yolu çizer. 🛤️

---

## 📖 İçindekiler

1. [Staff Engineer Nedir?](#1--staff-engineer-nedir)
2. [Büyük Resim Düşüncesi (Big-Picture Thinking)](#2--büyük-resim-düşüncesi)
3. [Teknik Vizyon ve Strateji](#3--teknik-vizyon-ve-strateji)
4. [Proje Yönetimi (Teknik Liderlik)](#4--proje-yönetimi-teknik-liderlik)
5. [Etki Alanını Genişletme](#5--etki-alanını-genişletme)
6. [Karar Verme ve Trade-off'lar](#6--karar-verme-ve-trade-offlar)
7. [İletişim ve Etki (Influence)](#7--i̇letişim-ve-etki-influence)
8. [Dokümantasyon ve Yazma](#8--dokümantasyon-ve-yazma)
9. [Mentorluk ve Sponsorluk](#9--mentorluk-ve-sponsorluk)
10. [Organizasyonel Farkındalık](#10--organizasyonel-farkındalık)
11. [Zaman ve Enerji Yönetimi](#11--zaman-ve-enerji-yönetimi)
12. [Teknik Borç ve Planlama](#12--teknik-borç-ve-planlama)
13. [Mimari Denetim (Architecture Review)](#13--mimari-denetim)
14. [Kültür Oluşturma](#14--kültür-oluşturma)
15. [Kariyer Büyümesi](#15--kariyer-büyümesi)
16. [Büyük Şirketlerde Staff Engineer Rolü](#16--büyük-şirketlerde-staff-engineer-rolü)
17. [Yapay Zeka Çağında Staff Engineering](#17--yapay-zeka-çağında-staff-engineering)
18. [Son Sözler](#18--son-sözler)

---

## 1. 🏔️ Staff Engineer Nedir?

### IC Kariyer Merdiveninin Üst Basamakları

```
Tipik IC (Individual Contributor) kariyer yolu:

  Junior Engineer → Mid-Level → Senior → ???

  Birçok şirkette Senior'dan sonra YOL İKİYE ayrılır:

  ┌─────────────────────────┐     ┌─────────────────────────┐
  │ YÖNETİCİ YOLU 👔        │     │ IC YOLU 🔧              │
  │                         │     │                         │
  │ Engineering Manager     │     │ Staff Engineer          │
  │ Senior EM               │     │ Senior Staff Engineer   │
  │ Director of Engineering │     │ Principal Engineer      │
  │ VP of Engineering       │     │ Distinguished Engineer  │
  │ CTO                     │     │ Fellow                  │
  └─────────────────────────┘     └─────────────────────────┘

  Yönetici: İNSANLARI yönetir (1-on-1, perf review, hiring)
  Staff IC: TEKNİK YÖNÜ yönetir (mimari, strateji, standartlar)

  "Staff engineer OLMAK İÇİN kod yazmaktan FAZLASINI yapmalısın.
   AMA kod yazmayı BIRAKMAMALSIN!" 🎯
```

### Staff Engineer'ın 4 Arketipi

```
Will Larson'ın tanımladığı 4 archetype:

1. TECH LEAD 🎯
   → Bir takımın teknik YÖNLENDİRİCİSİ
   → Takım mimarisini belirler, teknik kararları alır
   → "Bu sprint'te nasıl yapacağız?"
   → EN YAYGIN archetype

2. ARCHITECT 🏗️
   → Organizasyon genelinde mimari yön belirler
   → Sistem sınırlarını çizer, standartları koyar
   → "Şirket genelinde event-driven'a geçiyoruz"
   → Büyük şirketlerde yaygın

3. SOLVER 🔍
   → Kritik, karmaşık SORUNLARI çözer
   → Bir takıma kalıcı değil, soruna kalıcı
   → "Bu performans sorunu ÇÖZÜLMELI → gidip çöz!"
   → Zor problem UZMANICISI

4. RIGHT HAND 🤝
   → VP/Director'ün teknik ELİ
   → Organizasyonel ölçekte teknik kararlarda yardımcı
   → "CTO'nun güvendiği teknik danışman"
   → Nadir ama güçlü pozisyon

HANGISI SEN?
  → Çoğu Staff engineer birden fazla arketipi KARIŞTIRIR
  → Bağlamına göre şapka DEĞIŞTIR
  → "Bu hafta Tech Lead'im, gelecek ay Solver'ım" → normal!
```

### Senior vs Staff: FARK NE?

```
SENIOR ENGINEER:
  → Verilen problemi ÇÖZer
  → Kendi takımının kodunu iyileştirir
  → İyi PR review yapar
  → "Bu feature'ı nasıl implement ederim?"
  → ETKİ: Kendi takımı

STAFF ENGINEER:
  → Doğru problemi BULUR ve çözülmesini SAĞLAR
  → Birden fazla takımı ETKİLER
  → Teknik strateji BELIRLER
  → "Hangi feature'ları YAPMAMALIYIZ?"
  → ETKİ: Organizasyon geneli

  ┌────────────────────────────────────────────────────────┐
  │                                                        │
  │  Senior: "Bu kodu nasıl YAZARIM?"                     │
  │  Staff:  "Bu kodu YAZMALIMIYIZ?"                      │
  │                                                        │
  │  Senior: "Bu bug'ı nasıl DÜZELTİRİM?"               │
  │  Staff:  "Neden bu tür bug'lar OLUŞUYOR?"            │
  │                                                        │
  │  Senior: "Bu sistem nasıl ÖLÇEKLENİR?"              │
  │  Staff:  "Bu sistemi ölçeklemeli miyiz yoksa          │
  │           YENIDEN Mİ tasarlamalıyız?"                  │
  │                                                        │
  │  FARK: Doğru CEVAP bulmak değil,                      │
  │        doğru SORU sormak!                              │
  │                                                        │
  └────────────────────────────────────────────────────────┘
```

---

## 2. 🗺️ Büyük Resim Düşüncesi

### "Haritacı" Olmak

```
Senior engineer: AĞACIN detaylarını bilir 🌳
Staff engineer: ORMANIN haritasını çizer 🗺️

AĞAÇ (Senior bakışı):
  → "Bu fonksiyon O(n²), optimize edeyim"
  → "Bu endpoint'e cache ekleyeyim"
  → "Bu test coverage'ı düşük, artırayım"
  → DOĞRU ama KISMI bakış

ORMAN (Staff bakışı):
  → "Bu servis NEDEN yavaş? Tek fonksiyon mu yoksa MİMARİ mi?"
  → "Cache eklemek çözüm mü, yoksa veri modeli mi yanlış?"
  → "Test coverage yüksek AMA yanlış şeyleri mi test ediyoruz?"
  → Bağlamı GÖREN bakış

NASIL BÜYÜK RESMI GÖRMELI?

1. SİSTEM HARİTASINI ÇİZ
   → Tüm servislerin bağımlılık diyagramı
   → Veri akışı: A → B → C
   → Darboğazlar nerede?
   → Tek nokta arızaları nerede?
   → C4 modeli ile: Context → Container → Component

2. SORU SOR (çok soru sor!)
   → "Bu servisin SLA'sı ne?"
   → "Bu DB en son ne zaman kapasiteye ulaştı?"
   → "Bu API'yi kaç takım kullanıyor?"
   → "Bu bağımlılık çökerse ne olur?"
   → Kimsenin sormadığını SOR!

3. BAĞLANTILARI GÖR
   → "A takımının refactoring'i B takımını nasıl etkiler?"
   → "Bu migration başarısız olursa hangi müşteriler etkilenir?"
   → Silolar ARASI düşün!
```

### Teknik Radar

```
Şirketinin teknik RADARINI tut:

┌────────────────────────────────────────────────────┐
│                   TEKNİK RADAR                      │
├─────────────┬──────────────────────────────────────┤
│ ADOPT ✅     │ Aktif kullanıyoruz, standart          │
│             │ → Node.js, PostgreSQL, Kafka, K8s    │
├─────────────┼──────────────────────────────────────┤
│ TRIAL 🧪    │ Deniyoruz, umut verici                │
│             │ → gRPC, OpenTelemetry, Temporal      │
├─────────────┼──────────────────────────────────────┤
│ ASSESS 🔍   │ Araştırıyoruz, potansiyeli var        │
│             │ → WASM, Deno, event sourcing          │
├─────────────┼──────────────────────────────────────┤
│ HOLD ⛔     │ Kullanmayı BIRAKIN, yeni projelerde   │
│             │ KULLANMAYIN                           │
│             │ → jQuery, Mongoose, callback hell    │
└─────────────┴──────────────────────────────────────┘

Bu radar'ı KİM günceller? → SEN! (Staff engineer!)
  → Yeni teknolojileri DEĞERLENDİR
  → Mevcut teknolojilerin sağlığını İZLE
  → Eskiyen teknolojilerin GÖÇ planını yap
  → "Bu teknoloji 3 yıl sonra bizi DARBOĞAZA sokar mı?"
```

---

## 3. 🔭 Teknik Vizyon ve Strateji

### Vizyon vs Strateji vs Taktik

```
VİZYON = Nereye gidiyoruz? (Uzak gelecek, 2-5 yıl)
  → "Tüm sistemimiz event-driven olacak"
  → "Monorepo'dan polyrepo'ya geçeceğiz"
  → "Her servis kendi veritabanına sahip olacak"
  → ILHAM VERİCİ ama somut OLMAK ZORUNDA DEĞİL

STRATEJİ = Oraya nasıl gideceğiz? (Orta vade, 6-18 ay)
  → "İlk Q1'de sipariş servisini ayıracağız"
  → "Q2'de event bus'ı kuracağız (Kafka)"
  → "Q3'te ilk 3 servisi event-driven yapacağız"
  → SOMUT ama ESNEK (değişebilir!)

TAKTİK = Bu hafta/sprint NE yapacağız?
  → "Kafka cluster'ını kuruyoruz"
  → "Sipariş servisi event producer ekleyeceğiz"
  → Sprint planlama, ticket'lar, PR'lar
  → ÇOK SOMUT ve KISA VADELİ

PIRAMIT:
  ┌─────────┐
  │ VİZYON  │  ← Staff engineer BELIRLER
  ├─────────┤
  │STRATEJİ │  ← Staff engineer + EM birlikte PLANLAR
  ├─────────┤
  │ TAKTİK  │  ← Takım birlikte UYGULAR
  └─────────┘

  Staff engineer olarak SEN:
  → Vizyonu BELİRLERSİN (veya belirlenmesine KATKIDA bulunursun)
  → Stratejiyi PLANLARSIN
  → Taktiği DENETLERSIN (mikro yönetim DEĞİL!)
```

### Teknik Strateji Dokümanı

```
Her Staff engineer'ın yazması gereken DOKÜMAN:

═══════════════════════════════════════════
  TEKNİK STRATEJİ: [Alan Adı]
═══════════════════════════════════════════

1. MEVCUT DURUM (Where are we?)
   → Bugün sistemimiz nasıl görünüyor?
   → Güçlü yönler, zayıf yönler
   → Ölçümler: latency, uptime, deploy sıklığı

2. HEDEF DURUM (Where do we want to be?)
   → 12-18 ay sonra nasıl görünmeli?
   → Hangi problemler ÇÖZÜLMÜŞ olmalı?
   → Başarı metrikleri

3. BOŞLUK ANALİZİ (Gap Analysis)
   → Mevcut ↔ Hedef arasındaki FARK ne?
   → En büyük engeller?
   → Riskler?

4. ADIM ADIM PLAN (Incremental Steps)
   → Q1: ...
   → Q2: ...
   → Her adım BAĞIMSIZ DEĞERLİ olmalı!
   → "Büyük patlama" migration YASAK! 🚫

5. YAPMADIKLARIMIZ (Non-Goals)
   → "BUNU yapmıyoruz çünkü..." → KRITIK!
   → Kapsamı SINIRLA → her şeyi birden YAPMA!

6. RİSKLER VE ALTERNATİFLER
   → "Bu plan başarısız olursa Plan B ne?"
   → "Hangi koşullarda stratejiyi DEĞİŞTİRMELİYİZ?"
```

---

## 4. 📋 Proje Yönetimi (Teknik Liderlik)

### Staff Engineer = PM DEĞİL, ama...

```
Staff engineer projeyi "yönetmez" AMA:
  → Teknik YÖNÜ belirler
  → Riskleri ERKEN tespit eder
  → Engellereri KALDIRIR
  → Diğer takımlarla KOORDINE eder

"Teknik proje liderliği = 
 kimsenin yapmak İSTEMEDİĞİ ama birinin YAPMASI gereken iş!" 😅
```

### Projeyi Parçalara Ayırma

```
BÜYÜK PROJE → KÜÇÜK MILESTone'lar

❌ KÖTÜ PLAnlama:
  Milestone 1: Tüm altyapıyı kur (3 ay)
  Milestone 2: Tüm servisleri migrate et (6 ay)
  Milestone 3: Eski sistemi kapat (1 ay)
  → 9 ay boyunca SIFIR DEĞER! İlk milestone'a kadar hiç çıktı yok!
  → 3. ayda "yanlış gidiyoruz" → 3 ay HEBA!

✅ İYI PLANLAMA:
  Milestone 1: 1 servisi yeni altyapıda çalıştır (2 hafta)
  → HEMEN değer! Doğru yolda mıyız? ERKEN feedback!
  
  Milestone 2: 3 servisi daha geçir (4 hafta)
  → Patterın doğrulanıyor, artık HIZLANIYORUZ!

  Milestone 3: Kalan servisleri paralel geçir (6 hafta)
  → Deneyim birikimiyle HIZLI!

  → Her milestone BAĞIMSIZ DEĞERLİ!
  → Her birinde "doğru mu?" kontrolü var!
  → Yanlışsa ERKEN DÖN! ✅

"Her milestone rollback yapılabilir olmalı.
 Geri dönüşü olmayan adım EN SONA bırakılır."
```

### Risk Yönetimi

```
PROJENİN EN BÜYÜK RİSKLERİNİ BULMAK:

SORU: "Bu proje NEDEN başarısız olabilir?"

1. TEKNİK RİSKLER 🔧
   → "Bu teknoloji production'da hiç DENENMEDİ"
   → "Performans yeterli olacak mı BİLİNMİYOR"
   → ÇÖZÜM: PoC / spike → ERKEN test et!

2. BAĞIMLILIK RİSKLERİ 🔗
   → "Platform ekibinin API'si hazır OLMAZSA..."
   → "Üçüncü parti servis SLA'sı yetmezse..."
   → ÇÖZÜM: Bağımlılıkları listle → kritik olanları SİMÜLE ET

3. İNSAN RİSKLERİ 👥
   → "Senior dev bu projenin ortasında ayrılırsa..."
   → "Bilgi tek kişide yoğunlaşırsa..." (Brent problemi!)
   → ÇÖZÜM: Bilgi paylaşımı, pair programming, dokümantasyon

4. KAPSAM RİSKLERİ 📏
   → "Bu projeye sürekli yeni gereksinim ekleniyor!"
   → "Scope creep → hiç BİTMEYEN proje!"
   → ÇÖZÜM: Non-goals belgele, HAYIR demeyi öğren!

RİSK MATRİSİ:

  ┌────────────────────────────────────────┐
  │               ETKİ                     │
  │           Düşük    Yüksek              │
  │ Olasılık ─────────────────             │
  │ Yüksek  │ İZLE   │ ÖNCELİK│ ← İLK!   │
  │         │        │ DÜZELT! │           │
  │ Düşük   │ KABUL  │ PLANLA  │           │
  │         │ ET     │         │           │
  └────────────────────────────────────────┘
```

---

## 5. 🌊 Etki Alanını Genişletme

### Etki Daire Modeli

```
Junior:   → KENDİ kodu 🎯
Mid:      → KENDİ feature'ı 📦
Senior:   → KENDİ takımı 👥
Staff:    → BİRDEN FAZLA takım 🏢
Principal: → TÜM organizasyon 🌐

STAFF ENGINEER'ın ETKİ ALANI:

  ┌─────────────────────────────────────────┐
  │                                         │
  │   ┌───────────────────────────────┐     │
  │   │                               │     │
  │   │   ┌───────────────────┐       │     │
  │   │   │                   │       │     │
  │   │   │   KENDİ TAKIMI    │       │     │
  │   │   │   (do the work)   │       │     │
  │   │   │                   │       │     │
  │   │   └───────────────────┘       │     │
  │   │                               │     │
  │   │   KOMŞU TAKIMLAR             │     │
  │   │   (collaborate)               │     │
  │   │                               │     │
  │   └───────────────────────────────┘     │
  │                                         │
  │   ORGANİZASYON GENELİ                  │
  │   (influence & guide)                   │
  │                                         │
  └─────────────────────────────────────────┘

İÇ DAIRE: İşi KENDİN yap
ORTA DAIRE: Başkalarıyla İŞBİRLİĞİ yap
DIŞ DAIRE: ETKİLE ve YÖNLENDİR (yapma, YAPTIR!)
```

### Glue Work (Yapıştırıcı İş)

```
"GLUE WORK" = Kimsenin sahiplenmediği ama yapılmazsa
               projenin ÇÖKECEĞI işler

ÖRNEKLER:
  → İki takım arasında iletişimi SAĞLAMA
  → Toplantı notlarını YAZMA
  → Migration planını HAZIRLAMA
  → Cross-team bağımlılıkları YÖNETME
  → On-call runbook GÜNCELLEME
  → Yeni çalışanı ONBOARD etme

DİKKAT:
  Glue work ÖNEMLİDİR ama TUZAKTIR!

  → Çok fazla glue work → KOD YAZMAYI BIRAKTIN → teknik becerin KÖRELIR
  → Hiç glue work yapmaz → organizasyon ETKİN olarak çalışmaz
  → DENGE bul!

  KURAL:
  → Zamanının %30'u → glue work ✅
  → Zamanının %70'u → teknik iş (kod, mimari, review) ✅
  → Zamanının %80'i glue work → DUR! Yönetici mi oldun? 🚨

  "Glue work yapıyorsan ama bunun FARKINDA değilsen,
   performans değerlendirmende 'yetersiz katkı' yazabilir.
   GÖRÜNÜR KILMALI!" → Yöneticine SÖYLEMELİSİN!
```

---

## 6. ⚖️ Karar Verme ve Trade-off'lar

### Teknik Karar Çerçevesi

```
Staff engineer olarak EN ÖNEMLİ işin: KARAR vermek (veya VERDIRMEK!)

KARAR FRAMEWORK'Ü:

1. PROBLEMİ TANIMLA 🎯
   → "Ne çözmeye çalışıyoruz?" → NET olmalı!
   → "Docker imajları 15 dakikada build oluyor" → SORUN
   → "Build süresini 5 dakikaya indirmek istiyoruz" → HEDEF

2. KISITlARI BELİRLE 🚧
   → Zaman: "3 ayda bitmeli"
   → Bütçe: "Yeni altyapı maliyeti: max $X/ay"
   → İnsan: "2 developer müsait"
   → Teknik: "Mevcut CI/CD değişmemeli"

3. ALTERNATİFLERİ LİSTELE 📋
   → Seçenek A: Multi-stage build
   → Seçenek B: Buildkit cache
   → Seçenek C: Build'ı buluta taşı
   → Seçenek D: Hiçbir şey yapma (status quo!)

4. HER ALTERNATİFİN TRADE-OFF'LARI 📊
   → A: basit ama sınırlı iyileşme (15dk → 10dk)
   → B: orta karmaşıklık, iyi iyileşme (15dk → 5dk)
   → C: karmaşık kurulum ama en iyi sonuç (15dk → 2dk)
   → D: sıfır maliyet ama sorun DEVAM ediyor

5. KARAR VER ve BELGELE 📝
   → "B'yi seçiyoruz ÇÜNKÜ: [gerekçe]"
   → "C'yi seçmedik ÇÜNKÜ: kurulum maliyeti 3 ayı aşıyor"
   → ADR yaz! (Architecture Decision Record)

6. GERİ DÖN ve DOĞRULA ✅
   → 1 ay sonra: "Build süresi gerçekten 5dk'ya düştü mü?"
   → Ölç! Confirmed → harika! Unconfirmed → revize et!
```

### Karar Tipleri

```
TEK YÖNLÜ KAPI vs İKİ YÖNLÜ KAPI (Amazon)

TEK YÖNLÜ KAPI 🚪→ (Geri dönüşü ÇOK ZOR)
  → "PostgreSQL'den MongoDB'ye geçiyoruz" → geri dönmek ÇILIK!
  → "Monolith'i microservices'e böldük" → birleştirmek ÇOK pahalı!
  → Bu kararlar DİKKATLE alınmalı!
  → Daha çok analiz, daha çok ADR, daha çok onay

İKİ YÖNLÜ KAPI 🚪↔ (Geri dönüşü KOLAY)
  → "Bu library yerine şunu deneyelim" → beğenmezsek geri alırız
  → "Bu caching stratejisini deneyelim" → işe yaramazsa kaldırırız
  → Bu kararlar HIZLI alınabilir!
  → "Deney yap, sonucuna bak, gerekirse geri al"

STAFF ENGINEER OLARAK:
  → Tek yönlü kapılarda: YAVAŞLA, analiz et, ADR yaz
  → İki yönlü kapılarda: HIZLAN, deney yap, iterasyon!
  → "Her kararı aynı ağırlıkta ele almak = YAVAŞlık!"
  → Kararın GERİ DÖNÜŞÜNÜn maliyetine göre HARCANAN eforu AYARLA!
```

### "Disagree and Commit"

```
Her zaman HERKES aynı fikirde OLMAZ! Ve olması GEREKMEZ!

SENARYO:
  → Sen: "Event-driven yapmalıyız"
  → Meslektaş: "REST yeterli"
  → 3 saat tartışma → kimse ikna OLMUYOR

DISAGREE AND COMMIT:
  → "Sana katılmıyorum AMA takımın kararına SAYGI duyuyorum.
     REST ile gideceğiz. BEN de elimden gelenin en iyisini yapacağım."
  → Kararı SABOTE etme!
  → "Ben zaten event-driven demiştim" → YASAK! 🚫
  → Karar verildi → COMMIT et → başarılı olması için ÇALIŞ!

AMA:
  → Kararın YANLIŞ olduğunu gösteren VERİ topla
  → "3 ay önce REST seçtik. Şu an 15 endpoint arası senkron çağrı var,
     latency kabul edilemez seviyede. Event-driven'ı yeniden değerlendirelim mi?"
  → Veri ile GERİ GEL → kişisel fikirle DEĞİL!
```

---

## 7. 💬 İletişim ve Etki (Influence)

### Yetki Olmadan Liderlik

```
Staff engineer olarak SENİN ALTINDA kimse ÇALIŞMAZ!
→ İnsanlara"yap!" diyemezsin → ama "yapılmasını SAĞLAMALSIN!"
→ YETKI OLMADAN LIDERLIK = en zor liderlik türü!

NASIL?

1. GÜVENILIRLIK İNŞA ET (Credibility) 🏗️
   → "Bu kişi söylediğini YAPAR" → tutarlılık!
   → "Bu kişi teknik olarak GÜÇLÜ" → kanıtla (iyi PR'lar, çözümler)
   → "Bu kişi DİNLER" → başkalarının fikrini gerçekten DİNLE!
   → Güvenilirlik YILLARLA inşa edilir, DAKİKALARLA YIKILIR!

2. ORTAK ZEMIN BUL 🤝
   → "Sen de X'in performansından endişelisin? Ben de!"
   → Önce ORTAK PROBLEMI kabul et → sonra ÇÖZÜMÜ tartış
   → "SENİN önerdiğin çözüm de mantıklı, birlikte DAHA İYİSİNİ bulalım"

3. VERİ İLE KONUŞ 📊
   → "Bence Redis daha iyi" ❌ → sübjektif!
   → "Redis ile cache hit oranımız %95, latency p99 2ms olur" ✅ → objektif!
   → Veriye kimse İTİRAZ edemez (verinin kendisi tartışılabilir ama FİKİRLERDEN daha güçlü)

4. DOĞRU ORTAMI SEÇ 🎭
   → 1:1 → hassas konular, kişisel feedback
   → Küçük grup → teknik tartışma, karar verme
   → Büyük toplantı → bilgilendirme, hizalama
   → Yazılı → ADR, RFC, strateji dokümanı (kalıcı!)
   → "Toplantıda söylenen UNUTULUR, yazılan KALIR!"
```

### Farklı Kitlelerle İletişim

```
AYNI MESAJ → FARKLI DİL:

TEKNİK KİTLE'ye (geliştiriciler):
  "Connection pool boyutunu 20'den 50'ye çıkardığımızda,
   p99 latency 850ms'den 120ms'e düştü.
   HikariCP'nin bu davranışı connection wait timeout'undan kaynaklanıyor.
   Pool boyutunu core_count*2 + disk_spindle formülüyle ayarlamamız gerekiyor."

YÖNETİCİ KİTLE'ye (EM, Director):
  "Veritabanı bağlantı ayarlarını optimize ettik.
   En yavaş isteklerimiz 7x hızlandı (850ms → 120ms).
   Müşteri şikayetleri %60 azalacak (tahmin).
   Maliyet: 2 gün geliştirme, risk düşük."

ÜST YÖNETİM'e (VP, CTO):
  "Müşteri deneyimini olumsuz etkileyen bir performans sorunu vardı.
   Çözdük. %60 daha az şikayet bekliyoruz.
   Ek maliyet veya risk yok."

→ AYNI GERÇEK → FARKLI detay seviyesi → FARKLI dil!
→ "İzleyicini BİL, mesajını AYARLA!" 🎯
```

---

## 8. 📝 Dokümantasyon ve Yazma

### Yazma = Düşünme

```
"Bir fikri YAZAMAZSAN, o fikri ANLAMAMISSINDIR."

Staff engineer olarak YAZMAN gerekenler:

1. RFC (Request for Comments) / TASARIM DOKÜMANI
   → Büyük bir değişiklik ÖNERİYOR'sun
   → "Sipariş servisini event-driven'a geçirmeyi ÖNERİYORUM"
   → Neden? Nasıl? Trade-off'lar? Alternatifler? Timeline?
   → Takım ve paydaşlar yorum yapar → iyileşir → KARAR VERİLİR

2. ADR (Architecture Decision Record)
   → KARAR verildi → BELGELE!
   → "Ne seçtik, NEDEN seçtik, neleri SEÇMEDİK"
   → Gelecekteki mühendisler TEŞEKKÜR EDER!

3. TEKNİK STRATEJİ
   → "Önümüzdeki 12 ayda TEKNİK olarak NEREYE gidiyoruz?"
   → Vizyon + yol haritası

4. POSTMORTEM
   → "Ne oldu, neden oldu, nasıl ÖNLERİZ?"
   → Blameless! Öğrenme aracı!

5. ONBOARDING GUIDE
   → Yeni katılan mühendis ilk haftada NEYİ bilmeli?
   → Sistemi, kültürü, araçları BELGELE

6. RUNBOOK
   → "X alarmı çaldığında NE YAPACACAKSIN?"
   → Adım adım talimat → on-call mühendis İÇİN
```

### İyi Teknik Yazı Nasıl Yazılır?

```
1. ÖNCe SONUCU SÖYle (Bottom Line Up Front — BLUF)
   ❌ "3 ay boyunca araştırdık, şu şu alternatifleri değerlendirdik, 
       sonunda... Redis kullanmaya karar verdik."
   ✅ "Redis kullanmaya KARAR verdik. Gerekçe: [kısa özet]
       Detaylar aşağıda."
   → Okuyucu ilk 3 cümlede ANA MESAJI alsın!

2. KISA TUT (ama eksik BIRAKMA)
   → "Bu mesajı daha kısa yazardım ama vaktim yoktu" — Pascal
   → Uzun yazmak KOLAYDIR, kısa yazmak ZORDUR
   → Gereksiz kelimeyi SİL → kalan kelimeler DAHA GÜÇLÜ!

3. YAPILANDIR
   → Başlık, alt başlık, madde işaretleri, tablolar
   → Duvar gibi paragraf YAZMA → kimse OKUMAZ!
   → TL;DR (özet) ile BAŞLA

4. GÖRSEL KULLAN
   → Diyagram 1000 kelimeye bedel
   → Mimari diyagram, akış diyagramı, karşılaştırma tablosu
   → Mermaid, draw.io, excalidraw

5. İZLEYİCİNİ BİL
   → Kime yazıyorsun? Ne biliyorlar? Ne bilmiyorlar?
   → Çok teknik → üst yönetim ANLAMAZ
   → Çok basit → mühendisler BIKAR
```

---

## 9. 🌱 Mentorluk ve Sponsorluk

### Mentor vs Sponsor

```
MENTOR 🧑‍🏫 = Bilgi ve deneyim PAYLAŞIR
  → "Bu durumda ben şöyle yapardım..."
  → "Bu kitabı oku, çok faydalı olur"
  → "O hata normal, ben de yapmıştım. Çözüm şu..."
  → DANIŞMANLIK verir

SPONSOR 🏆 = Fırsat YARATIR ve SAVUNUR
  → "Bu projeye Ali'yi atayalım, hazır!" (görünürlük!)
  → "Ayşe bu konuşmayı konferansta yapmalı!" (platform!)
  → "Mehmet terfi etmeli, işte kanıtlar..." (savunuculuk!)
  → KAPILARI AÇAR

FARK:
  → Mentor: "Nasıl daha iyi yaparsın?" (1:1 ilişki)
  → Sponsor: "Bunu DAHA BÜYÜK sahnede yapmalısın!" (kariyer itme)

  → Mentor olmak HERKESİN işi (kıdemsiz birisi bile birini mentorlar)
  → Sponsor olmak EKSTrA SORUMLULUK → birisinin kariyerini SAHİPLENİYORSUN

STAFF ENGINEER OLARAK:
  → Junior/Mid mühendislere MENTOR ol
    → Code review'da NEDEN açıkla, sadece "değiştir" DEME!
    → Pair programming yap → derste öğrenilmeyen şeyleri GÖSTER
    → Hata yapma korkusunu AZALT → "Ben de bunu yaptım" de!

  → Yetenekli mühendislere SPONSOR ol
    → "Bu kişi terfi etmeli" → EM'e SÖYle (somut kanıtlarla!)
    → Görünürlük sağla → "Bu projeyi o yapsın, ben desteklerim"
    → Platform oluştur → tech talk, blog yazısı, konferans
```

### Code Review'da Mentorluk

```
STAFF ENGINEER'ın CODE REVIEW'u FARKLDIR:

Junior mühendis PR attı → Sen review ediyorsun:

❌ KÖTÜ REVIEW:
  "Bu fonksiyon çok uzun. Refactor et."
  → NE yapmalı? NASIL refactor etmeli? BİLMİYOR! 😤

✅ İYI REVIEW:
  "Bu fonksiyon şu anda 3 farklı iş yapıyor:
   1. Veri validasyonu
   2. İş kuralı uygulama
   3. DB kayıt
   Her birini AYRI fonksiyona çıkarırsan:
   → Her biri bağımsız test EDİLEBİLİR
   → İsimleri NE yaptığını ANLATIR
   → Değişiklik tek sorumluluğa ODAKLANIR
   Clean Code Bölüm 3'ü hatırla: 'Do one thing!'
   İstersen birlikte bakalım mı?"

  → NEDEN, NASIL ve REFERANS verdin
  → Birlikte bakma TEKLİFİ → güvenli öğrenme ortamı!
  → Bu kişi bir sonraki PR'da DAHA İYİ yazacak! 📈
```

---

## 10. 🏛️ Organizasyonel Farkındalık

### Politika Değil, Anlayış

```
"Office politics"ten NEFRET edebilirsin.
AMA organizasyonun nasıl ÇALIŞTIĞINI ANLAMALISIN!

BİLMEN GEREKENLER:

1. KARAR NASIL ALINIR?
   → "Kim onay veriyor?"
   → "Budget nasıl ayrılıyor?"
   → "Prioritization KRİTERLERİ ne?"
   → Bunu bilmezsen → doğru önerilerin bile REDDEDİLİR!

2. GÜÇ DİNAMİKLERİ
   → "Kim kimi DİNLER?"
   → "Kim kiminle çatışıyor?"
   → "Geçmişte benzer önerilere nasıl TEPKİ verildi?"
   → Bunu bilmezsen → aynı hataları TEKRARLARSIN!

3. MOTIVASYONLAR
   → VP A: "Cost cutting" öncelliği → ÖNERİNİ maliyete göre ÇERÇEVEle!
   → VP B: "Innovation" öncelliği → ÖNERİNİ yeniliğe göre ÇERÇEVEle!
   → AYNI ÖNERİ → FARKLI çerçeve → FARKLI tepki!
   → Bu manipülasyon DEĞİL, İLETIŞIM BECERİSİDİR!

4. TAKVİM
   → Q4'te bütçe kesilir → yeni proje önerme ZAMANI DEĞİL!
   → Q1'de yeni bütçe açılır → ÖNERİ ZAMANI! ✅
   → Performance review döneminde → başarılı SONUÇLARI göster!
```

### Conway's Law'u Avantajına Kullan

```
CONWAY'S LAW: "Organizasyonlar, kendi iletişim yapılarını
               YANSITAN sistemler tasarlar."

  3 takım var → 3 servis çıkar! (istemesen de!)
  Takımlar konuşmuyorsa → servisler de konuşaMIYOR!

STAFF ENGINEER OLARAK:
  → İstediğin MİMARİYE uygun TAKIM YAPISI öner!
  → "Sipariş ve ödeme servislerini ayırmak istiyoruz"
    → "O zaman sipariş ve ödeme TAKIMLARINI da ayıralım!" ✅
  → "Event-driven geçmek istiyoruz"
    → "O zaman platform takımı event bus'ı kurmalı!" ✅

INVERSE CONWAY MANEUVER:
  → Mimariyi değiştirmek için ÖNCE organizasyonu DEĞİŞTİR!
  → "Sistemi nasıl istiyorsak, takımları ÖYLE kur!"
  → Mimarlık değişikliği = ORGANİZASYON değişikliği
```

---

## 11. ⏰ Zaman ve Enerji Yönetimi

### Staff Engineer'ın Zaman Dağılımı

```
TİPİK BİR HAFTA:

  %30 → KOD ve TEKNİK İŞ 💻
    → Critical path'te kod yazma
    → Mimari spike/PoC
    → Performans analizi, debugging
    → "Koddan KOPMA! Ama her satırı sen yazma!"

  %25 → CODE REVIEW ve MENTORLUK 🧑‍🏫
    → PR review (özellikle mimari kararlar)
    → Pair programming
    → Teknik coaching

  %20 → PLANLAMA ve STRATEJİ 📋
    → Teknik strateji dokümanı
    → RFC yazma/review etme
    → Roadmap planlaması

  %15 → İLETIŞİM ve KOORDİNASYON 🤝
    → Cross-team toplantılar
    → Stakeholder alignment
    → Glue work

  %10 → ÖĞRENME 📚
    → Yeni teknoloji araştırma
    → Konferans/blog takibi
    → Deneysel proje (hobby time)

DİKKAT:
  → "Toplantılarım %60'ı kaplıyor" → SORUN! 🚨
  → → Gereksiz toplantılardan ÇIK!
  → → "Bu toplantıda BENİM olmam gerekiyor mu? Notlarla yakalayabilir miyim?"
  → → "Bu toplantı e-posta olabilir miydi?"
```

### Enerji Yönetimi (Zaman Yönetiminden Önemli!)

```
"ZAMAN yönetimi değil, ENERJİ yönetimi!"

YÜKSEK ENERJİ saatleri → DERİN İŞ (kod, mimari, yazma)
  → Sabah 9-12: çoğu insan en verimlidir
  → "Deep work window": TOPLANTI YOK! Slack KAPALI!
  → 3 saatlik kesintisiz blok = 8 saatlik bölük pörçük çalışmadan İYİ!

DÜŞÜK ENERJİ saatleri → HAFİF İŞ (toplantı, review, e-posta)
  → Öğleden sonra 14-16: enerji düşer
  → → Toplantıları BURAYA koy!
  → → Code review buraya koy
  → → Admin işleri buraya koy

ENERJI VAMPIRLERI 🧛:
  → Bitmek bilmeyen toplantılar
  → Context switching (her 5dk farklı konu)
  → Belirsiz beklentiler ("ne yapmam gerekiyor?")
  → Toxic tartışmalar

ENERJI VERENler ⚡:
  → Deep work (odaklı çalışma)
  → Birine yardım etmek (mentorluk)
  → Zor bir sorunu ÇÖZMEK
  → İlerleme HİSSETMEK (küçük de olsa!)

"Takvimindeki her şeyi EVET dersen, ENERJİNİ başkaları yönetir.
 HAYIR demeyi öğrenmek, Staff engineer olmanın ÖN KOŞULUDUR."
```

### Doğru İşe Zamanını Yatır

```
LEVERAGE (Kaldıraç Etkisi):

  Düşük kaldıraç:
  → Bir bug'ı KENDİN düzeltmek → 1 kişi faydalandı (sen)

  Orta kaldıraç:
  → Bir araç/library yazmak → 10 kişi faydalandı (takım)

  Yüksek kaldıraç:
  → Bir standart/pattern belirlemek → 100 kişi faydalandı (org)
  → Bir otomasyon kurmak → her gün 50 kişi faydalanıyor (sürekli!)
  → Bir mimari karar almak → gelecek 3 yılı ŞEKİLLENDİRDİN

  STAFF ENGINEER = YÜKSEK KALDIRAÇLI İŞLER YAP!

  Kendine sor:
  "Bu iş SADECE BENİM için mi değerli, yoksa ORGANİZASYON için mi?"
  → Sadece ben → belki YAPMA (başkası yapabilir)
  → Organizasyon → KESINLIKLE YAP! ✅

  "Bu işi BEN yapmazsam ne olur?"
  → Hiçbir şey → YAPMA!
  → Proje durur → BELKİ yap (ama başka biri yapabilir mi bak!)
  → Yanlış karar alınır → KESINLIKLE SEN yap/katıl! ✅
```

---

## 12. 🏗️ Teknik Borç ve Planlama

### Teknik Borç Kategorileri

```
Staff engineer olarak teknik borcu sadece "kötü şey" olarak GÖRME!
→ BİLİNÇLİ teknik borç → ARAÇTIR! (kredi gibi!)

4 ÇEYREK MODELİ (Martin Fowler):

            BİLİNÇLİ              BİLİNÇSİZ
          ┌────────────────────┬────────────────────┐
  İHTİYATLI│ "Bilerek basit    │ "Daha iyi bir yol │
          │  yaptık, sonra    │  olduğunu ŞİMDİ   │
          │  refactor edeceğiz"│  öğrendik"         │
          │                    │                    │
          │ → PLANLI teknik   │ → ÖğRENME borcu   │
          │   borç ✅          │   (normal!) ✅      │
          ├────────────────────┼────────────────────┤
  İHTİYATSIZ│ "Vakit yok,       │ "Katmanlama ne?"  │
          │  hızlı yapalım!"  │                    │
          │                    │ → Bilgi EKSİKLİĞİ │
          │ → ACELE borcu     │   borcu 😱          │
          │   (dikkatli ol!) ⚠️│   (eğitim lazım!)  │
          └────────────────────┴────────────────────┘

STAFF ENGINEER'ın GÖREVI:
  → BİLİNÇLİ-İHTİYATLI borcu YÖNET (ne zaman ödeyeceğiz?)
  → İHTİYATSIZ borcu SINIRLA (deadline baskısı sırasında bile!)
  → BİLİNÇSIZ borcu KEŞFET (kod incelemeleri, retrospective)
  → BİLGİ EKSİĞİ borcunu AZALT (eğitim, mentorluk)
```

### Teknik Borcu İş Diline Çevir

```
❌ TEKNİK DİL (yönetici ANLAMAZ):
  "Monolith'imizde circular dependency var, modülleri refactor etmeliyiz."
  → Yönetici: "Ne? Neden? Müşteriye etkisi ne?"

✅ İŞ DİLİ (yönetici ANLAR):
  "Yeni feature geliştirme süremiz 6 ayda %40 yavaşladı.
   Her yeni feature'ın ortalama geliştirme süresi 2 hafta → 3 hafta oldu.
   Bunun nedeni kod yapısındaki karmaşıklık.
   2 haftalık bir yeniden yapılandırma çalışması ile:
   → Feature geliştirme süresini tekrar 2 haftaya DÜŞÜREBİLİRİZ
   → Yılda ~10 ekstra feature çıkarabiliriz
   → Bu = yaklaşık X TL ek gelir veya Y müşteri memnuniyeti"

  → Teknik borcu para/zaman/müşteri ETKİSİne ÇEVİR!
  → Yönetici sayıları ANLAR!
```

### Teknik Borç Bütçesi

```
"Sprint kapasitesinin %20'si teknik borç ödemesinedir."

AMA bu %20'yi NASIL kullanıyorsun?

ÖNCELİKLENDİRME MATRİSİ:

                    Ödeme Kolaylığı
                    Kolay      Zor
  Etki    ┌──────────┬──────────┐
  Yüksek  │ HEMEN!   │ PLANLA!  │
          │ Quick win│ Büyük    │
          │          │ proje    │
          ├──────────┼──────────┤
  Düşük   │ BOŞTA    │ BIRAK!   │
          │ YAP      │ (şimdilik│
          │          │  değmez) │
          └──────────┴──────────┘

  Yüksek etki + kolay → HEMEN yap! (bu sprinte koy!)
  Yüksek etki + zor → PLANLA! (roadmap'e koy, R&D spike yap)
  Düşük etki + kolay → boşta kaldığında yap
  Düşük etki + zor → DOKUNMA! Zamanla ÖNEMSİZLEŞEBİLİR
```

---

## 13. 🔍 Mimari Denetim

### Architecture Review Süreci

```
Staff engineer olarak mimari denetim YAPMAN veya SÜRDÜRMEn beklenir.

NE ZAMAN MİMARİ REVIEW GEREKLİ?
  → Yeni servis oluşturuluyor
  → Mevcut servis önemli ölçüde değişiyor
  → Yeni teknoloji/framework kullanılacak
  → Veri modeli değişiyor
  → Dış bağımlılık ekleniyor
  → Güvenlik sınırları değişiyor

REVIEW SORULARI:

TASARIM:
  □ "Bu tasarım hangi gereksinimi ÇÖZÜYOR?"
  □ "Alternatifler neler? Neden BU seçildi?"
  □ "Trade-off'lar neler? Kabul edilebilir mi?"

ÖLÇEKLENEBİLİRLİK:
  □ "10x kullanıcıda çalışır mı?"
  □ "Darboğaz nerede oluşur?"
  □ "Bağımsız ölçeklenebilir mi?"

GÜVENİLİRLİK:
  □ "Bu bileşen çökerse ne olur?"
  □ "Fallback mekanizması var mı?"
  □ "Veri kaybı riski var mı?"

GÜVENLİK:
  □ "Authentication/authorization nasıl?"
  □ "Hassas veri nasıl korunuyor?"
  □ "3. parti erişim kontrollü mü?"

OPERASYONELLİK:
  □ "Monitoring nasıl yapılacak?"
  □ "Alert'ler tanımlı mı?"
  □ "Rollback planı var mı?"
  □ "Runbook yazıldı mı?"

ÖNEMLİ: Review STRATEJİK olmalı, satır satır kod inceleme DEĞİL!
  → "Bu modülün sınırları doğru mu?" → evet
  → "Bu fonksiyondaki for döngüsü optimal mi?" → bu iş için çok detaylı!
```

---

## 14. 🌿 Kültür Oluşturma

### Teknik Kültür = Alışkanlıklar

```
"Kültür, kimse bakmadığında insanların NE YAPTIĞIDIR."

Staff engineer olarak kültürü ŞEKILLENDIRIRSIN:

1. KOD İNCELEME KÜLTÜRÜ 👀
   ❌ "Gatekeeping" → PR 3 gün bekliyor, 50 yorum, nitpicking
   ✅ "Coaching" → Hızlı review, yapıcı feedback, öğrenme odaklı

   Kurallar:
   → PR 2 saatten fazla BEKLEMEMELİ (ilk yanıt)
   → Nitpick vs gerçek sorun ayrımı → "nit:" prefix'i kullan
   → "Request changes" sadece GERÇEKTEN bloklayan sorunlar için
   → Otomatikleştirebilecek şeyleri OTOMATIKLEŞTİR (lint, format)

2. POSTMORTEM KÜLTÜRÜ 📋
   → İlk postmortem'i KENDİN yaz → örnek ol!
   → Blameless → "KİM" değil "NE" ve "NEDEN"
   → Action items → owner + deadline → TAKIP ET!
   → "Postmortem yazdık ama hiçbir şey DEĞİŞMEDİ" → BAŞARISIZ!

3. DOKÜMANTASYON KÜLTÜRÜ 📝
   → Kendin yaz → başkaları "aa demek böyle yapılıyor" der → TAKLIT eder!
   → Template oluştur → "ADR böyle yazılır, RFC böyle yazılır"
   → "Doküman yoksa OLMADI sayılır" → normu KOYMALIDIR

4. DENEY KÜLTÜRÜ 🧪
   → "Deneyelim!" → güvenli ortam SAĞLA
   → Spike/PoC → 2 gün dene → sonucu PAYLAŞ
   → "Başarısız deney = ÖĞRENİLMİŞ bilgi" → kutla!
   → "Hiç deney yapılmayan ortam = DURAĞAN ortam" → tehlikeli!

5. İŞBIRLİĞI KÜLTÜRÜ 🤝
   → Silolar KIRMA → cross-team etkinlikler, guild'ler
   → "Backend guild", "Frontend guild", "Data guild"
   → Her guild: haftalık 30dk → bilgi paylaşımı, standart tartışma
```

### "Psikolojik Güvenlik" Oluşturma

```
Google'ın Project Aristotle araştırması:
→ En başarılı takımların 1 NUMARALI özelliği = PSİKOLOJİK GÜVENLİK

"Takım üyeleri HATA yapabileceklerini, SORU sorabileceklerini,
 FİKİR sunabileceklerini bilir ve bunun için CEZALANDIRILMAYACAKLARINA
 güvenirler."

STAFF ENGINEER OLARAK SEN bunu İNŞA edersin:

→ "Ben de bunu bilmiyorum, birlikte öğrenelim" → SÖYLEDIKÇE 
   başkaları da söyleme CESARETİ bulur
→ "Güzel soru!" → her soru DEĞERLIDIR
→ "Bu yaklaşım daha önce denendi ve başarısız oldu, 
    AMA koşullar değişmiş olabilir, yeniden düşünelim" → eski başarısızlıkları
   silah olarak KULLANMA
→ Toplantıda sessiz kalan birine: "Senin de fikrin var mı?" → ALAN AÇ
→ Hata yaptığında: "BENIM hatam, düzeltiyorum" → güvenilirlik!
```

---

## 15. 📈 Kariyer Büyümesi

### Staff'a Nasıl Terfi Edilir?

```
TERFI = "Zaten o seviyede ÇALIŞIYORSUN" → formalize ediliyor.

Staff engineer TERFİ ALMAZSIN → Staff engineer gibi ÇALIŞARAK terfi edersin!

❌ "Staff'a terfimi bekliyorum, sonra o işleri yaparım"
✅ "Staff seviyesinde iş yapıyorum, terfi bunun DOĞAL sonucu"

KANIT TOPLAMA (Brag Document):
→ Her ay yaptıklarının LİSTESİNİ tut!
→ "Bu ay ne YAPTIM? Etkisi ne OLDU?"

Brag Document örneği:
┌────────────────────────────────────────────────────────┐
│ MART 2025                                              │
│                                                        │
│ 🏗️ Mimari:                                             │
│ → Sipariş servisini event-driven'a geçirdim           │
│ → Latency %40 düştü, throughput 3x arttı               │
│                                                        │
│ 📝 Dokümantasyon:                                       │
│ → ADR-012: Event bus teknoloji seçimi yazdım           │
│ → Onboarding guide'ı güncelledim (5 yeni başlayan!) │
│                                                        │
│ 🧑‍🏫 Mentorluk:                                          │
│ → 2 junior developer ile haftalık 1:1                   │
│ → Ayşe'nin ilk production deploy'unu destekledim       │
│                                                        │
│ 🤝 Cross-team:                                          │
│ → Platform takımıyla monitoring standartları belirledik │
│ → 3 takımın kullandığı shared library'yi versiyonladım │
│                                                        │
│ 📊 Etki:                                                │
│ → [Metric improvement] → [business impact]              │
└────────────────────────────────────────────────────────┘

→ Performans review'da: "Ne yaptım?" → LİSTE HAZIR! ✅
→ Somut, ölçülebilir, ETKİ odaklı! ✅
```

### Kariyer Anti-Pattern'ları

```
1. "HİÇ KOD YAZMADIM" ❌
   → Staff = kod yazmayı BIRAK demek DEĞİL!
   → Teknik becerin KÖRELIR → güvenilirliğin DÜŞER
   → "Mimar telefon açıp dal döşerken parmağı kesmez
      ama nasıl keseceğini BİLMELİDIR" → dal kesmeye de DEVAM ET!

2. "HER ŞEYİ BEN YAPMALIYIM" ❌
   → Tüm mimari kararları BEN vermeliyim → DARBOĞAZ olursun!
   → Başkalarını YETISTIR ve GÜVENDIR
   → "Bus factor'ü artır, azaltma!"

3. "SADECE KOD YAZIYORUM" ❌
   → Senior gibi çalışıp Staff beklentisi → olmaz!
   → İletişim, dokümantasyon, strateji de KATKI!
   → "En iyi kodu yazan" = Staff DEĞİL, "en çok ETKİ yaratan" = Staff!

4. "SİYASET OYUNLARI OYNAMAM" ❌
   → Organizasyonel farkındalık ≠ politika
   → Doğru zamanda doğru kişiyle doğru mesajı KONUŞMAK = ETKİLİ olmak
   → "Her şeyi biliyorum ama kimse DİNLEMİYOR" → iletişim SORUNU senin!

5. "HER ŞEYİ BİLMELİYİM" ❌
   → "Bilmiyorum" demek UTANÇ DEĞİL → GÜÇTÜR!
   → "Bilmiyorum AMA öğreneceğim" → en güçlü cümle!
   → Bilmediğini kabul edemeyen → öğrenmeyi BIRAKMIŞ demektir!
```

---

## 16. � Büyük Şirketlerde Staff Engineer Rolü

### Google — L6+ ve Ötesi

```
Google'da Staff Engineer (L6) → Senior Staff (L7) → Principal (L8):

  L6 (Staff):
    → 1-2 ekibin teknik yönünü belirler
    → Design doc'ları YAZAR ve REVIEW eder
    → Cross-team teknik kararlar alır

  L7 (Senior Staff):
    → Bir organizasyonun (5-10 ekip) teknik stratejisi
    → Şirket genelinde standart belirleme
    → "Tech Lead of Tech Leads"

  L8 (Principal):
    → Şirket genelinde teknoloji yönü
    → Google Cloud, Search gibi büyük ürünlerin mimarisi
    → ÇOK nadirdir (şirketin %0.1'i)

Reilly'nin kitabıyla bağlantı:
  → Pillar (L6 genellikle) vs Solver (L7+ genellikle)
  → Scope arttıkça KOD YAZMA oranı AZALIR
  → AMA teknik derinlik HİÇBIR ZAMAN kaybolmaz
```

### Meta — Tech Lead Manager vs Staff IC

```
Meta'da iki yol:
  → Manager track: EM → Director → VP
  → IC track: E5 → E6 (Staff) → E7 (Senior Staff) → E8 (Principal)

IC track'te KALMAK Meta'da çok değerli:
  → E6+ IC'ler şirketin EN ZOR teknik problemlerini çözer
  → Reilly'nin uyarısı: "Management'a geçmek tek yol DEĞİL"
  → "Teknik liderlik yöneticilikten DAHA AZ değerli değil"
```

### Spotify — Teknik Liderlik Modeli

```
Spotify'da Staff Engineer ≈ "System Owner":
  → Bir veya birkaç kritik sistem'in teknik sahibi
  → Ekipler arası teknik koordinasyon
  → Architectural Decision Records (ADR) yazar

Reilly'nin "Technical Vision" kavramı burada:
  → Staff Engineer gelecekteki mimariyi TANIMLAR
  → Ekipler bu vizyona doğru çalışır
  → Ama vizyon DAYATILMAZ, ekiplerle birlikte oluşturulur
```

---

## 17. 🤖 Yapay Zeka Çağında Staff Engineering

### AI Staff Engineer'ın İşini DEĞİŞTİRİYOR

```
AI ARAÇLARI staff engineer'ın hangi yeteneklerini güçlendiriyor?

  ✅ DESIGN DOC YAZMA:
     → AI ilk taslağı oluşturur
     → Staff engineer DÜZENLER ve DERINLESTIRIR
     → Zaman kazancı: %40-50

  ✅ CODE REVIEW:
     → AI basit hataları yakalar
     → Staff engineer MİMARİ kaliteye odaklanır
     → "Bu değişiklik uzun vadede nasıl etki eder?"

  ✅ TEKNİK STRATEJİ:
     → AI trend analizi ve araştırma yapar
     → Staff engineer KARAR verir
     → "Bu teknoloji 3 yıl sonra hâlâ geçerli mi?"

  ❌ AI'ın YAPAMADIĞI (insana kalan):
     → Ekipler arası politik navigasyon
     → Teknik vizyonu ANLATMA ve KABUL ETTİRME
     → Mentoring — insan ilişkisi gerektirir
     → "Bu projeyi neden şimdi yapmalıyız?" sorusuna CEVAP
```

### Staff Engineer AI Promptları

```
DESIGN DOC:
  "Bu projenin design doc'unu oluştur.
   Tanya Reilly'nin Staff Engineer's Path formatını kullan:
   1. Context: Problem ne, neden şimdi?
   2. Goals / Non-Goals: Ne yapacağız, ne YAPMAYACAĞIZ?
   3. Options: En az 3 alternatif
   4. Recommendation: Neden bu seçenek?
   5. Risks: Ne yanlış gidebilir?
   6. Milestones: Adım adım plan
   Proje: [açıklama]"

TEKNİK VİZYON:
  "3 yıllık teknik vizyon belgesi oluştur.
   Mevcut mimari: [açıklama]
   Hedef mimari: [açıklama]
   Migration planı oluştur:
   - Quick wins (0-3 ay)
   - Medium-term (3-12 ay)
   - Long-term (12-36 ay)
   Her adımda rollback planı olsun."
```

### Topluluk Görüşleri

```
Tanya Reilly (kitabın yazarı):
  "Staff Engineer olmak sadece KOD yazmak değil.
   Staff Engineer ETKİ yaratır. Etki bazen kod,
   bazen design doc, bazen mentorluk,
   bazen de 'hayır, bunu YAPMAMALIYIZ' demektir."

Will Larson (Staff Engineer, An Elegant Puzzle yazarı):
  "Staff+ roller hakkında en büyük yanılgı:
   'Daha çok kod yaz, daha hızlı terfi et.'
   Hayır. 'Doğru problemi bul ve ÇÖZ' daha kritik."

Charity Majors (Honeycomb CTO):
  "Senior'dan Staff'a geçiş karierdeki EN ZOR geçiş.
   Çünkü daha önce YAPMAKLA ödüllendiriliyordun.
   Artık DÜŞÜNMEKLE ve YÖNLENDIRMEKLE ödüllendiriliyorsun."

Reddit r/experienceddevs:
  "Reilly'nin kitabı Staff+ seviyesine geçmek isteyenler için
   EN İYİ kaynak. Larson'ın kitabı ile birlikte oku."
```

---

## 18. �🎬 Son Sözler

### Staff Engineer Özet Kartı

```
┌──────────────────────────────────────────────────────────────┐
│          STAFF ENGINEER'S PATH CHEAT SHEET                   │
├──────────────────────────────────────────────────────────────┤
│ ROL:                                                         │
│  → Doğru problemi bul, çözülmesini SAĞLA                   │
│  → Ağacı değil ORMANI gör                                   │
│  → 4 archetype: Tech Lead, Architect, Solver, Right Hand    │
│                                                              │
│ TEKNİK:                                                      │
│  → Vizyon + Strateji + Taktik piramidi                      │
│  → Kod yaz AMA her satırı sen yazma                         │
│  → Mimari denetim, teknik radar                             │
│  → ADR, RFC ile kararları BELGELE                           │
│                                                              │
│ LIDERLIK:                                                    │
│  → Yetki olmadan ETKİLE                                     │
│  → Veri ile KONUŞ                                           │
│  → Disagree and commit                                       │
│  → Mentor ve sponsor OL                                      │
│                                                              │
│ ORGANİZASYON:                                                │
│  → Conway's Law'u avantajına KULLAN                         │
│  → Kültür OLUŞTUR (review, postmortem, doküman)             │
│  → Psikolojik güvenlik İNŞA ET                              │
│  → İş dilinde KONUŞ (teknik borç → iş etkisi)              │
│                                                              │
│ KARİYER:                                                     │
│  → Brag document TUT                                         │
│  → KALDRACI işlere odaklan                                  │
│  → Glue work'ü DENGEle (%30 max)                           │
│  → Enerji yönetimi > zaman yönetimi                         │
│  → "Bilmiyorum" deme CESARETi                               │
└──────────────────────────────────────────────────────────────┘
```

### Tüm Kitaplarla Bağlantı 🔗

```
📗 Grokking Algorithms → Teknik temel → Staff hâlâ algoritmayı BİLMELİ
📕 Clean Code → Kod kalite standartları → Staff BELİRLER
📘 Pragmatic Programmer → Pragmatik düşünce → trade-off analizi
📙 Missing README → İlk kariyer temeli → Staff'a uzanan YOL
📗 Philosophy of SD → Karmaşıklık yönetimi → Staff'ın TEMEL ENDIŞESi
📘 Design Patterns → Kalıplar → Staff ORGANİZASYONEL kalıpları da görür
📕 DDIA → Sistem bilgisi → Büyük resmi GÖRebilmek için ŞART
📙 Unit Testing → Test kültürü → Staff test KÜLTÜRÜNÜ oluşturur
📗 Refactoring → Teknik borç ödeme → Staff borcu PLANLAR
🏛️ Clean Architecture → Mimari prensipler → Staff UYGULAR ve DENETLER
🏗️ Fundamentals of SA → Mimari stiller → Staff SEÇer ve SAVUNUR
🔬 Building Microservices → Servis tasarımı → Staff SINIRLARINI çizer
🔥 Phoenix Project → Kültür dönüşümü → Staff KÜLTÜR oluşturur
🏗️ System Design → Ölçeklenebilir sistemler → Staff TASARLAR
🔵 DDD → Domain modelleme → Staff STRATEJIK tasarım yapar
🧩 Hard Parts → Zor kararlar → Staff KARAR verir
🧭 Staff Engineer's Path → TÜM bunları bir araya getiren KARİYER YOLu!

Bu kitap NASIL kod yazacağını öğretmez.
NASIL bir mühendis OLACAĞINI öğretir.
Teknik BECERİ yetmez.
ETKİ, İLETİŞİM ve VİZYON da gerekir.
```

### Faz 4 İlerleme Durumu 📊

```
FAZ 4 — Ustalık (18+ ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Domain-Driven Design          ✅
  2. Software Arch: The Hard Parts ✅
  3. The Staff Engineer's Path     ✅  ← BURADASIN
  4. Thinking in Systems           ⬜
```

---

> **"Staff engineer olmak,
> en çok kodu YAZMAK değil.
> En çok etkiyi YARATMAKTIR.
>
> Bazen etki = harika bir algorithm.
> Bazen etki = doğru zamanda 'HAYIR' demek.
> Bazen etki = sessiz kalan birine 'Sen ne düşünüyorsun?' sormak.
> Bazen etki = bir ADR yazmak ki 2 yıl sonra biri 'TEŞEKKÜRLER!' desin.
>
> Kodun ötesine geç, AMA koddan asla KOPMA.
> Ağaçları bil, ama her zaman ORMANI gör.
> Ve en önemlisi:
> SENDEN sonra gelenlerin yolunu KOLAYLAŞTIR.
>
> Çünkü gerçek mühendislik mirası,
> yazdığın KOD değil,
> yetiştirdiğin İNSANLAR ve
> bıraktığın KÜLTÜRDÜR."** 🧭
