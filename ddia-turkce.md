# 📊 Designing Data-Intensive Applications (DDIA) — Türkçe Kapsamlı Rehber

> **"Veri yoğun uygulamaların tasarımı, yazılım mühendisliğinin
> en kritik ve en az anlaşılan alanlarından biridir."**
> — Martin Kleppmann

Bu kitap, modern yazılım sistemlerinin **omurgası** olan veri katmanını
temelden tavana anlatır. Veritabanları, dağıtık sistemler, replikasyon,
partitioning, transaction'lar, batch/stream processing...

**Neden bu kadar önemli?** Çünkü bugün yazdığın uygulamaların %90'ı
**compute-intensive** (işlem yoğun) değil, **data-intensive** (veri yoğun).
Darboğaz CPU değil, VERİDİR: miktarı, karmaşıklığı, hızı.

---

## 📖 İçindekiler

### BÖLÜM I — Veri Sistemlerinin Temelleri
1. [Güvenilir, Ölçeklenebilir, Bakımı Kolay Uygulamalar](#1--güvenilir-ölçeklenebilir-bakımı-kolay-uygulamalar)
2. [Veri Modelleri ve Sorgu Dilleri](#2--veri-modelleri-ve-sorgu-dilleri)
3. [Depolama ve Veri Çekme](#3--depolama-ve-veri-çekme)
4. [Encoding ve Evrim](#4--encoding-ve-evrim)

### BÖLÜM II — Dağıtık Veri
5. [Replikasyon](#5--replikasyon)
6. [Partitioning (Bölümleme)](#6--partitioning-bölümleme)
7. [Transaction'lar](#7--transactionlar)
8. [Dağıtık Sistemlerin Sorunları](#8--dağıtık-sistemlerin-sorunları)
9. [Tutarlılık ve Konsensus](#9--tutarlılık-ve-konsensus)

### BÖLÜM III — Türetilmiş Veri
10. [Batch Processing](#10--batch-processing)
11. [Stream Processing](#11--stream-processing)
12. [Veri Sistemlerinin Geleceği](#12--veri-sistemlerinin-geleceği)

---

# BÖLÜM I — Veri Sistemlerinin Temelleri

---

## 1. 🏗️ Güvenilir, Ölçeklenebilir, Bakımı Kolay Uygulamalar

Her veri yoğun uygulamanın üç temel hedefi vardır:

### 1.1 Güvenilirlik (Reliability) 🛡️

> **"Bir şeyler ters gitse bile, sistem doğru çalışmaya devam etmeli."**

Hata (fault) ≠ Çökme (failure):
- **Fault:** Bir bileşenin beklentiden sapması (disk bozulması, ağ kesintisi)
- **Failure:** Sistemin kullanıcıya hizmet verememesi

Hedef: **Fault-tolerant** (hataya dayanıklı) sistem — fault'ları tolere ederek failure'ı ENGELLE.

```
Hata Türleri:

1. Donanım Hataları 💽
   - Disk bozulması: Yılda %2-4 (MTBF ~10-50 yıl)
   - RAM hataları, güç kesintisi, ağ kartı arızası
   - Çözüm: Yedeklilik (RAID, çift güç kaynağı, yedek sunucu)

2. Yazılım Hataları 🐛
   - Donanımdan DAHA TEHLİKELİDİR! Çünkü korelasyonlu:
     Bir bug tüm sunucularda AYNI ANDA tetiklenebilir!
   - Örnekler:
     - Linux çekirdeği bug'ı (2012): Artık saniye → tüm sunucular çöktü
     - Sonsuz döngüye giren süreç
     - Dış servis yavaşlayınca kaskat çökme (cascading failure)
   - Çözüm: Process izolasyonu, izleme, test, kaotik mühendislik

3. İnsan Hataları 👤
   - EN BÜYÜK HATA KAYNAĞI! (konfigürasyon hatası → %80+ kesinti)
   - Çözüm:
     - Hata yapmayı zorlaştıran API/UI tasarımı
     - Sandbox ortamları (prod'a değmeden test et)
     - Kolay rollback mekanizmaları
     - Telemetri ve izleme (monitoring)
```

### 1.2 Ölçeklenebilirlik (Scalability) 📈

> **"Yük arttığında, sistem performansı koruyabilmeli."**

#### Yükü Tanımlamak

İlk adım: **"Yük"ü somut rakamlarla tanımla.**

```
Twitter'ın Yükü (klasik örnek):

- Tweet gönderme: 4.6K istek/saniye (ortalama), 12K/saniye (zirve)
- Timeline okuma: 300K istek/saniye

Soru: Yeni bir tweet yazıldığında 300K kullanıcının timeline'ına
      nasıl ulaştırırsın?

Yaklaşım 1 — Okuma zamanında birleştir (fan-out on read):
  Timeline istendiğinde: Kullanıcının takip ettiklerinin tweet'lerini
  sorgula, birleştir, sırala, göster.
  → Okuma YAVAŞ (her seferinde join), yazma HIZLI

Yaklaşım 2 — Yazma zamanında dağıt (fan-out on write):
  Tweet yazıldığında: Her takipçinin timeline cache'ine tweet'i ekle.
  → Yazma YAVAŞ (N takipçi × write), okuma HIZLI (cache'ten oku)

Twitter'ın çözümü: İKİSİNİ DE KULLAN!
  - Normal kullanıcılar → Yaklaşım 2 (fan-out on write)
  - Ünlüler (10M+ takipçi) → Yaklaşım 1 (fan-out on read)
    Çünkü 10M cache'e yazmak çok pahalı!
```

#### Performansı Tanımlamak

Performansı ölçerken **ortalama** değil, **yüzdelik dilimler (percentile)** kullan:

```
Örnek: 1000 isteğin yanıt süreleri

Ortalama (mean): 200ms  ← YANILTICI! Tek bir 10s'lik istek ortalamayı bozar.

Yüzdelik dilimler:
  p50 (medyan):  180ms  ← İsteklerin yarısı bundan hızlı
  p95:           500ms  ← İsteklerin %95'i bundan hızlı
  p99:          1500ms  ← İsteklerin %99'u bundan hızlı
  p99.9:        5000ms  ← İsteklerin %99.9'u bundan hızlı

Neden p99 önemli?
→ En yüksek p99'a sahip kullanıcılar genellikle EN ÇOK
  alışveriş yapan (dolayısıyla en değerli) müşteriler.
  Amazon: p99.9 = %0.1'lik en yavaş kullanıcılar = TEK BİR müşterinin
  çok fazla siparişi var → sepeti büyük → sorgu yavaş
```

```
SLA Örneği (Service Level Agreement):
"Servisimiz p99'da 300ms altında yanıt verecektir,
 ayda %99.9 kullanılabilirlik sağlayacaktır."

%99.9 uptime = Yılda ~8.7 saat kesinti
%99.99 uptime = Yılda ~52 dakika kesinti
%99.999 uptime = Yılda ~5 dakika kesinti (beş dokuz!)
```

#### Ölçekleme Stratejileri

```
Dikey Ölçekleme (Scale Up) ⬆️
  → Daha güçlü makine: daha fazla RAM, daha hızlı CPU
  + Basit, tek sunucu
  - Sınırlı (bir noktada daha güçlü makine yok)
  - Pahalı (2x güç ≠ 2x fiyat, genelde daha pahalı)
  - Tek nokta arızası (single point of failure)

Yatay Ölçekleme (Scale Out) ↔️
  → Daha çok makine
  + Ucuz (commodity hardware)
  + Teorik olarak sınırsız
  + Hata toleransı (bir makine çökse diğerleri devam eder)
  - Karmaşık (dağıtık sistem sorunları)
  - Veri tutarlılığı zor

Pratikte: İKİSİNİN KOMBİNASYONU
  Olabildiğince iyi bir makine + yatay ölçekleme
```

### 1.3 Bakım Kolaylığı (Maintainability) 🔧

> **"Kodun ömrünün %80'i BAKIM'dır."**

Üç alt prensip:

```
1. Operability (İşletilebilirlik):
   → Operasyon ekibinin işini kolaylaştır
   → İyi monitoring, deployment, dokümantasyon

2. Simplicity (Basitlik):
   → Yeni mühendislerin sistemi anlamasını kolaylaştır
   → Gereksiz karmaşıklığı (accidental complexity) ortadan kaldır
   → İyi soyutlamalar kullan

3. Evolvability (Geliştirilebilirlik):
   → İleride değişiklik yapmayı kolaylaştır
   → Agile, TDD, refactoring
```

---

## 2. 📊 Veri Modelleri ve Sorgu Dilleri

### 2.1 İlişkisel Model (SQL) 🗃️

1970'lerde Edgar Codd tarafından önerildi. Veriler **tablolarda** (ilişkilerde) saklanır.

```sql
-- İlişkisel model: Tablolar ve ilişkiler
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),  -- Foreign Key (ilişki)
    total DECIMAL(10,2),
    created_at TIMESTAMP
);

-- JOIN ile ilişki
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.id = 123;
```

**Güçlü yanları:**
- ✅ Veri tutarlılığı (schema enforcement, foreign keys)
- ✅ Esnek sorgulama (JOIN, GROUP BY, aggregation)
- ✅ ACID transaction'ları
- ✅ 50 yıllık olgunluk

**Zayıf yanları:**
- ❌ Nesnesel verilerle "impedance mismatch" (ORM sorunu)
- ❌ Yatay ölçekleme zor
- ❌ Schema değişikliği maliyetli (ALTER TABLE)

### 2.2 Belge Modeli (Document - NoSQL) 📄

```javascript
// MongoDB / CouchDB: Her kayıt bağımsız bir "belge"
{
  "_id": "user-123",
  "name": "Ali Yılmaz",
  "email": "ali@example.com",
  "addresses": [
    {
      "type": "home",
      "city": "İstanbul",
      "district": "Kadıköy",
      "street": "Moda Caddesi 42"
    },
    {
      "type": "work",
      "city": "İstanbul",
      "district": "Levent",
      "street": "Büyükdere Cad. 100"
    }
  ],
  "orders": [
    { "id": "ord-1", "total": 150.50, "date": "2024-03-15" },
    { "id": "ord-2", "total": 89.90, "date": "2024-03-20" }
  ]
}
```

**Güçlü yanları:**
- ✅ Schema esnekliği (schema-on-read vs schema-on-write)
- ✅ Veri yerleşimi (bir kullanıcının tüm verisi TEK YERDE)
- ✅ Yatay ölçekleme (sharding) kolay
- ✅ Nesnesel yapılarla doğal uyum

**Zayıf yanları:**
- ❌ JOIN zor/yok (veri denormalize → tekrar/duplicate riski)
- ❌ Belgeler arası ilişkiler zayıf
- ❌ Karmaşık sorgular sınırlı

### 2.3 Grafik Modeli 🕸️

Veriler arası **ilişkiler** ön plandaysa:

```
Sosyal ağ, tavsiye motoru, fraud detection, bilgi grafiği...

Düğümler (Nodes): Varlıklar (kişi, yer, ürün)
Kenarlar (Edges): İlişkiler (arkadaş, satın aldı, yaşıyor)

Ali —[ARKADAŞ]→ Ayşe
Ali —[YAŞIYOR]→ İstanbul
Ali —[SATIN_ALDI]→ iPhone
İstanbul —[İÇİNDE]→ Türkiye
Ayşe —[SATIN_ALDI]→ iPhone
```

```
// Cypher (Neo4j sorgu dili):
MATCH (user:Person)-[:SATIN_ALDI]->(product:Product)
      <-[:SATIN_ALDI]-(other:Person)
WHERE user.name = 'Ali'
AND NOT (user)-[:ARKADAŞ]-(other)
RETURN other.name, product.name

// "Ali'nin aldığı ürünleri alan AMA Ali'nin arkadaşı OLMAYAN kişiler"
// → Öneri sistemi: "Bu ürünü alanlar şunları da aldı"
```

### 2.4 Ne Zaman Hangisi? 🤔

```
┌──────────────┬──────────────┬──────────────┬──────────────┐
│              │  İlişkisel   │   Belge      │   Grafik     │
│              │   (SQL)      │  (Document)  │  (Graph)     │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ Veri yapısı  │ Tablo/satır  │ JSON/BSON    │ Düğüm/Kenar  │
│ İlişkiler    │ Güçlü (JOIN) │ Zayıf        │ ÇOK GÜÇLÜ   │
│ Schema       │ Katı         │ Esnek        │ Esnek        │
│ Ölçekleme    │ Dikey (↑)    │ Yatay (↔)    │ Zor          │
│ Tutarlılık   │ Güçlü (ACID) │ Eventual     │ Değişir      │
│ İyi olduğu   │ Yapısal veri │ Hiyerarşik   │ Bağlantılı   │
│ alan         │ ERP, finans  │ CMS, profil  │ Sosyal ağ    │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ Örnekler     │ PostgreSQL   │ MongoDB      │ Neo4j        │
│              │ MySQL        │ CouchDB      │ Amazon        │
│              │ Oracle       │ DynamoDB     │ Neptune       │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

> **Önemli:** SQL vs NoSQL bir SAVAŞ değildir! Farklı problemler için farklı araçlar. Çoğu modern uygulama **polyglot persistence** kullanır: farklı verileri farklı veritabanlarında tutar.

---

## 3. 💾 Depolama ve Veri Çekme

### 3.1 Log-Structured Storage Engines 📝

**Temel fikir:** Verileri sıralı bir şekilde dosyaya **ekle** (append). Asla üzerine yazma.

#### Hash Index

```
Veriler dosyaya ardışık eklenir:
┌─────────────────────────────────────────┐
│ key1:val1 | key2:val2 | key1:val3 | ... │  (append-only log)
└─────────────────────────────────────────┘

Hash tablosu (bellekte):
{ key1: offset_3, key2: offset_2, key3: ... }
          ↓
Dosyada 3. pozisyona git → val3'ü oku

Yazma: O(1) → Dosyanın sonuna ekle + hash tablosunu güncelle
Okuma: O(1) → Hash'ten offset'i al → dosyada o pozisyona git

Problem: Hash tablosu BELLEĞE SAĞMALI! Anahtar sayısı sınırlı.
```

#### SSTable & LSM-Tree (Log-Structured Merge-Tree) 🌲

Modern NoSQL'lerin (Cassandra, LevelDB, RocksDB) temelindeki yapı:

```
Yazma akışı:

1. Yeni veri → MEMTABLE (bellekte sıralı ağaç, örn: Red-Black tree)
2. Memtable dolunca → Diske SSTABLE olarak yazılır (sorted string table)
3. Arka planda COMPACTION: Birden fazla SSTable birleştirilir

Memtable (bellekte, sıralı):
  apple → 5
  banana → 3
  cherry → 8
         │ (flush)
         ▼
SSTable (diskte, sıralı):
┌────────┬────────┬────────┐
│apple:5 │banana:3│cherry:8│  (key'lere göre sıralı!)
└────────┴────────┴────────┘

Okuma akışı:
1. Önce Memtable'da ara (bellekte → hızlı)
2. Yoksa en yeni SSTable'da ara
3. Yoksa bir önceki SSTable'da ara
4. ... (en eskiye doğru)

Optimizasyon: Bloom Filter → "Bu key bu SSTable'da var mı?"
  → Kesinlikle yoksa disk okuması YAPMA (false positive olabilir ama false negative OLMAZ)
```

```
Compaction stratejileri:

Size-Tiered (Cassandra varsayılan):
  Küçük SSTable'lar birikince → büyük SSTable'a birleştir
  + Yazma hızı yüksek
  - Okuma biraz yavaş (çok SSTable kontrol et)
  - Geçici disk kullanımı yüksek

Leveled (LevelDB, RocksDB):
  SSTable'lar "seviye"lere ayrılır
  Level 0: Memtable flush'ları (sırasız)
  Level 1: ~10MB toplam, örtüşmeyen aralıklar
  Level 2: ~100MB toplam, örtüşmeyen aralıklar
  ...
  + Okuma hızlı (her key en fazla 1 SSTable'da/seviyede)
  - Yazma amplifikasyonu (write amplification)
```

### 3.2 B-Tree (Geleneksel Veritabanları) 🌳

PostgreSQL, MySQL, Oracle — her büyük SQL veritabanı B-Tree kullanır:

```
B-Tree yapısı (sabit boyutlu sayfalar, genellikle 4KB):

                    [100 | 250 | 500]         ← Kök sayfa
                   /      |       \      \
        [20|60|90]   [150|200]  [300|400] [600|800]  ← İç sayfalar
        /  |  \  \
   [1-19][21-59][61-89][91-99]                ← Yaprak sayfalar (veri burada)

Arama: key=75
  1. Kök: 75 < 100 → Sol alt ağaç
  2. İç: 60 < 75 < 90 → Orta alt ağaç
  3. Yaprak: [61-89] → 75'i bul!

Derinlik: ~3-4 seviye yeterli (milyarlarca kayıt için!)
  - 4KB sayfa, branching factor ~500
  - 4 seviye = 500⁴ = 62.5 MİLYAR kayıt!
```

```
B-Tree vs LSM-Tree karşılaştırma:

┌────────────────┬─────────────────┬──────────────────┐
│                │    B-Tree       │    LSM-Tree      │
├────────────────┼─────────────────┼──────────────────┤
│ Okuma          │ Hızlı ✅       │ Biraz yavaş ⚠️   │
│ Yazma          │ Yavaş (rastgele│ Hızlı (sıralı    │
│                │ disk erişimi)   │ yazma) ✅        │
│ Disk kullanımı │ Fragmentasyon   │ Compact ✅       │
│ Tahmin edilebilir│ Evet ✅       │ Compaction'a bağlı│
│ Transaction    │ Doğal ✅       │ Zor ⚠️           │
│ Kullanım       │ PostgreSQL,     │ Cassandra,        │
│                │ MySQL, Oracle   │ RocksDB, LevelDB  │
└────────────────┴─────────────────┴──────────────────┘

Kural: Okuma ağırlıklı → B-Tree, Yazma ağırlıklı → LSM-Tree
```

### 3.3 OLTP vs OLAP 📊

İki farklı erişim deseni, iki farklı optimizasyon:

```
OLTP (Online Transaction Processing):
  "Kullanıcı 123'ün siparişini getir"
  → Az sayıda satır, tüm sütunlar
  → Düşük gecikme (ms) önemli
  → MySQL, PostgreSQL

OLAP (Online Analytical Processing):
  "Son 3 ayda, şehirlere göre satış toplamı nedir?"
  → Milyonlarca satır, az sayıda sütun
  → Gecikme değil, throughput önemli
  → Data Warehouse (BigQuery, Redshift, Snowflake)

┌─────────────────────┬───────────────┬───────────────┐
│                     │    OLTP       │    OLAP       │
├─────────────────────┼───────────────┼───────────────┤
│ Kullanıcı           │ Uygulama      │ Analist       │
│ Veri boyutu/sorgu   │ Az (KB)       │ Çok (GB)      │
│ Sorgu tipi          │ Anahtar bazlı │ Aggregation   │
│ Yazma               │ Sık, küçük    │ Nadir, toplu  │
│ Gecikme             │ ~ms           │ ~sn-dk        │
│ Depolama            │ Satır bazlı   │ Sütun bazlı   │
└─────────────────────┴───────────────┴───────────────┘
```

### 3.4 Sütun Bazlı Depolama (Column-Oriented) 📊

OLAP sorguları genellikle birkaç sütuna bakar ama MİLYONLARCA satırı tarar:

```
Satır bazlı depolama (Row-oriented):
┌──────┬────────┬──────┬────────┬──────────┐
│  id  │  name  │ city │ amount │   date   │
├──────┼────────┼──────┼────────┼──────────┤
│  1   │  Ali   │ IST  │  100   │ 2024-01  │
│  2   │  Ayşe  │ ANK  │  200   │ 2024-01  │
│  3   │  Mert  │ IST  │  150   │ 2024-02  │
│  ...                 ... (100M satır)      │
└──────┴────────┴──────┴────────┴──────────┘

Sorgu: SELECT city, SUM(amount) GROUP BY city
→ Tüm satırları oku ama sadece city ve amount lâzım!
→ name ve date'i de okumak ZAMAN KAYBI!

Sütun bazlı depolama (Column-oriented):
id:     [1, 2, 3, ...]      ← Ayrı dosya
name:   [Ali, Ayşe, Mert, ...]  ← Ayrı dosya (OKUNMAZ!)
city:   [IST, ANK, IST, ...]    ← Sadece BU okunur ✅
amount: [100, 200, 150, ...]     ← Sadece BU okunur ✅
date:   [2024-01, 2024-01, ...]  ← Okunmaz!

→ Sadece gerekli 2 sütunu oku, 3 sütunu ATLA!
→ 100M satır × 5 sütun yerine 100M satır × 2 sütun oku
→ %60 daha az disk I/O!

BONUS: Sütun sıkıştırma çok etkili!
  city sütunu: [IST, IST, IST, ANK, ANK, IST, IST, ...]
  → Run-Length Encoding: (IST, 3), (ANK, 2), (IST, 2), ...
  → Bitmap Index: IST=[1,1,1,0,0,1,1,...], ANK=[0,0,0,1,1,0,0,...]
  → 10x-100x sıkıştırma!
```

---

## 4. 📦 Encoding ve Evrim

### 4.1 Veri Formatları

Programın içindeki veriyi (objects, structs) ağ üzerinden veya diske yazılabilir hale getirme: **serialization / encoding / marshalling**.

```
                    Encoding
In-memory ─────────────────→ Byte dizisi
(objects)  ←───────────────── (JSON, Protobuf, Avro)
                    Decoding
```

### JSON vs Binary Formatlar

```json
// JSON: İnsan okunabilir, ama...
{
  "userName": "Ali",
  "favoriteNumber": 1337,
  "interests": ["swimming", "coding"]
}
// Bu JSON: 81 byte

// Problem 1: Tip belirsizliği
// "favoriteNumber": 1337  → İnteger mi? Float mu? Taşma var mı?
// Problem 2: Binary veri desteklemez (Base64 → %33 büyüme)
// Problem 3: Gereksiz tekrar ("favoriteNumber" her kayıtta tekrar)
```

```
Protocol Buffers (Google):
  message Person {
    required string user_name = 1;        // field tag = 1
    optional int64 favorite_number = 2;   // field tag = 2
    repeated string interests = 3;        // field tag = 3
  }
  // Aynı veri: 33 byte (JSON'un %40'ı!)
  // Tipler kesin (int64), schema zorunlu

Apache Avro (Hadoop ekosistemi):
  {
    "type": "record",
    "name": "Person",
    "fields": [
      {"name": "userName", "type": "string"},
      {"name": "favoriteNumber", "type": "long"},
      {"name": "interests", "type": {"type": "array", "items": "string"}}
    ]
  }
  // Aynı veri: 32 byte
  // Field adları bile yok (schema'dan çözümlenir)
```

### 4.2 Schema Evrimi 🔄

Gerçek dünyada schema'lar DEĞİŞİR. Önemli olan: **geriye dönük uyumluluk** (backward compatibility) ve **ileriye dönük uyumluluk** (forward compatibility).

```
Backward compatible (geriye dönük):
  YENİ kod, ESKİ veriyi okuyabilir ✅
  → Kolay: Yeni alanı "optional" veya "default" ile ekle

Forward compatible (ileriye dönük):
  ESKİ kod, YENİ veriyi okuyabilir ✅
  → Daha zor: Eski kod bilinmeyen alanları GÖRMEZDEN gelir

Kural:
  ✅ Alan EKLEMEk güvenli (yeni alan optional olmalı)
  ✅ Alan SİLMEk güvenli (ancak eski kod bunu handle edebilmeliyse)
  ❌ Alan TİPİNİ değiştirmek TEHLİKELİ
  ❌ Field tag/number değiştirmek YASAK (Protobuf)
```

```
Neden önemli? → Rolling upgrade!

Sunucu parkı: v1 v1 v1 v1 v1 (tüm sunucular eski versiyon)

Rolling upgrade: v2 v1 v1 v1 v1
                 v2 v2 v1 v1 v1
                 v2 v2 v2 v1 v1
                 ...
                 v2 v2 v2 v2 v2

Bu süreçte:
  - v2 sunucu, v1'in ürettiği veriyi OKUYACAK (backward compat.)
  - v1 sunucu, v2'nin ürettiği veriyi OKUYACAK (forward compat.)
  - İkisi de çalışmalı!
```

---

# BÖLÜM II — Dağıtık Veri

---

## 5. 🔄 Replikasyon

> **"Aynı veriyi birden fazla makinede tut."**

**Neden?**
1. **Gecikme:** Veriyi kullanıcıya yakın tut (coğrafi dağıtım)
2. **Kullanılabilirlik:** Bir makine çökerse diğeri devam etsin
3. **Okuma kapasitesi:** Okuma yükünü dağıt

### 5.1 Lider-Takipçi Replikasyonu (Leader-Follower)

```
En yaygın model:

Yazma → [LEADER] ──replikasyon──→ [FOLLOWER 1]
                  ──replikasyon──→ [FOLLOWER 2]
                  ──replikasyon──→ [FOLLOWER 3]

Okuma → [LEADER] veya [FOLLOWER 1/2/3]

Kurallar:
  - Yazma: SADECE Leader'a
  - Okuma: Leader veya herhangi bir Follower
  - Replikasyon: Leader → Follower (tek yönlü)
```

#### Senkron vs Asenkron Replikasyon

```
Senkron replikasyon:
  Client → Leader → Follower → OK → Client'a "tamam" de
  + Follower her zaman güncel (guaranteed consistency)
  - Follower yavaşlarsa TÜM SİSTEM yavaşlar 😱
  - Follower çökerse yazma DURUR

Asenkron replikasyon:
  Client → Leader → OK → Client'a hemen "tamam" de
                   → (Arka planda) Follower'lara gönder
  + Hızlı, Leader bağımsız çalışır
  - Follower geride kalabilir (replication lag)
  - Leader çökerse, henüz replike edilmemiş veri KAYBOLABİLİR 😱

Yarı-senkron (semi-synchronous):
  → BİR follower senkron, diğerleri asenkron
  → En yaygın pratik çözüm (PostgreSQL'de kullanılır)
```

#### Replikasyon Gecikmesi (Replication Lag) Sorunları ⏱️

```
Sorun 1: Read-after-write consistency (Kendi yazdığını oku)

  Kullanıcı profil günceller → Leader'a yazar → Sayfayı yeniler
  → Follower'dan okur → ESKİ veriyi görür!
  → "Güncelleme kaydedilmedi mi?!" 😡

  Çözüm: Kullanıcının KENDİ verisini her zaman Leader'dan oku
          Başkalarının verisini Follower'dan oku

Sorun 2: Monotonic reads (Zamanda geriye gitme)

  Kullanıcı sayfayı iki kez yeniler:
  İlk → Follower 1'den oku (güncel veri) ✅
  İkinci → Follower 2'den oku (eski veri! Follower 2 geride) ❌
  → Yorum var → yorum yok → yorum var... kaos!

  Çözüm: Aynı kullanıcıyı her zaman aynı Follower'a yönlendir
          (session-based routing, hash(userId) → follower)

Sorun 3: Consistent prefix reads (Nedensellik bozulması)

  Sohbet:
    Ayşe: "Cevap ne?" (t=1)  → Follower A'ya yazıldı
    Ali:  "42!"       (t=2)  → Follower B'ye yazıldı

  Okuyucu Follower B'yi önce okursa:
    Ali: "42!"          ← ???
    Ayşe: "Cevap ne?"   ← Ah, tamam

  → Nedensellik (causality) bozuldu! Cevap sorudan ÖNCE göründü!

  Çözüm: İlişkili yazmaları aynı partisyon'a yaz
          veya causal ordering mekanizması kullan
```

### 5.2 Çoklu Lider Replikasyon (Multi-Leader)

```
Birden fazla lidere yazma izni:

[LEADER A] ←──→ [LEADER B] ←──→ [LEADER C]
  ↓    ↓           ↓    ↓          ↓    ↓
[F1]  [F2]       [F3]  [F4]     [F5]  [F6]

Kullanım durumları:
  - Birden fazla veri merkezi (her DC'de bir leader)
  - Çevrimdışı çalışan uygulamalar (her cihaz bir leader)
    → Takvim uygulaması: Telefonda düzenle, bilgisayarda düzenle,
      internet olunca SENKRONİZE ET

Büyük problem: ÇAKIŞMA (conflict)!
```

#### Çakışma Çözme Stratejileri ⚔️

```
Ali (Leader A): Başlık = "Merhaba"     (t=1)
Ayşe (Leader B): Başlık = "Selam"      (t=1)

İkisi de aynı anda farklı değer yazdı! Hangisi kazanır?

Strateji 1: Last Write Wins (LWW) ⏰
  → Daha yüksek timestamp kazanır
  + Basit
  - VERİ KAYBI! Kaybeden yazma sessizce silinir 😱
  - Saat senkronizasyonu güvenilmez

Strateji 2: Kullanıcıya sor 👤
  → İki versiyonu da sakla, kullanıcıya "hangisini istersin?" sor
  → CouchDB bunu yapar
  + Veri kaybı yok
  - UX açısından kötü

Strateji 3: CRDT (Conflict-free Replicated Data Types) 🧬
  → Veri yapıları matematiksel olarak birleştirilebilir
  → Örn: Sayaçlar, kümeler, listeler
  + Otomatik, veri kaybı yok
  - Sınırlı veri tipleri, karmaşık

Strateji 4: Operational transformation 📝
  → Google Docs bunu kullanır
  → İşlemlerin sırasını ve etkisini dönüştürür
  + Gerçek zamanlı işbirliği
  - Çok karmaşık implementasyon
```

### 5.3 Lidersiz Replikasyon (Leaderless)

```
Leader YOK! Client doğrudan birden fazla node'a yazar.

Dynamo-style: Amazon DynamoDB, Cassandra, Riak

Yazma: N node'un W'sine yaz (W = write quorum)
Okuma: N node'un R'sinden oku (R = read quorum)

Koşul: W + R > N  → En az bir node'dan güncel veriyi alırsın!

Örnek: N=3, W=2, R=2
  Yazma: 3 node'dan 2'sine yaz → OK
  Okuma: 3 node'dan 2'sinden oku → En az 1'i güncel → EN YENİ değeri seç

      [Node1: v2] ───→ Oku
      [Node2: v2] ───→ Oku   → İkisi de v2 → Güncel! ✅
      [Node3: v1]            → Okunmadı (R=2 yeterli)

Ya da:
      [Node1: v2] ───→ Oku
      [Node2: v1] ───→ Oku   → v1 ve v2 → Daha yenisi v2 → Güncel! ✅
      [Node3: v2]            → Okunmadı

Ama: W + R ≤ N ise → Stale read mümkün!
  N=3, W=1, R=1 → Hızlı ama tutarsız okuma riski
```

```
Sloppy Quorum & Hinted Handoff:

Normal quorum: 3 node'dan 2'sine yaz
Ya 2 node çöktüyse? → Alamıyoruz quorum! Yazma BAŞARISIZ!

Sloppy quorum:
  → Asıl node'lar çöktüyse, GEÇİCİ başka node'lara yaz
  → Asıl node'lar geri gelince, veriyi onlara AKTAR (hinted handoff)
  + Yüksek kullanılabilirlik (her zaman yazabilirsin)
  - Tutarlılık garantisi zayıflar
```

---

## 6. 🧩 Partitioning (Bölümleme)

> **"Büyük bir veri setini PARÇALARA ayırarak birden fazla makineye dağıt."**

Replikasyon: Aynı veriyi birden fazla yere KOPYALA → Hata toleransı
Partitioning: Veriyi BÖLEREK dağıt → Ölçeklenebilirlik

```
100 GB veri, tek makine:
  [======================== 100 GB ========================]
  Okuma: Tüm yük tek makinede → DARBOĞAZ!

100 GB veri, 4 partition:
  Makine 1: [===== 25 GB =====]  ← A-F arası müşteriler
  Makine 2: [===== 25 GB =====]  ← G-L arası
  Makine 3: [===== 25 GB =====]  ← M-S arası
  Makine 4: [===== 25 GB =====]  ← T-Z arası
  → Her makine sadece KENDİ parçasını işler → 4x hız!
```

### 6.1 Partitioning Stratejileri

#### Key Range Partitioning (Anahtar Aralığı)

```
Anahtarı sıralı böl:
  Partition 1: A — F
  Partition 2: G — L
  Partition 3: M — S
  Partition 4: T — Z

+ Sıralı tarama (range scan) kolay
  "A'dan D'ye kadar tüm kullanıcılar" → Sadece Partition 1
+ Basit anlaşılır

- HOT SPOT riski! 🔥
  Anahtar = tarih ise → Bugünkü veriler HEP aynı partition'a!
  Anahtar = kullanıcı adı ise → "A" harfiyle başlayan daha çok olabilir
```

#### Hash Partitioning (Hash Bölümleme)

```
hash(key) mod N → Partition numarası

hash("Ali")    = 7    → 7 mod 4 = 3 → Partition 3
hash("Ayşe")   = 12   → 12 mod 4 = 0 → Partition 0
hash("Mehmet")  = 5    → 5 mod 4 = 1 → Partition 1

+ Eşit dağılım (hot spot riski düşük)
+ Basit

- Sıralı tarama İMKANSIZ
  "A'dan D'ye kadar kullanıcılar" → TÜM partition'ları tara! 😱
- N değişince TÜM veriler yer değiştirir (rehashing)
```

#### Consistent Hashing (Tutarlı Hash) 🔮

```
Normal hash: N değişince her şey yer değiştirir
Consistent hash: N değişince sadece ~1/N oranında veri yer değiştirir

Daire üzerinde hash:
        0°
       ╱  ╲
      A    D       (A, B, C, D = sunucular)
     ╱      ╲      Veriler saat yönünde ilk sunucuya gider
    ╱        ╲
   B──────────C
      180°

Yeni sunucu E eklendi → Sadece E'nin komşusundaki veriler taşınır!
A, B, C'deki verilerin ÇOĞU YERİNDE kalır ✅
```

### 6.2 Sekonder İndeksler ve Partitioning

```
Ana anahtar ile partitioning kolay. Peki sekonder indeksler?

Örnek: Araba ilanları
  Partition by: id (mod N)
  Ama kullanıcı "renk=kırmızı" diye arar!

Yaklaşım 1: Yerel indeks (document-based / local index)
  Her partition kendi indeksini tutar
  Sorgu: TÜM partition'lara sor → birleştir (scatter/gather)
  - Yavaş! N partition = N sorgu

Yaklaşım 2: Global indeks (term-based)
  Renk indeksi:
    Partition A: kırmızı → [id1, id5, id9]  (tüm kırmızılar burada)
    Partition B: mavi → [id2, id7, id12]
  Sorgu: Sadece ilgili indeks partition'ına sor
  + Hızlı okuma
  - Yavaş yazma (her yazma indeks partition'ını da güncelle)
  - Asenkron güncelleme → geçici tutarsızlık
```

### 6.3 Rebalancing (Yeniden Dengeleme) ⚖️

```
Partition'ları yeniden dağıtma ihtiyacı:
  - Yeni makine eklendi → Yükü paylaştır
  - Makine çöktü → Partition'larını başka makinelere taşı
  - Bir partition çok büyüdü → Böl

Strateji 1: Sabit sayıda partition (Cassandra, Riak, Elasticsearch)
  Baştan 1000 partition oluştur, 10 makineye dağıt (100'er)
  Yeni makine → Bazı partition'ları taşı
  + Basit, hızlı
  - Partition sayısını baştan iyi seçmelisin

Strateji 2: Dinamik partition (HBase, RethinkDB)
  Partition büyüdüğünde ikiye BÖL
  Partition küçüldüğünde BİRLEŞTİR
  + Otomatik ayarlama
  - Daha karmaşık

⚠️ ÖNEMLİ: hash(key) mod N KULLANMA rebalancing için!
  N değişince %100 veri yer değiştirir → Felaket!
```

---

## 7. 💼 Transaction'lar

> **"Transaction'lar, uygulamanın birden fazla okuma/yazma işlemini
> TEK bir mantıksal birim olarak gruplandırmasına olanak tanır."**

### 7.1 ACID ⚗️

```
A — Atomicity (Bütünlük):
  "Ya hepsi ya hiçbiri"
  → 3 adımlık işlem: 1 ✅ 2 ✅ 3 ❌ → TÜMÜne geri al (rollback)!

  Banka transferi:
    1. Ali'den 100₺ çık   ✅
    2. Ayşe'ye 100₺ ekle  ❌ (hata!)
    → 1. adım da GERİ ALINIR! Ali'nin parası geri döner. ✅

C — Consistency (Tutarlılık):
  "Veritabanı her zaman geçerli durumda"
  → İş kuralları korunur (bakiye < 0 olamaz, foreign key geçerli, vs.)
  NOT: Aslında bu uygulama sorumluluğu, DB bunu tam garanti edemez

I — Isolation (İzolasyon):
  "Eş zamanlı transaction'lar birbirini GÖRMEMELİ"
  → İki transaction aynı veriyi aynı anda okursa → sanki SERİ çalışmış gibi

D — Durability (Kalıcılık):
  "Commit edilen veri ASLA kaybolmaz"
  → Diske yazıldı, replike edildi, güç kesilse bile korunur
```

### 7.2 İzolasyon Seviyeleri 🔒

Bu bölüm **KRİTİK!** En çok hata yapılan konulardan biri.

#### Read Committed (En yaygın varsayılan)

```
İki garanti:
1. Dirty Read yok: Commit edilmemiş veriyi okuyamazsın
2. Dirty Write yok: Commit edilmemiş verinin üzerine yazamazsın

Dirty Read örneği:
  TX1: UPDATE users SET name='Ali' WHERE id=1;
       -- (henüz COMMIT etmedi!)
  TX2: SELECT name FROM users WHERE id=1;
       -- Read Committed'da: "eski değer" görür ✅
       -- Dirty read'de: "Ali" görür (commit edilmemiş!) ❌

Read Committed'ın çözemediği sorun: Read Skew (Non-repeatable read)

  Ali'nin 2 hesabı: A=500₺, B=500₺ (toplam: 1000₺)

  TX1 (transfer): A'dan B'ye 100₺ aktar
    1. A = A - 100 → A=400
    2. B = B + 100 → B=600
    3. COMMIT

  TX2 (Ali kontrol ediyor):
    1. SELECT A → 500 (TX1 henüz A'yı güncellemedi)
    2. (TX1 çalışır: A=400, B=600, COMMIT)
    3. SELECT B → 600 (TX1 tamamlandı)
    → Ali görür: A=500, B=600, toplam=1100₺ ???
    → Gerçek: A=400, B=600, toplam=1000₺
    → GEÇİCİ TUTARSIZLIK! 😱
```

#### Snapshot Isolation (MVCC) 📸

```
Her transaction, başladığı ANDAKİ veriyi görür.
Transaction sırasında diğerlerinin değişiklikleri GÖRÜNMEZ.

Teknik: Multi-Version Concurrency Control (MVCC)
  → Her satırın birden fazla VERSIYONU tutulur
  → Her transaction kendi "snapshot"ını okur

  TX1 (t=100): BEGIN
  TX2 (t=101): UPDATE users SET name='Ali' WHERE id=1; COMMIT;
  TX1: SELECT name FROM users WHERE id=1;
       → "eski değer" görür! (snapshot t=100'den)
       → TX2'nin değişikliği TX1 için GÖRÜNMEZ ✅

PostgreSQL bu seviyeyi "REPEATABLE READ" olarak sunar.
```

#### Serializable (En güçlü) 🏰

```
Transaction'lar sanki BİRER BİRER çalışmış gibi davranır.
En güçlü garanti, ama en yavaş!

Teknik 1: Gerçekten seri çalıştır (serial execution)
  → Tek thread, tek transaction → Garantili izolasyon!
  → VoltDB, Redis (komut bazlı)
  + Basit, lockless
  - YAVAŞ (tek thread → throughput düşük)
  - Transaction kısa olmalı

Teknik 2: İki Fazlı Kilitleme (2PL — Two-Phase Locking)
  → Yazar okuyucuyu bloklar, okuyucu yazarı bloklar
  → Expanding phase: Kilit al
  → Shrinking phase: Kilit bırak
  + Güvenli
  - ÇOK YAVAŞ (deadlock riski, bekleme)
  - Geleneksel DB'lerin çözümü (MySQL InnoDB)

Teknik 3: Serializable Snapshot Isolation (SSI)
  → Optimistik: Çakışma OLACAĞINI varsayma, oLURSA geri al
  → Transaction çalışır, commit'te kontrol eder:
    "Okuduğum veri hâlâ geçerli mi?"
    Evet → COMMIT ✅
    Hayır → ABORT, tekrar dene ❌
  + Hızlı (çakışma yoksa seri hız)
  + Deadlock yok
  - Çakışma çoksa → çok fazla abort
  → PostgreSQL "SERIALIZABLE" seviyesi bunu kullanır
```

### 7.3 Write Skew ve Phantom 👻

Snapshot Isolation'ın bile çözemediği sorunlar:

```
WRITE SKEW:

Hastane kuralı: En az 1 doktor nöbetçi olmalı.
Şu an: Ali nöbetçi, Ayşe nöbetçi (2 doktor)

TX1 (Ali):
  1. SELECT COUNT(*) FROM doctors WHERE on_call = true; → 2
  2. "2 >= 2, bir kişi çıkabilir" → UPDATE SET on_call = false WHERE name = 'Ali';
  3. COMMIT ✅

TX2 (Ayşe): (AYNI ANDA)
  1. SELECT COUNT(*) FROM doctors WHERE on_call = true; → 2 (snapshot!)
  2. "2 >= 2, bir kişi çıkabilir" → UPDATE SET on_call = false WHERE name = 'Ayşe';
  3. COMMIT ✅

Sonuç: Ali = off, Ayşe = off → HİÇ nöbetçi yok! 💀
Her TX tek başına doğru AMA birlikte YANLIŞ!

Çözüm: SERIALIZABLE izolasyon veya
        SELECT ... FOR UPDATE (kilitleme)
```

```
PHANTOM:

Oda rezervasyonu: 12:00-13:00 arası toplantı odası A boş mu?

TX1: SELECT COUNT(*) FROM reservations
     WHERE room = 'A' AND time BETWEEN '12:00' AND '13:00'; → 0
     INSERT INTO reservations(room, time) VALUES('A', '12:00'); COMMIT ✅

TX2: (Aynı anda) → Aynı sorgu → 0 → Aynı INSERT → COMMIT ✅

Sonuç: Aynı saatte 2 rezervasyon! 💥

Neden? İki TX aynı satırları okudular ama DİĞERİNİN INSERT'ini GÖRMEDİLER.
Olmayan satırları kilitleyemezsin! → PHANTOM problemi

Çözüm: Predicate lock veya index-range lock
```

---

## 8. 🌪️ Dağıtık Sistemlerin Sorunları

> **"Dağıtık bir sistemde HER ŞEY ters gidebilir. Ve GİDECEK."**

### 8.1 Güvenilmez Ağlar 🌐

```
Yerel makinede: Fonksiyon çağrısı → Ya sonuç döner ya exception
Ağ üzerinde: İstek gönderdin → ??? (N tane şey olabilir)

İstek gönderildi → ?
  1. İstek kayboldu (ağ sorunu)
  2. İstek kuyrukta bekliyor (yığılma)
  3. Sunucu çöktü
  4. Sunucu işledi ama cevap kayboldu
  5. Sunucu işledi ama cevap yavaş geliyor

HEPSİ dışarıdan AYNI GÖRÜNÜR: TIMEOUT! ⏱️

→ Timeout'tan sonra ne yapacaksın?
  a) Tekrar dene (retry) → İdempotent mi? Duplicates?
  b) Hatayı raporla → Sunucu aslında çalışıyor olabilir!
  c) Başka sunucuya dene → O da aynı sorunu yaşayabilir
```

### 8.2 Güvenilmez Saatler ⏰

```
Her makinenin kendi saati var ve FARKLI!

NTP (Network Time Protocol) ile senkronize edersin ama:
  - NTP doğruluğu: ~ms seviyesinde (bazen 100ms+ sapma!)
  - Ağ gecikmesi saat senkronizasyonunu bozar
  - Leap second: Beklenmedik 1 saniye eklenebilir
  - VM'lerde saat "durabilir" (VM pause)

Neden önemli?
"Last Write Wins" kullanıyorsan:
  Makine A saati: 10:00:00.100  → Yazma: x = "Ali"
  Makine B saati: 10:00:00.050  → Yazma: x = "Ayşe" (50ms geride!)

  LWW: A'nın saati daha büyük → "Ali" kazanır
  AMA gerçekte Ayşe'nin yazması DAHA SONRA olmuş olabilir!
  → Saat farklarından dolayı VERİ KAYBI! 😱

Çözüm: Lamport Timestamp veya Vector Clock (mantıksal saatler)
  Fiziksel saate GÜVENMEMELİSİN!
```

### 8.3 Gerçek ve Biçimlenmiş Bilgi 🤔

```
Dağıtık sistemde bir şeyi BİLMEK zordur:

"Bu node çöktü mü?"
→ Bilmiyorsun! Belki:
  - Çöktü (gerçekten öldü)
  - Ağ bağlantısı koptu (ama çalışıyor)
  - Çok yavaş (GC pause, disk I/O)
  - Cevap ağda kayboldu

"Bu işlem başarılı oldu mu?"
→ Bilmiyorsun! Cevap gelmedi:
  - İşlem yapıldı ama cevap kayboldu
  - İşlem yapılmadı ve sunucu çöktü
  - İşlem yapılmaya devam ediyor (yavaş)

Çözüm: Quorum kararları 🗳️
  → TEK BİR node'a güvenme
  → Birden fazla node'un ÇOĞUNLUĞU aynı fikirde mi?
  → Çoğunluk (majority): N node'dan ⌈N/2⌉ + 1 onay gerekli
  → 5 node → 3'ü "evet" demelidir
  → 2 node çökse bile karar alabilirsin!
```

### 8.4 Byzantine Faults 🏴‍☠️

```
Normal hata: Node çöker, yavaşlar, cevap vermez → DÜRÜST hata
Byzantine hata: Node YALAN söyler, bozuk veri gönderir → KÖTÜ NİYETLİ

Örnek:
  Node A: "Bakiye = 1000₺"  ← Doğru
  Node B: "Bakiye = 999999₺" ← SAHTE! (hacklendi veya bug)
  Node C: "Bakiye = 1000₺"  ← Doğru
  → 2/3 çoğunluk → 1000₺ doğru

Byzantine Fault Tolerance (BFT):
  → N node'dan en fazla ⌊(N-1)/3⌋ tanesi kötü niyetli olabilir
  → 3f+1 node gerekli (f = kötü niyetli sayısı)
  → Blockchain (Bitcoin, Ethereum) bunu kullanır!

Pratikte: Çoğu şirket BFT kullanmaz → çok pahalı!
  → Sunucularına güvenirler (kendi kontrolleri altında)
  → Sadece blockchain/kripto gibi "güvensiz ortamlarda" gerekli
```

---

## 9. 🤝 Tutarlılık ve Konsensus

### 9.1 Tutarlılık Modelleri

```
EN GÜÇLÜ ─────────────────────────────────── EN ZAYIF
Linearizable → Sequential → Causal → Eventual

Linearizability (Doğrusallaştırılabilirlik): 🏆
  "Tek bir kopya gibi davran"
  Tüm okumalar en güncel yazılan değeri görür.
  Zaman çizgisinde: Yazma tamamlandıktan sonra TÜM okumalar yeni değeri görür.

  ┌─ yazma x=1 ──────────┐
  │                        │
  ────────────────────────────────────→ zaman
               ↑
  Bu noktadan sonra HER okuma x=1 dönmeli!
  │ x=0 │   x=? │   x=1  │   x=1  │
          ← geçiş noktası →

  Pahalı! (Her okuma/yazma koordinasyon gerektirir)
  Ama gerekli olduğu yerler:
    - Lider seçimi (leader election)
    - Kilit servisleri (distributed lock)
    - Benzersizlik kısıtları (unique constraint)

Eventual Consistency (Son Tutarlılık): 🐢
  "Sonunda tutarlı olacak, ama NE ZAMAN belli değil"
  Yazma yapıldıktan sonra okumalar BİR SÜRE eski değeri görebilir.
  Tüm replikalar SONUNDA aynı değere ulaşır.

  Ne zaman yeterli?
    - Sosyal medya beğeni sayısı (birkaç saniye fark OK)
    - Arama motoru indeksi (güncellik o kadar kritik değil)
    - Ürün yorumları
```

### 9.2 CAP Teoremi ⚠️

```
⚠️ ÖNCE KLEPPMANN'IN UYARISI:
"CAP teoremi yaygın olarak yanlış anlaşılır!"

Geleneksel (ve YANILTICI) açıklama:
  C — Consistency (Tutarlılık)
  A — Availability (Kullanılabilirlik)  
  P — Partition Tolerance (Bölünme Toleransı)
  "İkisini seç!" → BU ÇOK BASİT!

KLEPPMANN'IN GERÇEKÇİ açıklaması:
  1. P (Partition Tolerance) SEÇİM değil → ZORUNLU!
     → Ağ bölünmesi OLACAK (kablolar kopar, switch'ler çöker)
     → P'yi "seçmemek" mümkün DEĞİL!
  
  2. Asıl seçim: Bölünme OLDUĞUNDA C mi A mı?
     → CP: Yanlış cevap vermektense hiç cevap verme
     → AP: Eski veri, hiç veri yoktan iyidir

  3. AMA Kleppmann der ki: Daha iyi çerçeve →
     TUTARLILIK vs GECİKME trade-off'u!
     → Bölünme OLMASA BİLE bu trade-off var!
     → Tutarlı okuma istiyorsan → gecikme artabilir (replikasyonu bekle)
     → Hızlı okuma istiyorsan → stale data okuyabilirsin

Pratikte:
  CP → Banka, sağlık, envanter (HBase, MongoDB varsayılan)
  AP → Sosyal medya, arama, sepet (Cassandra, DynamoDB, CouchDB)

  AMA: "Her zaman CP veya her zaman AP" diye sistem YOKTUR!
  → Aynı sistem içinde farklı işlemler farklı trade-off seçebilir!
  → Sipariş: Strong consistency (tutarlı) 
  → Ürün yorumu: Eventually consistent (gecikebilir)
```

### 9.3 Konsensus (Uzlaşma) 🤝

> **"Birden fazla node'un bir değer üzerinde ANLAŞMASI."**

Dağıtık sistemlerin **en temel** ve **en zor** problemi!

```
Konsensus gerekli olduğu durumlar:
  1. Lider seçimi: "Yeni lider kim olacak?"
  2. Atomik commit: "Bu transaction COMMIT mi ABORT mu?"
  3. Kilit alma: "Bu kaynağı KİM kullanabilir?"
  4. Benzersizlik: "Bu kullanıcı adı alınmış MI?"

Konsensus algoritmaları:

Raft (anlaşılır, yaygın):
  - Lider seçimi + log replikasyonu
  - Lider tüm yazmaları yönetir
  - Çoğunluk oyu ile lider seçilir
  - etcd, Consul kullanır

Paxos (teorik temel, karmaşık):
  - Leslie Lamport, 1989
  - Raft'ın esin kaynağı ama daha karmaşık
  - Google Chubby, Spanner buna dayanır

Zab (ZooKeeper Atomic Broadcast):
  - Apache ZooKeeper'ın protokolü
  - Raft'a benzer ama önce geliştirildi
```

```
Raft Algoritması (basitleştirilmiş):

Üç rol: Leader, Follower, Candidate

1. TERM (dönem): Zaman dilimleri
   Term 1: Leader = A
   Term 2: Leader = B (A çöktü, B yeni lider)

2. LEADER SEÇİMİ:
   - Follower, Leader'dan heartbeat almazsa → CANDIDATE olur
   - Diğer node'lara "Beni seç!" (RequestVote) gönderir
   - Çoğunluk (N/2 + 1) oy alırsa → LEADER olur
   - Split vote → Yeni term, yeniden seçim

3. LOG REPLİKASYONU:
   Client → Leader'a yaz
   Leader → Follower'lara replike et
   Çoğunluk onayladıysa → COMMIT
   Client'a "tamam" de

   Leader log: [x=1, y=2, z=3]  ← committed
   Follower 1: [x=1, y=2, z=3]  ← replike edildi ✅
   Follower 2: [x=1, y=2]       ← henüz z=3 ulaşmadı
   Follower 3: [x=1, y=2, z=3]  ← replike edildi ✅
   → 3/4 çoğunluk z=3'ü aldı → COMMIT ✅

Araçlar:
  etcd: Kubernetes'in kalbi (Raft kullanır)
  Consul: Servis keşfi, KV store (Raft)
  ZooKeeper: Dağıtık koordinasyon (Zab)
```

---

# BÖLÜM III — Türetilmiş Veri

---

## 10. ⚙️ Batch Processing

> **"Büyük miktarda biriktirdilmiş veriyi toplu olarak işle."**

### 10.1 Unix Felsefesi → MapReduce

```bash
# Unix pipeline: Basit araçları birleştir
cat access.log |
  awk '{print $7}' |       # URL'yi çıkar
  sort |                    # Sırala
  uniq -c |                 # Tekrar sayısını bul
  sort -rn |                # En çoktan aza sırala
  head -5                   # İlk 5'i göster

# Bu pipeline MILYONLARCA satırı işleyebilir!
# Her araç TEK bir iş yapar (Unix felsefesi)
# Araçlar pipe (|) ile bağlanır
```

Aynı fikir, DAĞITIK ölçekte → **MapReduce**

### 10.2 MapReduce 🗺️

```
Google'ın 2004 makalesi: Dağıtık batch processing

İki aşama:
  MAP → Veriyi (key, value) çiftlerine dönüştür
  REDUCE → Aynı key'li değerleri birleştir

Örnek: Web sayfalarındaki kelime sayımı

Girdi:
  Sayfa 1: "the cat sat on the mat"
  Sayfa 2: "the cat ate the fish"

MAP (her satır için paralel çalışır):
  Sayfa 1 → (the, 1), (cat, 1), (sat, 1), (on, 1), (the, 1), (mat, 1)
  Sayfa 2 → (the, 1), (cat, 1), (ate, 1), (the, 1), (fish, 1)

SHUFFLE (aynı key'leri grupla):
  the  → [1, 1, 1, 1]
  cat  → [1, 1]
  sat  → [1]
  on   → [1]
  mat  → [1]
  ate  → [1]
  fish → [1]

REDUCE (her grup için paralel çalışır):
  the  → 4
  cat  → 2
  sat  → 1
  ...
```

```
MapReduce iş akışı:

  [Girdi dosyaları] → [MAP görevleri] → [SHUFFLE] → [REDUCE görevleri] → [Çıktı]
  HDFS (dağıtık     100 makine         Ağ üzerinden    50 makine         HDFS
  dosya sistemi)     paralel           key'lere göre    paralel
                                        dağıtım

Hadoop MapReduce:
  - Girdi/çıktı: HDFS (Hadoop Distributed File System)
  - Hata toleransı: Görev çökerse başka makinede TEKRAR çalışır
  - Veri yerleşimi: "Veriyi işleme GÖNDERmek yerine, işlemi veriye GÖNDERmek"

Problem:
  - YAVAŞ! Her aşama diske yazar
  - Zincirleme MapReduce (join, çoklu aşama) → ÇOK gidiş-dönüş!
```

### 10.3 MapReduce'un Ötesi: Dataflow Engines

```
Spark, Flink, Tez → MapReduce'un evrimleşmiş hali

MapReduce sorunları:
  1. Her aşama diske yazıyor → YAVAŞ
  2. Sadece Map/Reduce → Karmaşık işlemler için zor
  3. İteratif algoritmalar (ML) için kötü

Spark yaklaşımı:
  - Ara sonuçlar BELLEKTE (disk yerine) → 10-100x hızlı!
  - MAP + REDUCE dışında: filter, join, group, sort...
  - DAG (Directed Acyclic Graph) tabanlı optimizasyon
  - Lazy evaluation: İşlemi planla, sonra çalıştır

Spark örneği (kavramsal):
  tekstGirdi.flatMap(satir => satir.split(" "))   // MAP: kelimeye böl
            .map(kelime => (kelime, 1))             // Her kelime = 1
            .reduceByKey((a, b) => a + b)           // REDUCE: topla
            .sortBy(_._2, ascending=false)          // SIRALA
            .take(10)                               // İlk 10
```

### 10.4 MapReduce'da JOIN Türleri

```
İki veri kümesini birleştirme (join), batch processing'in EN BÜYÜK sorunlarından biri:

Örnek:
  Kullanıcılar: {id: 1, name: "Ali"}, {id: 2, name: "Ayşe"}
  Aktiviteler: {userId: 1, page: "/home"}, {userId: 1, page: "/about"},
               {userId: 2, page: "/home"}

Sort-Merge Join:
  1. Her iki veriyi userId'ye göre SIRALA
  2. Sıralı dolaşarak BİRLEŞTİR
  → Büyük veri setleri için verimli
  → MapReduce'un doğal çözümü

Broadcast Hash Join:
  → Küçük tablo belleğe SIĞIYORSA → Her mapper'a kopyala
  → Büyük tabloyu tarar, küçük tabloyu bellekten arar
  → Ağ trafiği az (küçük tablo broadcast edilir)

Partitioned Hash Join:
  → Her iki tablo da aynı key'e göre partition'lanmış
  → Her partition çifti bağımsız join yapabilir
  → En hızlı ama ön koşul gerektirir
```

---

## 11. 🌊 Stream Processing

> **"Veriyi geldiği ANDA, sürekli olarak işle."**

Batch: Büyük veri → Toplu işle → Sonuç (saatler/günler)
Stream: Veri akar → Anlık işle → Sonuç (milisaniyeler/saniyeler)

### 11.1 Mesaj Broker'ları 📨

```
Producer → [Message Broker] → Consumer

İki tür broker:

1. Mesaj Kuyruğu (RabbitMQ, ActiveMQ):
   → Mesaj bir kez tüketilir ve SİLİNİR
   → İş dağıtımı: 100 görev → 10 worker

   Producer → [RabbitMQ] → Consumer A (mesaj 1, 3, 5...)
                         → Consumer B (mesaj 2, 4, 6...)
   Her mesaj TEK bir consumer tarafından işlenir

2. Log-Based Broker (Apache Kafka):
   → Mesajlar SİLİNMEZ, sırayla LOGLANIR
   → Birden fazla consumer AYNI mesajı okuyabilir
   → Consumer kendi offset'ini takip eder

   Producer → [Kafka Topic: Partition 0] → Consumer Group A (offset: 150)
                                          → Consumer Group B (offset: 120)
                                          → Consumer Group C (offset: 145)

   Her consumer group bağımsız okur!
   Kapasite: Partition sayısını artır → Paralel tüketim ↑
```

### 11.2 Apache Kafka Derinlemesine 📊

```
Kafka mimarisi:

Topic: Bir veri akışı kategorisi (örn: "orders", "user-events")
Partition: Topic'in bölümleri (paralellik birimi)
Offset: Partition içindeki mesaj sıra numarası

Topic "orders" (3 partition):
  Partition 0: [msg0, msg1, msg2, msg3, ...]  ← offset 0, 1, 2, 3...
  Partition 1: [msg0, msg1, msg2, ...]
  Partition 2: [msg0, msg1, msg2, msg3, msg4, ...]

Producer → Hangi partition'a? → hash(key) mod N veya round-robin

Consumer Group:
  Group "order-service":
    Consumer A → Partition 0 okur
    Consumer B → Partition 1 okur
    Consumer C → Partition 2 okur
  → Paralel tüketim! Her partition TEK consumer tarafından okunur (grup içinde)

  Group "analytics-service": (AYNI topic'i okuyan başka grup)
    Consumer D → Partition 0, 1 okur
    Consumer E → Partition 2 okur
  → Her grup BAĞIMSIZ!

Garanti:
  - Partition İÇİNDE sıralama GARANTİ ✅
  - Partition'lar ARASINDA sıralama garanti DEĞİL ⚠️
  - En az bir kez teslim (at-least-once) → İdempotent consumer gerekli!

Kafka'nın gücü:
  - Saklama: Mesajlar silinmez, saatlerce/günlerce/sonsuza kadar tutulabilir
  - Replay: Consumer offset'i geri sararak geçmiş verileri tekrar işleyebilir!
  - Throughput: Milyon mesaj/saniye
```

### 11.3 Olay Tabanlı Mimari (Event-Driven Architecture) 📡

```
Geleneksel: Request-Response
  Sipariş servisi → Ödeme servisi → Stok servisi → Email servisi
  (senkron, bağımlı, yavaş, tek hata tüm zinciri bozar)

Event-Driven: Pub/Sub
  Sipariş servisi → "SiparişOluşturuldu" olayını yayınla
    → Ödeme servisi: Olayı dinler → işler
    → Stok servisi: Olayı dinler → işler
    → Email servisi: Olayı dinler → işler
    → Analytics servisi: Olayı dinler → işler

  + Gevşek bağlı (loose coupling)
  + Her servis bağımsız ölçeklenir
  + Yeni servis eklemek → sadece abone ol, mevcut kodu DEĞİŞTİRME!
  - Eventual consistency (anlık tutarlılık yok)
  - Debugging zor (olay akışını izlemek karmaşık)
```

### 11.4 Event Sourcing 📜

```
Geleneksel: Mevcut durumu tut, üzerine yaz
  users tablosu: {id: 1, name: "Ali", email: "ali@mail.com"}
  UPDATE users SET email = 'ali@yeni.com' WHERE id = 1;
  → ESKİ email KAYBOLDUl!

Event Sourcing: TÜM DEĞİŞİKLİKLERİ kronolojik olarak sakla

  Events tablosu (ASLA DEĞİŞMEZ, sadece EKLE):
  ┌────┬──────────────────┬──────────────────────────────────┬──────────┐
  │ #  │     Event        │          Data                    │  Zaman   │
  ├────┼──────────────────┼──────────────────────────────────┼──────────┤
  │ 1  │ UserCreated      │ {name: "Ali", email: "ali@.."}   │ 10:00    │
  │ 2  │ EmailChanged     │ {oldEmail: "ali@..", new: ".."}  │ 11:30    │
  │ 3  │ NameChanged      │ {oldName: "Ali", new: "Alican"}  │ 14:00    │
  │ 4  │ EmailChanged     │ {old: "ali@yeni", new: "a@.."}   │ 15:45    │
  └────┴──────────────────┴──────────────────────────────────┴──────────┘

  Mevcut durumu hesapla: Event 1'den başla, sırayla uygula → son durum!
  Herhangi bir ANDAKİ durumu hesapla: İlk N event'i uygula → o andaki durum!

  + Tam denetim izi (audit trail) — "Kim, ne zaman, ne değiştirdi?"
  + Zaman yolculuğu — "3 ay önceki durum neydi?"
  + Bug düzeltme — Kodu düzelt, event'leri tekrar oynat → düzeltilmiş durum!
  - Karmaşıklık
  - Event miktarı çok büyüyebilir → snapshot'lar gerekli
```

### 11.5 CQRS (Command Query Responsibility Segregation) 📖✏️

```
CQRS: Okuma ve yazma modellerini AYIR

Geleneksel:
  [Aynı Model] ←--- OKUMA (SELECT) + YAZMA (INSERT/UPDATE)
  → İkisi de aynı tablo yapısını kullanır

CQRS:
  YAZMA (Command) → [Write Model / Event Store]
                              ↓ (event projeksiyonu)
  OKUMA (Query)   → [Read Model / Materialized View]

Örnek: E-ticaret ürün sayfası

  Write Model (Events):
    PriceChanged, StockUpdated, ReviewAdded, ...

  Read Model (Optimized for UI):
    {
      productId: "abc",
      name: "Laptop",
      price: 15000,
      stockCount: 42,
      averageRating: 4.3,
      reviewCount: 128,
      topReviews: [...]
    }

  → Yazma modeli NORMALIZE (clean, tutarlı)
  → Okuma modeli DENORMALIZE (hızlı, UI'a özel)
  → Her iki model bağımsız optimize edilir!
```

### 11.6 Stream Processing'de Zaman ⏱️

```
İki tür zaman:

1. Event Time: Olay GERÇEKTE ne zaman oldu?
   → Cihazın saati (ama saatler güvenilmez!)

2. Processing Time: Olay SİSTEME ne zaman geldi?
   → Sunucu saati (ama gecikmeli olabilir!)

Neden önemli?
  Kullanıcı uçakta offline alışveriş yaptı (event time: 14:00)
  İnternete bağlanınca sistem aldı (processing time: 18:00)
  → "Saat 14-15 arası alışveriş sayısı" hesabında HANGISINI kullanacaksın?

Geç gelen veriler (late events):

  Pencere: 14:00-15:00 arası satışlar
  14:58'de yapılan satış → 15:05'te ulaşır (ağ gecikmesi)
  Pencere zaten KAPANDI! Ne yapacaksın?

  a) Görmezden gel → Hatalı sonuç!
  b) Pencereyi UZUN SÜre aç → Gecikme artar
  c) Watermark: "Artık 14:00-15:00 arasından veri GELMEYECEK" tahmini
     → Watermark geçtikten sonra pencereyi kapat
     → Ama geç gelenler için "geç çıktı" (late output) üret
```

### 11.7 Stream İşleme Türleri

```
1. Event-at-a-time: Her olayı tek tek işle
   → Basit, düşük gecikme
   → Durum yönetimi zor

2. Micro-batching: Küçük gruplar halinde işle (Spark Streaming)
   → Her 500ms bir batch → toplu işle
   → Throughput iyi, ama minimum gecikme = batch süresi

3. Windowing: Zaman pencereli işleme

   Tumbling Window (Sıralı pencere):
   |--10dk--|--10dk--|--10dk--|
   Her olay TEK pencereye ait

   Sliding Window (Kayan pencere):
   |--10dk--|
       |--10dk--|
           |--10dk--|
   Pencereler örtüşür

   Session Window (Oturum penceresi):
   |---Session 1---|  (boşluk)  |---Session 2---|
   Aktivite arasındaki boşluğa göre grupla
   Kullanıcı 5dk inaktif → oturum sona erdi
```

---

## 12. 🔮 Veri Sistemlerinin Geleceği

### 12.1 Veri Entegrasyonu

```
Gerçek dünyada: BİRDEN FAZLA veri sistemi kullanırsın

  PostgreSQL (ana veri kaynağı)
       ↓ CDC (Change Data Capture)
  Kafka (olay akışı)
       ↓           ↓            ↓
  Elasticsearch   Redis      Data Warehouse
  (arama)         (cache)    (analitik)

CDC: Veritabanındaki her değişikliği yakalayıp
     diğer sistemlere gerçek zamanlı ilet
     → PostgreSQL WAL'dan okuyarak
     → MySQL binlog'dan okuyarak

Araçlar: Debezium, Maxwell, pgoutput
```

### 12.2 Lambda Mimarisi vs Kappa Mimarisi

```
Lambda Mimarisi:
  Toplu (Batch) ve akış (Stream) işlemeyi BİRLİKTE kullan

     [Ham Veri]
        ↓
  ┌────────────┐     ┌──────────────┐
  │ Batch Layer │     │ Speed Layer  │
  │ (MapReduce) │     │ (Stream)     │
  │ Doğru ama   │     │ Hızlı ama    │
  │ yavaş       │     │ yaklaşık     │
  └─────┬──────┘     └──────┬───────┘
        │                    │
        └────────┬───────────┘
                 ↓
         [Serving Layer]
         Sorguları cevapla

  - İki ayrı sistem, iki ayrı kod → BAKIMI ZOR
  - Sonuçları birleştirmek karmaşık

Kappa Mimarisi (Jay Kreps / Kafka yaratıcısı):
  HER ŞEYİ stream olarak işle!

  [Ham Veri] → [Kafka] → [Stream Processing] → [Serving Layer]

  "Batch" gerekiyorsa: Kafka'daki eski verileri tekrar oynat!

  + Tek kod tabanı
  + Basit mimari
  - Çok büyük geçmiş veri için Kafka depolama maliyeti yüksek
```

### 12.3 Doğruluk ve Etik

Kleppmann kitabın sonunda felsefi sorular sorar:

```
1. EXACTLY-ONCE DELIVERY (Tam bir kez teslim):
   Aslında imkansız! Ama "effectively once" mümkün:
   → İdempotent işlemler (aynı işlemi N kez yapsan bile sonuç aynı)
   → Deduplication (duplicate ID ile tekrarı engelle)

2. DOĞRULUK vs PERFORMANS:
   Her zaman trade-off var:
   → Tutarlılık ↑ → Performans ↓
   → Kullanılabilirlik ↑ → Tutarlılık ↓
   → Doğru seçim: İŞ GEREKSİNİMİNE göre karar ver

3. VERİ ETİĞİ:
   → Toplanan her veri bir sorumluluktur
   → GDPR, KVKK → Kullanıcı hakkı: verilerini SİL
   → Event Sourcing kullanıyorsan → "silme" = silme EVENT'i ekle
     Ama eski event'lerdeki veri hâlâ var!
     → Crypto shredding: Veriyi şifreli sakla, silme = anahtarı sil
```

---

## 🏆 Büyük Tablo: Her Şeyin Özeti

```
┌──────────────────┬───────────────────┬──────────────────────────────────┐
│ Kavram           │ Seçenekler        │ Trade-off                        │
├──────────────────┼───────────────────┼──────────────────────────────────┤
│ Veri Modeli      │ SQL / Document /  │ Esneklik vs Tutarlılık           │
│                  │ Graph             │                                  │
│ Depolama Engine  │ B-Tree / LSM-Tree │ Okuma hızı vs Yazma hızı        │
│ Replikasyon      │ Leader / Multi /  │ Tutarlılık vs Kullanılabilirlik  │
│                  │ Leaderless        │                                  │
│ Partitioning     │ Key Range / Hash  │ Range scan vs Eşit dağılım      │
│ Transaction      │ ACID / BASE      │ Doğruluk vs Performans           │
│ İzolasyon        │ Read Committed /  │ Güvenlik vs Hız                  │
│                  │ Snapshot / Serial │                                  │
│ Tutarlılık       │ Linearizable /    │ Gecikme vs Tutarlılık            │
│                  │ Eventual          │                                  │
│ Processing       │ Batch / Stream    │ Gecikme vs Doğruluk              │
│ Encoding         │ JSON / Protobuf / │ İnsan okunabilir vs Verimlilik   │
│                  │ Avro              │                                  │
└──────────────────┴───────────────────┴──────────────────────────────────┘
```

```
HER KARARDA SOR:

1. "Ne kadar VERİ tutarlılığı lazım?"
   → Banka = güçlü, Sosyal medya = eventual

2. "Ne kadar GECİKME kabul edilebilir?"
   → Trading = μs, Analitik = dakikalar

3. "Ne BOZULURSA ne olur?"
   → Veri kaybı kabul edilebilir mi?
   → Geçici tutarsızlık tolere edilebilir mi?

4. "Nasıl ÖLÇEKLENECEK?"
   → 1000 kullanıcı → 1M kullanıcı → 1B kullanıcı?
   → Okuma ağırlıklı mı, yazma ağırlıklı mı?
```

### 🤖 2024+ Güncellemeleri ve AI Bağlantısı

```
Kleppmann'ın kitabı 2017'de yazıldı. O zamandan beri:

YENI DEPOLAMA MOTORLARI:
  → Vector Databases (Pinecone, Weaviate, pgvector, Qdrant)
    → B-Tree/LSM-Tree yanına YENİ bir kategori eklendi!
    → AI embedding'lerini saklamak ve KNN araması yapmak için
    → DDIA'daki storage engine prensipleri HÂLÂ geçerli!

  → NewSQL gelişimi (CockroachDB, TiDB, YugabyteDB)
    → "SQL ölçeklenemez" → YANLIŞ! Distributed SQL mümkün!
    → Spanner konseptini open-source dünyasına taşıdılar

RAG PIPELINE'LARI → DDIA PRENSİPLERİ UYGULAMADA:
  → Batch Processing: Belgeleri embedding'e çevir (DDIA Ch.10!)
  → Stream Processing: Yeni belge geldiğinde anında embedding (Ch.11!)
  → Derived Data: Vector index = materialized view! (Ch.12!)
  → DDIA okumuş biri RAG mimarisini DOĞAL anlar!

FEATURE STORES (Feast, Tecton):
  → CQRS + Materialized View'un pratikte UYGULANMASI!
  → ML modeli eğitimi için: batch computed features
  → Real-time inference: stream-computed features
  → DDIA Ch.12 "unbundling databases" → TAM OLARAK BU!

KAFKA ALTERNATİFLERİ:
  → Redpanda (Kafka API uyumlu, C++ ile yazılmış, daha hızlı)
  → Apache Pulsar (multi-tenancy, tiered storage)
  → Ama PRENSIPLER aynı → log-based messaging değişmedi!

ETİK → AI ÇAĞINDA DAHA DA ÖNEMLİ!
  → Kleppmann'ın etik uyarıları:
    "Veri toplayan her sistem güç asimetrisi yaratır"
  → AI modelleri kişisel veriden öğreniyor → mahremiyet!
  → Bias in, bias out → veri kalitesi = model kalitesi
  → GDPR, AI Act → regulation ARTIYOR, engineer'ın bilmesi ŞART!
```

### Öğrenme Yolculuğu 🛤️

```
📗 Grokking Algorithms           → Algoritma temeli ✅
📕 Clean Code                    → Kod kalitesi ✅
📘 The Pragmatic Programmer      → Mühendislik zihniyeti ✅
📙 The Missing README            → Kariyer temeli ✅
📗 A Philosophy of Software Design → Tasarım felsefesi ✅
📘 Head First Design Patterns    → Pattern'lar ✅
📕 Designing Data-Intensive Apps → Dağıtık sistem temeli ✅  ← BURADASIN

Sıradaki (Faz 2 sonu):
📙 Unit Testing (Khorikov)       → Test stratejisi
📗 Refactoring (Fowler)          → Referans kitap
```

---

> **"Veri mühendisliğinde mükemmel çözüm YOKTUR.
> Sadece trade-off'lar vardır.
> Beceri, hangi trade-off'un SENİN durumuna uygun olduğunu BİLMEKTİR.
> Bu kitabı okuyan biri artık şunu sorar:
> 'Hangi teknolojiyi kullanmalıyım?' değil,
> 'Bu kararın SONUÇLARI ne olur?'
> İşte BU, bir mühendisi teknisyenden ayıran şeydir."** 🧠
>
> — Bu rehberin özü: **"Her şey bir trade-off. Önemli olan, hangi trade-off'u
> BİLİNÇLİ olarak seçtiğini bilmektir."**
