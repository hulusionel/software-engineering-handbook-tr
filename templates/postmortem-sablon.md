# 📋 Postmortem — Şablon (Blameless)

> **Kaynak:** Google SRE Workbook + Etsy "Blameless Postmortems" + PagerDuty IR docs.
> **Felsefe:** *"Hata kişide değil sistemdedir. Bireyleri suçlayan postmortem ekibi suskunlaştırır; sistemi değiştirmez."*

---

## Postmortem: [Kısa, açıklayıcı başlık — örn. "API gateway 47 dakika 5xx üretti"]

| Alan | Değer |
|---|---|
| **Olay tarihi** | YYYY-MM-DD HH:MM (UTC) — HH:MM (UTC) |
| **Süre** | X saat Y dakika |
| **Severity** | SEV1 / SEV2 / SEV3 |
| **Etkilenen servis(ler)** | … |
| **Incident commander** | … |
| **Yazar(lar)** | … |
| **Durum** | Taslak / Gözden geçirme / Yayınlandı |

---

## 🎯 Özet (TL;DR)

3-5 cümle. Ne oldu, ne kadar sürdü, kim etkilendi, kök neden bir cümleyle, ne öğrendik.

## 📊 Etki

- **Kullanıcı etkisi:** Etkilenen kullanıcı sayısı / oranı, hangi feature'lar.
- **İş etkisi:** Tahmini gelir kaybı, SLA ihlali, regülasyon raporlama yükümlülüğü.
- **Hata bütçesi tüketimi:** Bu olay error budget'ın %X'ini yedi (geri kalan: %Y).
- **Müşteri iletişimi:** Hangi kanaldan, hangi mesaj.

## ⏱️ Zaman Çizelgesi

UTC. Olduğu gibi, **yorumsuz**. *Saçmalık* tespitleri "Analiz" bölümünde.

| Saat (UTC) | Olay |
|---|---|
| 14:23 | Deployment X yayında. |
| 14:25 | Sentry'de 5xx artışı, ekip henüz fark etmedi. |
| 14:31 | PagerDuty alarmı tetiklendi (p99 > 1s, 5 dk). |
| 14:32 | On-call ack. |
| 14:38 | İlk hipotez: DB yavaşlığı. Yanlış çıktı. |
| 14:51 | Doğru hipotez: yeni cache key formatı eski client'ları kırıyor. |
| 14:54 | Rollback başlatıldı. |
| 15:10 | Rollback tamamlandı, metrikler normal. |
| 15:15 | Customer comms gönderildi. |

## 🕵️ Kök Neden Analizi

> **Kök neden tek bir şey değildir.** Bir kişi/araç/satır değil; bir **olaylar zinciri** + bir **sistem zayıflığıdır**.

**5 Why** veya **Ishikawa** kullan:

1. *Neden 5xx üretti?* — Cache miss'te DB sorgusu yavaştı.
2. *Neden cache miss?* — Yeni deployment cache key formatını değiştirdi.
3. *Neden eski client kırıldı?* — Backward compatibility shim eklenmedi.
4. *Neden eklenmedi?* — Code review'da kaçtı.
5. *Neden review'da kaçtı?* — Cache key değişiklikleri için checklist yok.

> **Sistemik zayıflık:** Cache key kontratı için contract test yok; review checklist'i yok; canary deployment %1 değil %100 başlıyor.

## 🔬 Katkıda Bulunan Faktörler

| Faktör | Açıklama |
|---|---|
| **Deployment süreci** | Canary olmadan %100 deploy. |
| **Test eksiği** | Eski client uyumluluk testi yok. |
| **Gözlem körlüğü** | Cache miss rate dashboard'da yok. |
| **Bilgi asimetrisi** | Cache değişikliklerinin etkisini yalnız 1 kişi biliyordu (bus factor 1). |
| **Alert gecikmesi** | İlk 5xx ile alert arası 6 dk. |

## ✅ İyi Giden Şeyler

> Bu bölümü atlamak postmortem kültürünü öldürür. **Her zaman yaz.**

- Rollback prosedürü beklenen sürede çalıştı.
- Incident command yapısı net işledi.
- Müşteri iletişimi 30 dk içinde gitti.

## 🚧 Kötü Giden Şeyler

- İlk hipotez yanlıştı, 13 dk kayıp.
- Dashboard'larda cache metric yoktu.

## 🍀 Şanslı Olduğumuz Şeyler

> *"Bunu farklı bir saatte fark etseydik N kat daha kötüydü."*

- Olay öğle saatinde değil, sabah erken saatte oldu — düşük trafik.

## 📚 Aksiyonlar (Action Items)

> Her aksiyon: **somut**, **sahibi olan**, **tarihli**, **ölçülebilir**.
> "Daha dikkatli olalım" aksiyon değildir.

| ID | Aksiyon | Tip | Sahip | Termin | Durum |
|---|---|---|---|---|---|
| AI-001 | Cache key kontratı için contract test ekle | Önleyici | @alice | YYYY-MM-DD | … |
| AI-002 | Canary deployment %1→%10→%50→%100 zorunlu hale getir | Süreç | @bob | YYYY-MM-DD | … |
| AI-003 | Cache miss rate'i SRE dashboard'una ekle | Tespit | @carol | YYYY-MM-DD | … |
| AI-004 | "Cache değişikliği" review checklist'i | Süreç | @dan | YYYY-MM-DD | … |
| AI-005 | Bus factor: cache modülü için 2. owner ata | Organizasyon | @lead | YYYY-MM-DD | … |

**Aksiyon türleri:**
- **Önleyici (Preventive):** Aynı kök nedenin tekrarını imkansızlaştırır.
- **Tespit (Detective):** Aynı sınıf olayı daha hızlı yakalar.
- **Hafifletici (Mitigating):** Gerçekleştiğinde etkisini azaltır.
- **Süreç:** Code review, deployment, on-call.
- **Organizasyon:** Bilgi paylaşımı, sahiplenme, eğitim.

## 🧠 Öğrendiklerimiz (Lessons)

3-5 madde. **Genelleştirilebilir** içgörüler — sadece bu olayı değil, gelecek olayları da aydınlatan.

- Cache anahtar formatları **API'dir**. Versionlanmadan değiştirilmez.
- Canary olmayan deployment **kabul edilemez** (her hız iddiasına rağmen).

## 📎 Ekler

- Grafana / Datadog snapshot link'leri (zaman aralığıyla).
- Slack / chat log özeti (PII redacted).
- İlgili PR'lar, deployment ID'leri.
- Önceki ilgili postmortem'lere link.

---

## ⚖️ Blameless İlkeler

1. **Birey adı yerine rol.** *"on-call mühendis"* — eğer öğretici değilse.
2. **Niyet doğru kabul edilir.** *"Operatör elinden geleni mantıklı bilgilerle yaptı."*
3. **Soru sor, suçlama.** *"Bu noktada hangi bilgiye sahiptin?"*
4. **Sistem soruları sor.** *"Bu hatayı imkansız kılacak ne kursak?"*
5. **Hatayı paylaş.** Postmortem'i dahili olarak herkese aç. Sadece SEV1 değil; SEV2/3 dahil.
6. **Aksiyonları takip et.** Tamamlanmayan aksiyon, postmortem'in yalanı olur.

## 🚫 Postmortem Anti-Pattern'leri

- ❌ **Suçlu arama** ("X bunu yapmasaydı")
- ❌ **Hindsight bias** ("Açıkçası bu olacaktı")
- ❌ **Vague aksiyonlar** ("Daha dikkatli olalım")
- ❌ **Aksiyon enflasyonu** (40 madde, hiçbiri tamamlanmaz)
- ❌ **Yayımlanmayan postmortem** (organizasyonel öğrenme yok)
- ❌ **"Human error"** ile bitirme (her insan hatası bir sistem zayıflığıdır)
