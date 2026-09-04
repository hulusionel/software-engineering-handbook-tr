# 🌍 Dünyada AI Nasıl Kullanılıyor

> **"Demo yapmak kolay, üretime almak zordur. Fark; mimari, değerlendirme ve yönetişimdedir."**

Bu doküman, LLM/agent'lerin **gerçek dünyada** — ürünlerde, ekiplerde, üretim sistemlerinde — nasıl kullanıldığını kalıplar hâlinde anlatır. Belirli şirket iddiaları yerine, **dayanıklı desenlere** ve mühendislik gerçeklerine odaklanır.

---

## 📑 İçindekiler

1. [Benimseme Gerçekliği](#1--benimseme-gerçekliği)
2. [Yaygın Kullanım Kalıpları](#2--yaygın-kullanım-kalıpları)
3. [Üretim Mimarileri](#3--üretim-mimarileri)
4. [Ekip & Organizasyon Pratikleri](#4--ekip--organizasyon-pratikleri)
5. [Ekonomi — Build vs Buy, Birim Maliyet](#5--ekonomi--build-vs-buy-birim-maliyet)
6. [Riskler & Yönetişim](#6--riskler--yönetişim)
7. [Olgunluk Modeli](#7--olgunluk-modeli)
8. [Anti-Pattern'ler](#8--anti-patternler)
9. [İleri Okuma](#9--i̇leri-okuma)

---

## 1. 📈 Benimseme Gerçekliği

```
GERÇEKÇİ TABLO (hype'ı çıkardığımızda):
  ✓ Kod asistanları en hızlı benimsenen kategori — geliştiricilerin büyük
    kısmı günlük kullanıyor (tamamlama, açıklama, test, refactor, hata ayıklama).
  ✓ Metin-yoğun işlerde net kazanç: özetleme, çıkarım (extraction), sınıflandırma,
    çeviri, taslak üretimi, müşteri desteği ilk-yanıtı.
  ⚠ "Pilot cehennemi": çok sayıda POC üretime GEÇMİYOR — değerlendirme,
    güvenilirlik, maliyet ve entegrasyon engelleri yüzünden.
  ⚠ Verimlilik kazancı gerçek ama ölçülmesi zor + göreve göre çok değişken;
    "10× herkes için" bir pazarlama cümlesidir, mühendislik gerçeği değil.
```

> **Staff dersi:** Değer, "AI ekledik" demekte değil; **dar, ölçülebilir bir problemi** güvenilir biçimde çözmekte. En başarılı benimseme, bir iş akışındaki spesifik bir sürtünmeyi (örn. destek biletlerini önceliklendirme) hedefler — "her şeyi yapan asistan"ı değil.

---

## 2. 🧰 Yaygın Kullanım Kalıpları

| Kalıp | Örnek | Neden işe yarar |
|---|---|---|
| **Copilot / asistan** | Kod, yazım, tasarım yardımcısı | İnsan döngüde; hata maliyeti düşük, hız kazancı yüksek |
| **Extraction (çıkarım)** | Fatura/sözleşme/e-postadan yapılı veri | Belirsiz metin → şema; deterministik kontrol eklenebilir |
| **Sınıflandırma & yönlendirme** | Destek bileti triage, içerik moderasyonu | Yüksek hacim, insan-üstü hız, örneklerle iyi çalışır |
| **RAG / doküman Q&A** | İç bilgi tabanı, dokümantasyon araması | Güncel/özel bilgiyi kaynağa bağlar; halüsinasyonu azaltır |
| **Özetleme & sentez** | Toplantı, log, araştırma özeti | Bilgi aşırı yükünü sıkıştırır |
| **Agentic otomasyon** | Çok-adımlı iş akışı (araştır→işlem→raporla) | En yüksek değer + en yüksek risk; guardrail şart |
| **Üretim/dönüşüm** | Kod/test üretimi, migration, çeviri | Doğrulanabilir (test) olduğunda güçlü |

```
DEĞER × RİSK HARİTASI:
  Düşük risk, hızlı kazanç → copilot, özetleme, extraction (buradan başla)
  Yüksek değer, yüksek risk → agentic otomasyon (guardrail + eval ile, kademeli)
  → Kural: düşük-riskli kazançlarla güven inşa et, sonra otonomiyi artır.
```

---

## 3. 🏗️ Üretim Mimarileri

Demo ile üretim arasındaki fark, aşağıdaki katmanlardır. Tipik bir üretim LLM sistemi şuna benzer:

```
  Kullanıcı / Sistem
        │
        ▼
  ┌───────────────┐   İstek yönlendirme, retry, fallback, rate-limit
  │  LLM GATEWAY  │   (birden çok sağlayıcı/model arasında soyutlama)
  └───────┬───────┘
          ▼
  ┌───────────────┐   Prompt injection filtresi, PII maskeleme, yetki,
  │  GUARDRAILS   │   çıktı doğrulama (şema), toksisite/politika kontrolü
  └───────┬───────┘
          ▼
  ┌───────────────┐   Sistem promptu + araçlar + RETRIEVAL (RAG)
  │  ORCHESTRATION│   + agent döngüsü + compaction/memory
  └───────┬───────┘
          ▼
  ┌───────────────┐   Prompt/response cache, semantic cache
  │   CACHING     │   → maliyet + latency düşer
  └───────┬───────┘
          ▼
  ┌───────────────┐   Trace, token/maliyet/latency metrikleri, eval,
  │ OBSERVABILITY │   geri bildirim toplama (feedback loop)
  └───────────────┘
```

### Kritik üretim bileşenleri

```
• LLM GATEWAY / ROUTER: Model/sağlayıcı bağımsızlığı; ucuz modeli basit işe,
  güçlü modeli zor işe yönlendir (model routing). Sağlayıcı kesintisine fallback.
• RETRIEVAL (RAG): Güncel/özel bilgiyi bağla → halüsinasyon azalır, kaynak gösterilir.
• CACHING: Prompt caching (aynı ön-ek) + semantic cache (benzer sorulara aynı cevap).
• GUARDRAILS: Girdi (injection) + çıktı (şema, PII, politika) kontrolü.
• EVAL + FEEDBACK: Üretim örnekleri eval setine döner → sistem zamanla iyileşir.
• FALLBACK: Model başarısız/emin değilse → deterministik yol veya insana devret.
```

> **Staff dersi:** "Model çağrısı" bir üretim sisteminin %10'udur; kalan %90'ı gateway, retrieval, guardrail, cache, eval ve gözlemlenebilirliktir. Bu, klasik dağıtık sistem mühendisliğidir — [API tasarımı](../pratik/api-tasarim-derinligi.md), [SRE](../pratik/sre-pratigi.md) ve [performans](../pratik/performance-engineering.md) dersleri aynen geçerli.

---

## 4. 👥 Ekip & Organizasyon Pratikleri

```
NASIL ENTEGRE EDİLİYOR (işe yarayan kalıplar):
  • İç platform: Ekiplerin ortak kullandığı LLM gateway + guardrail + gözlem
    → her ekip sıfırdan kurmaz; güvenlik/maliyet merkezî yönetilir.
  • "AI-assisted" review kültürü: AI üretimi kod da insan review'undan geçer;
    "AI yazdı" bir onay değildir (bkz. agentic-muhendislik §9).
  • Prompt/skill kütüphanesi: Kurumsal bilgi (kod standardı, runbook) paylaşılan
    skill/prompt olarak paketlenir → tutarlılık.
  • Politika: Hangi veri modele gidebilir, hangi sağlayıcı onaylı, gizli/kişisel
    veri kuralları net yazılı.
```

```
İNSAN ROLÜNÜN DEĞİŞİMİ:
  → Mühendis: kod yazan → yön veren + doğrulayan + mimari kuran.
  → Junior için risk: "üret ama anlama" tuzağı → temelleri yine de öğren.
  → Kıdem, "AI'ın nerede yanıldığını görebilme" yeteneğiyle daha değerli hâle gelir.
```

> **Staff dersi:** AI, iyi mühendisi hızlandırır; kötü mühendisi hızlı hatalı kod üreticisine çevirir. Bu yüzden bu el kitabındaki temeller (tasarım, test, [kod kalitesi](../kod-kalitesi/), [mimari](../mimari-tasarim/)) daha da önemli hâle geldi — AI çağı bunları eskitmedi, **kaldıracını artırdı**.

---

## 5. 💰 Ekonomi — Build vs Buy, Birim Maliyet

```
BUILD vs BUY vs FINE-TUNE:
  • Prompt + hazır API (buy)  → en hızlı, en esnek; çoğu vakada BAŞLA burada.
  • RAG (kendi verinle)        → özel/güncel bilgi gerekiyorsa; orta maliyet.
  • Fine-tune / kendi model    → yalnızca (a) çok özel format/ton, (b) çok yüksek
                                  hacimde birim maliyet düşürme, (c) gizlilik/
                                  yerinde çalıştırma zorunluluğu varsa. Pahalı & bakımlı.
  → Kural: prompt+RAG ile başla; fine-tune'u ölçülebilir bir gerekçe olmadan yapma.
```

```
BİRİM EKONOMİSİ (unit economics):
  → "Request başına maliyet" izle: token akışı × fiyat + altyapı.
  → Ölçekte token maliyeti gerçek bir kalem olur → caching + model routing +
    context minimizasyonu doğrudan kâr/zarar etkiler.
  → FinOps mantığı LLM'e de uygulanır (bkz. pratik/finops-cloud-maliyet.md):
    ucuz modeli varsayılan yap, güçlü modeli yalnız gerektiğinde çağır.
```

> **Staff dersi:** LLM maliyeti "görünmez" başlar, ölçekte "aniden görünür" olur. Birim maliyeti gün-1'den izle; en büyük tasarruf kalemleri neredeyse her zaman **caching, context küçültme ve model routing**tir — model değiştirmek değil.

---

## 6. ⚖️ Riskler & Yönetişim

```
BAŞLICA RİSKLER:
  • Halüsinasyon → yanlış ama emin çıktı (hukuk, sağlık, finans'ta tehlikeli).
  • Veri gizliliği → hangi veri sağlayıcıya gidiyor? Sözleşme/DPA, veri ikameti.
  • Prompt injection & veri sızıntısı → agentic sistemlerde (bkz. güvenlik).
  • IP/telif → üretilen içeriğin kaynağı/lisansı; eğitim verisi tartışmaları.
  • Önyargı (bias) & adalet → sınıflandırma/karar sistemlerinde ayrımcılık riski.
  • Aşırı bağımlılık → beceri körelmesi, tek-sağlayıcı kilidi.

YÖNETİŞİM (regülasyon yükseliyor):
  • AB AI Act → risk-temelli sınıflandırma; yüksek-riskli kullanımlara yükümlülük.
  • Sektörel: sağlık, finans, kamu → ek denetim, açıklanabilirlik, insan gözetimi.
  • İç politika: onaylı modeller, veri sınıflandırması, insan-döngüde zorunluluğu,
    denetim izi. → Bkz. pratik/hukuk-uyumluluk-etik.md
```

```
SORUMLU KULLANIM İLKELERİ:
  ✓ İnsan gözetimi (yüksek etkili kararlarda nihai sorumluluk insanda).
  ✓ Şeffaflık (kullanıcı AI ile konuştuğunu bilsin; kaynak göster).
  ✓ Doğrulanabilirlik (kritik çıktıyı kaynağa/deterministik kontrole bağla).
  ✓ Veri minimizasyonu (yalnız gereken veriyi modele ver).
  ✓ İzlenebilirlik (kim, ne zaman, hangi çıktı — audit).
```

---

## 7. 🪜 Olgunluk Modeli

```
SEVİYE 0 — Yasak/gölge kullanım
  → Politika yok; çalışanlar gizlice kullanıyor (shadow AI). En riskli seviye.

SEVİYE 1 — Bireysel copilot
  → Geliştiriciler kod asistanı kullanıyor; kurumsal entegrasyon yok.

SEVİYE 2 — Ürün özelliği
  → Tekil, iyi-tanımlı özellikler (özetleme, arama, extraction) üretimde;
    eval + gözlem var.

SEVİYE 3 — Platform
  → Ortak LLM gateway + guardrail + prompt/skill kütüphanesi; ekipler üstünde inşa ediyor.

SEVİYE 4 — Agentic iş akışları
  → İnsan-döngüde otonom agent'ler gerçek işleri yürütüyor; sağlam yönetişim + eval.
```

> **Staff dersi:** Çoğu kurum Seviye 1-2'dedir; Seviye 3-4 için gereken şey daha büyük model değil, **platform + eval + yönetişim** disiplinidir. Atlanan seviye, teknik borç olarak geri döner.

---

## 8. ⚠️ Anti-Pattern'ler

| Anti-Pattern | Neden tehlikeli | Doğru yaklaşım |
|---|---|---|
| **"AI ekleyelim" (çözüm arayan problem)** | Değer üretmeyen özellik, boşa maliyet | Önce dar, ölçülebilir problem; sonra araç |
| **Demo'yu üretim sanmak** | Guardrail/eval/maliyet olmadan çöker | Üretim katmanlarını (bkz. §3) kur |
| **Eval'siz kalite iddiası** | Sessiz regresyon, güvenilmezlik | Eval seti + üretim feedback döngüsü |
| **Gölge AI (politikasız)** | Veri sızıntısı, uyumluluk ihlali | Onaylı yol + veri politikası + eğitim |
| **Erken fine-tune** | Yüksek maliyet, bakım yükü, esneklik kaybı | Prompt+RAG ile başla; gerekçeyle fine-tune |
| **Maliyeti geç fark etmek** | Ölçekte fatura şoku | Gün-1 birim maliyet izleme + caching + routing |
| **Temelleri atlamak** | AI kötü mühendisi hızlandırır (hatalı) | Tasarım/test/mimari temelleri koru |

---

## 9. 📚 İleri Okuma

- Anthropic — *Building Effective Agents* (üretim agent kalıpları)
- Google/DORA — *DORA Reports* (AI'ın yazılım teslimatına etkisi, ölçüm)
- Stanford — *AI Index Report* (benimseme, yetenek, maliyet trendleri)
- OWASP — *Top 10 for LLM Applications* (üretim güvenliği)
- AB — *Artificial Intelligence Act* (risk-temelli düzenleme)
- Bu repo: [Agentic Mühendislik](agentic-muhendislik.md) · [En İyi Pratikler](en-iyi-pratikler.md) · [AI ile Neler Yapılabiliyor](ai-ile-neler-yapilabilir.md) · [Otonom & Öz-Gelişen Sistemler](otonom-ve-oz-gelisen-sistemler.md) · [Gelecek ve Pozisyon](gelecek-ve-pozisyon.md) · [AI/ML Mühendislik Pratiği](../pratik/ai-ml-muhendisligi.md) · [FinOps](../pratik/finops-cloud-maliyet.md) · [Hukuk/Uyumluluk/Etik](../pratik/hukuk-uyumluluk-etik.md)

---

> [⬅️ Yapay Zeka Çağı](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
