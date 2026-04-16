# 📚 Grokking Algorithms — Türkçe Kapsamlı Rehber

> **"Grokking"** kelimesi "bir şeyi derinden, sezgisel olarak anlamak" demek.
> Bu rehber, Aditya Bhargava'nın kitabını Türkçe olarak, hikayeler ve örneklerle anlatır.

---

## 📖 İçindekiler

1. [Giriş: Algoritma Nedir?](#1--giriş-algoritma-nedir)
2. [Binary Search (İkili Arama)](#2--binary-search-i̇kili-arama)
3. [Big O Notation (Büyük O Notasyonu)](#3--big-o-notation-büyük-o-notasyonu)
4. [Selection Sort (Seçmeli Sıralama)](#4--selection-sort-seçmeli-sıralama)
5. [Recursion (Özyineleme)](#5--recursion-özyineleme)
6. [Quicksort (Hızlı Sıralama)](#6--quicksort-hızlı-sıralama)
7. [Hash Tables (Hash Tabloları)](#7--hash-tables-hash-tabloları)
8. [Breadth-First Search — BFS (Genişlik Öncelikli Arama)](#8--breadth-first-search--bfs-genişlik-öncelikli-arama)
9. [Dijkstra's Algorithm (Dijkstra Algoritması)](#9--dijkstras-algorithm-dijkstra-algoritması)
10. [Greedy Algorithms (Açgözlü Algoritmalar)](#10--greedy-algorithms-açgözlü-algoritmalar)
11. [Dynamic Programming (Dinamik Programlama)](#11--dynamic-programming-dinamik-programlama)
12. [K-Nearest Neighbors — KNN (K En Yakın Komşu)](#12--k-nearest-neighbors--knn-k-en-yakın-komşu)
13. [Sonraki Adımlar](#13--sonraki-adımlar)

---

## 1. 🌟 Giriş: Algoritma Nedir?

### Hikaye Zamanı 🎬

Diyelim ki sabah uyandın ve kahvaltı yapacaksın. Kafanda şu adımlar var:

1. Mutfağa git
2. Buzdolabını aç
3. Yumurtaları çıkar
4. Tavayı ocağa koy
5. Yağ ekle
6. Yumurtaları kır
7. Pişir
8. Tabağa al

İşte bu bir **algoritma**! 🎉

> **Algoritma** = Bir problemi çözmek için izlenen adım adım talimatlar dizisi.

Yani algoritma süslü, korkutucu bir kelime değil. Sen zaten her gün yüzlerce algoritma kullanıyorsun:
- Google Maps'te yol tarifi alıyorsun → **en kısa yol algoritması**
- Netflix sana film öneriyor → **öneri algoritması**
- Instagram feed'in sıralanıyor → **sıralama algoritması**

### Peki Neden Öğrenmeliyiz? 🤔

Çünkü aynı problemi çözmenin **yüzlerce yolu** var, ama bazıları diğerlerinden **katbekat daha hızlı**.

Düşün: İstanbul'dan Ankara'ya gideceksin.
- 🐌 Yürüyerek: ~50 saat
- 🚗 Arabayla: ~4.5 saat
- ✈️ Uçakla: ~1 saat

Üçü de seni Ankara'ya götürür. Ama hangisi daha **verimli**?

İşte algoritmalar da böyle. Doğru algoritmayı seçmek, kodunun 1 saniyede mi yoksa 1 saatte mi çalışacağını belirler.

---

## 2. 🔍 Binary Search (İkili Arama)

### Problem: Sözlükte Kelime Aramak 📕

Diyelim ki elinde 100.000 kelimelik bir İngilizce sözlük var ve "python" kelimesini arıyorsun.

**Yöntem 1: Sırayla aramak (Linear Search)** 🐌
Sayfa 1'den başla, her sayfaya tek tek bak.
- En kötü ihtimalle 100.000 kez bakarsın
- Ortalama 50.000 kez bakarsın

**Yöntem 2: Akıllıca aramak (Binary Search)** 🧠
Sözlüğü ortadan aç!
- "Python" P harfiyle başlıyor
- Ortası M harfi civarı. P, M'den sonra gelir → sağ yarıya bak
- Sağ yarının ortası R civarı. P, R'den önce gelir → sol yarıya bak
- Böyle devam et...

Her adımda **yarısını eliyorsun**!

### Nasıl Çalışır? Adım Adım 👣

Diyelim ki 1'den 100'e kadar sıralı sayılar var. Bilgisayar bir sayı tuttu: **67**.

```
Adım 1: Ortayı kontrol et → 50
         67 > 50 → Sağ yarıya bak (51-100)

Adım 2: Ortayı kontrol et → 75
         67 < 75 → Sol yarıya bak (51-74)

Adım 3: Ortayı kontrol et → 62
         67 > 62 → Sağ yarıya bak (63-74)

Adım 4: Ortayı kontrol et → 68
         67 < 68 → Sol yarıya bak (63-67)

Adım 5: Ortayı kontrol et → 65
         67 > 65 → Sağ yarıya bak (66-67)

Adım 6: Ortayı kontrol et → 66
         67 > 66 → Sağ yarıya bak (67-67)

Adım 7: Kontrol et → 67 ✅ BULDUK!
```

**100 elemanda sadece 7 adım!** Sırayla arasan en kötü 100 adım olurdu.

### 🔢 Matematiksel Güzellik

| Eleman Sayısı | Linear Search (En Kötü) | Binary Search (En Kötü) |
|---|---|---|
| 100 | 100 adım | 7 adım |
| 1.000 | 1.000 adım | 10 adım |
| 1.000.000 | 1.000.000 adım | 20 adım |
| 1.000.000.000 | 1 milyar adım 😱 | 30 adım 😎 |

> **1 milyar elemanda sadece 30 adım!** Çünkü her adımda yarısını eliyoruz:
> $2^{30} = 1.073.741.824$ (yaklaşık 1 milyar)

### Kod Örneği (JavaScript) 💻

```javascript
function binarySearch(list, target) {
  let low = 0;                    // En düşük index
  let high = list.length - 1;     // En yüksek index

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);  // Ortayı bul
    const guess = list[mid];                     // Ortadaki eleman

    if (guess === target) {
      return mid;          // 🎉 Bulduk! Index'ini döndür
    }

    if (guess > target) {
      high = mid - 1;      // ⬅️ Tahmin büyük, sol yarıya bak
    } else {
      low = mid + 1;       // ➡️ Tahmin küçük, sağ yarıya bak
    }
  }

  return -1;  // 😢 Bulunamadı
}

// Kullanım:
const numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
console.log(binarySearch(numbers, 7));   // Output: 3 (index)
console.log(binarySearch(numbers, 12));  // Output: -1 (yok)
```

### ⚠️ Kritik Kural

Binary Search **SADECE sıralı (sorted) listelerde** çalışır!

Sırasız bir listede binary search yapmak, alfabetik olmayan bir sözlükte kelime aramak gibidir — imkansız! 🤷

### 🧠 Akılda Kalası Özet

> Sıralı bir listede bir şey arıyorsan, **ortadan başla ve her seferinde yarısını ele.**
> Bu sana logaritmik hız kazandırır: $O(\log n)$

---

## 3. 📐 Big O Notation (Büyük O Notasyonu)

### Hikaye: Pizza Siparişi 🍕

İki pizza dükkanı var:
- **Dükkan A**: Her pizza 10 dakika, kaç pizza olursa olsun → 10 pizza = 100 dk
- **Dükkan B**: İlk pizzayı 1 dakikada yapar, ama sonraki her pizza öncekinin 2 katı sürer → 10 pizza = 1 + 2 + 4 + 8 + ... = 1023 dk 🤯

1 pizza siparişinde ikisi de hızlı. Ama 20 pizza sipariş edersen? Dükkan B'de **ölürsün** ☠️

İşte Big O Notation, bir algoritmanın **eleman sayısı arttıkça ne kadar yavaşlayacağını** söyler.

### Big O Ne Demek?

Big O, algoritmanın **en kötü senaryodaki** performansını ifade eder. "Bu algoritma EN FAZLA şu kadar iş yapar" der.

> **Soruyu şöyle sor:** "Eleman sayısı 10'dan 10.000'e çıkınca, bu algoritma ne kadar daha yavaşlar?"

### Yaygın Big O Süreleri (Yavaştan Hızlıya) 🏎️

| Big O | İsim | Açıklama | Örnek |
|---|---|---|---|
| $O(1)$ | **Constant** (Sabit) | Eleman sayısı ne olursa olsun aynı süre | Array'den index ile eleman almak |
| $O(\log n)$ | **Logarithmic** (Logaritmik) | Her adımda problem yarıya iniyor | Binary Search |
| $O(n)$ | **Linear** (Doğrusal) | Her eleman için bir iş | Listeyi baştan sona taramak |
| $O(n \log n)$ | **Linearithmic** | Verimli sıralama algoritmaları | Quicksort, Merge Sort |
| $O(n^2)$ | **Quadratic** (Karesel) | Her eleman için tüm listeyi taramak | İç içe iki döngü, Selection Sort |
| $O(2^n)$ | **Exponential** (Üstel) | Her eleman problem boyutunu ikiye katlıyor | Tüm alt kümeleri bulma |
| $O(n!)$ | **Factorial** (Faktöriyel) | Tüm permütasyonları deneme | Gezgin satıcı problemi (brute force) |

### Görsel Karşılaştırma 📊

10 elemanlı bir listede:
```
O(1)       → 1 işlem          ⚡
O(log n)   → ~3 işlem         🏃
O(n)       → 10 işlem         🚶
O(n log n) → ~33 işlem        🐕
O(n²)      → 100 işlem        🐢
O(2ⁿ)      → 1.024 işlem      🐌
O(n!)      → 3.628.800 işlem  💀
```

1.000 elemanlı bir listede:
```
O(1)       → 1 işlem                    ⚡
O(log n)   → ~10 işlem                  🏃
O(n)       → 1.000 işlem                🚶
O(n log n) → ~10.000 işlem              🐕
O(n²)      → 1.000.000 işlem            🐢
O(2ⁿ)      → Evrenin ömrü yetmez 🤯    💀
O(n!)      → ... 🪦                     ⚰️
```

### Gerçek Hayat Analojileri 🎭

| Big O | Analoji |
|---|---|
| $O(1)$ | **Işık düğmesine basmak.** Odada 1 kişi olsun 100 kişi olsun, aynı sürede ışığı açarsın. |
| $O(\log n)$ | **Sözlükte kelime aramak.** Ortadan açıp yarıya bölüyorsun. |
| $O(n)$ | **Kuyrukta beklemek.** Öndeki herkes işini bitirene kadar bekliyorsun. |
| $O(n^2)$ | **Sınıftaki herkes birbiriyle tokalaşıyor.** 30 kişi varsa $30 \times 29 = 870$ tokalaşma! |
| $O(n!)$ | **Yemek masasında herkesin oturma düzenini deniyorsun.** 10 kişi = 3.628.800 farklı düzen! |

### Önemli Kurallar ✅

1. **Sabitler önemsizdir:**
   $O(2n)$ → $O(n)$ yazılır. Çünkü 10x büyüme ile 20x büyüme arasındaki fark, $n$ çok büyüyünce anlamsızlaşır.

2. **Küçük terimler önemsizdir:**
   $O(n^2 + n)$ → $O(n^2)$ yazılır. Çünkü $n$ büyüyünce $n^2$ yanında $n$ ihmal edilebilir.

3. **En kötü senaryoyu düşün:**
   Bir listede eleman arıyorsan, şanslıysan ilk elemanda bulursun. Ama Big O **en kötü** durumu söyler.

### 🧠 Akılda Kalası Özet

> Big O, algoritmanın **büyüme hızını** ölçer, kesin süresini değil.
> Aynı şeyi daha hızlı yapan algoritmayı seçmeni sağlar.
> **"Eleman sayısı arttıkça ne olur?"** sorusunun cevabıdır.

---

## 4. � Diziler vs Bağlı Listeler (Arrays vs Linked Lists)

### Bellekte Nasıl Saklanır? 🧠

Veri yapılarını anlamak için önce bilgisayarın **belleğini** anlamalısın.

Belleği bir sinema salonu gibi düşün 🎬:

```
Bellek = Dev bir koltuk sırası

  [_][_][_][KOL][_][_][KOL][KOL][_][_][_][_][KOL]...

  Her kutucuk = 1 bellek adresi
  KOL = dolu (başka veri var)
  _   = boş (kullanılabilir)
```

### Array (Dizi) — Sinema'da Yan Yana Oturmak 🎬

Array'de elemanlar bellekte **yan yana** oturur.

5 arkadaşsınız, sinemaya gittiniz → "Hepimiz yan yana oturmalıyız!"

```
Dizi: [Ali][Ayşe][Veli][Can][Deniz]
       100   101   102  103   104    ← ardışık bellek adresleri

→ Herhangi birine GİTMEK çok hızlı!
→ "103 numaraya git" → Can'ı ANINDA buldun → O(1)

→ AMA 6. arkadaş geldi → yan yana YER YOK!
→ Herkesi BAŞKA BİR SIRAYA taşımalısın → O(n) 😫
```

| İşlem | Performans | Neden |
|---|---|---|
| **Okuma** (index ile) | O(1) ✅ | Direkt adrese git |
| **Ekleme (sona)** | O(1)* | Yer varsa hızlı (*yer yoksa O(n)) |
| **Ekleme (başa/ortaya)** | O(n) ❌ | Diğer elemanları kaydır |
| **Silme** | O(n) ❌ | Boşluğu kapat, kaydır |

### Linked List (Bağlı Liste) — Sinema'da Dağınık Oturmak 🍿

Linked list'te elemanlar bellekte **dağınık** oturur. Her eleman bir sonrakinin adresini bilir.

```
[Ali|→204]  [Ayşe|→180]  [Veli|→310]  [Can|→422]  [Deniz|null]
  addr:100    addr:204     addr:180     addr:310     addr:422

→ Ali der ki: "Ayşe 204'te oturuyor"
→ Ayşe der ki: "Veli 180'de oturuyor"
→ ...
→ Deniz der ki: "Benden sonra kimse yok (null)"

→ 6. arkadaş geldi → HERHANGİ BİR boş koltuğa otur!
→ Son kişi yeni kişinin adresini bilsin → O(1) ekleme! ✅

→ AMA Can'ı bulmak için? Ali → Ayşe → Veli → Can
→ 3 adım gerekti → O(n) okuma 😫
```

| İşlem | Performans | Neden |
|---|---|---|
| **Okuma** (index ile) | O(n) ❌ | Baştan sırıyla git |
| **Ekleme (başa)** | O(1) ✅ | Yeni düğüm → eski head'e bağla |
| **Ekleme (ortaya/sona)** | O(n)* | (*Tail pointer varsa sona O(1)) |
| **Silme** | O(1)* | (*Düğümü biliyorsan, pointer güncelle) |

### Karşılaştırma Tablosu 📊

```
                    Array           Linked List
  Okuma:            O(1) ⭐         O(n)
  Ekleme (başa):    O(n)            O(1) ⭐
  Ekleme (sona):    O(1)*           O(1)*
  Silme:            O(n)            O(1)*
  Bellek:           Kompakt ⭐      Ekstra (pointer)
  Cache:            İyi ⭐          Kötü

  * koşullara bağlı

  NE ZAMAN HANGİSİ?
  → Çok okuma, az yazma → ARRAY (veritabanı index'i)
  → Çok ekleme/silme    → LINKED LIST (event queue)
  → Random access lazım → ARRAY
  → Boyut belirsiz      → LINKED LIST
```

### JavaScript'te Bu Fark 🤔

JavaScript'in `Array`'i aslında GERÇEK bir array değil — her ikisinin de avantajlarını taşıyan dinamik bir yapıdır. Ama motorun altında bu ayrım HÂLÂ geçerli!

```javascript
// JavaScript array'i (dinamik, ama temelde array benzeri)
const arr = [1, 2, 3, 4, 5];
arr[2];           // O(1) ← index ile erişim hızlı
arr.unshift(0);   // O(n) ← başa ekleme yavaş (hepsini kaydırır!)
arr.push(6);      // O(1) ← sona ekleme hızlı

// Linked List (JavaScript'te kendin yaparsın)
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  // Başa ekleme — O(1)!
  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
  }
}
```

> 🧠 **Bu ayrım neden önemli?**
> Bir veritabanı engine'i yazıyorsan → array tabanlı B-Tree kullanırsın (okuma hızlı).
> Bir message queue yazıyorsan → linked list tabanlı yapı kullanırsın (ekleme/silme hızlı).
> **Doğru veri yapısı = doğru performans!**

---

## 5. �🗂️ Selection Sort (Seçmeli Sıralama)

### Hikaye: Spotify Playlist'ini Sıralamak 🎵

Diyelim ki Spotify'da en çok dinlediğin 5 şarkı var, ama karışık sırada:

```
[148 dinlenme, 35 dinlenme, 291 dinlenme, 72 dinlenme, 15 dinlenme]
```

En çok dinlenenden en aza sıralamak istiyorsun.

### Selection Sort Nasıl Çalışır?

**Adım 1:** Tüm listeyi tara, en büyüğünü bul → 291
Onu yeni listenin başına koy.
```
Eski: [148, 35, 72, 15]
Yeni: [291]
```

**Adım 2:** Kalan listeyi tara, en büyüğünü bul → 148
```
Eski: [35, 72, 15]
Yeni: [291, 148]
```

**Adım 3:** Kalan listeyi tara, en büyüğünü bul → 72
```
Eski: [35, 15]
Yeni: [291, 148, 72]
```

**Adım 4:** Kalan listeyi tara, en büyüğünü bul → 35
```
Eski: [15]
Yeni: [291, 148, 72, 35]
```

**Adım 5:** Son kalan eleman → 15
```
Yeni: [291, 148, 72, 35, 15] ✅
```

### Performance Analizi 🔬

- İlk turda n eleman kontrol ediyorsun
- İkinci turda n-1
- Üçüncü turda n-2
- ...
- Toplam: $n + (n-1) + (n-2) + ... + 1 = \frac{n \times (n-1)}{2}$

Bu da $O(n^2)$ demek. Yani **yavaş** bir algoritma! 🐢

> 💡 **"Ama n²/2 değil mi? 2'ye bölüyoruz, daha hızlı olmuyor mu?"**
> Hayır! Big O sabit katsayıları ATAR. $n^2/2$ ile $n^2$ arasında Big O farkı yok.
> $O(n^2/2) = O(n^2)$. Aradaki 2x fark, n büyüdükçe önemsizleşir.
> Bu, mülakatlarla da sıkça sorulan bir tuzak sorudur! 🎯

5 elemanda sorun yok. Ama 1.000.000 elemanda? $10^{12}$ işlem = **saatler sürer.**

### Kod Örneği (JavaScript) 💻

Hikayede büyükten küçüğe sıraladık. Kodda ise küçükten büyüğe sıralıyoruz (en yaygın yöntem). Mantık aynı — sadece yön değişir:

```javascript
function findSmallestIndex(arr) {
  let smallest = arr[0];
  let smallestIndex = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < smallest) {
      smallest = arr[i];
      smallestIndex = i;
    }
  }
  return smallestIndex;
}

function selectionSort(arr) {
  const sorted = [];
  const copy = [...arr];       // Orijinal diziyi bozmamak için kopya

  while (copy.length > 0) {
    const smallestIdx = findSmallestIndex(copy);
    sorted.push(copy.splice(smallestIdx, 1)[0]);  // En küçüğü çıkar, yeni diziye ekle
  }

  return sorted;
}

console.log(selectionSort([64, 25, 12, 22, 11]));
// Output: [11, 12, 22, 25, 64]
```

### Neden Bu Kadar Önemli? 🤷

Selection Sort pratikte pek kullanılmaz (çünkü yavaş). Ama şu kavramları öğretir:
- **Sıralama problemi** nedir
- **Nested loop** (iç içe döngü) neden $O(n^2)$ olur
- Daha iyi algoritmaların (Quicksort gibi) neden önemli olduğunu anlamak için bir **baseline**

### 🧠 Akılda Kalası Analoji

> Selection Sort, bir sınıftaki öğrencileri boya göre dizmek gibidir.
> "En uzunu bul, öne geçir. Kalanlardan en uzunu bul, ikinci sıraya koy..."
> İşe yarar ama 1000 öğrenci olunca çok yorulursun! 😅

---

## 5. 🔄 Recursion (Özyineleme)

### Hikaye: Büyükannenin Sandığı 📦

Büyükannen sana dedi ki: "Sandığın içinde bir anahtar var."

Sandığı açtın. İçinde:
- 📦 Daha küçük bir kutu
- 📦 Bir başka kutu
- 🔑 Ah hayır, anahtar yok

Daha küçük kutuyu açtın:
- 📦 Daha da küçük bir kutu
- 🔑 Yine yok

En küçük kutuyu açtın:
- 🔑 **ANAHTAR BURADA!** 🎉

İşte recursion budur: **Problem kendini tekrar eden daha küçük versiyonlar içerir ve en sonunda bir "temel durum"a ulaşırsın.**

### İki Yaklaşım: Döngü vs Recursion

**Döngü (Loop) yaklaşımı:**
```
Bir kutu yığını oluştur.
Yığında kutu varken:
  Bir kutu al, aç.
  İçindeki her şey için:
    Eğer kutu ise → yığına ekle
    Eğer anahtar ise → BULDUN! Dur.
```

**Recursion yaklaşımı:**
```
Kutuyu aç.
İçindeki her şey için:
  Eğer kutu ise → AÇ (kendini çağır!)
  Eğer anahtar ise → BULDUN! Dur.
```

### Recursion'ın İki Şartı ✌️

Her recursive fonksiyonun **iki** vazgeçilmez parçası var:

1. **Base Case (Temel Durum):** Fonksiyonun durduğu nokta. "Artık kendimi çağırmama gerek yok."
2. **Recursive Case (Özyinelemeli Durum):** Fonksiyonun kendini tekrar çağırdığı nokta.

Base case olmazsa ne olur? **Sonsuz döngü!** Stack overflow! 💥

### Klasik Örnek: Geri Sayım ⏳

```javascript
function geriSayim(sayi) {
  // Base case: Durma noktası
  if (sayi <= 0) {
    console.log("🚀 KALKIŞ!");
    return;
  }

  // Recursive case: Kendini çağır
  console.log(sayi);
  geriSayim(sayi - 1);
}

geriSayim(5);
// 5
// 4
// 3
// 2
// 1
// 🚀 KALKIŞ!
```

### Klasik Örnek: Faktöriyel Hesaplama

$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$

Ama bunu şöyle de düşünebilirsin:
$5! = 5 \times 4!$
$4! = 4 \times 3!$
$3! = 3 \times 2!$
$2! = 2 \times 1!$
$1! = 1$ ← **Base case!**

```javascript
function faktoriyel(n) {
  // Base case (0! = 1, 1! = 1)
  if (n <= 1) return 1;

  // Recursive case
  return n * faktoriyel(n - 1);
}

console.log(faktoriyel(5)); // 120
```

### Çağrı Yığını (Call Stack) 📚

Bilgisayar recursive çağrıları bir **yığın (stack)** yapısında tutar. Her çağrı yığının üstüne eklenir, tamamlanınca çıkar.

```
faktoriyel(5) çağrıldı → 5 * faktoriyel(4) bekle...
  faktoriyel(4) çağrıldı → 4 * faktoriyel(3) bekle...
    faktoriyel(3) çağrıldı → 3 * faktoriyel(2) bekle...
      faktoriyel(2) çağrıldı → 2 * faktoriyel(1) bekle...
        faktoriyel(1) çağrıldı → 1 döndür ✅

Şimdi geriye doğru çözülüyor:
        faktoriyel(1) = 1
      faktoriyel(2) = 2 * 1 = 2
    faktoriyel(3) = 3 * 2 = 6
  faktoriyel(4) = 4 * 6 = 24
faktoriyel(5) = 5 * 24 = 120 🎉
```

> Bunu bir **tabak yığını** gibi düşün. Yeni tabağı üste koyarsın (push), alacağın zaman da üstten alırsın (pop). İlk koyduğun tabağa ulaşmak için tüm üsttekileri çıkarman lazım.

### ⚠️ Dikkat: Stack Overflow!

Her recursive çağrı bellekte yer kaplar. Eğer base case'e hiç ulaşamazsan veya çok derin recursion yaparsan:

```
💥 RangeError: Maximum call stack size exceeded
```

Bu yüzden:
- Base case'in **her zaman ulaşılabilir** olduğundan emin ol
- Çok derin recursion gerekiyorsa, **iterative (döngü) çözüm** düşün

### Recursion vs Döngü: Hangisini Kullanmalı? 🤔

| Durum | Tercih |
|---|---|
| Performans kritik | Döngü (genellikle daha hızlı, daha az bellek) |
| Kod okunabilirliği önemli | Recursion (bazen çok daha temiz) |
| Ağaç/graf yapıları | Recursion (doğal olarak uygun) |
| Basit tekrarlar | Döngü |

> **Ünlü söz:** "Recursion'ı anlamak için önce recursion'ı anlamalısın." 😄

### 🧠 Akılda Kalası Özet

> Recursion = Bir fonksiyonun **kendini çağırması**.
> Her recursion'da iki şey lazım: **Base case** (dur) ve **Recursive case** (devam et).
> Ağaç yapıları, bölüp fethetme problemleri için çok güçlü bir araç.

---

## 6. ⚡ Quicksort (Hızlı Sıralama)

### Ön Bilgi: Divide and Conquer (Böl ve Fethet) 🗡️

Quicksort'u anlamadan önce, arkasındaki stratejiyi anlamalısın:

**Divide and Conquer (D&C)** bir problem çözme stratejisidir:
1. **Böl:** Problemi daha küçük alt problemlere ayır
2. **Fethet:** Alt problemleri çöz (genellikle recursion ile)
3. **Birleştir:** Çözümleri bir araya getir

### D&C Örneği: Tarla Bölme 🌾

Diyelim ki 1680m x 640m boyutunda bir tarlan var. Bunu **eşit kare parsellere** bölmek istiyorsun ve kareler **mümkün olan en büyük** boyutta olmalı.

```
1680m x 640m tarla

Adım 1: 1680 / 640 = 2 kare (640x640) + kalan 400x640
Adım 2: 640 / 400 = 1 kare (400x400) + kalan 400x240
Adım 3: 400 / 240 = 1 kare (240x240) + kalan 160x240
Adım 4: 240 / 160 = 1 kare (160x160) + kalan 80x160
Adım 5: 160 / 80 = 2 kare (80x80) + kalan 0 ✅

Cevap: 80m x 80m kareler!
```

Bu aslında **Öklid Algoritması** (EBOB/GCD bulma)! Ve D&C'nin güzel bir örneği.

### Quicksort Nasıl Çalışır? 🎯

Diyelim ki şu diziyi sıralayacaksın: `[33, 15, 10, 45, 27]`

**Adım 1:** Bir **pivot** (dayanak noktası) seç. Basitlik için ilk elemanı seçelim: `33`

**Adım 2:** Diziyi **üçe** ayır:
- **Sol:** Pivot'tan küçük elemanlar → `[15, 10, 27]`
- **Pivot:** `[33]`
- **Sağ:** Pivot'tan büyük elemanlar → `[45]`

**Adım 3:** Sol ve sağ dizilere **aynı işlemi tekrarla** (recursion! 🔄)

```
                    [33, 15, 10, 45, 27]
                           |
                  pivot = 33
                 /         |          \
          [15, 10, 27]    [33]       [45]
               |                       |
          pivot = 15                 [45] (tek eleman, sıralı ✅)
         /     |      \
       [10]  [15]   [27]
        ✅    ✅     ✅

Birleştir: [10] + [15] + [27] = [10, 15, 27]
Birleştir: [10, 15, 27] + [33] + [45] = [10, 15, 27, 33, 45] 🎉
```

### Base Case'ler

- **Boş dizi** → zaten sıralı: `[]`
- **Tek elemanlı dizi** → zaten sıralı: `[42]`

### Kod Örneği (JavaScript) 💻

```javascript
function quicksort(arr) {
  // Base case: 0 veya 1 elemanlı dizi zaten sıralıdır
  if (arr.length < 2) {
    return arr;
  }

  // Pivot seç (ilk eleman)
  const pivot = arr[0];

  // Partition: Küçükler ve büyükler
  const less = arr.slice(1).filter(x => x <= pivot);    // Pivot'tan küçük/eşitler
  const greater = arr.slice(1).filter(x => x > pivot);  // Pivot'tan büyükler

  // Recursive olarak sırala ve birleştir
  return [...quicksort(less), pivot, ...quicksort(greater)];
}

console.log(quicksort([33, 15, 10, 45, 27]));
// Output: [10, 15, 27, 33, 45]
```

### Pivot Seçimi Neden Önemli? 🎲

Quicksort'un performansı **pivot seçimine** bağlıdır.

**En kötü senaryo:** Her seferinde en küçük veya en büyük elemanı pivot seçersen:
```
[1, 2, 3, 4, 5, 6, 7, 8]
pivot = 1 → sol: [] | sağ: [2,3,4,5,6,7,8]
  pivot = 2 → sol: [] | sağ: [3,4,5,6,7,8]
    pivot = 3 → ...
```
Her seviyede sadece 1 eleman eleniyor → $O(n^2)$ 🐢

**En iyi senaryo:** Her seferinde ortanca (median) elemanı seçersen:
```
Dizi her seferinde iki eşit parçaya bölünür → O(n log n) 🚀
```

**Pratikte:** Rastgele pivot seçimi genellikle iyi çalışır. Ortalama performans: $O(n \log n)$

### Quicksort vs Selection Sort 🏁

| | Selection Sort | Quicksort |
|---|---|---|
| Big O (En Kötü) | $O(n^2)$ | $O(n^2)$ |
| Big O (Ortalama) | $O(n^2)$ | $O(n \log n)$ |
| Pratikte | Yavaş | **Çok hızlı** |

Aynı Big O'ya sahip olsalar bile, Quicksort pratikte çok daha hızlıdır çünkü **ortalama durumda** $O(n \log n)$'dir ve sabit çarpanı küçüktür.

### 🧠 Akılda Kalası Özet

> Quicksort = **Pivot seç → Küçükleri sola, büyükleri sağa → Tekrarla**
> Divide & Conquer stratejisinin en ünlü örneğidir.
> Ortalama $O(n \log n)$, pratikte en hızlı sıralama algoritmalarından biri.

---

## 7. 🗃️ Hash Tables (Hash Tabloları)

### Hikaye: Market Kasası 🛒

Bir markette kasiyer olarak çalışıyorsun. Müşteri geldi, eline bir mango aldı. Fiyatını bilmen lazım.

**Yöntem 1: Liste (Array)**
```
Elma    → 3 TL
Armut   → 4 TL
Çilek   → 8 TL
...
Mango   → 12 TL    ← Tüm listeyi taradın! O(n)
...
Zencefil → 15 TL
```

100 ürün varsa, en kötü 100 satır tararsın.

**Yöntem 2: Sıralı liste + Binary Search**
$O(\log n)$ — daha iyi ama yine de arama gerekiyor.

**Yöntem 3: Kafanda bilen bir arkadaş 🧑**
"Mango kaç lira?" diye soruyorsun, anında "12 TL" diyor.
$O(1)$ — **SABİT SÜRE!** Eleman sayısından bağımsız!

İşte **Hash Table**, o her şeyi bilen arkadaşındır! 🎉

### Hash Function (Hash Fonksiyonu) Nedir?

Bir hash function, bir **girdi alır** ve bir **sayı (index) döndürür**.

```
hash("elma")    → 2
hash("armut")   → 0
hash("mango")   → 5
hash("çilek")   → 3
```

Bu sayılar, değerlerin bellekte **nereye kaydedileceğini** belirler:

```
Index:  [0]      [1]    [2]     [3]      [4]    [5]
Değer:  armut:4  boş    elma:3  çilek:8  boş    mango:12
```

"Mango kaç lira?" diye sorduğunda:
1. `hash("mango")` → 5
2. Index 5'e git → 12 TL
3. **Bitti!** Tek adım! ✅

### JavaScript'te Hash Table = Object / Map 💻

```javascript
// JavaScript'te hash table olarak object kullanılır
const fiyatlar = {};

// Ekleme - O(1)
fiyatlar["elma"] = 3;
fiyatlar["armut"] = 4;
fiyatlar["mango"] = 12;
fiyatlar["çilek"] = 8;

// Okuma - O(1)
console.log(fiyatlar["mango"]);  // 12

// Var mı kontrolü - O(1)
console.log("portakal" in fiyatlar);  // false

// Modern JavaScript'te Map daha iyi:
const fiyatMap = new Map();
fiyatMap.set("elma", 3);
fiyatMap.set("mango", 12);
console.log(fiyatMap.get("mango"));  // 12
```

### Kullanım Alanları 🌍

#### 1. Telefon Rehberi 📞
```javascript
const rehber = {
  "Ali": "0532-111-2233",
  "Ayşe": "0544-555-6677",
  "Mehmet": "0555-888-9900"
};

console.log(rehber["Ayşe"]); // "0544-555-6677"
```

#### 2. Tekrar Engelleme (Oy Kullanma) 🗳️
```javascript
const oyKullananlar = {};

function oyVer(isim) {
  if (oyKullananlar[isim]) {
    console.log(`${isim} zaten oy kullanmış! 🚫`);
    return;
  }
  oyKullananlar[isim] = true;
  console.log(`${isim} oy kullandı! ✅`);
}

oyVer("Ali");     // Ali oy kullandı! ✅
oyVer("Ayşe");    // Ayşe oy kullandı! ✅
oyVer("Ali");     // Ali zaten oy kullanmış! 🚫
```

#### 3. Cache (Önbellek) 🏎️
```javascript
const cache = {};

function getServerData(url) {
  if (cache[url]) {
    console.log("Cache'ten döndürülüyor ⚡");
    return cache[url];
  }

  console.log("Sunucudan çekiliyor... 🌐");
  const data = fetchFromServer(url);  // Yavaş işlem
  cache[url] = data;                   // Cache'e kaydet
  return data;
}
```

### Collision (Çakışma) Problemi ⚠️

İki farklı key aynı index'e denk gelirse ne olur?

```
hash("elma")  → 2
hash("karpuz") → 2   // 😱 Aynı yer!
```

Bu duruma **collision (çakışma)** denir. Çözüm yöntemleri:

**1. Chaining (Zincirleme):** O index'te bir linked list tut.
```
Index 2: elma:3 → karpuz:7 → null
```

**2. Open Addressing:** Boş bir sonraki index'e koy.

### Load Factor (Doluluk Oranı) 📏

$$\text{Load Factor} = \frac{\text{Dolu slot sayısı}}{\text{Toplam slot sayısı}}$$

- Load Factor < 0.7 → İyi ✅
- Load Factor > 0.7 → Tabloyu büyüt (**resize**)

Yüksek load factor = çok çakışma = yavaş performans.

### Performans Özeti 📊

| İşlem | Ortalama | En Kötü |
|---|---|---|
| Arama | $O(1)$ | $O(n)$ |
| Ekleme | $O(1)$ | $O(n)$ |
| Silme | $O(1)$ | $O(n)$ |

En kötü durum, her şeyin aynı index'e çakışması durumunda olur (pratikte çok nadir).

### 🧠 Akılda Kalası Özet

> Hash Table = **Anahtar-değer çiftlerini sabit sürede** ($O(1)$) saklayan veri yapısı.
> JavaScript'te `{}` (object) ve `Map` hash table'dır.
> Dünya'nın en çok kullanılan veri yapılarından biri. Cache, index, lookup, duplicate check — her yerde!

---

## 8. 🌊 Breadth-First Search — BFS (Genişlik Öncelikli Arama)

### Yeni Veri Yapısı: Graph (Graf) 🕸️

BFS'i anlamak için önce **graf** kavramını anlaman lazım.

#### Graf Nedir?

Bir graf, **düğümler (nodes)** ve onları birbirine bağlayan **kenarlardan (edges)** oluşur.

```
  Ali --- Ayşe --- Mehmet
   |        |
  Veli --- Fatma
```

Bu bir **sosyal ağ grafı**! Ali ile Ayşe arkadaş, Ayşe ile Mehmet arkadaş, vs.

#### Graflar Nerelerde Kullanılır? 🌍

- **Sosyal ağlar:** Facebook arkadaşlıkları
- **Haritalar:** Şehirler arası yollar
- **Web:** Sayfalar arası linkler
- **Öneri sistemleri:** "Bunu alanlar şunu da aldı"

### BFS: Mango Satıcısı Problemi 🥭

Hikaye zamanı! 🎬

Sen mango satıcısı arıyorsun. Önce kendi arkadaşlarına sorarsın:
- Ali → Manavda çalışmıyor ❌
- Ayşe → Manavda çalışmıyor ❌
- Veli → Manavda çalışmıyor ❌

Kimse mango satmıyor. O zaman **arkadaşlarının arkadaşlarına** sor:
- Ali'nin arkadaşı Burak → Manavda çalışmıyor ❌
- Ayşe'nin arkadaşı Zeynep → **MANGO SATICI!** 🥭✅

BFS tam olarak bunu yapar:
1. Önce **1. derece bağlantıları** kontrol et
2. Sonra **2. derece bağlantıları**
3. Sonra **3. derece...**
4. Ta ki bulana veya herkesi kontrol edene kadar

### Neden "Genişlik Öncelikli"? 🤔

Çünkü **önce genişliğine** yayılıyorsun, derinliğe değil.

```
         Sen
        / | \
      Ali Ayşe Veli        ← 1. seviye (önce bunlar)
      /    |     \
   Burak Zeynep  Deniz     ← 2. seviye (sonra bunlar)
    /       \
  Can      Ece             ← 3. seviye (en son bunlar)
```

### Queue (Kuyruk) Veri Yapısı 🚶‍♂️🚶‍♀️🚶

BFS bir **kuyruk (queue)** kullanır. Kuyruk, **FIFO** prensibiyle çalışır:
**F**irst **I**n, **F**irst **O**ut = İlk giren, ilk çıkar.

Banka kuyruğu gibi düşün:
- İlk gelen müşteri ilk hizmet alır
- Yeni gelen sona eklenir

```
Giriş → [Can] [Deniz] [Zeynep] [Burak] [Veli] [Ayşe] [Ali] → Çıkış
         sona ekle (enqueue)                            baştan çıkar (dequeue)
```

### BFS Algoritması 📋

```
1. Başlangıç düğümünün komşularını kuyruğa ekle
2. Kuyruktan bir düğüm al
3. Bu düğüm aradığımız mı?
   - Evet → BULDUK! 🎉
   - Hayır → Bu düğümün komşularını kuyruğa ekle
4. Adım 2'ye dön
5. Kuyruk boşsa ve bulamadıysan → YOK! 😢
```

### Kod Örneği (JavaScript) 💻

```javascript
// Graf: Her kişinin arkadaşları
const graf = {
  "sen":   ["ali", "ayse", "veli"],
  "ali":   ["burak"],
  "ayse":  ["zeynep"],
  "veli":  ["deniz"],
  "burak": ["can"],
  "zeynep":[], // Zeynep mango satıcısı!
  "deniz": [],
  "can":   []
};

function mangoSaticiMi(isim) {
  // Mango satıcısı "zeynep" olsun
  return isim === "zeynep";
}

function bfs(graf, baslangic) {
  const kuyruk = [...graf[baslangic]];  // Başlangıcın komşularını ekle
  const kontrolEdildi = new Set();       // Sonsuz döngüyü önle
  kontrolEdildi.add(baslangic);

  while (kuyruk.length > 0) {
    const kisi = kuyruk.shift();        // Kuyruktan ilk kişiyi al (dequeue)

    if (kontrolEdildi.has(kisi)) continue; // Zaten kontrol edilmiş, atla
    kontrolEdildi.add(kisi);

    if (mangoSaticiMi(kisi)) {
      console.log(`🥭 ${kisi} mango satıcısı!`);
      return true;
    }

    // Bu kişinin arkadaşlarını kuyruğa ekle
    if (graf[kisi]) {
      kuyruk.push(...graf[kisi]);
    }
  }

  console.log("😢 Mango satıcısı bulunamadı");
  return false;
}

bfs(graf, "sen");
// Output: 🥭 zeynep mango satıcısı!
```

### ⚠️ Sonsuz Döngü Tehlikesi

Eğer kontrol edilen düğümleri takip etmezsek:

```
Ali → Ayşe → Ali → Ayşe → Ali → ... 💥 Sonsuz döngü!
```

Bu yüzden `kontolEdildi` (visited) set'i **ŞART**!

### BFS İki Soruyu Cevaplar 🎯

1. **A'dan B'ye yol var mı?** (reachability)
2. **Varsa, en kısa yol hangisi?** (shortest path — kenar ağırlıkları eşitse)

### Performans ⏱️

$$O(V + E)$$

- $V$ = Vertex (düğüm) sayısı
- $E$ = Edge (kenar) sayısı

Yani tüm düğümleri ve tüm kenarları bir kez ziyaret edersin.

### 🧠 Akılda Kalası Özet

> BFS = **Yakınlardan başla, halka halka genişle.**
> En kısa yolu bulur (ağırlıksız graflarda).
> Kuyruk (Queue) veri yapısını kullanır (FIFO).
> Ziyaret edilenleri takip et, yoksa sonsuz döngüye girersin! 🔄

---

## 9. 🛤️ Dijkstra's Algorithm (Dijkstra Algoritması)

### BFS Yeterli Değil mi? 🤔

BFS "en az kenar sayısıyla" hedefe ulaşır. Ama ya kenarların **ağırlıkları** farklıysa?

```
       5 dk
  Ev --------→ Okul
  |                ↑
  | 2 dk          | 1 dk
  |                |
  → Park --------→
       6 dk
```

- **BFS:** Ev → Okul (1 kenar, 5 dk) ✅ en az kenar
- **Dijkstra:** Ev → Park → Okul (2 kenar, 2+6=8 dk)... Hmm, 8 > 5
- Aslında: Ev → Okul (5 dk) en hızlı ✅

Farklı bir örnek:
```
       10 dk
  Ev --------→ Okul
  |                ↑
  | 2 dk          | 1 dk
  |                |
  → Park --------→
       3 dk
```

- **BFS:** Ev → Okul (1 kenar, 10 dk)
- **Dijkstra:** Ev → Park → Okul (2+3=5 dk daha hızlı! 🏃)

BFS **kenar sayısını**, Dijkstra **toplam ağırlığı** minimize eder.

### Terminoloji 📝

- **Ağırlık (Weight):** Kenarın maliyeti (süre, mesafe, para, vs.)
- **Ağırlıklı Graf (Weighted Graph):** Kenarlarında ağırlık bulunan graf
- **Ağırlıksız Graf (Unweighted Graph):** Tüm kenarlar eşit (BFS için)

### Dijkstra Nasıl Çalışır? Adım Adım 👣

Harita:
```
          6
   A ──────────→ B
   |              |
 2 |              | 1
   ↓     3        ↓
   C ──────────→ D
   |
 5 |
   ↓
   E ──────────→ D
         1
```

Başlangıç: A, Hedef: D

**Tablo (başlangıçta):**
| Düğüm | En Kısa Maliyet | Önceki Düğüm |
|---|---|---|
| A | 0 | - |
| B | ∞ | ? |
| C | ∞ | ? |
| D | ∞ | ? |
| E | ∞ | ? |

**Adım 1:** A'nın komşularını güncelle
- A→B: 6
- A→C: 2

| Düğüm | En Kısa Maliyet | Önceki Düğüm |
|---|---|---|
| A | 0 ✅ (işlendi) | - |
| B | 6 | A |
| C | 2 | A |
| D | ∞ | ? |
| E | ∞ | ? |

**Adım 2:** En ucuz işlenmemiş düğümü seç → C (maliyet: 2)
C'nin komşularını güncelle:
- C→D: 2+3=5 (∞'dan küçük, güncelle!)
- C→E: 2+5=7

| Düğüm | En Kısa Maliyet | Önceki Düğüm |
|---|---|---|
| A | 0 ✅ | - |
| B | 6 | A |
| C | 2 ✅ (işlendi) | A |
| D | 5 | C |
| E | 7 | C |

**Adım 3:** En ucuz işlenmemiş düğüm → D (maliyet: 5)
D'nin komşusu yok (ya da hepsi daha pahalı). İşlendi.

**Adım 4:** En ucuz işlenmemiş düğüm → B (maliyet: 6)
B→D: 6+1=7 (5'ten büyük, güncelleme) ❌

**Adım 5:** E (maliyet: 7)
E→D: 7+1=8 (5'ten büyük, güncelleme) ❌

**Sonuç:** A→D en kısa yol = **5** (A→C→D) 🎉

### Kod Örneği (JavaScript) 💻

```javascript
function dijkstra(graf, baslangic) {
  // Maliyetler tablosu
  const maliyetler = {};
  const oncekiler = {};
  const islenmis = new Set();

  // Başlangıç değerleri
  for (const dugum in graf) {
    maliyetler[dugum] = Infinity;
  }
  maliyetler[baslangic] = 0;

  // En ucuz işlenmemiş düğümü bulan yardımcı fonksiyon
  function enUcuzDugum() {
    let enDusukMaliyet = Infinity;
    let enUcuz = null;
    for (const dugum in maliyetler) {
      if (!islenmis.has(dugum) && maliyetler[dugum] < enDusukMaliyet) {
        enDusukMaliyet = maliyetler[dugum];
        enUcuz = dugum;
      }
    }
    return enUcuz;
  }

  let dugum = enUcuzDugum();

  while (dugum !== null) {
    const maliyet = maliyetler[dugum];
    const komsular = graf[dugum] || {};

    for (const komsu in komsular) {
      const yeniMaliyet = maliyet + komsular[komsu];
      if (yeniMaliyet < maliyetler[komsu]) {
        maliyetler[komsu] = yeniMaliyet;
        oncekiler[komsu] = dugum;
      }
    }

    islenmis.add(dugum);
    dugum = enUcuzDugum();
  }

  return { maliyetler, oncekiler };
}

// Graf tanımı (ağırlıklı)
const graf = {
  "A": { "B": 6, "C": 2 },
  "B": { "D": 1 },
  "C": { "D": 3, "E": 5 },
  "D": {},
  "E": { "D": 1 }
};

const sonuc = dijkstra(graf, "A");
console.log(sonuc.maliyetler);
// { A: 0, B: 6, C: 2, D: 5, E: 7 }
```

### ⚠️ Dijkstra'nın Sınırlaması: Negatif Ağırlıklar

Dijkstra **negatif ağırlıklı kenarlarla çalışmaz!**

```
     -5
A ──────→ B
 \        ↑
  +3     +2
   \    /
    → C
```

Negatif ağırlık varsa **Bellman-Ford** algoritmasını kullanman gerekir.

### BFS vs Dijkstra Karşılaştırması 📊

| | BFS | Dijkstra |
|---|---|---|
| Ağırlıksız graf | ✅ En kısa yol bulur | ✅ (ama gereksiz) |
| Ağırlıklı graf | ❌ Yanlış sonuç verebilir | ✅ En kısa yol bulur |
| Negatif ağırlık | ❌ | ❌ |
| Veri Yapısı | Queue | Priority Queue |

### 🧠 Akılda Kalası Özet

> Dijkstra = **"Her zaman şu ana kadar en ucuz düğümü işle, komşularını güncelle."**
> Ağırlıklı graflarda en kısa yolu bulur.
> Negatif kenarlarla çalışmaz!

---

## 10. 🤑 Greedy Algorithms (Açgözlü Algoritmalar)

### Hikaye: Sınıf Programı Hazırlama 📅

Bir sınıfın var ve şu dersleri vermek istiyorsun:

| Ders | Başlangıç | Bitiş |
|---|---|---|
| Matematik | 09:00 | 10:00 |
| Fizik | 09:30 | 10:30 |
| Tarih | 10:00 | 11:00 |
| Müzik | 10:30 | 11:30 |
| Beden | 11:00 | 12:00 |
| İngilizce | 11:30 | 12:30 |

Tek sınıfın var, aynı anda iki ders olamaz. **En çok dersi** nasıl sığdırırsın?

### Greedy (Açgözlü) Yaklaşım 🍕

**Her adımda o an en iyi görünen seçimi yap!**

Strateji: **En erken biten dersi seç**, çakışanları ele.

```
1. En erken biten: Matematik (10:00'da bitiyor) ✅
   → Fizik çakışıyor (09:30-10:30) ❌ ele

2. Kalanlardan en erken biten: Tarih (11:00'da bitiyor) ✅
   → Müzik çakışıyor (10:30-11:30) ❌ ele

3. Kalanlardan en erken biten: Beden (12:00'da bitiyor) ✅
   → İngilizce çakışıyor (11:30-12:30) ❌ ele

Sonuç: Matematik, Tarih, Beden → 3 ders! 🎉
```

Bu en iyi sonuç mu? Evet! Ve bunu **kanıtlamak da mümkün.**

### Greedy Algoritmaların Güzel Yanı ✨

- **Basit:** Anlaması ve kodu yazması kolay
- **Hızlı:** Genellikle $O(n \log n)$ veya daha iyi
- Bazı problemlerde **optimal sonucu** verir

### Greedy Algoritmaların Zayıf Yanı ⚠️

Her problem için optimal değildir! Bazen "o an en iyi görünen" seçim, **genel olarak en iyi olmayabilir**.

#### Örnek: Para Üstü Problemi 💰

Bozuklukların: 25 kuruş, 10 kuruş, 5 kuruş, 1 kuruş
36 kuruş bozuk para vereceksin.

**Greedy:** Her seferinde en büyük bozukluğu seç:
- 25 + 10 + 1 = 36 ✅ (3 bozukluk)

Bu durumda optimal! Ama ya bozukluklar farklıysa?

Bozukluklar: 25 kuruş, 15 kuruş, 1 kuruş
30 kuruş vereceksin.

**Greedy:** 25 + 1 + 1 + 1 + 1 + 1 = 30 (6 bozukluk) 😕
**Optimal:** 15 + 15 = 30 (2 bozukluk!) 🎉

### Set Cover Problem (Küme Kapsama) 📻

Hikaye: Bir radyo programın var ve ABD'nin **tüm eyaletlerine** yayın yapmak istiyorsun. Her radyo istasyonu belirli eyaletleri kapsıyor.

```
İstasyon 1: Idaho, Nevada, Utah
İstasyon 2: Washington, Idaho, Montana
İstasyon 3: Oregon, Nevada, California
İstasyon 4: Nevada, Utah
İstasyon 5: California, Arizona
```

**En az istasyonla tüm eyaletleri** nasıl kapsarsın?

**Exact (Tam) çözüm:**
Tüm olası istasyon kombinasyonlarını dene → $O(2^n)$ 💀
5 istasyonda 32 kombinasyon. 50 istasyonda? $2^{50}$ = 1.125.899.906.842.624 kombinasyon!

**Greedy çözüm:**
Her adımda **en çok kapsanmamış eyaleti kapsayan** istasyonu seç.

```
Adım 1: İstasyon 1 (Idaho, Nevada, Utah → 3 yeni eyalet) ✅
Adım 2: İstasyon 2 (Washington, Montana → 2 yeni eyalet) ✅
Adım 3: İstasyon 3 (Oregon, California → 2 yeni eyalet) ✅
Adım 4: İstasyon 5 (Arizona → 1 yeni eyalet) ✅

4 istasyonla tüm eyaletler! 📻
```

Bu **optimal sonuç olmayabilir** ama çok **yakın** bir sonuçtur ve **makul sürede** çalışır.

### NP-Hard Problemler 🧩

Bazı problemlerin bilinen hızlı çözümü yoktur. Bunlara **NP-hard** denir.

**Gezgin Satıcı Problemi (Travelling Salesman):**
5 şehri en kısa rotayla ziyaret et → 120 olasılık ($5! = 120$)
20 şehir → $20! = 2.432.902.008.176.640.000$ olasılık 🤯

Bu problemlerde:
- **Exact çözüm** pratikte imkansız (çok yavaş)
- **Greedy/yaklaşık çözüm** makul sürede iyi bir sonuç verir

### Bir Problemin NP-Hard Olduğunu Nasıl Anlarsın? 🔍

- "Tüm kombinasyonları" hesaplaman gerekiyorsa
- $O(2^n)$ veya $O(n!)$ zaman karmaşıklığı varsa
- Problem "set cover" veya "gezgin satıcı"na benzetelebiliyorsa
- Tek bir eleman eklenmesi çözüm süresini dramatik artırıyorsa

### 🧠 Akılda Kalası Özet

> Greedy = **"Her adımda yerel olarak en iyi seçimi yap."**
> Bazı problemlerde optimal sonuç verir (sınıf programı, para üstü).
> NP-hard problemlerde mükemmel çözüm bulunamaz, greedy iyi bir **yaklaşım (approximation)** sağlar.

---

## 11. 💎 Dynamic Programming (Dinamik Programlama)

### Hikaye: Hırsız Problemi 🎒

Bir hırsızsın (kötü bir hırsız değil, etik hırsız diyelim 😅). Sırt çantan **4 kg** alıyor. Dükkanda şu eşyalar var:

| Eşya | Ağırlık | Değer |
|---|---|---|
| Gitar 🎸 | 1 kg | 1.500 TL |
| Müzik Seti 🔊 | 4 kg | 3.000 TL |
| Laptop 💻 | 3 kg | 2.000 TL |

Çantana en değerli kombinasyonu nasıl sığdırırsın?

**Greedy çözüm:** En değerlisini al → Müzik Seti (3.000 TL). Çanta doldu. Toplam: 3.000 TL

**Ama daha iyisi var:** Gitar (1.500) + Laptop (2.000) = 3.500 TL! 🎉

Greedy burada **optimal değil**. Çünkü bu bir **optimization problemi** ve alt problemler birbirine bağlı.

### Dynamic Programming (DP) Nedir?

> DP = **Büyük bir problemi alt problemlere böl, her alt problemi SADECE BİR KEZ çöz ve sonuçları sakla.**

Greedy'den farkı: DP **tüm olasılıkları** akıllıca değerlendirir ama **tekrar hesaplama yapmaz** çünkü sonuçları tabloda tutar.

### Sırt Çantası Problemini DP ile Çözmek 🎒

Bir tablo oluşturuyoruz. Satırlar = eşyalar, sütunlar = çanta kapasiteleri.

**Boş tablo:**

| | 1 kg | 2 kg | 3 kg | 4 kg |
|---|---|---|---|---|
| Gitar 🎸 | ? | ? | ? | ? |
| Müzik Seti 🔊 | ? | ? | ? | ? |
| Laptop 💻 | ? | ? | ? | ? |

**Satır 1: Sadece Gitar düşün**
Gitar 1 kg, 1.500 TL. Her kapasiteye sığar.

| | 1 kg | 2 kg | 3 kg | 4 kg |
|---|---|---|---|---|
| Gitar 🎸 | 1.500 | 1.500 | 1.500 | 1.500 |

**Satır 2: Gitar + Müzik Seti düşün**
Müzik Seti 4 kg. Sadece 4 kg'lık çantaya sığar.

| | 1 kg | 2 kg | 3 kg | 4 kg |
|---|---|---|---|---|
| Gitar 🎸 | 1.500 | 1.500 | 1.500 | 1.500 |
| Müzik Seti 🔊 | 1.500 | 1.500 | 1.500 | 3.000 |

- 4 kg hücresinde karar: Müzik Seti (3.000) > Gitar (1.500) → Müzik Seti al

**Satır 3: Gitar + Müzik Seti + Laptop düşün**
Laptop 3 kg, 2.000 TL.

| | 1 kg | 2 kg | 3 kg | 4 kg |
|---|---|---|---|---|
| Gitar 🎸 | 1.500 | 1.500 | 1.500 | 1.500 |
| Müzik Seti 🔊 | 1.500 | 1.500 | 1.500 | 3.000 |
| Laptop 💻 | 1.500 | 1.500 | 2.000 | **3.500** |

4 kg hücresinde:
- Önceki en iyi (müzik seti): 3.000 TL
- Laptop (2.000) + kalan 1 kg'a ne sığar? Gitar (1.500)! → 3.500 TL ✅

**Cevap: 3.500 TL (Laptop + Gitar)** 🎉

### DP Formülü 📐

Her hücre için:

$$cell[i][j] = \max\begin{cases} \text{Üstteki hücre (bu eşyayı almama)} \\ \text{Bu eşyanın değeri + kalan kapasitedeki en iyi değer} \end{cases}$$

### Başka Bir Örnek: Substring vs Subsequence 🔤

İki kelime arasındaki benzerliği bulmak istiyorsun. Ama DİKKAT — iki farklı problem var:

**Longest Common SUBSTRING** (En Uzun Ortak Alt DİZİ — ardışık!):
→ "fish" vs "fosh" → En uzun ardışık eşleşme: "sh" → Sonuç: **2**

**Longest Common SUBSEQUENCE** (En Uzun Ortak Alt DİZİLİM — ardışık olmayabilir!):
→ "fish" vs "fosh" → Ortak harfler: f, s, h (ardışık olmak zorunda değil) → Sonuç: **3**

Bu iki problem FARKLI DP kuralları ile çözülür!

**Substring Tablosu (ardışık eşleşme):**

| | f | o | s | h |
|---|---|---|---|---|
| **f** | 1 | 0 | 0 | 0 |
| **i** | 0 | 0 | 0 | 0 |
| **s** | 0 | 0 | 1 | 0 |
| **h** | 0 | 0 | 0 | **2** |

Kural: Eşleşme → sol üst çapraz + 1. Eşleşmezse → **0** (ardışıklık KIRILDI!)
Cevap: tablodaki EN BÜYÜK değer = **2** ("sh")

**Subsequence Tablosu (ardışık olmak ZORUNLU DEĞİL):**

| | f | o | s | h |
|---|---|---|---|---|
| **f** | 1 | 1 | 1 | 1 |
| **i** | 1 | 1 | 1 | 1 |
| **s** | 1 | 1 | 2 | 2 |
| **h** | 1 | 1 | 2 | **3** |

Kural: Eşleşme → sol üst çapraz + 1. Eşleşmezse → **max(sol, üst)** (önceki eşleşmeleri KORU!)
Cevap: sağ alt hücre = **3** (f, s, h)

> ⚠️ Bu iki problemi KARIŞTIRMA! `git diff` → Subsequence kullanır.
> Metin arama → Substring kullanır. Aradaki fark küçük ama sonuç çok farklı!

### Edit Distance (Düzenleme Mesafesi) ✏️

"Bunu mu demek istediniz?" → Google bunu **edit distance** ile yapar.

İki kelime arasında kaç **ekleme**, **silme** veya **değiştirme** yaparak birini diğerine çevirirsin?

"kitten" → "sitting": 3 adım
1. k**i**tten → s**i**tten (k→s değiştir)
2. sitt**e**n → sitt**i**n (e→i değiştir)
3. sittin → sittin**g** (g ekle)

```javascript
function editDistance(a, b) {
  const m = a.length, n = b.length;
  // DP tablosu: (m+1) x (n+1)
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  // İlk satır ve sütunu doldur
  for (let i = 0; i <= m; i++) dp[i][0] = i; // i silme
  for (let j = 0; j <= n; j++) dp[0][j] = j; // j ekleme

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (a[i - 1] === b[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1]; // Eşleşme → maliyet yok
      } else {
        dp[i][j] = 1 + Math.min(
          dp[i - 1][j],     // Silme
          dp[i][j - 1],     // Ekleme
          dp[i - 1][j - 1]  // Değiştirme
        );
      }
    }
  }
  return dp[m][n];
}

console.log(editDistance("kitten", "sitting")); // 3
```

> 💡 **Not:** Fractional Knapsack (kesirli sırt çantası) problemi DP ile DEĞİL, greedy ile çözülür.
> Eğer laptop'un yarısını alabilirsen → en değerli eşyanın kg başı değerine göre sıralayıp al.
> Tam sayı sırt çantası → DP. Kesirli sırt çantası → Greedy. Farkı bil!

### Gerçek Hayatta DP Nerelerde Kullanılır? 🌍

| Alan | Problem |
|---|---|
| **Metin editörleri** | `git diff` — iki dosya arasındaki farkı bulmak (Longest Common Subsequence) |
| **Biyoloji** | DNA dizilerinin benzerliği |
| **Arama motorları** | "Bunu mu demek istediniz?" — kelime benzerliği (edit distance) |
| **Finans** | Optimal yatırım portföyü |
| **Oyunlar** | En kısa yol bulma |
| **Netflix** | Video encoding — sahne başına optimal bitrate seçimi (DP tabanlı per-title encoding) |
| **Google Translate** | Cümle hizalama — sequence alignment DP kullanır |

### DP'nin Özü: İki Özellik 🎯

Bir problem DP ile çözülebilir mi? Şu iki özellik varsa EVET:

1. **Optimal Substructure (Optimal Alt Yapı):**
   Büyük problemin optimal çözümü, alt problemlerin optimal çözümlerinden oluşur.

2. **Overlapping Subproblems (Örtüşen Alt Problemler):**
   Aynı alt problem birden fazla kez çözülür. DP bu sonuçları saklar (memoization).

### Fibonacci ile DP'yi Görmek 🐇

$F(n) = F(n-1) + F(n-2)$

**Naive recursion (DP'siz):**
```
                    F(6)
                  /      \
              F(5)        F(4)
             /    \       /    \
          F(4)   F(3)  F(3)   F(2)    ← F(4), F(3) tekrar hesaplanıyor!
         /   \
       F(3) F(2)                       ← F(3) yine!
```

$O(2^n)$ — çok yavaş! F(50) hesaplamak dakikalar sürer.

**DP ile (memoization):**
```javascript
function fibonacci(n, memo = {}) {
  if (n in memo) return memo[n];  // Daha önce hesapladık mı? Tabloya bak!
  if (n <= 1) return n;

  memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
  return memo[n];
}

console.log(fibonacci(50)); // 12586269025 — anında hesaplar! ⚡
```

$O(n)$ — her alt problem SADECE BİR KEZ hesaplanır!

### DP Yaklaşımları

| Yaklaşım | Açıklama |
|---|---|
| **Top-Down (Memoization)** | Recursion + sonuçları cache'leme. Yukarıdan aşağı çözüm. |
| **Bottom-Up (Tabulation)** | Tabloyu küçük alt problemlerden başlayarak doldur. Aşağıdan yukarı. |

```javascript
// Bottom-Up Fibonacci
function fibonacciBottomUp(n) {
  if (n <= 1) return n;

  const tablo = [0, 1];
  for (let i = 2; i <= n; i++) {
    tablo[i] = tablo[i - 1] + tablo[i - 2];
  }
  return tablo[n];
}
```

### 🧠 Akılda Kalası Özet

> DP = **"Alt problemleri çöz, sonuçları sakla, tekrar tekrar hesaplama."**
> Greedy her zaman optimal sonuç vermez, DP verir (ama daha yavaştır).
> Sırt çantası, en uzun ortak dizi, edit distance, Fibonacci → hep DP!
> İki anahtar kavram: **Optimal alt yapı** + **Örtüşen alt problemler**

---

## 12. 🏘️ K-Nearest Neighbors — KNN (K En Yakın Komşu)

### Hikaye: Film Önerisi 🎬

Netflix'tesin ve yeni bir film arıyorsun. Netflix sana nasıl öneri yapıyor?

**Basit fikir:** Sana en çok benzeyen kullanıcıların sevdiği filmleri öner!

"Benzerlik" nasıl ölçülür? Anketlerle diyelim:

| | Aksiyon | Komedi | Romantik | Korku | Bilim Kurgu |
|---|---|---|---|---|---|
| **Sen** | 5 | 4 | 1 | 2 | 5 |
| **Ali** | 4 | 5 | 1 | 1 | 4 |
| **Ayşe** | 1 | 2 | 5 | 4 | 1 |
| **Veli** | 5 | 3 | 2 | 3 | 4 |

Ali ve Veli sana benziyor, Ayşe benzemiyor. Nasıl matematiksel olarak gösteririz?

### Öklid Uzaklığı (Euclidean Distance) 📏

İki nokta arasındaki **düz çizgi mesafesi.**

2 boyutlu alan için:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

n boyutlu alan için (her özellik bir boyut):
$$d = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + ... + (a_n - b_n)^2}$$

**Sen vs Ali:**
$$d = \sqrt{(5-4)^2 + (4-5)^2 + (1-1)^2 + (2-1)^2 + (5-4)^2}$$
$$d = \sqrt{1 + 1 + 0 + 1 + 1} = \sqrt{4} = 2$$

**Sen vs Ayşe:**
$$d = \sqrt{(5-1)^2 + (4-2)^2 + (1-5)^2 + (2-4)^2 + (5-1)^2}$$
$$d = \sqrt{16 + 4 + 16 + 4 + 16} = \sqrt{56} ≈ 7.48$$

Ali sana çok daha yakın! ✅

### KNN Nasıl Çalışır? 🎯

**K** = Kaç komşuya bakacağımız sayısı

**K=3 ile film önerisi:**
1. Sana en yakın 3 kişiyi bul (mesafe hesapla)
2. Bu 3 kişinin beğendiği ama senin izlemediğin filmleri bul
3. Öner! 🎬

### KNN ile Sınıflandırma (Classification)

**Problem:** Bir portakal mı, greyfurt mu? 🍊

Özellikleri:
- Boyut: 8 cm
- Kırmızılık: 3/10
- Ağırlık: 180 gram

K=3 ile en yakın 3 meyveye bak:
- Komşu 1: Portakal 🍊
- Komşu 2: Portakal 🍊
- Komşu 3: Greyfurt 🍊

Çoğunluk: **Portakal** (2/3)! → Bu meyve portakal! ✅

### KNN ile Regresyon (Tahmin)

**Problem:** Fırının yeni açıldığı mahallede günde kaç ekmek satacağını tahmin et.

En benzer 4 mahalle (K=4):
- Mahalle A: Günde 300 ekmek
- Mahalle B: Günde 250 ekmek
- Mahalle C: Günde 280 ekmek
- Mahalle D: Günde 320 ekmek

**Tahmin:** $(300 + 250 + 280 + 320) / 4 = 287.5$ ekmek/gün

### K Değerini Nasıl Seçeriz? 🔢

| K Değeri | Risk |
|---|---|
| Çok küçük (K=1) | **Overfitting** — gürültüye duyarlı, tek bir outlier sonucu bozar |
| Çok büyük (K=100) | **Underfitting** — çok genel, yerel desenleri kaçırır |
| İyi bir K | Genellikle tek sayı seç (beraberlikleri önlemek için). $\sqrt{n}$ iyi bir başlangıç noktası. |

### Feature Engineering (Özellik Mühendisliği) 🔧

Doğru özellikleri seçmek çok önemli!

**Kötü özellikler (film önerisi için):**
- Kullanıcının saç rengi ❌
- Kullanıcının ayak numarası ❌

**İyi özellikler:**
- Film türü tercihleri ✅
- İzleme geçmişi ✅
- Puan verme alışkanlığı ✅

> **Garbage in, garbage out!** 🗑️ → Kötü veri girersen, kötü sonuç alırsın.

### Normalizasyon 📏

Özellikler farklı ölçeklerde olabilir:
- Yaş: 0-100
- Gelir: 0-1.000.000

Gelir, sadece büyüklüğünden dolayı mesafeyi domine eder. Çözüm: **Normalizasyon**

$$x_{norm} = \frac{x - \min}{\max - \min}$$

Bu, tüm özellikleri 0-1 arasına sıkıştırır.

### KNN'in Sınırlamaları ⚠️

| Problem | Açıklama |
|---|---|
| **Yavaş** | Her tahmin için TÜM noktalarla mesafe hesaplar |
| **Boyut laneti** | Özellik sayısı arttıkça mesafeler anlamsızlaşır |
| **Bellek** | Tüm veriyi bellekte tutar |

Bu yüzden büyük ölçekli uygulamalarda (Netflix gibi) daha sofistike algoritmalar kullanılır. Ama KNN, makine öğreniminin **temelini** anlamak için harika bir başlangıçtır!

### 🧠 Akılda Kalası Özet

> KNN = **"Bana arkadaşlarını söyle, sana kim olduğunu söyleyeyim."**
> Sınıflandırma (bu nedir?) ve regresyon (bu ne kadar?) için kullanılır.
> Doğru K değeri ve doğru özellikler seçmek kritik.
> Basit ama güçlü — makine öğreniminin "Merhaba Dünya"sı!

---

## 13. 🚀 Sonraki Adımlar

Bu rehberdeki tüm konuları sindirdiysen, artık sağlam bir **algoritma ve veri yapıları temelin** var! 🎉

### Bu Rehberde Öğrendiklerin 📋

| Konu | Ne Öğrendin |
|---|---|
| Binary Search | Sıralı veride logaritmik arama |
| Big O | Algoritma performansını ölçme ve karşılaştırma |
| Selection Sort | Basit ama yavaş sıralama |
| Recursion | Fonksiyonların kendini çağırması |
| Quicksort | Hızlı ve pratik sıralama (D&C) |
| Hash Tables | O(1) anahtar-değer erişimi |
| BFS | Graflarda en kısa yol (ağırlıksız) |
| Dijkstra | Ağırlıklı graflarda en kısa yol |
| Greedy | Yerel optimal seçimlerle hızlı çözüm |
| Dynamic Programming | Alt problemleri saklayarak optimal çözüm |
| KNN | Benzerlik tabanlı sınıflandırma/tahmin |

### Kitapta Bahsedilen Ama Derinleşilmeyen Konular

Bunları daha sonra araştırmanı öneririm:

| Konu | Kısa Açıklama |
|---|---|
| **Trees (Ağaçlar)** | Binary Tree, Binary Search Tree — veritabanı index'lerinin temeli |
| **B-Trees** | Veritabanlarının gerçekte kullandığı ağaç yapısı |
| **Red-Black Trees** | Kendini dengeleyen arama ağacı |
| **Heaps** | Priority Queue implementasyonu — Dijkstra'da kullanılır |
| **Inverted Index** | Arama motorlarının temeli (Google, Elasticsearch) |
| **Fourier Transform** | Ses/görüntü işleme, sıkıştırma (Shazam bunu kullanır!) |
| **MapReduce** | Büyük veri üzerinde paralel hesaplama (Hadoop) |
| **Bloom Filters** | "Bu eleman sette var mı?" sorusuna hızlı (olasılıksal) cevap |
| **SHA / HyperLogLog** | Hash fonksiyonları ve olasılıksal veri yapıları |
| **Merge Sort** | Stabil, garantili $O(n \log n)$ sıralama |
| **DFS** | Depth-First Search — derinlik öncelikli graf araması |
| **Diffie-Hellman** | Şifreleme — iki taraf güvenli kanal OLMADAN gizli anahtar paylaşabilir |
| **Parallel Algorithms** | İşi çekirdeklere dağıt, AMA Amdahl Yasası: her iş paralelleşmez! |
| **Linear Programming** | Kısıtlar altında optimizasyon — kaynak tahsisi, planlama problemleri |

### 🏢 Büyük Şirketlerde Bu Algoritmalar

```
Bu kitaptaki algoritmalar soyut görünebilir ama HER GÜN kullanılıyor:

GOOGLE:
  → Binary Search varyantları → Search autocomplete, sorted index'ler
  → Hash Tables → Bigtable, Memcached, distributed cache
  → BFS/DFS → Web crawling (tüm interneti gezmek!)
  → Dijkstra (A* versiyonu) → Google Maps rota hesaplama
  → MapReduce → Milyarlarca sayfa index'leme
  → PageRank → graf algoritması (BFS tabanlı)

NETFLIX:
  → KNN benzeri → Film önerisi (collaborative filtering)
  → Dynamic Programming → Per-title video encoding (sahne başına optimal bitrate)
  → Hash Tables → Session cache, user profile lookup

AMAZON:
  → DP → "Customers who bought this also bought" (benzerlik algoritmaları)
  → Greedy → Depo yerleşim optimizasyonu
  → Hash Tables (DynamoDB) → Tüm e-ticaret altyapısının temeli

LINKEDIN:
  → BFS → "People You May Know" (2. ve 3. derece bağlantılar)
  → Graph algoritmaları → Sosyal ağ analizi

UBER/GRAB:
  → Dijkstra/A* → Gerçek zamanlı rota hesaplama
  → KNN benzeri → En yakın şoförü bulma

SPOTIFY:
  → KNN → Discover Weekly playlist önerisi
  → Hash → Şarkı ID lookup, cache
```

### 🤖 Yapay Zeka Çağında Algoritma Bilgisi

```
"Copilot/ChatGPT kod yazıyor, algoritma öğrenmeme gerek var mı?"
EVET! İşte neden:

1. AI'NIN ÜRETTİĞİ KODU DEĞERLENDİRMEN LAZIM
   → AI sana O(n²) çözüm verdi → sen O(n log n) isteyeceğini bilmelisin!
   → "Bu çözüm 1M veri ile çalışır mı?" sorusunu AI değil SEN sorarsın.

2. DOĞRU PROMPTU YAZMAK İÇİN
   → Kötü prompt: "Bu diziyi sırala"
   → İyi prompt: "Bu diziyi O(n log n) ile in-place sırala, stability önemli değil"
   → Algoritma bilgisi → daha iyi prompt → daha iyi kod!

3. SİSTEM TASARIMINDA AI YETMEZ
   → "Bu veri Redis'te hash table olarak mı saklanmalı, 
      yoksa PostgreSQL'de B-Tree index'li mi?"
   → Bu karar domain + algoritma bilgisi gerektirir!

4. EMBEDDING VE VECTOR DB'LER
   → Modern AI'ın temeli: metin → vektör (embedding) → KNN ile en yakın sonucu bul
   → RAG (Retrieval-Augmented Generation) = "soruyu vektöre çevir → KNN araması yap
      → en yakın belgeleri LLM'e bağlam olarak ver"
   → KNN anlamadan modern AI mimarisini ANLAYAMAZSIN!

5. AI HALÜSÜNASYON YAPAR
   → AI "bu O(log n)" diyebilir ama gerçekte O(n²) olabilir
   → Big O bilgisi olmadan bunu YAKALAYAMAZSIN!

ÖRNEK PROMPT'LAR:

  "Bu fonksiyon O(n²). Bunu O(n log n) veya O(n) ile optimize et.
   Memoization kullanabilirsin."

  "Bu graph traversal'da BFS yerine Dijkstra kullan,
   edge weight'ler pozitif tam sayı."

  "Bu arama fonksiyonunu binary search ile yeniden yaz.
   Input array sorted olduğunu varsay."
```

### Topluluk Görüşleri 💬

```
Bu kitap hakkında yazılım topluluğunun söylediği önemli şeyler:

✅ "Grokking Algorithms, algoritma öğrenmek için EN İYİ 
    İLK KİTAP. Ama son kitap olmamalı!"
    — Hacker News, Reddit r/learnprogramming genel kanı

✅ "Kitabın illüstrasyonları süper güç. Metinle anlatırken
    çizimlerin gücünü kaybediyorsun."
    — Bu yüzden ASCII diyagramlarımızı kullanıyoruz! 😄

✅ "Bu kitaptan sonra 'The Algorithm Design Manual' (Skiena)
    veya CLRS ile derinleş."

⚠️ "Kitap Dijkstra'yı sadece basit haliyle anlatıyor.
    Gerçek dünyada A* kullanılıyor (Dijkstra + heuristic).
    Google Maps gibi uygulamalar A* ve Contraction Hierarchies kullanır."

⚠️ "Quicksort'un in-place implementasyonu anlatılmıyor,
    filter-based versiyon bellek açısından verimsiz.
    Gerçek uygulamalarda Lomuto/Hoare partition kullanılır."
```

### Öğrenmeye Devam Etmek İçin 📚

1. **LeetCode** — Algoritma problemleri çöz (Easy'den başla!)
2. **"Introduction to Algorithms" (CLRS)** — Daha derin matematiksel analiz
3. **"The Algorithm Design Manual" (Skiena)** — Pratik odaklı, gerçek dünya algoritmaları
4. **Visualgo.net** — Algoritmaları görsel olarak izle
5. **NeetCode.io** — LeetCode soruları kategorize edilmiş, video açıklamalı
6. **"Designing Data-Intensive Applications"** — Bu konuları gerçek sistemlerde nasıl kullanacağını öğren

---

> **Son söz:** Algoritmalar korkutucu görünebilir ama özünde hepsi birer **tarif**. Yumurta pişirmeyi öğrenmek gibi — ilk seferinde belki yakarsın, ama pratikle hem hızlanırsın hem de kendi tariflerini yaratmaya başlarsın. 🍳👨‍🍳
>
> **Öğrenmenin bir sonu yok, ama bir başlangıcı var. Ve sen o başlangıcı çoktan yaptın!** 💪
