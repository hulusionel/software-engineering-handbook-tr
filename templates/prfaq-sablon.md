# 📣 Amazon PRFAQ — Şablon (Türkçe)

> **Bağlam:** PRFAQ, Amazon'un **"Working Backwards"** (tersten çalışma) sürecinin çekirdeğidir. Ürünü inşa etmeden **önce**, sanki lansman günüymüş gibi bir **basın bülteni (PR)** ve ardından **Sıkça Sorulan Sorular (FAQ)** yazılır. Amaç: müşteri deneyimini net görmeden koda başlamamak.
> **Amaç:** *"Bu ürün gerçekten var olmayı hak ediyor mu?"* sorusunu, mühendislik maliyeti harcanmadan cevaplamak.
> **6-Pager'dan farkı:** 6-pager bir **karar** memo'sudur; PRFAQ bir **vizyon** memo'sudur. Müşteri sesi burada anekdot değil, **birinci sınıf vatandaştır**. Bkz. [6-Pager şablonu](6-pager-sablon.md).

---

## BÖLÜM 1 — Basın Bülteni (Press Release · 1 sayfa)

> Gerçek bir gazeteci bunu yayınlayabilecekmiş gibi yaz. **Gelecek zamanla, lansman günü perspektifinden.** Jargon ve iç terminoloji yasak — bülteni müşteri okuyacak.

**Başlık:** [Ürünün müşteri için ne yaptığını anlatan tek satır]

**Alt başlık:** [Hedef müşteri + temel fayda — bir cümle]

**[Şehir, YYYY-AA-GG]** — Giriş paragrafı: Ürün nedir, kim için, hangi sorunu çözüyor, bugünden itibaren neden farklı. *Okuyucu tek bu paragrafı okusa bile ne olduğunu anlamalı.*

**Sorun paragrafı:** Bugün müşteri hangi acıyı çekiyor? Somut, gerçek, sayısal. Ürün olmadan hayatın nasıl olduğunu anlat.

**Çözüm paragrafı:** Ürün bu sorunu nasıl ortadan kaldırıyor? Nasıl çalıştığını değil, **müşteriye ne hissettirdiğini** anlat.

**Şirket sözcüsü alıntısı:** *"[Neden bu ürünü yaptık, hangi inanca dayanıyor]"* — [İsim, rol].

**Müşteri alıntısı:** *"[Ürünü kullanan hayali ama gerçekçi bir müşterinin, hayatının nasıl değiştiğini anlatan sözü]"* — [Müşteri adı, rolü].

**Nasıl başlanır (call to action):** Müşteri bugün ilk adımı nasıl atar? (Tek cümle.)

---

## BÖLÜM 2 — Müşteri SSS (External FAQ)

> Bir müşterinin / basının soracağı sorular. Ürünü **dışarıdan** gören birinin merakı.

- **Bu tam olarak nedir ve kimin için?**
  …
- **Ne kadara mal olur / fiyatlandırma nasıl?**
  …
- **Mevcut alternatiflerden / rakiplerden farkı ne?**
  …
- **Verilerim/gizliliğim ne olacak?**
  …
- **Ne zaman ve nerede kullanılabilir olacak?**
  …

---

## BÖLÜM 3 — İç SSS (Internal FAQ)

> **PRFAQ'in en zor ve en değerli kısmı.** Burada dürüst ol: en sert soruları **kendine** sor. Bir fikir buradaki sorularda ölürse, kod yazılmadan öldüğü için **ucuz** ölmüştür.

### Müşteri & Pazar
- **Bu sorunun gerçekten var olduğunu nereden biliyoruz?** (Kanıt: veri, görüşme, mevcut davranış.)
- **Toplam adreslenebilir pazar (TAM) ne kadar? İlk 12 ayda kaç müşteri?**
- **Müşteri bugün bu sorunu nasıl çözüyor ve bizimki neden 10× daha iyi?**

### Ürün & Kapsam
- **MVP kapsamı nedir? İlk sürümde neyi bilinçli olarak *yapmıyoruz*?**
- **Başarıyı nasıl ölçeceğiz?** (Kuzey Yıldızı metriği + karşı-metrik.)
- **En riskli varsayımımız ne, ve onu en ucuz nasıl test ederiz?**

### Mühendislik & Operasyon
- **Teknik olarak en zor kısım ne? Bilmediğimiz ne var?**
- **Tahmini maliyet:** N kişi × M ay geliştirme + aylık $X operasyon.
- **Hangi tek-yönlü kapı (one-way door) kararlarını veriyoruz?** (Geri dönülemez olanlar.)
- **Bağımlılıklar:** Hangi ekip, vendor, yasal/uyumluluk onayı gerekiyor?

### Karar
- **Bunu *yapmazsak* ne olur?** ("Hiçbir şey yapmama" senaryosu.)
- **Bu ürünü öldürmemiz gerekseydi, hangi sinyali görürdük?**

---

## ✍️ PRFAQ Yazma İlkeleri

1. **Tersten çalış.** Önce müşteri deneyimini (PR) yaz, mühendislik çözümünü değil. Çözüm en sona kalır.
2. **Müşteri sesi anekdot değil, kanıttır.** Alıntılar gerçekçi olmalı; uydurma pazarlama cümlesi değil.
3. **İç FAQ acıtmalı.** En zayıf noktanı kendin bulmazsan, launch günü müşteri bulur.
4. **Bir sayfayı geçme (PR).** Basın bülteni bir sayfaya sığmıyorsa, ürün fikri henüz netleşmemiştir.
5. **Metrik olmadan başarı tanımlama.** "Kullanıcılar sevecek" değil, "aktivasyon oranı ≥ %X".
6. **Jargonsuz yaz.** PR bölümünde bir iç terim varsa, müşteri o cümleyi anlamaz — sil.

---

## 🎯 PRFAQ vs 6-Pager vs RFC

| | PRFAQ | 6-Pager | RFC / Design Doc |
|---|---|---|---|
| Soru | *Bunu yapmalı mıyız?* | *Bu kararı veriyor muyuz?* | *Bunu nasıl inşa ederiz?* |
| Aşama | Vizyon / kavram | Karar öncesi | İnşa öncesi |
| Müşteri sesi | Birinci sınıf | Anekdotsal | Yok/az |
| Çıktı | Git/gitme kararı | Onay | Teknik plan |

> Sıra genellikle: **PRFAQ** (yapmalı mıyız?) → **6-Pager** (onaylıyor muyuz?) → **[RFC](rfc-design-doc-sablon.md)** (nasıl?) → **[ADR](adr-sablon.md)** (yol boyunca kararlar).

---

## 📚 Kaynak

- Amazon — *Working Backwards* (Colin Bryar & Bill Carr, 2021)
- Bezos shareholder letters — 6-pager ve PRFAQ kültürünün kökeni

> [⬅️ Şablonlar](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
