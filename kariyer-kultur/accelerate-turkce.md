# 🚀 Accelerate — Türkçe Kapsamlı Rehber

> **"Hız ve istikrar bir ödünleşim değildir. En iyi ekipler İKİSİNİ birden başarır — ve bunu veriyle kanıtlıyoruz."**
> — Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (2018)

Bu rehber, yazılım teslimatı üzerine yapılmış **en büyük bilimsel araştırmayı** Türkçe olarak anlatır. Accelerate, "iyi mühendislik pratikleri işe yarar" fikrini bir inançtan **ölçülebilir bir gerçeğe** dönüştürür. DORA metrikleri buradan gelir.

---

## 📖 İçindekiler

1. [Neden Bu Kitap Farklı? — Bilim](#1--neden-bu-kitap-farklı--bilim)
2. [Dört Anahtar Metrik (DORA)](#2--dört-anahtar-metrik-dora)
3. [Büyük Yanılgı: Hız vs İstikrar](#3--büyük-yanılgı-hız-vs-i̇stikrar)
4. [Performansı Yükselten Yetenekler](#4--performansı-yükselten-yetenekler)
5. [Continuous Delivery](#5--continuous-delivery)
6. [Mimari: Gevşek Bağ](#6--mimari-gevşek-bağ)
7. [Kültür: Westrum Tipolojisi](#7--kültür-westrum-tipolojisi)
8. [Tükenmişlik ve Deployment Acısı](#8--tükenmişlik-ve-deployment-acısı)
9. [Büyük Şirketlerde Accelerate](#9--büyük-şirketlerde-accelerate)
10. [Son Sözler](#10--son-sözler)

---

## 1. 🔬 Neden Bu Kitap Farklı? — Bilim

```
ÇOĞU YÖNETİM KİTABI: anekdot + kişisel görüş + "bende işe yaradı".
ACCELERATE: 4 yıl, 2000+ organizasyon, on binlerce yanıt → İSTATİSTİK.

  → Yöntem: State of DevOps araştırması (DORA — DevOps Research & Assessment).
  → Anket verisi + istatistiksel analiz (cluster analysis, SEM — yapısal
    eşitlik modeli) → NEDENSELLİK iddiaları (korelasyon değil, prediktif).
  → Sonuç: "Şu pratikler, şu sonuçları İSTATİSTİKSEL OLARAK öngörür."
```

> **Neden önemli:** Accelerate'ten önce "CI/CD iyidir" bir inançtı. Accelerate'ten sonra bir **kanıttır** — ve hangi pratiklerin gerçekten fark yarattığını, hangilerinin gürültü olduğunu ayırt eder.

---

## 2. 📊 Dört Anahtar Metrik (DORA)

Kitabın en kalıcı mirası: yazılım teslimat performansını **yalnızca dört metrikle** ölçmek. İkisi hız, ikisi istikrar.

```
HIZ (throughput):
  1. DEPLOYMENT FREQUENCY (dağıtım sıklığı)
     → Ne sıklıkla üretime dağıtıyorsun? (Elite: günde birçok kez)
  2. LEAD TIME FOR CHANGES (değişiklik teslim süresi)
     → Commit'ten üretime kadar geçen süre? (Elite: < 1 saat)

İSTİKRAR (stability):
  3. CHANGE FAILURE RATE (değişiklik başarısızlık oranı)
     → Dağıtımların yüzde kaçı arıza/rollback gerektiriyor? (Elite: %0-15)
  4. TIME TO RESTORE SERVICE (hizmeti geri getirme süresi / MTTR)
     → Bir arıza olduğunda ne kadar sürede toparlıyorsun? (Elite: < 1 saat)
```

```
PERFORMANS SEVİYELERİ (kümeleme analizinden):
  ┌──────────┬─────────────┬────────────┬──────────────┬───────────────┐
  │          │ Deploy sık. │ Lead time  │ Fail rate    │ Restore süresi│
  ├──────────┼─────────────┼────────────┼──────────────┼───────────────┤
  │ ELITE    │ Günde çok   │ < 1 saat   │ %0–15        │ < 1 saat      │
  │ HIGH     │ Gün–hafta   │ Gün–hafta  │ %0–15        │ < 1 gün       │
  │ MEDIUM   │ Hafta–ay    │ Hafta–ay   │ %0–15        │ < 1 gün       │
  │ LOW      │ Ay–6 ay     │ Ay–6 ay    │ Daha yüksek  │ Gün–hafta     │
  └──────────┴─────────────┴────────────┴──────────────┴───────────────┘
```

> **Kritik nokta:** Bu dört metrik hem **hızı** hem **istikrarı** ölçer. Sadece hızı ölçersen kaliteyi feda edersin; sadece istikrarı ölçersen donarsın. Dördü birlikte, sağlıklı bir teslimat sisteminin dengeli göstergesidir.

*(Not: Daha sonra DORA beşinci bir metrik ekledi: **Reliability** — operasyonel güvenilirlik/SLO'lara uyum.)*

---

## 3. ⚖️ Büyük Yanılgı: Hız vs İstikrar

```
YAYGIN İNANÇ (yanlış):
  "Hızlı gidersek kalite düşer. Kaliteyi korumak için yavaşlamalıyız."
  → Bu yüzden ağır onay süreçleri, seyrek/dev dağıtımlar, change board'lar.

ACCELERATE'İN BULGUSU (veriyle):
  → Elite ekipler HEM daha hızlı HEM daha istikrarlı. İkisi AYNI YÖNDE hareket eder!
  → Küçük, sık dağıtım → her değişiklik küçük → hata bulmak/geri almak KOLAY →
    hem hız hem istikrar ARTAR.
  → "Hız için kaliteyi feda et" yanlış bir ikilem; iyi pratikler ikisini de verir.
```

```
NEDEN? (mekanizma)
  Büyük, seyrek dağıtım:  100 değişiklik bir arada → hata olursa hangisi? →
                          uzun teşhis, riskli rollback → yavaş VE kırılgan.
  Küçük, sık dağıtım:     1 değişiklik → hata bariz → saniyeler içinde geri al →
                          hızlı VE sağlam.
```

> **Staff dersi:** "Daha az sıklıkta dağıtırsak daha güvenli oluruz" sezgisi **tam tersidir.** Risk, dağıtım *sıklığında* değil, dağıtım *büyüklüğünde*dir. Küçük parti (small batch) hem Lean üretimin hem de Accelerate'in kalbidir.

---

## 4. 🛠️ Performansı Yükselten Yetenekler

Accelerate, yüksek performansı **istatistiksel olarak öngören** 24 yeteneği belirler. Hepsi bir arada, dört metriği yukarı çeker.

```
TEKNİK YETENEKLER (Continuous Delivery temeli):
  • Sürüm kontrolü (HER şey: kod, config, altyapı)
  • Deployment otomasyonu
  • Continuous Integration (sık merge, otomatik test)
  • Trunk-based development (kısa ömürlü dallar, hızlı merge)
  • Test otomasyonu (güvenilir, geliştiricinin sahiplendiği)
  • Test verisi yönetimi
  • Shift-left security (güvenliği sürece erken göm)
  • Gevşek bağlı mimari (bkz. bölüm 6)

SÜREÇ / LEAN YETENEKLERİ:
  • Küçük parti (small batch) çalışma
  • İş görünürlüğü (value stream boyunca)
  • WIP (devam eden iş) sınırlama
  • Görsel yönetim (dashboard'lar)
  • Müşteri geri bildirimini sürece katmak
  • Hafif değişiklik onayı (ağır CAB DEĞİL — bkz. aşağıda)

KÜLTÜREL YETENEKLER:
  • Westrum "generative" kültür (bkz. bölüm 7)
  • Öğrenme kültürü (öğrenme bir yatırım, maliyet değil)
  • Ekipler arası işbirliği
  • İş tatmini, çalışan sahiplenmesi
```

```
ŞAŞIRTICI BULGU — Değişiklik Onay Kurulları (CAB):
  → Ağır, harici change approval board'lar performansı ARTIRMAZ; genelde
    yalnızca YAVAŞLATIR ve istikrarı İYİLEŞTİRMEZ.
  → Daha iyisi: eşler arası review (peer review) + otomasyon → hem hızlı hem güvenli.
```

---

## 5. 🔁 Continuous Delivery

```
CD PRENSİBİ: Yazılım HER AN üretime alınabilir durumda olmalı.
  → "Dallanıp aylarca entegre etmemek" değil; SÜREKLİ entegre + SÜREKLİ dağıtılabilir.

CD'NİN TEMEL PRATİKLERİ (Accelerate'in ölçtüğü):
  ✓ Her şey sürüm kontrolünde (kod + config + altyapı-as-code)
  ✓ Süreci otomatikleştir (build, test, deploy)
  ✓ Trunk-based development: kısa ömürlü dallar, günde en az bir merge
  ✓ Kaliteyi içine göm (test, güvenlik erken)
  ✓ "Deploy" ile "release"i ayır (feature flag)
  ✓ Pipeline yeşil DEĞİLSE herkes durur, önce onu düzeltir
```

> Bu, [The Phoenix Project](the-phoenix-project-turkce.md)'in roman diliyle anlattığı akışın **ölçülmüş** hâlidir; ve [Build, Release & Supply Chain](../pratik/build-release-supply-chain.md) dokümanı bunun modern araç karşılığıdır.

---

## 6. 🧩 Mimari: Gevşek Bağ

Accelerate'in en güçlü teknik bulgularından biri:

```
YÜKSEK PERFORMANSIN EN BÜYÜK BELİRLEYİCİLERİNDEN BİRİ:
  → Ekiplerin, DİĞER ekiplerden BAĞIMSIZ olarak:
    • Sistemlerini test edebilmesi (entegrasyon ortamı beklemeden)
    • Sistemlerini dağıtabilmesi/değiştirebilmesi (başka ekibin izni olmadan)
  → Bu "deployability + testability" bağımsızlığı, dört metriği güçlü öngörür.

  → Mimari, TAKIM bağımsızlığını mümkün kılmalı. Sıkı bağlı mimari →
    her değişiklik koordinasyon → yavaş VE kırılgan.
```

> Bu doğrudan [Team Topologies](team-topologies-turkce.md) (bağımsız stream-aligned takımlar) ve [gevşek bağlı mimari](../mimari-tasarim/fundamentals-of-software-architecture-turkce.md) ile örtüşür. Üçü birlikte okunur: bağımsız takım + gevşek mimari + CD = hızlı akış.

---

## 7. 🌿 Kültür: Westrum Tipolojisi

Accelerate, örgüt kültürünü ölçmek için sosyolog Ron Westrum'un modelini kullanır — ve kültürün performansı **öngördüğünü** bulur.

```
ÜÇ KÜLTÜR TİPİ (bilgi nasıl akar?):
  1. PATHOLOGICAL (patolojik / güç-odaklı):
     → Bilgi saklanır, hatalar cezalandırılır, sorumlu aranır.
     → Haberci vurulur; kötü haber gizlenir.
  2. BUREAUCRATIC (bürokratik / kural-odaklı):
     → Bilgi departman sınırlarında takılır; kurallar/kutucuklar öncelik.
  3. GENERATIVE (üretken / performans-odaklı): ⭐ HEDEF
     → Bilgi AKAR, hatalar ÖĞRENME fırsatıdır, sorumluluk paylaşılır.
     → Haberci ödüllendirilir; kötü haber hızlı yüzeye çıkar → hızlı düzeltilir.
```

```
BULGU: Generative kültür → daha iyi yazılım teslimatı + daha az tükenmişlik.
  → "Blameless postmortem" bir generative kültür pratiğidir (bkz. SRE).
  → Suçlama kültürü, bilgiyi saklatır → sorunlar gizlenir → felaketler büyür.
```

> Bu, [SRE Pratiği — blameless postmortem](../pratik/sre-pratigi.md) ve [Postmortem şablonu](../templates/postmortem-sablon.md) ile birebir hizalanır: hatayı kişide değil sistemde ara.

---

## 8. 🔥 Tükenmişlik ve Deployment Acısı

```
ACCELERATE İNSANI DA ÖLÇER:
  • DEPLOYMENT PAIN (dağıtım acısı): dağıtım ne kadar stresli/korkulu?
    → Yüksek acı → gece dağıtımları, "cuma deploy yasak", el titremesi.
    → Yüksek acı, düşük performans ve YÜKSEK tükenmişlikle ilişkili.
    → Çözüm: dağıtımı otomatik, küçük, sık ve GERİ ALINABİLİR yap → acı düşer.

  • BURNOUT (tükenmişlik): teknik + kültürel iyi pratikler tükenmişliği AZALTIR.
    → İyi mühendislik yalnızca hızı değil, İNSANI da korur.
```

> **Staff dersi:** "Dağıtımdan korkuyoruz" bir kültür veya kişi sorunu değil, bir **sistem sinyalidir**: küçük parti + otomasyon + geri alınabilirlik eksik. Acıyı çözmek moral konuşması değil, mühendislik işidir.

---

## 9. 🏢 Büyük Şirketlerde Accelerate

```
GERÇEK DÜNYA ETKİSİ:
  • DORA metrikleri sektör STANDARDI oldu: çoğu mühendislik org'u
    deploy frequency / lead time / MTTR / change fail rate izler.
  • "Elite performer" hedefi, dönüşüm programlarının ortak dili.
  • Platform mühendisliği + CD + trunk-based, Accelerate bulgularının
    doğrudan uygulaması.
  • Google/DORA her yıl State of DevOps raporunu yayımlamaya devam ediyor
    (yeni bulgular: platform, dokümantasyon kalitesi, ve AI'ın teslimata etkisi).
```

```
YAYGIN HATALAR:
  ✗ Metrikleri HEDEF yapıp oyunlamak ("deploy sayısını artıralım" → boş deploy).
    → Metrikler bir sağlık göstergesidir, bir KPI kamçısı değil (Goodhart yasası).
  ✗ Sadece hızı kovalayıp istikrar metriklerini görmezden gelmek.
  ✗ Araç almakla dönüşüm sandırmak (Jenkins kurmak ≠ CD kültürü).
  ✗ Kültürü (Westrum) atlayıp yalnızca teknik pratiklere yatırım yapmak.
```

---

## 10. 🎬 Son Sözler

```
ACCELERATE — 6 ALTIN KURAL:
  1. Yazılım teslimatını 4 metrikle ölç: deploy sıklığı, lead time,
     change fail rate, restore süresi (hız + istikrar birlikte).
  2. Hız ve istikrar ödünleşim DEĞİL — iyi pratikler ikisini birden verir.
  3. Risk, dağıtım büyüklüğündedir; küçük parti + sık dağıtım güvenlidir.
  4. Gevşek bağlı mimari + bağımsız takım = hızlı akışın teknik temeli.
  5. Generative kültür (bilgi akar, hata öğrenmedir) performansı öngörür.
  6. Metrikler sağlık göstergesidir, oyunlanacak KPI değil.
```

> **Kitabın son mesajı:** İyi mühendislik pratikleri bir "nice-to-have" değil, ölçülebilir bir **rekabet avantajıdır** — ve hem sistemi hem insanı korur. Artık tahmin etmene gerek yok; **ölç, öğren, iyileştir.**

---

## 📚 İleri Okuma

- Forsgren, Humble, Kim — *Accelerate* (2018) — kitabın kendisi
- Google/DORA — *State of DevOps* raporları (yıllık, güncel bulgular; dora.dev)
- Humble & Farley — *Continuous Delivery* (2010) — CD'nin temel kitabı
- Bu repo: [The Phoenix Project](the-phoenix-project-turkce.md) · [Team Topologies](team-topologies-turkce.md) · [Build, Release & Supply Chain](../pratik/build-release-supply-chain.md) · [SRE Pratiği](../pratik/sre-pratigi.md)

---

> [⬅️ Kariyer & Kültür](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
