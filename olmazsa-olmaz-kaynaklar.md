# 🧭 Olmazsa Olmaz Kaynaklar — Kitap Dışı Rehber

> [Kaynakça](kaynakca.md) birincil paper'lara yönlendirir. Bu doküman ise farklı bir boşluğu doldurur: **bu repoda henüz rehberi olmayan kilit kitaplar**, **hiçbir kitaba tam sığmayan ama mutlaka öğrenilmesi gereken konular** ve **mutlaka incelenmesi gereken GitHub repoları**.

---

## 📚 1. Eksik ama Kritik Kitaplar

Repoda kapsanan 18 kitabın ötesinde, bir backend/staff mühendisinin kütüphanesinde bulunması gereken, henüz rehberi yazılmamış kitaplar:

### ✅ Artık bu repoda rehberi olanlar (yeni eklendi)

| Kitap | Yazar | Rehber |
|---|---|---|
| **Release It!** (2nd ed.) | Michael Nygard | [📖 Türkçe rehber](mimari-tasarim/release-it-turkce.md) — üretim dayanıklılığı, circuit breaker, bulkhead, backpressure |
| **Team Topologies** | Skelton & Pais | [📖 Türkçe rehber](kariyer-kultur/team-topologies-turkce.md) — org tasarımı, bilişsel yük, ters Conway |
| **Accelerate** | Forsgren, Humble, Kim | [📖 Türkçe rehber](kariyer-kultur/accelerate-turkce.md) — DORA metrikleri, hız+istikrar |

### Hâlâ eksik (rehber bekleyen)

| Kitap | Yazar | Neden mutlaka |
|---|---|---|
| **Database Internals** | Alex Petrov | DDIA'nın storage-engine ve dağıtık-DB tarafını derinleştirir (B-tree/LSM, replikasyon, konsensüs implementasyonu). |
| **Working Effectively with Legacy Code** | Michael Feathers | Gerçek işin %90'ı legacy'dir: seam kavramı, karakterizasyon testi, testsiz kodu güvenle değiştirme. |
| **Fundamentals of Data Engineering** | Reis & Housley | Modern veri mühendisliğinin kanonik kitabı; veri yaşam döngüsü, lakehouse, orkestrasyon. |
| **Domain Modeling Made Functional** | Scott Wlaschin | DDD + tip-odaklı tasarım; "yasadışı durumları temsil edilemez kıl". DDD kitabının erişilebilir tamamlayıcısı. |

### İkinci sıra (güçlü tavsiye)

| Kitap | Yazar | Konu |
|---|---|---|
| **Code Complete** (2nd ed.) | Steve McConnell | Yazılım construction ansiklopedisi (referans). |
| **The Manager's Path** | Camille Fournier | Yönetici olmasan bile organizasyonu ve yöneticiliği anlamak. |
| **Understanding Distributed Systems** | Roberto Vitillo | Dağıtık sistemlere erişilebilir, modern giriş. |
| **Enterprise Integration Patterns** | Hohpe & Woolf | Mesajlaşma pattern'leri (kanonik referans). |
| **Tidy First?** | Kent Beck | Küçük, güvenli tasarım iyileştirmeleri; ekonomiyle refactoring. |
| **The Mythical Man-Month** | Fred Brooks | "No Silver Bullet" — yazılımın doğasındaki zorluk (klasik). |
| **Peopleware** | DeMarco & Lister | İnsan/takım dinamikleri; verimliliğin gerçek kaynağı. |
| **Kubernetes Patterns** | Ibryam & Huß | Bulut-doğal tasarım pattern'leri (k8s'e derinlik). |

> **Not:** Bunların en kritik birkaçı için bu repo formatında tam Türkçe rehberler zamanla eklenebilir (öncelik: Release It!, Team Topologies, Accelerate).

---

## 🛠️ 2. Kitaba Sığmayan, Mutlaka Öğrenilecek Konular

Bazı ustalıklar tek bir kanonik kitaba sığmaz; çoğu **yaparak, kod okuyarak, aracı kurcalayarak** öğrenilir. Bir mühendisin ihmal etmemesi gerekenler:

| Konu | Neden kritik | Nasıl öğrenilir |
|---|---|---|
| **Git internals** | Komutları ezberlemek değil, DAG/obje modelini anlamak → rebase, cherry-pick, reflog korkusuz olur | *Pro Git* (ücretsiz) + `.git` klasörünü kurcala |
| **Unix / CLI ustalığı** | Günlük üretkenliğin çarpanı: pipe, `grep/sed/awk/jq`, `find`, süreç yönetimi | `the-art-of-command-line` + günlük pratik |
| **SQL sorgu optimizasyonu** | `EXPLAIN ANALYZE` okumak, indeks stratejisi, N+1 avı — DB darboğazlarının çoğu burada | Use-the-index-luke.com + gerçek slow query'ler |
| **Debugging bir disiplin olarak** | Bilimsel yöntem, hipotez, `git bisect`, ikili arama, minimal tekrar üretimi | *Debugging* (Agans) + gerçek incident'ler |
| **Observability pratiği** | Kod okumadan üretimi anlamak: metrics/logs/**tracing**, OpenTelemetry | OTel docs + bir servise trace ekle |
| **Bulut primitifleri (elle)** | IAM/politika, VPC/subnet/security group, S3 tutarlılık semantiği | Provider konsolu + Terraform ile kur-yık |
| **Büyük projelerin kaynağını okumak** | İyi tasarımı *görmek*, kitaptan öğretici olabilir | Redis, SQLite, Postgres, Go stdlib |
| **Kendi X'ini yazmak** | Bir DB/git/Redis/derleyici yazmak → soyutlamanın altını görmek | `build-your-own-x`, CodeCrafters |
| **Regex + metin işleme** | Log/veri işlemede günlük ihtiyaç | regex101.com + gerçek problemler |
| **Yazma & iletişim** | Staff+ işin yarısı yazmaktır (bu repo: [staff-yazma-kulturu](pratik/staff-yazma-kulturu.md)) | Design doc/RFC yazarak |

> **Staff dersi:** Bu konuların ortak paydası: hiçbiri "bitirilmez", hepsi *pratikle derinleşir*. Bir mühendisi kıdemli yapan, bu ustalıkların **birikimidir** — tek bir kursla değil.

---

## 🐙 3. Mutlaka İncelenecek GitHub Repoları

Bir öğrenme kaynağı olarak GitHub, kitaplar kadar değerlidir. Aşağıdakiler alanın en çok yıldız alan, kanıtlanmış kaynaklarıdır.

### Sistem tasarımı & mimari

| Repo | Ne için |
|---|---|
| **donnemartin/system-design-primer** | System design'ın kanonik deposu — mutlak başlangıç noktası |
| **binhnguyennus/awesome-scalability** | Gerçek şirket mimarileri, ölçeklenme savaş hikâyeleri, paper'lar |
| **ByteByteGoHq/system-design-101** | Görsel, hızlı sindirilir system design kavramları |
| **karanpratapsingh/system-design** | Uçtan uca yazılı system design kursu |

### Temeller & öğrenme yolu

| Repo | Ne için |
|---|---|
| **ossu/computer-science** | Ücretsiz, eksiksiz bir CS lisans müfredatı |
| **kamranahmedse/developer-roadmap** | Görsel yol haritaları (roadmap.sh) |
| **jwasham/coding-interview-university** | Sıfırdan CS + interview hazırlığı |
| **practical-tutorials/project-based-learning** | Proje yaparak öğrenme listesi (her dilde) |

### Derinleşme (yaparak öğren)

| Repo | Ne için |
|---|---|
| **codecrafters-io/build-your-own-x** | Kendi Git/DB/Redis/Docker/derleyicini yaz — en derin öğrenme |
| **jlevy/the-art-of-command-line** | CLI ustalığı, tek sayfa |
| **papers-we-love/papers-we-love** | Sevilen CS paper'ları, tematik derleme |
| **danluu/post-mortems** | Ünlü kesinti postmortem arşivi *(bu repo bunu zaten referanslar)* |
| **kelseyhightower/kubernetes-the-hard-way** | K8s'i sıfırdan, elle kurarak öğren |
| **bregman-arie/devops-exercises** | DevOps/SRE alıştırmaları ve sorular |

### Meslek bilgisi & derlemeler

| Repo | Ne için |
|---|---|
| **charlax/professional-programming** | Profesyonel yazılımcı okuma listesi |
| **mtdvio/every-programmer-should-know** | Her yazılımcının bilmesi gereken teknik konular |
| **sindresorhus/awesome** | "Awesome" listelerinin kök dizini |

### Yapay zeka çağı (bkz. [yapay-zeka-cagi/](yapay-zeka-cagi/))

| Repo | Ne için |
|---|---|
| **anthropics/anthropic-cookbook** | LLM/agent uygulama örnekleri, pratik reçeteler |
| **openai/openai-cookbook** | LLM entegrasyon tarifleri |
| **karpathy/nanoGPT** & **karpathy/LLM101n** | LLM'i sıfırdan yazarak içini anlamak |
| **f/awesome-chatgpt-prompts** | Prompt örnekleri (temkinli kullan; niş için [agentic rehber](yapay-zeka-cagi/agentic-muhendislik.md)) |

> **Nasıl kullanılır:** Bu repolar *tüketilecek içerik* değil, *üstünde çalışılacak* kaynaklardır. Bir tanesini seç, bir hafta içinde küçük bir şey inşa et veya bir bölümünü derinlemesine oku — pasif okuma değil, aktif üretim.

---

> [⬅️ Ana sayfa](README.md) · [🔬 Kaynakça (paper'lar)](kaynakca.md) · [🗺️ Yol Haritası](yol-haritasi/) · [🤖 Yapay Zeka Çağı](yapay-zeka-cagi/)
