# 🧩 Software Architecture: The Hard Parts — Türkçe Kapsamlı Rehber

> **"Yazılım mimarisinde kolay kararlar yoktur. Sadece trade-off'lar vardır."**
> — Neal Ford & Mark Richards

Bu kitap, "Fundamentals of Software Architecture"ın **devamıdır** —
ama bu sefer kolay kararları değil, **ZOR kararları** ele alır.
Modüler monolith mi microservices mi? Servis nasıl bölünür?
Veri nasıl ayrıştırılır? Saga mı orkestrasyon mu?

Mimarlık kararlarının **gri alanlarında** rehberlik eder. 🎯

---

## 📖 İçindekiler

1. [Mimari Kararlar ve Trade-off Analizi](#1--mimari-kararlar-ve-trade-off-analizi)
2. [Modülerliği Keşfetmek](#2--modülerliği-keşfetmek)
3. [Mimari Ayrışma (Decomposition)](#3--mimari-ayrışma-decomposition)
4. [Bileşen Tabanlı Ayrışma](#4--bileşen-tabanlı-ayrışma)
5. [Taktiksel Forking](#5--taktiksel-forking)
6. [Veriyi Ayrıştırma](#6--veriyi-ayrıştırma)
7. [Servisler Arası İletişim](#7--servisler-arası-i̇letişim)
8. [Orkestrasyon vs Koreografi](#8--orkestrasyon-vs-koreografi)
9. [Transaksiyonel Saga'lar](#9--transaksiyonel-sagalar)
10. [Kontrat Yönetimi](#10--kontrat-yönetimi)
11. [Analitik Veri Yönetimi](#11--analitik-veri-yönetimi)
12. [Veri Mesh](#12--veri-mesh)
13. [Trade-off Teknikleri](#13--trade-off-teknikleri)
14. [Mimari Karar Kayıtları (ADR)](#14--mimari-karar-kayıtları-adr)
15. [Gerçek Hayata Uyarlama](#15--gerçek-hayata-uyarlama)
16. [Büyük Şirketlerde Hard Parts Kararları](#16--büyük-şirketlerde-hard-parts-kararları)
17. [Yapay Zeka Çağında Mimari Zor Kararlar](#17--yapay-zeka-çağında-mimari-zor-kararlar)
18. [Son Sözler](#18--son-sözler)

---

## 1. 🎯 Mimari Kararlar ve Trade-off Analizi

### "Kolay" vs "Zor" Kararlar

```
KOLAY KARAR (Fundamentals kitabı):
  → "REST mi GraphQL mi?" → Gereksinimlerinize göre seçin
  → "Hangi framework?" → Takım deneyimine göre seçin
  → "Hangi DB?" → Veri modeline göre seçin
  → Cevaplar NETTIR. Trade-off'lar BELLIDIR.

ZOR KARAR (Bu kitap!):
  → "Bu monoliti NASIL parçalayacağız?"
  → "Bu iki servis arasındaki veriyi NASIL paylaştıracağız?"
  → "Bu iş akışını ORKESTRASYON mu KOREOGRAFI mi ile yönetecağiz?"
  → "Bu servisi bölmeli miyiz yoksa birleştirmeli miyiz?"
  → Cevaplar NET DEĞİLDİR. "Duruma bağlı" → AMA NEYE BAĞLI?!

Bu kitap "NEYE BAĞLI" sorusunu cevaplamak için
sistematik bir FRAMEWORK sunar. 🧭
```

### İlk Kanun: HER ŞEY BİR TRADE-OFF'TUR!

```
╔════════════════════════════════════════════════════════════╗
║  "Yazılım mimarisinde her şey bir trade-off'tur."        ║
║                                                            ║
║  "Eğer bir mimar 'trade-off değil' dediği bir şey        ║
║   bulduğunu düşünüyorsa, muhtemelen trade-off'u           ║
║   henüz KEŞFETMEMİŞTİR."                                 ║
║                                                            ║
║  — Neal Ford & Mark Richards, Birinci Yasa                ║
╚════════════════════════════════════════════════════════════╝

Her seçimin BEDELI vardır:

  Microservices SEÇTİN:
    ✅ Bağımsız deployment, bağımsız ölçekleme, teknoloji çeşitliliği
    ❌ Ağ karmaşıklığı, dağıtık transaction, operasyonel maliyet

  Monolith SEÇTİN:
    ✅ Basitlik, tek transaction, kolay debug, düşük operasyonel maliyet
    ❌ Ölçekleme sınırları, deployment bağımlılığı, takım çatışması

  → "HANGİSİ DAHA İYI?" → YANLIŞ SORU!
  → "BENİM bağlamımda hangi trade-off'lar KABUL EDİLEBİLİR?" → DOĞRU SORU! ✅
```

### İkinci Kanun: Neden > Nasıl

```
╔════════════════════════════════════════════════════════════╗
║  "NEDEN, NASIL'dan daha önemlidir."                       ║
║                                                            ║
║  Mimari kararın KENDİSİ değil,                            ║
║  kararın ARKASINDAKI GEREKÇE önemlidir.                   ║
║                                                            ║
║  — İkinci Yasa                                             ║
╚════════════════════════════════════════════════════════════╝

❌ "Microservices kullanıyoruz."
✅ "Microservices kullanıyoruz ÇÜNKÜ:
    → 6 takımımız bağımsız deploy etmek istiyor
    → Sipariş servisi Black Friday'de 100x ölçeklenmeli
    → Ödeme servisi PCI uyumlu ayrı ortamda çalışmalı
    → BU trade-off'ları kabul ediyoruz:
      → Operasyonel maliyet artacak → SRE ekibi kurulacak
      → Dağıtık tracing gerekecek → Jaeger kurulacak"

NEDEN yazılmazsa:
  → 2 yıl sonra yeni gelen mühendis:
    "Neden microservices kullanıyoruz? Monolith daha basit olmaz mıydı?"
  → Kimse hatırlamıyor → YENİDEN tartışma → ZAMAN KAYBI!
  → ADR (Architecture Decision Record) ile BELGELE! 📝
```

---

## 2. 🔍 Modülerliği Keşfetmek

### Modülerlik Neden Önemli?

```
Monolitten microservices'e geçmeden ÖNCE:
"Mevcut monolitte modülerlik VAR MI?"

MONOLITH TÜRLERİ:

1. İYI MONOLITH (Modüler) ✅
   ┌──────────────────────────────────┐
   │           Monolith               │
   │  ┌──────┐ ┌──────┐ ┌──────┐    │
   │  │ Mod A│ │ Mod B│ │ Mod C│    │
   │  │      │ │      │ │      │    │
   │  └──┬───┘ └──┬───┘ └──┬───┘    │
   │     │ API    │ API    │ API    │
   │  ┌──▼───┐ ┌──▼───┐ ┌──▼───┐    │
   │  │ DB-A │ │ DB-B │ │ DB-C │    │
   │  └──────┘ └──────┘ └──────┘    │
   └──────────────────────────────────┘
   → Modüller arasında NET sınırlar
   → Her modülün kendi alanı → microservice'e geçiş KOLAY

2. KÖTÜ MONOLITH (Big Ball of Mud) ❌
   ┌──────────────────────────────────┐
   │     BIG BALL OF MUD 🧶          │
   │                                  │
   │  HER ŞEY ────── HER ŞEYE ───→  │
   │    ←──── BAĞIMLI ────→          │
   │                                  │
   │  "Bir yere dokunsan her yer     │
   │   KIRILIR!" 💀                  │
   └──────────────────────────────────┘
   → Sınır yok, bağımlılık çorbası
   → Microservice'e bölmek İMKANSIZA YAKIN
   → Önce modülerleştir, SONRA böl!
```

### Bağımlılık Analizi (Afferent & Efferent Coupling)

```
COUPLING (Bağımlılık) türlerini ölçmek:

AFFERENT COUPLING (Ca) = Gelen bağımlılık
  → "Kaç modül BENİ kullanıyor?"
  → Ca yüksek → BEN değişirsem ÇOK modül ETKİLENİR!
  → "Sorumluluğum büyük!" 😰

EFFERENT COUPLING (Ce) = Giden bağımlılık
  → "Ben kaç modülü KULLANIYORUM?"
  → Ce yüksek → BEN çok şeye BAĞIMLIYIM → kırılgan!
  → "Çok bağımlıyım!" 😰

INSTABILITY = Ce / (Ca + Ce)
  → 0 = tamamen kararlı (herkes bana bağımlı, ben kimseye değil)
  → 1 = tamamen kararsız (ben herkese bağımlıyım)

ABSTRACTION = soyut eleman sayısı / toplam eleman sayısı
  → 0 = tamamen somut (interface yok)
  → 1 = tamamen soyut (hep interface)

MAIN SEQUENCE DİYAGRAMI:
  → (0,1) ve (1,0) arasındaki çizgi = ideal
  → (0,0) = "Zone of Pain" 💀 → somut + kararlı = DEĞİŞTİRMESİ ZOR!
  → (1,1) = "Zone of Uselessness" 🗑️ → soyut + kararsız = KİMSE KULLANMIYOR!
```

### Bağımlılık Ölçüm Araçları

```javascript
// JavaScript/Node.js projelerde bağımlılık analizi

// 1. dependency-cruiser — modüller arası bağımlılık grafiği
// npm install --save-dev dependency-cruiser
// npx depcruise --output-type dot src | dot -T svg > deps.svg

// 2. Madge — circular dependency tespiti
// npm install --save-dev madge
// npx madge --circular src/

// Circular dependency BULURSAN → modülerlik BOZUK!
// A → B → C → A 🔄 → sınır YOK demek!

// 3. Kendi metrik hesabın:
function analyzeModule(moduleName, allImports) {
  const afferent = allImports.filter(i => i.target === moduleName).length;
  const efferent = allImports.filter(i => i.source === moduleName).length;
  const instability = efferent / (afferent + efferent);
  
  return {
    module: moduleName,
    Ca: afferent,       // Beni kaç modül kullanıyor?
    Ce: efferent,       // Ben kaç modül kullanıyorum?
    instability,        // 0=kararlı, 1=kararsız
    risk: instability > 0.7 ? '⚠️ YÜKSEK' : '✅ NORMAL'
  };
}
```

---

## 3. ✂️ Mimari Ayrışma (Decomposition)

### Ne Zaman Parçalamalı?

```
MONOLİTİ PARÇALAMA KARARI:

"Microservices'e geçelim mi?" diye sormadan ÖNCE:
→ "NEDEN parçalamak istiyoruz?"

GEÇERLİ NEDENLER ✅:
  1. BAĞIMSIZ DEPLOYMENT gerekiyor
     → "Sipariş takımı deploy yapınca ödeme takımı da deploy etmek ZORUNDA!"
     → Bağımsızlık istiyoruz → AYIR ✅

  2. FARKLI ÖLÇEKLEME gerekiyor
     → "Arama servisi 10x ölçeklenmeli ama sipariş servisi 1x yeterli"
     → Bağımsız ölçekleme → AYIR ✅

  3. FARKLI GÜVENİLİRLİK GEREKSİNİMİ
     → "Ödeme %99.99 uptime olmalı, blog %99 yeterli"
     → Farklı SLA → AYIR ✅

  4. FARKLI TEKNOLOJİ GEREKSİNİMİ
     → "ML modeli Python'da, API Node.js'te"
     → Farklı tech stack → AYIR ✅

  5. TAKIM BAĞIMSIZLIĞI
     → "6 takım aynı kodu değiştirmeye çalışıyor → merge conflict kabusu!"
     → Conway's Law → AYIR ✅

GEÇERSİZ NEDENLER ❌:
  → "Herkes yapıyor, trend!" → Cargo cult! ❌
  → "CV'mde microservices yazacak!" → Hayır! ❌
  → "Monolith kötüdür!" → Monolith kötü DEĞİLDİR! ❌
  → "Daha hızlı olur!" → Ağ hop'ları = DAHA YAVAŞ olabilir! ❌
```

### Ayrışma Sürücüleri (Decomposition Drivers)

```
Kitap, ayrışma kararını veren 7 SÜRÜCü tanımlar:

┌────────────────────────────────────────────────────────────────┐
│                    AYRIŞMA SÜRÜCÜLERİ                         │
├──────────────────────┬─────────────────────────────────────────┤
│ 1. Hız (Agility)     │ Deployment, değişiklik hızı             │
│ 2. Performans        │ Gecikme, throughput gereksinimleri       │
│ 3. Ölçeklenebilirlik │ Elastik veya hedefli ölçekleme         │
│ 4. Hata Toleransı    │ Bir servisin çökmesi diğerini etkiler mi│
│ 5. Güvenlik          │ Farklı güvenlik gereksinimleri          │
│ 6. Genişletilebilirlik│ Yeni özellik ekleme kolaylığı          │
│ 7. Takım Yapısı      │ Conway's Law, takım bağımsızlığı       │
└──────────────────────┴─────────────────────────────────────────┘

HER SÜRÜCÜyü puan ver (1-5):

                     Monolith  Microservice
  Hız                  2          5
  Performans           4          3 (ağ hop'ları!)
  Ölçeklenebilirlik    2          5
  Hata Toleransı       2          4
  Güvenlik             3          4
  Genişletilebilirlik   3          4
  Kolaylık             5          2 (karmaşıklık!)
  ───────────────────────────────────
  TOPLAM               21         27

  → Sayılar yakınsa → MONOLİTTE KAL!
  → Belirli sürücüler çok fark ediyorsa → O sürücüye göre karar ver!
  → "Ölçeklenebilirlik 2 vs 5" → bu SENİN İÇİN kritikse → microservice!
```

---

## 4. 🧱 Bileşen Tabanlı Ayrışma

### Bileşen Nedir?

```
BİLEŞEN = Dağıtılabilir en küçük mimari birim

Monolit'teki BİLEŞEN ≈ Modül/Paket/Namespace
Microservices'teki BİLEŞEN ≈ Bir servis

AYRIŞMA YAKLAŞIMLARI:

1. TEKNİK KATMAN AYRIŞMASI (YANLIŞ!) ❌
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │Controller│ │ Service  │ │Repository│
   │ Layer    │ │ Layer    │ │ Layer    │
   └──────────┘ └──────────┘ └──────────┘
   → controllers/, services/, repositories/ → TEKNİK bölme!
   → "Sipariş özelliği ekle" → 3 KATMANI değiştir! 😤
   → Değişiklik YAYILIYOR → kötü kohesyon!

2. DOMAIN AYRIŞMASI (DOĞRU!) ✅
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │ Sipariş  │ │ Ödeme    │ │ Kargo    │
   │ Modülü   │ │ Modülü   │ │ Modülü   │
   │          │ │          │ │          │
   │ ctrl     │ │ ctrl     │ │ ctrl     │
   │ service  │ │ service  │ │ service  │
   │ repo     │ │ repo     │ │ repo     │
   └──────────┘ └──────────┘ └──────────┘
   → HER modül kendi controller, service, repo'suna sahip
   → "Sipariş özelliği ekle" → SADECE sipariş modülüne dokun! ✅
   → Yüksek kohesyon, düşük coupling!
   → DDD'nin Bounded Context'i ile BİREBİR örtüşür!
```

### Bileşen Belirleme Süreci

```
ADIM 1: AKTÖR/AKSİYON HARİTALAMASI
  ─────────────────────────────────
  → "Sistemde KİM NE YAPIYOR?"

  Aktör: Müşteri
    → Ürün ara, sepete ekle, sipariş ver, ödeme yap, takip et
  Aktör: Satıcı
    → Ürün ekle, fiyat güncelle, siparişleri gör, kargo gönder
  Aktör: Admin
    → Kullanıcı yönet, rapor al, sistem ayarları

  → Her aktör/aksiyon grubu = potansiyel BİLEŞEN!

ADIM 2: İŞ AKIŞI ANALİZİ (Workflow)
  ─────────────────────────────────
  → "Sipariş verme" akışı:
    Sepet → Ödeme → Stok kontrolü → Kargo → Bildirim
  → Her adım hangi BİLEŞENE ait?
  → Bileşenler arası akış = entegrasyon noktaları!

ADIM 3: VERİ SAHİPLİĞİ ANALİZİ
  ─────────────────────────────────
  → "Bu veri KİME ait?"
  → Sipariş verisi → Sipariş Bileşeni
  → Ürün verisi → Ürün Kataloğu Bileşeni
  → Kullanıcı verisi → Kullanıcı Bileşeni
  → Aynı tabloya İKİ bileşen yazıyorsa → SİNYAL! → Veri ayrışması lazım!

ADIM 4: BİLEŞEN GRANÜLERLİĞİ
  ─────────────────────────────────
  Çok büyük bileşen → dağıtık monolith riski
  Çok küçük bileşen → çok fazla ağ iletişimi, karmaşıklık

  DENGE:
  → "Bu bileşen TEK bir takım tarafından yönetilebilir mi?" → EVET → OK ✅
  → "Bu bileşen BİRDEN FAZLA iş alanını kapsıyor mu?" → EVET → BÖL! ✂️
```

---

## 5. 🍴 Taktiksel Forking

### Alternatif Ayrışma Stratejisi

```
KLASİK YAKLAŞIM: Monolitten parça parça servis ÇIKAR (Strangler Fig)
  → Tek tek servisleri ayır, eski kodu sil
  → ZAMAN ALICI ama düşük riskli

TAKTİKSEL FORKING: Monolitin TAMAMI'nı KOPYALA, gereksiz kısmını SİL!
  → Monoliti kopyala → her kopya gereksiz modülleri SİLER
  → HIZLI ama disiplin gerektirir

GÖRSEL:

  Klasik (Strangler Fig):
  ┌─────────────────┐        ┌──────┐ ┌──────┐ ┌──────┐
  │   MONOLITH      │  ──→   │ Svc1 │ │ Svc2 │ │ Old  │
  │ [A][B][C][D]    │        │ [A]  │ │ [B]  │ │[C][D]│
  └─────────────────┘        └──────┘ └──────┘ └──────┘
  → Yavaş ama güvenli. A çıkar, B çıkar, C-D kalır...

  Taktiksel Forking:
  ┌─────────────────┐        ┌──────┐ ┌──────┐ ┌──────┐
  │   MONOLITH      │  ──→   │Fork1 │ │Fork2 │ │Fork3 │
  │ [A][B][C][D]    │        │ [A]  │ │ [B]  │ │[C][D]│
  └─────────────────┘        │ ---  │ │ ---  │ │ ---  │
       KOPYALA ×3             │B,C,D│ │A,C,D│ │ A,B │
                              │ SİL!│ │ SİL!│ │ SİL!│
                              └──────┘ └──────┘ └──────┘
  → HIZLI ama çok fazla "sil" operasyonu!
```

### Ne Zaman Taktiksel Forking?

```
KULLAN ✅:
  → Monolith ÇOK KARIŞIK → Strangler Fig çok zor
  → Modüller arasında NET sınır YOK (big ball of mud)
  → Hızlı sonuç gerekiyor
  → Monolith kodu ZATen çalışıyor (kararlı)

KULLANMA ❌:
  → Monolith zaten İYI modülerleştirilmiş → Strangler Fig daha kolay
  → Veritabanı PAYLAŞIMI çözülmemiş → fork'lamak DB sorununu çözmez!
  → Takımlar kopyalanmış kodu yönetecek DİSİPLİNE sahip değil

DİKKAT:
  → Fork sonrası HER kopya kendi GELİŞİMİNE devam eder
  → Aynı bug'ı 3 yerde düzeltmek gerekebilir (kısa vadede!)
  → Uzun vadede: her fork AYRI servise dönüşür → bağımsız evrilir ✅
```

---

## 6. 💾 Veriyi Ayrıştırma

### Kitabın EN ZOR Bölümü!

```
"Servisleri ayırmak KOLAYDIR.
 VERİYİ ayırmak EN ZOR KISIMDIR!" 🔥

Building Microservices'te de vardı, burada ÇOK DAHA DERİNE iniyoruz.

SORUN:
  Monolith'te tek DB → tüm tablolar birbirine JOIN yapıyor
  Servisleri ayırdığında → aynı DB'yi paylaşmaya DEVAM edersen:
  → "Distributed Monolith" → en kötü dünya! 💀
  → Bağımsız deployment YOK (DB schema değişikliği herkesi etkiler)
  → Bağımsız ölçekleme YOK (DB darboğaz)

  HEDEF: Her servisin KENDİ VERİTABANI olmalı (Database per Service)
```

### Veri Ayrışma Adımları

```
ADIM 1: VERİ SAHİPLİĞİNİ BELİRLE
  ───────────────────────────────
  "Bu tablo KİME ait?"

  orders tablosu → Sipariş Servisi ✅ (açık!)
  products tablosu → Ürün Servisi ✅ (açık!)
  
  AMA:
  order_items tablosu → Sipariş mi? Ürün mü? 🤔
  → order_items → Sipariş Servisi! (her sipariş kendi kalemlerini yönetir)
  → Ama product bilgisi lazım → SORUN!

ADIM 2: ORTAK VERİYİ AYIR
  ───────────────────────────────
  5 veri ilişki paterni:

  1. VERİ SAHİPLİĞİ (Data Ownership)
     → Tablo TEK bir servise ait → normal, sorun yok ✅
     → orders → Sipariş Servisi

  2. ORTAK VERİ (Shared Data)
     → Birden fazla servis AYNI tabloya erişiyor → PROBLEM!
     → country_codes → Sipariş, Kargo, Müşteri hepsi kullanıyor

     ÇÖZÜMLER:
     a) Her servisin kendi kopyası (replika) → eventual consistency
     b) Ortak veri servisi → Country Code Service → hepsi BUNU çağırır
     c) Paylaşılan kütüphane (statik veri ise) → npm paketi olarak dağıt

  3. REFERANS VERİSİ (Foreign Key İlişkisi)
     → order_items.product_id → products.id
     → Servisler ayrıysa → CROSS-DB JOIN yapılamaz!

     ÇÖZÜMLER:
     a) API çağrısı: Sipariş servisi → Ürün servisi API'sini çağır
        → Ek ağ hop'u, gecikme ↑
     b) Veri kopyalama: Sipariş servisi ürün bilgisini KENDİ DB'sinde tut
        → Denormalizasyon, eventual consistency
     c) Materialized View: Veri değişikliğini event ile dinle, view güncelle

  4. PAYLAŞILAN TABLO (Shared Table)
     → Tek tablo, birden fazla servisin alanları var
     → notifications: order_id, shipment_id, payment_id → herkes kullanıyor!

     ÇÖZÜM: Tabloyu BÖL!
     → order_notifications, shipment_notifications, payment_notifications

  5. VERİ İLİŞKİSİ (Aggregate Relationship)
     → Master-detail ilişki → ikisi ayrı servise mi gitmeli?
     → Order → OrderItems → AYNI aggregate → AYNI servis!
     → Order → Payment → FARKLI aggregate → farklı servis OK
```

### Veri Ayrışma Senaryoları

```javascript
// SENARYO: Sipariş servisi ürün bilgisine ihtiyaç duyuyor

// ❌ KÖTÜ: Cross-service JOIN (imkansız!)
// SELECT o.*, p.name, p.price 
// FROM order_service.orders o 
// JOIN product_service.products p ON o.product_id = p.id
// → ÇALIŞMAZ! Farklı DB'ler!

// ✅ ÇÖZÜM 1: API Composition
class OrderDetailService {
  async getOrderWithProducts(orderId) {
    // 1. Kendi DB'nden sipariş bilgileri
    const order = await this.orderRepo.findById(orderId);
    
    // 2. Ürün servisi API'sinden ürün bilgileri
    const productIds = order.items.map(i => i.productId);
    const products = await this.productServiceClient.getByIds(productIds);
    // → Ek ağ çağrısı! Gecikme ↑ ama doğru sınırlar! ✅
    
    // 3. Birleştir
    return {
      ...order,
      items: order.items.map(item => ({
        ...item,
        productName: products[item.productId].name,
        productImage: products[item.productId].imageUrl,
      }))
    };
  }
}

// ✅ ÇÖZÜM 2: Veri Kopyalama (Denormalizasyon)
// Sipariş oluşturulurken ürün bilgisini KOPYALA!
class OrderService {
  async createOrder(memberId, cartItems) {
    const order = new Order(generateId(), memberId);
    
    for (const item of cartItems) {
      // Ürün bilgisini ŞİMDİ al ve kopyala!
      const product = await this.productClient.getById(item.productId);
      
      order.addItem({
        productId: product.id,
        productName: product.name,      // KOPYALANDI!
        unitPrice: product.price,        // KOPYALANDI! (o anki fiyat!)
        quantity: item.quantity,
      });
    }
    
    await this.orderRepo.save(order);
    return order;
    // → Sipariş artık ürün servisine BAĞIMLI DEĞİL okuma için!
    // → AMA ürün adı değişirse ESKI ad kalır → kabul edilebilir mi?
    // → Siparişteki ürün adı = SİPARİŞ ANINDAKİ ad → genellikle OK! ✅
  }
}

// ✅ ÇÖZÜM 3: Event-Driven Senkronizasyon
// Ürün değiştiğinde event yayınla → sipariş servisi DİNLER
class ProductEventHandler {
  async handle(event) {
    if (event.type === 'ProductPriceChanged') {
      // Sipariş servisindeki ürün cache'ini güncelle
      await this.productCache.update(event.productId, {
        price: event.newPrice,
      });
    }
  }
}
// → Eventual consistency! Anlık tutarlılık YOK ama kabul edilebilir.
```

### Veri Ayrışma Karar Ağacı

```
VERİ X birden fazla servis tarafından kullanılıyor:

  X STATİK mi? (ülke kodu, para birimi, vs.)
  ├── EVET → Paylaşılan kütüphane / konfigürasyon ✅
  └── HAYIR → Dinamik veri
      │
      X'i SÜREKLİ mi okumanız gerekiyor?
      ├── NADIREN → API çağrısı (lazım olunca sor) ✅
      └── SIK SIK → Veri kopyalama gerekli
          │
          Tutarlılık NE KADAR kritik?
          ├── ÇOK KRİTİK → Senkron API + Cache ✅
          └── EVENTUAL OK → Event ile senkronizasyon ✅

  "Doğru cevap yok, bağlamına göre seçim yap!" 🎯
```

---

## 7. 📡 Servisler Arası İletişim

### İletişim Stilleri

```
┌──────────────────────────────────────────────────────────────┐
│                İLETİŞİM MATRİSİ                              │
├──────────────┬────────────────────┬───────────────────────────┤
│              │ SENKRON             │ ASENKRON                  │
├──────────────┼────────────────────┼───────────────────────────┤
│ İSTEK-YANIT  │ REST, gRPC         │ Async Request-Reply       │
│ (1:1)        │ "Bekliyorum!"      │ "Yanıtı sonra al"        │
├──────────────┼────────────────────┼───────────────────────────┤
│ OLAY ODAKLI  │ (nadir)            │ Event, Message Queue      │
│ (1:N)        │                    │ "İlgilenen dinlesin!"     │
└──────────────┴────────────────────┴───────────────────────────┘
```

### Senkron vs Asenkron Trade-off'ları

```
SENKRON (REST/gRPC):
  ✅ Basit! İstek yap → yanıt al → devam et
  ✅ Anlık tutarlılık (response = güncel veri)
  ✅ Debug kolay (request → response takip et)
  
  ❌ TEMPORAL COUPLING: Karşı servis ÇALIŞMAK ZORUNDA!
     → Payment servisi çöktüğünde → Order servisi de ÇÖKÜYOR! 💀
  ❌ Gecikme birikiyor: A→B→C→D = 4 ağ hop → toplam gecikme ↑↑
  ❌ Ölçekleme zinciri: A 100x ölçeklenirse → B,C,D de 100x? 😰

ASENKRON (Event/Message Queue):
  ✅ TEMPORAL DECOUPLING: Karşı servis çöktüyse → mesaj KUYRUKTA BEKLEr
     → Payment çöktü → sipariş mesajı kuyrukta → Payment ayağa kalkınca İŞLER!
  ✅ Bağımsız ölçekleme: Producer ve Consumer BAĞIMSIZ
  ✅ Natural buffer: Trafik patlaması → kuyruk absorbe eder

  ❌ Eventual consistency: Anlık tutarlılık YOK → "ödeme yapıldı mı?" → "bekle..."
  ❌ Debug ZOR: Mesaj nereye gitti? Hangi sırayla işlendi?
  ❌ Karmaşıklık: Dead letter queue, retry, idempotency yönetimi
  ❌ Error handling: Mesaj işleme başarısız → ne yapacağız?

KARAR:
  "Kullanıcı HEMEN sonucu görmeli mi?"
  → EVET → Senkron (ödeme sonucu, stok kontrolü)
  → HAYIR → Asenkron (bildirim, log, analitik, e-posta)

  "Karşı servis çökse bile çalışmaya devam etmeli miyim?"
  → EVET → Asenkron (sipariş al → ödemeyi sonra işle)
  → HAYIR → Senkron OK (ama circuit breaker ekle!)
```

### İletişim Granülerliği

```
SERVİS GRANÜLERLİĞİ iletişim MALİYETİNİ belirler:

  KABA GRANÜLERLİK (az, büyük servisler):
  ┌──────────┐  1 çağrı  ┌──────────┐
  │  Order   │──────────→│ Ful.     │
  │  Service │           │ Service  │  → Az ağ çağrısı ✅
  └──────────┘           └──────────┘  → Büyük servisler ❌

  İNCE GRANÜLERLİK (çok, küçük servisler):
  ┌──────────┐  4 çağrı  ┌─────────┐
  │  Order   │──────────→│ Stock   │
  │  Service │──────────→│ Payment │  → Çok ağ çağrısı ❌
  │          │──────────→│ Ship.   │  → Küçük, odaklı servisler ✅
  │          │──────────→│ Notif.  │
  └──────────┘           └─────────┘

  TRADE-OFF:
  → Daha ince bölme = daha fazla ağ iletişimi = daha yüksek gecikme
  → Daha kaba bölme = daha az ağ ama daha büyük deploy birimi

  STAMP COUPLING:
    → Servisler arası paylaşılan veri yapıları (DTO)
    → Çok fazla alan paylaşılıyorsa → servisler ÇOK BAĞIMLI
    → Minimumda tut: sadece İHTİYACIN olan alanları gönder!
```

---

## 8. 🎭 Orkestrasyon vs Koreografi

### İki Koordinasyon Stili

```
İŞ AKIŞI: Sipariş → Ödeme → Stok → Kargo → Bildirim

Bu akışı KİM yönetecek?

1. ORKESTRASYON 🎵 (Orkestra şefi var!)
   ─────────────────────────────────────
   Merkezi bir "orkestratör" tüm adımları YÖNETIR

            ┌──────────────┐
            │ Order        │
            │ Orchestrator │ ← ŞEF! 🎼
            └──────┬───────┘
                   │
         ┌─────────┼──────────┬──────────┐
         ↓         ↓          ↓          ↓
   ┌─────────┐┌────────┐┌────────┐┌────────┐
   │ Payment ││ Stock  ││ Ship.  ││ Notif. │
   └─────────┘└────────┘└────────┘└────────┘

   Orkestratör:
   1. Payment'ı çağır → "Öde!"
   2. Payment başarılı → Stock'u çağır → "Stok düş!"
   3. Stock başarılı → Shipping'i çağır → "Kargo oluştur!"
   4. Shipping başarılı → Notification → "Bildir!"
   5. Herhangi biri başarısız → KOMPANZASYON başlat!

2. KOREGRAFİ 💃 (Şef yok, herkes kendi biliyor!)
   ─────────────────────────────────────────────
   Servisler EVENT dinler ve TEPKİ verir

   Order ──event──→ Payment ──event──→ Stock ──event──→ Ship.
         "Sipariş     │     "Ödeme      │    "Stok      │
          oluşturuldu" │     alındı"     │    düştü"     │
                       │                 │               │
                       └─ event ─→ Notification          │
                                   "Bildir!"             │
                                                         │
                                          └─ event ─→ Notification
                                                      "Bildir!"
   
   Her servis:
   → Kendi ilgilendiği event'i DİNLER
   → İşini yapar
   → Kendi event'ini YAYINLAR
   → Kimseyi YÖNETMEZ! Herkes bağımsız!
```

### Karşılaştırma

```
┌──────────────────┬──────────────────┬────────────────────────┐
│ ÖZELLİK          │ ORKESTRASYON 🎵  │ KOREGRAFİ 💃           │
├──────────────────┼──────────────────┼────────────────────────┤
│ İş akışı görünür │ ✅ EVET          │ ❌ HAYIR (dağınık!)    │
│ lüğü             │ Tek yerde!       │ Loglardan TAKİP et! 😤│
├──────────────────┼──────────────────┼────────────────────────┤
│ Coupling         │ ❌ YÜKSEK        │ ✅ DÜŞÜK               │
│                  │ Orkestratör HE-  │ Servisler birbirini    │
│                  │ PİSİNE bağımlı   │ BİLMİYOR bile!        │
├──────────────────┼──────────────────┼────────────────────────┤
│ Hata yönetimi    │ ✅ KOLAY         │ ❌ ZOR                 │
│                  │ Orkestratör      │ Her servis kendi       │
│                  │ hepsini YÖNETİR │ hatasını yönetMELİ     │
├──────────────────┼──────────────────┼────────────────────────┤
│ Ölçeklenebilirlik│ ❌ SINIRLI       │ ✅ YÜKSEK              │
│                  │ Orkestratör      │ Her servis bağımsız    │
│                  │ darboğaz OLUR!   │ ölçeklenir             │
├──────────────────┼──────────────────┼────────────────────────┤
│ Yeni adım ekleme │ ✅ KOLAY         │ ❌ ZOR                 │
│                  │ Orkestratöre     │ Hangi servis hangi     │
│                  │ yeni adım ekle   │ event'i dinleMELİ? 🤔│
├──────────────────┼──────────────────┼────────────────────────┤
│ Tek Nokta Arızası│ ❌ EVET          │ ✅ HAYIR               │
│ (SPOF)           │ Orkestratör çö-  │ Merkezi bileşen       │
│                  │ kerse HEPSİ çöker│ YOK!                  │
└──────────────────┴──────────────────┴────────────────────────┘
```

### Ne Zaman Hangisi?

```
ORKESTRASYON SEÇ:
  → İş akışı KARMAŞIK (10+ adım, koşullu dallar)
  → Hata yönetimi KRİTİK (kompanzasyon, retry, timeout)
  → İş akışı GÖRÜNÜR olmalı (audit, compliance)
  → Yeni takım üyeleri akışı ANLAMALI

KOREOGRAFI SEÇ:
  → İş akışı BASİT (3-5 adım)
  → Servisler çok BAĞIMSIZ olmalı
  → Yüksek ÖLÇEKLENEBİLİRLİK gerekli
  → Domainler çok FARKLI (cross-domain event'ler)

HİBRİT (gerçek dünya!) 🌍:
  → Bir bounded context İÇİNDE: Orkestrasyon
  → Context'ler ARASINDA: Koreografi

  ┌────── Sipariş Context ───────┐   Event   ┌──── Kargo Context ────┐
  │ [Orchestrator]               │ ────────→ │ [Orchestrator]        │
  │   ↓       ↓        ↓        │           │   ↓      ↓            │
  │ Validate  Stock   Payment   │           │ Route  Dispatch       │
  └──────────────────────────────┘           └───────────────────────┘

  → Context İÇİ→ orkestrasyon (akış net, hata yönetimi kolay)
  → Context ARASI → event (loosely coupled, bağımsız deploy)
  → EN İYİ İKİ DÜNYANIN BİRLEŞİMİ! ✅
```

---

## 9. 🔄 Transaksiyonel Saga'lar

### Dağıtık Transaction Problemi

```
MONOLİTTE:
  BEGIN TRANSACTION
    INSERT INTO orders ...
    UPDATE inventory SET stock = stock - 1
    INSERT INTO payments ...
  COMMIT
  → HEPSİ BAŞARILI veya HEPSİ GERİ AL! → ACID ✅

MİCROSERVİCES'TE:
  Order Service → Payment Service → Stock Service
  → FARKLI veritabanları! → Tek transaction İMKANSIZ!
  → Payment başarılı oldu AMA Stock update başarısız → NE YAPACAĞIZ? 😱
  → ACID yok → SAGA lazım!
```

### Saga Pattern

```
SAGA = Bir dizi LOCAL transaction + KOMPANZASYON işlemleri

Her adım:
  → Başarılı → sonraki adıma geç
  → Başarısız → önceki adımları GERİ AL (compensate)

SIPARIŞ SAGA'SI:

  İLERİ YÖN (Happy Path):
  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
  │ Create  │───→│ Reserve │───→│ Process │───→│ Confirm │
  │ Order   │    │ Stock   │    │ Payment │    │ Shipping│
  └─────────┘    └─────────┘    └─────────┘    └─────────┘

  GERİ YÖN (Failure Path — ödeme başarısız!):
  ┌─────────┐    ┌─────────┐    ┌─────────┐
  │ Cancel  │←───│ Release │←───│ Payment │ ← BAŞARISIZ!
  │ Order   │    │ Stock   │    │ FAILED  │
  └─────────┘    └─────────┘    └─────────┘

  Her adımın KOMPANZASYON'u var:
  → Create Order → kompanzasyon: Cancel Order
  → Reserve Stock → kompanzasyon: Release Stock
  → Process Payment → kompanzasyon: Refund Payment
  → Confirm Shipping → kompanzasyon: Cancel Shipment
```

```javascript
// Saga Orkestratörü (basitleştirilmiş)
class OrderSaga {
  #steps = [];
  #completedSteps = [];

  constructor() {
    this.#steps = [
      {
        name: 'createOrder',
        execute: (ctx) => this.createOrder(ctx),
        compensate: (ctx) => this.cancelOrder(ctx),
      },
      {
        name: 'reserveStock',
        execute: (ctx) => this.reserveStock(ctx),
        compensate: (ctx) => this.releaseStock(ctx),
      },
      {
        name: 'processPayment',
        execute: (ctx) => this.processPayment(ctx),
        compensate: (ctx) => this.refundPayment(ctx),
      },
      {
        name: 'confirmShipping',
        execute: (ctx) => this.confirmShipping(ctx),
        compensate: (ctx) => this.cancelShipment(ctx),
      },
    ];
  }

  async run(context) {
    for (const step of this.#steps) {
      try {
        console.log(`▶ ${step.name} çalıştırılıyor...`);
        await step.execute(context);
        this.#completedSteps.push(step);
        console.log(`✅ ${step.name} başarılı!`);
      } catch (error) {
        console.log(`❌ ${step.name} BAŞARISIZ: ${error.message}`);
        await this.#compensate(context);
        throw new SagaFailedError(step.name, error);
      }
    }
    console.log('🎉 Saga tamamlandı!');
  }

  async #compensate(context) {
    console.log('🔄 Kompanzasyon başlatılıyor...');
    // TERS sırada geri al! (son başarılı olandan başa doğru)
    for (const step of this.#completedSteps.reverse()) {
      try {
        console.log(`↩ ${step.name} geri alınıyor...`);
        await step.compensate(context);
        console.log(`✅ ${step.name} geri alındı.`);
      } catch (compError) {
        // Kompanzasyon da BAŞARISIZ olduysa → ALARM! Manuel müdahale!
        console.error(`🚨 ${step.name} kompanzasyonu BAŞARISIZ!`, compError);
        // Dead letter queue'ya at, alert gönder!
      }
    }
  }

  // Adım implementasyonları...
  async createOrder(ctx) { /* Order servisi çağır */ }
  async cancelOrder(ctx) { /* Order iptal */ }
  async reserveStock(ctx) { /* Stock servisi çağır */ }
  async releaseStock(ctx) { /* Stok serbest bırak */ }
  async processPayment(ctx) { /* Payment servisi çağır */ }
  async refundPayment(ctx) { /* Ödeme iade */ }
  async confirmShipping(ctx) { /* Shipping servisi çağır */ }
  async cancelShipment(ctx) { /* Kargo iptal */ }
}
```

### Saga Kompanzasyon Zorlukları

```
KOMPANZAsyon = "geri al" ama her zaman MÜMKÜN DEĞİL!

SORUN 1: E-posta gönderildi → GERİ ALAMAZSIN!
  → "Siparişiniz onaylandı" e-postası gitti
  → Sonraki adım başarısız oldu
  → E-postayı geri çekemezsin!
  → ÇÖZÜM: "Siparişiniz iptal edildi" ikinci e-posta gönder

SORUN 2: Fiziksel eylem yapıldı
  → Depodan ürün toplanmaya başlandı
  → Ödeme başarısız oldu
  → Fiziksel eylemi geri almak PAHALIYA patlayabilir
  → ÇÖZÜM: Fiziksel eylemi EN SON yap!

SORUN 3: Zaman penceresi
  → Stok 5 dakika önce reserve edildi
  → Bu 5 dakika boyunca başka müşteri stok bulamadı
  → Şimdi geri alıyoruz → 5 dakika "hayalet stok"
  → ÇÖZÜM: Timeout + reservation pattern

SEMANTIC LOCK:
  → Aggregate'i "PROCESSING" durumuna al
  → Saga devam ederken başka işlem YAPAMASIN
  → Saga bitince (başarı veya kompanzasyon) → kilidi AÇ
```

---

## 10. 📜 Kontrat Yönetimi

### Servisler Arası Kontratlar

```
SERVİS İLETIŞIMINDE "KONTRAT" = API şeması
→ Siparış servisi, ödeme servisine NE gönderiyor?
→ Ödeme servisi NE döndürüyor?
→ Bu şemalar DEĞİŞİRSE ne olur?

SORUN: KATI KONTRAT (Tight)
  → Order → Payment'a: { orderId, amount, currency, date, items, memberId }
  → Payment tüm alanlara BAĞIMLI
  → Bir alan eklenirse/değişirse → Payment KIRILIR!

ÇÖZÜM: ESNEK KONTRAT (Loose)
  → "Robustness Principle" / Postel's Law:
    "Gönderdiğinde KATIL, aldığında ESNEK ol!"
  → Payment: "Bana orderId ve amount yeter, gerisini YOKSAY!"
  → Order'a yeni alan eklendi → Payment ETKİLENMEZ! ✅
```

### Kontrat Türleri

```
1. STRICT KONTRAT (Katı) 📏
   → Tüm alanlar zorunlu, tip kontrolü sıkı
   → (gRPC/Protobuf, GraphQL strict mode)
   → Avantaj: Derleme zamanında hata yakalama
   → Dezavantaj: Her değişiklik koordinasyon gerektirir

2. LOOSE KONTRAT (Esnek) 🤸
   → Bilinmeyen alanları yoksay, eksik alanları tolere et
   → (JSON + tolerant reader pattern)
   → Avantaj: Bağımsız evrim
   → Dezavantaj: Runtime hataları, belirsiz şema

3. CONTRACT TESTING (En iyi yaklaşım!) ✅
   → Consumer-Driven Contract:
   → TÜKETİCİ (consumer) ne beklediğini TANIMLAR
   → ÜRETİCİ (provider) bu beklentiyi karşılar mı kontrol eder

   Sipariş servisi (consumer):
   "Ben ödeme servisinden { transactionId, status } bekliyorum"
   
   Ödeme servisi (provider):
   "Bende { transactionId, status, amount, date } var → consumer'ın ihtiyacını KARŞILIYORUM ✅"

   → Consumer'ın beklemediği alanlar (amount, date) → sorun DEĞİL!
   → Consumer'ın beklediği alan (status) silinirse → TEST BAŞARISIZ! → DEĞİŞİKLİK ENGELLENIR!
```

---

## 11. 📊 Analitik Veri Yönetimi

### Operasyonel vs Analitik Veri

```
MİCROSERVİCES'te her servisin kendi DB'si var → HARIKA!
AMA: "Tüm siparişlerin toplam geliri nedir?" → SORUN!

  → Sipariş servisi → kendi siparişlerini bilir
  → Ödeme servisi → kendi ödemelerini bilir
  → Kargo servisi → kendi kargolarını bilir
  → "CROSS-SERVICE rapor" nasıl yapılacak? 🤔

ÇÖZÜMLER:

1. API COMPOSITION
   → Raporlama servisi → her servisi ÇAĞIR → birleştir
   → ❌ N+1 sorgu problemi, yavaş, servis bağımlılığı

2. DATA LAKE / WAREHOUSE
   → Her servis veriyi merkezi depoya AKTAR
   → Snowflake, BigQuery, Redshift
   → ✅ Büyük ölçekli analitik, ML, raporlama
   → ❌ ETL pipeline yönetimi, gecikme

3. EVENT-DRIVEN DATA SYNC
   → Her servis değişiklik event'i yayınlar
   → Analitik servisi TÜM event'leri dinler → kendi view'ını oluşturur
   → ✅ Real-time analytics
   → ❌ Event schema yönetimi, eventual consistency
```

---

## 12. 🕸️ Veri Mesh

### Zhamak Dehghani'nin Vizyonu

```
GELENeksel: Merkezi veri ekibi TÜM veriyi yönetir
  → Veri mühendisleri: "Bize veriyi verin, biz yönetelim"
  → Domain ekipleri: "Verimi istiyor ama 3 ay bekliyorum!"
  → Darboğaz: Merkezi veri ekibi! (Brent problemi tekrar! 🔥)

VERİ MESH: Veri sahipliğini DOMAIN EKİPLERİNE ver!
  → "Sipariş verisi → Sipariş ekibinin sorumluluğu!"
  → "Ödeme verisi → Ödeme ekibinin sorumluluğu!"
  → Her ekip kendi verisini "ürün" olarak SUNAR

4 PRENSİP:

1. DOMAIN ODAKLI VERİ SAHIPLİĞİ 🏠
   → Her domain kendi verisini OWN eder
   → Veri ÜRÜNÜ olarak sunar (API, event, dataset)
   → "Sipariş ekibi sipariş analitiğinden SORUMLUDUR"

2. VERİ ÜRÜN OLARAK (Data as a Product) 📦
   → Veri kaliteli, keşfedilebilir, güvenilir olmalı
   → SLA'sı olmalı (güncellik, doğruluk, erişilebilirlik)
   → Dokümantasyonu olmalı (şema, anlam, kullanım)
   → "Veri sağlayıcı = ürün sahibi!"

3. SELF-SERVE VERİ PLATFORMU 🛠️
   → Ekiplerin kendi veri ürününü oluşturabilmesi için altyapı
   → "click-button" ile veri pipeline oluştur
   → Merkezi platform: tooling, infra, governance
   → Domain ekipleri: veri ürünü oluşturma ve yönetme

4. FEDERATED GOVERNANCE 🏛️
   → Merkezi kurallar + domain özerkliği
   → Global: Veri standardları, güvenlik politikaları, meta-data
   → Lokal: Domain'e özgü şema, iş kuralları, güncelleme sıklığı
```

---

## 13. ⚖️ Trade-off Teknikleri

### MECE (Mutually Exclusive, Collectively Exhaustive)

```
Karar verirken TÜM alternatifleri analiz et:
→ Seçenekler BİRBİRİNI DIŞLAMALI (mutually exclusive)
→ Seçenekler HER ŞEYİ KAPSAMALI (collectively exhaustive)

Örnek: Servisler arası iletişim

  SEÇENEKLER:
  ┌──────────┬────────────┬────────────┬────────────┐
  │          │ Senkron    │ Asenkron   │ Hibrit     │
  │          │ (REST)     │ (Event)    │            │
  ├──────────┼────────────┼────────────┼────────────┤
  │ Basitlik │ ✅ yüksek  │ ❌ düşük   │ 🟡 orta   │
  │ Coupling │ ❌ yüksek  │ ✅ düşük   │ 🟡 orta   │
  │ Perf.    │ 🟡 orta   │ ✅ yüksek  │ ✅ yüksek  │
  │ Hata tol.│ ❌ düşük   │ ✅ yüksek  │ ✅ yüksek  │
  │ Debug    │ ✅ kolay   │ ❌ zor     │ 🟡 orta   │
  │ Tutarlık │ ✅ strong  │ ❌ eventual│ 🟡 karma  │
  └──────────┴────────────┴────────────┴────────────┘

  HER seçenek listelenmiş → collectivelly exhaustive ✅
  Seçenekler çakışmıyor → mutually exclusive ✅
  Trade-off'lar GÖRÜNÜR → bilinçli karar ver! ✅
```

### Qualitative vs Quantitative Analiz

```
QUALITATIF (Niteliksel):
  → "Bu yaklaşım DAHA BASİT" → basitliği nasıl ölçüyorsun?
  → "Güvenlik DAHA İYİ" → ne kadar daha iyi?
  → Sübjektif, ama hızlı karar için yeterli

QUANTITATIF (Niceliksel):
  → "Latency p99: 50ms vs 200ms" → NET!
  → "Deployment süresi: 5dk vs 45dk" → NET!
  → Objektif, ama ölçüm ZAMANI ve ÇABASI gerekli

PRATIKTE:
  → İlk QUALITATIF analiz yap (hızlı eleme)
  → Kalan 2-3 seçenek arasında QUANTITATIF analiz yap (PoC/prototyp)
  → "Bunu denemeden BİLEMEMİZ" → PROTOTYPE YAP!

FITNESS FUNCTION:
  → Mimari kararı OTOMATİK DENETLEyen ölçüm
  → "Servisler arası senkron çağrı sayısı < 3 olmalı" → CI'da kontrol et!
  → İhlal → BUILD FAILS → FARKINDA ol! 🚨
```

---

## 14. 📝 Mimari Karar Kayıtları (ADR)

### Kararları BELGELE!

```
"NEDEN bu mimariyi seçtik?"
→ 6 ay sonra kimse hatırlamıyorsa → karar TEKRAR tartışılır → ZAMAN KAYBI!
→ ÇÖZÜM: ADR (Architecture Decision Record)

HER önemli mimari karar bir ADR ile BELGELENMELIDIR!
```

### ADR Formatı

```markdown
# ADR-001: Sipariş ve Ödeme Servislerinin Ayrılması

## Durum
Kabul Edildi (2024-03-15)

## Bağlam
Monolith uygulamada sipariş ve ödeme modülleri aynı
deployment biriminde. Ödeme ekibi PCI compliance için
ayrı ortam istiyor. Sipariş ekibi günde 3 deploy yapmak
istiyor ama her deployment ödeme modülünü de içeriyor.

## Karar
Sipariş ve ödeme modülleri AYRI microservice'ler olacak.
İletişim: Senkron REST (ödeme sonucu anında gerekli).
Fallback: Circuit breaker + ödeme kuyruğu.

## Alternatifler Değerlendirildi
1. Monolitte kalma → ❌ PCI compliance karşılanamıyor
2. Sadece DB ayırma → ❌ Bağımsız deploy sağlanamıyor
3. Event-driven asenkron → ❌ Kullanıcı ödeme sonucunu
   hemen görememeli → UX kötüleşir

## Sonuçlar
- ✅ Bağımsız deployment
- ✅ PCI compliance ayrı ortam
- ❌ Ağ gecikme artışı (+30ms)
- ❌ Dağıtık transaction yönetimi (Saga gerekecek)
- ❌ Operasyonel karmaşıklık artışı

## İlgili ADR'ler
- ADR-002: Saga pattern seçimi (orkestrasyon)
- ADR-003: Circuit breaker konfigürasyonu
```

### ADR İpuçları

```
NE ZAMAN ADR YAZ:
  → Mimari stil kararı (monolith vs microservice)
  → Teknoloji seçimi (PostgreSQL vs MongoDB)
  → İletişim stili (sync vs async)
  → Veri ayrışma kararı
  → Güvenlik stratejisi
  → DEĞİŞTİRMESİ PAHALI olan her karar!

NE ZAMAN ADR YAZMA:
  → Library seçimi (lodash vs ramda → küçük karar)
  → Kod stili (tabs vs spaces → linter'a bırak!)
  → Günlük teknik kararlar

FORMAT:
  → docs/adr/ klasöründe Markdown dosyaları
  → ADR-001-siparis-odeme-ayirma.md
  → Git'te VERSION CONTROLLED → değişiklik geçmişi otomatik!
  → "Bu ADR artık geçersiz" → Durum: Superseded by ADR-015
```

---

## 15. 🌍 Gerçek Hayata Uyarlama

### Aşamalı Dönüşüm Stratejisi

```
GÜN 1: MONOLİTTEYSEN
  ─────────────────────
  1. Modülerliği ÖLÇE (bağımlılık analizi)
  2. Bounded Context'leri BELIRLE (DDD!)
  3. Modüller ARASI sınırları GÜÇLENDIR

GÜN 30: MODÜLER MONOLİT
  ──────────────────────
  4. Her modül kendi verisini YÖNETsin
  5. Modüller arası iletişim → in-process event bus
  6. Modül sınırlarını TEST ET (architectural fitness functions)

GÜN 90: İLK AYRIŞTIRMA
  ──────────────────────
  7. EN FAYDALI servisi ayır (ROI en yüksek olan!)
     → Bağımsız ölçeklenmesi gereken? → İLK onu ayır!
     → PCI/güvenlik gereksinimi olan? → İLK onu ayır!

GÜN 180+: KADEMELI BÜYÜME
  ──────────────────────
  8. İhtiyaç oldukça yeni servisler ayır
  9. "Microservices for microservices' sake" YAPMA!
  10. Her ayrışma kararı ADR ile BELGELE!
```

### Karar Matrisi: Monolith ↔ Microservices

```
┌────────────────────────┬──────────┬──────────┬──────────────┐
│ BAĞLAM                 │ Monolith │ Modüler  │ Microservice │
│                        │          │ Monolith │              │
├────────────────────────┼──────────┼──────────┼──────────────┤
│ Takım: 1-5 kişi        │ ✅       │ 🟡      │ ❌ overkill  │
│ Takım: 5-20 kişi       │ 🟡      │ ✅       │ 🟡          │
│ Takım: 20+ kişi        │ ❌       │ 🟡      │ ✅           │
├────────────────────────┼──────────┼──────────┼──────────────┤
│ Ölçek: düşük           │ ✅       │ ✅       │ ❌ overkill  │
│ Ölçek: orta            │ 🟡      │ ✅       │ 🟡          │
│ Ölçek: yüksek/elastic  │ ❌       │ 🟡      │ ✅           │
├────────────────────────┼──────────┼──────────┼──────────────┤
│ Domain karmaşıklığı: ↓ │ ✅       │ ✅       │ ❌           │
│ Domain karmaşıklığı: ↑ │ ❌       │ ✅       │ ✅           │
├────────────────────────┼──────────┼──────────┼──────────────┤
│ Deploy hızı gereksinimi │ 🟡      │ ✅       │ ✅           │
│ Ops olgunluğu: düşük   │ ✅       │ ✅       │ ❌ tehlikeli │
│ Ops olgunluğu: yüksek  │ ✅       │ ✅       │ ✅           │
└────────────────────────┴──────────┴──────────┴──────────────┘

💡 MODÜLER MONOLİT = EN İYİ BAŞLANGIÇ NOKTASI!
  → Monolith'in basitliği + microservice'in sınırları
  → Gerektiğinde microservice'e geçiş KOLAY
  → Gerekmezse → KALIR → ve BU DA İYİDİR! ✅
```

---

## 16. � Büyük Şirketlerde Hard Parts Kararları

### Amazon — Monolith'e GERİ Dönüş

```
Amazon Prime Video ekibi (2023):
  → Microservices → Monolith geri geçiş yaptı!
  → Neden? AWS Lambda + Step Functions = çok pahalı
  → Monolith'e geçince %90 maliyet düşüşü

Bu kitabın ana mesajı tam bunu anlatır:
  → Microservice HER ZAMAN doğru cevap DEĞİL
  → Trade-off analizi yap: performans, maliyet, karmaşıklık
  → "Microservice çünkü herkes yapıyor" = YANLIŞ
```

### Shopify — Modular Monolith Champion

```
Shopify dünyanın EN BÜYÜK Ruby on Rails monolith'i:
  → 3M+ satır kod, tek deploy unit
  → AMA: İç yapısı modüler (component-based)
  → Packwerk tool ile modül sınırları ENFORCElaniyor

Kitaptaki karşılığı:
  → "Decompose etmeden ÖNCE modülerleştir"
  → Monolith içinde sınırları çiz → sonra karar ver
```

### Google — Saga Pattern Ölçeğinde

```
Google'ın Spanner veritabanı:
  → Distributed transaction GLOBAL ölçekte
  → TrueTime API ile saat senkronizasyonu
  → Kitaptaki "saga vs 2PC" tartışmasının ÖTESİNDE

Ama çoğu şirket Google DEĞİL:
  → Saga pattern yeterli
  → Eventually consistent çoğu case'de kabul edilebilir
  → "Google gibi yap" = overengineering
```

---

## 17. 🤖 Yapay Zeka Çağında Mimari Zor Kararlar

### AI Trade-off Analizi Yapabilir mi?

```
Bu kitabın RUHU: "Her karar bir trade-off"
AI bu trade-off'ları ANALİZ edebilir mi?

  ✅ Coupling analizi:
     → "Bu iki servis arasında ne tür coupling var?"
     → Static analysis + AI = güçlü

  ✅ Data decomposition önerisi:
     → "Bu 15 tabloyu servisler arasında nasıl bölerim?"
     → AI pattern eşleştirmesi yapabilir

  ❌ Organizational trade-off:
     → "Bu ekip saga pattern yönetebilir mi?"
     → Conway's Law + insan faktörü → AI cevaplayamaz

  ❌ Cost-benefit anlık:
     → "Microservice'e geçmek bize 6 ay mı kazandırır yoksa kaybettirir mi?"
     → Çok fazla bilinmeyen var
```

### AI ile Mimari Karar Promptları

```
DECOMPOSITION ANALİZİ:
  "Bu monolith'i decompose etmek için analiz yap.
   Richards & Ford'un Hard Parts kitabındaki 7 sürücüyü kullan:
   1. Hız (agility) — Bağımsız deploy gerekli mi?
   2. Performans — Ağ gecikmesi kabul edilebilir mi?
   3. Ölçeklenebilirlik — Farklı bileşenler farklı ölçeklenmeli mi?
   4. Hata toleransı — Biri çökünce diğerleri ayakta kalmalı mı?
   5. Güvenlik — Farklı güvenlik seviyeleri gerekli mi?
   6. Genişletilebilirlik — Bağımsız evrilme gerekli mi?
   7. Takım yapısı — Conway's Law nasıl etkiliyor?
   Her sürücüyü 1-5 puan ver."

SAGA vs 2PC:
  "Bu iş akışı için saga mı yoksa distributed transaction mı kullanmalıyız?
   Richards & Ford'un karar matrisini kullan:
   - Atomicity gerekli mi? → 2PC (performans pahasına)
   - Eventually consistent yeterli mi? → Saga
   - Compensation logic karmaşık mı? → Orchestrated Saga
   İş akışı: [açıklama]"
```

### Topluluk Görüşleri

```
Neal Ford (kitabın yazarı):
  "Hard Parts, Fundamentals of SA'nın devamı.
   Fundamentals TEORİ, Hard Parts PRATİK.
   İkisini birlikte oku."

Mark Richards (diğer yazar):
  "Microservice'e geçmek bir YOLCULUK.
   Bu kitap o yolculuktaki her KAVŞAKTA
   nasıl karar vereceğini anlatır."

Sam Newman:
  "Bu kitabın 'data decomposition' bölümü 
   Building Microservices'ta EKSİK olan PARÇA.
   İki kitap birbirini tamamlar."

Reddit r/softwarearchitecture:
  "Hard Parts okuyana kadar distributed transaction'ın
   ne kadar ZOR olduğunu bilmiyordum. Saga pattern
   basit görünür ama compensation logic KABUS."
```

---

## 18. �🎬 Son Sözler

### Kitabın Özet Kartı

```
┌──────────────────────────────────────────────────────────────┐
│         SOFTWARE ARCHITECTURE: THE HARD PARTS                │
│                   CHEAT SHEET                                │
├──────────────────────────────────────────────────────────────┤
│ YASALAR:                                                      │
│  1. Her şey bir trade-off'tur                                │
│  2. NEDEN, NASIL'dan önemlidir                               │
│                                                              │
│ AYRIŞMA:                                                     │
│  → Sürücüler: hız, performans, ölçek, hata tol., güvenlik   │
│  → Domain bazlı (teknik katman DEĞİL!)                      │
│  → Modüler monolith → en iyi başlangıç                      │
│                                                              │
│ VERİ:                                                        │
│  → Veri ayrışması en ZOR kısımdır                            │
│  → API composition, veri kopyalama, event sync               │
│  → Her servis kendi DB'si (database per service)             │
│                                                              │
│ İLETİŞİM:                                                    │
│  → Senkron: basit ama temporal coupling                      │
│  → Asenkron: loosely coupled ama eventual consistency        │
│  → Hibrit: context içi senkron, arası asenkron               │
│                                                              │
│ KOORDİNASYON:                                                │
│  → Orkestrasyon: görünür akış, merkezi kontrol               │
│  → Koreografi: bağımsız, ölçeklenebilir                     │
│  → Saga: dağıtık transaction → kompanzasyon ile              │
│                                                              │
│ KARAR:                                                       │
│  → ADR ile belgele                                           │
│  → MECE analiz                                               │
│  → Fitness functions ile ÖLÇÜLEBILIR kontrol                 │
└──────────────────────────────────────────────────────────────┘
```

### Tüm Kitaplarla Bağlantı 🔗

```
📕 Clean Code → Temiz kod → temiz servis sınırları
📘 Pragmatic Programmer → Trade-off düşüncesi → HER KARAR bir trade-off!
📗 Philosophy of SD → Deep modules → doğru granülerlikte servisler
📘 Design Patterns → Strategy/Observer → orkestrasyon/koreografi
📕 DDIA → Replikasyon, partitioning → veri ayrışma temelleri
📙 Unit Testing → Contract testing → servisler arası kontrat doğrulama
📗 Refactoring → Monolith refactoring → modülerleştirme
🏛️ Clean Architecture → Dependency Rule → servis katmanları
🏗️ Fundamentals of SA → Mimari stiller → hangi stil, ne zaman?
🔬 Building Microservices → Microservice temelleri → bu kitap DEVAMI
🔥 Phoenix Project → Akış, WIP → deployment pipeline, değişiklik yönetimi
🏗️ System Design → Ölçeklenebilir sistemler → doğru bölme = iyi ölçek
🔵 DDD → Bounded Context → servis SINIRLARININ TEMELİ!
🧩 Hard Parts → TÜM bunların ZOR KARARLARI! Gri bölge rehberi.

Bu kitap "doğru cevabı" vermez.
DOĞRU SORUYU sormayı öğretir.
"Hangi trade-off'ları KABUL etmeye hazırım?" sorusunu! 🎯
```

### Faz 4 İlerleme Durumu 📊

```
FAZ 4 — Ustalık (18+ ay)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Domain-Driven Design          ✅
  2. Software Arch: The Hard Parts ✅  ← BURADASIN
  3. The Staff Engineer's Path     ⬜
  4. Thinking in Systems           ⬜
```

---

> **"Mimarlık kararları 'doğru' veya 'yanlış' değildir.
> 'Bağlamında uygun' veya 'bağlamında uygunsuz'dur.
>
> Microservices mükemmel DEĞİLDİR.
> Monolith kötü DEĞİLDİR.
> Her ikisi de BELİRLİ koşullarda EN İYİ seçimdir.
>
> İyi mimar, trade-off'ları GÖREN,
> bağlamı ANLAYAN ve kararını
> GEREKÇEYLE belgeleyen kişidir.
>
> Ve en önemlisi:
> 'Bilmiyorum, AMA öğreneceğim.'
> diyebilen kişidir.
>
> Çünkü mimarlık bir SON değil,
> sürekli evrilen bir YOLCULUKTUR."** 🧩
