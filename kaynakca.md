# 📚 Kaynakça — Birincil Kaynak İndeksi

Bu repodaki kavramların **birincil kaynaklarına** yönlendirme. Staff/Principal seviyede bir mühendis blog post'ta okuduğu kavramı **paper'ında okur**. Aşağıdaki liste tematik olarak organize edilmiştir.

---

## 🧪 1. Dağıtık Sistemler & Konsensüs

### Klasik Paper'lar (mutlak okunmalı)

| Yıl | Yazar(lar) | Eser | Önemi |
|---|---|---|---|
| 1978 | Lamport | *Time, Clocks, and the Ordering of Events in a Distributed System* | Lamport saatleri, happens-before |
| 1985 | Fischer, Lynch, Paterson | *Impossibility of Distributed Consensus with One Faulty Process* | FLP — neden konsensüs teorik olarak imkansız |
| 1990 | Lamport | *The Part-Time Parliament* (Paxos) | Paxos'un orijinal makalesi |
| 1998 | Lamport | *The Part-Time Parliament* (resmî) | Paxos sade dilde |
| 2000 | Brewer | CAP Conjecture (PODC keynote) | CAP teoreminin doğuşu |
| 2002 | Gilbert, Lynch | *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services* | CAP'in formal kanıtı |
| 2007 | DeCandia et al. (Amazon) | *Dynamo: Amazon's Highly Available Key-value Store* | AP system'in temeli, vector clock, hinted handoff |
| 2008 | Chang et al. (Google) | *Bigtable: A Distributed Storage System for Structured Data* | LSM tabanlı dağıtık DB |
| 2010 | Lakshman, Malik | *Cassandra: A Decentralized Structured Storage System* | Dynamo + BigTable hibridi |
| 2011 | Hunt et al. | *ZooKeeper: Wait-free Coordination for Internet-scale Systems* | Koordinasyon servisi |
| 2012 | Corbett et al. (Google) | *Spanner: Google's Globally-Distributed Database* | TrueTime, external consistency |
| 2013 | Dean, Barroso | *The Tail at Scale* | Kuyruk gecikmesi, hedged requests |
| 2014 | Ongaro, Ousterhout | *In Search of an Understandable Consensus Algorithm* | **Raft** |
| 2014 | Bailis, Ghodsi | *Eventual Consistency Today: Limitations, Extensions, and Beyond* | Eventual consistency'nin sınırları |
| 2017 | Howard | *Distributed Consensus Revised* (PhD thesis) | Modern Paxos varyantları |

### CRDT & Saat
- Shapiro et al. 2011 — *A Comprehensive Study of Convergent and Commutative Replicated Data Types*
- Almeida et al. 2014 — *Δ-CRDTs: Making δ-CRDTs Delta-based*
- Kulkarni et al. 2014 — *Logical Physical Clocks and Consistent Snapshots in Globally Distributed Databases* (HLC)

### Konsensüs Varyantları
- Liskov, Cowling 2012 — *Viewstamped Replication Revisited*
- Moraru et al. 2013 — *There Is More Consensus in Egalitarian Parliaments* (EPaxos)

---

## 💾 2. Storage & Databases

### Klasik
- Codd 1970 — *A Relational Model of Data for Large Shared Data Banks*
- Stonebraker 1981 — *Operating System Support for Database Management*
- Gray 1981 — *The Transaction Concept: Virtues and Limitations*
- Mohan et al. 1992 — *ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging*
- O'Neil et al. 1996 — *The Log-Structured Merge-Tree (LSM-Tree)*

### Modern
- Kleppmann 2017 — **Designing Data-Intensive Applications** (kitap)
- Neumann 2011 — *Efficiently Compiling Efficient Query Plans for Modern Hardware*
- Stoica, Ailamaki 2014 — *Enabling Efficient OS Paging for Main-Memory OLTP Databases*
- Diaconu et al. 2013 — *Hekaton: SQL Server's Memory-Optimized OLTP Engine*

### Replication
- Renesse, Schneider 2004 — *Chain Replication for Supporting High Throughput and Availability*
- Terrace, Freedman 2009 — *Object Storage on CRAQ* (chain replication varyantı)

---

## ⚡ 3. Performans & Sistem Programlama

- Brendan Gregg — **Systems Performance** (2nd ed., 2020)
- Brendan Gregg — **BPF Performance Tools** (2019)
- Drepper 2007 — *What Every Programmer Should Know About Memory*
- Herb Sutter 2005 — *The Free Lunch Is Over*
- Tene, Iyengar, Wolf 2011 — *C4: The Continuously Concurrent Compacting Collector*
- Gil Tene — *How NOT to Measure Latency* (sunum, coordinated omission)

### io_uring & Modern Linux IO
- Axboe 2019 — *Efficient IO with io_uring*

### NUMA / Cache
- Drepper 2007 (yukarıda) — bölüm 5 NUMA
- Intel — *Intel 64 and IA-32 Architectures Optimization Reference Manual*

---

## 🔀 4. Eşzamanlılık (Concurrency)

- Herlihy, Shavit — **The Art of Multiprocessor Programming** (2nd ed., 2020)
- McKenney — *Is Parallel Programming Hard, And, If So, What Can You Do About It?* (ücretsiz, RCU dahil)
- Adve, Gharachorloo 1996 — *Shared Memory Consistency Models: A Tutorial*
- Boehm, Adve 2008 — *Foundations of the C++ Concurrency Memory Model*
- Manson, Pugh, Adve 2005 — *The Java Memory Model*
- Michael 2004 — *Hazard Pointers: Safe Memory Reclamation for Lock-Free Objects*

---

## 🌐 5. Networking

### TCP / HTTP
- RFC 9293 — Transmission Control Protocol (TCP) (2022 güncel)
- RFC 5681 — TCP Congestion Control
- Cardwell et al. 2016 — *BBR: Congestion-Based Congestion Control*
- RFC 7540 — HTTP/2
- RFC 9114 — HTTP/3
- RFC 9000 — QUIC

### Yük Dengeleme & Hashing
- Karger et al. 1997 — *Consistent Hashing and Random Trees*
- Lamping, Veach 2014 — *A Fast, Minimal Memory, Consistent Hash Algorithm* (Jump Hash)
- Eisenbud et al. 2016 — *Maglev: A Fast and Reliable Software Network Load Balancer*
- Thaler, Ravishankar 1998 — *Using Name-Based Mappings to Increase Hit Rates* (Rendezvous hashing)

### Service Mesh & eBPF
- Calavera, Fontana — **Linux Observability with BPF** (O'Reilly 2019)
- Cilium docs (cilium.io) — eBPF dataplane

---

## 🔐 6. Güvenlik

### OAuth / Identity
- RFC 6749 — OAuth 2.0
- RFC 7636 — PKCE
- RFC 9449 — DPoP (Demonstrating Proof-of-Possession)
- RFC 7515 / 7516 / 7519 — JWS / JWE / JWT
- OpenID Connect Core 1.0
- SPIFFE / SPIRE specifications

### Crypto
- Boneh, Shoup — *A Graduate Course in Applied Cryptography* (ücretsiz)
- Cryptopals Challenges (cryptopals.com) — pratik
- Joux 2006 — *Authentication Failures in NIST version of GCM* (nonce reuse)
- Vaudenay 2002 — *Security Flaws Induced by CBC Padding* (padding oracle)

### Threat Modeling & Supply Chain
- Shostack 2014 — **Threat Modeling: Designing for Security**
- *The SLSA Framework* (slsa.dev)
- *In-toto* — supply chain attestation
- *Sigstore / cosign* docs

### Hata vakaları (öğretici)
- log4shell (CVE-2021-44228) — postmortem
- SolarWinds Sunburst — Mandiant raporu
- Heartbleed (CVE-2014-0160) — Codenomicon analizi

---

## 📊 7. Veri Mühendisliği & Streaming

### Stream Processing
- Akidau et al. 2015 — *The Dataflow Model* (Google) — watermark, triggers, accumulation
- Carbone et al. 2017 — *State Management in Apache Flink*
- Kreps 2013 — *The Log: What every software engineer should know* (LinkedIn blog, kitap-uzunluğunda)
- Kafka transactions design doc (KIP-98)

### Lakehouse
- Armbrust et al. 2020 — *Delta Lake: High-Performance ACID Table Storage*
- Apache Iceberg specification (iceberg.apache.org/spec)
- Apache Hudi documentation

### CDC
- Debezium documentation
- Maxwell, Brooklyn Data — *Change Data Capture: The Definitive Guide*

---

## 🛡️ 8. SRE & Operasyon

### Google SRE Üçlemesi (ücretsiz)
- **Site Reliability Engineering** (Beyer et al. 2016) — sre.google/sre-book
- **The Site Reliability Workbook** (2018) — sre.google/workbook
- **Building Secure & Reliable Systems** (2020)

### Incident Management
- *PagerDuty Incident Response Documentation*
- *FEMA ICS-100* — Incident Command System
- Allspaw — *Blameless Postmortems and a Just Culture* (Etsy 2012)

### Chaos Engineering
- Basiri et al. 2016 — *Chaos Engineering* (Netflix)
- Rosenthal, Jones — **Chaos Engineering** (O'Reilly 2020)
- *Principles of Chaos Engineering* (principlesofchaos.org)

---

## 🚀 9. Build, Release, Test

- Humble, Farley — **Continuous Delivery** (2010)
- Forsgren, Humble, Kim — **Accelerate** (2018) — DORA metrics
- Bazel docs, Buck2 docs, Pants v2 docs
- Jepsen reports (jepsen.io) — dağıtık sistem testi reference
- *Foundationdb's Deterministic Simulation* (FoundationDB Summit talks, McCaffrey)

### Property-based & Formal
- MacIver — Hypothesis docs (hypothesis.readthedocs.io)
- Lamport — **Specifying Systems** (TLA+ kitabı, ücretsiz PDF)
- Newcombe et al. 2015 — *How Amazon Web Services Uses Formal Methods*

---

## 💰 10. FinOps

- *Cloud FinOps* — Storment, Fuller (O'Reilly 2nd ed.)
- AWS Well-Architected — Cost Optimization Pillar
- *FinOps Foundation* — finops.org framework

---

## ⚖️ 11. Hukuk / Etik / Lisans

- GDPR (Regulation EU 2016/679) — gdpr-info.eu
- CCPA (California 2018)
- *Choose a License* — choosealicense.com
- *Open Source Licenses* — SPDX license list
- *Server Side Public License* — MongoDB, Elastic, Redis tartışmaları

---

## 🏛️ 12. Mimari & DDD

- Evans 2003 — **Domain-Driven Design**
- Vernon 2013 — **Implementing Domain-Driven Design**
- Khononov 2021 — **Learning Domain-Driven Design**
- Newman 2021 — **Building Microservices** (2nd ed.)
- Ford, Richards 2020 — **Fundamentals of Software Architecture**
- Ford et al. 2021 — **Software Architecture: The Hard Parts**
- Fowler — **Patterns of Enterprise Application Architecture**
- Hohpe, Woolf — **Enterprise Integration Patterns**

### Vakalar
- Shopify — *The Majestic Modular Monolith* (blog)
- Amazon Prime Video 2023 — *Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%*
- Segment — *Goodbye Microservices: From 100s of problem children to 1 superstar*
- Uber — *Microservice Architecture at Uber*

---

## 🤖 13. AI/ML — Backend Açısından

### RAG & Vektör DB
- Lewis et al. 2020 — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*
- Malkov, Yashunin 2018 — *Efficient and robust approximate nearest neighbor search using HNSW*
- Jegou et al. 2011 — *Product Quantization for Nearest Neighbor Search* (IVF temeli)
- Guo et al. 2020 — *Accelerating Large-Scale Inference with Anisotropic Vector Quantization* (ScaNN)

### LLM Operasyon
- Yao et al. 2023 — *ReAct: Synergizing Reasoning and Acting in Language Models*
- *RAGAS* — Es et al. 2023, *RAGAS: Automated Evaluation of RAG*
- *TruLens* documentation

### MLOps
- Sculley et al. 2015 — *Hidden Technical Debt in Machine Learning Systems*
- Kleppmann, Kreps — *Online/Offline Feature Parity* tartışmaları

---

## 🏗️ 14. Modern / Edge / WASM

- Bytecode Alliance — WASI documentation
- *Cloudflare Workers* — engineering blog
- *Fastly Compute@Edge* — documentation
- Local-first software — Kleppmann et al. 2019 — *Local-first software: You own your data, in spite of the cloud*
- *Automerge* paper — Kleppmann, Beresford, Svingen 2019

---

## 👥 15. Staff+ Soft Skills

- Reilly 2022 — **The Staff Engineer's Path**
- Larson 2021 — **Staff Engineer: Leadership beyond the management track**
- Skelton, Pais 2019 — **Team Topologies**
- Forsgren et al. — **Accelerate** (yukarıda)
- Hunt, Thomas — **The Pragmatic Programmer** (20th anniv., 2019)

### Yazma kültürü
- Amazon — *6-pager* memo formatı (Bezos shareholder letters'da bahsi)
- *Amazon PRFAQ* — working backwards süreci
- Google — Design Doc culture (Caitie McCaffrey, Jeff Dean tweets)
- ThoughtWorks — *Architecture Decision Records (ADR)* (Michael Nygard 2011)

---

## 🎯 16. Sayısal Sezgi (Latency / Capacity)

- Jeff Dean — *Numbers Everyone Should Know* (Stanford 2009 dersi)
- Aleksey Shipilёv — JMH / latency benchmarking talks
- Brendan Gregg — *Latency Heat Maps* blog series

---

## 📜 17. Ünlü Postmortem Arşivleri

- *Awesome Postmortems* — github.com/danluu/post-mortems
- AWS Service Health Dashboard arşivleri
- GitHub Engineering blog — "Investigating..." postları
- Cloudflare blog — "What happened on..."
- GitLab Engineering — "Postmortem of database outage of January 31"

---

## 🔧 Kullanım

Bir konuyu derinleştirmek istediğinde bu listeden başla. Her doküman sonundaki **"İleri Okuma"** bölümleri buraya referans verir. Bir paper'ı eklemek istersen: PR aç, ilgili tematik bölüme yıl sırasında ekle.
