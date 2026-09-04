# 🎯 AI ile Doğru Çalışma — En İyi Pratikler

> **"En iyi agent sistemi en karmaşık olan değil, ihtiyacın için doğru olan en basit sistemdir."** — Anthropic, *Building Effective Agents*

Bu doküman, LLM ve agent'leri **üretim kalitesinde ve doğru** kullanmanın damıtılmış pratiklerini toplar. Kaynak: alanın birincil mühendislik yazıları (Anthropic engineering, akademik eval/güvenlik literatürü) + saha deneyimi. [Agentic Mühendislik](agentic-muhendislik.md) temellerini bildiğini varsayar.

---

## 📑 İçindekiler

1. [Altın Kural: Basit Başla](#1--altın-kural-basit-başla)
2. [Workflow vs Agent — 5 Temel Desen](#2--workflow-vs-agent--5-temel-desen)
3. [Prompt Mühendisliği Pratiği](#3--prompt-mühendisliği-pratiği)
4. [Reasoning Modelleri & Extended Thinking](#4--reasoning-modelleri--extended-thinking)
5. [System Prompt "Doğru İrtifa" + Tool Tasarımı](#5--system-prompt-doğru-i̇rtifa--tool-tasarımı)
6. [Context'i Dinamik Yönetmek](#6--contexti-dinamik-yönetmek)
7. [Eval-Driven Development](#7--eval-driven-development)
8. [Model Seçimi & Routing](#8--model-seçimi--routing)
9. [Doğru Kullanım Kontrol Listesi](#9--doğru-kullanım-kontrol-listesi)
10. [İleri Okuma](#10--i̇leri-okuma)

---

## 1. 🪶 Altın Kural: Basit Başla

Alanın en tutarlı bulgusu: **karmaşık framework'lerle değil, basit ve birleştirilebilir kalıplarla başla.**

```
DOĞRU SIRALAMA (Anthropic'in tavsiyesi):
  1. Önce TEK bir LLM çağrısı dene (retrieval + iyi bir prompt ile).
  2. Yetmezse → yapılandırılmış WORKFLOW (önceden tanımlı adımlar).
  3. Ancak gerçekten gerekince → AGENT (modelin kendi yolunu seçtiği döngü).
  → "Çok adımlı agentic sistemi, basit çözümler yetmediğinde EKLE."

NEDEN? Her ek katman: gecikme + maliyet + hata yüzeyi + hata ayıklama zorluğu getirir.
```

```
FRAMEWORK TUZAĞI:
  → LangGraph/CrewAI/Agents SDK işi hızlandırır AMA soyutlama katmanı,
    "altında ne olduğunu" gizler → hata ayıklaması zorlaşır.
  → Tavsiye: önce ham API çağrılarıyla kalıbı ANLA; framework kullanacaksan
    altındaki kodu bil; üretime giderken gereksiz soyutlamayı azalt.
```

> **Staff dersi:** "Agent kurdum" bir başarı değildir; **doğru problemi en basit yapıyla çözmek** başarıdır. Sofistike görev çoğu zaman sade bir uygulamayla çözülür. Karmaşıklığı, ölçülebilir bir fayda karşılığında ekle.

---

## 2. 🔀 Workflow vs Agent — 5 Temel Desen

**Workflow**: LLM ve araçlar **önceden tanımlı kod yollarında** ilerler (öngörülebilir). **Agent**: model **kendi sürecini ve araç kullanımını dinamik yönetir** (açık uçlu). Çoğu üretim değeri, aslında iyi tasarlanmış **workflow**'lardan gelir.

Anthropic'in 5 birleştirilebilir workflow deseni:

```
1. PROMPT CHAINING (zincirleme):
   Görevi sıralı adımlara böl; her adım öncekinin çıktısını işler.
   Araya "kapı" (gate) koyup ara sonucu doğrula.
   → Örnek: taslak üret -> doğrula -> tam metne genişlet. Doğruluk > hız.

2. ROUTING (yönlendirme):
   Girdiyi sınıflandır, uygun uzman yola gönder.
   → Örnek: destek biletini türüne göre ayır; basit soru ucuz modele,
     zor soru güçlü modele. Endişelerin ayrımı + prompt uzmanlaşması.

3. PARALLELIZATION (paralelleştirme):
   • Sectioning: bağımsız alt görevleri aynı anda çalıştır.
   • Voting: aynı görevi birden çok kez çalıştır, sonuçları birleştir/oyla.
   → Örnek: yanıt üretirken ayrı bir çağrı guardrail kontrolü yapsın.

4. ORCHESTRATOR-WORKERS (koordinatör-işçi):
   Merkezî LLM işi DİNAMİK olarak alt görevlere böler, işçilere dağıtır,
   sentezler. (Alt görevler ÖNCEDEN bilinmiyor.)
   → Örnek: çok dosyalı kod değişikliği; çok kaynaklı araştırma.

5. EVALUATOR-OPTIMIZER (değerlendirici-iyileştirici):
   Bir LLM üretir, AYRI bir LLM eleştirir; döngüde iyileşir.
   → Örnek: net kriter varken çeviri/araştırma kalitesini yükseltme.
```

```
NE ZAMAN AGENT (workflow değil)?
  ✓ Adım sayısı öngörülemez, sabit yol kodlanamaz.
  ✓ Modelin karar vermesi gerçekten değer katıyor.
  ✓ Uzun, açık uçlu, keşif gerektiren görev.
  NE ZAMAN AGENT DEĞİL?
  ✗ Tek LLM çağrısı + retrieval yetiyor.
  ✗ Görev doğrusal ve önceden tanımlı.
  ✗ Gecikme/maliyet kritik, görev basit.
```

> **Staff dersi:** "Agent mı workflow mu?" sorusunun doğru cevabı çoğu zaman **workflow**'dur. Agent'i, belirsizlik ve açık-uçluluk gerçekten gerektirdiğinde seç; aksi hâlde öngörülebilir workflow hem ucuz hem güvenilirdir.

---

## 3. ✍️ Prompt Mühendisliği Pratiği

Prompt hâlâ önemli — ama artık [context mühendisliğinin](agentic-muhendislik.md#3--context-mühendisliği) bir alt kümesi olarak. Dayanıklı teknikler:

| Teknik | Ne zaman | Not |
|---|---|---|
| **Yapılandır (XML/başlık)** | Her zaman | `<talimat>`, `<bağlam>`, `<örnek>` ile bölümle — model yapıyı izler |
| **Kanonik few-shot** | Davranış göstermek | 20 kenar durumu yığma; **çeşitli, temsili** 2-5 örnek ver |
| **Görev ayrıştırma** | Karmaşık iş | Tek dev prompt yerine adımlara böl (prompt chaining) |
| **Structured output** | Makineye veri | JSON şema / tool-calling ile deterministik çıktı zorla |
| **Rol + hedef + kısıt** | Genel | "Kimsin, ne yapacaksın, neyi YAPMAYACAKSIN" net olsun |
| **Negatif örnek/kısıt** | Sık hata | "Şunu YAPMA" bazen "şunu yap"tan güçlüdür |

```
FEW-SHOT TUZAĞI (yaygın hata):
  ✗ Prompt'a onlarca kenar-durum örneği doldurmak → context şişer, model kaybolur.
  ✓ Az sayıda ama BEKLENEN DAVRANIŞI TEMSİL EDEN çeşitli örnek.
  → "Örnekler, LLM için bin kelimelik resimlerdir." Kalite > nicelik.

STRUCTURED OUTPUT:
  → Çıktıyı başka bir sistem tüketecekse: serbest metin değil, ŞEMA zorla
    (JSON mode / tool schema). Sonra deterministik doğrula (şema geçerli mi?).
```

---

## 4. 🧠 Reasoning Modelleri & Extended Thinking

Son kuşak "reasoning" (muhakeme) modelleri, zincirleme düşünmeyi (chain-of-thought) **içselleştirdi**. Bu, prompt pratiğini değiştirir.

```
NE DEĞİŞTİ?
  → Reasoning modelleri, yanıttan önce KENDİ İÇLERİNDE adım adım düşünür.
  → Sana "düşünme bütçesi" (thinking budget / effort/reasoning level) verilir:
    modelin ne kadar "düşüneceğini" ayarlarsın.

PRATİK KURALLAR:
  ✓ Reasoning modelinde MANUEL "adım adım düşün" EKLEME → kendi süreciyle
    çelişir/tekrar üretir. Bunun yerine düşünme bütçesini/seviyesini ayarla.
  ✓ Zor, çok adımlı, mantık/matematik/planlama işlerinde reasoning aç.
  ✗ Basit, hız-kritik işlerde reasoning kapalı tut (pahalı + yavaş).
  ✓ Muhakemeyi bir RUBRİK ile yönlendir: ara adımları adlandır, nihai cevabı
    muhakeme izine göre değerlendir.

TREE OF THOUGHTS (ileri):
  → Tek bir düşünce zinciri yerine, birden çok yolu paralel keşfet, en iyiyi seç.
  → Maliyetli; yalnızca yüksek-değerli, çok-yollu problemlerde.
```

> **Staff dersi:** Reasoning modelleri "her şeye açık bırakılacak bir düğme" değildir. Doğru kullanım: **görev zorluğuna göre düşünme bütçesini ayarlamak** — kolay işte kapat (maliyet/latency), zor işte aç (doğruluk). Ölçmeden "hep açık" bırakmak paranı yakar.

---

## 5. 🎚️ System Prompt "Doğru İrtifa" + Tool Tasarımı

### System prompt: doğru irtifa

```
İKİ UÇTAN DA KAÇIN:
  ✗ ÇOK KATI: her mantığı sabit kodlamak → kırılgan, bakımı zor.
  ✗ ÇOK BELİRSİZ: "iyi bir asistan ol" → somut sinyal yok.
  ✓ DOĞRU İRTİFA: davranışı yönlendirecek kadar somut, esneklik bırakacak
    kadar genel. Güçlü heuristik'ler ver, mikro-yönetme.

YAKLAŞIM: minimum talimatla başla, en iyi modelle test et, GÖZLENEN hata
  kalıplarına göre talimat EKLE (baştan her ihtimali yazma).
```

### Tool tasarımı: Agent-Computer Interface (ACI)

Araçlar, agent'in "insan arayüzü"dür — aynı özenle tasarlanmalı.

```
İYİ TOOL (Anthropic ACI ilkeleri):
  ✓ Kendine yeten, hataya dayanıklı, kullanımı ÇOK açık.
  ✓ İşlevleri örtüşmesin; belirsiz karar noktası yaratma.
  ✓ Açık, tanımlayıcı parametreler + örnekler + kenar durumlar.
  ✓ "Poka-yoke" (hataya-yer-bırakmama): parametreyi yanlış kullanılamayacak
    şekilde tasarla (ör. göreli yol yerine MUTLAK yol zorunlu).
  ✓ Format modelin doğal ürettiğine yakın olsun (satır sayma/aşırı escape yok).

TEST: "Bir insan mühendis bu durumda hangi tool'u kullanacağını kesin
  söyleyemiyorsa, agent de söyleyemez." → tool setini sadeleştir.
```

---

## 6. 🗂️ Context'i Dinamik Yönetmek

Uzun/çok adımlı görevlerde context'i bir işletim sistemi gibi yönet (detay: [agentic §3, §8](agentic-muhendislik.md#3--context-mühendisliği)). Üç güçlü teknik:

```
1. JUST-IN-TIME (tam zamanında) RETRIEVAL:
   → Tüm veriyi önden yükleme; hafif TANIMLAYICILAR tut (dosya yolu, sorgu, URL)
     ve çalışma anında araçla çek. İnsan gibi: her şeyi ezberleme, gerekince bak.
   → HİBRİT en iyisi: bir kısmını önden yükle (hız), gerisini keşfet (esneklik).
     Örn: Claude Code, CLAUDE.md'yi önden alır, grep/glob ile anlık arar.

2. STRUCTURED NOTE-TAKING (agentic memory):
   → Agent, context DIŞINA not yazar (NOTES.md / to-do listesi), sonra okur.
   → Compaction/reset sonrası kendi notunu okuyup KALDIĞI YERDEN devam eder.
   → Saatlerce süren görevlerde tutarlılığın anahtarı budur.

3. SUB-AGENT İZOLASYONU:
   → Alt görevi TEMİZ context'li bir alt-agent yapsın; binlerce token harcasa da
     ana agent'e yalnızca 1-2K token'lık ÖZET dönsün.
   → Ana agent sentezler; detay context izole kalır → ana context şişmez.
```

> **Staff dersi:** "Daha büyük context penceresi" bir çözüm değil. Pencere ne kadar büyük olursa olsun **context rot** (token arttıkça isabet düşer) sürer. Doğru pratik: en yüksek sinyalli en küçük token setini kurmak — retrieval + not + alt-agent üçlüsüyle.

---

## 7. 📊 Eval-Driven Development

"Sanki iyi çalışıyor" mühendislik değildir. AI sistemlerinin **test paketi eval'lerdir**; ve prompt/model/araç değiştirdiğinde tek güvenilir pusuladır.

```
ÜÇ SEVİYEDE DEĞERLENDİR:
  • END-TO-END: Görev BAŞARILDI mı? (en anlamlı metrik)
  • TRAJECTORY: İzlenen YOL verimli ve sağlam mıydı? (gereksiz adım? döngü?)
  • COMPONENT: Hangi retriever/tool/alt-agent BOZULDU? (arıza izolasyonu)

DÖRT METRİK ALANI (agent):
  tool calling (doğru araç/argüman) · planning · task completion · reasoning
  + üretimde: safety, latency, cost.
```

```
YÖNTEMLERİ KARIŞTIR (tek yöntem her arızayı yakalamaz):
  • Deterministik kontrol: şema geçerli mi, test geçti mi, sayı tutuyor mu.
    → %100 trafikte çalıştır (ucuz, kesin).
  • LLM-as-judge: açık uçlu kaliteyi ayrı model puanlar. İnsanla ~%85 uyum
    (iki insanın birbiriyle uyumundan yüksek!). Rubriği NET yaz; yargıç da yanılır.
    → Üretim trafiğinin %5-10'unda çalıştır (pahalı).
  • İnsan review: kalibrasyon + zor vakalar.
  • Üretim örnekleme (continuous eval): sadece test setinde değil, CANLI trafikte.

VERİ: 2026 pratiği → toplu metriğe güvenmek için >=500 vaka.
REGRESYON: eval seti CI'da çalışsın → sessiz bozulmayı yakala.
```

> **Staff dersi:** Eval setin en değerli varlığındır. "Prompt'u iyileştirdim" diyip eval'i olmayan, aslında körlemesine tweak yapıyordur. Önce ölç, sonra değiştir, tekrar ölç.

---

## 8. 🎛️ Model Seçimi & Routing

```
TEK MODEL DEĞİL, DOĞRU MODEL:
  → Ucuz/hızlı model (ör. Haiku sınıfı) VARSAYILAN olsun.
  → Zor işi güçlü modele (Opus/Sonnet sınıfı) YÖNLENDİR (routing deseni).
  → Reasoning gereken işe reasoning modeli; basit işe düz model.

NEDEN? Basit işlerin %80'i ucuz modelde yeterli çözülür → maliyet 5-10× düşer,
  latency azalır. "Her şeye en güçlü model" hem pahalı hem gereksiz yavaş.

KARAR: build vs buy vs fine-tune (bkz. dunyada-ai-kullanimi §5)
  → Prompt + RAG ile BAŞLA. Fine-tune'u yalnızca ölçülebilir gerekçe
    (çok özel format/ton, çok yüksek hacimde birim maliyet, gizlilik) varsa.
```

---

## 9. ✅ Doğru Kullanım Kontrol Listesi

### Tasarım
- [ ] En basit çözümü (tek çağrı → workflow → agent) sırayla denedim mi?
- [ ] Bu iş gerçekten **agent** mi gerektiriyor, yoksa **workflow** mu yeter?
- [ ] System prompt "doğru irtifada" mı (ne çok katı, ne çok belirsiz)?
- [ ] Araçlar az, net, örnekli ve **Poka-yoke** mi? Hata mesajları modele öğretici mi?
- [ ] Context minimum-ilgili mi? Just-in-time retrieval + not + alt-agent düşünüldü mü?
- [ ] Reasoning bütçesi göreve göre ayarlandı mı (kolay işte kapalı)?
- [ ] Ucuz-model-varsayılan + routing kuruldu mu?

### Kalite & üretim
- [ ] 3 seviyeli **eval seti** (end-to-end/trajectory/component) var mı, CI'da mı?
- [ ] Deterministik kontrol %100, LLM-judge %5-10 örnekleme kuruldu mu?
- [ ] Token/latency/maliyet ve **trace** izleniyor mu?
- [ ] Yıkıcı eylemde insan onayı + least privilege + sandbox var mı?
- [ ] Prompt injection savunması (containment) var mı? (bkz. [otonom §5](otonom-ve-oz-gelisen-sistemler.md#5--guardrailler--güvenlik))

---

## 10. 📚 İleri Okuma

- Anthropic — *Building Effective Agents* (workflow vs agent, 5 desen, ACI)
- Anthropic — *Effective Context Engineering for AI Agents* (doğru irtifa, JIT retrieval, compaction, not alma, alt-agent)
- Anthropic — *Writing Effective Tools for AI Agents* (tool/ACI tasarımı)
- Anthropic — *Prompt Engineering Best Practices* (yapılandırma, few-shot, extended thinking)
- Wei et al. 2022 — *Chain-of-Thought Prompting* · Yao et al. 2023 — *Tree of Thoughts*
- Schulhoff et al. 2024 — *The Prompt Report: A Systematic Survey of Prompt Engineering Techniques*
- Eval: DeepEval / Confident AI / Arize kılavuzları (3-seviye eval, LLM-as-judge, continuous eval)
- Bu repo: [Agentic Mühendislik](agentic-muhendislik.md) · [Otonom & Öz-Gelişen Sistemler](otonom-ve-oz-gelisen-sistemler.md) · [AI ile Neler Yapılabiliyor](ai-ile-neler-yapilabilir.md) · [Gelecek ve Pozisyon](gelecek-ve-pozisyon.md)

---

> [⬅️ Yapay Zeka Çağı](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
