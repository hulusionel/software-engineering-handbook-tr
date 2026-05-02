# 📰 Amazon 6-Pager — Şablon (Türkçe)

> **Bağlam:** Amazon yönetici toplantılarında PowerPoint **yasaktır**. Yerine 6 sayfalık (max ~4500 kelime) bir memo okunur. İlk 20-30 dakika herkes **sessizce** okur. Sonra tartışılır.
> **Amaç:** Karar vericinin slayt güzelliğine değil, **argümanın berraklığına** odaklanmasını sağlamak.

---

## Başlık: [Kararın bir cümlede özeti]

**Tarih:** YYYY-MM-DD · **Yazar:** [İsim] · **Karar verici:** [İsim/rol] · **Toplantı tarihi:** YYYY-MM-DD

> Memo **akıcı düz yazıyla** yazılır. Madde işareti, slayt başlığı **kullanılmaz**. Tablo ve grafik ek (appendix) olarak en sona konur.

---

## 1. Giriş (½ sayfa)

Bir paragrafta: *Hangi sorun, kim için, neden şimdi, biz ne öneriyoruz, ne karar bekliyoruz.*

Ardından **bir paragraf bağlam** — okuyucu başka bir konudan geliyor olabilir.

## 2. Müşteri / Sorun (1 sayfa)

Sorunu **kullanıcının dilinden** anlat. Anonim alıntı, gerçek metrik, gerçek hikaye. *"Geliştiriciler haftada ~6 saat manuel rebase ile uğraşıyor"* türü somut tespit.

Ardından sorunu **işten** açıkla: gelir kaybı, takım hızı, risk. Yine sayılarla.

## 3. Önerilen Çözüm (1.5 sayfa)

Çözümü düz yazıyla anlat. **Implementation detayına girme** — RFC bu işi yapar. Burada:

- Çözüm cümlesi (1 paragraf).
- Çözümün getireceği davranış değişikliği (kullanıcı / sistem cephesinden).
- Neden bu yaklaşım — *artıları sıralarken* alternatifleri yargılamadan, neden bu yaklaşımın "sorun-çözüm uyumu" en iyi olduğunu yaz.

## 4. Alternatifler (½ sayfa)

Her alternatif için **bir paragraf**:
- Ne öneriyor, neden cazip, neden seçmedik.
- "Hiçbir şey yapmama" alternatifi dahil.

## 5. Etki & Maliyet (1 sayfa)

- **Mühendislik maliyeti:** N kişi × M hafta. Hangi ekiplerin time-slice'ı.
- **Operasyonel maliyet:** Aylık $X. 1 yıllık TCO.
- **Risk:** İlk 3 risk + hafifletme.
- **Sayısal hedef:** p99 ≤ Y ms, error rate ≤ Z%, aylık maliyet ≤ $W.
- **Bağımlılıklar:** Hangi ekip, hangi vendor, hangi onay.

## 6. Yol Haritası & Karar Talebi (½ sayfa)

- Mil taşları (F0 → F4) tarihleriyle.
- Tersine çevrilemez (one-way door) noktalar işaretli.
- **Karar talebi:** *"Bu memo'dan çıkışta, X kararını veriyor muyuz?"*

---

## EK A — Sıkça Sorulacak Sorular (FAQ)

> Bu bölüm **6 sayfanın dışında**. Anticipated questions + cevapları. *İyi 6-pager FAQ'i okumadan da anlaşılır; FAQ "vakitten kazanmak için" vardır.*

- **S1:** Neden bunu üçüncü partiden almıyoruz?
  **C:** …
- **S2:** Bunu yapmazsak en kötü ne olur?
  **C:** …
- **S3:** Bu karar 1 yıl sonra yanlış çıkarsa ne yaparız?
  **C:** …

## EK B — Veri / Tablolar / Grafikler

Müşteri sayıları, latency dağılımı, maliyet kalemleri. Her grafik tek başına anlaşılabilir olmalı (caption + eksen + birim).

## EK C — Kaynaklar

- İlgili ADR ve RFC'ler
- Önceki postmortem'ler
- Paper/RFC atıfları

---

## ✍️ 6-Pager Yazma İlkeleri

1. **Düz yazı, madde işaretsiz.** Madde işareti kelimeyi kelimeden, fikri fikirden ayırır — Bezos buna karşıdır.
2. **Sayfa sayısına sadık kal.** 6 sayfayı geçen memo karar dokümanı değil; tasarım dokümanıdır.
3. **Önce yaz, sonra kısalt.** İlk taslak iki katı uzunluğunda olur. Editleme yazmanın yarısı kadar zaman alır.
4. **Veri olmadan iddia yazma.** *"Önemli ölçüde"* yerine *"%23"*.
5. **Karşı argümanı kendin yaz.** FAQ'in yarısı *senin önerin neden yanlış olabilir* sorularına gitmeli.
6. **Sessiz okuma süresi**ne hazırla. Memo, dünya senin sözlü açıklamalarına ihtiyaç duymadan okunmalı.

## 🎯 6-Pager vs PRFAQ

| | 6-Pager | PRFAQ |
|---|---|---|
| Kim için | İç karar | Yeni ürün/girişim |
| Yapı | Memo | Sahte basın bülteni + FAQ |
| Müşteri sesi | Anekdotsal | Birinci sınıf vatandaş |
| Aşama | Karar öncesi | Working backwards (kavram) |

> 6-pager **karar memo'sudur**. PRFAQ **vizyon memo'sudur**. İkisi karıştırılmamalı.
