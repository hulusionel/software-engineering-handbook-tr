# 📐 Architecture Decision Record (ADR) — Şablon

> **Kaynak:** Michael Nygard, *Documenting Architecture Decisions* (2011).
> **Amaç:** Mimari kararı, alındığı andaki bağlamla birlikte donduran kısa, sürüm-kontrollü, ekleme-değil-üzerine-yazma ile evrilen bir kayıt.
> **Uzunluk hedefi:** 1-2 sayfa. Daha uzunsa tasarım dokümanına (RFC) çıkar.

---

## ADR-NNNN: [Kararın kısa, fiil-içeren başlığı]

- **Durum:** Önerildi | Kabul edildi | Reddedildi | Geçersiz | ADR-XXXX ile değiştirildi
- **Tarih:** YYYY-MM-DD
- **Karar Verenler:** [İsim/rol — RFC süreciyle uyumlu]
- **Danışılanlar:** [İsim/rol]
- **Bilgilendirilenler:** [İsim/rol]
- **Etiketler:** `data` | `security` | `api` | `infrastructure` | …

### Bağlam

Sorunu, çevresel kısıtları ve karar gereksinimini **kararın alındığı andaki gerçeklikle** anlat. Bağlam **olgudur**, görüş (opinion) değil. Şunlar olmalı:

- Sorun cümlesi (1-2 cümle).
- Mevcut durum / status quo'nun zayıflığı.
- Tetikleyici (yeni gereksinim, ölçek, regülasyon, vb.).
- İlgili **iş kısıtları**: SLO, bütçe, takım kapasitesi, yasal sınırlar.
- İlgili **teknik kısıtlar**: mevcut yığın, sürüm, transitif bağımlılıklar.

### Karar

> Tek paragraf. *"X'i Y şekilde yapacağız çünkü Z."*

Ardından **uygulama notları** (max 5-10 madde):

1. ...
2. ...

### Değerlendirilen Alternatifler

Her alternatif için kısa blok:

#### A) [Alternatif adı]
- **Özet:** ...
- **Artılar:** ...
- **Eksiler:** ...
- **Neden seçilmedi:** ...

#### B) [Alternatif adı]
...

> **En az 2 reddedilen alternatif olmalı.** "Tek seçenek vardı" diyen ADR, ADR değildir.

### Sonuçlar

- **Pozitif:** Bu karar bize neyi açar? (yeni yetenekler, ölçek, hız.)
- **Negatif:** Bu karar bizden ne alır? (esnekliği, bir teknolojinin imkanlarını, bütçenin bir kısmını.)
- **Nötr / Bilinmeyen:** Riskler, izlenmesi gereken sinyaller.

### Doğrulama

Bu kararın **doğru olup olmadığını** ölçmek için ne izlenecek?

| Sinyal | Eşik | Kararı yeniden ele al |
|---|---|---|
| Örn: p99 latency | > 250 ms | 1 hafta |
| Örn: aylık egress maliyeti | > $X | sonraki sprint |

### İlgili Belgeler

- RFC-NNNN — [tasarım dokümanı]
- ADR-XXXX — [bağlı veya değiştirilen karar]
- Kaynakça'daki paper/RFC numaraları

---

## 🚫 ADR Olmayan Şeyler

- ❌ Implementasyon detayı (`hangi kütüphane çağrısı`)
- ❌ "İdeal mimari" makalesi
- ❌ Pazarlama yazısı
- ❌ Geriye dönük yazılan post-rationalization

## ✅ İyi ADR'ın 4 Testi

1. **Bağlamı bilmeyen biri** kararın *neden* alındığını anlayabilir mi?
2. **6 ay sonra** "biz ne düşünüyorduk?" sorusunu cevaplar mı?
3. Reddedilen seçenekler **dürüst** mü değerlendirilmiş?
4. Kararın **yanlışlanabileceği** sinyaller tanımlı mı?
