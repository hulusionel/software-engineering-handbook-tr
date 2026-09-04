# Yazılım Mühendisliği: Kapsamlı Gelişim Yol Haritası

Temel bilgisayar bilimlerinden mimari düşünceye, kod kalitesinden kariyer gelişimine kadar katmanlı bir yol haritası.

---

## 1. Bilgisayar Bilimlerinin Temelleri (CS Fundamentals)

Okulda eksik kalan temeli buradan sağlamlaştırırsın.

### Kitaplar
| Kitap | Açıklama |
|---|---|
| **"Introduction to Algorithms" (CLRS)** — Cormen, Leiserson, Rivest, Stein | Algoritma ve veri yapılarının kutsal kitabı. Tamamını okumak şart değil, temel bölümleri (sorting, graph, dynamic programming) sindirmek yeterli. |
| **"Grokking Algorithms"** — Aditya Bhargava | CLRS çok ağır geliyorsa, görsel ve sade bir giriş. · 📖 [Türkçe rehber](../veri-sistemler/grokking-algorithms-turkce.md) |
| **"Computer Systems: A Programmer's Perspective" (CS:APP)** — Bryant & O'Hallaron | Bellek, CPU, OS, networking — kodunun aslında makinede nasıl çalıştığını anlamak için. |
| **"Operating Systems: Three Easy Pieces" (OSTEP)** — Arpaci-Dusseau | Process, thread, concurrency, memory management. Ücretsiz online: [pages.cs.wisc.edu/~remzi/OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| **"Networking: A Top-Down Approach"** — Kurose & Ross | TCP/IP, HTTP, DNS — her gün kullandığın şeylerin altını anlarsın. |

### Ücretsiz Kaynaklar
- **MIT OpenCourseWare 6.006** (Introduction to Algorithms) — YouTube'da tam ders videoları
- **Teach Yourself Computer Science** — [teachyourselfcs.com](https://teachyourselfcs.com) (9 temel konuyu hangi kitap/videoyla öğreneceğini gösteren harika rehber)

---

## 2. Temiz Kod Yazmak & Yazılım Zanaatkarlığı

### Kitaplar (Sırasıyla)
| # | Kitap | Açıklama |
|---|---|---|
| 1 | **"Clean Code"** — Robert C. Martin | İsimlendirme, fonksiyon tasarımı, yorum yazma, hata yönetimi. İlk okunacak kitap. · 📖 [Türkçe rehber](../kod-kalitesi/clean-code-turkce.md) |
| 2 | **"The Pragmatic Programmer"** — Hunt & Thomas (20th Anniversary Edition) | Mühendislik mindset'i. DRY, orthogonality, tracer bullets. Her bölüm bağımsız okunabilir. · 📖 [Türkçe rehber](../kariyer-kultur/pragmatic-programmer-turkce.md) |
| 3 | **"Refactoring"** — Martin Fowler (2nd Edition) | Kötü kodu iyi koda dönüştürmenin sistematik yolu. Katalog formatında, referans kitap gibi kullanılır. · 📖 [Türkçe rehber](../kod-kalitesi/refactoring-turkce.md) |
| 4 | **"A Philosophy of Software Design"** — John Ousterhout | Complexity management. Clean Code'dan daha derin ve daha az dogmatik. Stanford'daki CS 190 dersinin kitabı. **Şiddetle tavsiye ederim.** · 📖 [Türkçe rehber](../kod-kalitesi/philosophy-of-software-design-turkce.md) |
| 5 | **"Code Complete"** — Steve McConnell | 900+ sayfa dev bir kitap ama yazılım construction'ın ansiklopedisi. Referans olarak kullanılır. |
| 6 | **"Working Effectively with Legacy Code"** — Michael Feathers | Gerçek dünyada karşılaşacağın miras kodla nasıl başa çıkılır. |

---

## 3. Tasarım Desenleri & OOP / Yazılım Tasarımı

| Kitap | Açıklama |
|---|---|
| **"Head First Design Patterns"** — Freeman & Robson | GoF patterns'ı öğrenmenin en erişilebilir yolu. · 📖 [Türkçe rehber](../kod-kalitesi/head-first-design-patterns-turkce.md) |
| **"Design Patterns" (Gang of Four)** — Gamma, Helm, Johnson, Vlissides | Klasik referans. Head First'ten sonra okunursa daha anlamlı olur. |
| **"Patterns of Enterprise Application Architecture"** — Martin Fowler | Repository, Unit of Work, Domain Model gibi enterprise pattern'lar. |

---

## 4. Yazılım Mimarisi

### Kitaplar
| Kitap | Açıklama |
|---|---|
| **"Clean Architecture"** — Robert C. Martin | Dependency Rule, Use Case driven design, katmanlı mimari. · 📖 [Türkçe rehber](../mimari-tasarim/clean-architecture-turkce.md) |
| **"Fundamentals of Software Architecture"** — Richards & Ford | Mimari stilleri (monolith, microservices, event-driven, vb.) karşılaştırmalı anlatır. **Çok güncel ve pratik.** · 📖 [Türkçe rehber](../mimari-tasarim/fundamentals-of-software-architecture-turkce.md) |
| **"Software Architecture: The Hard Parts"** — Richards, Ford, Sadalage, Dehghani | Distributed architecture'daki zor kararlar: data ownership, coupling, saga, vb. · 📖 [Türkçe rehber](../mimari-tasarim/software-architecture-hard-parts-turkce.md) |
| **"Building Microservices"** — Sam Newman (2nd Ed.) | Microservices'e geçiş, decomposition, inter-service communication. · 📖 [Türkçe rehber](../mimari-tasarim/building-microservices-turkce.md) |
| **"Designing Data-Intensive Applications" (DDIA)** — Martin Kleppmann | **Mutlaka okunmalı.** Replication, partitioning, consistency, stream processing. Modern backend mühendisliğinin temeli. · 📖 [Türkçe rehber](../veri-sistemler/ddia-turkce.md) |
| **"Domain-Driven Design"** — Eric Evans | Bounded Context, Aggregate, Ubiquitous Language. Zor bir kitap ama çığır açıcı. · 📖 [Türkçe rehber](../mimari-tasarim/ddd-turkce.md) |
| **"Implementing Domain-Driven Design"** — Vaughn Vernon | Evans'ın kitabının pratik uygulaması. |

### Makaleler & Online
- **Martin Fowler's Blog** — [martinfowler.com](https://martinfowler.com) — Mimari, refactoring, CI/CD üzerine tonlarca makale
- **"The Twelve-Factor App"** — [12factor.net](https://12factor.net) — Cloud-native app tasarımının 12 prensibi
- **"Microservices.io"** — Chris Richardson'ın pattern kataloğu

---

## 5. Sistem Tasarımı (System Design)

| Kaynak | Tür |
|---|---|
| **"System Design Interview" Vol 1 & 2** — Alex Xu | Interview odaklı ama sistem düşüncesini geliştirmek için müthiş. · 📖 [Türkçe rehber](../mimari-tasarim/system-design-interview-turkce.md) |
| **"Understanding Distributed Systems"** — Roberto Vitillo | Distributed systems'e erişilebilir giriş. |
| **ByteByteGo Newsletter** — Alex Xu | Haftalık sistem tasarımı görselleri ve yazıları. [blog.bytebytego.com](https://blog.bytebytego.com) |
| **highscalability.com** | Gerçek şirketlerin mimari case study'leri. |

---

## 6. Test Yazma & TDD

| Kitap | Açıklama |
|---|---|
| **"Test Driven Development: By Example"** — Kent Beck | TDD'nin mucidinden. Kısa ve pratik. |
| **"Unit Testing: Principles, Practices, and Patterns"** — Vladimir Khorikov | Hangi testleri yazmalı, hangilerini yazmamalı. Test kalitesi üzerine en iyi kitap. · 📖 [Türkçe rehber](../kod-kalitesi/unit-testing-turkce.md) |
| **"Growing Object-Oriented Software, Guided by Tests"** — Freeman & Pryce | TDD ile tasarımın nasıl ortaya çıktığını gösterir. |

---

## 7. DevOps, CI/CD & Operasyonel Mükemmellik

| Kitap | Açıklama |
|---|---|
| **"The Phoenix Project"** — Kim, Behr, Spafford | Roman formatında DevOps felsefesi. Çok akıcı. · 📖 [Türkçe rehber](../kariyer-kultur/the-phoenix-project-turkce.md) |
| **"The DevOps Handbook"** — Kim, Humble, Debois, Willis | Phoenix Project'in teknik rehberi. |
| **"Continuous Delivery"** — Jez Humble & David Farley | CI/CD pipeline tasarımının temeli. |
| **"Site Reliability Engineering" (SRE Book)** — Google | Ücretsiz online: [sre.google/sre-book](https://sre.google/sre-book/table-of-contents/) |
| **"Observability Engineering"** — Majors, Fong-Jones, Miranda | Logging, metrics, tracing — modern observability. |

---

## 8. Düşünce Yapısı, Kariyer & Soft Skills

| Kitap | Açıklama |
|---|---|
| **"The Staff Engineer's Path"** — Tanya Reilly | IC track'te yükselmenin yol haritası. · 📖 [Türkçe rehber](../kariyer-kultur/staff-engineers-path-turkce.md) |
| **"The Manager's Path"** — Camille Fournier | Yönetici olmasan bile, yöneticini ve organizasyonu anlamak için. |
| **"Thinking in Systems"** — Donella Meadows | Sistem düşüncesi. Yazılımla doğrudan ilgili değil ama mühendislik zihniyetini şekillendirir. · 📖 [Türkçe rehber](../veri-sistemler/thinking-in-systems-turkce.md) |
| **"An Elegant Puzzle"** — Will Larson | Engineering management ve organizasyon tasarımı. |
| **"The Missing README"** — Riccomini & Ryaboy | Yeni mezun → deneyimli mühendis geçişi için pratik rehber. · 📖 [Türkçe rehber](../kariyer-kultur/the-missing-readme-turkce.md) |

---

## 9. Önemli Makaleler & Blog Yazıları (Must-Read)

| Makale | Link / Kaynak |
|---|---|
| **"No Silver Bullet"** — Fred Brooks (1986) | Yazılım mühendisliğinin doğasındaki zorluk üzerine klasik makale |
| **"Out of the Tar Pit"** — Moseley & Marks | Complexity yönetimi üzerine dönüm noktası makale |
| **"How Complex Systems Fail"** — Richard Cook | 18 maddelik kısa ama çığır açıcı makale |
| **"On Designing and Deploying Internet-Scale Services"** — James Hamilton | Büyük ölçekli sistemler için operasyonel prensipler |
| **"The Log: What every software engineer should know..."** — Jay Kreps | Distributed systems ve event streaming temeli |
| **"Falsehoods Programmers Believe About..."** serisi | İsimler, tarihler, adresler, zaman dilimleri... gerçek dünyanın karmaşıklığı |
| **Joel on Software** — Joel Spolsky | [joelonsoftware.com](https://www.joelonsoftware.com) — özellikle "The Joel Test", "Things You Should Never Do" |
| **Paul Graham Essays** | [paulgraham.com/articles.html](http://paulgraham.com/articles.html) — "Maker's Schedule", "Do Things That Don't Scale" |

---

## 10. Düzenli Takip Edilecek Kaynaklar

| Kaynak | Tür |
|---|---|
| **InfoQ** | Konferans konuşmaları, makaleler, mimari trendler |
| **The Morning Paper** (blog) | Adrian Colyer'ın akademik makale özetleri (artık güncellenmese de arşiv altın) |
| **Engineering Blogs** | Uber, Netflix, Airbnb, Stripe, Cloudflare, Discord engineering blogları |
| **Hacker News** | Günlük teknoloji haberleri ve tartışmalar |
| **Dev.to / Hashnode** | Topluluk yazıları |
| **ThoughtWorks Technology Radar** | Her 6 ayda bir güncellenen teknoloji trendleri |

---

## 11. Güvenlik (Security)

Güvenlik ayrı bir kariyer katmanı değil, her mühendisin temel sorumluluğudur. Bu konuyu bu repoda derinlemesine ele alan saha kılavuzu:

| Kaynak | Odak |
|---|---|
| 📖 [Güvenlik Derinlemesine](../pratik/guvenlik-derinlemesine.md) | STRIDE tehdit modelleme, OWASP Top 10, AuthN/AuthZ, kriptografi, secret yönetimi, supply chain güvenliği |
| **"The Web Application Hacker's Handbook"** — Stuttard & Pinto | Web güvenlik açıklarını saldırgan gözünden anlamak |
| **OWASP Cheat Sheet Series** — [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org) | Pratik, uygulanabilir güvenlik kontrolleri |
| **"Threat Modeling"** — Adam Shostack | Tasarım aşamasında güvenlik düşüncesi |

> **Zihniyet (mindset):** Güvenliği sona bırakma. Tehdit modellemeyi tasarım aşamasında yap; kimlik doğrulama, yetkilendirme ve girdi doğrulamayı baştan planla.

---

## 12. Bu Repodaki Saha Kılavuzları, İleri Rehberler & Şablonlar

Kitap özetleri temeli verir; aşağıdaki bölümler üretim gerçekliğine ve staff+ pratiğine köprü kurar.

### 🛠️ Pratik Saha Kılavuzları ([`pratik/`](../pratik/))
Kitapların ötesinde, sayısal ve karar-odaklı kılavuzlar: [Latency & Kapasite Matematiği](../pratik/latency-numbers-ve-kapasite-matematigi.md), [Dağıtık Sistemler Derinlemesine](../pratik/dagitik-sistemler-derinlemesine.md), [Storage Engine İç Yapısı](../pratik/storage-engine-ic-yapisi.md), [Postmortem Arşivi](../pratik/postmortem-arsivi.md), [Karar Çerçevesi Matrisleri](../pratik/karar-cercevesi-matrisleri.md), [Anti-Pattern Kataloğu](../pratik/anti-pattern-katalogu.md) ve daha fazlası (24 doküman).

### 🚀 İleri Düzey Kapsamlı Rehberler ([`ileri-duzey-rehberler/`](../ileri-duzey-rehberler/))
- [Senior Backend Developer Yol Haritası](../ileri-duzey-rehberler/senior-backend-developer-roadmap.md) — Cloud, K8s, event-driven, microservices, API tasarımı, güvenlik, observability
- [Advanced Backend Engineering](../ileri-duzey-rehberler/advanced-backend-engineering.md) — Staff/Principal seviyesi ileri backend mühendisliği

### 📐 Yazım Şablonları ([`templates/`](../templates/))
Öğrendiklerini uygulamaya dökmek için: [ADR](../templates/adr-sablon.md), [RFC / Design Doc](../templates/rfc-design-doc-sablon.md), [6-Pager](../templates/6-pager-sablon.md), [Postmortem](../templates/postmortem-sablon.md).

> Ayrıca: [📚 Terim Sözlüğü](../glossary/terim-sozlugu.md) · [🔬 Kaynakça (birincil kaynaklar)](../kaynakca.md)

---

## 13. Önerilen Okuma Sırası (Yol Haritası)

Hepsini aynı anda okumaya çalışma. İşte katmanlı bir plan:

### Faz 1 — Temel (0–6 ay)
1. **Grokking Algorithms** — Algoritma temeli
2. **Clean Code** — Kod kalitesi
3. **The Pragmatic Programmer** — Mühendislik zihniyeti
4. **The Missing README** — Kariyer temeli
5. [teachyourselfcs.com](https://teachyourselfcs.com) — CS boşluklarını tespit et

### Faz 2 — Derinleşme (6–12 ay)
6. **A Philosophy of Software Design** — Daha derin tasarım düşüncesi
7. **Head First Design Patterns** — Pattern'lar
8. **Designing Data-Intensive Applications** — Dağıtık sistem temeli
9. **Unit Testing (Khorikov)** — Test stratejisi
10. **Refactoring (Fowler)** — Referans olarak yanında bulundur

### Faz 3 — Mimari & Ölçek (12–18 ay)
11. **Clean Architecture** — Mimari prensipler
12. **Fundamentals of Software Architecture** — Mimari stiller
13. **Building Microservices** — Microservices derinlemesine
14. **The Phoenix Project** — DevOps kültürü
15. **System Design Interview Vol 1** — Sistem tasarımı pratiği

### Faz 4 — Ustalık (18+ ay)
16. **Domain-Driven Design** — Karmaşık domain modelleme
17. **Software Architecture: The Hard Parts** — Zor mimari kararlar
18. **The Staff Engineer's Path** — Kariyer büyümesi
19. **Thinking in Systems** — Sistem düşüncesi
20. Akademik makaleler ve engineering blog'ları düzenli takip

---

## Son Tavsiyeler

- **Okuduğunu uygula.** Her kitaptan 1-2 şeyi mevcut projende dene. Uygulanmayan bilgi unutulur.
- **Kod oku.** Açık kaynak projeleri oku (Express.js, Redis, VS Code). İyi yazılmış kodu görmek, kitaplardan bile öğretici olabilir.
- **Yaz.** Blog yazmak, öğrendiklerini pekiştirmenin en etkili yolu.
- **Bir mentor bul veya topluluk bul.** Tartışarak öğrenmek, yalnız okumaktan çok daha etkili.
- **Hepsini bilmek zorunda değilsin.** Derinlik > Genişlik. Bir konuyu gerçekten anla, sonra diğerine geç.

> Bu liste uzun görünebilir ama bu bir maraton, sprint değil. Her hafta birkaç saat ayırarak 2-3 yıl içinde bu temellerin büyük kısmını sağlamlaştırabilirsin.
