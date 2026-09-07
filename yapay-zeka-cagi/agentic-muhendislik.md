# 🤖 Agentic Mühendislik — Uygulayıcının Rehberi

> **"Model bir fonksiyondur; agent bir döngüdür. Mühendislik, döngünün etrafındaki her şeydedir."**

Bu doküman "yapay zeka nedir, hayatımıza nasıl girdi" anlatmaz. **Bir yazılım mühendisinin, LLM ve agent'leri üretim kalitesinde kullanmak için bilmesi gereken niş, pratik konuları** ele alır: token ekonomisi, context mühendisliği, agent anatomisi, tool/skill tasarımı, MCP, compaction ve AI ile kodlama disiplini.

Hedef kitle: LLM API'sini "çalıştırmış" ama neden bazen harika bazen berbat sonuç aldığını, maliyetin neden patladığını, agent'in neden döngüye girdiğini **derinlemesine** anlamak isteyen mühendisler.

---

## 📑 İçindekiler

1. [Zihinsel Model: Fonksiyon vs Döngü](#1--zihinsel-model-fonksiyon-vs-döngü)
2. [Token Ekonomisi](#2--token-ekonomisi)
3. [Context Mühendisliği](#3--context-mühendisliği)
4. [Agent Anatomisi — Agentic Loop](#4--agent-anatomisi--agentic-loop)
5. [Tool / Function Calling Tasarımı](#5--tool--function-calling-tasarımı)
6. [Skills — Yetenek Paketleme](#6--skills--yetenek-paketleme)
7. [MCP — Model Context Protocol](#7--mcp--model-context-protocol)
8. [Compaction & Bellek Yönetimi](#8--compaction--bellek-yönetimi)
9. [AI ile Kodlama Pratiği](#9--ai-ile-kodlama-pratiği)
10. [Anti-Pattern'ler](#10--anti-patternler)
11. [Staff+ Kontrol Listesi](#11--staff-kontrol-listesi)
12. [İleri Okuma](#12--i̇leri-okuma)

---

## 1. 🧠 Zihinsel Model: Fonksiyon vs Döngü

Her şeyin temelinde yatan iki soyutlama:

```
LLM (model) = SAF bir fonksiyon:
  f(context) → sonraki token'ların olasılık dağılımı
  → Durumsuz (stateless). Hafızası YOK. Her çağrı sıfırdan.
  → "Hatırladığı" tek şey: ona verdiğin context penceresi.

AGENT = LLM'i bir DÖNGÜ içine koymak:
  while (görev bitmedi):
    1. Modele context ver  → 2. Model bir eylem/araç seçer
    3. Aracı ÇALIŞTIR      → 4. Sonucu context'e ekle → tekrar
  → Durum, context penceresinde BİRİKİR.
  → "Zeka" modelde; "yetkinlik" döngü + araçlar + context'te.
```

> **Staff dersi:** LLM uygulaması geliştirmek, model eğitmek değildir. **Context'i doğru kurmak, doğru araçları vermek ve döngüyü doğru yönetmek** bir *yazılım mühendisliği* problemidir. Kötü sonuçların %90'ı modelden değil, **context ve orkestrasyondan** gelir.

### İki temel hata

| Hata | Belirti | Doğru bakış |
|---|---|---|
| "Model aptal" | Kötü sonuç → daha büyük model ararsın | Genelde context eksik/kirli; önce onu düzelt |
| "Prompt sihirdir" | Sonsuz prompt tweak'i | Prompt bir arayüzdür; asıl kaldıraç context + araçlar + değerlendirme |

---

## 2. 🪙 Token Ekonomisi

Token = modelin metni işlediği birim (kabaca ~4 karakter / ~0.75 kelime İngilizce; Türkçe ve kod **daha fazla** token harcar). Her şey token cinsinden ölçülür ve faturalandırılır.

```
İKİ YÖNLÜ MALİYET:
  INPUT token'lar  → context'e koyduğun her şey (sistem promptu, geçmiş,
                     araç tanımları, retrieve edilen doküman, araç çıktıları)
  OUTPUT token'lar → modelin ürettiği (genelde input'tan PAHALI, çünkü
                     otoregresif: her token bir forward pass)

ÖNEMLİ ASİMETRİ:
  → Uzun bir agent görevinde, geçmiş her turda TEKRAR gönderilir.
  → 20 turluk bir agent, aynı context'i 20 kez "input" olarak öder.
  → Maliyet, tur sayısı × biriken context ile KAREsel büyüyebilir!
```

### Context penceresi (context window)

Modelin tek seferde "görebildiği" maksimum token. Aşarsan ya hata alırsın ya da en eski kısım düşer.

```
BÜYÜK PENCERE ≠ HER ŞEYİ DOLDUR!
  → Pencere 200K token olabilir ama:
    • Daha fazla token = daha yavaş + daha pahalı
    • "Lost in the middle": model uzun context'in ORTASINDAKİ bilgiyi
      kaçırır (baş ve son daha güçlü hatırlanır)
    • İlgisiz context, modeli YANILTIR (context rot / dikkat dağılması)
  → Kural: pencereyi bir BÜTÇE gibi yönet, çöp kutusu gibi değil.
```

### Prompt caching (önbellekleme)

Aynı context ön-eki (sistem promptu, araç tanımları, sabit doküman) tekrar tekrar gönderiliyorsa, sağlayıcılar bunu **önbelleğe** alıp çok daha ucuza/hızlıya sunar.

```
KALDIRAÇ: Değişmeyen kısmı BAŞA koy, değişeni SONA.
  [ SABİT: sistem promptu + araç tanımları + referans doküman ]  ← cache HIT
  [ DEĞİŞKEN: kullanıcı mesajı + o anki durum ]                  ← her sefer yeni
  → Doğru sıralama, maliyeti 5-10× düşürebilir + latency'yi azaltır.
```

### Sayısal sezgi (ezberden çok, mertebe)

```
• Kısa bir sohbet turu           → yüzlerce–birkaç bin token
• Bir kod dosyası (~500 satır)   → ~5-10K token
• Büyük bir repo context'i       → 100K+ token (çoğu zaman GEREKSİZ)
• Output genelde input'tan 3-5× pahalı (sağlayıcıya göre değişir)
```

> **Staff dersi:** Token bütçesi, latency ve maliyetin **aynı** kaldıracıdır. "Doğru context'i minimumda tut" hem ucuz hem hızlı hem de daha **doğru** sonuç verir. Fiyatlar hızla değiştiği için $ ezberleme; **token akışını** ölç ve mimariye göre optimize et (caching, retrieval, compaction).

---

## 3. 🎯 Context Mühendisliği

**Context engineering, prompt engineering'in bir üst kümesidir.** Prompt "ne sorduğun"; context "modele o an neyi gösterdiğinin tamamı"dır: sistem promptu, araç tanımları, konuşma geçmişi, retrieve edilen belgeler, araç çıktıları, örnekler.

```
CONTEXT = AGENT'IN "RAM"i.
  Model durumsuz olduğu için, context penceresi onun ÇALIŞMA BELLEĞİDİR.
  → İyi context mühendisi, bir işletim sistemi gibi bu belleği yönetir:
    neyi yükle, neyi at, neyi özetle, neyi sıkıştır.
```

### Doğru context'in ilkeleri

| İlke | Açıklama |
|---|---|
| **İlgili, minimum** | Göreve gerekmeyen her token gürültüdür; doğruluğu düşürür |
| **Yapılandırılmış** | Başlık/bölüm/etiketle; model yapıyı takip eder ("<kurallar>…</kurallar>") |
| **Konum bilinçli** | En kritik talimatı BAŞA veya SONA koy (orta kaybolur) |
| **Taze** | Bayat/çelişen context, modeli yanlış yönlendirir — güncelle veya at |
| **Kaynaklı** | Modelin uyması gereken olguları context'e koy; "bildiğini" varsayma |

### Retrieval (RAG) vs uzun context

```
"Tüm dokümanları pencereye tıkıştırayım" ❌
  → Pahalı, yavaş, lost-in-the-middle, ilgisiz bilgi yanıltır.

RETRIEVAL: Soruya göre SADECE ilgili parçaları getir ✅
  Kullanıcı sorusu → embedding → vektör arama → top-k ilgili parça → context
  → Doğru mimari: retrieval + küçük, keskin context.
  → Bkz. pratik/ai-ml-muhendisligi.md (RAG, vektör DB, HNSW derinliği)
```

### Context rot ve "context poisoning"

```
CONTEXT ROT: Uzun görevde context şişer, eski/çelişen bilgi birikir →
  model kararsızlaşır, kendini tekrar eder, talimatları unutur.

CONTEXT POISONING: Modelin kendi ürettiği bir hata context'e girer →
  sonraki turlarda o hatayı "gerçek" sanıp üstüne inşa eder.
  → Çözüm: hatalı çıktıyı context'ten TEMİZLE; yanlış varsayımı düzelt.
```

> **Staff dersi:** "Daha iyi prompt" arayışında saatler harcamadan önce sor: *Model doğru kararı vermek için gereken bilgiye context'te sahip mi, ve gereksiz gürültü var mı?* Çoğu "model hatası" aslında bir **context tasarım hatasıdır**.

---

## 4. 🔁 Agent Anatomisi — Agentic Loop

Bir agent, LLM'i araçlarla donatıp bir döngüye sokar. Klasik çerçeve **ReAct** (Reason + Act): düşün → araç kullan → gözlemle → tekrar.

```
        ┌─────────────────────────────────────────────┐
        │                                             │
        ▼                                             │
  ┌───────────┐   ┌──────────────┐   ┌─────────────┐  │
  │ 1. DÜŞÜN  │──→│ 2. EYLEM SEÇ │──→│ 3. ARACI    │──┘
  │ (plan)    │   │ (tool call)  │   │   ÇALIŞTIR  │
  └───────────┘   └──────────────┘   └──────┬──────┘
        ▲                                    │
        │         4. GÖZLEM (araç çıktısı)   │
        └────────────────────────────────────┘
                  (görev bitene / durma koşuluna kadar)
```

### Bir agent'in temel bileşenleri

| Bileşen | Rolü |
|---|---|
| **Model** | Muhakeme + hangi aracın çağrılacağına karar |
| **Araçlar (tools)** | Dış dünyaya el: dosya oku/yaz, kod çalıştır, API çağır, ara |
| **Sistem promptu** | Kimlik, kurallar, hedef, kısıtlar |
| **Bellek/context** | O ana kadarki durum (bkz. bölüm 3, 8) |
| **Durma koşulu** | Görev bitti / bütçe doldu / insan onayı gerekiyor |

### Planlama kalıpları

```
• PLAN-THEN-EXECUTE: Önce tüm planı çıkar, sonra adımları yürüt.
  → Öngörülebilir, ama ortamdaki sürprizlere zayıf.
• ReAct (interleaved): Her adımda yeniden düşün, gözleme göre uyarla.
  → Esnek, gerçek dünyaya dayanıklı; çoğu kod/araç agent'i bunu kullanır.
• PLAN MODE (salt-okunur keşif): Değişiklik yapmadan önce araştır + plan
  sun, insan onayından sonra uygula. → Riskli/geniş işlerde güvenli.
```

> **Staff dersi:** Agent'in gücü modelden çok **araçların kalitesinden** ve **durma koşullarının netliğinden** gelir. Belirsiz hedef + kötü araç geri bildirimi = sonsuz döngü ve token yakımı. Her agent'e net bir "başardım/başaramadım" sinyali ve bir bütçe tavanı ver.

---

## 5. 🔧 Tool / Function Calling Tasarımı

Model, "araçları" JSON şema ile görür ve hangisini hangi argümanlarla çağıracağına karar verir. **Araçlar agent'in API'sidir — tıpkı bir insan API'si gibi tasarlanmalı.**

```
İYİ ARAÇ TASARIMI = İYİ API TASARIMI:
  ✓ Tek sorumluluk, net isim (search_orders, refund_payment)
  ✓ Açıklayıcı description (model bunu OKUYUP karar verir!)
  ✓ Minimum, tipli parametreler; zorunlu/opsiyonel net
  ✓ Hata mesajları MODELE YÖNELİK: "başarısız" değil, "X eksik, şunu ver"
  ✓ İdempotent yaz-işlemleri (agent aynı aracı tekrar çağırabilir!)
  ✓ Çıktı KOMPAKT: 10.000 satır log değil, özet + gerekirse detay aracı
```

```javascript
// Kötü: model ne yapacağını bilemez, hata sessiz
{ name: "process", description: "processes data", parameters: {...} }

// İyi: niyet + geri bildirim modele öğretir
{
  name: "refund_payment",
  description: "Bir siparişin ödemesini iade eder. Yalnızca 'shipped' " +
               "olmayan siparişlerde çalışır. İdempotent: aynı order_id " +
               "ikinci kez çağrılırsa mevcut iadeyi döner, yeni iade AÇMAZ.",
  parameters: { order_id: "string (zorunlu)", reason: "string (opsiyonel)" }
}
// Hata çıktısı: "İade başarısız: order_id=123 zaten 'shipped'. Önce
//   iade yerine 'return' akışını kullan." ← model bunu OKUYUP düzeltir
```

### Araç sayısı tuzağı

```
ÇOK ARAÇ = KARAR FELCİ:
  → 50 araç verirsen, model yanlış olanı seçer + araç tanımları context'i şişirir.
  → Çözüm: az ve öz araç; ilgisizleri göreve göre GİZLE (progressive disclosure).
  → İlişkili işlemleri tek "akıllı" araçta topla (ör. tek bir "file_edit"
    yerine oku/yaz/ara ayrı ama tutarlı bir set).
```

---

## 6. 🎁 Skills — Yetenek Paketleme

**Skill**, bir agent'e "belirli bir işi nasıl yapacağını" öğreten paketlenmiş bir talimat + kaynak kümesidir (bir prosedür, bir kontrol listesi, şablonlar, yardımcı script'ler). Araçtan farkı: araç bir *eylem*tir; skill bir *uzmanlıktır* (ne zaman, nasıl, hangi sırayla).

```
NEDEN SKILL?
  → Aynı karmaşık işi (deploy, kod-review, rapor formatı) her seferinde
    prompt'a yazmak yerine, bir kez PAKETLE, gerektiğinde YÜKLE.
  → Tekrarlanabilirlik + kurumsal bilgi + tutarlılık.

PROGRESSIVE DISCLOSURE (kademeli açığa çıkarma) — skill'in kalbi:
  1. Agent yalnızca skill'in KISA açıklamasını görür (bir satır).
  2. Görev eşleşince skill'in TAM talimatı context'e yüklenir.
  3. Gerekirse skill içindeki dosyalar/script'ler devreye girer.
  → Böylece context şişmez; uzmanlık "lazım oldukça" gelir.
```

| Ne zaman ne? | Kullan |
|---|---|
| Tek bir dış eylem | **Tool** (API çağrısı, dosya yazma) |
| "Şu işi şöyle yap" prosedürü, tekrar eden | **Skill** (paketli talimat + kaynak) |
| Görev-özel tek seferlik yönlendirme | **Prompt** (o anki mesaj) |
| Kalıcı, oturumlar arası olgu | **Memory** (bkz. bölüm 8) |

> **Staff dersi:** Skill, "kurumsal runbook'un agent'e taşınmış hâlidir". İyi skill; net tetikleyici (ne zaman devreye girer), minimum ama yeterli talimat ve deterministik yardımcılar (script) içerir. Kötü skill; her şeyi context'e boca eden, tetikleyicisi belirsiz bir dev metindir.

---

## 7. 🔌 MCP — Model Context Protocol

Her araç/veri kaynağını her agent'e ayrı ayrı entegre etmek N×M patlamasıdır. **MCP**, agent'ler ile araçlar/veri kaynakları arasında **standart bir arayüz** sunar (USB-C benzetmesi): bir kez MCP sunucusu yaz, her MCP-uyumlu agent kullanabilsin.

```
MCP OLMADAN:            MCP İLE:
  Agent A ── Slack        Agent A ─┐
  Agent A ── GitHub                ├─ MCP ─ Slack sunucusu
  Agent B ── Slack        Agent B ─┘        GitHub sunucusu
  Agent B ── GitHub                         DB sunucusu
  (N×M entegrasyon)       (N+M — standart protokol)

MCP SUNUCUSU 3 ŞEY SUNAR:
  • Tools     → agent'in çağırabileceği eylemler
  • Resources → agent'in okuyabileceği veri (dosya, kayıt, doküman)
  • Prompts   → hazır prompt şablonları
```

```
GÜVENLİK UYARISI (kritik!):
  → MCP sunucusu araç açıklamaları + veri döndürür. Bu içerik GÜVENİLMEZ:
    kötü niyetli/zehirlenmiş bir sunucu, açıklamaya gizli talimat gömebilir
    (prompt injection). Agent bunları VERİ olarak görmeli, KOMUT olarak değil.
  → İlke: yalnızca güvenilen sunucuları bağla; yaz-işlemlerinde insan onayı;
    sunucu çıktısını asla kör "talimat" gibi yürütme.
  → Bkz. Bölüm 10 (anti-pattern) ve pratik/guvenlik-derinlemesine.md
```

---

## 8. 🗜️ Compaction & Bellek Yönetimi

Uzun görevlerde context penceresi dolar. **Compaction (sıkıştırma)**, biriken konuşma/durumu kaybetmeden özetleyip pencereyi boşaltma işlemidir. Bu, agent'lerin uzun süre çalışabilmesinin anahtarıdır.

```
PROBLEM: 100 turluk bir görevde context 200K'yı aşar → ya hata ya kesinti.

COMPACTION (context'i özetleyerek küçült):
  1. Pencere dolmaya yakın → tetiklen (otomatik veya elle).
  2. Eski turları MODELE ÖZETLET: "şu ana kadar ne yapıldı, hangi kararlar,
     hangi dosyalar değişti, sıradaki adım ne".
  3. Ham geçmişi ÇIKAR, özeti bırak → pencere boşalır, görev DEVAM eder.
  → Kayıp: ince detay. Korunan: kararlar, durum, plan.

İYİ COMPACTION İLKELERİ:
  ✓ Kararları ve gerekçeleri koru (neyi neden yaptık)
  ✓ Açık TODO / sıradaki adımı koru
  ✓ Kalıcı olması gerekeni MEMORY'ye yaz (aşağıda) — özet uçucudur
  ✗ "Her şeyi yarıya indir" değil; SİNYALİ koru, gürültüyü at
```

### Bellek katmanları (agent hafızası)

```
1. CONTEXT (RAM)      → o anki pencere; uçucu, her compaction'da değişir
2. SCRATCHPAD (disk)  → ara sonuçlar, geçici dosyalar (görev boyu)
3. MEMORY (kalıcı)    → oturumlar arası olgular: kullanıcı tercihleri, proje
                        kararları, "geçen sefer şu işe yaramadı"
4. RETRIEVAL (harici) → vektör DB / dosya; "lazım oldukça" çekilen bilgi
```

> **Staff dersi:** Compaction ve bellek, agent mühendisliğinin **işletim-sistemi katmanıdır** — sayfalama (paging) ve önbellekleme gibi. "Kalıcı olması gerekeni özete bırakma; özeti kalıcı sanma." Uzun süre çalışan agent'lerin başarısı, ham zekadan çok bu bellek disiplininden gelir. Ayrıca bkz. [Otonom & Öz-Gelişen Sistemler](otonom-ve-oz-gelisen-sistemler.md).

---

## 9. 💻 AI ile Kodlama Pratiği

AI kod asistanları (agentic coding araçları) artık "otomatik tamamlama" değil; **repo'da gezen, test çalıştıran, çok-dosyalı değişiklik yapan agent'lerdir**. Onları etkili kullanmak yeni bir disiplindir.

```
SPEC-DRIVEN / PLAN-FIRST:
  → Doğrudan "şunu kodla" deme; önce NE istediğini netleştir:
    hedef, kısıtlar, kabul kriterleri. Belirsizlik = kötü kod.
  → Riskli/geniş işlerde: önce PLAN iste (salt-okunur), gözden geçir, sonra uygula.

BAĞLAM SAĞLA (context engineering, kod tarafı):
  → İlgili dosyaları/örnek desenleri göster; "bizim konvansiyonumuz şu".
  → Proje seviyesi kalıcı talimatlar (kodlama standartları, mimari kurallar)
    bir yönerge dosyasında (ör. proje kök talimatları) tutulur → her oturuma girer.

DÖNGÜYÜ KAPAT (agent kendini doğrulasın):
  → Agent'e test/lint/build çalıştırma yeteneği ver → kendi hatasını görsün, düzeltsin.
  → "Yeşil testler" en güçlü durma sinyalidir.
```

### AI-üretimi kodun review disiplini

```
AI KODU DA İNSAN KODU GİBİ REVIEW EDİLİR — hatta daha dikkatli:
  ⚠ Makul GÖRÜNEN ama yanlış kod (plausible-but-wrong) en tehlikelisidir.
  ⚠ Var olmayan API/kütüphane "uydurma" (hallucination) — bağımlılıkları doğrula.
  ⚠ Güvenlik: enjeksiyon, gizli anahtar, yetkisiz erişim — otomatik + insan kontrolü.
  ⚠ "Çalışıyor" ≠ "doğru": kenar durumlar, eşzamanlılık, hata yolları.
  → Küçük, gözden geçirilebilir diff'ler iste; dev "tek seferde her şey" değil.
```

```
GÜVENLİK SINIRI (agentic coding'de olmazsa olmaz):
  → Agent'e verilen yetki = agent'i kandıran içeriğin yetkisi.
  → Untrusted girdi (issue metni, web sayfası, bağımlılık README'si) KOMUT değil VERİDİR.
  → Yıkıcı/dışa-dönük eylemlerde (push, deploy, sil, dış API) insan onayı katmanı.
  → İzinleri en aza indir (least privilege); sandbox'ta çalıştır.
```

> **Staff dersi:** AI ile kodlama, "daha hızlı yazmak" değil **"daha hızlı doğrulanabilir küçük adımlar atmak"** demektir. Mühendisin işi kaymaz; kod *yazmaktan* koda *yön vermeye ve doğrulamaya* kayar. Spec netliği + test + review, hızın ön koşuludur — kısayolu değil.

---

## 10. ⚠️ Anti-Pattern'ler

| Anti-Pattern | Neden tehlikeli | Doğru yaklaşım |
|---|---|---|
| **Context'e her şeyi doldur** | Pahalı, yavaş, lost-in-the-middle, yanıltır | Minimum ilgili context + retrieval |
| **Prompt tweak bağımlılığı** | Kök sorun context/araç iken saatler yakılır | Önce context + araç + eval'i düzelt |
| **Değerlendirmesiz (eval'siz) ilerleme** | "Sanki iyi oldu" ile prod'a çıkış → sessiz regresyon | Otomatik eval seti (bkz. diğer doküman) |
| **Sınırsız agent döngüsü** | Token yakımı, sonsuz döngü | Bütçe tavanı + net durma koşulu |
| **Untrusted içeriği komut sanmak** | Prompt injection → veri sızıntısı/yıkıcı eylem | Gözlemlenen içerik = veri, kaynak = yalnız kullanıcı |
| **İnsan onayı olmadan yıkıcı eylem** | Geri alınamaz hata (sil/push/ödeme) | Riskli eylemde insan-döngüde onay |
| **"Model halüsinasyonu yapmaz" varsayımı** | Uydurma API/olgu prod'a sızar | Olguları doğrula; kritik çıktıyı kaynağa bağla |
| **Büyük pencere = düşünme yok** | Bağlam şişer, kalite düşer | Pencereyi bütçe gibi yönet + compaction |

---

## 11. 🎯 Staff+ Kontrol Listesi

### Yeni bir LLM/agent özelliği tasarlarken
- [ ] Görev gerçekten agent mi gerektiriyor, yoksa tek bir LLM çağrısı / klasik kod yeter mi?
- [ ] Context'te yalnızca **ilgili** bilgi var mı? Gürültü ayıklandı mı?
- [ ] Sabit ön-ek (sistem promptu, araç tanımları) **cache** için başa alındı mı?
- [ ] Araçların açıklamaları ve hata mesajları **modele öğretici** mi? Yaz-işlemleri idempotent mi?
- [ ] Net durma koşulu + token/tur **bütçe tavanı** var mı?
- [ ] Uzun görev için **compaction** ve kalıcı **memory** stratejisi var mı?
- [ ] Untrusted içerik (araç çıktısı, web, doküman) **veri** olarak mı ele alınıyor?
- [ ] Yıkıcı/dışa-dönük eylemlerde **insan onayı** katmanı var mı? İzinler minimum mu?
- [ ] Bir **eval seti** ile kalite ölçülüyor mu (bkz. diğer doküman)?

### Üretimde
- [ ] Token akışı, latency ve maliyet **izleniyor** mu (per-request + toplam)?
- [ ] Regresyon için eval **CI'da** çalışıyor mu?
- [ ] Fallback/timeout/retry (idempotent) var mı? Sağlayıcı kesintisine dayanıklı mı?
- [ ] Gizlilik: hangi veri modele/sağlayıcıya gidiyor, sözleşme/uyumluluk uygun mu?

---

## 12. 📚 İleri Okuma

- Yao et al. 2023 — *ReAct: Synergizing Reasoning and Acting in Language Models* (agentic loop temeli)
- Anthropic — *Building Effective Agents* (agent kalıpları; ne zaman agent, ne zaman değil)
- Anthropic — *Effective Context Engineering for AI Agents*
- Model Context Protocol — resmi spesifikasyon (standart araç/veri arayüzü)
- Lewis et al. 2020 — *Retrieval-Augmented Generation* (RAG)
- Liu et al. 2023 — *Lost in the Middle: How Language Models Use Long Contexts*
- Bu repo: [En İyi Pratikler](en-iyi-pratikler.md) · [AI ile Neler Yapılabiliyor](ai-ile-neler-yapilabilir.md) · [Otonom & Öz-Gelişen Sistemler](otonom-ve-oz-gelisen-sistemler.md) · [Gelecek ve Pozisyon](gelecek-ve-pozisyon.md) · [Dünyada AI Kullanımı](dunyada-ai-kullanimi.md) · [AI/ML Mühendislik Pratiği](../pratik/ai-ml-muhendisligi.md)

---

> [⬅️ Yapay Zeka Çağı](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
