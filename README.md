# 📚 Software Engineering Handbook TR

Yazılım mühendisliği alanındaki en önemli kitapların **Türkçe kapsamlı rehberleri**, kariyer yol haritaları ve pratik notlar.

## 🗂️ İçindekiler

### 🗺️ [Yol Haritası](yol-haritasi/)

| Rehber | Açıklama |
|--------|----------|
| [Yazılım Mühendisliği Yol Haritası](yol-haritasi/yazilim-muhendisligi-yol-haritasi.md) | CS temellerinden mimari düşünceye, kod kalitesinden kariyer gelişimine katmanlı bir yol haritası |

### 🏛️ [Mimari & Tasarım](mimari-tasarim/)

| Rehber | Kitap |
|--------|-------|
| [Clean Architecture](mimari-tasarim/clean-architecture-turkce.md) | Robert C. Martin — *Clean Architecture* |
| [Fundamentals of Software Architecture](mimari-tasarim/fundamentals-of-software-architecture-turkce.md) | Mark Richards & Neal Ford — *Fundamentals of Software Architecture* |
| [Software Architecture: The Hard Parts](mimari-tasarim/software-architecture-hard-parts-turkce.md) | Neal Ford, Mark Richards, Pramod Sadalage & Zhamak Dehghani |
| [Building Microservices](mimari-tasarim/building-microservices-turkce.md) | Sam Newman — *Building Microservices* |
| [Domain-Driven Design (DDD)](mimari-tasarim/ddd-turkce.md) | Eric Evans — *Domain-Driven Design* |
| [System Design Interview](mimari-tasarim/system-design-interview-turkce.md) | Alex Xu — *System Design Interview Vol 1* |

### 🧹 [Kod Kalitesi & Pratikler](kod-kalitesi/)

| Rehber | Kitap |
|--------|-------|
| [Clean Code](kod-kalitesi/clean-code-turkce.md) | Robert C. Martin — *Clean Code* |
| [Refactoring](kod-kalitesi/refactoring-turkce.md) | Martin Fowler — *Refactoring: Improving the Design of Existing Code* |
| [Unit Testing](kod-kalitesi/unit-testing-turkce.md) | Vladimir Khorikov — *Unit Testing: Principles, Practices, and Patterns* |
| [A Philosophy of Software Design](kod-kalitesi/philosophy-of-software-design-turkce.md) | John Ousterhout — *A Philosophy of Software Design* |
| [Head First Design Patterns](kod-kalitesi/head-first-design-patterns-turkce.md) | Eric Freeman & Elisabeth Robson — *Head First Design Patterns* |

### 📊 [Veri & Sistemler](veri-sistemler/)

| Rehber | Kitap |
|--------|-------|
| [Designing Data-Intensive Applications](veri-sistemler/ddia-turkce.md) | Martin Kleppmann — *Designing Data-Intensive Applications* |
| [Thinking in Systems](veri-sistemler/thinking-in-systems-turkce.md) | Donella H. Meadows — *Thinking in Systems: A Primer* |
| [Grokking Algorithms](veri-sistemler/grokking-algorithms-turkce.md) | Aditya Bhargava — *Grokking Algorithms* |

### 🧭 [Kariyer & Kültür](kariyer-kultur/)

| Rehber | Kitap |
|--------|-------|
| [The Staff Engineer's Path](kariyer-kultur/staff-engineers-path-turkce.md) | Tanya Reilly — *The Staff Engineer's Path* |
| [The Pragmatic Programmer](kariyer-kultur/pragmatic-programmer-turkce.md) | David Thomas & Andrew Hunt — *The Pragmatic Programmer* |
| [The Missing README](kariyer-kultur/the-missing-readme-turkce.md) | Chris Riccomini & Dmitriy Ryaboy — *The Missing README* |
| [The Phoenix Project](kariyer-kultur/the-phoenix-project-turkce.md) | Gene Kim, Kevin Behr & George Spafford — *The Phoenix Project* |

### 🚀 [İleri Düzey Kapsamlı Rehberler](ileri-duzey-rehberler/)

| Rehber | Açıklama |
|--------|----------|
| [Senior Backend Developer Yol Haritası](ileri-duzey-rehberler/senior-backend-developer-roadmap.md) | Cloud, K8s, event-driven architecture, microservices, API design, security, observability ve daha fazlası |
| [Advanced Backend Engineering](ileri-duzey-rehberler/advanced-backend-engineering.md) | Staff/Principal Engineer seviyesi için ileri düzey backend mühendislik rehberi |

### 🤖 [Yapay Zeka Çağında Mühendislik](yapay-zeka-cagi/)

Bir developer'ın el kitabında olması gereken **niş, uygulayıcı odaklı** AI konuları — "AI nedir" değil, agent mühendisliği.

| Doküman | İçerik |
|--------|--------|
| [Agentic Mühendislik](yapay-zeka-cagi/agentic-muhendislik.md) | Token ekonomisi, context mühendisliği, agentic loop, tool/skill tasarımı, MCP, compaction, AI ile kodlama |
| [Otonom & Öz-Gelişen Sistemler](yapay-zeka-cagi/otonom-ve-oz-gelisen-sistemler.md) | Çoklu-agent orkestrasyon, gece çalışan otonom agent'ler, öz-düzelten/öğrenen yapılar, guardrail, eval |
| [Dünyada AI Nasıl Kullanılıyor](yapay-zeka-cagi/dunyada-ai-kullanimi.md) | Benimseme, üretim mimarileri, kullanım kalıpları, ekonomi, riskler & yönetişim, olgunluk modeli |

### 🛠️ [Pratik — Saha Kılavuzu](pratik/)

Kitap özetlerinin ötesinde, üretim odaklı, sayısal ve karar-verme kılavuzları.

**Temel Saha Kılavuzları**

| Doküman | İçerik |
|--------|--------|
| [Latency Numaraları & Kapasite Matematiği](pratik/latency-numbers-ve-kapasite-matematigi.md) | Jeff Dean tablosu, Little's Law, p99 tail-at-scale, sizing |
| [Postmortem Arşivi](pratik/postmortem-arsivi.md) | 20 ünlü kesinti yapılandırılmış (Knight Capital → CrowdStrike 2024) |
| [Karar Çerçevesi Matrisleri](pratik/karar-cercevesi-matrisleri.md) | DB, sync/async, monolith/microservice, build/buy, cache |
| [API Tasarım Derinliği](pratik/api-tasarim-derinligi.md) | Idempotency, pagination, RFC 9457, rate limiting, webhook |
| [Staff+ Yazma Kültürü](pratik/staff-yazma-kulturu.md) | Design Doc, ADR, RFC, 6-pager, PRFAQ, postmortem disiplini |
| [Anti-Pattern Kataloğu](pratik/anti-pattern-katalogu.md) | 60+ anti-pattern (mimari, veri, API, dağıtık, ops, kod, test, güvenlik) |

**Derinlemesine Sistem Konuları**

| Doküman | İçerik |
|--------|--------|
| [Dağıtık Sistemler Derinlemesine](pratik/dagitik-sistemler-derinlemesine.md) | 8 fallacy, FLP, CAP/PACELC, consensus, CRDT, idempotency/outbox |
| [Storage Engine İç Yapısı](pratik/storage-engine-ic-yapisi.md) | WAL, B-tree, LSM-tree, MVCC, snapshot/checkpoint, indexing |
| [Performance Engineering](pratik/performance-engineering.md) | USE/RED/Four Golden Signals, profiling, flame graph, mechanical sympathy |
| [Eşzamanlılık Primitifleri](pratik/eszamanlilik-primitifleri.md) | Threading, memory model, locks, lock-free, async/await, backpressure |
| [Networking Derinlemesine](pratik/networking-derinlemesine.md) | OSI, TCP, TLS, HTTP/1.1/2/3, DNS, LB, gRPC, WebSocket, CDN |
| [Güvenlik Derinlemesine](pratik/guvenlik-derinlemesine.md) | STRIDE, OWASP Top 10, AuthN/Z, crypto, secret mgmt, supply chain |
| [Veri Mühendisliği](pratik/veri-muhendisligi.md) | OLTP/OLAP, lakehouse, ETL/ELT, Lambda/Kappa, CDC, schema evolution |

**Pratik Disiplinler & Modern Stack**

| Doküman | İçerik |
|--------|--------|
| [SRE Pratiği](pratik/sre-pratigi.md) | SLI/SLO/SLA, error budget, toil, on-call, incident, chaos |
| [Build, Release & Supply Chain](pratik/build-release-supply-chain.md) | CI/CD, deterministic build, SLSA/SBOM/Sigstore, deployment |
| [Test Stratejileri](pratik/test-stratejileri.md) | Test pyramid, contract test, property-based, mutation, fuzzing |
| [FinOps & Cloud Maliyet](pratik/finops-cloud-maliyet.md) | Inform/optimize/operate, unit economics, compute/storage optimization |
| [Hukuk, Uyumluluk, Etik](pratik/hukuk-uyumluluk-etik.md) | GDPR, KVKK, PCI-DSS, SOC 2, lisans hijyeni, AI etiği |
| [Modern Teknoloji Radarı](pratik/modern-teknoloji-radari.md) | Adopt/Trial/Assess/Hold: eBPF, WASM, Rust, edge, modern data, LLM |
| [AI/ML Mühendislik Pratiği](pratik/ai-ml-muhendisligi.md) | MLOps, feature store, drift, RAG, LLM eval, cost & latency |
| [Mimari Eleştiri](pratik/mimari-elestiri.md) | Microservices/DDD/Clean/Event Sourcing eleştirisi, over-engineering |
| [Domain Mimarileri](pratik/domain-mimarileri.md) | Exchange/LMAX, Ad-tech/RTB, Gaming, IoT, Multi-tenancy |
| [Operasyonel Derinlik](pratik/operasyonel-derinlik.md) | Connection storm, idempotency key API, operasyonel kalıplar |
| [Staff+ Soft Skills](pratik/staff-soft-skills.md) | Glue work, promotion/impact, executive communication |

### 📐 [Şablonlar](templates/) · 📚 [Terim Sözlüğü](glossary/terim-sozlugu.md) · 🔬 [Kaynakça](kaynakca.md) · 🧭 [Olmazsa Olmaz Kaynaklar](olmazsa-olmaz-kaynaklar.md)

| Şablon | Kullanım |
|--------|----------|
| [ADR](templates/adr-sablon.md) | Mimari karar kaydı (Michael Nygard formatı) |
| [RFC / Design Doc](templates/rfc-design-doc-sablon.md) | Sistem/özellik tasarım dokümanı |
| [6-Pager](templates/6-pager-sablon.md) | Amazon yönetici karar memo'su |
| [PRFAQ](templates/prfaq-sablon.md) | Amazon working backwards — yeni ürün/girişim vizyonu |
| [Postmortem](templates/postmortem-sablon.md) | Blameless olay sonrası analizi |

---

## 📊 İstatistikler

- **21** kapsamlı kitap/yol haritası rehberi
- **24** pratik saha dokümanı + 5 yazım şablonu + terim sözlüğü + kaynakça
- **3** yapay zeka çağı rehberi (agentic mühendislik, otonom sistemler, dünyada AI kullanımı)
- **~65.000+** satır içerik
- **17** farklı kitap özeti
- **3** kariyer yol haritası
- **%100** Türkçe

---

## 🎯 Kimler İçin?

- Yazılım mühendisliği kitaplarını Türkçe okumak isteyenler
- Senior/Staff seviyesine hazırlanan backend geliştiriciler
- System design interview'a hazırlananlar
- Mimari kararlar vermesi gereken tech lead'ler
- Türkçe kaynak arayan CS öğrencileri

---

## 🤝 Katkıda Bulunma

Hata, eksik veya iyileştirme önerileriniz için PR açabilirsiniz. Yeni kitap özetleri eklemek isterseniz, mevcut rehberlerin formatını takip etmeniz yeterlidir.

---

## 📄 Lisans

Bu içerikler kişisel notlar ve özetlerdir. Orijinal kitapların telif hakları yazarlarına aittir. Bu rehberler kitapların yerine geçmeyi değil, öğrenmeye yardımcı olmayı amaçlar. **Kitapları satın alarak yazarları desteklemenizi öneririm.**
