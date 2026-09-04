# 🔭 Geleceğe Bakış ve Pozisyon Alma

> **"Gelecek zaten burada — sadece eşit dağılmamış."** — William Gibson

Bu doküman iki soruyu ele alır: **(1) Bu yapı nereye evriliyor?** ve **(2) Biz — bireysel mühendis, ekip, organizasyon — nasıl pozisyon almalıyız, ne öğrenmeliyiz?** Kesin kehanet değil; güncel literatür ve trendlere dayalı, karar vermene yarayacak bir çerçeve sunar. Sayılar hızla eskir; **yön** ve **strateji** kalıcıdır.

---

## 📑 İçindekiler

1. [Nereye Gidiyoruz — Üç Büyük Kayma](#1--nereye-gidiyoruz--üç-büyük-kayma)
2. [Sürükleyici Kuvvetler](#2--sürükleyici-kuvvetler)
3. [Senaryolar: Yakın / Orta / Uzak](#3--senaryolar-yakın--orta--uzak)
4. [Mühendisin Değişen Rolü](#4--mühendisin-değişen-rolü)
5. [Bireysel Pozisyon: Ne Öğrenmeli?](#5--bireysel-pozisyon-ne-öğrenmeli)
6. [Ekip & Organizasyon Pozisyonu](#6--ekip--organizasyon-pozisyonu)
7. [Pişman Olmayacağın Hamleler](#7--pişman-olmayacağın-hamleler)
8. [İnsan Ne Zaman Vazgeçilmez Kalır?](#8--i̇nsan-ne-zaman-vazgeçilmez-kalır)
9. [İleri Okuma](#9--i̇leri-okuma)

---

## 1. 🌊 Nereye Gidiyoruz — Üç Büyük Kayma

Alanın 2030'a doğru üç temel dönüşümü (araştırmaların ortak teması):

```
1. GÖREN & DUYAN AGENT'LER (multimodal)
   → Yalnız metin değil; ekranı görür, sesi duyar, video anlar.
   → "Computer use" ile API'siz her yazılımı sürebilir hâle geliyor.

2. HATIRLAYAN AGENT'LER (kalıcı bellek)
   → Oturumlar arası hatırlar; senin/projenin bağlamını biriktirir.
   → Dosya-tabanlı bellek + not alma standartlaşıyor.

3. TAKIM HÂLİNDE ÇALIŞAN AGENT'LER (çoklu-agent)
   → Tek dev agent yerine, orchestrator + uzman alt-agent'ler.
   → Ajanlar birbiriyle konuşur (agent-to-agent protokolleri doğuyor).
```

```
BİRLEŞİK YÖN: "yanıt veren sistem" -> "iş yapan sistem"
  2026'nın asıl kayması: metin üretmekten EYLEME. LLM'ler planlıyor, araç
  çağırıyor, uzman ajanları koordine ediyor, çok adımlı iş süreçlerini
  tamamlıyor — "dijital montaj hatları".
```

---

## 2. 🚀 Sürükleyici Kuvvetler

```
• REASONING / TEST-TIME COMPUTE: Modeller "yanıt anında daha çok düşünerek"
  (düşünme bütçesi) zor problemlerde büyük sıçrama yapıyor. Ölçek yalnız
  eğitimde değil, ÇIKARIM anında da artıyor.
• MCP & ARAYÜZ STANDARTLARI: Model Context Protocol, araç/veri bağlamayı
  standartlaştırıp N×M entegrasyon patlamasını çözüyor → ekosistem hızlanıyor.
• BENİMSEME İVMESİ (sektör tahminleri): Gartner, 2026 sonuna dek kurumsal
  uygulamaların ~%40'ının agent gömeceğini öngörüyor (2025'te <%5). Agentic
  pazar tahminleri 2030'a doğru on milyarlarca dolar bandında.
• EKONOMİK BASINÇ: Token maliyeti düşerken yetenek artıyor → daha fazla iş
  ekonomik olarak otomatikleştirilebilir hâle geliyor.
```

> **Uyarı — hype filtresi:** Bu sayılar analist tahminidir, kesinlik değil; "pilot cehennemi" gerçektir (çok POC üretime geçmez). Yön güçlü, ama takvim ve büyüklük belirsiz. Kararını **kendi ölçtüğün değere** göre ver, manşete göre değil.

---

## 3. 🎬 Senaryolar: Yakın / Orta / Uzak

```
YAKIN (0-1 yıl) — büyük ölçüde bugün:
  • Agentic kodlama, RAG asistanları, destek/otomasyon yaygınlaşır.
  • MCP ekosistemi olgunlaşır; her araca "agent arayüzü" beklentisi.
  • Reasoning modelleri varsayılan olur; eval + gözlem zorunlu hijyen.

ORTA (1-3 yıl) — makul projeksiyon:
  • Çoklu-agent + kalıcı bellek üretimde normalleşir ("dijital iş gücü").
  • Computer use olgunlaşır; uzun otonom görevler güvenilirleşir.
  • Ajanlar-arası protokoller (A2A) + "agent pazarları" doğar.
  • "Verify" (doğrulama) ve yönetişim, mühendisliğin merkezine oturur.

UZAK (3+ yıl) — spekülatif ama hazırlıklı ol:
  • Yarı-otonom "ajan organizasyonları"; insan gözetimi stratejik seviyeye çıkar.
  • Fiziksel dünya ile kesişim (robotik, IoT) → ajanlar dijitalden çok veri üretir.
  • Belirsizlik yüksek; kesin öngörü YAPMA — opsiyonel kalmayı ve öğrenmeyi koru.
```

> Not: Bunlar olasılık dağılımıdır, takvim değil. Doğru tavır: **hazırlıklı ama dogmatik değil** — birden çok senaryoya dayanıklı beceri ve mimari kur.

---

## 4. 🧭 Mühendisin Değişen Rolü

```
KAYMA: "kod YAZAN" -> "kod'a YÖN VEREN + DOĞRULAYAN + MİMARİSİNİ KURAN"
  • Üretim ucuzladıkça, kıt olan beceri YARGI (taste) ve DOĞRULAMA oluyor.
  • "AI'ın nerede yanıldığını görebilme" yeteneği kıdemi daha değerli kılıyor.
  • Rol giderek: orkestrasyon (ajanları/işi düzenleme) + kalite kapıları + mimari.

BU YÜZDEN TEMELLER DAHA ÖNEMLİ (eskimedi, KALDIRACI ARTTI):
  → AI iyi mühendisi hızlandırır; kötü mühendisi "hızlı hatalı kod üreticisine"
    çevirir. Tasarım, test, mimari, sistem düşüncesi = AI'ı güvenli kullanmanın
    ön koşulu. (Bu el kitabının tamamı bu yüzden hâlâ geçerli.)
```

```
JUNIOR İÇİN RİSK & FIRSAT:
  ✗ Risk: "üret ama anlama" tuzağı → temelleri atlama → sığ kalma.
  ✓ Fırsat: AI ile daha hızlı öğren, daha çok deneyle — AMA ürettiğini
    ANLAMAYI ve DOĞRULAMAYI bırakma. Anlamadığın kodu merge etme.
```

---

## 5. 🎓 Bireysel Pozisyon: Ne Öğrenmeli?

İş ilanlarında "agentic systems" talebi patladı (bir yılda yüzlerceden on binlere). Talep gören ve **dayanıklı** beceriler:

```
KATMAN 0 — TEMELLER (asla eskimeyen; bu el kitabının çekirdeği):
  • Yazılım tasarımı, test disiplini, dağıtık sistemler, veri, güvenlik.
  • Sistem düşüncesi + net yazma/iletişim (agentları da bunlarla yönetirsin).

KATMAN 1 — AI-NATIVE MÜHENDİSLİK (bu bölümün konusu):
  • Token/context ekonomisi, context mühendisliği, agentic loop.
  • Prompt + eval + tool/skill tasarımı; reasoning modellerini doğru kullanma.
  • RAG mimarisi (embedding, hibrit arama, reranking).
  • Güvenlik: prompt injection, least privilege, guardrail.

KATMAN 2 — ARAÇLAR & EKOSİSTEM (hızla değişir; kalıbı öğren, aracı takip et):
  • Bir agent framework'ü (ör. LangGraph) — durum/bellek/orkestrasyon.
  • MCP sunucu yazımı (talebi en dik artan beceri) — kendi araçlarını aç.
  • Gözlemlenebilirlik + eval araçları (trace, LLM-as-judge pipeline).
  • Bir agentic kodlama aracında ustalık (Claude Code / benzeri).

KATMAN 3 — MATEMATİK SEZGİSİ (derinleşmek için):
  • Lineer cebir (embedding), olasılık (belirsizlik/güven), graf (akış/bağımlılık).
```

```
ÖĞRENME YOLU (pratik):
  1. Bu bölümü oku + küçük bir RAG/agent inşa et (bkz. ai-ile-neler-yapilabilir §9).
  2. Bir eval seti kur → "ölçmeden değiştirme" alışkanlığı.
  3. Bir MCP sunucusu yaz → aracı ekosisteme aç.
  4. Gece çalışan küçük, test-korumalı bir agent kur → otonomi + guardrail hissi.
  5. Gerçek bir işi uçtan uca otomatikleştir → değeri ÖLÇ.
```

> **Staff dersi:** Aracı değil **kalıbı** öğren. Framework'ler 6 ayda değişir; "context'i doğru kur, doğru araç ver, döngüyü yönet, ölç" ilkeleri kalıcıdır. Belirli bir kütüphaneye kilitlenme; taşınabilir zihinsel modeller edin.

---

## 6. 🏢 Ekip & Organizasyon Pozisyonu

```
OLGUNLUK MERDİVENİNİ TIRMAN (bkz. dunyada-ai-kullanimi §7):
  gölge kullanım -> bireysel copilot -> ürün özelliği -> PLATFORM -> agentic akışlar

PLATFORM YAKLAŞIMI (kazanan kalıp):
  → Ortak LLM gateway + guardrail + eval + prompt/skill kütüphanesi.
  → Her ekip sıfırdan kurmaz; güvenlik/maliyet merkezî; hız dağıtık.
  → Bu, Team Topologies'in "platform takımı" fikridir. (bkz. kariyer-kultur/team-topologies)

YÖNETİŞİM ÖNCE:
  • Onaylı modeller + veri sınıflandırma politikası (hangi veri nereye gider).
  • İnsan-döngüde zorunluluğu (yüksek-etkili kararlarda).
  • Denetim izi + eval + gözlem. Regülasyon (AB AI Act vb.) yükseliyor.
```

```
STRATEJİK KARARLAR:
  • Build vs Buy: prompt+RAG ile başla; fine-tune/kendi model için ölçülebilir gerekçe iste.
  • Tek-sağlayıcı kilidi riskine karşı gateway/soyutlama (model bağımsızlığı).
  • Beceri yatırımı: temeller + AI-native mühendislik; "araç eğitimi" tek başına yetmez.
```

---

## 7. ✅ Pişman Olmayacağın Hamleler

Gelecek belirsiz; ama her senaryoda değerli olan "no-regret" hamleler:

```
BİREY:
  [ ] Temelleri sağlamlaştır (bu el kitabı) — AI'ı güvenli kullanmanın önkoşulu.
  [ ] Eval + doğrulama disiplinini içselleştir ("ölçmeden değiştirme").
  [ ] Küçük ama gerçek bir şey inşa et; kalıbı yaparak öğren.
  [ ] Yargı/taste geliştir: AI'ın nerede yanıldığını görebilmek.
  [ ] Yazma + iletişimi güçlendir (ajanları da, insanları da bununla yönetirsin).

EKİP/ORG:
  [ ] Platform + guardrail + eval altyapısını erken kur (teknik borç birikmesin).
  [ ] Veri/güvenlik/uyumluluk politikasını netleştir (gölge AI'ı önle).
  [ ] Model bağımsızlığı (gateway) — sağlayıcı kilidine düşme.
  [ ] Küçük, ölçülebilir bir pilotla değeri KANITLA, sonra ölçekle.
```

---

## 8. 🛡️ İnsan Ne Zaman Vazgeçilmez Kalır?

Abartıya karşı denge: AI'ın ölçekleyemediği/almaması gereken alanlar.

```
İNSAN VAZGEÇİLMEZ:
  • Nihai sorumluluk & yargı: etik/hukuki/yüksek-etkili kararlar.
  • Problem tanımı & öncelik: "hangi problemi çözmeli?" (AI çözer, insan seçer).
  • Belirsizlik altında taste: neyin iyi/doğru/güvenli olduğuna dair sezgi.
  • Doğrulama & hesap verebilirlik: "makul ama yanlış"ı yakalamak.
  • İnsan ilişkileri, güven, bağlam, kurumsal politika.

DEĞİŞMEYEN İLKE: agent MUHAKEME eder; insan + deterministik sistem GARANTİ eder.
  En olgun gelecek "insan yerine AI" değil, "doğru katmanda AI + doğru katmanda insan".
```

> **Kapanış:** Doğru soru "AI işimi alacak mı?" değil, **"AI'ı en iyi kullanan mühendis/ekip nasıl çalışır ve ben nasıl o olurum?"**dur. Temelleri derinleştir, kalıpları öğren, ölçerek ilerle, yargını bile. Pozisyon almanın en sağlam yolu — her zaman olduğu gibi — **öğrenmeye devam etmektir.**

---

## 9. 📚 İleri Okuma

- Anthropic — *Building Effective Agents* / *Effective Context Engineering* (yön ve pratik)
- Gartner / Salesforce / sektör 2026 agentic AI trend raporları (benimseme, pazar)
- DORA / Stanford AI Index — AI'ın yazılım teslimatına ve iş gücüne etkisi
- Reilly — **The Staff Engineer's Path** ([bu repo](../kariyer-kultur/staff-engineers-path-turkce.md)) — yargı, etki, teknik liderlik
- Skelton & Pais — **Team Topologies** ([bu repo](../kariyer-kultur/team-topologies-turkce.md)) — platform/organizasyon
- Bu repo: [Agentic Mühendislik](agentic-muhendislik.md) · [En İyi Pratikler](en-iyi-pratikler.md) · [AI ile Neler Yapılabiliyor](ai-ile-neler-yapilabilir.md) · [Otonom & Öz-Gelişen Sistemler](otonom-ve-oz-gelisen-sistemler.md) · [Dünyada AI Kullanımı](dunyada-ai-kullanimi.md)

---

> [⬅️ Yapay Zeka Çağı](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
