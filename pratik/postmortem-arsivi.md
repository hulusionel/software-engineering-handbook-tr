# 💀 Postmortem Arşivi — Ünlü Outage'lardan Dersler

> **"Senior mühendis, kendi başına gelmemiş hatalardan ders çıkarandır."**

Bu doküman tarihin en öğretici ~20 üretim olayını **yapı-temelli** analiz eder. Her vaka için: **Trigger, contributing factors, mitigation, action items, generalizable lessons.** Sansasyon değil; **mimari ve süreç** dersleri.

> 🔗 Format: [postmortem-sablon.md](../templates/postmortem-sablon.md) ile uyumlu.

---

## 📑 İçindekiler

| # | Olay | Yıl | Sektör | Ana ders |
|---|---|---|---|---|
| 1 | [Knight Capital](#1-knight-capital--440m-45-dakikada) | 2012 | Finans | Dead code + flag yeniden kullanımı |
| 2 | [GitLab DB silme](#2-gitlab-2017--production-veritabanı-silindi) | 2017 | DevOps | Backup ≠ restore + insan-makine arayüzü |
| 3 | [AWS S3 us-east-1](#3-aws-s3-us-east-1-2017--debug-typo) | 2017 | Cloud | Tooling input validation + blast radius |
| 4 | [GitHub MySQL](#4-github-2018--24-saat-tutarsızlık) | 2018 | DevOps | Cross-region failover + split-brain |
| 5 | [Cloudflare regex](#5-cloudflare-2019--regex-cpu-tükenmesi) | 2019 | Edge | ReDoS + global rollout |
| 6 | [Cloudflare BGP leak](#6-cloudflare-2019-haziran--verizon-bgp-leak) | 2019 | Networking | BGP route filter eksikliği |
| 7 | [GitLab gitaly](#7-gitlab-2020--shared-storage-failure) | 2020 | DevOps | Single point of failure |
| 8 | [Slack auth meltdown](#8-slack-2021-ocak--baglanti-fırtınası) | 2021 | SaaS | Connection storm + thundering herd |
| 9 | [Fastly config](#9-fastly-2021-haziran--tek-müşteri-config-ile-internet-yarısı) | 2021 | Edge | Tek tetikleyicinin küresel etkisi |
| 10 | [Akamai DNS](#10-akamai-2021-temmuz--dns-config-rollback-yok) | 2021 | Edge | Rollback prosedürünün eksikliği |
| 11 | [Roblox Consul](#11-roblox-2021-ekim--consul-cascading-failure) | 2021 | Gaming | Service discovery cascading failure |
| 12 | [Facebook BGP withdraw](#12-facebookmeta-2021-ekim--kendini-internetten-cıkardı) | 2021 | Sosyal | İçeride dış araçlara bağımlılık |
| 13 | [AWS us-east-1 Kinesis](#13-aws-us-east-1-2021-aralık--ic-bagımlılık-zinciri) | 2021 | Cloud | Bölge içi bağımlılık fan-out |
| 14 | [log4shell](#14-log4shell-cve-2021-44228--gunluğun-kod-calıstırması) | 2021 | Güvenlik | Log girdisinde JNDI injection |
| 15 | [Atlassian veri kaybı](#15-atlassian-2022-nisan--maintenance-script-müşterileri-sildi) | 2022 | SaaS | Soft delete'siz sahip silme |
| 16 | [Datadog uzantısı](#16-datadog-2023-mart--bölgesel-systemd-bug) | 2023 | Observability | Çekirdek-üstü yan etki |
| 17 | [Discord journal](#17-discord-2023-haziran--mongodb-snapshot-recovery) | 2023 | Sosyal | Recovery testinin yokluğu |
| 18 | [CrowdStrike Falcon](#18-crowdstrike-2024-temmuz--dünya-kernel-driver-ile-durdu) | 2024 | Güvenlik | Kernel driver canary'siz rollout |
| 19 | [Google Cloud Universe](#19-google-cloud-2024-mayıs--unicredit-musteri-projesi-silindi) | 2024 | Cloud | Replikasyon ≠ backup |
| 20 | [TigerBeetle simulation finds](#20-tigerbeetle-yöntemi--simulation-driven-development) | 2024 | Finans | Simulation testing örneği (pozitif vaka) |

---

## 1. Knight Capital — $440M 45 dakikada

**📅 Tarih:** 1 Ağustos 2012
**🕐 Süre:** 45 dakika canlı, ardından 1 hafta içinde şirket battı.

### Trigger
SMARS adlı emir yönlendirme sistemine yeni RLP modülü deploy edildi. **8 sunucudan 7'sine kod gitti, 1'inde eski kod kaldı** (manuel deployment, otomasyon yok). Yeni kod, 2003'ten kalan **"Power Peg"** test bayrağını yeniden kullandı. Eski sunucu o bayrağı **eski anlamıyla** yorumladı: "alt limit yokken sınırsız al-sat".

### Sonuç
- Saniyede binlerce piyasa emri gitti.
- 45 dakikada **$440 milyon** zarar.
- Hisse %75 düştü; şirket bir hafta içinde Getco'ya satıldı.

### Sistemik zayıflıklar
1. **Kullanılmayan kod (dead code) silinmedi** — 8 yıl bekledi.
2. **Bayrak yeniden kullanıldı** (yeni anlam vermek için eski isim).
3. **Manuel deployment** — bir node'u atlamak insan hatasıyla mümkündü.
4. **Pre-deployment dry run yok**.
5. **Emir akışında devre kesici (kill switch) yok** — yöneticiler 45 dk müdahale edemedi.

### Genelleştirilebilir dersler
- ☠️ **Dead code ölü değildir.** Silinmedikçe, bir gün başka bir şeyle yeniden tetiklenir.
- 🚦 **Feature flag isim yeniden kullanılmaz.** Yeni davranış → yeni isim.
- 🛑 **Finansal sistemde kill switch zorunlu** (otomatik trip eşiği + manuel düğme).
- 🤖 **Manuel deploy adımı = sıfır olmalı**. Atomik all-or-nothing.

---

## 2. GitLab 2017 — Production veritabanı silindi

**📅 Tarih:** 31 Ocak 2017
**🕐 Süre:** ~18 saat tam restore.

### Trigger
Replication lag büyüdü. SRE ekibi sorunu çözmek için **secondary** DB'yi temizlemek istedi. Yorgun mühendis (gece 23:00 sonrası) **yanlış pencerede** `rm -rf` çalıştırdı → **primary** silindi.

### Backup durumu (8 katman, hiçbiri çalıştı)
1. **LVM snapshot:** 6 saat eski.
2. **Daily backup:** Disk dolduğu için **boş dosya** atılıyordu.
3. **Azure disk snapshot:** DB için aktif değildi.
4. **PostgreSQL replication:** Az önce silindi.
5. **WAL-E S3:** **Hiç ayar yapılmamıştı.**
6. **Periyodik logical backup:** 24 saat eski.
7. **Staging env:** **Eski dump'tan kuruldu, çalıştığı düşünülüyordu.**
8. **Geliştirici makinesinde dump:** Şans eseri 6 saat eski → kurtarıcı oldu.

### Sonuç
- **6 saatlik veri kaybı** (issues, MR'lar, commits, kullanıcılar).
- Olay canlı YouTube yayınında düzeltildi (transparency MVP).

### Sistemik zayıflıklar
1. **Backup'ların geri yüklenebilirliği test edilmiyordu.**
2. **Sudo kabuk pencereleri görsel olarak ayırt edilemez** (pre-prompt warning yoktu).
3. **On-call rotasyonu yorgun bireye yığıldı**.
4. **Disaster recovery drill** yıllardır yapılmamıştı.

### Genelleştirilebilir dersler
- 🧪 **Backup ≠ restore.** Yılda en az 2 kez **gerçekten geri yükle**, RTO'yu ölç.
- 🎨 **Production prompt'ları görsel olarak farklılaştır** (renk, hostname banner).
- 🚷 **Yorgun mühendis = yüksek risk.** "Get a buddy" politikası SEV1 dışı işlerde.
- 📜 **Backup checklist'i monitor'lu olmalı**: "son 24h'de başarılı restore yapıldı mı?".

---

## 3. AWS S3 us-east-1 2017 — Debug typo

**📅 Tarih:** 28 Şubat 2017
**🕐 Süre:** 4 saat

### Trigger
S3 ekibi billing alt-sisteminde yavaşlama araştırıyordu. Bir mühendis **debug tool ile az sayıda sunucu kapatmak istedi**, parametrede typo yaptı, **çok daha büyük bir alt-küme** kapandı. Bu alt-küme, S3'ün **index ve placement** subsystem'lerini içeriyordu — bunlar olmadan S3 hiç çalışmaz.

### Sonuç
- us-east-1 bölgesinde S3 4 saat down.
- Bağımlı servisler (Slack, Trello, Quora, Medium, hatta AWS Health Dashboard'un kendisi) çöktü.
- **AWS Health Dashboard'u S3'e bağlıydı** → "her şey iyi" gösterdi 😬.

### Sistemik zayıflıklar
1. **Tool'da input validation yok**: yüksek-etkili komutlar onay istemezdi.
2. **Index subsystem yıllardır restart edilmemişti**: cold start çok uzun sürdü.
3. **AWS dashboard'unun kendisi failed dependency'ye bağlıydı**.
4. **Blast radius hesaplı değildi** — bir komut tüm bölgeyi etkileyebiliyordu.

### Genelleştirilebilir dersler
- 🛡️ **Tehlikeli komutlar guard'lı olmalı**: dry-run, confirmation, magic-string.
- 🌍 **Status sayfası kendi sistemine bağımlı olamaz.** Out-of-band hosting.
- 🔄 **Cold start'ları periyodik test et**: yıllarca restart edilmemiş subsystem son raunda hazır değildir.
- 📦 **Blast radius limit'i**: tek komutun max etkileyebileceği makine sayısı tool seviyesinde sabit.

---

## 4. GitHub 2018 — 24 saat tutarsızlık

**📅 Tarih:** 21-22 Ekim 2018
**🕐 Süre:** ~24 saat 11 dakika.

### Trigger
Bir optik fiber çalışması East Coast → West Coast trafiğini **43 saniye** kopardı. Bu süre yeterliydi ki **Orchestrator**, batı kümesini "primary" yaptı. Bağlantı dönünce iki primary aynı anda yazıyordu → **split brain**.

### Hangi veriler etkilendi?
- 5 dakika boyunca her iki taraf da yazdı.
- Webhook, gist, branch metadata: ~954 yazma çakışması.
- Çözüm: **Yazılımsal merge yok**, **manuel reconciliation** gerekti.

### Sistemik zayıflıklar
1. **Failover otomasyonu** ağ kesintisini *kalıcı kesinti* sandı.
2. **Split-brain detection** çok geç tetiklendi.
3. **Cross-region replication async** olduğu için lag birikmişti.

### Genelleştirilebilir dersler
- ⏳ **Failover'da minimum failover delay** ayarla — geçici hıçkırıklara sabret.
- 🎯 **Split-brain prevention** için **fencing token** veya **STONITH** mekaniği.
- 📊 **Network partition **simülasyonu** (chaos test) yıllık.

---

## 5. Cloudflare 2019 — Regex CPU tükenmesi

**📅 Tarih:** 2 Temmuz 2019
**🕐 Süre:** 27 dakika global, %82 traffic 502.

### Trigger
WAF kuralı XSS detection için **catastrophic backtracking** içeren bir regex aldı:

```regex
(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*(?:.*=.*)))
```

→ Belirli input'larla **eksponansiyel** zaman alıyor. CPU %100, all-traffic 502.

### Sistemik zayıflıklar
1. **WAF kuralı tüm dünyaya aynı anda deploy edildi** (kanarya yok).
2. **Regex performans sınırı (RE2 / re-limited)** kullanılmıyordu.
3. **CPU watchdog (max process time)** yoktu.

### Genelleştirilebilir dersler
- 📐 **Regex tehlikelidir.** Kullanıcıya yakınsa **RE2** veya benzeri lineer-zaman-garanti motoru kullan.
- 🐤 **Edge config'i kanarya'sız deploy edilmez.** %1 → %10 → %50 → %100.
- ⏰ **Per-request CPU bütçesi** zorunlu (ör. 10 ms üstü kill).

---

## 6. Cloudflare 2019 Haziran — Verizon BGP leak

**📅 Tarih:** 24 Haziran 2019
**🕐 Süre:** ~2 saat.

### Trigger
Pennsylvania'da küçük bir ISP (DQE), kendi BGP router'ında route optimizer kullandı; sonuç olarak **internet'in büyük kısmının route'larını** kendi network'üne sızdırdı. Verizon, bu route'ları **route filter olmadan** kabul edip global'e yaydı.

### Sonuç
- Cloudflare, AWS, Linode trafiğinin önemli kısmı küçük bir ISP üzerinden geçti.
- 502 ve timeout patlaması.

### Sistemik zayıflıklar
1. **Verizon'da BGP filter yok** (RFC 7454'e uyumsuz).
2. **RPKI** (Resource Public Key Infrastructure) yaygın değildi.

### Genelleştirilebilir dersler
- 🌐 **BGP komşularına filter zorunlu**. Her org kendi MANRS uyumunu kontrol etmeli.
- 🔐 **RPKI route origin validation** vendor seçim kriteri olmalı.
- 🚧 İnternet **merkezi-olmayan** olduğu kadar **kırılgan** ve "olmazsa olmaz" partner zinciri var.

---

## 7. GitLab 2020 — Shared storage failure

**📅 Tarih:** 1 Eylül 2020
**🕐 Süre:** ~5 saat git operasyonları.

### Trigger
**Gitaly** (Git RPC sunucusu) kullandığı CephFS storage'da paket kaybı yaşadı. Git operasyonları timeout'a düştü. Push retry → bağlantı patlaması → daha çok timeout.

### Genelleştirilebilir dersler
- 🚧 **Shared storage** dağıtık sistem performansının en zayıf halkasıdır.
- 🔁 **Retry storm**'u önlemek için **exponential backoff + jitter** zorunlu.
- 🧊 **Local SSD** üzerinden replication, network FS'den hızlıdır ve daha öngörülebilirdir.

---

## 8. Slack 2021 Ocak — Bağlantı fırtınası

**📅 Tarih:** 4 Ocak 2021
**🕐 Süre:** ~3 saat.

### Trigger
Yeni yıl tatili sonrası ilk Pazartesi. Kullanıcı sayısı normalin %2-5 üstündeydi. Internal AWS scaling grubu yetişmedi → bazı backend service'leri TCP TIME_WAIT'i tüketti. Yeni bağlantılar açılamadı; client'lar **agresif retry** ile durumu kötüleştirdi.

### Sistemik zayıflıklar
1. **Tatil sonrası kapasite tahmini** insan davranışını yanlış modelledi.
2. **Client-side retry** exponential backoff'suzdu.
3. **TIME_WAIT** sayısı dashboard'da değildi.

### Genelleştirilebilir dersler
- ❄️ **Tatil sonrası ilk gün** = en yüksek risk. Kapasiteyi 2× tut.
- 🎚️ **TIME_WAIT** üretim metriği olmalı.
- 🔁 Client retry: **exponential + jitter + circuit breaker** üçlüsü.

---

## 9. Fastly 2021 Haziran — Tek müşteri config ile internet yarısı

**📅 Tarih:** 8 Haziran 2021
**🕐 Süre:** ~1 saat.

### Trigger
Bir müşterinin geçerli config değişikliği, Fastly'nin POP yazılımındaki **dormant bug**'ı tetikledi. Tek POP'tan tüm POP'lara cascade. Sonuç: NYTimes, Reddit, Twitch, BBC, UK Gov, Amazon, eBay simultane down.

### Genelleştirilebilir dersler
- 🐛 **Dormant bug**'lar config değişikliği ile uyanır. Config değişikliği = code değişikliği gibi davran.
- 🌐 **Edge platform'ları** tek-tenant'ın hatasını **multi-tenant** kuruluşlara yansıtmamalı.
- 🐤 Müşteri config değişiklikleri bile **kanarya** ile gitmeli.

---

## 10. Akamai 2021 Temmuz — DNS config rollback yok

**📅 Tarih:** 22 Temmuz 2021
**🕐 Süre:** ~1 saat.

### Trigger
DNS hizmetinde routing config değişikliği. **Rollback prosedürü test edilmemişti**, panik içinde uygulanırken sorunu uzattı.

### Genelleştirilebilir dersler
- 🔄 **Rollback** = production prosedür. Drill et.
- ⏰ **MTTR**, MTTD ve MTBF ile birlikte raporlanır.

---

## 11. Roblox 2021 Ekim — Consul cascading failure

**📅 Tarih:** 28-31 Ekim 2021
**🕐 Süre:** **73 saat** (3 gün).

### Trigger
Yeni "streaming" özelliği Consul KV store'a yoğun yazma yapıyordu. Belirli bir trafik seviyesinde Consul leader CPU'su saturate oldu, leader election döngüsü başladı. Her election diğer service'lerin discovery'sini bozdu → cascading failure.

### Etki
- 50M kullanıcı 3 gün servisi kullanamadı.
- Mühendislik ekibi paralel: HashiCorp + Roblox.
- Çözüm: Consul performans tuning + KV write traffic'i ayrı kümeye almak.

### Sistemik zayıflıklar
1. **Service discovery = single point of failure.** Tüm sistem ona bağlıydı.
2. **Consul'a write/read trafiği aynı küme**.
3. **Capacity test**'leri canlı yük seviyesini yakalamamıştı.

### Genelleştirilebilir dersler
- 🏛️ **Service discovery** kararlılık sınıfında en yüksek olmalı; özellik geliştirme rotalanmaz.
- 📊 **Read/Write workload izolasyonu** discovery + KV için ayrı.
- 🧪 **Production-realistic load test** zorunlu (synthetic değil, real traffic shadow).

---

## 12. Facebook/Meta 2021 Ekim — Kendini internetten çıkardı

**📅 Tarih:** 4 Ekim 2021
**🕐 Süre:** ~6 saat.

### Trigger
Backbone fiziksel network audit komutu, **bug nedeniyle tüm BGP advertisement'larını çekti**. Sonuç:
- Facebook, Instagram, WhatsApp, Oculus DNS'leri **internet'te yok oldu**.
- DNS resolver'lar timeout → trafik patlaması başka servislere kaydı.
- **İçerideki araçlar** (Workplace, badge erişimi) Facebook auth'a bağlıydı → mühendisler datacenter'a fiziksel giremedi!

### Sistemik zayıflıklar
1. **Audit komutunun blast radius'u sınırsız**.
2. **Out-of-band çıkış yok** — internal araçlar dış internet üzerinden auth'lanıyordu.
3. **Datacenter fiziksel erişimi** Facebook badge'ine bağlı.

### Genelleştirilebilir dersler
- 🚪 **Out-of-band yönetim** (SSH bastion, alternatif identity, fiziksel anahtar) zorunlu.
- 🔌 **Operatör araçları üretim sistemine bağımlı olamaz.**
- 🎚️ Tehlikeli komutlar için **iki insan onayı** (4-eyes principle).

---

## 13. AWS us-east-1 2021 Aralık — İç bağımlılık zinciri

**📅 Tarih:** 7 Aralık 2021
**🕐 Süre:** ~7 saat.

### Trigger
Internal scaling tetiklendi. Internal API gateway, throttling thresholds'u aşan trafik aldı. **API gateway'in monitoring'i de kendi içinde** aynı API gateway'den geçiyordu → görünürlük yok. ELB, CloudWatch, Lambda, RDS, EC2 console hepsi etkilendi.

### Genelleştirilebilir dersler
- 🪞 **Monitoring kendi sistemini observe edemez.** Out-of-band telemetry gerekli.
- 🌐 us-east-1 = AWS'nin "kontrol düzlemi" merkezi → çoklu bölgeyi mümkün olan her yerde dağıt.

---

## 14. log4shell (CVE-2021-44228) — Günlüğün kod çalıştırması

**📅 Tarih:** 9 Aralık 2021
**🌍 Etki:** Internet'in geniş kısmı.

### Trigger
log4j 2.x'in JNDI lookup özelliği, **log mesajındaki** `${jndi:ldap://...}` ifadesini değerlendirip **uzaktan sınıf yüklemesine** izin veriyordu. User-Agent'a yazılan satır kod çalıştırıyordu.

### Sistemik zayıflıklar
1. **Logger'da kod yürütme** — özellik tasarımı.
2. **Uzun yaşlı OSS bileşeni**, supply chain.
3. **Default'lar güvensiz**.

### Genelleştirilebilir dersler
- 🔒 **Untrusted input → kod yürütme = imkansız** olmalı (her abstraction katmanında).
- 📦 **SBOM** (Software Bill of Materials) zorunlu — etkilenen sistemleri listeleyebilmek için.
- 🛡️ **Secure-by-default** > opt-in security.

---

## 15. Atlassian 2022 Nisan — Maintenance script müşterileri sildi

**📅 Tarih:** 5 Nisan — 18 Nisan 2022
**🕐 Süre:** **2 hafta** restore.

### Trigger
Eski "Insight" özelliğini kaldırmak için maintenance script çalıştırıldı. Script, "Insight'ı kaldır" yerine **400+ müşteri tenant'ının tamamını sildi** (yanlış ID listesi).

### Restore neden 2 hafta sürdü?
- Backup'lar mevcuttu, ama **tek-tenant restore** prosedürü yoktu.
- Her tenant **manuel** geri yüklendi.

### Genelleştirilebilir dersler
- 🗑️ **Soft delete** zorunlu — hiçbir destructive operasyon hard-delete değildir.
- 🪟 **Tenant-level point-in-time restore** SaaS'ın temel yeteneği olmalı.
- 📋 Tehlikeli script: dry-run + diff review + 4-eyes + canary tenant.

---

## 16. Datadog 2023 Mart — Bölgesel systemd bug

**📅 Tarih:** 8 Mart 2023
**🕐 Süre:** ~24 saat.

### Trigger
Ubuntu 22.04 systemd'in `systemd-resolved` bileşenindeki bir bug, **eş zamanlı** olarak 5 farklı bölgede tetiklendi (otomatik OS update). Datadog agent'lar DNS resolve edemedi → metric akışı durdu.

### Genelleştirilebilir dersler
- 🌍 **Çoklu bölge ≠ izolasyon**, eğer aynı OS image'ı **aynı anda** otomatik güncelleniyorsa.
- 🔄 OS update'leri bölgeler arası **fasing** yapılmalı (rolling).
- 📡 Observability platformunun OS bağımlılıklarına özel ihtimam.

---

## 17. Discord 2023 Haziran — MongoDB snapshot recovery

**📅 Tarih:** 23 Haziran 2023
**🕐 Süre:** ~10 saat.

### Trigger
MongoDB cluster'ın replica seti drift etti. Recovery için snapshot'tan restore gerekti. **Snapshot'lar düzenli alınıyordu ama restore sürecini kimse yıllardır test etmemişti** — gerçek RTO beklentinin **8×** üstüne çıktı.

### Genelleştirilebilir dersler
- 🧪 **Restore drill yıllık zorunlu**, ölçülmüş RTO ile.
- 📐 Recovery prosedürü playbook'unun **versionu** olmalı; cluster topolojisi değiştiğinde update edilmeli.

---

## 18. CrowdStrike Falcon 2024 Temmuz — Dünya kernel driver ile durdu

**📅 Tarih:** 19 Temmuz 2024
**🕐 Süre:** Çoğu kuruluş için 1-3 gün.

### Trigger
CrowdStrike Falcon Sensor'ün **kernel-mode driver**'ına yapılan content update, malformed data içerdi. Driver crash → BSOD. Windows boot sırasında Falcon yüklendiği için **boot loop**.

### Etki
- 8.5 milyon Windows makinesi etkilendi.
- Havayolları, hastaneler, bankalar durdu.
- Manuel düzeltme gerekti (her makineye fiziksel müdahale).

### Sistemik zayıflıklar
1. **Content update, code update gibi davranılmadı** — staged rollout yoktu.
2. **Driver canlı çalışırken malformed input parse** ediyordu (no validation).
3. **Kernel driver güvenliği = işletim sistemi güvenliği**.

### Genelleştirilebilir dersler
- 🐤 **Her update kanarya'lı**, içerik dahil.
- 🛡️ **Kernel-level kod input validation** kritik.
- 🔄 **Otomatik recovery** (safe mode + auto-rollback) işletim sistemi seviyesi.

---

## 19. Google Cloud 2024 Mayıs — UniCredit müşteri projesi silindi

**📅 Tarih:** Mayıs 2024
**🕐 Süre:** **2 hafta** restore.

### Trigger
UniSuper'in (Avustralya emeklilik fonu) Google Cloud projesi, GCP-tarafı internal config hatası nedeniyle **silindi**. Google bunu "tek-seferlik unprecedented" olarak duyurdu.

### Recovery
- UniSuper'in own backup'ları (off-cloud) sayesinde kurtuldu.
- Google'ın replikasyonu da silinmişti — replication ≠ backup.

### Genelleştirilebilir dersler
- ☁️ **Cloud provider'a güvenme.** Backup başka cloud'da veya on-prem.
- ❌ **Replication ≠ backup**: silmeyi de replicate eder.
- 📅 **3-2-1 kuralı**: 3 kopya, 2 farklı medya, 1 off-site.

---

## 20. TigerBeetle yöntemi — Simulation-driven development

**📅 Tarih:** Sürekli
**🎯 Pozitif vaka.**

### Yaklaşım
TigerBeetle (finansal ledger DB), kendi yazılımını **deterministic simulation**'da çalıştırır:
- Network: random partition, paket kayıp, reorder.
- Disk: bit rot, fsync gecikme, dolu disk.
- Time: clock skew.
- Crashes: random kill her N işlemde.

Yıllık eşdeğer **400.000+ saat simulation**. Hata bulunursa stack trace + seed yeniden üretilebilir.

### Dersler
- 🧠 **Determinizm** test edilebilirliğin temelidir.
- 🎲 **Fuzzing**'i sistem seviyesine taşı.
- 📜 **Doğru olduğu kanıtlanmamış kod yanlıştır.**

---

## 🎓 Tüm Vakalardan Sentez

### 5 tekrar eden tema

1. **Backup/restore drill yapılmıyor.** Backup var sanıyoruz; restore çalışmıyor (#2, #15, #17, #19).
2. **Blast radius sınırsız**: tek komut, tek config tüm üretimi etkiledi (#1, #3, #9, #12, #15).
3. **Monitoring/auth/discovery sistemi kendine bağımlı** (#3, #11, #12, #13).
4. **Canary olmayan rollout**: code, config, content (#5, #9, #14, #18).
5. **Cascading failure** retry storm + thundering herd (#7, #8, #11).

### 10 staff+ kontrol listesi (her sistem için)

- [ ] Restore drill yıllık takvimde mi? RTO **ölçülmüş** mü?
- [ ] En tehlikeli komutun **blast radius limit'i** kodda var mı?
- [ ] Status sayfası **out-of-band** host edilmiş mi?
- [ ] Auth sistemi **kendi auth'una** bağlı değil, değil mi?
- [ ] Service discovery'nin **read** ve **write** trafiği ayrı küme mi?
- [ ] Tüm rollout (code + config + content) kanaryalı mı?
- [ ] Client retry: **exponential + jitter + circuit breaker** üçlüsü tam mı?
- [ ] **Soft delete** SaaS'ta zorunlu mu? Tenant-level PITR var mı?
- [ ] Backup'lar **farklı cloud / off-site** mi? (Replication backup değil.)
- [ ] **Simulation/chaos testing** prod-realistic yük altında yıllık var mı?

---

## 📚 İleri Okuma

- *Awesome Postmortems* — github.com/danluu/post-mortems (canon liste)
- John Allspaw — *Blameless Postmortems and a Just Culture* (Etsy 2012)
- *How Complex Systems Fail* — Richard Cook (1998), 18 sayfa, mutlak okunmalı
- Kafka book — *Site Reliability Engineering* (Google), bölüm 15 Postmortem Culture
- *Resilience Engineering* — Hollnagel, Woods, Leveson
- TigerBeetle blog — *Simulation Testing*

> [⬅️ Pratik klasörü](README.md) · [📋 Postmortem şablonu](../templates/postmortem-sablon.md)
