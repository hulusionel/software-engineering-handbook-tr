# 🛠️ AI ile Neler Yapılabiliyor — Yetenek Kataloğu

> **"2026'nın en büyük LLM trendi daha iyi metin üretmek değil; harekete geçen LLM'ler."**

Bu doküman "AI ne işe yarar" sorusuna somut, mühendis gözüyle cevap verir: **bugün gerçekten neler inşa edilebiliyor**, hangi olgunlukta, hangi mimariyle. Amaç ilham değil, **karar ve uygulama** rehberi. Yetenekleri değer/risk/olgunluk ekseninde ele alır.

---

## 📑 İçindekiler

1. [Yetenek Haritası — Büyük Resim](#1--yetenek-haritası--büyük-resim)
2. [Kod & Yazılım Mühendisliği](#2--kod--yazılım-mühendisliği)
3. [Bilgi & RAG (Doküman Zekâsı)](#3--bilgi--rag-doküman-zekâsı)
4. [Computer Use / Tarayıcı & GUI Agent'leri](#4--computer-use--tarayıcı--gui-agentleri)
5. [Metin İşleri: Üretim, Özet, Çıkarım, Sınıflandırma](#5--metin-i̇şleri-üretim-özet-çıkarım-sınıflandırma)
6. [Multimodal: Görüntü, Ses, Video](#6--multimodal-görüntü-ses-video)
7. [İş Akışı Otomasyonu & Agent'ler](#7--i̇ş-akışı-otomasyonu--agentler)
8. [Veri & Analiz](#8--veri--analiz)
9. [Ne Hafta Sonunda İnşa Edilebilir?](#9--ne-hafta-sonunda-i̇nşa-edilebilir)
10. [Olgunluk & Sınırlar](#10--olgunluk--sınırlar)
11. [İleri Okuma](#11--i̇leri-okuma)

---

## 1. 🗺️ Yetenek Haritası — Büyük Resim

```
LLM'LERİN 6 TEMEL YETENEĞİ (her uygulama bunların bileşimidir):
  1. ÜRETME     → metin/kod/plan üret (generation)
  2. DÖNÜŞTÜRME → özet, çeviri, format değiştirme, yeniden yazma
  3. ÇIKARIM    → belirsiz metinden yapılı veri (extraction)
  4. SINIFLANDIRMA → etiketle, yönlendir, moderasyon
  5. MUHAKEME   → çok adımlı çıkarım, planlama, karar (reasoning)
  6. EYLEM      → araç kullan, sistemleri sür (agentic) ← en yeni, en değerli
```

```
DEĞER × RİSK (nereden başlamalı):
  DÜŞÜK RİSK, HIZLI KAZANÇ  → copilot, özet, çıkarım, sınıflandırma (BURADAN BAŞLA)
  ORTA                      → RAG Q&A, içerik üretimi, kod üretimi
  YÜKSEK DEĞER, YÜKSEK RİSK → otonom agentic iş akışları, computer use
                              (guardrail + eval ile, kademeli aç)
```

---

## 2. 💻 Kod & Yazılım Mühendisliği

En olgun ve en yüksek benimseme alanı. "Otomatik tamamlama"nın çok ötesinde.

```
BUGÜN YAPILABİLENLER:
  • Agentic kodlama: repo'da gezen, test çalıştıran, çok-dosyalı değişiklik
    yapan, PR açan agent'ler (Claude Code, Cursor, benzerleri).
  • Test üretimi + kapsam artırma; hata ayıklama (log oku, hipotez üret, düzelt).
  • Büyük ölçekli refactor / migration (framework/dil geçişi, API güncelleme).
  • Kod inceleme (review) yardımcısı; güvenlik/stil taraması.
  • Legacy kod anlama: "bu 5000 satır ne yapıyor?" + dokümantasyon üretimi.
  • Spec -> iskele: gereksinimden çalışan taslak + testler.

MİMARİ KALIP: spec-driven + plan-first + test-korumalı döngü
  → Belirsizliği önce netleştir; riskli işte önce plan (salt-okunur), sonra uygula;
    agent test/lint çalıştırıp kendini doğrulasın.

DİKKAT: AI kodu da insan review'ından geçer — "makul görünen ama yanlış" en
  tehlikelisi. Bkz. [agentic §9 — AI ile kodlama](agentic-muhendislik.md#9--ai-ile-kodlama-pratiği).
```

---

## 3. 📚 Bilgi & RAG (Doküman Zekâsı)

Güncel/özel bilgiyi modele bağlamanın standart yolu. Halüsinasyonu azaltır, kaynak gösterir.

```
NE İNŞA EDİLİR:
  • İç bilgi tabanı Q&A (dokümantasyon, wiki, politika, sözleşme).
  • Müşteri destek asistanı (ürün dokümanına dayalı, kaynak-atıflı).
  • Araştırma asistanı: çok kaynağı tara, sentezle, atıf ver.
  • "Sohbet et" arayüzü: DB/dosya/API üstünde doğal dille sorgu.

RAG MİMARİSİ (üretim):
  Soru -> embedding -> vektör arama (+ anahtar-kelime = HİBRİT) -> RERANK ->
    en ilgili parçalar -> LLM (kaynakla) -> atıflı cevap
  → İyileştiriciler: chunking stratejisi, hibrit arama, reranker, GraphRAG
    (ilişkileri graf olarak), metadata filtresi.
  → Derinlik: [pratik/ai-ml-muhendisligi](../pratik/ai-ml-muhendisligi.md) (vektör DB, HNSW, RAGAS).
```

> **Staff dersi:** RAG'de kalite %80 **retrieval**tan gelir, %20 modelden. Kötü cevabın kök nedeni genelde "yanlış/eksik parça getirildi"dir — önce retrieval'ı ölç ve iyileştir.

---

## 4. 🖥️ Computer Use / Tarayıcı & GUI Agent'leri

En yeni ve en hızlı büyüyen sınır: agent'in **ekranı görüp fare/klavye kullanarak** yazılımları sürmesi (API olmasa bile).

```
NE YAPABİLİR:
  • API'si olmayan legacy yazılımı otomatikleştirme (ekranı görerek).
  • Web'de çok adımlı görev: form doldur, veri topla, rezervasyon, satın alma akışı.
  • Uçtan uca QA testi: uygulamayı gerçek kullanıcı gibi tıklayarak test etme.
  • Masaüstü veri girişi, tekrarlayan ofis işleri.
  → Örnekler: Anthropic "computer use", OpenAI "Operator", Google "Project Astra".

GERÇEKLİK KONTROLÜ (2026):
  ✗ Henüz kırılgan: karmaşık/uzun akışlarda hata oranı yüksek, yavaş, pahalı.
  ✗ Güvenlik yüzeyi büyük: ekrandaki içerik prompt injection taşıyabilir.
  ✓ İnsan-döngüde + dar kapsam + geri-alınabilirlik ile değerli.
  → Kritik/geri-alınamaz eylemde (ödeme, gönder, sil) MUTLAKA onay.
```

---

## 5. 📝 Metin İşleri: Üretim, Özet, Çıkarım, Sınıflandırma

En düşük riskli, en hızlı ROI veren kategori.

| İş | Örnek | Neden güçlü |
|---|---|---|
| **Üretim** | Taslak, e-posta, ürün açıklaması, ilan | İnsan-döngüde; hız kazancı yüksek |
| **Özetleme** | Toplantı, log, uzun rapor, thread | Bilgi aşırı yükünü sıkıştırır |
| **Çıkarım (extraction)** | Fatura/sözleşme/CV → yapılı veri (JSON) | Belirsiz metin → şema; deterministik doğrulanabilir |
| **Sınıflandırma & yönlendirme** | Destek bileti triage, moderasyon, duygu | Yüksek hacim, insan-üstü hız |
| **Çeviri & yeniden yazma** | Dil, ton, seviye değiştirme | Bağlam-duyarlı, akıcı |

```
"RESEARCH-TO-X" KALIBI (2026'da yaygın):
  → Prospekt hakkında oku (LinkedIn, haber, rapor) -> kişiselleştirilmiş
    e-posta taslağı. Aynı kalıp: research-to-brief, research-to-proposal.
```

---

## 6. 🎨 Multimodal: Görüntü, Ses, Video

Modeller artık yalnız metin değil; görür, duyar, üretir.

```
GÖRÜNTÜ: OCR/belge anlama (fatura, form, el yazısı), diyagram/ekran anlama,
  görsel arama, kalite kontrol (üretim hattı), tıbbi/uydu görüntü analizi (uzman
  gözetiminde), görsel üretim (tasarım/prototip).
SES: transkripsiyon, çağrı analizi/özet, sesli asistan, gerçek-zamanlı çeviri.
VİDEO: içerik analizi/özet, sahne arama, moderasyon.
BİRLEŞİK: "ekran görüntüsünü anla + eylem al" (computer use'un temeli).
```

---

## 7. ⚙️ İş Akışı Otomasyonu & Agent'ler

En yüksek iş değeri buradan geliyor: **çok adımlı iş süreçlerini uçtan uca yürüten** agent'ler ("dijital montaj hattı").

```
FONKSİYONEL ÖRNEKLER:
  • Satış: research-to-email, lead zenginleştirme, CRM güncelleme.
  • Destek: tier 1-2 çözümü (vakaların %60-80'i), gerisini insana devret.
  • Operasyon: sipariş/tedarik/takip koordinasyonu, IT/HR/finans akışları.
  • Yazılım: on-call ilk müdahale, bağımlılık güncelleme, log-triage.

MİMARİ: orchestrator-workers + insan-döngüde checkpoint + MCP ile araç/sistem
  entegrasyonu. Detay: [otonom-ve-oz-gelisen-sistemler](otonom-ve-oz-gelisen-sistemler.md).
```

> **Staff dersi:** Otomasyonda değer, "her şeyi otomatikleştirmek"te değil; **dar, tekrarlayan, doğrulanabilir bir süreci** güvenilir kılmakta. En başarılı uygulamalar tek bir sürtünme noktasını çözer — "her işi yapan asistan"ı değil.

---

## 8. 📈 Veri & Analiz

```
NE YAPILABİLİR:
  • Doğal dille veri sorgulama (text-to-SQL, "geçen çeyrek en çok satan 5 ürün?").
  • Yapısız veriyi yapılandırma (metin/PDF/e-posta → tablo).
  • Anomali/duygu/tema analizi (yorumlar, destek biletleri, anketler).
  • Otomatik rapor/dashboard yorumu ("bu grafikte ne oluyor?").
  • Kod üreterek analiz (agent Python yazıp çalıştırır → grafik/sonuç).

DİKKAT: sayısal doğruluk kritikse → LLM'i TEK doğrulayıcı yapma. Hesabı
  deterministik kod yapsın, LLM yorumlasın/yönlendirsin.
```

---

## 9. 🚀 Ne Hafta Sonunda İnşa Edilebilir?

Öğrenmek için somut, küçük projeler:

```
BAŞLANGIÇ:
  • Kişisel dokümanların üstüne RAG Q&A (notlarını sorgula).
  • E-posta/mesaj taslağı üreten + tona uyarlayan asistan.
  • PDF/fatura → JSON çıkaran + doğrulayan araç.
ORTA:
  • Bir API'yi tool olarak veren küçük agent (hava, takvim, GitHub).
  • Kod tabanında "bu nasıl çalışır?" sorularını yanıtlayan repo-asistanı.
  • Bir eval seti + LLM-as-judge ile "prompt'umu ölçen" mini pipeline.
İLERİ:
  • MCP sunucusu yazıp kendi aracını her agent'e açmak.
  • Orchestrator + alt-agent'lerle çok kaynaklı araştırma asistanı.
  • Gece çalışan, test-korumalı küçük bakım agent'i (bağımlılık güncelleme).
```

---

## 10. ⚖️ Olgunluk & Sınırlar

```
OLGUN (güven yüksek):      copilot, özet, çıkarım, sınıflandırma, RAG Q&A, kod yardımı
GELİŞMEKTE (dikkatli):     agentic iş akışları, kod agent'leri, multimodal analiz
SINIR/KIRILGAN (2026):     uzun otonom computer use, denetimsiz çok-agent,
                           yüksek-riskli otonom karar

DEĞİŞMEYEN SINIRLAR:
  ✗ Determinizm yok → kritik/tekrarlanabilir işte deterministik kontrol ekle.
  ✗ Halüsinasyon → kritik olguyu kaynağa/koda bağla.
  ✗ Nihai sorumluluk İNSANDA (etik/hukuki/yüksek-etkili karar).
  → En olgun mimari: agent muhakeme eder, klasik kod GARANTİ eder.
```

---

## 11. 📚 İleri Okuma

- Anthropic — *Building Effective Agents* / *Computer Use* dokümantasyonu
- Enterprise LLM use-case derlemeleri (AssemblyAI, n-ix, 2026)
- Lewis et al. 2020 — *Retrieval-Augmented Generation* (RAG temeli)
- Bu repo: [Agentic Mühendislik](agentic-muhendislik.md) · [En İyi Pratikler](en-iyi-pratikler.md) · [Otonom & Öz-Gelişen Sistemler](otonom-ve-oz-gelisen-sistemler.md) · [Dünyada AI Kullanımı](dunyada-ai-kullanimi.md) · [AI/ML Mühendislik Pratiği](../pratik/ai-ml-muhendisligi.md)

---

> [⬅️ Yapay Zeka Çağı](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
