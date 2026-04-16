# 🚀 Senior Backend Developer Yol Haritası

## 📋 İçindekiler
1. [Giriş](#giriş)
2. [Cloud Infrastructure & DevOps](#-cloud-infrastructure--devops)
3. [Kubernetes & Container Orchestration](#-kubernetes--container-orchestration)
4. [Event-Driven Architecture](#-event-driven-architecture)
5. [Microservices & Distributed Systems](#-microservices--distributed-systems)
6. [API Design & Communication](#-api-design--communication)
7. [Database & Data Management](#-database--data-management)
8. [Search & Real-time Technologies](#-search--real-time-technologies)
9. [Security & Authentication](#-security--authentication)
10. [Monitoring & Observability](#-monitoring--observability)
11. [Deployment Strategies & GitOps](#-deployment-strategies--gitops)
12. [Architecture Patterns](#-architecture-patterns)
13. [CRM ve Diğer Business Uygulamaları](#-crm-ve-diğer-business-uygulamaları)
14. [Team Leadership & Engineering Management](#-team-leadership--engineering-management)
15. [Production Excellence](#-production-excellence)
16. [Best Practices & Soft Skills](#-best-practices--soft-skills)
17. [Node.js Internals & Performance](#-nodejs-internals--performance)
18. [Yapay Zeka Çağında Backend Engineering](#-yapay-zeka-çağında-backend-engineering)
19. [Öğrenme Kaynakları](#-öğrenme-kaynakları)
20. [Gelişim Yol Haritası](#-gelişim-yol-haritası)
21. [Özet & Aksiyon Planı](#-özet--aksiyon-planı)

---

## 🎯 Giriş

Bu doküman, mevcut bir backend developer'dan senior seviyeye geçiş için gerekli bilgi ve becerileri kapsamaktadır. Lambda, cron job, consumer/producer gibi araçları kullanmış olsanız da, bunların altyapısını, neden ve nasıl çalıştıklarını, ne zaman kullanılacaklarını derinlemesine anlamak senior seviyeye geçişin anahtarıdır.

---

## ☁️ Cloud Infrastructure & DevOps

### AWS Compute Services

#### 1. EC2 (Elastic Compute Cloud)

**EC2 Nedir? — Bulutta Bilgisayar Kiralamak**

EC2'yi şöyle düşünün: Bir bilgisayar satın almak yerine, bulutta bir bilgisayar **kiralıyorsunuz**. Evde server odası kurmak, klima takmak, UPS almak, 7/24 elektrik ödemek yerine — Amazon'un devasa data center'larından bir makine kiralıyorsunuz. Anahtarı alıyorsunuz, istediğiniz işletim sistemini kuruyorsunuz, yazılımlarınızı yüklüyorsunuz. Tamamen sizin kontrolünüzde. "Elastik" olması da şu demek: Bayram trafiği geldi mi 10 makine daha eklersiniz, trafik düşünce kapatırsınız. Fiziksel sunucuda bunu yapmaya çalışsanız, sunucuyu sipariş edin, kargo bekleyin, rack'e takın... 3 haftanız gider.

**Instance Tipleri — Araba Seçmek Gibi:**

EC2 instance tipi seçmek, araba seçmeye benzer. Herkesin ihtiyacı farklı:

| Tip | Analoji | Kullanım | Örnekler |
|-----|---------|----------|----------|
| **General Purpose (t3, m5)** | Sedan araba — her işe yarar | Web sunucuları, küçük-orta uygulamalar | t3.micro, t3.small, m5.large |
| **Compute Optimized (c5)** | Spor araba — hız şart | Yoğun hesaplama, video encoding, ML inference | c5.large, c5.4xlarge |
| **Memory Optimized (r5)** | Kamyon — çok yük taşır | Büyük veritabanları, in-memory cache | r5.large, r5.2xlarge |
| **GPU (p3, g4)** | Formula 1 — özel yarış aracı | Deep learning training, 3D rendering | p3.2xlarge |

**Fiyatlandırma — Cebinizi Düşünün:**

EC2'nin 3 temel fiyatlandırma modeli var ve aralarındaki fark DEVASA:

- **On-Demand (Anında):** Otel odasına walk-in girmek gibi. En pahalı ama en esnek. İstediğiniz zaman açıp kapatırsınız. Test/geliştirme ortamları için ideal.
- **Reserved Instances (Rezerve):** 1-3 yıllık sözleşme imzalarsınız. **%50-72 tasarruf!** Evinizi kiralamak gibi — uzun vadeli taahhüt, ama çok daha ucuz. Production workload'ları için birebir.
- **Spot Instances (Spot):** Amazon'un boşta kalan kapasitesini satması. **%90'a varan tasarruf!** AMA — Amazon istediği zaman makinenizi 2 dakika uyarıyla GERİ ALABİLİR. Müzayedede tezgah açmak gibi: ucuz ama güvensiz. Batch processing, CI/CD pipeline'ları, stateless workload'lar için harika.

**💰 Gerçek Dünya Örneği:**
Bir startup hikayesi: İlk gün `t3.micro` ($8/ay) ile başladılar. Kullanıcı sayısı arttıkça `t3.medium`'a geçtiler. Viral oldular — `c5.4xlarge` aldılar compute-heavy operasyonlar için. Reserved instance aldıklarında aylık AWS faturası $2000'dan $800'a düştü. Spot instance'ları da CI/CD pipeline'larında kullanıp test maliyetlerini %85 azalttılar.

**Security Groups — Sanal Güvenlik Duvarı:**

Security Group, EC2 instance'ınızın etrafındaki **sanal güvenlik duvarıdır**. Bir apartman kapısının güvenlik görevlisi gibi düşünün: kim girebilir, kim giremez?

- **Inbound Rules:** Hangi IP'lerden hangi portlara erişilebilir? (Örn: "Sadece şirket VPN'inden SSH izni ver")
- **Outbound Rules:** Instance dışarıya ne yapabilir?
- **Stateful:** Bir isteğe izin verdiyseniz, cevabı otomatik geçer. Güvenlik görevlisi misafiri içeri aldıysa, çıkışta tekrar sormaz.
- **Deny by Default:** Açıkça izin vermediğiniz her şey engellidir. "Paranoyak güvenlik görevlisi" modu.

**Lambda ile Farkı:**
```
EC2:
- Sürekli çalışan sunucu
- Tam kontrol (OS, network, security)
- Ölçeklemesi manuel veya Auto Scaling ile
- Dakika bazlı ücretlendirme
- Örnek: Web server, database, long-running processes

Lambda:
- Serverless (sunucusuz)
- Event-triggered (olay tetiklemeli)
- Otomatik ölçekleme
- Milisaniye bazlı ücretlendirme
- Örnek: API endpoints, scheduled tasks, event processors
```

**Ne Zaman Kullanılır:**
- **EC2**: Sürekli çalışması gereken uygulamalar (web server, database, cache)
- **Lambda**: Kısa süreli, event-driven işlemler (API calls, image processing)

**Öğrenmeniz Gerekenler:**
```bash
# EC2 Instance Types
- t3.micro, t3.small (genel amaçlı, düşük maliyet)
- c5.large (compute-optimized)
- r5.large (memory-optimized)
- GPU instances (ML workloads için)

# Security Groups (Güvenlik Duvarı Kuralları)
- Inbound rules (hangi portlar açık)
- Outbound rules
- VPC içinde network izolasyonu

# AMI (Amazon Machine Image)
- Hazır imajlar ile hızlı deployment
- Kendi custom AMI'larınızı oluşturma

# Auto Scaling
- Load'a göre otomatik instance ekleme/çıkarma
- Health checks
- Load balancer integration
```

#### 2. Lambda (Serverless Computing)

**Lambda Nedir? — Otomat Makinesi Analojisi**

Lambda'yı bir **otomat makinesi** gibi düşünün. Otomat makinesini siz satın almadınız, bakımını siz yapmıyorsunuz, elektriğini siz ödemiyorsunuz. Sadece butona basıyorsunuz ve sonucu alıyorsunuz. İşte Lambda tam olarak bu: siz kodu yazıyorsunuz, AWS gerisini hallediyor — sunucu yok, işletim sistemi yok, ölçekleme yok. Sadece "bu event geldiğinde şu kodu çalıştır" diyorsunuz.

Bu kadar basit olması hem güzel hem tehlikeli. Güzel çünkü müthiş hızlı geliştirme yaparsınız. Tehlikeli çünkü "serverless" demek "sorunsuz" demek değil — kendi kendine gelen bir sürü tuzağı var.

**Cold Start Problemi — Sabah İlk Kahve:**

Cold start, Lambda'nın en çok konuşulan problemidir. Otomat makinesi analojisine dönelim: makine uzun süredir kullanılmamışsa, ilk kahveyi yapmak için ısınması gerekir. İşte Lambda da böyle:

- **Cold Start (~100-1000ms):** Lambda ilk çağrıldığında, AWS bir container oluşturur, runtime'ı başlatır, kodunuzu yükler, dependency'leri initialize eder. Bu süre Java'da 3-5 saniyeye kadar çıkabilir! Node.js'te genelde 100-300ms.
- **Warm Start (~1-10ms):** Eğer Lambda yakın zamanda çağrıldıysa, container hâlâ ayakta — direkt kodunuz çalışır. Işık hızında.
- **Çözüm:** Provisioned Concurrency — otomat makinesini her zaman sıcak tutarsınız. Ama bu da para! Serverless'ın "sadece kullandığın kadar öde" felsefesiyle çelişir.

**Fiyatlandırma — İNANILMAZ Ucuz Olabilir:**

Lambda'nın fiyatlandırması 1ms çözünürlüğünde (minimum 100ms):
- **İlk 1 milyon istek/ay: ÜCRETSİZ** (evet, bedava!)
- Sonrası: $0.20 / 1 milyon istek
- Memory-duration: $0.0000166667 / GB-saniye

Pratik örnek: 128MB memory ile günde 100.000 kez çağrılan, ortalama 200ms süren bir Lambda → aylık maliyet: ~$5. Aynı işi EC2'de yapsan minimum $30-50/ay. 10x fark!

**Limitler — Duvarları Bilin:**

| Limit | Değer | Ne Demek? |
|-------|-------|-----------|
| Max Execution Süresi | **15 dakika** | Video transcoding gibi uzun işler için UYGUN DEĞİL |
| Max Memory | **10 GB** | Büyük ML modelleri sığmayabilir |
| Deployment Package | **250 MB** (unzipped) | Dev dependency'leri dahil etmeyin! |
| Concurrent Executions | **1000** (default) | Artırılabilir ama dikkat — downstream servisler patlar |
| /tmp Storage | **10 GB** | Geçici dosya işlemleri için |

**🚫 Lambda Ne Zaman YANLIŞ Seçim?**
- **Uzun süren işler:** 15 dakikayı aşan batch processing → ECS/Fargate kullanın
- **Stateful uygulamalar:** WebSocket, session yönetimi → EC2/ECS
- **Yüksek frekanslı çağrılar:** Saniyede 10.000+ istek → her cold start bir felaket, EC2 daha stabil
- **GPU gerektiren işler:** ML training → EC2 GPU instance veya SageMaker
- **Öngörülebilir yük:** 7/24 sabit trafik → Reserved EC2 çok daha ucuz olur

**Derinlemesine:**

```javascript
// Lambda'nın Anatomy'si
exports.handler = async (event, context) => {
  // event: Tetikleyen kaynak (API Gateway, S3, DynamoDB, SQS, etc.)
  // context: Runtime bilgileri (requestId, memory, timeout, etc.)
  
  // Cold Start vs Warm Start
  // Cold Start: İlk çağrıda container başlatılır (~100-1000ms)
  // Warm Start: Hazırdaki container kullanılır (~1-10ms)
  
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Success' })
  };
};
```

**Lambda Runtime Environment:**
- Container'lar: Her Lambda execution bir container içinde çalışır
- Execution Role: IAM permissions
- Environment Variables
- Layers: Shared code/dependencies
- VPC Integration: Private resources'a erişim

**Lambda Trigger Sources:**
```yaml
API Gateway: HTTP/REST API endpoints
S3: File upload/delete events
DynamoDB Streams: Database değişiklikleri
SQS: Queue messages
SNS: Notifications
EventBridge: Scheduled events (cron)
Kinesis: Real-time data streams
```

**Best Practices:**
- Keep functions small and focused (single responsibility)
- Minimize cold starts (Provisioned Concurrency, layers)
- Handle errors properly (DLQ - Dead Letter Queue)
- Monitor with CloudWatch Logs & X-Ray

#### 3. ECS/EKS (Container Orchestration)

Container orchestration, **bir orkestra şefi** gibi düşünülmelidir. 🎼 Elinizde 50 müzisyen (container) var. Hepsi aynı anda çalacak, kimisi solo yapacak, birisi hasta olursa yedek hazır olacak, seyirci (trafik) artınca belki birkaç müzisyen daha sahneye çıkacak. İşte ECS ve EKS, AWS'deki iki orkestra şefiniz.

**ECS (Elastic Container Service) — AWS'nin Kendi Çocuğu:**

ECS, AWS'nin sıfırdan geliştirdiği container orchestration servisidir. Kubernetes'ten ÇOK daha basit — ama o basitlik bir güç. AWS ekosistemiyle derin entegrasyonu var: IAM role'leri doğrudan task'lara atanır, CloudWatch log'ları otomatik akar, Application Load Balancer ile service discovery built-in.

ECS'in iki çalışma modu var:
- **EC2 Launch Type:** Container'larınız sizin yönettiğiniz EC2 instance'ları üzerinde çalışır. Makine seçimi, AMI güncelleme, OS patch'leme SİZİN sorumluluğunuz.
- **Fargate Launch Type:** 🪄 SIHIR! EC2 yok. Siz sadece "bu container'ı çalıştır, 512MB memory ver" diyorsunuz. AWS gerisini hallediyor. Hangi makinede çalışıyor? Bilmiyorsunuz. Bilmeniz de gerekmiyor. "Serverless containers" kavramı tam da bu.

**Fargate — EC2 Yönetiminden Kurtuluş:**

Fargate'i anlamak için şu hikayeyi düşünün: Taksi çağırıyorsunuz. Aracın markasını, lastik basıncını, motor yağını siz kontrol etmiyorsunuz. Sadece "beni şuraya götür" diyorsunuz. İşte Fargate, container'larınız için "serverless taksi". EC2 instance seçmek, cluster capacity yönetmek, OS güncellemek, güvenlik patch'lemek — HİÇBİR ŞEY yapmazsınız. Sadece Task Definition'da CPU/memory söylersiniz, Fargate çalıştırır.

⚠️ Fargate'in bedeli var: **aynı workload için EC2'den ~%20-40 pahalı.** Ama operasyonel yükü düşürdüğünde, DevOps mühendisinin saatlik maliyetini düşünürsünüz ve çoğu zaman Fargate daha ucuza gelir. "EC2 yönetmek için bir DevOps mühendisi işe almak" mı daha pahalı, yoksa Fargate fazlası mı? 🤔

**EKS (Elastic Kubernetes Service) — Kubernetes, AWS Usulü:**

EKS, Kubernetes'i AWS'de managed olarak çalıştırmanızı sağlar. Control plane (API Server, etcd, scheduler) AWS tarafından yönetilir — siz sadece worker node'larınızla ilgilenirsiniz. Kubernetes'in TÜM gücü (HPA, VPA, CRD'ler, Helm, service mesh, GitOps) + AWS entegrasyonu (ALB Ingress Controller, EBS CSI Driver, IAM for Service Accounts).

**ECS vs EKS — Hangisini Seçmeli?**

| Kriter | ECS | EKS |
|--------|-----|-----|
| **Karmaşıklık** | Basit — 1 gün, öğrenilir | Karmaşık — haftalarca öğrenilir |
| **AWS Lock-in** | EVET — tamamen AWS'ye bağlı | HAYIR — yarın GCP'ye taşıyabilirsiniz |
| **Ekosistem** | AWS servisleriyle sıkı entegrasyon | Kubernetes ekosistemi (Helm, Istio, ArgoCD, Prometheus...) |
| **Maliyet** | ECS bedava (sadece compute öde) | EKS control plane: $0.10/saat (~$72/ay) + compute |
| **Esneklik** | Sınırlı — AWS'nin sunduğu kadar | Sınırsız — CRD yazarsın, operator geliştirirsin |
| **DevOps Olgunluk** | Küçük/orta takımlar | Büyük/olgun DevOps takımları |

**Task Definitions — Kubernetes Pod Spec'inin ECS Hali:**

ECS'te her container grubu bir **Task Definition** ile tanımlanır. Bu, Kubernetes'teki Pod spec'e benzer ama AWS-flavored: IAM role'leri direkt atanır, CloudWatch log driver built-in, secret'lar AWS Secrets Manager'dan çekilir.

**Gerçek Dünya:** AWS-heavy şirketlerin çoğu ECS ile başlar — basit, hızlı, çalışır. Şirket büyüdükçe, multi-cloud ihtiyacı doğdukça, Kubernetes bilgisi olan mühendisler ekibe katıldıkça EKS'e geçiş yapılır. Getir gibi yüksek ölçekli şirketler EKS kullanır — çünkü Kubernetes'in auto-scaling, self-healing, canary deployment gibi gelişmiş özellikleri bu ölçekte ZORUNLU. Küçük bir startup mı? ECS + Fargate ile başla, mutlu ol, büyüyünce düşünürsün. 🚀

```yaml
# ECS Task Definition örneği
{
  "family": "my-app",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::123456789:role/ecsTaskExecutionRole",
  "containerDefinitions": [{
    "name": "web",
    "image": "nginx:latest",
    "cpu": 256,
    "memory": 512,
    "portMappings": [{
      "containerPort": 80,
      "protocol": "tcp"
    }],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/my-app",
        "awslogs-region": "eu-west-1",
        "awslogs-stream-prefix": "web"
      }
    },
    "healthCheck": {
      "command": ["CMD-SHELL", "curl -f http://localhost/health || exit 1"],
      "interval": 30,
      "timeout": 5,
      "retries": 3
    }
  }]
}
```

### AWS Storage Services

#### S3 (Simple Storage Service)

**S3 Nedir? — Sonsuz Hard Disk**

S3'ü **buluttaki sonsuz hard disk** olarak düşünün. Gerçekten sonsuz — Amazon'un resmi ifadesiyle "virtually unlimited storage". Birine "benim hard diskim doldu" dediğinizi düşünün. S3'te böyle bir cümle kuramazsınız. Ne kadar dosya yüklerseniz yükleyin, asla dolmaz. Netflix TÜM içeriğini S3'te saklar. Spotify müzik dosyalarını S3'te tutar. Airbnb'nin milyonlarca ev fotoğrafı S3'tedir. Dayanıklılığı 99.999999999% (11 nines) — yani 10 milyon dosya saklasanız, 10.000 YIL boyunca en fazla 1 dosya kaybedersiniz. Paranoyak düzeyde güvenilir.

**🔑 Önemli Kavram — Key, Directory Değil:**

S3'ün en çok yanlış anlaşılan özelliği: S3 FLAT bir yapıdadır, **klasör diye bir şey YOKTUR!** AWS konsolunda `images/profile/avatar.jpg` gördüğünüzde bir klasör hiyerarşisi gibi görünür ama aslında bu sadece bir **key** (anahtar). `/` karakterleri sadece görsel bir illüzyon yaratır. Bu neden önemli? Çünkü S3'te "klasör silme" veya "klasör taşıma" gibi atomik operasyonlar yoktur — her dosya bağımsızdır. 10.000 dosyalık bir "klasörü" taşımak = 10.000 ayrı copy + delete operasyonu demek.

**Storage Classes — Sıcak, Ilık, Soğuk Depolama:**

Düşünün: mutfaktaki buzdolabı (sık erişim), bodrumdaki dolap (ara sıra), şehir dışındaki depo (yılda bir).

| Class | Analoji | Maliyet | Erişim Süresi | Kullanım |
|-------|---------|---------|---------------|----------|
| **S3 Standard** | Buzdolabı — her an eli altında | $$$ | Milisaniye | Aktif dosyalar, API response'ları |
| **S3 IA (Infrequent Access)** | Bodrumdaki dolap | $$ | Milisaniye (ama retrieval ücreti var) | Aylık raporlar, eski loglar |
| **S3 Glacier Instant Retrieval** | Şehir dışı depo (hızlı kurye ile) | $ | Milisaniye | Compliance data, medikal kayıtlar |
| **S3 Glacier Deep Archive** | Arşiv kasası — anahtarı bulmak bile zaman alır | ¢ | 12-48 SAAT! | Yasal zorunluluk arşivleri |
| **S3 Intelligent-Tiering** | Akıllı ev sistemi — otomatik optimize eder | Değişken | Otomatik | Erişim paterni bilinmiyorsa |

**Pre-signed URLs — Geçici Giriş Kartı:**

S3 bucket'ınız private (ve öyle olmalı!). Ama bazen bir kullanıcıya geçici erişim vermeniz gerekir. Pre-signed URL tam bunu yapar: "Bu URL ile 15 dakika boyunca şu dosyayı indirebilirsin" dersiniz. Süre dolunca link ölür. Otel odası kartı gibi — check-out saatinde deaktive olur.

```javascript
// Pre-signed URL örneği
const url = s3.getSignedUrl('getObject', {
  Bucket: 'my-private-bucket',
  Key: 'secret-report.pdf',
  Expires: 900 // 15 dakika
});
// url: https://my-bucket.s3.amazonaws.com/secret-report.pdf?X-Amz-Signature=...
```

**Lifecycle Policies — Otomatik Temizlik:**

Dosyalarınızı hayat döngüsüne göre otomatik yönetin. Kuralı bir kez yazarsınız, AWS sonsuza dek uygular:
- 30 gün sonra → Standard'dan IA'ya taşı (maliyet %40 düşer)
- 90 gün sonra → Glacier'a taşı (maliyet %80 düşer)
- 365 gün sonra → Deep Archive'a taşı (maliyet %95 düşer)
- 730 gün sonra → Sil

Bu kurallar olmadan ne olur? Log dosyaları birikir, birikir, birikir... Ay sonunda AWS faturası gelir ve CFO'nuz sizi arar: "Neden S3'e $15.000 ödüyoruz?!" 🫠

**Kullanım Alanları:**
- Static assets (images, videos, files)
- Backup & archiving
- Data lake (big data analytics)
- Static website hosting

**Best Practices:**
- Lifecycle policies (eski file'ları Glacier'a taşı)
- Versioning (accidental delete prevention)
- Encryption (at rest & in transit)
- Cross-region replication
- Bucket policy'lerinde `s3:*` KULLANMAYIN — principle of least privilege!

#### EBS (Elastic Block Store)
- EC2 için disk storage
- SSD vs HDD options
- Snapshot'lar ile backup

#### EFS (Elastic File System)
- Network file system
- Multiple EC2 instances arasında shared storage

### Networking

#### VPC (Virtual Private Cloud)

**VPC Nedir? — Buluttaki Özel Mahalleniz**

VPC'yi şöyle düşünün: AWS, devasa bir şehir. Bu şehirde siz **kendi özel mahallenizi** kuruyorsunuz — kendi sokaklarınız, kapılarınız, güvenlik görevlileriniz var. Komşu mahalleler (diğer AWS müşterileri) sizin mahallenize giremez. Siz de onlarınkine giremezsiniz. Her şey izole. Kendi IP range'inizi tanımlarsınız (örneğin 10.0.0.0/16 — bu size 65.536 IP adresi verir) ve bu adres aralığında dilediğiniz gibi yapılanırsınız.

**Subnets — Ön Bahçe vs Arka Bahçe:**

Mahallenizin içinde farklı bölgeler var:

- **Public Subnet (Ön Bahçe):** Sokağa bakan, herkesin görebildiği alan. Load balancer'lar, bastion host'lar buraya konur. Internet Gateway üzerinden dış dünyayla konuşabilir.
- **Private Subnet (Arka Bahçe):** Duvarların arkası, dışarıdan görünmez. Veritabanları, uygulama sunucuları, cache'ler buraya konur. Dışarıdan doğrudan erişilemez — güvenli!

Neden bu ayrım? Çünkü veritabanınızın internet üzerinden erişilebilir olmasını ASLA istemezsiniz. Bir hacker port taraması yaptığında, private subnet'teki RDS instance'ınızı göremez bile.

**Route Tables — Trafik Yönlendirme Levhaları:**

Her subnet'in bir route table'ı var — yani "bu adrese gitmek istiyorsan şu yoldan git" tabelaları. Public subnet'in route table'ında "0.0.0.0/0 → Internet Gateway" yazar (tüm dış trafik internet'e git). Private subnet'te bu kural YOKTUR — dış dünyaya çıkış yolu kapalı.

**NAT Gateway — Tek Yönlü Ayna:**

Peki private subnet'teki uygulama dışarıya nasıl istek atar? NPM paketleri indirmek, API çağrısı yapmak gerekebilir. İşte NAT Gateway! Bunu **tek yönlü ayna** gibi düşünün: içeriden dışarıyı görebilirsiniz (outbound trafik OK), ama dışarıdan içeriyi göremezsiniz (inbound trafik engelli). Private instance → NAT Gateway → Internet Gateway → Dış dünya. Dış dünya ise NAT Gateway'in arkasını göremez.

⚠️ NAT Gateway PAHALIDIR — saat başı $0.045 + data transfer ücreti. Dev ortamlarında gereksiz NAT Gateway açık bırakmak, aylık $100+ israftır.

**Security Groups vs NACLs — İki Katmanlı Güvenlik:**

| Özellik | Security Group | NACL |
|---------|---------------|------|
| Seviye | Instance (pod/makine) | Subnet (tüm ağ bloğu) |
| Analoji | Apartman kapısının güvenlik görevlisi | Mahalle girişindeki bariyer |
| Stateful/Stateless | **Stateful** — giriş izni verdiyseniz, çıkış otomatik serbest | **Stateless** — giriş ve çıkış kuralları AYRI tanımlanmalı |
| Default | Tüm inbound ENGEL, tüm outbound SERBEST | Tüm trafik SERBEST |
| Kural tipi | Sadece ALLOW kuralları | ALLOW ve DENY kuralları |

Gerçek hayatta genelde Security Group yeterlidir. NACL'ı ek savunma katmanı olarak veya belirli IP'leri subnet seviyesinde engellemek için kullanırsınız.

**Nedir:**
- AWS içinde izole edilmiş network ortamınız
- Kendi IP range'inizi tanımlarsınız (10.0.0.0/16)

**Örnek Senaryo:**
```
VPC (10.0.0.0/16)
├── Public Subnet (10.0.1.0/24)
│   ├── Load Balancer
│   └── Bastion Host
├── Private Subnet (10.0.2.0/24)
│   ├── Application Servers (EC2/ECS)
│   └── Lambda (VPC içinde)
└── Private Subnet (10.0.3.0/24)
    └── Database (RDS)
```

#### Load Balancers

Load Balancer'ı bir **trafik polisi** gibi düşünün. 🚦 Bir kavşakta binlerce araç geliyor (kullanıcı istekleri). Trafik polisi olmasa ne olur? Herkes aynı yoldan gitmeye çalışır, trafik tıkanır, kimse bir yere varamaz. Trafik polisi araçları farklı yollara (sunuculara) yönlendirir — yük eşit dağılır, trafik akar, herkes mutlu.

Load Balancer olmadan, TÜM trafik tek sunucuya gider. O sunucu çökünce? Sıfır erişim. Load balancer ile 5 sunucunuz var, biri çökse 4'ü devam eder. Kullanıcı farkını bile anlamaz. Bu kadar basit, bu kadar kritik.

**ALB vs NLB vs CLB — Üç Nesil, Üç Farklı Güç:**

| Özellik | ALB (Application) | NLB (Network) | CLB (Classic) |
|---------|-------------------|---------------|---------------|
| **Katman** | Layer 7 (HTTP/HTTPS) | Layer 4 (TCP/UDP) | Layer 4 + 7 (eski) |
| **Analoji** | Akıllı resepsiyon — "sipariş mi, iade mi?" diye sorar, doğru departmana yönlendirir | Otomatik kapı — kim gelirse gelsin, en boş odaya yönlendirir | Eski model güvenlik görevlisi — emekli olması lazım |
| **Routing** | Path-based (`/api` → Service A, `/web` → Service B), Host-based (`api.getir.com` vs `web.getir.com`), HTTP header/query string | Port-based, IP-based | Basit round-robin |
| **Performans** | İyi (~100K req/s) | MÜTHIŞ (~milyon req/s, ultra-low latency) | Orta |
| **WebSocket** | ✅ Tam destek | ✅ (TCP seviyesinde) | ❌ |
| **gRPC** | ✅ HTTP/2 desteği | ✅ | ❌ |
| **Static IP** | ❌ (DNS name alırsınız) | ✅ (Elastic IP atanabilir) | ❌ |
| **Kullanım** | Web API'lar, mikroservisler | Oyun server'ları, IoT, finansal sistemler | **YENİ PROJEDE KULLANMAYIN** |

**ALB Detay — Layer 7 Zekası:**

ALB, HTTP header'larını, path'leri, query string'leri OKUYARAK karar verir. Bu güç inanılmaz esneklik sağlar:
- `/api/v1/*` → API Service cluster
- `/api/v2/*` → Yeni API Service (canary deployment!)
- `Accept: application/grpc` → gRPC backend
- `Host: admin.example.com` → Admin panel

Kubernetes'te **ALB Ingress Controller** ile ALB'yi otomatik Kubernetes Ingress olarak kullanabilirsiniz. Annotation'larla path routing, SSL, WAF entegrasyonu yaparsınız.

**NLB Detay — Hız Canavarı:**

NLB, paketlerin İÇİNE BAKMAZ — sadece IP ve port'a göre yönlendirir. Bu yüzden inanılmaz hızlı. TCP/UDP trafiği için idealdir: gRPC (HTTP/2 üzerinden), WebSocket bağlantıları, veritabanı proxy'leri, oyun server'ları. Elastic IP atanabilir — firewall'larda whitelist yapmanız gerektiğinde hayat kurtarır.

**CLB — Veda Zamanı:** 👋

Classic Load Balancer, AWS'nin ilk nesil load balancer'ıdır. Hâlâ çalışır ama yeni özellik GELMİYOR. Legacy projeler dışında kullanmak için hiçbir neden yok. AWS bile "lütfen ALB/NLB'ye geçin" diyor.

**Health Checks — Sağlık Kontrolü:**

Load balancer, backend sunucularınıza düzenli olarak "hayatta mısın?" diye sorar (genelde `/health` endpoint'ine HTTP GET). Cevap gelmezse veya 5xx dönerse, o sunucuyu **unhealthy** işaretler ve TRAFİK GÖNDERMEYİ DURDURUR. Sunucu düzeldiğinde otomatik tekrar devreye alınır.

```yaml
# ALB Health Check ayarları
HealthCheckPath: /health
HealthCheckIntervalSeconds: 30      # Her 30 saniyede bir kontrol
HealthyThresholdCount: 2            # 2 başarılı = sağlıklı
UnhealthyThresholdCount: 3          # 3 başarısız = sağlıksız
HealthCheckTimeoutSeconds: 5         # 5 saniye içinde cevap gelmezse başarısız
```

⚠️ **Yaygın Hata:** Health check path'ini `/` yapmak. Ana sayfa heavy rendering yapıyorsa, health check yavaş döner, LB sunucuyu sağlıksız sanır ve devreden çıkarır. `/health` endpoint'i HIZLI, HAFİF ve BAĞIMSIZ olmalı — sadece `{ status: "ok" }` dönmeli.

**Sticky Sessions — "Beni Hep Aynı Garson Karşılasın":**

Normalde load balancer her isteği farklı sunucuya yönlendirebilir. Ama bazı durumlarda (session-based auth, shopping cart, WebSocket) aynı kullanıcının hep AYNI sunucuya gitmesi gerekir. ALB bunu cookie ile yapar: ilk istekte `AWSALB` cookie'si set eder, sonraki isteklerde bu cookie'ye bakarak aynı target'a yönlendirir.

🚫 **Ama dikkat:** Sticky sessions, scaling'i zorlaştırır! Bir sunucu çökerse, o sunucuya sticky olan TÜM kullanıcıların session'ı kaybolur. Mümkünse uygulamanızı **stateless** yapın (session'ı Redis'te tutun) ve sticky session'a ihtiyaç duymayın.

**Cross-Zone Load Balancing — AZ'ler Arası Denge:**

AWS'de sunucularınız farklı Availability Zone'larda (AZ) dağılır (örn: us-east-1a'da 3, us-east-1b'de 7 sunucu). Cross-zone LB kapalıysa, her AZ'ye eşit trafik gider: 1a'ya %50 (3 sunucuya), 1b'ye %50 (7 sunucuya). Sonuç: 1a'daki sunucular EZILIR, 1b'dekiler rahat rahat çalışır.

Cross-zone açıkken, LB TÜM sunucuları TEK bir havuz olarak görür ve 10 sunucuya eşit dağıtır. ALB'de default AÇIK, NLB'de default KAPALI (AZ bazında ücretlendirme var). Production'da cross-zone'u MUTLAKA açın.

**Best Practice:**
```
Users -> Route 53 (DNS) -> ALB -> Target Groups -> EC2/ECS/Lambda
                                      ↓
                               Health checks (her 30s)
                               Connection draining (deregistration delay: 300s)
                               Sticky sessions (gerekiyorsa, ama stateless tercih edin)
                               SSL termination (HTTPS ALB'de biter, backend HTTP kalır)
                               WAF integration (SQL injection, XSS koruması)
                               Cross-zone load balancing (AZ'ler arası eşit dağılım)
```

---

## 🐳 Kubernetes & Container Orchestration

### Kubernetes Nedir?

**Tanım:**
- Container orchestration platform (Google tarafından geliştirildi)
- Container'ları manage etme, scaling, deployment
- Industry standard (cloud-agnostic)
- Declarative configuration

**ECS vs Kubernetes:**
```
ECS:
✓ AWS native, kolay entegrasyon
✓ Basit setup
✓ AWS ecosystem içinde optimize
✗ Vendor lock-in
✗ Limitli features

Kubernetes:
✓ Cloud-agnostic (taşınabilir)
✓ Huge ecosystem & community
✓ Advanced features (self-healing, auto-scaling)
✓ Industry standard skills
✗ Karmaşık
✗ Steep learning curve
```

### Kubernetes Architecture

```
┌─────────────────────────────────────────────────────┐
│                  CONTROL PLANE                       │
│  ┌──────────┐  ┌──────────┐  ┌────────────────┐   │
│  │ API      │  │ Scheduler│  │ Controller     │   │
│  │ Server   │  │          │  │ Manager        │   │
│  └──────────┘  └──────────┘  └────────────────┘   │
│  ┌──────────────────────────────────────────────┐  │
│  │            etcd (Key-Value Store)            │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
   │ NODE 1  │     │ NODE 2  │     │ NODE 3  │
   ├─────────┤     ├─────────┤     ├─────────┤
   │ Kubelet │     │ Kubelet │     │ Kubelet │
   │ Kube    │     │ Kube    │     │ Kube    │
   │ Proxy   │     │ Proxy   │     │ Proxy   │
   ├─────────┤     ├─────────┤     ├─────────┤
   │ Pods    │     │ Pods    │     │ Pods    │
   └─────────┘     └─────────┘     └─────────┘
```

**Components:**
```
Control Plane:
- API Server: K8s ile iletişim (kubectl commands)
- Scheduler: Pod'ları node'lara assign eder
- Controller Manager: State'i manage eder
- etcd: Cluster data store

Worker Nodes:
- Kubelet: Node agent, pod lifecycle
- Kube-proxy: Network routing
- Container Runtime: Docker, containerd
```

### Kubernetes Core Concepts

Kubernetes kavramlarını anlamadan YAML yazmak, şehir haritası olmadan taksi sürmek gibidir — bir yere varırsın ama neresi olduğunu bilemezsin. 😄

Her kavramı "neden var?" sorusuyla öğrenelim.

#### 1. Pod

**Hikaye:** Docker container'ını düşün. Tek başına çalışıyor, güzel. Ama ya bu container'ın yanında bir de log toplayıcı container çalışması gerekiyorsa? Ya da bir sidecar proxy? İşte Pod, "birlikte yaşaması gereken container'ları" tek bir birim olarak yönetmek için var.

**Pod = Kubernetes'in en küçük deploy birimi.** Tek bir container olabilir (en yaygın), veya birden fazla container aynı pod'da çalışabilir (sidecar pattern).

**Kritik bilgi:** Pod'lar EPHEMERAL'dir (geçici). Öldüğünde aynı Pod geri GELMEZ — yeni bir Pod OLUŞTURULUR. Bu yüzden Pod'a doğrudan hiçbir zaman bağlanma, her zaman bir Service üzerinden git!

**Gerçek dünya:** Getir'de bir sipariş servisinin pod'u ölürse, Kubernetes otomatik olarak yenisini başlatır. Müşteri hiçbir şey fark etmez. Ama eğer pod'a doğrudan IP ile bağlansaydın — 💥 "Siparişim nerede?!" 😱

**En küçük deployment unit:**

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
  labels:
    app: web
    tier: frontend
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
    env:
    - name: ENVIRONMENT
      value: "production"
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    livenessProbe:
      httpGet:
        path: /health
        port: 80
      initialDelaySeconds: 3
      periodSeconds: 3
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
```

#### 2. Deployment

**Hikaye:** Pod tek başına bir işçi gibidir. Ama sen "3 işçi çalışsın, biri ölürse yerine yenisi gelsin, güncelleme olduğunda sırayla değişsinler" demek istersin. İşte **Deployment** tam bunu yapar.

**Deployment** = "Ben 3 tane pod istiyorum, şu image'ı kullanarak, ve güncelleme geldiğinde rolling update yap" demenin YAML hali.

**Neden önemli?**
- **Declarative (Bildirimsel):** "3 replica istiyorum" dersin, Kubernetes bunu sağlar. Bir pod ölürse yenisini başlatır (self-healing).
- **Rolling Update:** Yeni versiyon deploy ederken eski pod'ları TEK TEK kapatır, yenisini açar. Kesinti SIFIR!
- **Rollback:** Yeni versiyon patlarsa → `kubectl rollout undo` → eski versiyona 10 saniyede GERİ DÖN!

**Gerçek dünya hikayesi:** 2017'de GitLab, yanlış bir production deployment yaptı ve veritabanının bir kısmını sildi. Kubernetes rollback özelliği olsaydı (o zamanlar farklı bir altyapı kullanıyorlardı), 1 komutla geri dönebilirlerdi. Bu olay, tüm endüstrinin declarative deployment'a geçişini hızlandırdı.

**Declarative updates for Pods:**

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:v1.0
        ports:
        - containerPort: 8080
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
```

**Commands:**
```bash
# Apply deployment
kubectl apply -f deployment.yaml

# Get deployments
kubectl get deployments

# Scale deployment
kubectl scale deployment web-deployment --replicas=5

# Update image (rolling update)
kubectl set image deployment/web-deployment web=myapp:v2.0

# Rollback
kubectl rollout undo deployment/web-deployment

# Check rollout status
kubectl rollout status deployment/web-deployment

# View rollout history
kubectl rollout history deployment/web-deployment
```

#### 3. Service

**Sorunu düşün:** Pod'ların IP adresleri her ölüp yeniden doğduğunda DEĞİŞİR. Eğer "sipariş servisi" pod'una IP ile bağlanırsan, pod yeniden başladığında bağlantın KOPAR. 💀

**Service = Kubernetes'in DNS + Load Balancer'ı.** Bir Service oluşturduğunda, Kubernetes ona SABİT bir DNS adı verir (mesela `web-service.default.svc.cluster.local`). Arkadaki pod'lar ölse bile, yenileri aynı Service üzerinden erişilebilir.

**Analoji:** Service = bir şirketin GENEL TELEFON NUMARASI. Çalışanlar (pod'lar) işten ayrılsa, yenileri gelse, sen hep aynı numara ile arayabilirsin. Santral (Service) doğru kişiye yönlendirir.

**Network abstraction for Pods:**

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: LoadBalancer  # ClusterIP, NodePort, LoadBalancer
  selector:
    app: web
  ports:
  - protocol: TCP
    port: 80         # Service port
    targetPort: 8080 # Container port
```

**Service Types:**
```
ClusterIP (default):
- Internal cluster IP
- Sadece cluster içinden erişilebilir
- Use: Microservices arası iletişim

NodePort:
- Node IP:Port üzerinden erişim
- 30000-32767 port range
- Use: Development, testing

LoadBalancer:
- External load balancer (cloud provider)
- Public IP address
- Use: Production web services

ExternalName:
- DNS CNAME record
- External service mapping
```

#### 4. ConfigMap & Secret

Kubernetes dünyasında uygulamanızın çalışması için gereken konfigürasyonları ve hassas bilgileri yönetmek, sanıldığından çok daha kritik bir konudur. İşte burada **ConfigMap** ve **Secret** devreye girer.

**Basit Bir Analoji: Bülten Tahtası vs. Kilitli Kasa**

ConfigMap'i ofisteki **herkese açık bülten tahtası** olarak düşünün. Üzerine "Toplantı saat 15:00'te", "WiFi şifresi: misafir123" (evet, bazıları bunu da yapıyor 😅), "Log seviyesi: INFO" gibi bilgiler asarsınız. Herkes görebilir, herkes okuyabilir — ve bu gayet normaldir çünkü bu bilgiler hassas değildir.

Secret ise ofisteki **kilitli kasa** gibidir. İçinde banka hesap bilgileri, API key'leri, veritabanı şifreleri gibi "yanlış ellere geçerse felaket olur" türünden bilgiler saklanır. Kasanın anahtarı sadece yetkili kişilerde bulunur.

**12-Factor App Prensibi #3: "Store Config in the Environment"**

[12-Factor App](https://12factor.net/config) metodolojisinin üçüncü prensibi açıkça der ki: **"Konfigürasyonu environment'ta sakla."** Yani veritabanı URL'ini, API endpoint'lerini, log seviyesini kod içine gömmek yerine environment variable olarak dışarıdan inject etmelisiniz.

Neden mi? Çünkü aynı uygulama image'ı `dev`, `staging` ve `production` ortamlarında farklı konfigürasyonlarla çalışmalıdır. Kodu değiştirmeden, sadece konfigürasyonu değiştirerek farklı ortamlara deploy edebilmelisiniz. ConfigMap ve Secret, Kubernetes'in bu prensibi native olarak destekleme yöntemidir.

```
Kod içinde:  DATABASE_URL = "postgres://prod-db:5432/mydb"  ← YANLIŞ ❌
Environment: DATABASE_URL env var → ConfigMap'ten gelir          ← DOĞRU ✅
```

**ConfigMap vs. Secret: Fark Ne? (Spoiler: base64 ≠ Şifreleme!)**

Bu noktada çok kritik bir yanlış anlaşılmayı düzeltelim. Birçok geliştirici Secret'ların "şifreli" (encrypted) olduğunu sanır. **HAYIR!** Kubernetes Secret'ları varsayılan olarak sadece **base64 encode** edilmiştir. base64, bir encoding formatıdır, şifreleme DEĞİLDİR. Herhangi biri `echo "cGFzc3dvcmQxMjM=" | base64 -d` komutunu çalıştırarak Secret'ınızı anında okuyabilir.

```bash
# "Şifreli" sanılan Secret'ı çözmek tam 1 saniye sürer:
$ echo "cGFzc3dvcmQxMjM=" | base64 -d
password123
# Vay canına, ne kadar "güvenli" 🙃
```

O zaman Secret'ın ConfigMap'ten farkı ne?

| Özellik | ConfigMap | Secret |
|---------|-----------|--------|
| **Amaç** | Hassas olmayan konfigürasyon | Hassas bilgiler (şifreler, key'ler) |
| **Encoding** | Plain text | base64 encoded (şifreleme DEĞİL!) |
| **RBAC** | Standart erişim kontrolü | Daha kısıtlı RBAC politikaları uygulanabilir |
| **etcd'de saklama** | Plain text | Encryption at rest etkinleştirilebilir |
| **Boyut limiti** | 1 MB | 1 MB |
| **tmpfs** | Hayır | Secret volume'lar tmpfs kullanır (diske yazılmaz) |
| **kubectl get** | Değerler açıkça görünür | Değerler gizlenir (`kubectl get secret -o yaml` ile görünür) |
| **Audit logging** | Standart | Secret erişimleri ayrıca loglanabilir |

Yani Secret'ın asıl avantajı şifreleme değil, **erişim kontrolü ve audit** katmanıdır. Kubernetes RBAC ile "şu kullanıcı Secret'lara erişemesin ama ConfigMap'leri okuyabilsin" diyebilirsiniz. Ayrıca `EncryptionConfiguration` ile etcd'deki Secret'ları gerçekten şifreleyebilirsiniz.

**Ne Zaman HashiCorp Vault (veya Benzeri) Kullanmalı?**

Kubernetes Secret'ları basit senaryolar için yeterli olsa da, production ortamlarında genellikle yetersiz kalır. Şu durumlarda **HashiCorp Vault**, **AWS Secrets Manager** veya **Azure Key Vault** gibi çözümlere geçmelisiniz:

- 🔐 **Otomatik secret rotation** gerektiğinde (her 30 günde bir DB şifresi değişmeli)
- 🔐 **Dynamic secrets** gerektiğinde (her pod'a geçici, unique bir DB credential üretmek)
- 🔐 **Audit trail** kritik olduğunda (kim, ne zaman, hangi secret'a erişti?)
- 🔐 **Cross-cluster** secret paylaşımı gerektiğinde
- 🔐 **Encryption as a service** gerektiğinde (Transit secrets engine)
- 🔐 **Compliance** gereksinimleri olduğunda (PCI-DSS, HIPAA, SOC2)

Vault'u Kubernetes ile entegre etmek için genellikle **Vault Agent Sidecar Injector** veya **External Secrets Operator** kullanılır. External Secrets Operator, Vault'taki secret'ları otomatik olarak Kubernetes Secret'larına senkronize eder.

**ConfigMap Mounting Stratejileri: Env Var vs. Volume Mount**

ConfigMap verilerini Pod'a iki şekilde aktarabilirsiniz ve her birinin kendine özgü avantajları vardır:

**1. Environment Variable olarak mount etmek:**
```
env:
- name: LOG_LEVEL
  valueFrom:
    configMapKeyRef:
      name: app-config
      key: LOG_LEVEL
```
- ✅ Basit key-value çiftleri için ideal
- ✅ Uygulama kodunda `process.env.LOG_LEVEL` ile kolay erişim
- ❌ Pod restart olmadan güncellenemez!
- ❌ Büyük konfigürasyon dosyaları için uygun değil

**2. Volume olarak mount etmek:**
```
volumeMounts:
- name: config
  mountPath: /etc/config
volumes:
- name: config
  configMap:
    name: app-config
```
- ✅ Büyük konfigürasyon dosyaları için ideal (JSON, YAML, properties)
- ✅ **Hot-reload destekler!** ConfigMap güncellendiğinde dosya otomatik güncellenir
- ❌ Uygulamanın dosya okuma mantığı olması gerekir
- ❌ Biraz daha karmaşık setup

**🔥 Hot-Reload: En Çok Karıştırılan Konu**

Bu çok kritik bir fark ve production'da sorunlara neden olabilir:

- **Volume mount** ile bağlanan ConfigMap'ler, ConfigMap güncellendiğinde **otomatik olarak güncellenir** (kubelet sync period'una bağlı, genellikle 60 saniye içinde). Uygulamanız dosyayı tekrar okuduğunda yeni değerleri görür.
- **Environment variable** olarak inject edilen ConfigMap değerleri ise **POD RESTART OLMADAN ASLA GÜNCELLENMEZİ!** Pod oluşturulduğu anda env var'lar set edilir ve artık sabittir.

Bu yüzden sık değişen konfigürasyonları (feature flag'ler, timeout değerleri) volume mount olarak bağlamak çok daha mantıklıdır. Ancak uygulamanızın da bu dosya değişikliklerini watch edecek bir mekanizmaya sahip olması gerekir (örneğin Node.js'te `fs.watch()` veya Spring Boot'ta `@RefreshScope`).

**😱 Gerçek Dünya Hikayesi: "Git'e Commit'lenen DB Şifresi"**

Bir geliştirici düşünün — diyelim adı Ahmet. Ahmet, yeni bir microservice geliştiriyor ve local'de test etmek için `.env` dosyasına production DB şifresini yazıyor:

```
DB_HOST=prod-db.company.internal
DB_PASSWORD=SuperGizliSifre2024!
DB_PORT=5432
```

Ahmet commit atıyor, push yapıyor... ve `.gitignore`'a `.env` eklemeyi unutuyor. 💀

Sonuç? Production veritabanı şifresi artık git history'de sonsuza kadar yaşıyor. `git filter-branch` ile temizlemeye çalışsanız bile, birisi fork yapmışsa veya CI/CD cache'inde kalmışsa, o şifre artık "açık"tır.

**Bu senaryodan çıkarılacak dersler:**
1. **Hassas bilgileri ASLA kod reposuna koymayın** — ConfigMap/Secret veya Vault kullanın
2. **git-secrets** veya **trufflehog** gibi araçlarla pre-commit hook'ları kurun
3. Eğer bir secret sızdıysa, temizlemek yerine **hemen rotate edin** (şifreyi değiştirin)
4. **SOPS (Secrets OPerationS)** ile encrypted secrets'ı git'te güvenle saklayabilirsiniz

**⚠️ Sık Yapılan Hatalar**

1. **Secret'ları ConfigMap'e koymak:** "Nasılsa cluster içinde, kim görecek ki?" demeyin. RBAC ile ConfigMap'lere erişim genellikle daha açıktır. Hassas bilgiyi her zaman Secret'ta tutun.

2. **Secret'ları rotate etmemek:** Bir secret oluşturup yıllarca aynı şifreyi kullanmak, evinizin kapı kilidini 10 yıl boyunca değiştirmemek gibidir. Düzenli rotation politikası şart!

3. **base64'ü şifreleme sanmak:** Yukarıda anlattık ama tekrar vurgulayalım — `base64` bir şifreleme yöntemi DEĞİLDİR. Production'da mutlaka `EncryptionConfiguration` ile etcd encryption'ı etkinleştirin.

4. **ConfigMap/Secret boyut limitini aşmak:** Her ikisi de maksimum **1 MB** boyutundadır. Büyük konfigürasyon dosyaları için farklı stratejiler düşünün.

5. **immutable ConfigMap/Secret kullanmamak:** Kubernetes 1.21+ ile `immutable: true` ayarı yapabilirsiniz. Bu hem performansı artırır (kubelet watch yapmaz) hem de yanlışlıkla değiştirilmeyi engeller.

6. **Tüm env var'ları tek bir ConfigMap'e tıkmak:** Microservice'lerin farklı konfigürasyon ihtiyaçları olabilir. İlgisiz konfigürasyonları ayrı ConfigMap'lere bölün.

**📋 Best Practice Tablosu**

| Best Practice | Açıklama | Öncelik |
|---------------|----------|---------|
| **Secret'ları ayrı tutun** | Hassas bilgileri ConfigMap'e değil, Secret'a koyun | 🔴 Kritik |
| **etcd encryption** | `EncryptionConfiguration` ile Secret'ları etcd'de şifreleyin | 🔴 Kritik |
| **RBAC kısıtlamaları** | Secret'lara erişimi minimum düzeyde tutun (least privilege) | 🔴 Kritik |
| **Secret rotation** | Düzenli aralıklarla secret'ları rotate edin | 🟡 Yüksek |
| **External secret management** | Production'da Vault/AWS Secrets Manager kullanın | 🟡 Yüksek |
| **git-secrets / pre-commit** | Repo'ya secret push'ını engelleyin | 🟡 Yüksek |
| **immutable ConfigMap/Secret** | Değişmeyecek konfigürasyonlar için `immutable: true` kullanın | 🟢 Orta |
| **Volume mount for hot-reload** | Sık değişen config'leri volume olarak mount edin | 🟢 Orta |
| **ConfigMap'leri bölün** | Her microservice için ayrı ConfigMap oluşturun | 🟢 Orta |
| **Sealed Secrets / SOPS** | GitOps workflow'larında encrypted secrets için kullanın | 🟢 Orta |

Şimdi tüm bu kavramları YAML örnekleriyle görelim:

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_URL: "postgres://db:5432/mydb"
  LOG_LEVEL: "info"
  config.json: |
    {
      "timeout": 30,
      "retries": 3
    }

---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  DB_PASSWORD: cGFzc3dvcmQxMjM=  # base64 encoded
  API_KEY: YWJjZGVmZ2hpams=

---
# Using in Pod
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    # From ConfigMap
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DATABASE_URL
    # From Secret
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: DB_PASSWORD
    # Mount as volume
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config
```

#### 5. Ingress

Ingress, Kubernetes cluster'ınızın **resepsiyonisti**dir. Düşünün ki cluster'ınız kocaman bir iş merkezi ve içinde onlarca şirket (microservice) var. Her şirketin kendi ofisi, kendi kapısı var. Ama dışarıdan gelen bir müşteri (HTTP isteği) kapıdan girdiğinde, hangi kata, hangi ofise gideceğini bilemez. İşte Ingress tam burada devreye girer — lobideki o güler yüzlü resepsiyonist gibi, gelen isteğe "Siz `/users` mı istiyorsunuz? 3. kat, user-service ofisi. `/orders` mı? 5. kat, order-service" diye yol gösterir.

**Ingress Olmadan Hayat: Her Servise Ayrı LoadBalancer 💸**

Ingress olmadan her microservice'e dışarıdan erişim sağlamak istediğinizde, her birine ayrı bir `LoadBalancer` tipi Service oluşturmanız gerekir. Cloud provider'da her LoadBalancer'ın bir maliyeti var — AWS'de her ALB/NLB aylık ~$20-25 + data transfer ücretleri. 50 microservice'iniz varsa, sadece LoadBalancer'lar için ayda **$1000+** ödüyorsunuz. Ve daha kötüsü, her birinin ayrı bir IP adresi var, DNS yönetimi kabus oluyor.

Ingress ile tek bir LoadBalancer + tek bir IP adresi ile TÜM servislerinize routing yapabilirsiniz. Maliyet farkı dramatik.

**Ingress Resource vs. Ingress Controller: Kafalar Karışmasın!**

Bu ayrım çok kritik ve yeni başlayanların en çok takıldığı yer:

- **Ingress Resource:** Yukarıda gördüğünüz YAML dosyası. Bu sadece bir "arzu beyanı" (desired state). "Ben istiyorum ki `/users`'a gelen trafik user-service'e gitsin" diyorsunuz. Ama bu YAML tek başına HİÇBİR ŞEY yapmaz!

- **Ingress Controller:** İşin asıl beyni. Bu bir Pod olarak cluster'da çalışır ve Ingress Resource'ları izleyerek gerçek routing kurallarını uygular. Ingress Controller olmadan Ingress Resource oluşturmak, trafik polisi olmadan trafik levhası dikmek gibidir — kurallar yazılıdır ama kimse uygulamaz. 🚦

**Popüler Ingress Controller'lar:**

| Controller | Avantajları | Ne Zaman Kullanmalı? |
|------------|-------------|---------------------|
| **NGINX Ingress** | En yaygın, topluluk desteği büyük, esnek annotation sistemi | Genel amaçlı, çoğu senaryo için ideal |
| **Traefik** | Otomatik Let's Encrypt, dinamik konfigürasyon, güzel dashboard | Modern stack, otomatik TLS isteyenler |
| **AWS ALB Ingress (aws-load-balancer-controller)** | AWS native entegrasyon, WAF/Shield desteği | AWS'de çalışanlar, WAF gereksinimi olanlar |
| **Istio Gateway** | Service mesh entegrasyonu, gelişmiş traffic management | Zaten Istio kullananlar |
| **Kong Ingress** | API Gateway özellikleri (rate limiting, auth, plugins) | API management ihtiyacı olanlar |

Getir gibi yoğun trafik alan bir platformda genellikle **NGINX Ingress Controller** veya cloud-native çözümler (AWS ALB Controller) tercih edilir.

**TLS Termination: SSL'i Nerede Sonlandırmalı?**

TLS termination, HTTPS şifrelemesinin nerede çözüldüğü anlamına gelir. Ingress seviyesinde TLS termination yapmak şu anlama gelir:

```
Kullanıcı --[HTTPS/TLS]--> Ingress Controller --[HTTP]--> Pod'lar
```

Neden Ingress'te terminate ediyoruz?
1. **Sertifika yönetimi merkezileşir:** 50 microservice'in her birine ayrı TLS sertifikası koymak yerine, tek bir yerde yönetirsiniz
2. **Pod'lar üzerindeki yük azalır:** TLS handshake CPU-intensive bir işlem. Bunu Ingress'e bırakmak Pod'ları rahatlatır
3. **cert-manager ile otomatik:** Let's Encrypt sertifikaları otomatik alınır, yenilenir — siz uyuyorken!

**Path-Based vs Host-Based Routing**

Ingress iki tür routing destekler:

**Path-based routing** — Aynı domain, farklı path'ler:
```
api.getir.com/users    → user-service
api.getir.com/orders   → order-service
api.getir.com/payments → payment-service
```

**Host-based routing** — Farklı subdomain'ler:
```
users.getir.com   → user-service
orders.getir.com  → order-service
admin.getir.com   → admin-dashboard
```

Pratikte genellikle ikisi birlikte kullanılır. Örneğin Getir'in mimarisini hayal edin: `api.getir.com` altında path-based routing ile onlarca microservice'e yönlendirme yapılırken, `admin.getir.com` tamamen farklı bir frontend uygulamasına gider.

**Annotation'ların Gücü: Ingress'te Her Şey Mümkün**

Ingress annotation'ları inanılmaz güçlüdür. Sadece routing değil, güvenlik ve performans politikalarını da Ingress seviyesinde tanımlayabilirsiniz:

```yaml
annotations:
  # Rate Limiting
  nginx.ingress.kubernetes.io/rate-limit-rps: "100"        # Saniyede max 100 istek
  nginx.ingress.kubernetes.io/rate-limit-burst: "200"       # Burst toleransı
  
  # CORS
  nginx.ingress.kubernetes.io/enable-cors: "true"
  nginx.ingress.kubernetes.io/cors-allow-origin: "https://getir.com"
  
  # Authentication
  nginx.ingress.kubernetes.io/auth-url: "https://auth.internal/verify"
  
  # Timeout'lar
  nginx.ingress.kubernetes.io/proxy-read-timeout: "600"    # Uzun süreli işlemler için
  nginx.ingress.kubernetes.io/proxy-body-size: "50m"       # Dosya upload limiti
  
  # Redirect
  nginx.ingress.kubernetes.io/ssl-redirect: "true"         # HTTP → HTTPS zorla
```

Bu annotation'lar sayesinde rate limiting, authentication, CORS, timeout gibi cross-cutting concern'leri her microservice'te ayrı ayrı implemente etmek yerine, Ingress seviyesinde merkezi olarak yönetebilirsiniz. DRY prensibi burada da geçerli!

**😱 En Sık Yapılan Hata: Controller Olmadan Resource Oluşturmak**

Her Kubernetes yolculuğunda en az bir kez şu sahne yaşanır:

```bash
kubectl apply -f ingress.yaml   # ✅ Başarılı!
kubectl get ingress             # ADDRESS sütunu boş... 🤔
curl api.example.com            # Connection refused 💀
```

Sorun: Ingress Resource'u oluşturdunuz ama cluster'da **Ingress Controller yok!** Bu, restorana menü koymak ama aşçı tutmamak gibidir. Menü var, sipariş alabilirsiniz, ama kimse yemek yapmıyor.

Çözüm:
```bash
# Önce Ingress Controller'ı kurun!
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace

# Sonra Ingress Resource'unuzu apply edin
kubectl apply -f ingress.yaml
```

**🎯 Production Checklist:**
- [ ] Ingress Controller kurulu mu?
- [ ] TLS sertifikası yapılandırıldı mı? (cert-manager önerilir)
- [ ] Rate limiting annotation'ları eklendi mi?
- [ ] Health check path'leri doğru mu?
- [ ] `ssl-redirect: true` ile HTTP'den HTTPS'e yönlendirme var mı?
- [ ] Timeout değerleri uygulamanıza uygun mu?

Şimdi tüm bu kavramları birleştiren bir YAML örneği görelim:

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - api.example.com
    secretName: api-tls
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /users
        pathType: Prefix
        backend:
          service:
            name: user-service
            port:
              number: 80
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: order-service
            port:
              number: 80
```

#### 6. StatefulSet

StatefulSet'i anlamak için şu analojiyi düşünün: **Deployment bir hostel yatakhanesi, StatefulSet ise bir oteldir.**

Hostel yatakhanesinde (Deployment) 10 yatak var. Gelen misafir herhangi bir yatağa yatar, çıkınca yerine başkası gelir. Yatakların numarası önemli değil, hepsi aynı. Misafirin eşyaları (state) yatakta kalmaz — çıkınca her şey temizlenir.

Otelde (StatefulSet) ise durum farklı. Ahmet Bey **her zaman 301 numaralı odada** kalır. Oda kapısında adı yazar. Odadaki eşyaları (PersistentVolume) check-out yapsa bile saklanır — tekrar geldiğinde aynı odaya, aynı eşyalarına kavuşur. Ve otel müşterileri sırayla check-in yapar: önce 301, sonra 302, sonra 303...

İşte Kubernetes'teki StatefulSet tam olarak budur.

**Neden Veritabanları Deployment ile Çalışmaz?**

Bir MongoDB replica set düşünün. 3 node'unuz var: bir Primary (yazma işlemleri) ve iki Secondary (okuma + replikasyon). Bu node'ların birbirini **ismiyle** tanıması gerekir:

```
mongo-0 → Primary ("Ben liderim, yazma işlemleri bana gelsin")
mongo-1 → Secondary ("Ben mongo-0'dan veri kopyalıyorum")
mongo-2 → Secondary ("Ben de mongo-0'dan veri kopyalıyorum")
```

Eğer Deployment kullansaydık ne olurdu?
- Pod isimleri rastgele olurdu: `mongo-xk29f`, `mongo-p83ql`, `mongo-9zmt2`
- Pod restart olduğunda yeni rastgele isim alırdı → diğer node'lar onu tanıyamaz!
- Hangi Pod'un Primary, hangisinin Secondary olduğu bilinemezdi
- Her Pod'un kendi diski olmazdı — veriler uçardı! 💀

Bu kaos, veritabanı dünyasında **kabul edilemez**.

**StatefulSet'in 3 Süper Gücü**

**1. Stable Network Identity (Sabit Ağ Kimliği)**

StatefulSet Pod'ları her zaman `<statefulset-adı>-<sıra-numarası>` formatında isimlendirilir:

```
mongodb-0  →  Her zaman mongodb-0, restart olsa bile
mongodb-1  →  Her zaman mongodb-1
mongodb-2  →  Her zaman mongodb-2
```

Ve Headless Service ile birlikte her Pod'un kendine özel DNS kaydı olur:
```
mongodb-0.mongodb-headless.default.svc.cluster.local
mongodb-1.mongodb-headless.default.svc.cluster.local
mongodb-2.mongodb-headless.default.svc.cluster.local
```

Bu DNS kayıtları **sabittir**. Pod crash olup yeniden oluşturulsa bile, aynı isim ve aynı DNS kaydına sahip olur. Diğer Pod'lar ve uygulamalar her zaman aynı adresten erişebilir.

**2. Stable Storage (Kalıcı Depolama)**

StatefulSet'te her Pod kendi **PersistentVolumeClaim (PVC)**'ine sahiptir ve bu PVC Pod'a bağlıdır:

```
mongodb-0 → data-mongodb-0 (10Gi disk, MongoDB verileri burada)
mongodb-1 → data-mongodb-1 (kendi 10Gi diski)
mongodb-2 → data-mongodb-2 (kendi 10Gi diski)
```

Pod silinse bile PVC **silinmez!** Pod tekrar oluşturulduğunda, aynı PVC'ye yeniden bağlanır ve tüm verilerine kavuşur. Bu, otel odasındaki eşyalarınızın check-out sonrası bile saklanması gibidir.

Deployment'ta ise tüm Pod'lar tek bir PVC'yi paylaşır (veya hiç PVC kullanmaz). Bir Pod ölüp yerine yenisi geldiğinde, eski veriler kaybolur.

**3. Ordered Deployment (Sıralı Dağıtım)**

StatefulSet Pod'ları **sırayla** oluşturulur ve sırayla silinir:

**Oluşturma sırası:**
```
mongodb-0 oluştur → Ready olmasını bekle → mongodb-1 oluştur → Ready olmasını bekle → mongodb-2 oluştur
```

**Silme sırası (tersten):**
```
mongodb-2 sil → tamamen silinmesini bekle → mongodb-1 sil → mongodb-0 sil
```

Bu neden önemli? Çünkü MongoDB replica set'inde **önce Primary (mongodb-0) ayağa kalkmalı**, sonra Secondary'ler ondan veri replike etmeye başlayabilir. Aynı anda 3 Pod'u birden başlatırsanız, Redis Cluster oluşturma veya Kafka partition atama gibi işlemler kaosa döner.

**Headless Service: StatefulSet'in Olmazsa Olmazı**

StatefulSet'in düzgün çalışması için mutlaka bir **Headless Service** gerekir. Normal bir Service'ten farkı `clusterIP: None` olmasıdır:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongodb-headless
spec:
  clusterIP: None          # ← Bu satır onu "headless" yapar
  selector:
    app: mongodb
  ports:
  - port: 27017
```

Normal Service bir **sanal IP** oluşturur ve gelen trafiği rastgele bir Pod'a yönlendirir. Ama veritabanlarında "rastgele bir Pod'a git" olmaz! Primary'e mi yazacaksınız, Secondary'den mi okuyacaksınız — bunu bilmeniz gerekir.

Headless Service sanal IP oluşturmaz, bunun yerine **her Pod için ayrı DNS A kaydı** oluşturur. Böylece uygulamanız doğrudan `mongodb-0.mongodb-headless` diye Primary'e, `mongodb-1.mongodb-headless` diye Secondary'e bağlanabilir.

**🤔 Ne Zaman StatefulSet Kullanmamalısınız?**

Bu çok önemli bir soru ve cevabı belki sizi şaşırtacak: **Çoğu durumda StatefulSet kullanmamalısınız!**

Kubernetes'te veritabanı çalıştırmak operasyonel olarak karmaşıktır. Backup, restore, failover, upgrade — bunların hepsi manuel (veya operator ile yarı-otomatik) yönetilmesi gereken işlemler. Bu yüzden:

| Senaryo | Tavsiye |
|---------|---------|
| Production veritabanı | ☁️ **Managed service kullanın** (AWS RDS, MongoDB Atlas, ElastiCache) |
| Dev/Test ortamı | ✅ StatefulSet ile kendi DB'nizi çalıştırabilirsiniz |
| Kafka/RabbitMQ/Redis | 🤏 **Operator kullanın** (Strimzi, RabbitMQ Operator) — düz StatefulSet yerine |
| Özel gereksinimler (data locality, compliance) | ✅ StatefulSet mantıklı olabilir |

Getir gibi bir platformda production MongoDB'yi Kubernetes StatefulSet ile çalıştırmak yerine **MongoDB Atlas** kullanmak çok daha mantıklıdır. Çünkü Atlas otomatik backup, point-in-time recovery, auto-scaling, monitoring gibi özellikleri kutudan çıkar çıkmaz sunar. Aynı şeyleri StatefulSet ile yapmak, kendi evinizi kendiniz inşa etmek gibidir — yapabilirsiniz ama neden yapasınız?

**🔥 Gerçek Dünya: MongoDB Replica Set in K8s**

Eğer yine de Kubernetes'te MongoDB çalıştırmanız gerekiyorsa (dev/test veya compliance gereksinimleri), şu adımları izlersiniz:

1. **Headless Service** oluşturun (yukarıda gösterdik)
2. **StatefulSet** ile 3 replica MongoDB Pod'u oluşturun
3. Pod'lar ayağa kalktıktan sonra **replica set'i initialize** edin:
```bash
# mongodb-0 Pod'una bağlanın
kubectl exec -it mongodb-0 -- mongosh

# Replica set'i başlatın
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb-0.mongodb-headless:27017" },
    { _id: 1, host: "mongodb-1.mongodb-headless:27017" },
    { _id: 2, host: "mongodb-2.mongodb-headless:27017" }
  ]
})
```

Ancak production için **MongoDB Community Operator** veya **Percona Operator** kullanmak çok daha akıllıca — bunlar backup, scaling, failover gibi işlemleri otomatik yönetir.

**⚠️ Sık Yapılan Hatalar**

1. **Headless Service'i unutmak:** StatefulSet oluşturdunuz ama Headless Service yok → Pod'lar birbirini DNS ile bulamaz
2. **PVC'leri temizlememek:** StatefulSet'i sildiğinizde PVC'ler **silinmez** (kasıtlı bir davranış). Disk maliyeti artmaya devam eder. Manuel temizlik gerekir: `kubectl delete pvc -l app=mongodb`
3. **`serviceName` alanını yanlış yazmak:** StatefulSet'teki `serviceName` ile Headless Service'in `metadata.name`'i birebir eşleşmeli
4. **Stateless uygulamalar için StatefulSet kullanmak:** Web server'ınız için StatefulSet kullanmanıza gerek yok — Deployment yeterli ve daha basit

Şimdi tüm bu kavramları birleştiren örneğe bakalım:

```yaml
# statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
spec:
  serviceName: "mongodb"
  replicas: 3
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
      - name: mongodb
        image: mongo:5.0
        ports:
        - containerPort: 27017
        volumeMounts:
        - name: data
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi
```

**Deployment vs StatefulSet:**
```
Deployment (Stateless):
- Random pod names (web-abc123, web-def456)
- Any pod is interchangeable
- Use: Web servers, APIs

StatefulSet (Stateful):
- Predictable names (mongo-0, mongo-1, mongo-2)
- Stable network identity
- Ordered deployment/scaling
- Persistent storage per pod
- Use: Databases, message queues
```

#### 7. Namespace

Namespace'i anlamak için şu analojiyi düşünün: Kubernetes cluster'ınız **bir apartman binası**, Namespace'ler ise **katlarıdır**. Her takım kendi katında oturur — mobilyaları (Pod'lar), mutfağı (Service'ler), dolabı (Secret'lar) ayrı. 3. kattaki backend takımı ne kadar gürültü yaparsa yapsın, 5. kattaki frontend takımının işini etkilemez. Herkes kendi katında, kendi kurallarıyla yaşar. İşte Namespace tam olarak budur: cluster içinde **mantıksal izolasyon** sağlayan sanal duvarlar.

**Neden Namespace'lere İhtiyacımız Var?**

Tek bir cluster'da 20 takım, 200 microservice çalıştırdığınızı hayal edin. Namespace olmadan ne olur?
- `kubectl get pods` yazdığınızda ekranınızda 500+ Pod listelenir — hangi Pod hangi takımın? Bulmak samanlıkta iğne aramak gibi.
- Bir junior developer yanlışlıkla production `user-service`'i siler çünkü aynı isimde dev ortamında da bir tane var — hangisini sildiğini fark edemez. 💀
- Bir takımın uygulaması CPU'nun %90'ını yer, diğer tüm takımlar "neden servislerimiz yavaşladı?" diye sorar.

Namespace'ler bu kaosun çözümüdür: **multi-tenancy** (birden fazla takımın aynı cluster'ı paylaşması), **environment separation** (dev/staging/prod ayrımı) ve **resource isolation** (kaynakların adil dağılımı) sağlar.

**Kubernetes'in Varsayılan Namespace'leri**

Her Kubernetes cluster'ı kurulduğunda 4 namespace ile gelir:

| Namespace | Ne İşe Yarar? | Dokunmalı mısınız? |
|-----------|--------------|---------------------|
| **default** | Namespace belirtmezseniz her şey buraya düşer. Yeni başlayanların "çöplüğü" 🗑️ | Production'da KULLANMAYIN — her şeyi explicit namespace'e koyun |
| **kube-system** | Kubernetes'in kendi bileşenleri: CoreDNS, kube-proxy, controller-manager | Asla dokunmayın, sadece izleyin |
| **kube-public** | Tüm kullanıcıların (authentication olmadan bile) okuyabileceği veriler | Nadiren kullanılır |
| **kube-node-lease** | Node heartbeat bilgileri — node'ların "ben hayattayım" sinyalleri | Asla dokunmayın |

**ResourceQuota: "Herkes Kendi Payını Yesin!"**

Apartman analojimize dönelim. Her katta bir elektrik sayacı olduğunu düşünün. Bir kat ne kadar elektrik harcayabileceği sınırlıdır — aksi halde bir kat tüm binanın elektriğini çeker ve diğer katlar karanlıkta kalır.

ResourceQuota tam olarak budur: bir Namespace'in tüketebileceği **maksimum kaynak miktarını** belirler. CPU, memory, Pod sayısı, PVC sayısı — hepsine limit koyabilirsiniz.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: backend-team-quota
  namespace: backend
spec:
  hard:
    requests.cpu: "10"        # Toplam CPU request'i max 10 core
    requests.memory: 20Gi     # Toplam memory request'i max 20Gi
    limits.cpu: "20"           # Toplam CPU limit'i max 20 core
    limits.memory: 40Gi       # Toplam memory limit'i max 40Gi
    pods: "50"                 # Maximum 50 Pod
    persistentvolumeclaims: "20" # Maximum 20 PVC
    services.loadbalancers: "2"  # Maximum 2 LoadBalancer (pahalı!)
```

ResourceQuota aktifken her Pod **mutlaka** resource request/limit belirtmek zorundadır. Belirtmezseniz Pod oluşturulamaz! Bu da bizi bir sonraki konuya getiriyor...

**LimitRange: "Varsayılan Limitleri Ben Koyuyorum"**

ResourceQuota namespace genelinde toplam limitleri belirler, ama ya developer Pod'una hiç limit koymayı unutursa? İşte LimitRange burada devreye girer — Pod veya Container seviyesinde **varsayılan (default)** ve **minimum/maximum** resource değerlerini tanımlar:

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: backend
spec:
  limits:
  - type: Container
    default:           # Pod'a limit belirtilmezse bu değerler uygulanır
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:    # Pod'a request belirtilmezse bu değerler uygulanır
      cpu: "100m"
      memory: "128Mi"
    max:               # Hiçbir container bundan fazlasını isteyemez
      cpu: "2"
      memory: "4Gi"
    min:               # Hiçbir container bundan azını isteyemez
      cpu: "50m"
      memory: "64Mi"
```

LimitRange bir güvenlik ağıdır. Developer "resource limits mı, ne gerek var?" deyip Pod'unu deploy ettiğinde, LimitRange otomatik olarak varsayılan limitleri enjekte eder. Böylece bir Pod'un tüm node'un memory'sini yiyip OOMKilled kaosuna neden olması önlenir.

**Namespace'ler Arası Network Policy: Duvarları Örme**

Varsayılan olarak Kubernetes'te tüm Pod'lar birbirleriyle konuşabilir — namespace farkı olsa bile! Bu güvenlik açısından tehlikelidir. `dev` namespace'indeki bir test Pod'unun `production` namespace'indeki veritabanına erişebilmesini istemezsiniz.

Network Policy ile namespace'ler arasında **güvenlik duvarları** oluşturabilirsiniz:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-from-other-namespaces
  namespace: production
spec:
  podSelector: {}           # production'daki TÜM Pod'lara uygula
  ingress:
  - from:
    - podSelector: {}        # Sadece AYNI namespace'ten gelen trafiğe izin ver
```

Bu policy, `production` namespace'ine dışarıdan gelen tüm trafiği engeller — sadece production içindeki Pod'lar birbirine erişebilir. Dev namespace'indeki meraklı bir developer artık production DB'ye bağlanamaz. 🛡️

**⚠️ Ne Zaman Ayrı Namespace YETERSİZDİR?**

Çok kritik bir nokta: Namespace'ler **mantıksal** izolasyon sağlar, **fiziksel** değil! Aynı cluster'daki namespace'ler aynı node'ları, aynı etcd'yi, aynı control plane'i paylaşır.

Bu ne anlama gelir?
- Bir namespace'teki Pod, node'un tüm CPU'sunu tüketirse (resource limits yoksa), diğer namespace'lerdeki Pod'lar da etkilenir
- Bir security breach cluster seviyesinde yayılabilir
- etcd'deki bir sorun TÜM namespace'leri etkiler

Bu yüzden **production ortamını ayrı bir cluster'da çalıştırın!** Namespace ile dev/prod ayırmak, aynı kasada farklı çekmecelere para koymak gibidir — hırsız kasayı açtığında hepsini görür. Farklı cluster'lar ise farklı kasalar demektir:

```
✅ Doğru yaklaşım:
  Cluster-1 (dev):   dev namespace'leri → team-a-dev, team-b-dev
  Cluster-2 (staging): staging namespace'leri → team-a-stg, team-b-stg
  Cluster-3 (prod):  production namespace'leri → team-a-prod, team-b-prod

❌ Riskli yaklaşım:
  Tek Cluster: dev, staging, production namespace'leri yan yana 😰
```

**🏢 Gerçek Dünya: Takım Bazlı Namespace Stratejisi**

Getir gibi bir şirkette namespace stratejisi genellikle şöyle görünür:

```
# Takım bazlı namespace'ler (her environment'ta)
backend-core/          → Auth, User, Core API servisleri
backend-commerce/      → Order, Payment, Catalog servisleri
backend-logistics/     → Courier, Route, Delivery servisleri
data-platform/         → Kafka consumers, ETL jobs, analytics
infrastructure/        → Monitoring (Prometheus, Grafana), logging (ELK)
ingress-nginx/         → Ingress controller (kendi namespace'inde izole)
cert-manager/          → TLS sertifika yönetimi
```

Her takım kendi namespace'inde tam yetkiye sahip (RBAC ile), ama başka takımların namespace'lerine erişemez. Platform/SRE takımı ise tüm namespace'leri görebilir ve yönetebilir. Bu yapı DevOps'un ruhuna uygundur: **"You build it, you run it."**

**📋 Namespace Best Practices:**

| Practice | Açıklama | Öncelik |
|----------|---------|----------|
| **Her namespace'e ResourceQuota koyun** | Kaynak tüketimini sınırlandırın | 🔴 Kritik |
| **LimitRange tanımlayın** | Developer'ların limit koymayı unutmasına karşı güvenlik ağı | 🔴 Kritik |
| **Network Policy uygulayın** | Namespace'ler arası izolasyon sağlayın | 🔴 Kritik |
| **RBAC ile erişim kontrolü** | Her takım sadece kendi namespace'ine erişsin | 🔴 Kritik |
| **`default` namespace'i kullanmayın** | Her şeyi explicit namespace'e deploy edin | 🟡 Önemli |
| **İsimlendirme standardı belirleyin** | `<takım>-<ortam>` formatı önerilir | 🟡 Önemli |
| **Label ve annotation ekleyin** | `team=backend`, `env=dev` gibi metadata ekleyin | 🟢 Orta |

Şimdi tüm bu kavramları YAML örnekleriyle görelim:

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production

---
# Resource quota
apiVersion: v1
kind: ResourceQuota
metadata:
  name: prod-quota
  namespace: production
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
    pods: "50"
```

```bash
# Create namespace
kubectl create namespace staging

# Deploy to namespace
kubectl apply -f deployment.yaml -n staging

# Set default namespace
kubectl config set-context --current --namespace=staging

# Get resources from all namespaces
kubectl get pods --all-namespaces
```

### Kubernetes Networking

#### Service Discovery

Service Discovery'yi anlamak için şu sahneyi hayal edin: Yeni bir şehre taşındınız. Bir pizzacı arıyorsunuz ama adresini bilmiyorsunuz. Ne yaparsınız? **Telefon rehberine** bakarsınız! İşte Kubernetes'teki Service Discovery tam olarak budur — cluster içindeki servislerin birbirini bulması için kullanılan **otomatik telefon rehberi** sistemi.

Geleneksel dünyada microservice'ler birbirine IP adresiyle bağlanırdı. Ama Kubernetes'te Pod'lar gelip gider, her seferinde yeni IP alır. Dün `10.244.1.5`'teki user-service bugün `10.244.3.12`'de olabilir. IP'leri hardcode'lamak intihar olur. Service Discovery bu sorunu çözer: **"user-service nerede?" diye sorarsınız, sistem size güncel adresi verir.**

**CoreDNS: Cluster'ın Görünmez Kahramanı**

Her Kubernetes cluster'ında sessiz sedasız çalışan bir kahraman vardır: **CoreDNS**. Bu, `kube-system` namespace'inde çalışan bir DNS sunucusudur ve cluster içindeki tüm Service'ler için otomatik DNS kayıtları oluşturur. Siz bir Service oluşturduğunuz anda, CoreDNS bunu kaydeder ve herkesin erişebileceği bir DNS adı oluşturur.

CoreDNS olmadan Kubernetes'te service discovery mümkün olmazdı. Ama çoğu developer CoreDNS'in varlığından bile haberdar değildir — tıpkı şehirdeki telefon santralinin varlığını düşünmeden telefon kullanmamız gibi. 📞

**DNS Format: Cluster İçi Adres Sistemi**

Kubernetes'teki her Service'in tam DNS adresi şu formattadır:

```
<service-adı>.<namespace>.svc.cluster.local
```

Örneğin:
```
user-service.backend.svc.cluster.local      → backend namespace'indeki user-service
order-service.production.svc.cluster.local   → production namespace'indeki order-service
redis.cache.svc.cluster.local                → cache namespace'indeki redis
```

Ama güzel haber: **aynı namespace içindeyseniz, sadece service adını kullanmanız yeterli!** Kubernetes otomatik olarak namespace ve domain kısmını ekler:

```javascript
// Aynı namespace'teyseniz — kısa isim yeterli!
const url = 'http://user-service:8080';

// Bu, arka planda şuna dönüşür:
// http://user-service.backend.svc.cluster.local:8080
```

Farklı namespace'teki bir servise erişiyorsanız, o zaman namespace'i de belirtmeniz gerekir. Tam FQDN (Fully Qualified Domain Name) genellikle gereksizdir — `service-name.namespace` çoğu zaman yeterlidir.

**Environment Variables vs DNS: İkisi de Var, Biri Daha İyi**

Kubernetes aslında iki yöntemle service discovery bilgisi sunar:

1. **Environment Variables:** Pod oluşturulduğunda, o an var olan tüm Service'lerin IP ve port bilgileri environment variable olarak enjekte edilir:
```bash
# Pod içinde otomatik oluşturulan env vars:
USER_SERVICE_SERVICE_HOST=10.96.45.12
USER_SERVICE_SERVICE_PORT=8080
```

2. **DNS:** CoreDNS üzerinden isim çözümleme.

**DNS her zaman tercih edilmelidir.** Neden mi?
- Environment variable'lar sadece **Pod oluşturulduğu anda** var olan servisleri içerir. Pod'dan sonra oluşturulan servisler env var'larda görünmez!
- Circular dependency riski: Service A, Service B'nin env var'ına ihtiyaç duyar ama B henüz oluşturulmamıştır
- DNS ise **dinamiktir** — Service ne zaman oluşturulursa oluşturulsun, DNS sorgusu güncel sonucu döner

**Headless Service ile StatefulSet Discovery**

Normal Service'ler tek bir ClusterIP üzerinden load balancing yapar. Ama StatefulSet'lerde (veritabanları, Kafka gibi) **belirli bir Pod'a** erişmeniz gerekir. İşte Headless Service burada devreye girer:

```
# Headless Service + StatefulSet = Her Pod'un kendi DNS kaydı
mongo-0.mongodb.default.svc.cluster.local   → İlk MongoDB Pod'u (genellikle Primary)
mongo-1.mongodb.default.svc.cluster.local   → İkinci MongoDB Pod'u (Secondary)
mongo-2.mongodb.default.svc.cluster.local   → Üçüncü MongoDB Pod'u (Secondary)
```

Bu sayede uygulamanız "beni Primary'e bağla" diyebildiği gibi, "beni spesifik olarak mongo-2'ye bağla" da diyebilir. Headless Service, StatefulSet bölümünde detaylıca anlattığımız `clusterIP: None` olan Service türüdür.

**🔧 Gerçek Dünya Debugging: Service Discovery Sorunlarını Çözme**

Production'da en sık karşılaşılan sorunlardan biri: "Servisim diğer servise bağlanamıyor!" İşte adım adım debug yöntemi:

```bash
# 1. Pod içinden DNS çözümleme testi
kubectl exec -it my-pod -- nslookup user-service
# Çıktı: user-service.backend.svc.cluster.local → 10.96.45.12 ✅

# 2. Eğer nslookup yoksa, wget ile deneyin
kubectl exec -it my-pod -- wget -qO- http://user-service:8080/health

# 3. CoreDNS Pod'ları çalışıyor mu?
kubectl get pods -n kube-system -l k8s-app=kube-dns

# 4. Service endpoint'leri doğru mu? (Arkasında Pod var mı?)
kubectl get endpoints user-service
# Eğer ENDPOINTS sütunu boşsa → Service'in selector'ı Pod'larla eşleşmiyor! 🐛

# 5. Farklı namespace'ten erişmeye çalışıyorsanız
kubectl exec -it my-pod -- nslookup user-service.backend.svc.cluster.local
```

En sık yapılan hatalar:
- Service selector'ı ile Pod label'ı **uyuşmuyor** → endpoints boş kalır
- Farklı namespace'ten erişirken **namespace belirtmeyi** unutmak
- Port numaralarını karıştırmak (Service port vs Container port)
- NetworkPolicy'nin trafiği **engellemesi** — "DNS çalışıyor ama bağlanamıyorum" durumu

```javascript
// DNS-based service discovery
// service-name.namespace.svc.cluster.local

// From same namespace
const userServiceUrl = 'http://user-service:8080';

// From different namespace
const orderServiceUrl = 'http://order-service.production.svc.cluster.local:8080';

// External service
const externalApi = 'http://external-api.default.svc.cluster.local';
```

#### Network Policies

Network Policies, cluster İÇİNDEKİ firewall kurallarıdır. Bunu şöyle düşünün: bir apartman kompleksinde yaşıyorsunuz. Varsayılan olarak herkes herkesin kapısını çalabilir — komşunuz, tesisatçı, hatta tanımadığınız biri bile. Network Policies, her dairenin kapısına güvenlik görevlisi koymak gibidir: "Sen girebilirsin, sen giremezsin."

**Varsayılan Durum — TEHLİKELİ:**
Kubernetes'te varsayılan olarak **TÜM pod'lar TÜM pod'larla konuşabilir**. Hiçbir izolasyon yok! Bu development için rahat ama production'da bir kabus. Bir pod hack'lenirse, tüm cluster'a erişebilir. Hırsız bir daireye girdiğinde tüm apartmanı gezebilir — bunu istemezsiniz.

**Ingress vs Egress:**
- **Ingress policies:** Kim İÇERİ gelebilir? (Kapıya gelen misafirleri kontrol etmek)
- **Egress policies:** Kim DIŞARI çıkabilir? (Hangi servislere bağlanabileceğinizi kontrol etmek)

**Label-based Selection:**
Policies, pod'lara label'lar aracılığıyla uygulanır. `app: api` label'ına sahip tüm pod'lara "sadece `role: frontend` label'lı pod'lardan gelen trafiği kabul et" diyebilirsiniz. Etiketleme sistemi = akıllı güvenlik sistemi.

**Default Deny — Zero Trust Yaklaşımı:**
En iyi pratik: önce HER ŞEYİ engelle, sonra sadece gerekli olanları aç. Askeri üs mantığı — kimse giriş kartı olmadan giremez, herkesin kartı sadece yetkili olduğu bölgelere açar.

**Gerçek Dünya Senaryosu:**
Frontend pod'ları sadece API pod'larıyla konuşmalı. API pod'ları sadece database pod'larıyla konuşmalı. Frontend pod'ları direkt database'e ERİŞEMEMELİ! Bir e-ticaret sitesinde kasiyere sipariş verirsiniz, kasanın arkasına girip mutfağa dalmazsınız.

```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-allow-ingress
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 8080
```

### Auto-scaling

Auto-scaling, sisteminizin iş yüküne göre otomatik olarak büyüyüp küçülmesidir. Bunu bir restoran gibi düşünün: öğle saatlerinde kalabalık olunca yeni masalar açarsınız, gece boşalınca fazla masaları kaldırırsınız. Garsonları da buna göre ayarlarsınız. Sürekli 100 kişilik salon açık tutmak yerine, kaç müşteri varsa ona göre kapasite ayarlarsınız.

**Üç Seviye Auto-scaling:**
1. **HPA (Horizontal Pod Autoscaler):** Daha fazla pod ekler. Restorana yeni garson almak gibi — aynı boyutta ama daha fazla.
2. **VPA (Vertical Pod Autoscaler):** Pod'ları daha güçlü yapar. Garsona daha fazla kol vermek gibi — aynı kişi ama daha güçlü.
3. **Cluster Autoscaler:** Daha fazla node ekler. Restorana yeni bir kat açmak gibi — tamamen yeni fiziksel alan.

**Neden Auto-scaling?**
- **Maliyet:** Kullanmadığınız kapasiteye para ödemeyin. Gece 3'te 50 pod çalıştırmanın anlamı yok.
- **Performans:** Trafik spike'larını otomatik karşılayın. Black Friday geldiğinde manual scaling ile geç kalırsınız.
- **Operasyonel yük:** 7/24 monitoring yapıp "aa CPU %90 oldu, hadi scale edelim" demekten kurtulun.

#### Horizontal Pod Autoscaler (HPA)

HPA, Kubernetes'in en çok kullanılan auto-scaling mekanizmasıdır. Metric'leri izler (CPU, memory, custom metrics) ve otomatik olarak pod sayısını ayarlar.

**Nasıl Çalışır:**
1. Her **15 saniyede** bir metric'leri kontrol eder (metrics-server'dan)
2. Mevcut kullanım ile hedef kullanımı karşılaştırır
3. Gerekli replica sayısını hesaplar: `istenenReplica = mevcutReplica × (mevcutMetric / hedefMetric)`
4. Scale up veya scale down yapar

**Custom Metrics ile Scaling:**
Sadece CPU/memory değil, kendi metric'lerinizle de scale edebilirsiniz:
- Request per second (RPS)
- Queue length (Kafka consumer lag gibi)
- Active WebSocket connections
- Custom Prometheus metric'leri

**Cooldown Period — Flapping Önleme:**
HPA'nın bir stabilization window'u vardır. Scale up sonrası hemen scale down yapılmaz (varsayılan 5 dakika bekler). Neden? Trafik dalgalanıyor olabilir. Sürekli 3→10→3→10 yapılırsa (flapping), pod'lar sürekli oluşturulup yok edilir — bu kaos yaratır.

**Gerçek Dünya:**
Black Friday günü bir e-ticaret sitesi: normal günlerde 3 pod yeterli. Kampanya başlayınca trafik 10x artar → HPA bunu tespit eder → 3 pod'dan 30 pod'a otomatik scale eder → kampanya bitince kademeli olarak 3'e düşer. Manuel müdahale SIFIR.

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

#### Vertical Pod Autoscaler (VPA)

VPA, pod'ların CPU ve memory REQUEST'lerini otomatik olarak ayarlar. HPA daha fazla pod eklerken, VPA mevcut pod'ları daha güçlü yapar. Analoji: HPA = daha fazla garson işe almak, VPA = garsona protein tozu vererek daha güçlü yapmak. 💪

**Ne Zaman VPA, Ne Zaman HPA?**
- **VPA kullan:** Batch job'lar, tek instance çalışması gereken veritabanları (single-instance DB), JVM uygulamalarında heap size optimizasyonu
- **HPA kullan:** Web server'lar, API gateway'ler, stateless mikroservisler — yatay scale edilebilen her şey

**⚠️ KRİTİK UYARI:** VPA ve HPA aynı resource'u (CPU veya memory) hedef alarak **AYNI ANDA KULLANILMAMALIDIR!** Birisi "pod'u büyüt" derken diğeri "daha fazla pod ekle" der — kaos çıkar. HPA CPU'ya göre scale ediyorsa, VPA sadece memory'yi yönetmelidir.

**Update Modes:**
- **Auto:** Pod'ları otomatik yeniden başlatarak yeni resource değerlerini uygular (downtime olabilir!)
- **Initial:** Sadece yeni oluşturulan pod'lara uygular, mevcut pod'lara dokunmaz
- **Off:** Hiçbir değişiklik yapmaz, sadece "şu kadar resource öneriyorum" der — recommendation-only mode. Production'da önce bu mode ile başlayıp önerileri incelemeniz tavsiye edilir.

```yaml
# vpa.yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: web-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-deployment
  updatePolicy:
    updateMode: "Auto"  # Recreate, Initial, Off
```

#### Cluster Autoscaler
- Node'ları otomatik olarak scale eder
- Pod schedule edilemiyorsa node ekler
- Idle node'ları kaldırır

### Helm - Package Manager

Helm, Kubernetes dünyasının **App Store'u**dur. Telefonunuza uygulama yüklerken tek bir "Yükle" butonuna basarsınız — arka planda onlarca dosya indirilir, yapılandırılır, kurulur. Helm de aynısını Kubernetes için yapar: `helm install redis` dersiniz, arka planda Deployment, Service, ConfigMap, Secret, PersistentVolumeClaim... hepsi otomatik oluşturulur. 10 tane YAML dosyası yazmak yerine tek komut!

**Temel Kavramlar:**

**Chart = Paket:**
Bir Helm Chart, bir uygulamayı Kubernetes'e deploy etmek için gereken TÜM resource tanımlarını içerir. Redis chart'ında Deployment, Service, ConfigMap, health check'ler, security context — her şey hazır. Siz sadece "kur" dersiniz.

**values.yaml = Ayarlar Dosyası:**
Chart'ı değiştirmeden özelleştirmenizi sağlar. Tıpkı bir oyunda `settings.json` gibi: grafik kalitesini, ses seviyesini değiştirirsiniz ama oyunun koduna dokunmazsınız. `replicaCount: 3`, `image.tag: "2.0"` gibi değerlerle chart'ı kendi ortamınıza uyarlarsınız.

**Neden Helm Önemli?**
- **Version management:** Her deployment bir "release" olur. v1.0, v1.1, v2.0... Her birini takip edebilirsiniz.
- **Kolay rollback:** Yeni versiyon patlattı mı? `helm rollback myapp 1` — 3 saniyede eski versiyona dönüş. Geri al butonu işte bu kadar basit.
- **Paylaşım:** Artifact Hub'da binlerce hazır chart var. Prometheus, Grafana, PostgreSQL, Redis... Hepsini community yazmış, test etmiş, production-ready.

**Helm 3 vs Helm 2:**
Helm 2'de cluster içinde **Tiller** adında bir server çalışıyordu — cluster-admin yetkisiyle! Bu devasa bir güvenlik açığıydı. Helm 3'te Tiller tamamen kaldırıldı. Artık Helm doğrudan kubeconfig kullanarak çalışır. Güvenlik açısından büyük bir adım.

**Gerçek Dünya:**
`helm install prometheus prometheus-community/kube-prometheus-stack` — bu TEK komutla Prometheus, Grafana, AlertManager, node-exporter ve onlarca ServiceMonitor kurulur. Manuel yapılsa? En az 2 gün YAML yazarsınız. Helm ile 2 dakika.

**Nedir (Özet):**
- Kubernetes için package manager (apt, yum gibi)
- Charts: Pre-configured K8s resources
- Templating & versioning

```bash
# Add repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Install chart
helm install my-redis bitnami/redis --namespace production

# List releases
helm list

# Upgrade release
helm upgrade my-redis bitnami/redis --set auth.password=newpass

# Rollback
helm rollback my-redis 1

# Uninstall
helm uninstall my-redis
```

**Custom Chart:**
```yaml
# Chart.yaml
apiVersion: v2
name: myapp
description: My application
version: 1.0.0

# values.yaml
replicaCount: 3
image:
  repository: myapp
  tag: "1.0"
service:
  type: LoadBalancer
  port: 80

# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Chart.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

### Kubernetes Best Practices

#### 1. Resource Management

Resource management, pod'larınıza ne kadar CPU ve memory verileceğini kontrol etmektir. Bunu bir restoran rezervasyonu gibi düşünün:

**Requests = Restoran Rezervasyonu:**
Rezervasyon yaptırdığınızda, restoran sizin için bir masa AYIRIR. Gelmesseniz bile o masa sizin için bekler. Kubernetes'te `requests`, scheduler'ın pod'u bir node'a yerleştirirken kullandığı garantili minimum kaynaktır. "Bu pod'a EN AZ 128Mi memory lazım" dediğinizde, scheduler sadece bu kadar boş alanı olan node'lara yerleştirir.

**Limits = Sipariş Edebileceğiniz Maksimum Yemek:**
Restorana gittiniz ama "en fazla 5 tabak sipariş edebilirsiniz" kuralı var. Pod limit'i aştığında:
- **Memory limit aşımı:** Pod **OOM Killed** olur (Out Of Memory). Direkt öldürülür. Restorandan kovulursunuz.
- **CPU limit aşımı:** Pod **throttle** edilir. Yavaşlatılır ama öldürülmez. Siparişiniz gelir ama çok yavaş.

**QoS (Quality of Service) Classes — VIP Sistemi:**
- **Guaranteed (VIP müşteri):** `requests == limits` olduğunda. En son evict edilen. Kırmızı halı serilir. Production database'leri için ideal.
- **Burstable (Normal müşteri):** `requests < limits` olduğunda. Gerektiğinde daha fazla kaynak kullanabilir, ama kaynak sıkışınca Guaranteed'dan önce evict edilir.
- **BestEffort (Kapıda bekleyen):** Hiç request/limit belirlenmemiş. İlk evict edilen! Masa boşta kaldıysa otururlar, biri gelince kalkarlar. Dev/test ortamı dışında KULLANMAYIN.

**Yaygın Hatalar:**
- ❌ Limit'leri çok düşük ayarlamak → sürekli OOM kill'ler → pod restart döngüsü → kullanıcılar 502 görür
- ❌ Limit'leri çok yüksek ayarlamak → kaynak israfı → bulut faturası katlanır → CFO kapınızı çalar
- ✅ Doğru yaklaşım: monitoring ile gerçek kullanımı izleyin, sonra %20-30 buffer ekleyin

```yaml
# Always set requests and limits
resources:
  requests:
    memory: "128Mi"
    cpu: "100m"
  limits:
    memory: "256Mi"
    cpu: "200m"

# Quality of Service (QoS) Classes:
# Guaranteed: requests == limits
# Burstable: requests < limits
# BestEffort: no requests/limits (evicted first)
```

#### 2. Health Checks

Health check'ler, Kubernetes'in pod'larınızın durumunu anlaması için kullandığı mekanizmadır. Bunu bir doktor muayenesi gibi düşünün: doktor nabzınızı, ateşinizi ve reflekslerinizi kontrol eder — her biri farklı bir şeyi test eder.

**Üç Probe Tipi:**

**1. Liveness Probe — "Uygulama HAYATTA mı?"**
Doktorun nabız kontrolü. Nabız yoksa → defibrilatör (pod'u öldür ve yeniden başlat). Uygulama deadlock'a girmiş olabilir, sonsuz döngüde olabilir, memory leak yüzünden cevap veremiyordur. Liveness probe başarısız olursa Kubernetes pod'u ÖLDÜRÜR ve yeniden oluşturur.

**2. Readiness Probe — "Uygulama trafik almaya HAZIR mı?"**
Doktorun "spor yapabilir misiniz?" sorusu. Hasta ayaktadır (alive) ama henüz koşamaz (not ready). Readiness probe başarısız olursa, pod Service'den ÇIKARILIR — artık trafik yönlendirilmez. Pod öldürülmez, sadece "dinlenmeye" alınır. Database bağlantısı kurulana kadar, cache ısınana kadar, config yüklenene kadar not-ready olabilir.

**3. Startup Probe — "Uygulama başlamayı BİTİRDİ mi?"**
Yeni doğan bebeğin muayenesi. Henüz yürüyemiyor — ama bu normal, biraz zaman ver. Ağır Java uygulamaları, büyük ML model'leri yükleyen servisler startup'ta uzun sürebilir. Startup probe tamamlanana kadar liveness probe DEVRE DIŞI kalır — yoksa yavaş başlayan uygulama daha başlamadan öldürülür!

**🚨 Yaygın ve TEHLİKELİ Hata:**
Liveness probe'u bir dependency'ye (database, Redis, external API) yönlendirmek. Database 30 saniye erişilemez olursa ne olur? TÜM pod'lar restart eder → yeniden başlayan pod'lar database'e bağlanmaya çalışır → database daha da yüklenir → kısır döngü → **tam bir cascading failure!**

**✅ Best Practice:**
- **Liveness:** Basit bir `/healthz` endpoint'i — sadece "ben yaşıyorum, 200 OK" dönsün. Dependency kontrolü YAPMAYIN.
- **Readiness:** `/ready` endpoint'i — dependency'leri kontrol edin (DB bağlantısı var mı, cache hazır mı?).
- Liveness = "hastanın kalbi atıyor mu?", Readiness = "hasta taburcu edilebilir mi?"

```yaml
# Liveness: Should container be restarted?
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
  failureThreshold: 3

# Readiness: Should container receive traffic?
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5

# Startup: For slow-starting containers
startupProbe:
  httpGet:
    path: /started
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

#### 3. Security

**Pod Güvenliği Neden Önemli? — Ana Anahtar Analojisi**

Bir apartmanda yaşadığınızı düşünün. Apartman yönetimi size dairenizin anahtarını verir — bu normal. Ama ya yönetim herkese **binanın ana anahtarını** verse? Herkes her daireye, bodrum kata, çatı katına, elektrik panosuna erişebilir. İşte container'da `root` olarak çalışmak tam olarak bu — container'a binanın ana anahtarını veriyorsunuz. Bir saldırgan bu container'ı ele geçirirse, host sistemine kadar ulaşabilir.

**🚨 Gerçek Dünya Hikayesi: Container'larda Kripto Madenciliği**

Son yıllarda en yaygın Kubernetes saldırılarından biri: Saldırganlar, root olarak çalışan ve güvenlik ayarları gevşek pod'ları tespit ediyor → container'a sızıyor → kripto madencilik yazılımı yüklüyor → sizin bulut faturanız patlayana kadar madencilik yapıyor. Bir şirket sabah uyandığında $50.000'lık AWS faturasıyla karşılaştı. Sebebi? Pod'lar root olarak çalışıyor, filesystem yazılabilir, capability'ler kısıtlanmamıştı.

**Güvenlik Katmanları — Defense in Depth:**

**1. `runAsNonRoot` — En Az Yetki Prensibi:**
"Bu container ROOT olarak ÇALIŞAMAZ" der. Eğer image yanlışlıkla root user ile build edildiyse, Kubernetes pod'u BAŞLATMAZ. Bu basit bir kural birçok saldırıyı önler.

**2. `readOnlyRootFilesystem` — Yazma Engeli:**
Container'ın filesystem'ı salt okunur. Saldırgan sızsa bile dosya yazamaz — malware indiremez, script oluşturamaz, config değiştiremez. "Hırsız eve girdi ama her şey camdan ve hiçbir şeye dokunamıyor." Geçici dosyalar gerekiyorsa `emptyDir` volume mount edin, geri kalan her yer kilitli.

**3. `capabilities: drop: ALL` — Kernel Yetkilerini Kapat:**
Linux capabilities, root yetkisini küçük parçalara böler (network yönetimi, dosya sahipliği değiştirme, raw socket açma vs.). `drop: ALL` dediğinizde TÜM bu yetkileri kaldırırsınız. Container'ın kernel ile iletişimi minimuma iner. Gerçekten gerekli bir capability varsa (nadiren), sadece onu geri eklersiniz.

**4. Network Policies + RBAC + Pod Security = Derinlemesine Savunma:**
- **Network Policies:** Pod'lar arası trafiği kısıtlar — "sadece frontend pod'u backend pod'la konuşabilir, başka hiçbir pod konuşamaz"
- **RBAC:** Kim hangi Kubernetes API'sine erişebilir — "developer sadece kendi namespace'inde pod görebilir"
- **Pod Security Standards:** Cluster seviyesinde güvenlik politikaları — "bu namespace'te privileged container YASAKLANMIŞTIR"

Bu üçlü bir arada çalıştığında, bir katman aşılsa bile diğerleri sizi korur. Kalenin surları, hendeği ve nöbetçileri gibi.

```yaml
securityContext:
  # Run as non-root
  runAsNonRoot: true
  runAsUser: 1000
  # Read-only filesystem
  readOnlyRootFilesystem: true
  # Drop capabilities
  capabilities:
    drop:
      - ALL
```

**✅ Altın Kural:** Varsayılan olarak HER ŞEYİ kısıtlayın, sadece gerçekten gerekeni açın. Güvenlikte "beyaz liste" yaklaşımı her zaman "kara liste"den üstündür.

#### 4. Pod Disruption Budget

**PDB Nedir? — Hastane Acil Servisi Kuralı**

Bir hastane acil servisinde **minimum personel kuralı** vardır: "Her zaman en az 2 doktor görevde olmalı." Bir doktor izne çıkmak isterse, ancak 3. doktor varsa izin verilir. 2 doktor kaldıysa, kimse ayrılamaz — hasta güvenliği her şeyden önemli.

Pod Disruption Budget (PDB) tam olarak bu kuralı Kubernetes'e uygular: "Bu servisten her zaman en az N pod ayakta olmalı. Kim ne yaparsa yapsın — node upgrade, cluster autoscaler, rolling update — bu sayının altına DÜŞEMEZSİN."

**Neden İhtiyacımız Var?**

Kubernetes'te pod'larınızı öldürebilecek birçok "meşru" senaryo var:
- **Node Drain:** Cluster yöneticisi bir node'u bakıma alıyor → o node'daki tüm pod'lar tahliye edilir
- **Cluster Autoscaler:** Kaynak tasarrufu için boş node'ları kapatıyor → pod'lar başka yere taşınır
- **Rolling Update:** Yeni deployment çıktığında eski pod'lar yavaş yavaş öldürülür
- **Spot Instance Reclaim:** AWS spot instance'ı geri alıyor → node aniden kapanır

PDB OLMADAN ne olur? Cluster upgrade sırasında Kubernetes "hadi şu 3 node'u aynı anda drain edelim" diyebilir. Eğer servisinizin 4 pod'u bu 3 node'da dağılmışsa → aynı anda 3 pod ölür → sadece 1 pod kalır → o pod tüm trafiği almaya çalışır → o da patlar → **DOWNTIME!** Gece 3'te pager çalar. 😱

**`minAvailable` vs `maxUnavailable` — Aynı Madalyonun İki Yüzü:**

5 pod'unuz varsa:
- `minAvailable: 3` → "En az 3 pod her zaman çalışmalı" → aynı anda en fazla 2 pod öldürülebilir
- `maxUnavailable: 2` → "Aynı anda en fazla 2 pod unavailable olabilir" → aynı anda en az 3 pod çalışmalı

İkisi de aynı sonucu verir! Hangisini kullanacağınız tercihe bağlı. `minAvailable` daha sezgiseldir: "Bu servisten en az kaç tane lazım?" sorusunun cevabı. Yüzde de kullanabilirsiniz: `minAvailable: 50%`.

**🏆 Gerçek Dünya:**
"PDB hayatımızı kurtardı. Node upgrade'i sırasında `minAvailable: 2` koymuştuk. Kubernetes iki node'u aynı anda drain etmeye çalıştı ama PDB izin vermedi — önce bir node drain edildi, pod'lar başka node'a taşındı, sonra ikinci node drain edildi. Servisimiz hiç kesintiye uğramadı. PDB'siz olsa 3 dakika downtime yaşayacaktık — bu da SLA ihlali ve $10K ceza demekti."

⚠️ **Dikkat:** `minAvailable`'ı toplam replica sayısına eşit yaparsanız (örn: 3 replica, `minAvailable: 3`), hiçbir pod asla drain edilemez → node upgrade'leri SONSUZA DEK bekler. Bu bir deadlock'tur!

```yaml
# Ensure availability during updates
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: web
```

### Managed Kubernetes Options

**AWS EKS:**
```bash
# Create cluster
eksctl create cluster \
  --name my-cluster \
  --region us-east-1 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 3 \
  --nodes-min 1 \
  --nodes-max 4

# Update kubeconfig
aws eks update-kubeconfig --name my-cluster --region us-east-1
```

**GKE (Google):**
- Auto-pilot mode (fully managed)
- Advanced networking
- Integrated monitoring

**AKS (Azure):**
- Azure integration
- Virtual nodes (serverless containers)

### Kubernetes Monitoring

Kubernetes cluster'ınızı monitoring'siz çalıştırmak, gözleri bağlı araba kullanmak gibidir. 🚗 "Her şey çalışıyor" diye düşünürsünüz — ta ki birisi "site çöktü!" diye bağırana kadar. O zaman panikle `kubectl get pods` yazarsınız, 47 tane `CrashLoopBackOff` görürsünüz ve "bu ne zaman başladı?" diye sorarsınız. Kimse bilmez. Çünkü monitoring yoktu.

**K8s Monitoring Ne Kapsar?**

Kubernetes monitoring'i dört katmandan oluşur — her biri farklı bir soruyu cevaplar:

| Katman | Ne İzlenir? | Soru |
|--------|------------|------|
| **Cluster Health** | Node durumları, API Server responsivity | "Altyapı sağlam mı?" |
| **Node Resources** | CPU, memory, disk, network per node | "Makineler yeterli mi?" |
| **Pod/Container Status** | Pod phase, restart count, OOMKill | "Uygulamalar yaşıyor mu?" |
| **Application Metrics** | Request rate, error rate, latency (RED) | "Kullanıcılar etkileniyor mu?" |

Bu dört katmanı izlemezseniz, sorunları ancak KULLANICI şikayet ettiğinde öğrenirsiniz. Ve o noktada zaten çok geç.

**Prometheus + Grafana: Kubernetes'in Standart Monitoring Stack'i**

Kubernetes monitoring dendiğinde ilk akla gelen ikili: **Prometheus** (veri toplama ve saklama) + **Grafana** (görselleştirme). Bu ikili, Kubernetes dünyasının "Batman ve Robin"idir — birlikte müthiş güçlüler. 🦇

- **Prometheus:** Pull-based metric collection. Her X saniyede (genelde 15-30s) servislerinizin `/metrics` endpoint'inden veri çeker. TSDB (Time Series Database) ile saklar. PromQL sorgu diliyle analiz yaparsınız.
- **Grafana:** Prometheus'tan verileri çekip güzel dashboard'lar oluşturur. Grafikler, gauge'lar, heatmap'ler. Ekip odasındaki büyük TV'ye Grafana dashboard'unu yansıtırsınız — herkes cluster'ın nabzını görür.
- **AlertManager:** Prometheus'un alarm sistemi. Belirlediğiniz eşikler aşıldığında Slack'e, PagerDuty'ye, e-mail'e alarm gönderir.

Kurulum? `helm install prometheus prometheus-community/kube-prometheus-stack` — TEK KOMUT ile Prometheus, Grafana, AlertManager, node-exporter, kube-state-metrics HEPSİ kurulur. Eskiden günlerce YAML yazardınız. Helm ile 2 dakika. ☕

**kube-state-metrics: Kubernetes Objelerinin Röntgeni**

kube-state-metrics, Kubernetes API'dan obje durumlarını metric olarak expose eder. Pod'lar, Deployment'lar, Node'lar, Job'lar hakkında detaylı bilgi verir:

- `kube_pod_status_phase` → Pod hangi phase'de? (Running, Pending, Failed, Succeeded)
- `kube_deployment_spec_replicas` → Kaç replica isteniyor vs kaç tane hazır?
- `kube_node_status_condition` → Node Ready mi, MemoryPressure var mı?
- `kube_pod_container_status_restarts_total` → Container kaç kez restart oldu? (Çok yüksekse CrashLoopBackOff uyarısı!)

Bu metric'ler olmadan, cluster'ınızda kaç pod'un `Pending` durumda olduğunu bilmezsiniz. Pending pod demek = schedule edilememiş pod = resource yetersizliği = kullanıcılarınız 503 alıyor olabilir.

**node-exporter: Makinelerin Sağlık Raporu**

node-exporter her node üzerinde çalışır ve host-level metric'leri expose eder:
- **CPU:** Kullanım oranı, idle time, iowait (disk bekleyen CPU süresi)
- **Memory:** Used, available, cache, swap kullanımı
- **Disk:** I/O throughput, disk kullanım yüzdesi, inode kullanımı
- **Network:** Bytes in/out, packet drop'lar, connection count

⚠️ Disk dolma en sinsi sorundur. CPU ve memory alarmları herkes kurar, ama disk? Container log'ları birikir, emptyDir volume'lar şişer, bir gün node'un diski %100 olur ve kubelet pod'ları **evict** etmeye başlar. Tüm pod'larınız birden farklı node'lara taşınır, rebalancing kaosun eşiğine gelir. node-exporter ile disk kullanımını izleyin, %80'de alarm kurun.

**Key Dashboards — Grafana'da Olmazsa Olmazlar:**

1. **Cluster Overview:** Node sayısı, toplam CPU/memory kapasitesi vs kullanım, pod count
2. **Namespace Resource Usage:** Her namespace ne kadar kaynak tüketiyor? (Hangi takım çok yiyor?)
3. **Pod Lifecycle:** Restart count, OOMKill sayısı, pod age, CrashLoopBackOff'lar
4. **Network Dashboard:** Inter-pod trafik, ingress throughput, DNS query latency
5. **Persistent Volume:** PVC usage percentage — dolmadan ÖNCE alarma geçin

Grafana Labs'ın hazır dashboard kataloğu var (grafana.com/grafana/dashboards). Dashboard ID'yi import edersiniz, 30 saniyede production-ready dashboard'unuz hazır. Tekerleği yeniden icat etmeyin. 🎨

**🚨 Kritik Alarmlar — Bunları MUTLAKA Kurun:**

```yaml
# AlertManager rule örnekleri
groups:
  - name: kubernetes-critical
    rules:
      # Pod CrashLoopBackOff — uygulama sürekli çöküp restart oluyor
      - alert: PodCrashLoopBackOff
        expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Pod {{ $labels.pod }} sürekli restart oluyor!"

      # Node NotReady — makine cevap vermiyor
      - alert: NodeNotReady
        expr: kube_node_status_condition{condition="Ready",status="true"} == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Node {{ $labels.node }} NotReady durumda!"

      # Yüksek CPU kullanımı
      - alert: HighCPUUsage
        expr: (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)) > 0.85
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Node {{ $labels.instance }} CPU %85 üzerinde!"

      # Yüksek Memory kullanımı
      - alert: HighMemoryUsage
        expr: (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) > 0.90
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Node {{ $labels.instance }} memory %90 üzerinde! OOMKill riski!"

      # PVC disk dolma uyarısı
      - alert: PVCAlmostFull
        expr: kubelet_volume_stats_used_bytes / kubelet_volume_stats_capacity_bytes > 0.85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "PVC {{ $labels.persistentvolumeclaim }} %85 dolu!"
```

Bu alarmları kurmak 30 dakikanızı alır, ama gece 3'te sizi UYANDIRARAK 3 saatlik bir incident'ı 5 dakikaya indirir. Alarm kurmamak, yangın alarmı olmayan binada çalışmak gibidir — yangın çıkana kadar rahat, çıkınca felaket. 🔥

```yaml
# Prometheus & Grafana
# ServiceMonitor for custom metrics
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-metrics
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
  - port: metrics
    interval: 30s
```

**kubectl Commands — Hızlı Monitoring Komutları:**

Grafana harika ama bazen terminalde hızlı bir bakış yeterlidir. Şu `kubectl` komutlarını ezbere bilin:

```bash
# Get cluster info
kubectl cluster-info
kubectl get nodes -o wide   # Node'ların IP, OS, kernel bilgisi

# Pod management
kubectl get pods -A          # TÜM namespace'lerdeki pod'lar
kubectl get pods --field-selector=status.phase!=Running  # Sorunlu pod'lar!
kubectl describe pod <pod-name>    # Pod detayı — Events kısmına BAKIN!
kubectl logs <pod-name> -f          # Canlı log takibi
kubectl logs <pod-name> --previous  # ÖNCEKI container'ın logları (crash sonrası işe yarar)
kubectl exec -it <pod-name> -- /bin/bash  # Pod'un içine gir

# Debugging — ALTIN komutlar
kubectl top nodes             # Node CPU/memory kullanımı (metrics-server gerekli)
kubectl top pods --sort-by=cpu    # En çok CPU yiyen pod'lar
kubectl top pods --sort-by=memory # En çok memory yiyen pod'lar
kubectl get events --sort-by='.lastTimestamp' -A  # Son olaylar — sorun tespiti için İLK bakılacak yer

# Port forwarding — local debug
kubectl port-forward pod/myapp-123 8080:8080
kubectl port-forward svc/grafana 3000:80  # Grafana'ya local erişim

# Copy files
kubectl cp <pod-name>:/path/to/file ./local-file
```

💡 **Pro Tip:** `kubectl top pods --sort-by=memory` komutuyla memory leak'li pod'ları hemen tespit edebilirsiniz. Memory sürekli artıp hiç düşmüyorsa → leak var, restart gerekebilir ama ASIL NEDEN araştırılmalı.

### Infrastructure as Code (IaC)

Bir düşünün: IKEA'dan dolap aldınız. Elinizde montaj kılavuzu var — adım adım, hangi vidayı nereye takacağınız yazıyor. Bu kılavuzu 100 kişiye verseniz, 100'ü de BİREBİR aynı dolabı yapar. İşte Infrastructure as Code tam olarak bu. Altyapınızı elle tıklayarak değil, KOD YAZARAK tanımlıyorsunuz.

**IaC olmadan ne oluyor?** Birisi AWS Console'a giriyor, "Launch Instance" tıklıyor, security group'u elle ayarlıyor, 3 gün sonra aynı şeyi yapmaya çalışıyor ama hangi ayarları seçtiğini hatırlamıyor. Sonuç: **Snowflake Servers** — her biri eşsiz, hiçbiri birbirine benzemeyen, kimsenin tam olarak nasıl yapıldığını bilmediği sunucular. Birisi "production server'ı kim kurdu?" diye sorduğunda herkes birbirine bakıyor. O kişi şirketten ayrılmış, bilgi de onunla gitmiş. 😱

**Declarative vs Imperative — İki Felsefi Yaklaşım:**

Burada temel bir ayrım var:
- **Declarative (Bildirimsel):** "3 tane server OLSUN" diyorsun. Nasıl yapılacağı senin sorunun değil. Terraform böyle çalışır. Hedef durumu tanımlarsın, araç mevcut durumla karşılaştırır ve farkı kapatır.
- **Imperative (Buyurgan):** "Bir server oluştur, sonra bir tane daha, sonra bir tane daha" diyorsun. Adım adım talimat verirsin. Ansible daha çok bu tarza yakındır.

Declarative yaklaşımın güzelliği: 3 server'ın var, yanlışlıkla birini sildin. Terraform'u tekrar çalıştırıyorsun, eksik olan 1 server'ı oluşturuyor. Imperative olsaydı? 3 tane daha oluşturur, toplamda 5 olurdu. 🤦

#### Terraform

Terraform, HashiCorp tarafından geliştirilmiş, şu anda **dünyanın en popüler IaC aracıdır**. AWS, Azure, GCP, Cloudflare, Datadog — neredeyse her cloud provider ile çalışır.

**Neden Kullanılır:**
- **Declarative infrastructure tanımı:** Ne istediğini yazarsın, Terraform nasıl yapacağını bilir
- **Multi-cloud support:** AWS'de başla, yarın GCP'ye geç, aynı mantık
- **State management:** Neyin var olduğunu takip eder
- **Reusable modules:** Kod gibi fonksiyonlar yazarsın, tekrar tekrar kullanırsın
- **Plan before apply:** Değişikliği YAPMADAN ÖNCE ne olacağını görürsün

**Terraform'un Beyni: State File (terraform.tfstate)**

Terraform'un en kritik konsepti state file'dır. Bu dosya, Terraform'un "şu anda ne var" bilgisini tutar. Mesela "us-east-1'de i-0abc123 ID'li bir EC2 instance var" der. Bir sonraki `terraform plan` çalıştığında, kodundaki tanımla state'teki gerçekliği karşılaştırır.

⚠️ **ALTIN KURAL:** State file'ı ASLA silmeyin, ASLA git'e commit etmeyin (içinde secret'lar olabilir). State'i **S3 + DynamoDB** (locking için) ile remote backend'de saklayın. State silindi = Terraform altyapınızı "tanımıyor" = tek tek import etmeniz lazım = geçmiş olsun.

**Terraform Workflow: Plan → Apply → Destroy**
```bash
# 1. terraform init — provider'ları indir, backend'i konfigüre et
terraform init

# 2. terraform plan — "Ne değişecek?" sorusunun cevabı
#    Hiçbir şey YAPMAZ, sadece GÖSTERIR
terraform plan
# Çıktı: "1 to add, 0 to change, 0 to destroy"

# 3. terraform apply — Gerçekten UYGULA
terraform apply
# "Do you want to perform these actions?" — evet dersen yapar

# 4. terraform destroy — Her şeyi YOK ET (dikkat!)
terraform destroy
```

**Modules: Tekrar Kullanılabilir Yapı Taşları**

Modüller Terraform'daki fonksiyonlar gibidir. Bir kere "VPC oluştur" modülü yazarsın, her projede çağırırsın:
```hcl
# Ana config — modül çağrısı
module "vpc" {
  source = "./modules/vpc"
  cidr   = "10.0.0.0/16"
  env    = "production"
}

module "web_server" {
  source        = "./modules/ec2"
  instance_type = "t3.micro"
  vpc_id        = module.vpc.vpc_id
  subnet_id     = module.vpc.public_subnet_id
}
```

```hcl
# Terraform örneği — basit bir altyapı tanımı
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  
  tags = {
    Name = "WebServer"
    Environment = "Production"
  }
}

resource "aws_s3_bucket" "data" {
  bucket = "my-company-data"
  
  versioning {
    enabled = true
  }
}

# Remote state backend — MUTLAKA kullanın
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

**🎯 Gerçek Hayat Hikayesi:** Bir gece vakti, bir mühendis yanlışlıkla production RDS instance'ını sildi. Panik, ter, kalp çarpıntısı... Ama altyapı Terraform ile yönetiliyordu. `terraform apply` çalıştırdılar — 5 dakika içinde yeni RDS instance ayağa kalktı, backup'tan restore edildi. Terraform olmasaydı? AWS Console'da saatlerce "hangi ayardı, hangi VPC'deydi, security group hangisiydi" diye uğraşacaklardı. IaC hayat kurtarır — bazen kelimenin tam anlamıyla.

#### CloudFormation
- AWS native IaC
- JSON/YAML templates
- Stack management

#### CDK (Cloud Development Kit)
- Code ile infrastructure (TypeScript, Python, Java)
- Daha programmatic approach

### CI/CD Pipeline

Bir fabrikadaki montaj hattını düşünün: ham madde bir ucundan girer, kalite kontrol noktalarından geçer, paketlenir ve rafta yerini alır. İşçiler her seferinde aynı adımları, aynı sırayla, aynı kalitede uygular. İşte CI/CD tam olarak bu — kodunuz için otomatik bir montaj hattı.

**CI/CD olmadan deployment nasıl oluyor?** Cuma saat 17:00, herkes eve gitmek istiyor ama "deploy günü" gelmiş. Ali FTP ile dosyaları sunucuya yüklüyor (evet, hâlâ FTP kullanan yerler var). Ama server'daki config dosyası farklı, Ali'nin local'inde çalışan kod production'da çalışmıyor. 4 saat debug, 3 kişi weekend'i feda ediyor. "Works on my machine" dünyanın en tehlikeli cümlesidir.

**CI — Continuous Integration (Sürekli Entegrasyon):**
Geliştiriciler kodlarını SIKÇA (günde birkaç kez) ana branch'e merge eder. Her merge'de otomatik olarak:
- Kod derlenir (build)
- Unit test'ler çalışır
- Lint/format kontrolleri yapılır
- Çakışmalar anında tespit edilir

CI'ın mantığı basit: "Sorunları erken yakala." Bir hafta boyunca ayrı branch'lerde çalışıp Cuma günü merge etmek = merge conflict cehennemi. Her gün merge etmek = küçük, yönetilebilir conflict'ler.

**CD — İki Farklı Anlam:**
- **Continuous Delivery (Sürekli Teslimat):** Kod her zaman deploy EDİLEBİLİR durumda. Ama deploy kararı insana bırakılır ("deploy" butonuna birisi basar).
- **Continuous Deployment (Sürekli Dağıtım):** Tüm testlerden geçen kod OTOMATİK olarak production'a deploy edilir. İnsan müdahalesi yok. Bu cesur bir yaklaşım — test suite'inize %100 güvenmeniz lazım.

**Araç Karşılaştırması:**
| Araç | Avantaj | Dezavantaj |
|------|---------|------------|
| **GitHub Actions** | GitHub ile entegre, marketplace zengin, kolay başlangıç | GitHub'a bağımlılık |
| **GitLab CI/CD** | Güçlü, self-hosted option, built-in container registry | Öğrenme eğrisi dik |
| **Jenkins** | Ultra esnek, 1800+ plugin, legacy projelerde yaygın | UI eski, bakımı zor, "Jenkins admin" ayrı bir meslek |
| **CircleCI** | Hızlı, paralel job'lar, Docker-native | Pricing karmaşık |
| **AWS CodePipeline** | AWS native, diğer AWS servisleriyle sorunsuz entegrasyon | AWS dışı projeler için zayıf |

**Pipeline as Code — Pipeline'ı da Versiyon Kontrolüne Al:**
Pipeline tanımı repo'nun içinde yaşar (`.gitlab-ci.yml`, `.github/workflows/deploy.yml`). Bu sayede:
- Pipeline değişiklikleri code review'dan geçer
- Eski pipeline versiyonuna geri dönebilirsin
- Her branch kendi pipeline'ını override edebilir
- "Pipeline'ı kim değiştirdi?" sorusunun cevabı git log'da

**GitLab CI/CD, GitHub Actions, Jenkins:**
```yaml
# GitLab CI örneği (.gitlab-ci.yml)
stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - npm install
    - npm test

build:
  stage: build
  script:
    - docker build -t my-app .
    - docker push registry/my-app

deploy:
  stage: deploy
  script:
    - terraform apply
    - kubectl apply -f deployment.yaml
```

**Pipeline Stages:**
1. **Source:** Git push trigger
2. **Build:** Compile code, run tests
3. **Test:** Unit, integration, e2e tests
4. **Security Scan:** SAST, DAST, dependency check
5. **Deploy to Staging:** Automatic
6. **Deploy to Production:** Manual approval

**🎯 Gerçek Hayat Hikayesi:** Bir ekip, CI/CD öncesi her deployment'ta 4 saat harcıyordu. 3 kişi koordine oluyordu, Slack'te "ben şimdi deploy ediyorum, kimse commit atmasın" yazılıyordu. CI/CD pipeline kurulduktan sonra? Deployment 15 dakikaya düştü. Kimse fark bile etmiyor — kod merge ediliyor, testler geçiyor, staging'e gidiyor, QA onaylıyor, production'a çıkıyor. Bir keresinde Cuma 16:00'da hotfix çıkardılar ve kimsenin tansiyonu yükselmedi. İşte CI/CD'nin gerçek değeri bu: deployment'ı SIKICI bir olay olmaktan çıkarıp SIRADAN bir rutine dönüştürmek.

---

## ⚡ Event-Driven Architecture

### Message Queues

Bir postane düşünün. Mektubunuzu zarfa koyuyorsunuz, pul yapıştırıyorsunuz, postaneye bırakıyorsunuz. Alıcının evde olup olmadığını bilmiyorsunuz, kapısında beklemiyorsunuz. Postane mektubu depolar, taşır ve alıcı müsait olduğunda teslim eder. İşte message queue tam olarak bu — gönderen (producer) mesajı kuyruğa bırakır ve yoluna devam eder, alıcı (consumer) hazır olduğunda mesajı alır ve işler.

**Neden Queue Kullanırız? — Synchronous vs Asynchronous İletişim:**

REST API ile bir servisi çağırdığında, cevap gelene kadar BEKLERSİN. Karşı servis yavaşsa, sen de yavaşlarsın. Karşı servis çökerse, sen de çökersin. Bu, iki kişinin telefonda konuşması gibi — ikisi de aynı anda müsait OLMAK ZORUNDA.

Message queue ile durum farklı: mesajını bırakır, gidersin. Karşı servis çökmüş olsa bile mesaj kuyrukta BEKLER. Servis ayağa kalktığında mesajı alır ve işler. Bu, mesaj bırakmak gibi — alıcının müsait olmasını beklemeye gerek yok.

**Queue Kullanmanın 3 Büyük Faydası:**
1. **Decoupling (Bağımsızlaştırma):** Service A, Service B'nin varlığını bilmek zorunda değil. Sadece kuyruğa mesaj bırakır.
2. **Load Leveling (Yük Dengeleme):** Black Friday'de saniyede 10.000 sipariş geliyor. Siparişleri kuyruğa at, consumer'lar kendi hızlarında işlesin. Kuyruk BUFFER görevi görür.
3. **Reliability (Güvenilirlik):** Consumer çöktü mü? Mesaj kuyrukta kalır. Mesaj kaybolmaz, sistem dayanıklıdır.

**Mesajlaşma Kalıpları — Queue vs Topic vs Stream:**
| Kalıp | Nasıl Çalışır | Örnek |
|-------|---------------|-------|
| **Queue (Point-to-Point)** | 1 mesaj → 1 consumer. Mesaj işlenince silinir. | SQS, RabbitMQ |
| **Topic (Pub/Sub)** | 1 mesaj → N subscriber. Herkese kopyası gider. | SNS, RabbitMQ Exchange |
| **Stream (Log)** | Mesajlar kalıcı, consumer'lar istedikleri yerden okur. | Kafka, Kinesis |

**Dead Letter Queue (DLQ) — Teslim Edilemeyen Mesajlar Birimi:**

Postanede "alıcı bulunamadı" damgası vurulan mektuplar gibi. Bir mesaj 3 kez işlenmeye çalışıldı ama her seferinde hata aldı mı? O mesaj DLQ'ya gönderilir. Bu sayede:
- Hatalı mesajlar ana kuyruğu tıkamaz
- Sonradan incelenip düzeltilebilir
- Alarm kurarsınız: "DLQ'da 100'den fazla mesaj var" = bir şeyler yanlış gidiyor!

DLQ olmadan ne olur? Hatalı mesaj sürekli retry edilir, consumer'lar başka mesajları işleyemez, kuyruk şişer, sistem durur. DLQ bir güvenlik supabıdır.

#### SQS (Simple Queue Service)
**Nedir:**
- AWS'nin managed message queue servisi
- Asenkron iletişim için kullanılır

**Ne Zaman Kullanılır:**
```
Senaryolar:
1. Decoupling: Service A ile Service B arasında bağımlılığı azaltmak
2. Load Leveling: Traffic spike'larında buffer görevi
3. Asynchronous Processing: Email gönderme, image processing
```

**Nasıl Çalışır:**
```javascript
// Producer (Mesaj gönderen)
const AWS = require('aws-sdk');
const sqs = new AWS.SQS();

async function sendMessage(orderData) {
  const params = {
    QueueUrl: 'https://sqs.us-east-1.amazonaws.com/123456789012/orders',
    MessageBody: JSON.stringify(orderData),
    MessageAttributes: {
      'OrderType': {
        DataType: 'String',
        StringValue: 'URGENT'
      }
    }
  };
  
  await sqs.sendMessage(params).promise();
}

// Consumer (Mesaj işleyen)
async function receiveMessages() {
  const params = {
    QueueUrl: 'https://sqs.us-east-1.amazonaws.com/123456789012/orders',
    MaxNumberOfMessages: 10,
    WaitTimeSeconds: 20 // Long polling
  };
  
  const data = await sqs.receiveMessage(params).promise();
  
  for (const message of data.Messages) {
    // Process message
    await processOrder(JSON.parse(message.Body));
    
    // Delete from queue
    await sqs.deleteMessage({
      QueueUrl: params.QueueUrl,
      ReceiptHandle: message.ReceiptHandle
    }).promise();
  }
}
```

**SQS Types:**
```
Standard Queue:
- Unlimited throughput
- At-least-once delivery (duplicate olabilir)
- Best-effort ordering (sıra garanti değil)

FIFO Queue:
- Exactly-once processing
- Guaranteed ordering
- 300 msg/sec limit (batching ile 3000)
```

**Advanced Concepts:**
- **DLQ (Dead Letter Queue):** İşlenemeyen mesajlar
- **Visibility Timeout:** Mesaj işlenirken başkaları görmez
- **Message Retention:** 1 dakika - 14 gün arası

#### SNS (Simple Notification Service)
**Nedir:**
- Pub/Sub (Publish-Subscribe) messaging
- Fan-out pattern: 1 event -> multiple subscribers

**SQS vs SNS:**
```
SQS (Queue):
- Pull-based: Consumer mesajları çeker
- 1 consumer per message
- Processing guarantee

SNS (Topic):
- Push-based: Subscribers'a gönderilir
- Multiple subscribers
- Fire-and-forget

Combined Pattern (Fan-out):
SNS Topic
├── SQS Queue 1 (Email service)
├── SQS Queue 2 (SMS service)
└── Lambda (Logging)
```

**Örnek Kullanım:**
```javascript
// SNS ile multiple services'e notify
const sns = new AWS.SNS();

async function publishEvent(event) {
  await sns.publish({
    TopicArn: 'arn:aws:sns:us-east-1:123456789012:order-events',
    Message: JSON.stringify({
      eventType: 'OrderCreated',
      orderId: '12345',
      timestamp: Date.now()
    })
  }).promise();
}
```

#### Kafka (Apache Kafka)

Kafka'yı anlamak için önce şunu bilin: Kafka bir message queue DEĞİLDİR. Kafka bir **distributed commit log**'dur — yani dağıtık, append-only bir kayıt defteridir. Bu fark çok önemli.

Geleneksel queue'larda (SQS, RabbitMQ) mesaj okunduğunda kuyruktan SİLİNİR. Kafka'da ise mesajlar **KALICI**dır. Consumer mesajı okudu diye mesaj kaybolmaz. Bir kitabı okuduğunuzda sayfalar yırtılıp atılmaz — sadece siz hangi sayfada olduğunuzu hatırlarsınız. Kafka'daki offset kavramı tam olarak budur.

Kafka'yı LinkedIn yarattı. Neden? Çünkü 2010'ların başında LinkedIn'in günde milyarlarca event'i vardı (profil görüntüleme, iş başvurusu, mesaj, bildirim...) ve mevcut mesajlaşma sistemleri bu yüke dayanamıyordu. Bugün LinkedIn'in Kafka altyapısı günde **7 TRİLYON mesaj** işliyor. Evet, trilyon.

**Nedir:**
- Distributed streaming platform — dağıtık bir akış platformu
- High-throughput, low-latency — saniyede milyonlarca mesaj, milisaniye gecikme
- Event sourcing & stream processing — olayları kaydedip gerçek zamanlı analiz

**Kafka vs Geleneksel Queue'lar — Temel Fark:**
```
Geleneksel Queue (SQS, RabbitMQ):
- Mesaj okundu → SİLİNDİ
- 1 mesaj → 1 consumer
- "Postane" modeli: mektup teslim edildi, bitti

Kafka:
- Mesaj okundu → HÂLÂ DURUYOR (retention period boyunca)
- Aynı mesaj birden fazla consumer group tarafından okunabilir
- Consumer'lar geçmişe gidip mesajları TEKRAR okuyabilir (replay!)
- "Kütüphane" modeli: kitaplar rafta durur, herkes okuyabilir
```

Bu replay özelliği altın değerinde. Diyelim yeni bir analytics servisi yazdınız. Geleneksel queue'da "geçmiş 1 haftanın event'lerini tekrar işle" diyemezsiniz — onlar çoktan silindi. Kafka'da? Consumer offset'ini 1 hafta geriye alır, tüm event'leri tekrar işlersiniz. Sıfırdan veri migrationları bu sayede mümkün.

**Partition = Paralellik:**

Bir topic'i birden fazla partition'a bölersiniz. Her partition bağımsız bir log'dur. Neden? Çünkü:
- 1 partition = 1 consumer thread. 10 partition = 10 consumer thread = 10 kat throughput!
- Mesajlar key'e göre partition'lara dağıtılır. Aynı key her zaman aynı partition'a gider → sıralama GARANTİ.
- Örnek: `userId` key'i kullanırsanız, aynı user'ın tüm event'leri aynı partition'da, doğru sırada olur.

**Consumer Groups:**

Bir consumer group içinde her partition SADECE bir consumer'a atanır. Bu kritik bir kural:
- 6 partition, 3 consumer → her consumer 2 partition okur ✅
- 6 partition, 6 consumer → her consumer 1 partition okur ✅ (ideal)
- 6 partition, 8 consumer → 2 consumer BOŞ durur ❌ (partition sayısından fazla consumer = israf)

Farklı consumer group'lar ise AYNI mesajları bağımsız olarak okuyabilir. "order-service" group'u ve "analytics-service" group'u aynı topic'ten okur, birbirini etkilemez.

**Offset — "Nerede Kaldım?":**

Her consumer, her partition için "en son hangi mesajı okudum" bilgisini (offset) saklar. Bu offset Kafka'nın kendisinde (`__consumer_offsets` topic) tutulur. Consumer çökerse, yeniden başladığında kaldığı yerden devam eder. Manuel offset yönetimi de yapabilirsiniz: `earliest` (en baştan oku), `latest` (sadece yeni mesajları oku).

**Ne Zaman SQS Yerine Kafka:**
```
SQS kullan:
- Simple use cases
- AWS native integration
- Managed service (zero ops)
- Düşük-orta throughput yeterli

Kafka kullan:
- Very high throughput (millions msg/sec)
- Event sourcing (messages kalıcı, replay gerekli)
- Stream processing (real-time analytics)
- Multi-subscriber patterns (aynı event birden fazla servis tarafından okunacak)
- Ordering guarantee gerekli (partition bazında)
```

**Kafka Concepts (Özet):**
```
Broker: Kafka cluster'daki sunucu (genelde 3-5 broker)
Topic: Message category ("user-events", "order-events")
Partition: Topic'in bölümleri (parallelism & ordering unit)
Producer: Mesaj gönderen uygulama
Consumer Group: Mesajları paylaşarak okuyan consumer'lar topluluğu
Offset: Consumer'ın her partition'da okuduğu pozisyon
Replication Factor: Her partition'ın kaç kopyası var (genelde 3)
ISR (In-Sync Replicas): Güncel kopyalar — leader çökerse birisi devralır
```

**Kafka Example:**
```javascript
// Producer
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['kafka1:9092', 'kafka2:9092']
});

const producer = kafka.producer();

await producer.connect();
await producer.send({
  topic: 'user-events',
  messages: [
    { 
      key: 'user123',
      value: JSON.stringify({ event: 'signup', userId: 'user123' })
    }
  ]
});

// Consumer
const consumer = kafka.consumer({ groupId: 'email-service' });

await consumer.connect();
await consumer.subscribe({ topic: 'user-events' });

await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    const event = JSON.parse(message.value.toString());
    await sendWelcomeEmail(event.userId);
  }
});
```

**Managed Kafka Options:**
- **AWS MSK (Managed Streaming for Kafka)**
- **Confluent Cloud**
- **Azure Event Hubs**

### Cron Jobs & Scheduled Tasks

Cron job'lar, yazılım dünyasının **çalar saatleridir** — bir kez kurarsınız, belirlenen saatte otomatik olarak çalışırlar. ⏰

**Nereden Geliyor?**

Cron, Unix dünyasının en eski araçlarından biridir (1975'ten beri var!). Adı "chronos" (Yunanca "zaman") kelimesinden gelir. 50 yıldan fazladır aynı mantıkla çalışıyor — ve hâlâ HER yerde kullanılıyor.

**Cron Expression — 5 Yıldızın Gücü:**

Cron ifadesi 5 alandan oluşur ve her biri bir zaman birimini temsil eder:

```
┌───────────── dakika (0-59)
│ ┌───────────── saat (0-23)
│ │ ┌───────────── ayın günü (1-31)
│ │ │ ┌───────────── ay (1-12)
│ │ │ │ ┌───────────── haftanın günü (0-7, 0 ve 7 = Pazar)
│ │ │ │ │
* * * * *
```

**Örnekler:**
- `*/5 * * * *` → Her 5 dakikada bir (health check, cache refresh)
- `0 * * * *` → Her saat başı (metrik toplama)
- `0 2 * * *` → Her gece 02:00'de (database backup)
- `0 8 * * 1` → Her Pazartesi sabah 08:00'de (haftalık rapor)
- `0 0 1 * *` → Her ayın 1'inde gece yarısı (aylık fatura oluşturma)
- `0 9 * * 1-5` → Hafta içi her gün 09:00'da (iş günü bildirimleri)

**Kullanım Alanları — Her SaaS Ürününün İhtiyacı:**
- 🗑️ **Database Cleanup:** Eski log'ları, soft-deleted kayıtları, expired session'ları temizle
- 📊 **Rapor Oluşturma:** Günlük satış raporu, haftalık kullanıcı analizi, aylık fatura
- 🔥 **Cache Warming:** Popüler verileri önceden cache'e yükle (sabah 06:00'da, kullanıcılar uyanmadan önce)
- 📧 **Digest Email'ler:** Haftalık özet maili, günlük bildirim derlemesi
- 🔄 **Data Sync:** Harici API'lerden veri çekme (döviz kurları, hava durumu, stok bilgisi)
- 🏥 **Health Check:** Servislerin ayakta olup olmadığını kontrol etme

**⚠️ Dağıtık Sistemlerde Cron — Büyük Tuzak:**

Tek bir sunucuda cron job harika çalışır. Ama ya 10 sunucunuz varsa? Cron job 10 sunucunun HEPSİNDE çalışır! Günlük rapor 10 kez oluşturulur, temizlik script'i 10 kez çalışır, fatura 10 kez kesilir. 😱 Bu sorunu çözmek için **leader election** gerekir: sunucular arasında BİR tanesi "lider" seçilir ve cron job SADECE lider üzerinde çalışır. Araçlar: Redis lock, DynamoDB lock, Consul lock, veya K8s CronJob (K8s bunu otomatik yapar — sadece bir Pod oluşturur).

**K8s CronJob vs EventBridge+Lambda:**

| Özellik | K8s CronJob | EventBridge+Lambda |
|---------|-------------|--------------------|
| **Yaklaşım** | Container-based | Serverless |
| **Başlangıç süresi** | Pod ayağa kalkma (~5-30sn) | Cold start (~100ms-3sn) |
| **Maksimum çalışma** | Sınırsız | 15 dakika (Lambda limiti) |
| **Maliyet** | Cluster maliyeti (sürekli) | Sadece çalıştığında öde |
| **Long-running tasks** | ✅ Saatler süren job'lar OK | ❌ 15dk limiti var |
| **Basit scheduled tasks** | Biraz fazla altyapı | ✅ Mükemmel |

**Gerçek Dünya:** Her SaaS ürünün scheduled job'lara ihtiyacı vardır — Stripe aylık fatura keser, Netflix günlük izleme raporları oluşturur, Slack haftalık workspace analizi gönderir, GitHub günlük contribution grafiğini günceller. Eğer bir ürün inşa ediyorsanız, er ya da geç bir cron job yazacaksınız. 📅

#### EventBridge (CloudWatch Events)
**Nedir:**
- AWS'nin event bus servisi
- Scheduled events (cron) + event-driven triggers

**Cron Expression:**
```
# EventBridge cron syntax
cron(0 10 * * ? *)  # Her gün 10:00'da
cron(0/15 * * * ? *)  # Her 15 dakikada
cron(0 0 1 * ? *)  # Her ayın 1'inde
```

**Lambda ile Cron:**
```javascript
// Serverless Framework kullanarak
functions:
  dailyReport:
    handler: handlers/reports.generate
    events:
      - schedule:
          rate: cron(0 8 * * ? *)  # Her sabah 8:00
          enabled: true
          
  cleanupOldData:
    handler: handlers/cleanup.run
    events:
      - schedule:
          rate: rate(7 days)  # Her 7 günde
```

**Alternative: ECS Scheduled Tasks**
- Container-based cron jobs
- Long-running tasks için daha uygun
- Resource control (CPU, memory)

#### Kubernetes CronJobs
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: "0 2 * * *"  # Her gece 02:00
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: backup-script:latest
            command: ["node", "backup.js"]
          restartPolicy: OnFailure
```

---

## 🔗 Microservices & Distributed Systems

### Microservices Architecture

**Monolith vs Microservices:**
```
Monolith:
✓ Basit deployment
✓ Kolay development (başlangıçta)
✗ Scaling zor
✗ Technology lock-in
✗ Büyük takımlarda koordinasyon zor

Microservices:
✓ Independent deployment
✓ Technology diversity
✓ Team autonomy
✓ Granular scaling
✗ Complexity (network, deployment)
✗ Data consistency challenges
✗ Monitoring & debugging zor
```

**When to Use Microservices:**
- Büyük takım (>20 developer)
- Farklı scaling ihtiyaçları
- Farklı technology stack'ler
- Rapid deployment cycles

### Service Communication

Microservice'ler bağımsız yaşar ama birbirleriyle KONUŞMAk zorundadır. Ve bu konuşma biçimi, sisteminizin dayanıklılığını, performansını ve complexity'sini doğrudan belirler. İki temel model var: arayıp cevap beklemek (synchronous) veya mesaj bırakıp gitmek (asynchronous).

**Synchronous vs Asynchronous — Trade-off'lar:**

| Özellik | Synchronous (REST/gRPC) | Asynchronous (Event/Queue) |
|---------|------------------------|---------------------------|
| **Hız** | Anında cevap (ms) | Gecikmeli işleme (ms-sn) |
| **Coupling** | Sıkı — karşı servis ayakta OLMALI | Gevşek — kuyruk araya girer |
| **Hata Yayılımı** | Yüksek — biri çökerse çağıran da çöker | Düşük — mesaj kuyrukta bekler |
| **Debug** | Kolay — request/response takip edilir | Zor — event'ler asenkron akar |
| **Kullanım** | Anında cevap gereken işler (kullanıcı bilgisi getir) | Arka plan işler (email gönder, rapor oluştur) |

**Savunma Üçlüsü: Timeout + Retry + Exponential Backoff:**

Synchronous iletişimde 3 mekanizma OLMAZSA OLMAZ:

1. **Timeout:** Her dış çağrıya bir süre limiti koy. Payment servisi 30 saniye cevap vermezse, sonsuza kadar bekleme! `axios.get(url, { timeout: 5000 })` — 5 saniyede cevap gelmezse kes.

2. **Retry:** İlk denemede hata aldın mı? Tekrar dene. Ama kaç kez? Sonsuz değil — genelde 3 retry yeterli.

3. **Exponential Backoff:** Retry'lar arasında giderek artan bekleme süreleri koy. 1s → 2s → 4s → 8s. Neden? Karşı servis zaten yük altında olabilir — anında 1000 retry göndermek yangına benzin dökmek olur.

```javascript
// Exponential backoff ile retry örneği
async function callWithRetry(fn, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === maxRetries - 1) throw error;
      const delay = Math.pow(2, attempt) * 1000; // 1s, 2s, 4s
      const jitter = Math.random() * 1000; // Random jitter ekle
      await new Promise(r => setTimeout(r, delay + jitter));
    }
  }
}
```

**Circuit Breaker — Otomatik Sigorta:**

Evinizde elektrik sigortası vardır. Aşırı akım olduğunda sigorta ATAR ve tüm evi korur. Circuit breaker aynı mantık:
- **CLOSED (Normal):** İstekler geçer.
- **OPEN (Sigorta attı):** Karşı servise istek GÖNDERİLMEZ, anında hata döner. Bu sayede timeout beklemezsin.
- **HALF-OPEN (Test):** Belli süre sonra bir deneme isteği gönderilir. Başarılıysa CLOSED'a döner.

```
 Payment Service'e 5/10 istek başarısız
            ↓
 Circuit OPEN — "Payment servisi çökmüş, boşuna deneme"
            ↓ (30 saniye bekle)
 Circuit HALF-OPEN — "Bir deneyelim bakalım"
            ↓
 Başarılı → CLOSED (normal akış)
 Başarısız → OPEN (bir 30 saniye daha bekle)
```

Circuit breaker olmazsa ne olur? Payment servisi çöker → Order servisi payment'ı bekler (timeout) → Order servisi thread'leri tükenir → Order servisi de çöker → Frontend çöker → **Cascading Failure!** Bir domino taşı TÜM sistemi yıkar.

**Event-Driven Architecture — Olaylara Dayalı Mimari:**

Servisler birbirini doğrudan ÇAĞIRMAK yerine, olan biteni "olay" olarak DUYURUR. "Sipariş oluşturuldu" olayını yayınlarsın — kim ilgiliyse o dinler. Yeni bir servis mi eklendi? Mevcut servisleri DEĞİŞTİRMEDEN sadece event'e subscribe olur.

**Choreography vs Orchestration:**

- **Choreography (Koreografi):** Her servis ne zaman ne yapacağını BİLİR. Merkezi kontrol yok. Servisler event'lere react eder. Dans gibi — herkes kendi adımlarını bilir.
  - ✅ Düşük coupling, kolay ölçekleme
  - ❌ Akışı takip etmek zor, debug kabus

- **Orchestration (Orkestrasyon):** Merkezi bir "orkestra şefi" (saga coordinator) tüm adımları yönetir. "Önce stok azalt, sonra ödeme al, sonra kargo başlat."
  - ✅ Akış net, debug kolay
  - ❌ Orchestrator single point of failure olabilir

```
Choreography:                         Orchestration:
OrderCreated event →                  Orchestrator:
  ├─ InventoryService (stok azalt)      1. InventoryService.reserve()
  ├─ PaymentService (ödeme al)          2. PaymentService.charge()
  └─ NotificationService (email at)     3. NotificationService.notify()
                                        4. Hata? → Compensating transactions
```

**🎯 Gerçek Hayat: Netflix'in Microservice Mimarisi:**
Netflix 700'den fazla microservice çalıştırıyor. Neredeyse tamamı asenkron event-driven. Bir kullanıcı "Play" butonuna bastığında arka planda 10+ servis devreye giriyor: authentication, profile, recommendation, streaming, CDN routing, billing, analytics... Bunların hepsi birbirini doğrudan çağırsa, bir tanesinin çökmesi TÜM Netflix'i çökertir. Event-driven + circuit breaker ile bir servis çökse bile diğerleri çalışmaya devam eder. Netflix, kendi altyapısında kasten sunucu çökerten bir araç bile geliştirdi: **Chaos Monkey**. "Eğer production'da rastgele sunucu ölünce sistem çöküyorsa, tasarımınız yanlış" felsefesi.

#### Synchronous (Request-Response)

**REST APIs:**
```javascript
// API Gateway pattern
const express = require('express');
const axios = require('axios');

app.get('/orders/:id', async (req, res) => {
  // Call multiple services
  const [order, user, inventory] = await Promise.all([
    axios.get(`${ORDER_SERVICE}/orders/${req.params.id}`),
    axios.get(`${USER_SERVICE}/users/${userId}`),
    axios.get(`${INVENTORY_SERVICE}/stock/${productId}`)
  ]);
  
  // Aggregate response
  res.json({
    order: order.data,
    user: user.data,
    stock: inventory.data
  });
});
```

**gRPC:**
- Binary protocol (protobuf)
- HTTP/2 based
- Bi-directional streaming
- Type-safe

```protobuf
// user.proto
syntax = "proto3";

service UserService {
  rpc GetUser (UserRequest) returns (UserResponse);
  rpc ListUsers (Empty) returns (stream UserResponse);
}

message UserRequest {
  string user_id = 1;
}

message UserResponse {
  string user_id = 1;
  string name = 2;
  string email = 3;
}
```

#### Asynchronous (Event-Driven)

**Event-Driven Communication:**
```javascript
// Event publishing
class OrderService {
  async createOrder(orderData) {
    // Save to database
    const order = await Order.create(orderData);
    
    // Publish event
    await eventBus.publish('OrderCreated', {
      orderId: order.id,
      userId: order.userId,
      items: order.items,
      total: order.total
    });
    
    return order;
  }
}

// Event consumers
class InventoryService {
  constructor() {
    eventBus.subscribe('OrderCreated', this.reserveStock);
  }
  
  async reserveStock(event) {
    for (const item of event.items) {
      await Inventory.decrement(item.productId, item.quantity);
    }
  }
}

class NotificationService {
  constructor() {
    eventBus.subscribe('OrderCreated', this.sendConfirmation);
  }
  
  async sendConfirmation(event) {
    await emailService.send({
      to: event.userId,
      subject: 'Order Confirmation',
      body: `Your order ${event.orderId} is confirmed!`
    });
  }
}
```

### Service Discovery

Service Discovery, mikro servis dünyasının **telefon rehberidir** — ama kendini otomatik güncelleyen bir telefon rehberi! Monolitik dünyada servislerinizin adresleri sabittir: `user-service` hep `10.0.1.5:3000`'da çalışır, bunu config dosyasına yazarsınız, biter. Ama mikro servis + Kubernetes dünyasında? Pod'lar ölür, yeniden doğar. Her seferinde FARKLI bir IP alırlar. Bugün `10.0.1.5`'te olan servis, yarın `10.0.2.99`'da olabilir. URL'leri hardcode etmek İMKANSIZ.

**Nasıl Çalışır?**

Service Discovery'nin mantığı basittir:
1. **Register (Kayıt):** Bir servis ayağa kalktığında, kendini discovery servisine kaydeder: "Ben order-service'im, adresim 10.0.1.50:3000" 📝
2. **Discover (Keşif):** Başka bir servis order-service'i çağırmak istediğinde, discovery servisine sorar: "order-service nerede?" ve güncel adresi alır 🔍
3. **Deregister (Kayıt Silme):** Servis kapanırken kendini listeden çıkarır: "Ben artık yokum" 👋
4. **Health Check:** Discovery servisi düzenli olarak servislere ping atar. Cevap gelmezse, o servisi "sağlıksız" olarak işaretler ve trafik yönlendirmez 💓

**Client-Side vs Server-Side Discovery:**

| Yaklaşım | Nasıl Çalışır? | Avantaj | Dezavantaj |
|---|---|---|---|
| **Client-Side** | Client, registry'den servis listesini alır ve kendisi load balance yapar | Daha az hop, daha az latency | Client'a logic eklemek gerekir |
| **Server-Side** | Client, load balancer'a istek atar, LB registry'ye sorar ve yönlendirir | Client basit kalır | Ekstra hop, ekstra bileşen |

Kubernetes'te **kube-dns** (CoreDNS) server-side discovery yapar: `http://order-service.default.svc.cluster.local` yazarsınız, K8s bunu otomatik olarak doğru pod'a yönlendirir. Siz IP adresi görmezsiniz bile.

**DNS-Based vs Registry-Based:**
- **DNS-Based (K8s Service):** Basit, built-in, ama TTL cache sorunları olabilir (eski IP'ye yönlendirme)
- **Registry-Based (Consul, Eureka):** Daha gelişmiş — health check, key-value store, service mesh entegrasyonu

**Araçlar:**
- **Consul (HashiCorp):** En kapsamlı. Service discovery + health checking + KV store + service mesh. Multi-datacenter desteği.
- **Eureka (Netflix OSS):** Java/Spring ekosisteminin favorisi. Netflix 700+ mikro servisi Eureka ile yönetiyordu. Basit ama etkili.
- **AWS Cloud Map:** AWS-native çözüm. ECS, EKS, Lambda ile entegre. AWS'deyseniz en az sürtünme burada.

**Gerçek Dünya:** Netflix, Eureka ile 700+ mikro servisin keşfini yönetiyordu. Bir servis 100 instance'a scale olduğunda, Eureka tüm instance'ların adreslerini bilir ve client'lar arasında dağıtır. Servis çökerse, 30 saniye içinde listeden çıkarılır. Sıfır insan müdahalesi. 🎬

**Consul, Eureka, AWS Cloud Map:**
```javascript
// Service registration
const consul = require('consul')();

await consul.agent.service.register({
  name: 'order-service',
  address: '10.0.1.50',
  port: 3000,
  check: {
    http: 'http://10.0.1.50:3000/health',
    interval: '10s'
  }
});

// Service discovery
const services = await consul.health.service('user-service');
const healthyService = services[0];
const response = await axios.get(
  `http://${healthyService.Service.Address}:${healthyService.Service.Port}/users/123`
);
```

### API Gateway Pattern

API Gateway nedir? Bir **otel resepsiyoncusu** düşünün. 🏨 Otele gelen misafirler oda numaralarını bilmez. Resepsiyona gider: "Restoran nerede?", "Havuz ne zaman açık?", "203 numaralı odaya mesaj bırakın." Resepsiyoncu hepsini yönlendirir, yetkisiz kişileri engeller, soruları cevaplar. API Gateway de aynısını yapar: tüm client'lar (web, mobil, 3rd party) için **tek giriş noktasıdır.** Client'lar arka plandaki 50 farklı mikro servisin varlığından bihaber — sadece gateway'e istek atar.

**Neden API Gateway?**

API Gateway olmadan, client uygulamanız kullanıcı bilgisi için `user-service:3001`'e, sipariş için `order-service:3002`'ye, ödeme için `payment-service:3003`'e ayrı ayrı istek atar. Bu demektir ki:
- Client, tüm servislerin adreslerini bilmeli ❌
- Her serviste ayrı ayrı auth kontrolü yapılmalı ❌
- Rate limiting her serviste tekrarlanmalı ❌
- CORS, logging, monitoring HER yerde ayrı ayrı ❌

API Gateway ile tüm bu **cross-cutting concern'ler** TEK bir yerde yönetilir. Auth? Gateway halleder. Rate limiting? Gateway halleder. Logging? Gateway halleder. Servisler sadece iş mantığına odaklanır.

**BFF (Backend for Frontend) Pattern:**

Her client türü farklı veri ihtiyacına sahiptir. Mobil app küçük payload ister (bant genişliği sınırlı), web app detaylı veri ister, smart TV sadece temel bilgileri gösterir. BFF pattern'ında her client türü için AYRI bir gateway oluşturursunuz:
- `web-gateway` → Zengin veri, pagination, detaylı response'lar
- `mobile-gateway` → Kompakt veri, optimize edilmiş payload, resim boyutları küçük
- `iot-gateway` → Minimal veri, düşük bant genişliği

Bu, frontend ekiplerinin kendi gateway'lerini kontrol etmesini sağlar — backend'e bağımlılık azalır.

**Kong vs AWS API Gateway vs NGINX:**

| Özellik | Kong | AWS API Gateway | NGINX |
|---|---|---|---|
| **Tip** | Open-source, plugin-based | Fully managed | Web server + reverse proxy |
| **Plugin Ekosistemi** | 100+ plugin (auth, rate limit, logging...) | AWS Lambda, Cognito entegrasyonu | Lua scripting ile genişletilebilir |
| **Scaling** | Kendi yönetirsiniz | Otomatik | Kendi yönetirsiniz |
| **Maliyet** | Free (OSS) / Enterprise | Per-request pricing | Free (OSS) / NGINX Plus |
| **En İyi Kullanım** | K8s ortamları, multi-cloud | AWS-native projeler | Basit reverse proxy ihtiyaçları |

**⚠️ Yaygın Hata: Gateway'e Business Logic Koymak!**

Bu çok tehlikeli bir anti-pattern. Gateway "kullanıcının VIP olup olmadığını kontrol et, VIP ise %20 indirim uygula" gibi iş mantığı YAPMAMALIDIR. Gateway'in görevi: **routing, auth, rate limiting, logging.** İş mantığı servislerde kalmalı. Gateway'e logic koyarsanız, gateway bir "god service"e dönüşür — test edilmesi zor, deploy edilmesi korkunç, debug edilmesi imkansız.

**Kong, AWS API Gateway, NGINX:**
```yaml
# Kong configuration
services:
  - name: order-service
    url: http://orders:3000
    routes:
      - paths: [/api/orders]
    plugins:
      - name: rate-limiting
        config:
          minute: 100
      - name: jwt
      - name: cors

  - name: user-service
    url: http://users:3000
    routes:
      - paths: [/api/users]
```

**API Gateway Responsibilities:**
- Routing
- Rate limiting
- Authentication/Authorization
- Request/Response transformation
- Caching
- Logging & monitoring
- Load balancing

### Circuit Breaker Pattern

Circuit Breaker (Devre Kesici) pattern'ını anlamak için evinizdeki **sigorta kutusunu** düşünün. ⚡ Elektrik hattında aşırı akım olduğunda (kısa devre, aşırı yük) sigorta ATLANIR ve elektriği keser. Neden? Çünkü kesmezse kablolar erir, yangın çıkar, tüm ev yanar. Circuit Breaker pattern'ı da yazılımda aynısını yapar: bir servis sürekli hata veriyorsa, o servise istek GÖNDERMEYİ DURDURUR. Çünkü hatalı bir servise istek göndermeye devam etmek, tüm sistemi çökertebilir.

**Cascade Failure: Domino Etkisi 🎯**

Circuit Breaker olmazsa ne olur? Şu senaryoyu düşünün:
1. `payment-service` yavaşladı (veritabanı sorunu)
2. `order-service` payment-service'i çağırıyor, cevap gelmiyor, thread BEKLEMEDE
3. order-service'in tüm thread'leri payment-service'i beklerken tıkandı
4. `checkout-service` order-service'i çağırıyor, o da cevap veremiyor
5. `api-gateway` checkout-service'i çağırıyor, o da cevap veremiyor
6. **TÜM SİSTEM ÇÖKTÜ** — sadece payment-service yüzünden! 💀

Bir servisin hatası, dalga dalga yayılarak tüm sistemi felç eder. Buna **cascade failure** denir ve mikro servis mimarisinin en büyük kâbusudur.

**Üç Durum (State Machine):**

Circuit Breaker bir state machine gibi çalışır:

```
🟢 CLOSED (Normal)          → İstekler normal akıyor, hatalar sayılıyor
    ↓ (hata oranı eşiği aşıldı, ör: %50)
🔴 OPEN (Devre Açık)        → Tüm istekler ANINDA reddedilir (fail-fast), servise hiç gitmez
    ↓ (timeout süresi doldu, ör: 30 saniye)
🟡 HALF-OPEN (Yarı Açık)    → Sadece BİR test isteği gönderilir
    ↓ başarılı → 🟢 CLOSED (servis iyileşti!)
    ↓ başarısız → 🔴 OPEN (henüz iyileşmedi, tekrar bekle)
```

Half-Open durumu dahice bir tasarım: sistemi tamamen kapatmak yerine, periyodik olarak "acaba düzeldi mi?" diye kontrol eder. Düzeldiyse normal akışa döner, düzelmediyse beklemeye devam eder. İnsanın "acaba internet geldi mi?" diye sayfayı yenilemesi gibi düşünün — ama otomatik ve akıllıca. 😄

**Fallback Stratejileri — "B Planı Her Zaman Olsun":**

Circuit açıldığında ne yapacaksınız? Kullanıcıya "500 Internal Server Error" mı göstereceksiniz? HAYIR! Graceful degradation:
- **Cached Data:** Ödeme servisi çalışmıyorsa, son başarılı fiyatı cache'ten göster
- **Default Response:** Öneri servisi çöktüyse, "en popüler ürünler" listesini göster
- **Graceful Degradation:** Tam özellik çalışmıyorsa, azaltılmış özellikle devam et (ör: canlı fiyat yerine son bilinen fiyat)
- **Queue for Later:** İşlemi kuyruğa at, servis düzelince işle

**Opossum: Node.js Circuit Breaker**

Node.js dünyasında en popüler circuit breaker kütüphanesi `opossum`'dur (evet, keseli hayvan opossum — "ölü taklidi" yapar, tıpkı circuit breaker'ın hatalı servisi "görmezden gelmesi" gibi 🦡). Opossum, Promise tabanlıdır ve Express/Fastify ile kolayca entegre olur.

**Gerçek Dünya:** Netflix bu pattern'ı meşhur eden şirkettir. Netflix Hystrix (artık maintenance modda) Java dünyasının circuit breaker standardıydı. Bugün:
- **Java:** resilience4j (Hystrix'in halefi)
- **Node.js:** opossum
- **.NET:** Polly
- **Go:** sony/gobreaker

Netflix'in her mikro servisi circuit breaker kullanır. Bir servise giden isteklerin %50'si başarısız olduğunda, circuit AÇILIR, 30 saniye boyunca o servis çağrılmaz, fallback devreye girer. Kullanıcı belki her özelliği göremez ama **uygulama ÇÖKMEZ.** Bu "partial failure tolerance" yaklaşımı, %100 uptime hedefleyen sistemlerin temelidir.

**Resilience için gerekli:**
```javascript
const CircuitBreaker = require('opossum');

// Protect external service call
const options = {
  timeout: 3000, // 3 saniye
  errorThresholdPercentage: 50, // %50 fail rate
  resetTimeout: 30000 // 30 saniye sonra tekrar dene
};

const breaker = new CircuitBreaker(callExternalService, options);

breaker.fallback(() => {
  // Fallback response when circuit is open
  return { cached: true, data: getCachedData() };
});

// Usage
try {
  const result = await breaker.fire(userId);
} catch (err) {
  // Circuit open or request failed
}

// Events
breaker.on('open', () => console.log('Circuit opened'));
breaker.on('halfOpen', () => console.log('Circuit half-open'));
breaker.on('close', () => console.log('Circuit closed'));
```

### Distributed Tracing

Distributed tracing, bir isteğin **GPS takibi** gibidir — kullanıcının tıkladığı andan sonucun döndüğü ana kadar, o isteğin her microservice'teki yolculuğunu takip edersiniz. Monolith dünyada hata ayıklamak kolaydı: tek bir uygulamanın loglarına bakardınız. Ama microservices dünyasında? Bir kullanıcı "sipariş veremiyorum" dediğinde, o istek sırasıyla API Gateway → Auth Service → Order Service → Inventory Service → Payment Service → Notification Service üzerinden geçmiş olabilir. **Hangisinde sorun var?** Distributed tracing olmadan bunu bulmak, samanlıkta iğne aramaktır.

**Neden Gerekli? — Gerçek Bir Senaryo:**

Düşünün: Kullanıcı "sipariş çok yavaş" diye şikayet ediyor. Loglarınıza bakıyorsunuz — API Gateway'de 50ms, Order Service'de 100ms, Inventory Service'de 80ms... Her şey normal görünüyor. Ama toplam süre 8 saniye! Nerede kayboldu bu zaman? Distributed tracing olmadan bunu bulmak neredeyse imkansız. Tracing ile? Tek bir Trace ID ile tüm journey'yi görürsünüz ve Payment Service'in 3. parti ödeme API'sine yapılan çağrıda 7.5 saniye beklediğini hemen fark edersiniz.

**Temel Kavramlar:**

🔹 **Trace ID:** Her isteğe atanan benzersiz kimlik — tıpkı bir kargo takip numarası gibi. Bu ID, istek hangi servise giderse gitsin birlikte taşınır (HTTP header olarak: `X-Trace-Id` veya `traceparent`). Tüm servislerdeki logları bu ID ile birleştirirsiniz.

🔹 **Span:** Her servisin isteği işlerken oluşturduğu bir "zaman dilimi" kaydıdır. Başlangıç zamanı, bitiş zamanı, servis adı, operasyon adı ve metadata içerir. Bir trace birçok span'den oluşur ve parent-child ilişkisi ile tree yapısı oluşturur.

🔹 **OpenTelemetry (OTel):** Distributed tracing'in **emerging standard'ı**dır. Eskiden OpenTracing ve OpenCensus ayrı projelerdi, ikisi birleşerek OpenTelemetry oldu. CNCF (Cloud Native Computing Foundation) projesidir. Vendor-agnostic'tir — aynı kodla Jaeger'a da, AWS X-Ray'e de, Datadog'a da veri gönderebilirsiniz.

🔹 **Sampling — Her İsteği Trace Edemezsiniz:**

Üretim ortamında saniyede binlerce istek geliyor. Her birini trace etmek hem performansa hem depolamaya aşırı yük bindirir. Bu yüzden **sampling** yapılır: isteklerin %1-10'unu trace edersiniz. Akıllı sampling stratejileri de var: hatalı istekleri %100, başarılı istekleri %1 trace etmek gibi (head-based vs tail-based sampling).

**Popüler Araçlar:**
- **Jaeger:** Uber tarafından geliştirildi, CNCF projesi. Open-source, Kubernetes-native. En yaygın self-hosted çözüm.
- **AWS X-Ray:** AWS ekosistemine entegre. Lambda, ECS, EKS ile doğal uyum. AWS kullanıyorsanız en kolay başlangıç.
- **Zipkin:** Twitter tarafından geliştirildi. Basit ve hafif. Google Dapper paper'ından esinlenilmiş.
- **Datadog APM, New Relic:** Ticari çözümler. Dashboard'ları, alerting'i ve AI-destekli analizi ile güçlü.

**Gerçek Dünya Hikayesi:** "Kullanıcı yavaşlıktan şikayet etti. İsteği trace ettik ve Payment Service'in yavaş bir DB query yüzünden 8 saniye sürdüğünü bulduk. Query'ye bir index ekledik → süre 200ms'e düştü. Distributed tracing olmasa, bu sorunu bulmamız belki günler sürerdi. Tracing ile 15 dakikada bulduk." Bu, distributed tracing'in gerçek değeridir — sorunları hızlı bulma ve çözme yeteneği. 🎯

**Jaeger, AWS X-Ray, Zipkin:**
```javascript
// OpenTelemetry ile distributed tracing
const { trace } = require('@opentelemetry/api');
const tracer = trace.getTracer('order-service');

app.post('/orders', async (req, res) => {
  const span = tracer.startSpan('create_order');
  
  try {
    // Database write
    const dbSpan = tracer.startSpan('db_insert', { parent: span });
    const order = await Order.create(req.body);
    dbSpan.end();
    
    // Call inventory service
    const invSpan = tracer.startSpan('check_inventory', { parent: span });
    await axios.post('http://inventory/reserve', { items: req.body.items });
    invSpan.end();
    
    res.json(order);
  } finally {
    span.end();
  }
});
```

---

## 🔌 API Design & Communication

### API Paradigmları Karşılaştırması

#### REST vs GraphQL vs gRPC

**REST (Representational State Transfer):**
```
Avantajları:
✓ Simple & widely understood
✓ HTTP semantics (GET, POST, PUT, DELETE)
✓ Cacheable (HTTP caching)
✓ Stateless
✓ Good for CRUD operations

Dezavantajları:
✗ Over-fetching (gereksiz data)
✗ Under-fetching (multiple requests)
✗ Versioning challenges
✗ No type safety

Ne Zaman Kullanılır:
- Public APIs
- Simple CRUD
- HTTP caching önemli
- Mobile apps (HTTP/1.1)
```

**GraphQL:**
```
Avantajları:
✓ Tek endpoint, flexible queries
✓ No over-fetching
✓ No under-fetching
✓ Strong typing (schema)
✓ Introspection
✓ Great for complex data requirements

Dezavantajları:
✗ Complexity (server-side)
✗ Caching zor
✗ N+1 query problem
✗ Learning curve

Ne Zaman Kullanılır:
- Complex frontend requirements
- Mobile apps (reduce requests)
- Rapid prototyping
- Aggregating multiple services
```

**gRPC:**
```
Avantajları:
✓ Binary protocol (fast)
✓ HTTP/2 (multiplexing, streaming)
✓ Strong typing (Protocol Buffers)
✓ Bi-directional streaming
✓ Code generation

Dezavantajları:
✗ Not browser-friendly
✗ Binary format (debugging zor)
✗ Less human-readable
✗ Steeper learning curve

Ne Zaman Kullanılır:
- Microservices communication
- High-performance requirements
- Streaming data
- Polyglot environments
```

### REST API Design Best Practices

REST API tasarımı, bir evin MİMARİ planını çizmek gibidir. Kötü bir plan ile ev de yapılır — ama sonra her yeni oda eklemeye çalıştığında duvarları YIKIYOR olursun. 😄

İyi bir REST API'nin "güzel URL'ler" ile ilgisi yok — **tutarlılık, ölçeklenebilirlik ve kullanım kolaylığı** ile ilgisi var.

**Altın kural:** API'ın tüketicisi (frontend developer, mobile developer, 3rd party entegratör) senin koduyu bilmez. API onun "PENCERE"sidir — pencere net, tutarlı ve tahmin edilebilir olmalı.

#### 1. Resource Naming

**REST'te her şey bir KAYNAK'tır (resource).** URL'ler fiil (verb) değil, isim (noun) olmalıdır. Fiil HTTP method ile belirtilir (GET, POST, PUT, DELETE).

**Neden?** Çünkü URL bir "adres" gibidir. Ev adresin "Atatürk Caddesi No:5" dir, "5 numaraya git" değil. 😄
```javascript
// ✅ Good
GET    /users
POST   /users
GET    /users/123
PUT    /users/123
DELETE /users/123
GET    /users/123/orders
POST   /users/123/orders

// ❌ Bad
GET    /getUsers
POST   /createUser
GET    /user/123  (inconsistent plural/singular)
GET    /users/123/getOrders
```

#### 2. HTTP Methods & Status Codes

**HTTP Method'ları "sihirli değnek" gibidir** — her birinin özel bir ANLAMI vardır ve bu anlamı yanlış kullanırsan tüketicini şaşırtırsın.

**Kritik kavramlar:**
- **Idempotent (Tekrarlanabilir):** Aynı isteği 10 kez gönderirsen sonuç HEP AYNI kalır. GET, PUT, DELETE idempotent. POST değil!
- **Safe (Güvenli):** Sunucuda hiçbir değişiklik yapmaz. Sadece GET ve HEAD safe.

**Neden önemli?** Ağ sorunlarında istemci aynı isteği tekrar gönderebilir. POST idempotent değilse, aynı sipariş 2 kez oluşturulabilir! 😱 Bu yüzden ödeme API'larında **idempotency key** kullanılır (Stripe'ın yaptığı gibi).
```javascript
// GET: Retrieve resource
app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  res.status(200).json(user);
});

// POST: Create resource
app.post('/users', async (req, res) => {
  const user = await User.create(req.body);
  res.status(201)
    .header('Location', `/users/${user.id}`)
    .json(user);
});

// PUT: Replace resource
app.put('/users/:id', async (req, res) => {
  const user = await User.update(req.params.id, req.body);
  res.status(200).json(user);
});

// PATCH: Partial update
app.patch('/users/:id', async (req, res) => {
  const user = await User.patch(req.params.id, req.body);
  res.status(200).json(user);
});

// DELETE: Remove resource
app.delete('/users/:id', async (req, res) => {
  await User.delete(req.params.id);
  res.status(204).send();
});

// Common Status Codes
200 OK               // Success
201 Created          // Resource created
204 No Content       // Success, no return data
400 Bad Request      // Invalid input
401 Unauthorized     // Not authenticated
403 Forbidden        // Authenticated but no permission
404 Not Found        // Resource doesn't exist
409 Conflict         // Duplicate resource
422 Unprocessable    // Validation error
429 Too Many Requests // Rate limit
500 Internal Error   // Server error
503 Service Unavailable // Maintenance
```

#### 3. Filtering, Sorting, Pagination

**Bu konu interview'larda SİK sorulur!** Özellikle "çok büyük veri setlerinde pagination nasıl yapılır?" sorusu.

**İki yaklaşım var:**

| Yöntem | Nasıl Çalışır | Artı | Eksi |
|--------|-----------------|------|------|
| **Offset-based** | `LIMIT 20 OFFSET 100` | Basit, sayfa numarası gösterebilirsin | Derin sayfalarda ÇOK YAVAŞ! (100.000. sayfa = DB 100K satır sayıp atlar) |
| **Cursor-based** | `WHERE id > last_seen_id LIMIT 20` | Her zaman Hızlı! | Sayfa numarası gösteremezsin, sadece "önceki/sonraki" |

**Gerçek dünya:** Twitter/X'in timeline'u cursor-based pagination kullanır. Neden? Milyonlarca tweet var — `OFFSET 1000000` yapmak postgreSQL'i öldürür. 💀 Bunun yerine "son gördüğün tweet ID'sinden sonrakiler" denir → her zaman hızlı!

**Getir'de:** Ürün listesinde cursor-based, admin panelinde sayfa numaralı (offset-based) kullanılabilir — çünkü admin'de veri seti küçük.
```javascript
app.get('/products', async (req, res) => {
  const {
    page = 1,
    limit = 20,
    sort = 'created_at',
    order = 'desc',
    category,
    min_price,
    max_price,
    search
  } = req.query;

  // Build query
  const query = Product.query();

  // Filtering
  if (category) {
    query.where('category', category);
  }
  if (min_price) {
    query.where('price', '>=', min_price);
  }
  if (max_price) {
    query.where('price', '<=', max_price);
  }
  if (search) {
    query.where('name', 'ILIKE', `%${search}%`);
  }

  // Sorting
  query.orderBy(sort, order);

  // Pagination
  const offset = (page - 1) * limit;
  const products = await query.limit(limit).offset(offset);
  const total = await Product.count(query);

  res.json({
    data: products,
    meta: {
      page: parseInt(page),
      limit: parseInt(limit),
      total,
      totalPages: Math.ceil(total / limit)
    },
    links: {
      self: `/products?page=${page}&limit=${limit}`,
      next: page * limit < total ? `/products?page=${parseInt(page) + 1}&limit=${limit}` : null,
      prev: page > 1 ? `/products?page=${parseInt(page) - 1}&limit=${limit}` : null
    }
  });
});

// Usage:
// GET /products?category=electronics&min_price=100&max_price=500&sort=price&order=asc&page=2&limit=10
```

#### 4. Versioning Strategies

API versioning, yazılım dünyasının **geriye dönük uyumluluk sözleşmesidir** — ve bu sözleşmeyi bozarsanız, müşterileriniz (yani API'nizi kullanan geliştiriciler) sizi TERK EDER. 📜

**Neden Versioning?**

Diyelim ki `GET /users` endpoint'iniz `{ name, email }` döndürüyor. Bir gün product manager gelip "kullanıcının adresini de ekleyelim" diyor — sorun yok, yeni field eklemek breaking change değil. Ama "email field'ını `emailAddress` olarak değiştirelim" derse? İşte o zaman PROBLEM: 500 client'ınız `response.email` okuyordur. Bunu değiştirirseniz, hepsi PATLAR. Versioning tam da bu yüzden var: **mevcut client'ları kırmadan API'yi evrimleştirmek.**

**Üç Temel Strateji:**

| Strateji | Örnek | Avantaj | Dezavantaj |
|----------|-------|---------|------------|
| **URL Versioning** | `/api/v1/users` | En basit, en yaygın, tarayıcıda test kolay | URL'ler çirkinleşir |
| **Header Versioning** | `Api-Version: 2` | URL temiz kalır | Tarayıcıda test zor, keşfedilebilirlik düşük |
| **Query Param** | `/users?version=2` | Basit | URL caching sorunları, standart dışı |

**URL Versioning en yaygın olanıdır** — Stripe (`/v1/charges`), GitHub (`/v3/repos`), Twitter (`/2/tweets`) hepsi kullanır. Sebebi basit: explicit, keşfedilebilir ve herkesin anlayacağı bir format.

**Semantic Versioning API'ler İçin:**
- **Major (v1 → v2):** Breaking change — response formatı değişti, field silindi, endpoint kaldırıldı
- **Minor (v1.1 → v1.2):** Yeni özellik — yeni endpoint eklendi, yeni opsiyonel field eklendi
- **Patch (v1.1.0 → v1.1.1):** Bug fix — davranış düzeltmesi, hata mesajı iyileştirmesi

**Deprecation Stratejisi — Nazikçe Veda Etmek:**
1. **Announce (Duyur):** "v1 6 ay sonra kaldırılacak" → API response'larına `Sunset` header ekle
2. **Sunset Date (Son Tarih):** `Sunset: Sat, 01 Jan 2025 00:00:00 GMT`
3. **Migrate (Göç):** v1 kullanıcılarına migration guide sağla, SDK'ları güncelle
4. **Monitor (İzle):** v1 trafiğini izle, hâlâ kullananları uyar (email, dashboard notification)
5. **Remove (Kaldır):** Son tarih geldiğinde v1'i kapat, `410 Gone` döndür

**🏆 Gerçek Dünya — Stripe'ın Efsanevi Yaklaşımı:**

Stripe, backward compatibility'nin KRALDIR. 2011'den beri yayınladıkları HER API versiyonunu hâlâ desteklerler. Nasıl mı? Her API isteği bir `Stripe-Version` header'ı taşır. Stripe, bu versiyona göre request/response'u dönüştüren **version compatibility layer**'lar kullanır. Yani internal olarak tek bir codebase çalışır, ama dışarıya her versiyon için uyumlu response döner. Bu yaklaşımın bedeli? Devasa bir test matrisi ve karmaşık middleware katmanları. Ama Stripe bunun karşılığında milyonlarca geliştiricinin GÜVENİNİ kazandı — "Stripe API'yi kullanıyorsan, kodun 5 yıl sonra da çalışır." 💳

```javascript
// URL Versioning (Recommended)
app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);

// Header Versioning
app.use((req, res, next) => {
  const version = req.headers['api-version'] || '1';
  req.apiVersion = version;
  next();
});

// Accept Header Versioning
// Accept: application/vnd.myapi.v1+json

// Query Parameter (Not recommended)
// /users?version=1
```

#### 5. HATEOAS (Hypermedia)

HATEOAS, REST'in en **unutulmuş** ve en **yanlış anlaşılmış** prensibidir. Tam adı: **Hypermedia As The Engine Of Application State** — evet, ismi bile korkutucu. 😅

**Analoji — Web Sitesi Navigasyonu:**

Bir web sitesine girdiğinizde URL'leri ezberlemenize gerek yoktur. Ana sayfada "Ürünler", "Hakkımızda", "İletişim" LİNKLERİ vardır — tıklarsınız, doğru sayfaya gidersiniz. Ürünler sayfasında "Sepete Ekle" butonu vardır — tıklarsınız, sepet sayfasına gidersiniz. Her sayfa size "bundan sonra ne yapabilirsin" bilgisini VERİR. HATEOAS, API'lerin de böyle çalışması gerektiğini söyler: **her response, client'a bir sonraki adımda yapabileceği aksiyonların linklerini içermelidir.**

**Nasıl Çalışır:**

Normal REST: `GET /users/123` → `{ name: "Ali", email: "ali@test.com" }`. Client, siparişleri görmek isterse `/users/123/orders` URL'sini KENDİSİ bilmek zorunda — bu URL hardcode edilmiş, dokümantasyondan ezberlenmiş.

HATEOAS REST: `GET /users/123` → response'un içinde `_links` objesi var: "siparişlere buradan git", "avatarı buradan güncelle", "hesabı buradan sil". Client URL ezberlemez, response'taki linkleri TAKİP EDER.

**Faydaları:**
- **Self-describing API:** API kendi dokümantasyonunu TAŞIR
- **Decoupled client:** URL yapısı değişirse, client kırılmaz (linkler güncel gelir)
- **Discoverability:** Yeni özellik eklendiğinde, client otomatik keşfeder (yeni link response'ta görünür)
- **State-driven navigation:** Kullanıcının durumuna göre farklı linkler → sipariş "pending" ise "iptal et" linki var, "shipped" ise yok

**Gerçeklik Kontrolü — Neredeyse Kimse Tam Uygulamıyor:**

HATEOAS güzel bir FİKİR ama pratikte tam uygulanması karmaşıktır. Her response'a link eklemek ekstra efor gerektirir, client tarafında link parsing mantığı yazılmalıdır ve çoğu frontend ekibi "biz zaten URL'leri biliyoruz, neden link takip edelim?" der. Sonuç? REST'in teorik olarak en yüksek olgunluk seviyesi (Richardson Maturity Model Level 3) neredeyse hiç uygulanmaz.

**Kim Kullanıyor?** PayPal API HATEOAS'ı güçlü bir şekilde uygular — ödeme oluşturduktan sonra response'ta "approve", "capture", "void" linkleri gelir. Bazı enterprise API'ler (SAP, Oracle) de kısmen uygular. GitHub API v3'ün response'larında `_links` bulunur ama çoğu geliştirici bunları görmezden gelir. 😄

```javascript
// Self-descriptive API responses
{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com",
  "_links": {
    "self": { "href": "/users/123" },
    "orders": { "href": "/users/123/orders" },
    "avatar": { "href": "/users/123/avatar" }
  }
}
```

### GraphQL Deep Dive

GraphQL, API dünyasının **menü sipariş sistemidir** — REST'in "komple tabldot" yaklaşımı yerine, "à la carte" sipariş vermenizi sağlar. 🍽️

**Hikaye:** 2012 yılında Facebook'un mobil ekibi bir SORUNLA boğuşuyordu. News Feed'i yüklemek için mobil app, 10+ farklı REST endpoint'ine istek atıyordu: `/users/me`, `/posts`, `/comments`, `/likes`, `/friends`... Her endpoint gereğinden FAZLA veri döndürüyordu (over-fetching: kullanıcı sadece isim ve avatar istiyor ama API 47 field döndürüyor) veya EKSIK veri döndürüyordu (under-fetching: post'ları aldın ama yazar bilgisi yok, bir istek daha at). 3G bağlantıda bu FELAKET demekti. Facebook mühendisleri Lee Byron, Dan Schafer ve Nick Schrock bir çözüm geliştirdi: **GraphQL.** 2015'te open-source olarak yayınladılar ve dünya değişti.

**GraphQL Nedir?**

GraphQL, API'niz için bir **query language** (sorgu dili) ve **runtime**'dır. SQL veritabanları için ne ise, GraphQL API'ler için odur. Ama dikkat: GraphQL bir veritabanı sorgu dili DEĞİLDIR — client ile server arasındaki iletişim dilidir.

**Schema-First Yaklaşım — Sözleşme Önce Gelir:**

GraphQL'de her şey **schema** ile başlar. Schema, frontend ve backend arasındaki SÖZLEŞME'dir — "ben sana bu verileri bu formatta vereceğim, sen bana bu formatta istekte bulunacaksın." Bunu TypeScript'in API versiyonu olarak düşünebilirsiniz: strongly typed, self-documenting, ve compile-time'da hataları yakalar.

**Type System — API'nizin TypeScript'i:**

GraphQL strongly typed'dır. Her field'ın bir tipi vardır: `String`, `Int`, `Float`, `Boolean`, `ID`. `!` işareti non-nullable demektir (null OLAMAZ). `[Post!]!` ise "boş olamayan, içindeki elemanlar da null olamayan bir Post dizisi" demektir. Bu tip sistemi sayesinde, API dokümantasyonu OTOMATİK oluşur — Swagger/OpenAPI yazmaya gerek kalmaz.

**Tek Endpoint — Hepsini Yönetecek Tek Yüzük:**

REST'te 20 farklı endpoint vardır: `GET /users`, `POST /orders`, `PUT /products/:id`... GraphQL'de TEK endpoint vardır: `POST /graphql`. Tüm sorgular, mutation'lar ve subscription'lar bu tek endpoint üzerinden geçer. Bu, routing karmaşıklığını SIFIRA indirir.

**Trade-off'lar — Her Gül'ün Dikeni Var:**

| REST | GraphQL |
|------|--------|
| Basit, herkes bilir | Öğrenme eğrisi var |
| HTTP caching built-in (GET request) | Caching ZOR (her şey POST) |
| Over-fetching / Under-fetching | Tam istediğini alırsın |
| Endpoint başına rate limiting kolay | Rate limiting karmaşık (query complexity) |
| Basit CRUD için mükemmel | Basit CRUD için overkill |
| Birden fazla round-trip | Tek request'te tüm veri |

**Ne Zaman GraphQL?** Karmaşık frontend'ler (dashboard'lar, mobil app'ler, çoklu client türleri) için harika. Basit bir CRUD API için? REST yeterli — GraphQL overkill olur.

**Gerçek Dünya:** GitHub API v4 tamamen GraphQL'dir. Neden? Çünkü GitHub'ın milyonlarca geliştiricisi, binlerce farklı kullanım senaryosu var. REST API v3'te bir repository'nin bilgilerini almak için 5 farklı endpoint çağırmanız gerekiyordu. GraphQL ile TEK sorguyla repository + owner + contributors + languages + last 10 commits'i alabilirsiniz. Shopify, Airbnb, Twitter ve PayPal da GraphQL kullanıyor. 🚀

#### Schema Definition
```graphql
# schema.graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
  createdAt: DateTime!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
  published: Boolean!
}

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
  post(id: ID!): Post
  posts(authorId: ID, published: Boolean): [Post!]!
}

type Mutation {
  createUser(name: String!, email: String!): User!
  updateUser(id: ID!, name: String, email: String): User!
  deleteUser(id: ID!): Boolean!
  createPost(title: String!, content: String!, authorId: ID!): Post!
}

type Subscription {
  postAdded: Post!
  commentAdded(postId: ID!): Comment!
}
```

#### Resolvers

Resolver'lar, GraphQL'in **mutfak personeli**dir. 👨‍🍳 Schema menüyü tanımlar ("Adana kebap servisi yapıyoruz"), ama resolver o kebabı gerçekten PİŞİREN kişidir. Her field'ın arkasında bir resolver vardır — o field'ın verisini nereden ve nasıl getireceğini bilen bir fonksiyon.

**Resolver Chain — Şelale Modeli:**

Bir GraphQL sorgusu geldiğinde, resolver'lar bir ŞELALE gibi çalışır:
1. **Query Resolver:** Önce en üst seviye çözülür → `user(id: "123")` → User nesnesini veritabanından getirir
2. **Type Resolver:** Sonra User tipinin field'ları çözülür → `posts` field'ı için `User.posts` resolver'ı çalışır
3. **Field Resolver:** İç içe gidebilir → her Post'un `author` field'ı, her Comment'in `user` field'ı...

Bu zincir, ağaç yapısında aşağı doğru iner. Parent resolver'ın döndürdüğü değer, child resolver'ın `parent` parametresi olur.

**Context Object — Herkesin Paylaştığı Sırt Çantası:**

Her resolver 4 parametre alır: `(parent, args, context, info)`. Bunlardan `context` en önemlisidir — tüm resolver'lar arasında PAYLAŞILAN bir nesnedir. İçine ne koyarsınız?
- **Authentication bilgisi:** `context.user` → JWT'den decode edilmiş kullanıcı
- **DataLoader instance'ları:** `context.loaders` → N+1 problemini çözen batch loader'lar
- **Database bağlantısı:** `context.db` → Prisma, Sequelize, Knex...
- **Request bilgisi:** `context.req` → IP adresi, headers...

**⚠️ N+1 Problemi — GraphQL'in En Büyük Tuzağı:**

Diyelim ki 10 kullanıcıyı ve her birinin siparişlerini çekiyorsunuz. Naif yaklaşımla: 1 sorgu ile 10 kullanıcıyı çekersiniz, sonra HER kullanıcı için AYRI bir sorgu ile siparişleri çekersiniz = 1 + 10 = **11 sorgu!** 100 kullanıcı olsa? 101 sorgu. 1000 kullanıcı? 1001 sorgu. Veritabanınız ağlıyor. 😭 Bu N+1 problemidir ve çözümü DataLoader'dır (bir sonraki bölümde).

```javascript
const resolvers = {
  Query: {
    user: async (parent, { id }, context) => {
      return await context.db.User.findById(id);
    },
    users: async (parent, { limit, offset }, context) => {
      return await context.db.User.findAll({ limit, offset });
    }
  },
  
  Mutation: {
    createUser: async (parent, { name, email }, context) => {
      // Authentication check
      if (!context.user) {
        throw new Error('Not authenticated');
      }
      
      return await context.db.User.create({ name, email });
    }
  },
  
  // Field resolvers
  User: {
    posts: async (user, args, context) => {
      // Efficient data loading with DataLoader
      return await context.loaders.postsByUser.load(user.id);
    }
  },
  
  Post: {
    author: async (post, args, context) => {
      return await context.loaders.userById.load(post.authorId);
    }
  }
};
```

#### DataLoader (N+1 problem solution)

DataLoader, N+1 probleminin **ilacıdır** — Facebook tarafından özellikle GraphQL için geliştirilmiştir. 💊

**Problem (Tekrar):** 10 post'un author bilgisini çekmek istiyorsunuz. Her post'un `author` resolver'ı ayrı ayrı çalışıyor:
```
SELECT * FROM users WHERE id = 1;  -- Post 1'in yazarı
SELECT * FROM users WHERE id = 2;  -- Post 2'nin yazarı
SELECT * FROM users WHERE id = 1;  -- Post 3'ün yazarı (aynı yazar, YİNE sorgu!)
SELECT * FROM users WHERE id = 3;  -- Post 4'ün yazarı
... 10 ayrı sorgu!
```

**Çözüm (DataLoader):** DataLoader tüm ID'leri toplar (Node.js event loop'unun tek bir tick'inde), sonra TEK bir batch sorgusu yapar:
```
SELECT * FROM users WHERE id IN (1, 2, 3);  -- TEK SORGU! 🎉
```

**Nasıl Çalışır — Event Loop Büyüsü:**

1. Resolver `userLoader.load(1)` çağırır → DataLoader ID'yi kuyruğa ekler
2. Resolver `userLoader.load(2)` çağırır → kuyruğa eklenir
3. Resolver `userLoader.load(1)` çağırır → zaten kuyrukta, tekrar eklenmez (dedup!)
4. Event loop'un mevcut tick'i biter → DataLoader `process.nextTick`'te batch fonksiyonunu çağırır
5. Batch fonksiyonu `[1, 2]` ID'leri ile TEK sorgu yapar
6. Sonuçlar ilgili resolver'lara dağıtılır

**Per-Request Caching:**

DataLoader aynı zamanda bir request-scoped cache'tir. Aynı request içinde `userLoader.load(1)` 5 kez çağrılsa bile, veritabanına sadece 1 kez gidilir. Ama bu cache SADECE o request süresince yaşar — farklı request'ler arasında paylaşılmaz (bu güvenlik açısından önemli: User A'nın request'inde cache'lenen veri, User B'ye sızmamalı).

**⚠️ Önemli Kural:** DataLoader'ı global olarak OLUŞTURMAYIN. Her request'te yeni bir DataLoader instance'ı oluşturun (context'te). Aksi takdirde stale data ve memory leak sorunları yaşarsınız.

```javascript
const DataLoader = require('dataloader');

// Batch loading
const userLoader = new DataLoader(async (userIds) => {
  const users = await User.findAll({
    where: { id: userIds }
  });
  
  // Return in same order as requested
  return userIds.map(id => users.find(u => u.id === id));
});

// Usage in resolver
const user = await userLoader.load(post.authorId);

// Multiple requests batched into one query
const users = await userLoader.loadMany([1, 2, 3, 4, 5]);
```

#### Client Usage
```javascript
// Query
const query = `
  query GetUserWithPosts($userId: ID!) {
    user(id: $userId) {
      id
      name
      email
      posts {
        id
        title
        published
      }
    }
  }
`;

const result = await fetch('/graphql', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    query,
    variables: { userId: '123' }
  })
});

// Mutation
const mutation = `
  mutation CreatePost($title: String!, $content: String!, $authorId: ID!) {
    createPost(title: $title, content: $content, authorId: $authorId) {
      id
      title
      author {
        name
      }
    }
  }
`;
```

### gRPC Implementation

gRPC, Google'un geliştirdiği yüksek performanslı RPC (Remote Procedure Call) framework'üdür. REST'ten FARKLI düşün:

**REST:** "Bana `/users/123` kaynağını ver" → Kaynak odaklı
**gRPC:** "Şu fonksiyonu çağır: `GetUser(123)`" → Fonksiyon odaklı

**gRPC neden hızlı?**
- **Protocol Buffers (protobuf):** JSON yerine binary format kullanır. Aynı veri JSON'da 100 byte iken, protobuf'ta 30 byte! 🚀
- **HTTP/2:** Multiplexing (aynı bağlantı üzerinden birden fazla istek), header compression, server push
- **Streaming:** Client streaming, server streaming, bidirectional streaming destekler

**Ne zaman gRPC?**
- Microservices ARASI iletişim (iç servisler) → ✅ gRPC
- Dış dünyaya API (frontend, mobile, 3rd party) → ✅ REST/GraphQL
- Yüksek throughput + düşük latency gereken yerler → ✅ gRPC

**Gerçek dünya:** Netflix iç servislerini REST'ten gRPC'ye taşıdığında, bandwidth'te %50 düşüş ve latency'de %30 iyileşme gördü.

#### Protocol Buffers Definition

**Protocol Buffers** gRPC'nin "dili"dir. `.proto` dosyasında servisini ve veri yapılarını tanımlarsın, sonra `protoc` compiler ı istediğin dilde (Node.js, Go, Python, Java) kod üretir.

**Önemli kurallar:**
- Field numaraları (1, 2, 3...) BİR KEZ verilir ve asla DEĞİŞTIRILMEZ (backward compatibility için)
- Field silmek yerine `reserved` ile işaretle
- 1-15 numaraları 1 byte, 16-2047 numaraları 2 byte kaplar → en çok kullanılan alanları 1-15'e koy!
```protobuf
// user.proto
syntax = "proto3";

package user;

service UserService {
  // Unary RPC
  rpc GetUser (GetUserRequest) returns (UserResponse);
  
  // Server streaming
  rpc ListUsers (ListUsersRequest) returns (stream UserResponse);
  
  // Client streaming
  rpc CreateUsers (stream CreateUserRequest) returns (CreateUsersResponse);
  
  // Bi-directional streaming
  rpc Chat (stream ChatMessage) returns (stream ChatMessage);
}

message GetUserRequest {
  string user_id = 1;
}

message UserResponse {
  string user_id = 1;
  string name = 2;
  string email = 3;
  int64 created_at = 4;
}

message ListUsersRequest {
  int32 page = 1;
  int32 page_size = 2;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
}

message CreateUsersResponse {
  int32 total_created = 1;
  repeated string user_ids = 2;
}

message ChatMessage {
  string user_id = 1;
  string message = 2;
  int64 timestamp = 3;
}
```

#### Node.js Server

gRPC server kurmak, bir restoran açmaya benzer. Önce **menüyü yazarsınız** (proto dosyası), sonra **şefleri işe alırsınız** (handler'ları implement edersiniz), en son **restoranı açarsınız** (server'ı başlatırsınız). Üç adım, bu kadar.

**Proto → Stub → Handler Akışı:**

1. **.proto dosyasını tanımla:** Bu sizin kontratınız — hangi metotlar var, ne alır, ne döner. Client ve server bu dosyayı paylaşır.
2. **Server stub'larını oluştur:** `@grpc/proto-loader` proto dosyasını okur ve JavaScript objeleri üretir. Artık hangi fonksiyonları implement etmeniz gerektiğini biliyorsunuz.
3. **Handler'ları yaz:** Her RPC metodu için gerçek iş mantığını yazarsınız — veritabanı sorgusu, hesaplama, validasyon ne gerekiyorsa.

**Unary vs Streaming — Tek Atış vs Sürekli Akış:**

| Tip | Analoji | Ne Zaman? |
|-----|---------|----------|
| **Unary** | Telefon: "Saat kaç?" → "15:30" | Klasik request-response. Kullanıcı getir, sipariş oluştur |
| **Server Streaming** | FM Radyo: Bir kere aç, sürekli müzik gelsin | Büyük veri listeleri, log stream'leri, borsa fiyatları |
| **Client Streaming** | Dosya upload: Parça parça gönder, sonunda "tamam" de | Batch insert, IoT sensör verileri |
| **Bidirectional Streaming** | Telefon görüşmesi: İki taraf da konuşur | Chat, multiplayer oyun, collaborative editing |

Unary en basit olanı — REST'in gRPC versiyonu gibi düşünün. Streaming ise gRPC'nin REST'ten **kökten ayrıldığı** yer. HTTP/2'nin multiplexing özelliği sayesinde tek bir TCP bağlantısı üzerinden onlarca stream aynı anda akabilir. REST ile bunu yapmaya çalışsanız? Long polling cehennemi. 😈

**Server Reflection — gRPC'nin Swagger'ı:**

REST API'larda Swagger/OpenAPI var: endpoint'leri keşfedersin, denersin. gRPC'de bunun karşılığı **Server Reflection**'dır. Reflection aktifken, `grpcurl` gibi araçlarla server'a "hangi servisler var?", "bu metodun input'u ne?" diye sorabilirsiniz — proto dosyasına bile ihtiyaç duymadan! Debug için HAYAT KURTARIR.

```bash
# grpcurl ile reflection kullanımı
grpcurl -plaintext localhost:50051 list                    # Tüm servisleri listele
grpcurl -plaintext localhost:50051 describe user.UserService  # Servis detayları
grpcurl -plaintext -d '{"user_id": "123"}' localhost:50051 user.UserService/GetUser  # Metod çağır
```

**Error Handling — gRPC Status Codes:**

gRPC'nin kendi status code sistemi var (HTTP status code'larından FARKLI!):

| gRPC Code | HTTP Karşılığı | Ne Zaman? |
|-----------|---------------|----------|
| `OK` (0) | 200 | Her şey yolunda |
| `NOT_FOUND` (5) | 404 | Kaynak bulunamadı |
| `ALREADY_EXISTS` (6) | 409 | Zaten var (duplicate) |
| `PERMISSION_DENIED` (7) | 403 | Yetkisiz erişim |
| `INTERNAL` (13) | 500 | Server hatası |
| `DEADLINE_EXCEEDED` (4) | 504 | Timeout! En sık karşılaşılan |
| `UNAVAILABLE` (14) | 503 | Servis hazır değil, retry yapılabilir |

`DEADLINE_EXCEEDED` özellikle kritik: gRPC'de her isteğe **deadline** koyarsınız. Deadline dolduğunda istek otomatik iptal edilir — hiçbir thread sonsuza kadar beklemez. REST'te timeout ayarlamayı unutursunuz, thread havuzu tıkanır, uygulama donar. gRPC'de bu ZORUNLU bir kültür.

**Middleware / Interceptors — Express Middleware'in gRPC Hali:**

Express'te `app.use(authMiddleware)` yazarsınız. gRPC'de bunun karşılığı **interceptor**'lardır. Her gelen/giden istek bu interceptor zincirinden geçer:

```javascript
// gRPC Server Interceptor örneği
function authInterceptor(methodDescriptor, call) {
  const metadata = call.metadata;
  const token = metadata.get('authorization')[0];
  
  if (!token || !verifyToken(token)) {
    call.sendStatus({
      code: grpc.status.UNAUTHENTICATED,
      details: 'Invalid or missing token'
    });
    return;
  }
  
  return new grpc.ServerInterceptingCall(call);
}

// Logging interceptor — her isteği logla
function loggingInterceptor(methodDescriptor, call) {
  const start = Date.now();
  console.log(`[gRPC] ${methodDescriptor.path} started`);
  
  // İstek tamamlandığında süreyi logla
  const listener = new grpc.ServerListenerBuilder()
    .withOnReceiveMessage((message, next) => {
      next(message);
    })
    .build();
  
  return new grpc.ServerInterceptingCall(call, listener);
}
```

Interceptor'larla auth, logging, tracing (OpenTelemetry), rate limiting hepsini merkezi olarak yönetirsiniz. Her handler'a ayrı ayrı auth kodu yazmak yerine, interceptor zincirinde bir kez tanımlarsınız. DRY prensibi burada da geçerli. 🎯

```javascript
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// Load proto
const packageDefinition = protoLoader.loadSync('user.proto');
const userProto = grpc.loadPackageDefinition(packageDefinition).user;

// Implement service
const userService = {
  // Unary
  GetUser: async (call, callback) => {
    const userId = call.request.user_id;
    const user = await User.findById(userId);
    
    callback(null, {
      user_id: user.id,
      name: user.name,
      email: user.email,
      created_at: user.createdAt.getTime()
    });
  },
  
  // Server streaming
  ListUsers: async (call) => {
    const { page, page_size } = call.request;
    const users = await User.findAll({ 
      limit: page_size, 
      offset: page * page_size 
    });
    
    for (const user of users) {
      call.write({
        user_id: user.id,
        name: user.name,
        email: user.email,
        created_at: user.createdAt.getTime()
      });
    }
    
    call.end();
  },
  
  // Client streaming
  CreateUsers: async (call, callback) => {
    const users = [];
    
    call.on('data', async (request) => {
      const user = await User.create({
        name: request.name,
        email: request.email
      });
      users.push(user);
    });
    
    call.on('end', () => {
      callback(null, {
        total_created: users.length,
        user_ids: users.map(u => u.id)
      });
    });
  },
  
  // Bi-directional streaming
  Chat: async (call) => {
    call.on('data', (message) => {
      // Broadcast to other clients
      call.write({
        user_id: message.user_id,
        message: message.message,
        timestamp: Date.now()
      });
    });
    
    call.on('end', () => {
      call.end();
    });
  }
};

// Start server
const server = new grpc.Server();
server.addService(userProto.UserService.service, userService);
server.bindAsync(
  '0.0.0.0:50051',
  grpc.ServerCredentials.createInsecure(),
  () => {
    server.start();
    console.log('gRPC server running on port 50051');
  }
);
```

#### Node.js Client

gRPC client kullanmak, uzaktaki bir servisi **sanki yerel bir fonksiyon gibi** çağırmak demektir. `client.GetUser({ user_id: '123' })` yazdığınızda, arka planda proto serialization, HTTP/2 framing, network call hepsi olur — ama siz sadece bir fonksiyon çağırdığınızı hissedersiniz. Bu, gRPC'nin en büyük sihri: **location transparency**. Kod okurken "bu fonksiyon lokalde mi yoksa 3000 km ötedeki bir data center'da mı çalışıyor?" diye düşünmezsiniz. Tam Remote Procedure Call'un vaat ettiği şey.

**Client Oluşturma Adımları:**
1. Proto dosyasını yükle (server ile AYNI proto!) — kontrat paylaşımı
2. Client instance oluştur (adres + credentials)
3. Metotları çağır — callback, Promise veya stream bazlı

**⏰ Deadlines — MUTLAKA Koyun, Yoksa Pişman Olursunuz!**

Deadline, gRPC'nin "bu istek en fazla X sürede tamamlanmalı" kuralıdır. Deadline KOYMAZSANIZ ne olur? Client sonsuza kadar bekler. Thread'ler tıkanır. Uygulama donar. Kullanıcı "bu uygulama çöktü" der, 1-star review bırakır.

```javascript
// Deadline OLMADAN (TEHLİKELİ — sonsuza kadar bekleyebilir!)
client.GetUser({ user_id: '123' }, callback);

// Deadline İLE (DOĞRU — 5 saniye sonra timeout)
const deadline = new Date();
deadline.setSeconds(deadline.getSeconds() + 5);
client.GetUser({ user_id: '123' }, { deadline }, callback);
```

Google'ın kendi internal coding guideline'ında "deadline olmayan gRPC çağrısı code review'dan geçemez" yazar. Bu kadar ciddi.

**Load Balancing — HTTP/2'nin Tuzağı:**

gRPC, HTTP/2 kullanır. HTTP/2'nin güzel özelliği multiplexing: tek bir TCP bağlantısı üzerinden yüzlerce istek akar. AMA! Bu, geleneksel load balancing'i BOZAR. Neden?

HTTP/1.1'de her istek ayrı TCP bağlantısı → Load balancer her bağlantıyı farklı backend'e yönlendirir → güzel dağılım ✅
HTTP/2'de TÜM istekler TEK TCP bağlantısı → Load balancer bu bağlantıyı BİR backend'e yönlendirir → tüm yük tek sunucuya ❌

Çözüm: **Client-side load balancing**. Client, birden fazla backend adresini bilir ve istekleri kendisi dağıtır. Kubernetes'te `headless service` kullanarak tüm pod IP'lerini alır, round-robin ile dağıtırsınız.

```javascript
// Client-side load balancing (round-robin)
const client = new userProto.UserService(
  'dns:///user-service.default.svc.cluster.local:50051',  // dns:/// prefix!
  grpc.credentials.createInsecure(),
  {
    'grpc.service_config': JSON.stringify({
      loadBalancingConfig: [{ round_robin: {} }]
    })
  }
);
```

**Channel Options — İnce Ayarlar:**

Production'da default ayarlar YETMEZ. Şu channel option'ları bilin:

| Option | Ne Yapar? | Önerilen Değer |
|--------|-----------|---------------|
| `grpc.keepalive_time_ms` | Bağlantıyı canlı tutmak için ping aralığı | 30000 (30s) |
| `grpc.keepalive_timeout_ms` | Ping cevabı için max bekleme | 10000 (10s) |
| `grpc.max_receive_message_length` | Max gelen mesaj boyutu (byte) | 4MB default, gerekirse artır |
| `grpc.max_send_message_length` | Max giden mesaj boyutu (byte) | 4MB default |
| `grpc.default_compression_algorithm` | Sıkıştırma (gzip, deflate) | gzip (büyük payload'larda %60-80 tasarruf) |

```javascript
// Production-ready client
const client = new userProto.UserService(
  'localhost:50051',
  grpc.credentials.createInsecure(),
  {
    'grpc.keepalive_time_ms': 30000,
    'grpc.keepalive_timeout_ms': 10000,
    'grpc.max_receive_message_length': 1024 * 1024 * 10, // 10MB
    'grpc.default_compression_algorithm': 2, // GZIP
  }
);
```

**Gerçek Dünya:** Google'ın kendi iç sistemlerinde saniyede **10 milyar** gRPC çağrısı yapılıyor. Slack, Netflix, Spotify, Dropbox hepsi mikro servisleri arasında gRPC kullanıyor. gRPC client'ları gerçekten "yerel fonksiyon çağırıyormuş gibi" hissettiriyor — ve bu his, üretkenliği MÜTHIŞ artırıyor. REST'te endpoint URL'si oluştur, HTTP metodu seç, header ekle, body serialize et... gRPC'de? `client.GetUser({ user_id: '123' })`. Nokta. 🚀

```javascript
const client = new userProto.UserService(
  'localhost:50051',
  grpc.credentials.createInsecure()
);

// Unary call
client.GetUser({ user_id: '123' }, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('User:', response);
});

// Server streaming
const stream = client.ListUsers({ page: 0, page_size: 10 });
stream.on('data', (user) => {
  console.log('Received user:', user);
});
stream.on('end', () => {
  console.log('Stream ended');
});
```

### WebSockets & Real-time Communication

#### WebSocket vs SSE vs Long Polling

```
WebSocket:
✓ Full-duplex (bi-directional)
✓ Low latency
✓ Persistent connection
✗ More complex
Use: Chat, gaming, collaborative editing

Server-Sent Events (SSE):
✓ Simple (HTTP)
✓ Auto-reconnect
✓ Event-driven
✗ One-way (server -> client)
Use: Notifications, live feeds, stock tickers

Long Polling:
✓ Works everywhere
✗ Higher latency
✗ More server resources
Use: Fallback mechanism
```

#### WebSocket Implementation

**HTTP normal akış:** Client istek gönderir → Server cevap verir → Bağlantı KAPANIR. Her seferinde yeni bağlantı.

**WebSocket:** Client ve server arasında SÜREKLİ bir kanal açılır. İki taraf da istedikleri zaman mesaj gönderebilir. Ta ki bağlantı kapatılana kadar.

**Analoji:** HTTP = Mektuplaşma (her seferinde zarf aç, yaz, gönder, bekle). WebSocket = Telefon görüşmesi (hat açık, istediğin zaman konuş). 📞

**Ne zaman WebSocket?**
- ✅ Chat uygulamaları (WhatsApp, Slack)
- ✅ Canlı bildirimler (Getir sipariş durumu!)
- ✅ Multiplayer oyunlar
- ✅ Canlı borsa/kripto fiyatları
- ❌ E-ticaret ürün listesi (REST yeterli)
- ❌ Dosya upload (HTTP daha uygun)

**ÖNEMLİ Production Götcha'lar:**
1. **Ölçekleme ZORDUR:** Her WebSocket bağlantısı bir TCP connection tutar. 10K kullanıcı = 10K açık bağlantı! Birden fazla sunucuda bağlantıları yönetmek için Redis Pub/Sub veya Redis Adapter kullanmalısın.
2. **Reconnection:** Ağ kesildiğinde client otomatik yeniden bağlanmalı (exponential backoff ile).
3. **Heartbeat:** Bağlantının hala CANLI olduğunu anlamak için ping/pong mesajları gönder.
```javascript
// Server (ws library)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws, req) => {
  console.log('Client connected');
  
  // Send welcome message
  ws.send(JSON.stringify({
    type: 'welcome',
    message: 'Connected to server'
  }));
  
  // Receive messages
  ws.on('message', (data) => {
    const message = JSON.parse(data);
    
    // Broadcast to all clients
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({
          type: 'message',
          data: message,
          timestamp: Date.now()
        }));
      }
    });
  });
  
  // Handle disconnect
  ws.on('close', () => {
    console.log('Client disconnected');
  });
  
  // Heartbeat (keep-alive)
  const interval = setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.ping();
    }
  }, 30000);
  
  ws.on('close', () => clearInterval(interval));
});

// Client
const ws = new WebSocket('ws://localhost:8080');

ws.onopen = () => {
  console.log('Connected');
  ws.send(JSON.stringify({ text: 'Hello server!' }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
};

ws.onerror = (error) => {
  console.error('Error:', error);
};

ws.onclose = () => {
  console.log('Disconnected');
};
```

#### Socket.IO (Enhanced WebSockets)

Socket.IO ile WebSocket arasındaki farkı anlamak çok önemli çünkü bu ikisi **aynı şey değil**. WebSocket bir *protokol*, Socket.IO ise bunun üzerine inşa edilmiş bir *framework*tir. Hatta Socket.IO, bir WebSocket kütüphanesi bile değildir — kendi protokolünü kullanır! Yani bir Socket.IO client'ı raw WebSocket server'a bağlanamaz, tersi de geçerlidir. Bu, insanların en sık yaptığı yanılgıdır.

Peki Socket.IO, raw WebSocket'e ne **ekler**?
- 🔄 **Auto-reconnection**: Bağlantı koparsa otomatik yeniden bağlanır. WebSocket'te bunu kendiniz yazmanız gerekir.
- 📡 **Fallback mekanizması**: Eğer WebSocket kullanılamıyorsa (eski proxy, firewall), HTTP long-polling'e düşer. Kullanıcı farkı bile hissetmez.
- 🏠 **Rooms**: Socket'leri gruplama. Bir chat odası düşünün — `socket.join('oda-42')` dediğinizde o socket artık oda-42'nin üyesidir. `io.to('oda-42').emit('mesaj', data)` dediğinizde sadece o odadakilere gider.
- 🔀 **Namespaces**: Ayrı iletişim kanalları. Aynı sunucu üzerinde `/chat`, `/notifications`, `/admin` gibi farklı namespace'ler oluşturabilirsiniz. Her biri bağımsız çalışır.
- 💓 **Heartbeat/Ping-Pong**: Bağlantının canlı olup olmadığını otomatik kontrol eder.
- 📦 **Binary support**: Dosya, resim, ses gibi binary veri gönderebilirsiniz.

**Rooms ve Namespaces — analoji ile:**
Bir **namespace**, bir binadaki farklı **katlar** gibidir. `/chat` katı, `/notifications` katı, `/live-scores` katı. Her katın kendi kapısı, kendi asansörü var. **Room** ise o kattaki **odalar**dır. Chat katında (namespace) "genel-sohbet" odası, "backend-takımı" odası, "random" odası olabilir.

**Scaling Sorunu — dikkat!**
Socket.IO tek bir sunucuda harika çalışır. Ama birden fazla sunucu (Node.js instance) kullandığınızda sorun başlar: Bir kullanıcı A sunucusuna, diğeri B sunucusuna bağlıysa, `io.to('oda-42').emit()` sadece o sunucudaki socket'lere gider. Çözüm:
1. **Sticky sessions**: Load balancer'ın aynı kullanıcıyı hep aynı sunucuya yönlendirmesi
2. **Redis Adapter** (`@socket.io/redis-adapter`): Sunucular arası mesaj senkronizasyonu. Redis pub/sub kullanarak tüm instance'lar arasında koordinasyon sağlar — **production'da bu şart!**

> 💬 **Gerçek Dünya:** Slack benzeri chat uygulamaları, Google Docs tarzı collaborative editing, canlı dashboard'lar, müzayede siteleri (teklif anında herkese broadcast), canlı skor takibi... Hepsi Socket.IO'nun parlayan kullanım alanları.

**Ne Zaman Socket.IO Kullanmamalı?**
- 🎮 **Online gaming**: Milisaniye seviyesinde latency kritikse, Socket.IO'nun overhead'i kabul edilemez. Raw WebSocket veya UDP tabanlı çözümler tercih edin.
- 📈 **Finansal trading**: Her mikrosaniye önemli. Raw WebSocket + binary protocol (Protobuf) daha mantıklı.
- 📺 **Video/audio streaming**: Bunun için WebRTC var. Socket.IO signaling için kullanılabilir ama medya akışı için değil.

Kısacası Socket.IO, *"raw WebSocket çok düşük seviye, ben işimi hızlı halletmek istiyorum"* diyen developer'lar için mükemmel bir seçimdir. Ama *"her nanosaniye önemli"* diyorsanız, raw WebSocket dünyasına hoş geldiniz.

```javascript
// Server
const io = require('socket.io')(3000, {
  cors: { origin: '*' }
});

io.on('connection', (socket) => {
  console.log('User connected:', socket.id);
  
  // Join room
  socket.on('join', (room) => {
    socket.join(room);
    io.to(room).emit('user-joined', socket.id);
  });
  
  // Send to specific room
  socket.on('message', ({ room, text }) => {
    io.to(room).emit('message', {
      userId: socket.id,
      text,
      timestamp: Date.now()
    });
  });
  
  // Private message
  socket.on('private-message', ({ to, text }) => {
    io.to(to).emit('private-message', {
      from: socket.id,
      text
    });
  });
  
  socket.on('disconnect', () => {
    console.log('User disconnected:', socket.id);
  });
});

// Client
const socket = io('http://localhost:3000');

socket.on('connect', () => {
  console.log('Connected:', socket.id);
  socket.emit('join', 'room-123');
});

socket.on('message', (data) => {
  console.log('Message:', data);
});

socket.emit('message', {
  room: 'room-123',
  text: 'Hello everyone!'
});
```

#### Server-Sent Events (SSE)

SSE'yi anlamanın en kolay yolu şu analoji: **haber ticker'ı**. Borsanın alt kısmında akan o yazılar var ya — sürekli sunucudan size bilgi akıyor, ama siz ticker'a bir şey yazamıyorsunuz. İşte SSE tam olarak budur: **sunucudan istemciye tek yönlü, sürekli bir veri akışı**.

WebSocket ile karşılaştıralım:
| | SSE | WebSocket |
|---|---|---|
| Yön | Tek yönlü (sunucu → istemci) | Çift yönlü |
| Protokol | Sade HTTP | Kendi protokolü (ws://) |
| Reconnection | **Otomatik!** (built-in) | Manuel yazmanız lazım |
| Binary data | Hayır, sadece text | Evet |
| Karmaşıklık | Çok basit | Daha karmaşık |
| Proxy/Firewall | HTTP olduğu için sorunsuz geçer | Bazen engellenir |

SSE'nin en büyük avantajı **sadeliği**dir. Sunucu tarafında `Content-Type: text/event-stream` header'ı ile bir HTTP response açarsınız, `data: ...\n\n` formatında veri gönderirsiniz, o kadar. İstemci tarafında tek satır: `new EventSource('/events')`. Kütüphane yok, npm install yok, polyfill yok — **tarayıcıda native `EventSource` API'si var!**

**Ne Zaman SSE Kullanılır?**
- 📰 **Canlı bildirimler**: "Siparişiniz kargoya verildi" bildirimi
- 📊 **Real-time dashboard'lar**: Sunucu metrikleri, borsa fiyatları, skor tabloları
- 📝 **Canlı feed'ler**: Twitter/X timeline güncellemeleri, haber akışları
- 🔄 **Progress updates**: Uzun süren bir işlemin ilerlemesi (dosya yükleme, rapor oluşturma)
- 🤖 **AI streaming responses**: ChatGPT'nin cevabı kelime kelime yazdığını gördünüz mü? İşte o SSE!

Ortak nokta: hepsinde **istemcinin sunucuya veri göndermesine gerek yok**. Sadece dinliyor. Eğer çift yönlü iletişim gerekiyorsa, SSE yerine WebSocket tercih edin.

**Önemli Sınırlama — HTTP/1.1 bağlantı limiti:**
HTTP/1.1'de tarayıcılar aynı domain'e **maksimum 6 eşzamanlı bağlantı** açar. Eğer her tab bir SSE bağlantısı açıyorsa, 6 tab = limit doldu, yeni bağlantı açılamaz! Çözüm: **HTTP/2 kullanın**. HTTP/2 multiplexing sayesinde tek bir TCP bağlantısı üzerinden yüzlerce stream taşınabilir. Modern altyapılarda bu sorun büyük ölçüde ortadan kalkmıştır.

> 🧠 **Pro Tip:** Eğer *"WebSocket mi SSE mi?"* diye düşünüyorsanız, kendinize şu soruyu sorun: *"İstemcinin sunucuya mesaj göndermesi gerekiyor mu?"* Hayır ise → SSE. Evet ise → WebSocket. Bu kadar basit.

```javascript
// Server
app.get('/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  
  // Send event every 5 seconds
  const intervalId = setInterval(() => {
    res.write(`data: ${JSON.stringify({
      time: new Date().toISOString(),
      value: Math.random()
    })}\n\n`);
  }, 5000);
  
  // Cleanup on disconnect
  req.on('close', () => {
    clearInterval(intervalId);
  });
});

// Client
const eventSource = new EventSource('/events');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
};

eventSource.onerror = (error) => {
  console.error('Error:', error);
  eventSource.close();
};
```

---

## 🗄️ Database & Data Management

### Relational Databases

Relational database nedir? En basit anlatımla: **birbiriyle ilişkili Excel tablolarıdır.** Bir "Müşteriler" tablonuz var, bir "Siparişler" tablonuz var. Her siparişin hangi müşteriye ait olduğunu bir `customer_id` ile belirtirsiniz. İşte bu "ilişki" (relation) kavramı, relational database'lere adını veren şeydir. 1970'te IBM'de Edgar F. Codd bu modeli ortaya attığında, veri dünyası sonsuza dek değişti.

**SQL: Verinin Evrensel Dili**

SQL (Structured Query Language) 1974'te ortaya çıktı — yani 50 yılı aşkın süredir hayatımızda! Ve hâlâ en çok aranan teknik becerilerden biri. Neden? Çünkü SQL **deklaratif** bir dildir: "Ne istediğini söyle, nasıl yapılacağını ben hallederim" der. `SELECT * FROM users WHERE age > 25` yazdığınızda, veritabanı motoru indexleri kontrol eder, query plan oluşturur, en optimal yolu bulur — siz sadece sonucu alırsınız. JavaScript'te 20 satır yazacağınız şeyi SQL'de 2 satırda yaparsınız.

Analoji ile: SQL bir restoranda garson gibidir. "Bana az pişmiş bir bonfile, yanında patates püresi" dersiniz. Mutfakta etin nasıl hazırlandığını, patateslerin nasıl ezildiğini bilmenize gerek yok. 🍽️

**ACID: Bankalar Neden Relational DB Kullanır?**

ACID, relational database'lerin en güçlü silahıdır:
- **A**tomicity: İşlem ya TAMAMEN yapılır, ya HİÇ yapılmaz. Banka havalesinde paranız hesaptan çıktı ama karşı tarafa geçmedi mi? Atomicity sayesinde bu İMKANSIZ — işlem rollback edilir.
- **C**onsistency: Veritabanı her zaman tutarlı bir durumda kalır. Tanımladığınız kurallar (constraints) her zaman geçerlidir.
- **I**solation: Eşzamanlı işlemler birbirini görmez. İki kişi aynı anda aynı ürünü almaya çalışırsa, biri bekler.
- **D**urability: İşlem onaylandıktan sonra, sunucu çökse bile veri kaybolmaz. Diske yazıldı mı, yazıldı.

Bu yüzden bankalar, finans kurumları, sağlık sistemleri — yani **veri kaybının kabul edilemez** olduğu her yerde relational database görürsünüz.

**Ne Zaman Relational Database?**
- ✅ Yapılandırılmış (structured) veri — şemanız bellidir, sık değişmez
- ✅ Karmaşık sorgular — JOIN'ler, alt sorgular, window functions
- ✅ Transaction'lar — para transferi, envanter yönetimi, sipariş işleme
- ✅ Veri bütünlüğü kritik — foreign key, unique constraint, check constraint
- ❌ Şeması sürekli değişen veriler (her döküman farklı yapıda)
- ❌ Saniyede milyonlarca yazma operasyonu (horizontal scaling zor)
- ❌ Çok büyük, ilişkisiz veri kümeleri (log, IoT sensör verisi)

#### PostgreSQL

PostgreSQL'e "dünyanın en gelişmiş açık kaynak veritabanı" denmesinin bir sebebi var — ve bu sadece pazarlama değil. PostgreSQL, 1986'da UC Berkeley'de başlayan bir akademik proje (POSTGRES) olarak doğdu ve 35+ yıl boyunca sürekli gelişti. Bugün, diğer veritabanlarının "yeni özellik" diye sunduğu şeylerin çoğunu PostgreSQL yıllardır yapıyordu.

**PostgreSQL vs MySQL — Hangisini Seçmeli?**

| Özellik | PostgreSQL | MySQL |
|---|---|---|
| **JSONB desteği** | ✅ Mükemmel (GIN index ile) | ⚠️ JSON var ama sınırlı |
| **Array tipi** | ✅ Native array desteği | ❌ Yok |
| **CTE (WITH queries)** | ✅ Recursive CTE dahil | ⚠️ MySQL 8.0+ ile geldi |
| **Full-text search** | ✅ Built-in, güçlü | ⚠️ Temel düzeyde |
| **Window Functions** | ✅ Kapsamlı | ⚠️ MySQL 8.0+ ile geldi |
| **Öğrenme eğrisi** | Daha dik | Daha kolay |
| **Yaygınlık** | Hızla büyüyor | Daha yaygın (LAMP stack) |
| **Replication** | Logical + Physical | Daha kolay kurulum |

Kısa özet: **PostgreSQL = daha fazla özellik, daha güçlü.** MySQL = daha basit, daha yaygın. Sıfırdan yeni bir proje başlıyorsanız? PostgreSQL. Legacy WordPress/PHP projeniz varsa? MySQL.

**JSONB: İki Dünyanın En İyisi**

PostgreSQL'in en havalı özelliklerinden biri JSONB. "Ama bekle, relational database'de JSON mı saklıyoruz?" diye sorabilirsiniz. EVET! Ve bu çok güçlü bir pattern. Düşünün: kullanıcı profili var, herkeste `name` ve `email` alanı aynı (relational sütunlar). Ama `preferences` alanı? Her kullanıcıda farklı olabilir — biri tema rengi saklar, biri bildirim tercihleri, biri dil ayarları. İşte bu değişken kısmı JSONB olarak saklarsınız. Relational'ın disiplini + Document'ın esnekliği = BİR veritabanında!

Üstelik JSONB üzerinde GIN index oluşturabilirsiniz — yani JSON içinde arama yapmak BİLE hızlıdır.

**Full-Text Search: Elasticsearch'e İhtiyacınız Olmayabilir**

Birçok uygulama için PostgreSQL'in built-in full-text search özelliği yeterlidir. `tsvector` ve `tsquery` ile metin arama yapabilirsiniz. Dil desteği var (Türkçe dahil!), stemming var, ranking var. Ürün araması, blog araması, basit arama ihtiyaçları için ayrı bir Elasticsearch cluster kurmak yerine PostgreSQL'in FTS'ini kullanmak hem maliyet hem de karmaşıklık açısından büyük avantaj.

Elbette, Elasticsearch'ün sunduğu fuzzy search, synonym handling, aggregation gibi gelişmiş özellikler gerekiyorsa, o zaman Elasticsearch'e geçiş yaparsınız. Ama önce PostgreSQL'i deneyin — %80 ihtimalle yeterli olacaktır.

**Partitioning: Milyarlarca Satırı Yönetmek**

Tablonuz 100 milyon satırı geçtiğinde sorgular yavaşlamaya başlar. Partitioning ile tabloyu mantıksal parçalara bölersiniz. En yaygın strateji: `RANGE partitioning` — örneğin log tablosunu aya göre bölmek. `SELECT * FROM logs WHERE created_at > '2024-01-01'` sorgusu sadece ilgili partition'ı tarar, tüm tabloyu değil. 100x hızlanma mümkün!

**Extension Ekosistemi:**
- **PostGIS:** Coğrafi veriler için. "Bana 5 km içindeki restoranları bul" gibi sorgular.
- **pg_stat_statements:** En yavaş sorgularınızı bulmanızı sağlar. Performance tuning'in ilk adımı.
- **TimescaleDB:** Zaman serisi verileri için (IoT, metrikler). PostgreSQL'i bir time-series DB'ye dönüştürür.
- **pg_cron:** Veritabanı içinde cron job'lar çalıştırma.
- **uuid-ossp:** UUID v4 üretimi.

**Gerçek Dünya:** Instagram (milyarlarca fotoğraf metadatası), Spotify (müzik kataloğu ve kullanıcı verileri), Apple (CloudKit altyapısı), Reddit, Twitch — hepsi PostgreSQL kullanıyor. Hatta Uber bir ara PostgreSQL'den MySQL'e geçti, sonra pişman olup tekrar döndü! 😄

**Advanced Features:**
```sql
-- JSONB support (document + relational)
CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  event_type VARCHAR(50),
  payload JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_payload ON events USING GIN (payload);

SELECT * FROM events WHERE payload @> '{"userId": "123"}';

-- Full-text search
CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  search_vector tsvector
);

CREATE INDEX idx_search ON articles USING GIN (search_vector);

UPDATE articles SET search_vector = 
  to_tsvector('english', title || ' ' || content);

SELECT * FROM articles 
WHERE search_vector @@ to_tsquery('postgresql & performance');

-- Partitioning (large tables)
CREATE TABLE logs (
  id BIGSERIAL,
  created_at TIMESTAMP,
  message TEXT
) PARTITION BY RANGE (created_at);

CREATE TABLE logs_2024_01 PARTITION OF logs
  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

**Connection Pooling:**
```javascript
// pg-pool
const { Pool } = require('pg');

const pool = new Pool({
  host: 'localhost',
  database: 'mydb',
  max: 20, // Maximum connections
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});

// Use pool for queries
const result = await pool.query('SELECT * FROM users WHERE id = $1', [userId]);
```

#### MySQL/MariaDB
**When to use:**
- Simple read-heavy workloads
- WordPress, eCommerce platforms
- Replication setup

### NoSQL Databases

NoSQL — bu isim çok yanıltıcı. İnsanlar "SQL karşıtı" diye anlıyor ama aslında **"Not Only SQL"** anlamına geliyor. Yani "sadece SQL değil, başka yollar da var" demek. NoSQL bir savaş ilanı değil, bir alternatif.

**Peki neden böyle bir alternatife ihtiyaç duyuldu?**

2000'lerin başında internet patladı. Facebook günde milyarlarca post, Google petabaytlarca veri, Amazon saniyede yüz binlerce sipariş işliyordu. Ve geleneksel relational database'ler bu ölçekte zorlanmaya başladı. Neden? Çünkü relational DB'ler **vertical scaling** (daha güçlü sunucu alarak büyüme) gerektirir — ve bir sunucunun ne kadar güçlü olabileceğinin bir sınırı var. NoSQL ise **horizontal scaling** için tasarlandı — veriyi birden fazla sunucuya dağıtmak. 10 sunucu yetmiyor mu? 100 yap. Hâlâ yetmiyor? 1000 yap.

**NoSQL Türleri — Her Biri Farklı Bir İhtiyaç İçin:**

| Tür | Örnek | Ne İçin? | Analoji |
|---|---|---|---|
| **Document** | MongoDB, CouchDB | Esnek şema, JSON benzeri belgeler | Dosya dolabı (her dosyanın içeriği farklı olabilir) |
| **Key-Value** | Redis, DynamoDB | Ultra hızlı okuma/yazma, basit erişim | Sözlük (kelime → anlam) |
| **Column-Family** | Cassandra, HBase | Zaman serisi, çok büyük veri setleri | Excel ama sütunlar dinamik |
| **Graph** | Neo4j, Neptune | İlişki ağları, sosyal graflar | Zihin haritası (düğümler ve bağlantılar) |

**Ne Zaman NoSQL?**
- ✅ Şeması sık değişen veriler (her döküman farklı yapıda olabilir)
- ✅ Yatay ölçekleme gerekli (milyarlarca kayıt, dağıtık mimari)
- ✅ Belirli erişim kalıpları (key ile hızlı erişim, tam tablo taraması yok)
- ✅ Yüksek yazma throughput'u (log, event, IoT verisi)
- ❌ Karmaşık JOIN'ler ve ilişkiler (relational daha iyi)
- ❌ ACID transaction'lar kritik (çoğu NoSQL eventual consistency tercih eder)

**⚠️ Yaygın Hata: "Trendy olduğu için NoSQL kullanalım!"**

Bu hatayı ÇOK görüyorum. Startup'lar "MongoDB cool, hadi MongoDB kullanalım" deyip sonra 6 ay sonra "şu tabloları JOIN etmemiz lazım ama yapamıyoruz" diye ağlıyor. Eğer veriniz ilişkisel, şemanız belli ve transaction'lar önemliyse — PostgreSQL kullanın. Kimse sizi yargılamaz. **Doğru araç, doğru iş için.** NoSQL'i bir çözüm olarak değil, belirli problemler için bir araç olarak görün.

#### DynamoDB

DynamoDB, AWS'nin tamamen yönetilen (fully managed) NoSQL veritabanıdır. "Fully managed" ne demek? Sunucu yok, cluster yok, patch yok, backup konfigürasyonu yok — AWS HER ŞEYİ halleder. Siz sadece tablo oluşturur, veri yazarsınız. Scaling? OTOMATİK. Availability? %99.999 SLA (yani yılda SADECE 5 dakika downtime!). Bu, DynamoDB'yi "sıfır operasyon" servisi yapar.

**Single-Table Design: SQL Geliştiricilerin Beyni Yanan Konsept**

Relational dünyadan geliyorsanız, DynamoDB'nin en şaşırtıcı yanı **single-table design** olacak. SQL'de "users" tablosu, "orders" tablosu, "products" tablosu yaparsınız. DynamoDB'de? TEK bir tablo! Tüm entity'leri tek tabloda, Partition Key ve Sort Key kombinasyonlarıyla saklarsınız. `PK: USER#123, SK: PROFILE#123` bir kullanıcı. `PK: USER#123, SK: ORDER#456` aynı kullanıcının bir siparişi. Bu yaklaşım başta çılgınca görünür ama bir sebebi var: DynamoDB'de JOIN yoktur, ve tek tabloda ilişkili verilere tek query ile erişebilirsiniz.

**Partition Key = Verinin Adresi**

Partition Key, verinin hangi fiziksel sunucuda (partition) saklanacağını belirler. Bu seçim KRİTİKTİR:
- İyi PK: `userId` — her kullanıcının verisi eşit dağılır ✅
- Kötü PK: `country` — Türkiye partition'ı patlar, Lihtenştayn partition'ı boş kalır ❌ (hot partition!)
- Kural: **Yüksek kardinalite + eşit dağılım** = iyi partition key

**On-Demand vs Provisioned Capacity:**
- **On-Demand:** İstek başına ödeme. Trafik öngörülemeyen uygulamalar için ideal. Gece 0, gündüz 10K request? Sorun değil.
- **Provisioned:** Sabit kapasite rezerve edersiniz (RCU/WCU). Tahmin edilebilir trafik için %70'e kadar ucuz olabilir. Auto-scaling ile kombine edin.

**Gerçek Dünya:** Amazon.com'un kendisi DynamoDB üzerinde çalışıyor. 2023 Prime Day'de DynamoDB **saniyede 89.2 MİLYON request** işledi. Trilyon request, sıfır downtime. Ayrıca Lyft, Samsung, Capital One, Airbnb gibi devler de DynamoDB kullanıyor. Eğer "sınırsız ölçek, sıfır yönetim" istiyorsanız, DynamoDB cevabınız.

**Key Concepts:**
```javascript
// Single-table design pattern
const AWS = require('aws-sdk');
const dynamodb = new AWS.DynamoDB.DocumentClient();

// Partition Key + Sort Key
const params = {
  TableName: 'MyApp',
  Item: {
    PK: 'USER#123',           // Partition Key
    SK: 'PROFILE#123',        // Sort Key
    email: 'user@example.com',
    name: 'John Doe',
    GSI1PK: 'EMAIL#user@example.com',  // Global Secondary Index
    GSI1SK: 'USER#123'
  }
};

await dynamodb.put(params).promise();

// Query by partition key
const users = await dynamodb.query({
  TableName: 'MyApp',
  KeyConditionExpression: 'PK = :pk',
  ExpressionAttributeValues: { ':pk': 'USER#123' }
}).promise();

// Query by GSI
const userByEmail = await dynamodb.query({
  TableName: 'MyApp',
  IndexName: 'GSI1',
  KeyConditionExpression: 'GSI1PK = :email',
  ExpressionAttributeValues: { ':email': 'EMAIL#user@example.com' }
}).promise();
```

**Best Practices:**
- Single-table design (denormalization)
- Use composite keys
- Watch for hot partitions
- DynamoDB Streams for change data capture

#### MongoDB

MongoDB, dünyanın en popüler **document database**'idir. "Document" derken Word dökümanı değil, **JSON benzeri belgeler** kastediliyor. Her bir kayıt (document) bir JSON objesidir ve her document'ın yapısı farklı olabilir. SQL'de tablo şeması değiştirmek için `ALTER TABLE` çalıştırırsınız ve bu migration süreci bazen saatler sürer. MongoDB'de? Yeni bir alan eklemek istiyorsanız, sadece yeni document'a o alanı eklersiniz. Eski document'lar etkilenmez. Bu esneklik, MongoDB'yi "hızlı iterasyon" gerektiren projelerde süper güçlü yapar.

**Analoji:** SQL veritabanı bir **matbaa** gibidir — önce kalıbı (şemayı) hazırlarsınız, sonra aynı formatta binlerce kopya basarsınız. MongoDB ise bir **defter** gibidir — her sayfaya istediğinizi, istediğiniz formatta yazarsınız. Bir sayfada tablo var, diğerinde çizim, bir diğerinde metin. 📓

**MongoDB Ne Zaman Parlar?**
- ✅ **Content Management (CMS):** Blog yazıları, makaleler — her içeriğin farklı alanları olabilir (video, galeri, anket...)
- ✅ **Kullanıcı Profilleri:** Her kullanıcının farklı tercih ve ayar alanları olabilir
- ✅ **Ürün Katalogları:** Bir tişört ile bir laptop'un özellikleri tamamen farklıdır — flexible schema ideal
- ✅ **Rapid Prototyping:** Startup'lar MVP yaparken şema değişiklikleri çok sık olur, MongoDB bu hıza ayak uydurur
- ❌ Karmaşık ilişkiler ve JOIN'ler gereken durumlar (PostgreSQL'e gidin)
- ❌ Transaction'ların kritik olduğu finans uygulamaları (MongoDB 4.0+ multi-document transaction destekliyor AMA performans maliyeti var)

**Mongoose: Node.js İçin ODM (Object Document Mapper)**

Mongoose, MongoDB'nin Node.js ekosistemindeki en popüler kütüphanesidir. SQL dünyasında Sequelize veya TypeORM ne ise, MongoDB dünyasında Mongoose odur. Schema validation, middleware (pre/post hooks), virtual fields, population (referans çözümleme) gibi özellikler sunar. "Ama MongoDB schema-less değil miydi?" diye sorabilirsiniz — evet, veritabanı seviyesinde schema yoktur, ama uygulama seviyesinde Mongoose ile schema tanımlayarak veri tutarlılığını sağlarsınız. En iyi iki dünya!

**Aggregation Pipeline: MongoDB'nin Gizli Silahı**

Aggregation Pipeline, MongoDB'nin veri işleme framework'üdür. SQL'deki `GROUP BY`, `HAVING`, `JOIN` gibi operasyonların MongoDB karşılığıdır — ama çok daha güçlü ve esnek. Pipeline aşamalardan (stages) oluşur: `$match` → `$unwind` → `$group` → `$sort` → `$limit`. Her aşama veriyi transform eder ve bir sonraki aşamaya geçirir. Unix pipe'ları gibi düşünün: `cat file | grep error | sort | head -10`.

**MongoDB Atlas: Yönetilen MongoDB**

MongoDB Atlas, MongoDB'nin resmi bulut hizmetidir — AWS, GCP veya Azure üzerinde çalışır. Tıpkı RDS'nin PostgreSQL için yaptığı gibi, Atlas da MongoDB için backup, monitoring, scaling, security işlerini halleder. Free tier'ı var — öğrenme ve küçük projeler için mükemmel.

**⚠️ Yaygın Hata: Her Şeyi Embed Etmek**

MongoDB'ye başlayanların en sık yaptığı hata: her ilişkili veriyi document'ın İÇİNE gömmek (embedding). Bir kullanıcının siparişleri? Embed! Siparişin ürünleri? Embed! Ürünün yorumları? Embed! Sonuç: document büyür, büyür, büyür... ve **16MB document boyut sınırına** çarpar. 💥 Kural: sık birlikte okunan veriyi embed edin, bağımsız büyüyen veriyi referans (`ObjectId`) ile bağlayın.

**Gerçek Dünya:** MongoDB'yi Uber (sürücü/yolcu verileri), eBay (ürün kataloğu), Forbes, EA Games ve sayısız startup kullanıyor. Özellikle MVP ve rapid prototyping aşamasında MongoDB'nin esnekliği altın değerinde — şemanızı kafanızda netleştirmeden kod yazmaya başlayabilirsiniz.

**When to use:**
- Flexible schema
- Document-heavy applications
- Rapid prototyping

```javascript
// Mongoose schema
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true, index: true },
  profile: {
    age: Number,
    location: String
  },
  orders: [{
    orderId: mongoose.Schema.Types.ObjectId,
    total: Number,
    date: Date
  }]
});

// Aggregation pipeline
const result = await User.aggregate([
  { $match: { 'profile.age': { $gte: 18 } } },
  { $unwind: '$orders' },
  { $group: {
    _id: '$_id',
    totalSpent: { $sum: '$orders.total' }
  }},
  { $sort: { totalSpent: -1 } },
  { $limit: 10 }
]);
```

#### Redis

Redis'i sadece bir "cache" olarak düşünüyorsanız, ona büyük haksızlık ediyorsunuz. Redis, **in-memory data structure store** — yani bellekte çalışan, çok hızlı bir veri yapısı deposudur. Cache olarak kullanılabilir, evet. Ama aynı zamanda message broker, session store, rate limiter, leaderboard engine, real-time analytics aracı ve daha pek çok şey olabilir. Redis'i sadece cache olarak kullanmak, Ferrari'yi sadece markete gitmek için kullanmak gibidir — işini görür ama potansiyelinin yüzde birini bile kullanmamış olursun.

**Gerçek Dünya Analojisi: Post-it Tahtası vs Dosya Dolabı**

Bir ofis düşünün. Dosya dolabı (disk tabanlı veritabanı) her belgeyi düzenli bir şekilde saklar, ama bir şey bulmak için çekmeceyi açmanız, dosyaları karıştırmanız gerekir — yavaştır. Bir de masanızın yanındaki **post-it tahtası** var (Redis). En sık ihtiyaç duyduğunuz bilgileri oraya yazarsınız: "Müşteri X'in telefon numarası", "Bugünkü toplantı saat 3'te", "Projenin deadline'ı Cuma". Göz atarsınız, anında bulursunuz. Ama tahtanın alanı sınırlıdır — her şeyi oraya yazamazsınız. Ve eğer biri gelip tahtayı silerse (sunucu restart), bilgiler kaybolabilir (persistence ayarlamadıysanız).

Redis tam olarak bu post-it tahtasıdır: **hızlı, sınırlı, ama inanılmaz pratik.**

---

**Redis Veri Yapıları — Hangi Durumda Hangisi?**

Redis'in gücü, sadece key-value olmaktan çok ötesinde, **zengin veri yapıları** sunmasından gelir:

| Veri Yapısı | Ne İşe Yarar? | Gerçek Dünya Örneği |
|---|---|---|
| **String** | En basit yapı. Tek bir değer saklar. Counter olarak da kullanılabilir (`INCR`/`DECR`). | Cache'lenmiş JSON, rate limit sayacı, feature flag değeri |
| **Hash** | Bir key altında birden fazla field-value çifti. Küçük bir obje gibi düşünün. | Kullanıcı session bilgisi (`session:abc → {userId, ip, loginAt}`), ürün detayları |
| **List** | Sıralı bir koleksiyon. Baştan veya sondan ekleme/çıkarma yapılabilir (LPUSH/RPUSH/LPOP/RPOP). | Mesaj kuyruğu, son N aktivite logu, Twitter timeline |
| **Set** | Benzersiz elemanlardan oluşan sırasız koleksiyon. Küme operasyonları yapılabilir (SUNION, SINTER, SDIFF). | Kullanıcının beğendiği ürünler, online kullanıcı listesi, tag sistemi |
| **Sorted Set (ZSet)** | Her elemana bir "score" atanmış sıralı küme. Score'a göre sıralama yapılabilir. | Leaderboard, en çok satılan ürünler, priority queue |
| **Stream** | Append-only log yapısı. Kafka benzeri event streaming için kullanılabilir. Consumer group desteği var. | Event sourcing, audit log, real-time veri akışı |

Bir örnek üzerinden anlatayım: Getir'de bir kullanıcının sepetini düşünün.
- Sepet bilgisini **Hash** ile saklarsınız: `cart:user123 → {item1: 2, item2: 1}`
- Son görüntülenen ürünleri **List** ile tutarsınız: `recent:user123 → [productA, productB, productC]`
- Kullanıcının favorilerini **Set** ile saklarsınız: `favorites:user123 → {productX, productY}` (aynı ürün iki kez eklenmez)
- En çok sipariş veren müşterileri **Sorted Set** ile sıralarsınız: `top_customers → [{user456: 150}, {user789: 120}]`

Her veri yapısı farklı bir problemi çözer. Yanlış yapıyı seçmek, çivi çakmak için tornavida kullanmak gibidir — belki işi görürsünüz ama çok zorlanırsınız.

---

**Redis Persistence: Verilerim Kaybolur mu?**

"Redis in-memory ise sunucu kapanınca her şey uçar mı?" — En sık sorulan soru. Cevap: **Hayır, eğer persistence ayarladıysanız.**

Redis iki persistence mekanizması sunar:

**1. RDB (Redis Database) Snapshots:**
- Belirli aralıklarla (örneğin her 5 dakikada, veya 1000 yazma işleminden sonra) tüm verinin anlık görüntüsünü (snapshot) diske yazar.
- **Avantaj:** Dosya kompakt, yedekleme/taşıma kolay. Restart sonrası hızlı yüklenir.
- **Dezavantaj:** Son snapshot'tan sonraki veriler kaybolabilir. 5 dakikada bir snapshot alıyorsanız, en kötü senaryoda 5 dakikalık veri kaybı yaşarsınız.
- **Analoji:** Her gece uyumadan önce günlüğünüze o günkü önemli olayları yazmanız gibi — sabah hatırlarsınız, ama gece yarısı bir şey olursa son yazdıklarınız kayıptır.

**2. AOF (Append-Only File):**
- Her yazma işlemini bir log dosyasına ekler. Sunucu restart olduğunda bu log'u baştan oynatarak veriyi geri oluşturur.
- **Avantaj:** Çok daha az veri kaybı riski. `appendfsync always` ile sıfır kayıp bile mümkün (ama performans düşer).
- **Dezavantaj:** Dosya büyür, restart süresi uzar. AOF rewrite ile dosya sıkıştırılabilir ama ek CPU yükü getirir.
- **Analoji:** Her yapılan işlemi anında not defterine yazmanız gibi — hiçbir şey kaybolmaz, ama defter giderek kalınlaşır.

**Pratikte ne yapılır?** Çoğu production ortamda **ikisi birden** açılır. RDB hızlı yedekleme için, AOF veri güvenliği için. Redis 7+ ile gelen **RDB-AOF hybrid** mod ise en iyi çözüm: AOF dosyasının başına RDB snapshot'ı koyar, sonrasına AOF loglarını ekler. Hem hızlı yükleme, hem minimum veri kaybı.

---

**Redis Cluster vs Redis Sentinel — Hangisini Ne Zaman Kullanmalı?**

İkisi de "Redis'i production'da güvenilir çalıştırmak" içindir, ama farklı problemleri çözer:

**Redis Sentinel:**
- **Ne yapar?** Master-slave replication üzerine otomatik failover sağlar. Master çökerse, Sentinel slave'lerden birini otomatik olarak yeni master yapar.
- **Ne zaman kullanılır?** Verinin tek bir Redis sunucusunun belleğine sığdığı durumlarda. High availability (yüksek erişilebilirlik) istiyorsanız ama sharding'e ihtiyacınız yoksa.
- **Kapasite:** Dikey ölçekleme — daha büyük sunucu al.

**Redis Cluster:**
- **Ne yapar?** Veriyi birden fazla node'a **otomatik olarak dağıtır** (sharding). Her node verinin bir kısmını tutar. Ayrıca built-in replication ve failover da var.
- **Ne zaman kullanılır?** Veri tek bir sunucunun belleğine sığmadığında. Yüksek throughput gerektiğinde. Yatay ölçekleme istediğinizde.
- **Dikkat:** Multi-key operasyonlar (MGET, pipeline) sadece **aynı slot'taki** key'ler için çalışır. `{user}:profile` ve `{user}:cart` gibi **hash tag** kullanarak ilgili key'leri aynı slot'a yönlendirebilirsiniz.

**Kısa özet:** Verin belleğe sığıyor ve sadece failover istiyorsan → **Sentinel**. Verin çok büyük veya yük çok yüksek → **Cluster**.

---

**Eviction Policies — Bellek Dolduğunda Ne Olur?**

Redis'in belleği sınırlıdır (post-it tahtası analojisini hatırlayın). `maxmemory` limiti dolduğunda Redis ne yapmalı? İşte eviction policy burada devreye girer:

| Policy | Davranış | Ne Zaman Kullanılır? |
|---|---|---|
| **noeviction** | Yeni yazma isteklerini reddeder (hata döner). Mevcut veri korunur. | Veri kaybının kabul edilemez olduğu durumlar. Session store gibi. |
| **allkeys-lru** | Tüm key'ler arasında en uzun süredir erişilmeyeni siler. | Genel amaçlı cache. En yaygın tercih. |
| **volatile-lru** | Sadece TTL set edilmiş key'ler arasında LRU uygular. TTL'siz key'lere dokunmaz. | Kalıcı veri + cache karışık kullanıldığında. |
| **allkeys-lfu** | Tüm key'ler arasında en az erişileni siler (Least Frequently Used). | Bazı key'lerin sürekli "sıcak" olduğu, diğerlerinin nadiren erişildiği senaryolar. |
| **volatile-ttl** | TTL'si en yakın olan key'i siler. | TTL'ye dayalı önceliklendirme istediğinizde. |
| **allkeys-random** | Rastgele bir key siler. | Eşit erişim dağılımı olan, önemli olmayan cache verileri. |

**Kritik uyarı:** Production'da `noeviction` kullandığınızda ve bellek dolduğunda, Redis yazma işlemlerini **reddeder**. Bu da uygulamanızın hata alması demektir. `maxmemory` ve eviction policy'yi bilinçli seçin, yoksa gece 3'te sizi uyandıran alarm olur.

---

**Redis Ne Zaman YANLIŞ Tercih?**

Redis harika bir araçtır ama **her problem için doğru çözüm değildir:**

1. **Verinin tamamı belleğe sığmıyorsa:** 500 GB veri mi var? Redis için bu astronomik bir maliyet. Disk tabanlı veritabanı (PostgreSQL, MongoDB) veya Redis on Flash gibi çözümlere bakın.

2. **Karmaşık sorgular gerekiyorsa:** "Şu tarihteki, şu kategorideki, şu fiyat aralığındaki ürünleri bul" gibi sorgular? Redis bunun için tasarlanmadı. SQL veya Elasticsearch kullanın.

3. **ACID transaction garantisi gerekiyorsa:** Redis'in MULTI/EXEC'i var ama bu gerçek bir ACID transaction değil. Finansal işlemler, stok yönetimi gibi kritik işler için ilişkisel veritabanı şart.

4. **Veri ilişkileri karmaşıksa:** JOIN'ler, foreign key'ler, nested ilişkiler? Redis key-value mantığında çalışır, ilişkisel veri modeli için uygun değildir.

5. **Cold data (nadir erişilen veri) saklıyorsanız:** 3 yıl önceki log kayıtlarını Redis'te tutmak, altın tabakta ekmek servis etmek gibidir — gereksiz lüks.

---

**Gerçek Dünya Örnekleri**

🔸 **Getir — Session Store:** Milyonlarca kullanıcının session bilgisi Redis Hash'lerinde saklanır. Kullanıcı her istek attığında session bilgisi milisaniyeler içinde doğrulanır. TTL ile eski session'lar otomatik temizlenir.

🔸 **Twitter — Timeline Cache:** Timeline'ınızdaki tweet'ler Redis List'lerinde tutulur. Yeni bir tweet geldiğinde LPUSH ile listenin başına eklenir, LTRIM ile liste belirli bir boyutta tutulur. "Fan-out on write" stratejisi ile her takipçinin timeline list'ine tweet anında eklenir.

🔸 **Gaming Leaderboard:** Bir mobil oyunda milyonlarca oyuncunun sıralamasını düşünün. Redis Sorted Set ile `ZADD leaderboard 1500 "player123"` diyerek oyuncunun skorunu eklersiniz. `ZREVRANGE leaderboard 0 9` ile top 10'u milisaniyede alırsınız. `ZRANK leaderboard "player123"` ile oyuncunun sıralamasını öğrenirsiniz. Bunu PostgreSQL ile yapmaya çalışsanız, milyonlarca satırda `ORDER BY score DESC` çekmeniz gerekirdi — çok yavaş.

---

**Production'da Sık Karşılaşılan Gotcha'lar**

⚠️ **Memory Limit Bilmezliği:** `maxmemory` ayarlamadan production'a çıkmak, fren kontrolü yapmadan otobana çıkmak gibidir. Redis belleği tüketir, OOM killer devreye girer, process ölür, kullanıcılar hata alır. **Her zaman** `maxmemory` ve uygun eviction policy set edin.

⚠️ **Big Keys (Dev Anahtarlar):** 100 MB'lık bir String veya 1 milyon elemanlı bir Set? Bu bir felaket reçetesi. Big key'ler:
- `DEL` komutu çalıştırıldığında Redis'i **bloklar** (single-threaded olduğunu unutmayın!)
- Network trafiğini patlatır
- Failover süresini uzatır
- **Çözüm:** Büyük verileri parçalara bölün. `UNLINK` (async delete) kullanın. `redis-cli --bigkeys` ile big key'leri tespit edin.

⚠️ **Hot Key Problemi:** Tek bir key'e saniyede milyonlarca istek geliyorsa (örneğin viral bir ürünün cache'i), o key'in bulunduğu node aşırı yüklenir. Cluster bile bunu çözmez çünkü bir key sadece bir node'da bulunur.
- **Çözüm:** Key'i replikalara dağıtın (`product:123:replica1`, `product:123:replica2`), client tarafında random seçim yapın. Veya local cache (application-level cache) ile Redis'e olan yükü azaltın.

⚠️ **KEYS Komutu:** Production'da `KEYS *` çalıştırmak, Redis'in single-threaded yapısını düşününce, tüm sistemi **dondurmak** demektir. Bunun yerine `SCAN` kullanın — cursor-based, non-blocking iteration sağlar.

⚠️ **Thundering Herd (Cache Stampede):** Popüler bir key'in TTL'si dolduğunda, yüzlerce istek aynı anda cache miss yaşar ve hepsi veritabanına koşar. Veritabanı çöker.
- **Çözüm:** Mutex/lock ile sadece bir isteğin cache'i yenilemesini sağlayın. Veya TTL'ye jitter (rastgele süre) ekleyerek cache'lerin aynı anda expire olmasını engelleyin.

---

**Use Cases:**
```javascript
const redis = require('redis');
const client = redis.createClient();

// Caching
await client.setEx('user:123', 3600, JSON.stringify(userData));
const cached = await client.get('user:123');

// Session management
await client.hSet('session:abc123', {
  userId: '123',
  loginAt: Date.now(),
  ip: '1.2.3.4'
});

// Rate limiting
const key = `rate:${userId}:${endpoint}`;
const count = await client.incr(key);
if (count === 1) {
  await client.expire(key, 60); // 1 dakika TTL
}
if (count > 100) {
  throw new Error('Rate limit exceeded');
}

// Pub/Sub
await client.subscribe('notifications', (message) => {
  console.log('Received:', message);
});

await client.publish('notifications', JSON.stringify({ 
  type: 'NEW_ORDER', 
  orderId: '12345' 
}));

// Leaderboard (Sorted Sets)
await client.zAdd('leaderboard', { score: 1500, value: 'player1' });
const top10 = await client.zRange('leaderboard', 0, 9, { REV: true });
```

### Data Consistency Patterns

#### ACID vs BASE

**Data consistency** nedir? Basit bir ATM analojisi düşün: ATM'den 100₺ çektin. Bakiyen 1000₺'ydi. Şimdi bakiyen KESİNLİKLE 900₺ olmalı. Eğer para çıktı ama bakiye hâlâ 1000₺ gösteriyorsa — tebrikler, bankayı hackledin (şaka, banka seni bulur 😄). İşte **data consistency**, verinin her zaman doğru ve tutarlı kalmasını garanti etmektir.

Ancak dağıtık sistemlerde tutarlılığı sağlamak o kadar kolay değil. İşte burada **CAP Theorem** sahneye çıkıyor:

🔺 **CAP Theorem** — Dağıtık bir sistemde aynı anda yalnızca 3'ünden 2'sini seçebilirsin:
- **C**onsistency (Tutarlılık): Her okuma en son yazılan veriyi döner
- **A**vailability (Erişilebilirlik): Her istek bir yanıt alır (hata olsa bile)
- **P**artition Tolerance (Bölünme Toleransı): Ağ bölünmeleri olsa bile sistem çalışmaya devam eder

Gerçek dünyada **P (Partition Tolerance)** zorunludur — ağ HER ZAMAN bölünebilir. Yani gerçek seçim **CP vs AP**'dir:
- **CP (Consistency + Partition Tolerance):** "Eski veri vermektense hiç veri verme" → MongoDB (strong consistency mode), HBase
- **AP (Availability + Partition Tolerance):** "Eski veri olsa da bir şeyler göster" → Cassandra, DynamoDB, CouchDB

---

🏦 **ACID — Banka Hikayesi ile Anlatalım:**

Ahmet, Mehmet'e 500₺ transfer ediyor. Bu işlem 2 adımdan oluşur:
1. Ahmet'in hesabından 500₺ düş
2. Mehmet'in hesabına 500₺ ekle

Şimdi hayal et: Adım 1 tamamlandı (Ahmet'ten 500₺ düştü) ama tam o anda sunucu ÇÖKTÜ. Adım 2 hiç çalışmadı. Sonuç? 500₺ havada kayboldu! Ahmet'ten düştü ama Mehmet'e ulaşmadı. İşte **ACID** bunu önler:

- **Atomicity (Bölünmezlik):** Ya İKİ adım da çalışır, ya HİÇBİRİ. Crash olursa? Adım 1 de geri alınır. "All or nothing" — yarım transfer DİYE BİR ŞEY YOKTUR.
- **Consistency (Tutarlılık):** İşlem öncesi toplam para = 10.000₺, işlem sonrası da 10.000₺ olmalı. Para ne üretilir ne yok olur.
- **Isolation (İzolasyon):** Ayşe aynı anda Ahmet'in bakiyesini sorgulasa, ya transfer ÖNCESİ ya SONRASI halini görür. Asla "yarı transfer" halini göremez.
- **Durability (Kalıcılık):** Transfer tamamlandı ve "başarılı" döndü? Artık sunucunun fişini çeksen bile veri kaybolmaz. Diske yazıldı, bitti.

---

📱 **BASE — Instagram Likes Analojisi:**

Bir post'a 1000. beğeniyi attın. Ama sayaç hâlâ 999 gösteriyor. 2 saniye sonra yeniliyorsun — 1000 oldu! Bu bir BUG değil, bu **BASE**'dir ve KASITLIDIR.

- **Basically Available (Temelde Erişilebilir):** Sistem her zaman yanıt verir. Instagram'ın "beğeni sayısını 2 saniye geç göstermesi" kabul edilebilir, ama "Instagram çöktü, hiç açılmıyor" kabul EDİLEMEZ.
- **Soft State (Yumuşak Durum):** Verinin durumu zaman içinde değişebilir — external input olmadan bile. Replika'lar arası senkronizasyon devam eder.
- **Eventually Consistent (Sonunda Tutarlı):** Yeterli zaman verildiğinde TÜM node'lar aynı veriyi gösterecektir. "Sonunda" ne kadar? Genelde milisaniyeler, bazen saniyeler.

**Gerçek hayattan eventual consistency örneği:** DNS propagation! Bir domain'in DNS kaydını değiştirdiğinde, tüm dünyaya yayılması **24-48 saat** sürebilir. ABD'deki bir kullanıcı yeni IP'yi görürken, Japonya'daki kullanıcı hâlâ eski IP'ye gidebilir. Bu eventual consistency'nin en geniş ölçekli örneğidir.

---

**Ne zaman ACID, ne zaman BASE?**

| Senaryo | ACID ✅ | BASE ✅ |
|---|---|---|
| Banka transferleri, ödeme | ✅ Para kaybolmamalı! | ❌ |
| E-ticaret stok yönetimi | ✅ Overselling felaket | ❌ |
| Uçak bileti rezervasyonu | ✅ Aynı koltuğa 2 kişi? | ❌ |
| Sosyal medya feed | ❌ | ✅ 1 sn gecikme OK |
| Analytics dashboard | ❌ | ✅ Yaklaşık sayı yeter |
| IoT sensor verileri | ❌ | ✅ Milyonlarca event, bazıları geç gelebilir |
| Arama motoru indexleme | ❌ | ✅ Yeni içerik biraz geç indexlenebilir |

**Altın kural:** "Bu veri 1 saniye yanlış olursa ne olur?" sorusuna "kullanıcı para kaybeder" diyorsan → ACID. "Bir şey olmaz" diyorsan → BASE.

```
ACID (Relational):
- Atomicity: All or nothing
- Consistency: Valid state
- Isolation: Concurrent transactions
- Durability: Permanent storage

BASE (NoSQL):
- Basically Available: Always responds
- Soft state: State may change
- Eventual consistency: Eventually consistent
```

#### Saga Pattern (Distributed Transactions)

Monolith dünyada hayat güzeldi. Tek bir veritabanın vardı ve transaction'lar basitti: `BEGIN → işlemler → COMMIT veya ROLLBACK`. Bitti. Ama microservices dünyasına geçtiğinde, **her servisin kendi veritabanı var** ve servisler arası tek bir transaction YAPAMAZSIN. Neden? Çünkü distributed transaction (2-Phase Commit / 2PC) çok yavaş, çok kırılgan ve ölçeklenmiyor. Bir servis yanıt vermezse tüm sistem kilitlenir. İşte bu yüzden **Saga Pattern** icat edildi.

🎭 **Saga Nedir?** Basitçe: Büyük bir distributed transaction'ı, **birbiri ardına çalışan küçük local transaction'lara** bölersin. Her adımın bir de **compensating action**'ı (telafi aksiyonu) vardır — yani "geri alma" planı.

✈️ **Uçuş Rezervasyonu Analojisi:**
Bir tatil planlıyorsun ve 3 şey rezerve etmen gerekiyor:
1. ✅ Uçak bileti al → Başarılı!
2. ✅ Otel rezervasyonu yap → Başarılı!
3. ❌ Araç kirala → BAŞARISIZ! (Araç kalmamış)

Şimdi ne olacak? Otel rezervasyonunu İPTAL ET, uçak biletini İADE ET. İşte bu "geri alma" işlemleri **compensating transaction**'lardır.

---

🚗 **Gerçek Dünya Örneği — Uber:**
1. Yolcu ride talep etti → ✅ Sürücü atandı
2. Ödeme çekildi → ❌ Kredi kartı reddedildi!
3. Compensate: Sürücüyü serbest bırak, ride'ı iptal et

Bu akış Saga'dır. Her adım bağımsız bir local transaction'dır ve hata olursa geriye doğru compensate edilir.

---

**İki tür Saga vardır:**

| | Choreography Saga | Orchestration Saga |
|---|---|---|
| **Koordinasyon** | Her servis bir event yayınlar, diğer servisler dinler | Merkezi bir orchestrator tüm adımları yönetir |
| **Analoji** | Dans — herkes müziği duyar ve kendi adımını atar | Orkestra şefi — şef kimin ne zaman çalacağını söyler |
| **Coupling** | Düşük (event-driven) | Orta (orchestrator bağımlılığı) |
| **Karmaşıklık** | Az serviste basit, çok serviste kaotik | Her zaman anlaşılır, ama orchestrator karmaşık |
| **Debugging** | ZOR — event chain'i takip etmek kabusa döner | KOLAY — orchestrator'da tüm akış görünür |
| **Ne zaman?** | 2-4 servislik basit akışlar | 5+ servislik karmaşık iş akışları |

**Choreography örneği:** Order Service → `order.created` event'i yayınlar → Inventory Service dinler ve stok rezerve eder → `inventory.reserved` event'i yayınlar → Payment Service dinler ve ödemeyi çeker.

**Orchestration örneği:** OrderSaga orchestrator sırayla her servisi çağırır: "Inventory, stok ayır" → "Payment, ödemeyi çek" → "Shipping, kargola". Hata olursa orchestrator ters sırayla compensate eder.

---

⚠️ **Idempotency ZORUNLUDUR!** Compensating action'lar ağ hatası nedeniyle BİRDEN FAZLA KEZ çalışabilir. Eğer `refund()` fonksiyonun idempotent değilse, müşteriye 2 kez para iade edebilirsin! Her compensating action'a bir `saga_id + step_id` ile idempotency key ekle.

⚠️ **Saga ne zaman OVERKILL?** Eğer monolith'in varsa ve tek bir veritabanı kullanıyorsan — Saga'ya GEREK YOK. Düz `BEGIN TRANSACTION ... COMMIT` yeter. Saga, dağıtık sistemlerin getirdiği karmaşıklığa bir çözümdür, karmaşıklık yaratmak için değil. "Tek DB'de Saga kullanıyorum" diyorsan, muhtemelen over-engineering yapıyorsun. 😅

```javascript
// Saga orchestrator
class OrderSaga {
  async execute(orderData) {
    const sagaId = generateId();
    
    try {
      // Step 1: Create order
      const order = await orderService.createOrder(orderData);
      await sagaLog.save({ sagaId, step: 'ORDER_CREATED', data: order });
      
      // Step 2: Reserve inventory
      const reservation = await inventoryService.reserve(order.items);
      await sagaLog.save({ sagaId, step: 'INVENTORY_RESERVED', data: reservation });
      
      // Step 3: Process payment
      const payment = await paymentService.charge(order.total);
      await sagaLog.save({ sagaId, step: 'PAYMENT_PROCESSED', data: payment });
      
      return { success: true, order };
    } catch (error) {
      // Compensating transactions (rollback)
      await this.compensate(sagaId);
      throw error;
    }
  }
  
  async compensate(sagaId) {
    const steps = await sagaLog.find({ sagaId });
    
    // Reverse order
    for (const step of steps.reverse()) {
      switch (step.step) {
        case 'PAYMENT_PROCESSED':
          await paymentService.refund(step.data.paymentId);
          break;
        case 'INVENTORY_RESERVED':
          await inventoryService.release(step.data.reservationId);
          break;
        case 'ORDER_CREATED':
          await orderService.cancelOrder(step.data.orderId);
          break;
      }
    }
  }
}
```

### Database Sharding & Replication

Veritabanın büyüdükçe iki temel sorunla karşılaşırsın: okuma trafiği kaldırılamıyor ("sayfa 5 saniyede yükleniyor!") ve veri tek bir makineye sığmıyor ("disk dolu!"). İşte **Replication** ve **Sharding** bu iki soruna iki farklı çözümdür.

---

📋 **Replication Nedir? — "Ödevi Kopyalamak" Analojisi**

Okuldaki o arkadaşı hatırla — ödevi bir kişi yapar, diğer 3 kişi kopyalar. Ama sadece BİR kişi değişiklik yapabilir (orijinal yazar). Diğerleri sadece okuma amaçlı kopya tutar. İşte veritabanı replication'ı tam olarak budur:

- **Primary (Master):** Tek yazma noktası. Tüm INSERT, UPDATE, DELETE buraya gelir.
- **Replica (Slave):** Primary'nin kopyaları. Sadece SELECT sorguları buradan okunur.

**Neden Replication?** Gerçek dünya trafiğinde genellikle **%80 READ, %20 WRITE** oranı vardır. Bir e-ticaret sitesinde 100 kişi ürün sayfasını görüntülerken, belki 1 kişi satın alıyor. O 80 READ'i tek bir DB'ye yığmak yerine, 4 replica'ya dağıtırsan → her replica sadece 20 READ alır. 4x performans artışı! 🚀

**Synchronous vs Asynchronous Replication:**

| | Synchronous | Asynchronous |
|---|---|---|
| **Nasıl çalışır?** | Primary, replica'ya yazdığını ONAYLATMADAN client'a "tamam" demez | Primary yazıp hemen "tamam" der, replica arka planda güncellenir |
| **Tutarlılık** | Strong consistency — replica HER ZAMAN güncel | Eventual consistency — replica birkaç ms geride olabilir |
| **Performans** | Yavaş (her yazma replica'yı bekler) | Hızlı (yazma anında beklemez) |
| **Veri kaybı riski** | Yok (replica onayladı) | Var (primary çökerse, replica'ya henüz gitmemiş veri kaybolabilir) |
| **Kullanım** | Finansal sistemler, kritik veri | Sosyal medya, analytics, loglar |

**Replication Lag — "Yorum Attım Ama Görünmüyor" Problemi:**

Twitter'a bir tweet attın. `POST /tweets` → Primary'ye yazıldı ✅. Hemen sayfayı yeniliyorsun. `GET /tweets` → Replica'dan okunuyor... ama replica henüz güncellenmemiş! Tweet'in görünmüyor. 2 saniye sonra yeniliyorsun — işte orada! Bu **replication lag**'dir.

**Çözümler:**
- **Read-your-own-writes:** Kullanıcı kendi yazdığı veriyi okuyorsa → Primary'den oku. Başka kullanıcının verisiyse → Replica'dan oku.
- **Causal consistency:** "Bu yazma işleminden SONRA yapılan okumaları Primary'den al" gibi akıllı routing.

---

📚 **Sharding Nedir? — "Kütüphane Binaları" Analojisi**

Bir kütüphane düşün: 10 milyon kitap var. Hepsini tek bir binaya koyarsan, raf bulmak bile 10 dakika sürer. Çözüm? 4 bina yap:
- 🏛️ Bina 1: A-F harfleriyle başlayan kitaplar
- 🏛️ Bina 2: G-L harfleriyle başlayan kitaplar
- 🏛️ Bina 3: M-R harfleriyle başlayan kitaplar
- 🏛️ Bina 4: S-Z harfleriyle başlayan kitaplar

"MySQL" kitabını arıyorsan? Bina 3'e git. "Redis" kitabını arıyorsan? Bina 4'e git. Her bina daha küçük, daha hızlı! İşte bu **horizontal sharding**'dir — veriyi BÖLÜP farklı makinelere dağıtmak.

---

🔑 **Shard Key Seçimi — EN ÖNEMLİ Karar!**

Shard key, verinin HANGİ shard'a gideceğini belirler. Ve kötü bir shard key seçimi, sharding'in tüm faydasını yok eder:

**Kötü shard key örneği — `country` alanı:**
E-ticaret sitende `country` shard key'i olarak seçtin. Kullanıcıların %60'ı Türkiye'den. Sonuç? Türkiye shard'ı TÜM trafiğin %60'ını alıyor, diğer 3 shard boş boş oturuyor. Bu **hotspot** problemidir — tüm yük tek bir shard'a biner.

**İyi shard key örneği — `user_id` hash'i:**
User ID'nin hash'ini alıp mod 4 yaparsın → veriler 4 shard'a EŞİT dağılır. Hotspot yok, her shard aynı yükü taşır.

**Shard key seçiminde altın kurallar:**
1. **Yüksek kardinalite:** Shard key'in çok fazla unique değeri olmalı (user_id ✅, gender ❌)
2. **Eşit dağılım:** Veriler shard'lara dengeli dağılmalı
3. **Query pattern'i:** En sık sorgulanan alan shard key olmalı — aksi halde her sorgu TÜM shard'lara gider (scatter-gather = yavaş)

---

🔄 **Resharding — Kabusu Yaşamak İstemezsin!**

4 shard'la başladın, işler büyüdü, 8 shard'a çıkman gerekiyor. Sorun? `hash(user_id) % 4` ile dağıttığın tüm veriyi şimdi `hash(user_id) % 8` ile YENİDEN dağıtman gerekiyor. Bu milyarlarca satırın taşınması demek — SIFIR downtime ile! Bu bir mühendislik kabusu. **Consistent hashing** bu sorunu hafifletir ama tamamen çözmez. Mümkünse baştan yeterli shard ile başla.

---

🌍 **Gerçek Dünya Örnekleri:**
- **Discord:** Mesajları `channel_id`'ye göre shard'lıyor. Neden? Bir kullanıcı mesaj okurken genelde TEK bir kanalda — yani tek bir shard'a gider. Cross-shard query gerekmiyor!
- **Instagram:** Kullanıcı verilerini `user_id`'ye göre shard'lıyor. Bir kullanıcının profili, postları, followerleri hep AYNI shard'da — tek sorguda hepsi gelir.
- **Vitess (YouTube):** MySQL'i shard'lama katmanı. YouTube'un milyarlarca videosunu yöneten altyapı.

**Replication:**
```
Primary-Replica (Master-Slave):
Primary (Write)
├── Replica 1 (Read)
├── Replica 2 (Read)
└── Replica 3 (Read)

Use cases:
- Read scalability
- High availability
- Disaster recovery
```

**Sharding:**
```javascript
// Horizontal partitioning
function getShardId(userId) {
  // Hash-based sharding
  const hash = crypto.createHash('md5').update(userId).digest('hex');
  const numShards = 4;
  return parseInt(hash, 16) % numShards;
}

// Route to correct shard
async function getUserData(userId) {
  const shardId = getShardId(userId);
  const db = databases[shardId];
  return await db.query('SELECT * FROM users WHERE id = ?', [userId]);
}
```

---

## 🔍 Search & Real-time Technologies

### Elasticsearch

**Nedir:**
- Distributed search and analytics engine
- Document-oriented (JSON)
- Real-time indexing & searching
- Built on Apache Lucene

**Use Cases:**
```
1. Full-text search (products, articles, documents)
2. Log analytics (ELK Stack)
3. Metrics & monitoring
4. Application performance monitoring
5. Security analytics
```

#### Architecture
```
┌─────────────────────────────────────┐
│         Elasticsearch Cluster        │
├─────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐           │
│  │ Node 1  │  │ Node 2  │  ...      │
│  │ Master  │  │ Data    │           │
│  └─────────┘  └─────────┘           │
├─────────────────────────────────────┤
│  Indices -> Shards -> Documents      │
└─────────────────────────────────────┘
```

#### Basic Operations

**Elasticsearch'e veri yazma ve okuma temel işlemlerini görelim.** Önemli kavramlar:

- **Index:** Veritabanındaki 'tablo' gibi düşün. Her index bir mapping'e (schema) sahip.
- **Document:** Tablodaki 'satır' gibi. JSON formatında.
- **Mapping:** Hangi alanın `text` (full-text search için analyze edilir) vs `keyword` (exact match, filtreleme için) olduğunu belirler.
- **Bulk API:** Tek tek yazmak yerine toplu yazma — performans 10-100x artar! Production'da her zaman bulk kullan.

**Kritik fark:** `text` vs `keyword`
- `text`: "iPhone 15 Pro Max" → tokenize edilir → ["iphone", "15", "pro", "max"] → arama yapabilirsin
- `keyword`: "iPhone 15 Pro Max" → OLDUĞU GİBİ saklanır → sadece tam eşleşme/filtreleme
```javascript
const { Client } = require('@elastic/elasticsearch');
const client = new Client({ node: 'http://localhost:9200' });

// Create index
await client.indices.create({
  index: 'products',
  body: {
    mappings: {
      properties: {
        name: { type: 'text' },
        description: { type: 'text' },
        price: { type: 'float' },
        category: { type: 'keyword' },
        tags: { type: 'keyword' },
        created_at: { type: 'date' }
      }
    }
  }
});

// Index document
await client.index({
  index: 'products',
  id: '1',
  document: {
    name: 'iPhone 15',
    description: 'Latest Apple smartphone with A17 chip',
    price: 999,
    category: 'electronics',
    tags: ['smartphone', 'apple', 'ios'],
    created_at: new Date()
  }
});

// Bulk indexing (efficient)
const operations = products.flatMap(doc => [
  { index: { _index: 'products' } },
  doc
]);

await client.bulk({
  refresh: true,
  operations
});

// Search
const result = await client.search({
  index: 'products',
  query: {
    match: {
      description: 'smartphone'
    }
  }
});

// Advanced search with filters
const result = await client.search({
  index: 'products',
  body: {
    query: {
      bool: {
        must: [
          { match: { description: 'smartphone' } }
        ],
        filter: [
          { range: { price: { gte: 500, lte: 1500 } } },
          { term: { category: 'electronics' } }
        ]
      }
    },
    sort: [
      { price: { order: 'asc' } }
    ],
    aggs: {
      price_ranges: {
        range: {
          field: 'price',
          ranges: [
            { to: 500 },
            { from: 500, to: 1000 },
            { from: 1000 }
          ]
        }
      },
      categories: {
        terms: { field: 'category' }
      }
    }
  }
});
```

#### Full-Text Search Features

Full-text search nedir? Şunu hayal edin: Bir kütüphanede 10 milyon kitap var. "Yapay zeka" konusunu arıyorsunuz. Sıradan bir arama (SQL LIKE) her kitabın her sayfasını baştan sona okur — yıllar sürer. Ama bir de düşünün ki, bu kütüphanenin bir kütüphanecisi var ve bu kütüphaneci **her kitabın her kelimesini okumuş, hangi kelimenin hangi kitabın hangi sayfasında geçtiğini not etmiş.** "Yapay zeka" dediğinizde, not defterine bakıp milisaniyeler içinde tüm ilgili kitapları size verir. İşte Elasticsearch'ün yaptığı tam olarak budur.

**Inverted Index — Sihrin Kaynağı:**

Full-text search'ün temelinde **inverted index** (ters indeks) yatar. Normal bir index "belge → kelimeler" eşlemesi yapar. Inverted index ise tam tersini yapar: **"kelime → belge ID'leri"** eşlemesi.

Örnek:
```
Belge 1: "Redis çok hızlıdır"
Belge 2: "Elasticsearch çok güçlüdür"
Belge 3: "Redis ve Elasticsearch birlikte kullanılır"

Inverted Index:
"redis"         → [Belge 1, Belge 3]
"çok"           → [Belge 1, Belge 2]
"hızlıdır"      → [Belge 1]
"elasticsearch" → [Belge 2, Belge 3]
"güçlüdür"      → [Belge 2]
"birlikte"      → [Belge 3]
"kullanılır"    → [Belge 3]
```
"redis" araması yapıldığında, Elasticsearch inverted index'e bakar ve anında Belge 1 ve 3'ü döner. 10 milyon belge olsa bile bu işlem milisaniyeler sürer çünkü tüm belgeler taranmaz, doğrudan kelimenin kayıtlı olduğu belgelere gidilir.

**Analyzers — Metni Arama İçin Hazırlamak:**

Bir metin indexlenmeden önce **analyzer** denilen bir pipeline'dan geçer. Bu pipeline üç aşamadan oluşur:

1. **Character Filter:** Özel karakterleri temizler (HTML tag'leri kaldırma, aksan işaretlerini normalize etme).
2. **Tokenizer:** Metni kelimelere (token) ayırır. "Running quickly!" → ["Running", "quickly"]
3. **Token Filters:** Her token'a dönüşümler uygular:
   - **Lowercase:** "Running" → "running"
   - **Stemmer:** "running" → "run" (kelimenin köküne indirgeme)
   - **Stop words:** "the", "is", "and" gibi anlamsız kelimeleri çıkarma
   - **Synonym:** "quick" ve "fast" aynı şey olarak kabul etme

Sonuç: "Running quickly!" → ["run", "quick"]. Artık kullanıcı "run" veya "runs" veya "running" yazsa hepsinde bu belge bulunur.

**Fuzzy Search — Yazım Hatası Toleransı:**

Kullanıcılar yazım hatası yapar. "iPhone" yerine "iphne" yazar. Fuzzy search, **Levenshtein distance** (edit distance) kullanarak benzer kelimeleri bulur. Edit distance = bir kelimeyi diğerine dönüştürmek için gereken minimum karakter ekleme/silme/değiştirme sayısı.

- "iphne" → "iphone" = 1 edit (h ve o yer değiştir + n→n) aslında 2 edit
- Elasticsearch'te `fuzziness: 'AUTO'` ayarı, kelime uzunluğuna göre otomatik tolerans belirler: 1-2 karakter = 0 edit, 3-5 karakter = 1 edit, 5+ karakter = 2 edit. Çoğu yazım hatası edit distance 1-2 ile yakalanır.

**Boosting — Hangi Alan Daha Önemli:**

Bir kullanıcı "Samsung Galaxy" aradığında, ürün adında geçen sonuçlar, açıklamada geçenlerden daha önemli olmalıdır. `name^3` ifadesi, name alanındaki eşleşmenin 3 kat daha yüksek skor alacağı anlamına gelir. Bu sayede kullanıcı aradığı ürünü ilk sırada görür, "Samsung Galaxy kılıfı" gibi yan ürünler sonralara düşer.

**Autocomplete — Yazarken Tamamlama:**

İki popüler yaklaşım var:
- **match_phrase_prefix:** Hızlı ama sınırlı. "iph" yazdığında "iPhone 15 Pro" gelir. Dezavantaj: sadece prefix match yapar, ortadaki kelimeleri yakalayamaz.
- **Edge N-grams:** Index zamanında kelimenin prefix'lerini oluşturur: "iPhone" → ["i", "ip", "iph", "ipho", "iphon", "iphone"]. Daha esnek ama index boyutu artar. Büyük ölçekli e-ticaret sitelerinin tercihi genellikle budur.

**"Bunu mu demek istediniz?" (Did you mean?) Suggestions:**

Google'ın meşhur özelliği. Elasticsearch'te `suggest` API'si ile yapılır. Trigram (3-karakter) tabanlı benzerlik hesabı kullanır. "iphne" yazdığınızda, trigram analizi ile en yakın doğru formu bulur ve "iphone" önerir. Arka planda phonetic analysis, n-gram benzerliği ve term frequency istatistikleri bir arada çalışır.

**Relevance Scoring — Neden Sonuçlar Sıralı Gelir:**

Elasticsearch sonuçları rastgele sıralamaz. Her belge bir **relevance score** alır. Eskiden **TF-IDF** (Term Frequency - Inverse Document Frequency) kullanılırdı, şimdi daha gelişmiş **BM25** (Best Match 25) algoritması varsayılandır.

- **TF (Term Frequency):** Kelime belgede ne kadar çok geçiyorsa, o kadar relevant.
- **IDF (Inverse Document Frequency):** Kelime tüm belgelerde çok geçiyorsa (örn: "the"), aslında ayırt edici değildir, skoru düşürülür.
- **BM25:** TF-IDF'in gelişmiş versiyonu — belge uzunluğunu normalize eder, saturation (doygunluk) ekler. Çok uzun belgelerin haksız avantaj almasını engeller.

Kısacası: Elasticsearch "bu belge aramanızla ne kadar alakalı?" sorusunu matematik ve istatistikle cevaplar.

```javascript
// Fuzzy search (typo tolerance)
{
  query: {
    match: {
      name: {
        query: 'iphne',
        fuzziness: 'AUTO'
      }
    }
  }
}

// Multi-field search
{
  query: {
    multi_match: {
      query: 'smartphone',
      fields: ['name^3', 'description', 'tags^2'],  // ^3 = boost
      type: 'best_fields'
    }
  }
}

// Autocomplete
{
  query: {
    match_phrase_prefix: {
      name: {
        query: 'iph',
        max_expansions: 10
      }
    }
  }
}

// Suggestions (Did you mean?)
{
  suggest: {
    text: 'iphne',
    simple_phrase: {
      phrase: {
        field: 'name.trigram',
        size: 1,
        gram_size: 3,
        direct_generator: [{
          field: 'name.trigram',
          suggest_mode: 'always'
        }]
      }
    }
  }
}
```

#### Analyzers

Analyzer'lar Elasticsearch'ün **tercümanlarıdır** — ham metni alır, aranabilir token'lara çevirirler. Bunu şöyle düşünün: siz "Türkiye'nin en güzel şehirleri" diye aratıyorsunuz, ama Elasticsearch bu cümleyi olduğu gibi saklamaz. Önce bu cümleyi parçalar, temizler ve normalize eder ki daha sonra "güzel şehir" diye arattığınızda da bulabilsin. Bu işlem üç aşamada gerçekleşir ve bu aşamaları bilmek, arama kalitesi ile "aman hiçbir şey çıkmıyor" arasındaki farktır.

**Analyzer'ın 3 Aşaması — Bir Fabrika Hattı Gibi:**

1. **Character Filters (Karakter Filtreleri):** Ham metindeki karakterleri dönüştürür. HTML tag'lerini temizler (`<b>güzel</b>` → `güzel`), özel karakterleri normalize eder. Bu ilk aşamadır — hammaddeyi temizleme.
2. **Tokenizer:** Temizlenmiş metni token'lara (kelimelere) böler. Standard tokenizer boşluklardan ve noktalama işaretlerinden böler: `"Türkiye'nin en güzel şehirleri"` → `["Türkiye'nin", "en", "güzel", "şehirleri"]`. Farklı tokenizer'lar farklı kurallara göre böler.
3. **Token Filters:** Token'ları son kez işler — lowercase yapar, gereksiz kelimeleri (stop words: "the", "a", "ve", "bir") atar, stemming uygular.

**Standard Analyzer:** Elasticsearch'ün default analyzer'ıdır. Küçük harfe çevirir, boşluktan ve noktalamadan böler. İngilizce metin için çoğu durumda yeterlidir. Ama Türkçe için? **YETERSIZ.**

**Neden Custom Analyzer Lazım? — Türkçe Meselesi:**

Türkçe, analyzer açısından İngilizce'den çok daha zor bir dildir. Düşünün:
- **ş, ı, ö, ü, ç, ğ** karakterleri: Kullanıcı "istanbul" yazarsa "İstanbul" bulunmalı, "Ístanbul" bile bulunmalı → `asciifolding` filtresi (ş→s, ı→i, ö→o, ü→u, ç→c, ğ→g)
- **Stop words:** "ve", "bir", "bu", "da", "de" gibi kelimeler arama sonuçlarına gürültü katar → stop word filtresi ile temizlenir
- **Stemming:** "koşuyor", "koştu", "koşacak" hepsi "koş" kökünden gelir. Stemming olmadan kullanıcı "koşmak" aratırsa "koşuyor" içeren sonuçları BULAMAZ. Stemming ile hepsi aynı köke indirgenir → arama kalitesi DRAMATIK artar. İngilizce'de de aynı: "running", "runs", "ran" hepsi "run" olur. Bu özellik GÜÇLÜDÜR.

**Analyzer Testing — `_analyze` API:**

Custom analyzer yazdınız ama doğru çalışıp çalışmadığını nasıl test edersiniz? `_analyze` API tam bunun için var — bir debugging aracıdır:

```
GET /_analyze
{
  "analyzer": "custom_analyzer",
  "text": "Türkiye'nin en güzel şehirleri"
}
```

Bu size token listesini döner: `["turkiye", "guzel", "sehir"]` — stop word'ler atılmış, Türkçe karakterler normalize edilmiş, stemming uygulanmış. Beklediğiniz gibi değilse analyzer'ınızı düzeltirsiniz.

**⚠️ Yaygın Hata: `keyword` vs `text` Karışıklığı:**

Bu hata çok yapılır! `keyword` tipi metni **hiç analiz etmez** — exact match için kullanılır (email, status, order_id gibi). `text` tipi ise analyzer'dan geçirir — full-text search için kullanılır (açıklama, yorum, ürün adı gibi). Bir ürün adını `keyword` olarak tanımlarsanız, "iPhone" aramak için tam olarak "iPhone 15 Pro Max 256GB Mavi" yazmanız gerekir. `text` olarak tanımlarsanız sadece "iphone" yazmanız yeterli. Doğru tip seçimi, arama deneyiminin temelidir.

```javascript
// Custom analyzer for better search
{
  settings: {
    analysis: {
      analyzer: {
        custom_analyzer: {
          type: 'custom',
          tokenizer: 'standard',
          filter: [
            'lowercase',
            'asciifolding',  // ş -> s, ı -> i
            'stop',          // remove "the", "a", etc.
            'snowball'       // stemming (running -> run)
          ]
        }
      }
    }
  },
  mappings: {
    properties: {
      name: {
        type: 'text',
        analyzer: 'custom_analyzer'
      }
    }
  }
}
```

#### Performance Optimization

Elasticsearch performans optimizasyonu demek, aslında **cüzdanınızı ve kullanıcı deneyiminizi aynı anda kurtarmak** demek. Yanlış query yazarsanız hem Elasticsearch cluster'ınız ağlar, hem kullanıcılarınız "bu arama niye bu kadar yavaş?" diye şikayet eder. Gelin en etkili tekniklere bakalım.

**Filter vs Query Context — ES'in 1 Numaralı Performans Hilesi:**

Bu farkı anlamak, Elasticsearch performansında **DÖNÜM NOKTASIDIR:**

- **Query Context (Sorgu Bağlamı):** "Bu döküman aramayla ne kadar İYİ eşleşiyor?" sorusunu cevaplar. Her döküman için bir **relevance score** hesaplar (0.0 - 10.0+). Bu hesaplama CPU-yoğundur, pahalıdır ve sonuçları **cache'lenemez** çünkü skor dinamiktir.
- **Filter Context (Filtre Bağlamı):** "Bu döküman eşleşiyor mu? EVET veya HAYIR." Binary cevap. Skor hesaplanmaz. Ve en güzeli: sonuçlar **cache'lenir!** Aynı filtre tekrar geldiğinde Elasticsearch hiç hesaplamadan cache'ten döner. ⚡

**Altın Kural:** Metin araması (kullanıcının yazdığı search query) → `must` içinde (query context). Filtreleme (fiyat aralığı, kategori, stok durumu, tarih aralığı) → `filter` içinde (filter context).

**Gerçek Dünya:** Bir e-ticaret sitesinde 3 filtreyi (kategori, fiyat aralığı, stok durumu) query context'ten filter context'e taşıdık. Sonuç? p95 latency **800ms'den 200ms'e** düştü. Aynı donanım, aynı veri, sadece query yapısı değişti. Bu kadar fark yaratıyor.

**Aggregation'lar — SQL GROUP BY'ın Çok Güçlü Hali:**

Aggregation'lar Elasticsearch'ün en güçlü özelliklerinden biridir. SQL'deki `GROUP BY` gibidir ama çok daha fazlasını yapabilir. **Faceted search** (soldaki filtre paneli: "Elektronik (234)", "Giyim (89)" gibi sayıları gösteren kategoriler) aggregation ile yapılır. Aynı anda ortalama fiyat, minimum-maximum, histogram dağılımı hesaplayabilirsiniz. Dashboard'larda trend analizi, e-ticarette filtre panelleri — hep aggregation.

**Scroll API — Büyük Sonuç Setleri İçin:**

`from: 10000, size: 100` yapmak Elasticsearch için **KÂBUSTur**. ES önce 10.100 sonucu sıralar, sonra ilk 10.000'ini atar. Büyük veri setlerini işlemek için **Scroll API** kullanın — cursor gibi çalışır, her seferinde bir batch alırsınız. Veya yeni ES sürümlerinde `search_after` parametresini tercih edin.

**Index Lifecycle Management (ILM) — Depolama Maliyetini Düşürün:**

Log verileri zamanla değerini kaybeder. Dünkü loglar çok önemli, geçen ayki loglar bazen lazım, geçen yılki loglar nadiren bakılır. ILM ile:
- **Hot tier:** Yeni veriler, SSD'lerde, tam replikasyon → hızlı arama
- **Warm tier:** 7+ günlük veriler, HDD'lere taşınır, replica azalır
- **Cold tier:** 30+ günlük veriler, minimum kaynak
- **Delete:** 90+ günlük veriler silinir

Bu strateji depolama maliyetini %60-80 oranında azaltabilir.

**Bulk API — İndeksleme Performansının Sırrı:**

Tek tek döküman indekslemek, marketten her seferinde TEK ürün almak gibidir — 100 kere gidip gelirsiniz. Bulk API ile hepsini tek seferde gönderirsiniz. Performans farkı? **10-100x daha hızlı.** Production'da veri yüklerken, migration yaparken, batch işlerde HER ZAMAN bulk kullanın. Optimal batch boyutu genelde 5-15MB veya 1000-5000 döküman arasıdır — test ederek bulun.

```javascript
// Use filter context (cacheable) instead of query context
{
  query: {
    bool: {
      must: [
        { match: { description: 'smartphone' } }  // Scored
      ],
      filter: [
        { term: { category: 'electronics' } },    // Cached, not scored
        { range: { price: { lte: 1000 } } }       // Cached, not scored
      ]
    }
  }
}

// Aggregations with filtering
{
  query: { match_all: {} },
  aggs: {
    filtered_products: {
      filter: { term: { category: 'electronics' } },
      aggs: {
        avg_price: { avg: { field: 'price' } }
      }
    }
  }
}

// Scroll API for large result sets
let result = await client.search({
  index: 'products',
  scroll: '1m',
  size: 1000,
  query: { match_all: {} }
});

while (result.hits.hits.length) {
  // Process batch
  processBatch(result.hits.hits);
  
  // Get next batch
  result = await client.scroll({
    scroll_id: result._scroll_id,
    scroll: '1m'
  });
}
```

#### ELK Stack (Elasticsearch + Logstash + Kibana)

ELK Stack nedir? Şu analojiyi düşünün: Büyük bir gazete arşivi sistemi kuruyorsunuz.

- **Logstash** = Muhabir ağı. Dünyanın dört bir yanından haberleri toplar, düzenler, standart formata sokar ve arşive gönderir.
- **Elasticsearch** = Dev bir arşiv odası + süper hızlı kütüphaneci. Gelen tüm haberleri depolar, indeksler ve "2024'te İstanbul'daki deprem haberleri" gibi sorulara milisaniyede cevap verir.
- **Kibana** = Gazete okuma salonu. Arşivdeki verileri güzel grafikler, tablolar ve dashboard'larla görselleştirir. Editörler burada trend analizi yapar.

Bu üçlü birlikte **"log topla → depola ve indeksle → görselleştir ve analiz et"** pipeline'ını oluşturur.

**Her Komponentin Rolü Detaylıca:**

**Elasticsearch — Depolama + Arama Motoru:**
Core bileşen. Apache Lucene üzerine inşa edilmiş, dağıtık bir arama ve analitik motorudur. JSON belgelerini depolar, inverted index ile milisaniyede arama yapar. Cluster yapısında çalışır — node'lar arası veri replikasyonu ile yüksek erişilebilirlik sağlar. Hem tam metin arama (full-text search) hem de metrik aggregation yapabilir.

**Logstash — Veri Toplama + Dönüşüm Pipeline'ı:**
ETL (Extract-Transform-Load) aracıdır. Input plugin'leri ile veriyi onlarca kaynaktan alır (dosya, TCP, HTTP, Kafka, veritabanı...), filter plugin'leri ile parse eder, zenginleştirir, dönüştürür ve output plugin'leri ile hedeflere yazar. Grok pattern'leri ile unstructured log satırlarını structured JSON'a çevirir. Ağır ve JVM tabanlıdır — ciddi RAM tüketir.

**Kibana — Görselleştirme + Dashboard'lar:**
Elasticsearch'ün web arayüzüdür. Verilerden line chart, pie chart, heatmap, data table oluşturabilirsiniz. Dashboard'lar birden fazla görselleştirmeyi bir araya getirir — "son 24 saat error oranı", "en çok hata veren endpoint'ler", "response time trendi" gibi paneller tek ekranda. Alerting modülü ile belirli koşullarda (error rate > %5) email/Slack bildirimi gönderir.

**Filebeat / Metricbeat — Hafif Veri Toplayıcılar:**
Logstash ağırdır ve her sunucuya kurmak kaynak israfıdır. Bu yüzden **Beat ailesi** geliştirildi:
- **Filebeat:** Log dosyalarını okur ve Logstash'e veya doğrudan Elasticsearch'e gönderir. Çok hafif (~10MB RAM), Go ile yazılmış.
- **Metricbeat:** Sistem metrikleri (CPU, memory, disk) ve servis metrikleri (MySQL, Redis, Nginx) toplar.
- **Packetbeat:** Network trafiğini analiz eder.

Modern mimaride genellikle: **Filebeat (sunucularda) → Logstash (merkezi dönüşüm) → Elasticsearch (depolama) → Kibana (görselleştirme)** şeklinde kurulur.

**Neden ELK ve Neden Sadece `grep` Yetmez?**

Tek sunucuda 100MB log dosyası var — `grep "ERROR" app.log` gayet çalışır. Ama...
- 50 sunucu × günde 2GB log = **günde 100GB log**. `grep` ile hangi sunucuya SSH olacaksınız?
- "Son 1 saatte en çok hata veren endpoint hangisi?" — `grep` ile bunu yapamazsınız.
- "Geçen haftanın aynı saatine göre error rate artmış mı?" — `grep` ile kesinlikle yapamazsınız.
- Logları 90 gün saklamak + anında aramak — `grep` ile imkansız.

ELK Stack, log verilerini **aranabilir, filtrelenebilir, görselleştirilebilir ve alert'lenebilir** hale getirir. Küçük ölçekte lüks, büyük ölçekte zorunluluk.

**Alternatifler:**

- **Grafana Loki:** "Log'lar için Prometheus" sloganıyla çıktı. Log içeriğini indekslemez, sadece label'ları indeksler — bu sayede çok daha ucuz ve hafif. Grafana ile doğal entegrasyon. Kubernetes ortamlarında popüler.
- **Datadog:** SaaS çözüm. Logs + Metrics + Traces hepsi bir arada. Kurulum yok, operasyon yok. Ama fiyat... 💸 Büyük ölçekte ayda onbinlerce dolar.
- **Splunk:** Enterprise dünyanın kralı. Güçlü arama dili (SPL), güvenlik analizi için mükemmel. Fiyatı da kraliyet düzeyinde.
- **CloudWatch Logs:** AWS-native. Lambda + ECS + API Gateway logları otomatik akar. Basit sorgular için yeterli, karmaşık analiz için sınırlı.

**Index Lifecycle Management (ILM) — Verilerin Yaşam Döngüsü:**

Log verileri sonsuza kadar hot storage'da kalamaz. ILM politikaları ile veriler yaşam döngüsünden geçer:

- **Hot (Sıcak):** Son 7 gün. Hızlı SSD diskler, tüm replica'lar aktif. Aktif yazma ve okuma.
- **Warm (Ilık):** 7-30 gün. Daha yavaş diskler, replica sayısı azaltılabilir. Sadece okuma.
- **Cold (Soğuk):** 30-90 gün. En ucuz depolama, frozen tier. Nadiren erişilir.
- **Delete (Silme):** 90+ gün. Otomatik silinir.

**💰 Gerçek Dünyadan Maliyet Uyarısı:**

Elasticsearch cluster maliyetleri kontrol edilmezse korkunç şekilde patlayabilir. Bir e-ticaret şirketi günde 500GB log üreterek aylık $30.000 ES faturası ödüyordu. Çözümler:
- **ILM politikaları:** Hot → Warm → Cold geçişleri maliyet tasarrufu sağlar (warm tier %40, cold tier %70 daha ucuz olabilir).
- **Log seviyesi filtreleme:** DEBUG loglarını production'da ES'e göndermek para yakmaktır. Sadece WARN ve üstünü gönderin.
- **Sampling:** Her 10 istekten birinin logunu detaylı tut, diğerlerini özetle.
- **Index pattern optimizasyonu:** Gereksiz alan indekslemeyi kapatın (`"index": false`).

Doğru ILM politikaları ile o $30.000'lık fatura $8.000'a düşürülebilir. Para yakılmasını engellemek de mühendisliğin parçasıdır.

```yaml
# Logstash configuration
input {
  file {
    path => "/var/log/app/*.log"
    type => "app-logs"
  }
  
  beats {
    port => 5044
  }
}

filter {
  if [type] == "app-logs" {
    grok {
      match => { 
        "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:message}" 
      }
    }
    
    date {
      match => [ "timestamp", "ISO8601" ]
    }
  }
  
  # Parse JSON logs
  json {
    source => "message"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "app-logs-%{+YYYY.MM.dd}"
  }
}
```

#### Monitoring & Alerting (Kibana)

Kibana, sisteminizin **kontrol odasıdır** — tıpkı bir nükleer santralin kontrol odasındaki TV ekranları gibi, sisteminizin her parçasını gerçek zamanlı izlemenizi sağlar. Bir şey kırmızıya dönerse hemen görürsünüz. Alarm çalarsa müdahale edersiniz. Kibana olmadan Elasticsearch'teki verileriniz karanlık bir depodaki kutuların içindedir — var ama göremezsiniz.

**Dashboard'lar — Büyük Resmi Görün:**

Dashboard, birden fazla görselleştirmeyi (visualization) tek bir ekranda birleştirir. "Son 24 saatteki error oranı" + "En çok hata veren endpoint'ler" + "Response time trendi" + "Aktif kullanıcı sayısı" — tüm bunlar tek bir ekranda. Dashboard'lar interaktiftir: bir grafiğe tıklayarak filtreleyebilir, zaman aralığını değiştirebilirsiniz.

**Index Patterns — Kibana'ya Ne Göstereceğini Söyleyin:**

Kibana tek başına hangi Elasticsearch index'lerini görselleştireceğini bilmez. Index pattern ile "app-logs-*" gibi bir pattern tanımlarsınız ve Kibana o pattern'e uyan tüm index'leri (app-logs-2024.01.15, app-logs-2024.01.16...) birleştirerek gösterir. Bu, zaman bazlı index'ler (günlük, haftalık) ile çalışırken çok güçlüdür.

**KQL (Kibana Query Language) — Basit Ama Güçlü Filtreleme:**

KQL, Kibana'da veri filtrelemek için kullandığınız query dilidir. SQL biliyorsanız 5 dakikada öğrenirsiniz:
- `status:error AND service:payment` → payment servisinin hataları
- `response_time > 1000` → 1 saniyeden yavaş istekler
- `message:"timeout" AND NOT service:health-check` → timeout hataları (health check hariç)
- `status:error AND @timestamp >= "2024-01-15"` → belirli tarihten sonraki hatalar

**Watchers/Alerts — Uyurken Bile Güvendesiniz:**

Manuel izleme 7/24 mümkün değil. Watcher'lar otomatik olarak belirli koşulları kontrol eder ve tetiklendiğinde aksiyon alır:
- Error rate %5'i geçerse → Slack'e mesaj at
- Response time ortalaması 2 saniyeyi geçerse → ops ekibine email gönder
- Disk kullanımı %80'i aşarsa → PagerDuty'ye incident oluştur

Bu, gece 3'te bir sorun çıktığında sizi uyandıran güvenlik ağıdır. Watcher'ları ciddiye alın — doğru konfigüre edilmiş alert'ler, downtime'ı saatlerden dakikalara indirir.

**Lens — Sürükle-Bırak Görselleştirme Oluşturucu:**

Eskiden Kibana'da görselleştirme oluşturmak karmaşık JSON query'ler yazmayı gerektiriyordu. Lens ile artık alan adlarını sürükleyip bırakarak görselleştirme oluşturabilirsiniz. "X eksenine tarih, Y eksenine hata sayısı, renk olarak servis adı" — bitti. Verileri keşfetmek ve hızlı insight elde etmek için muazzam bir araç. Teknik olmayan ekip üyeleri bile kullanabilir.

**Gerçek Dünya:** Birçok ops ekibinin ofisinde büyük bir TV ekranı vardır ve bu ekranda Kibana dashboard'u sürekli açık durur. Gerçek zamanlı error rate, response time, aktif kullanıcı sayısı, deployment durumu — hepsi gözünüzün önünde. Bir deployment sonrası error rate yükselmeye başlarsa, dashboard'a bakan herkes hemen fark eder. Bu, **observability kültürünün** fiziksel tezahürüdür. 📺

```javascript
// Create index pattern in Kibana
// Visualizations: Line chart, pie chart, data table
// Dashboards: Combine multiple visualizations
// Alerting: Trigger on specific conditions

// Example: Alert when error rate > 5%
{
  trigger: {
    schedule: { interval: '5m' }
  },
  input: {
    search: {
      request: {
        indices: ['app-logs-*'],
        body: {
          query: {
            bool: {
              filter: [
                { range: { '@timestamp': { gte: 'now-5m' } } },
                { term: { level: 'ERROR' } }
              ]
            }
          }
        }
      }
    }
  },
  condition: {
    compare: { 'ctx.payload.hits.total': { gt: 100 } }
  },
  actions: {
    email: {
      to: 'ops@company.com',
      subject: 'High error rate detected',
      body: 'Error count: {{ctx.payload.hits.total}}'
    },
    slack: {
      message: {
        text: 'Alert: High error rate!'
      }
    }
  }
}
```

### Alternative Search Solutions

Elasticsearch güçlü bir araçtır — ama güç, karmaşıklıkla birlikte gelir. Cluster yönetimi, shard optimizasyonu, JVM tuning, mapping stratejileri, node failure handling... Bunlar ciddi operasyonel yüktür. "Ben sadece arama fonksiyonu istiyorum, Elasticsearch cluster'ı yönetmek istemiyorum" diyorsanız, alternatifler var.

**Managed vs Self-hosted — Temel Karar:**

Bu karar aslında çok basit bir soruya dayanır: **Altyapı yönetmek istiyor musunuz, yoksa sadece arama API'si mi istiyorsunuz?**
- **Self-hosted (Elasticsearch):** Tam kontrol, sınırsız özelleştirme, ama operasyonel yük yüksek. DevOps ekibiniz varsa ve karmaşık arama ihtiyaçlarınız varsa ideal.
- **Managed ES (AWS OpenSearch, Elastic Cloud):** Elasticsearch'ün gücü, ama cluster yönetimini provider halleder. Orta yol.
- **SaaS (Algolia, Typesense Cloud):** Sıfır altyapı. API key alırsınız, veri gönderirsiniz, arama yaparsınız. En hızlı başlangıç.

**Karar Matrisi — Ne Zaman Hangisi?**

| Kriter | Elasticsearch | Algolia | Typesense | Meilisearch |
|---|---|---|---|---|
| **Karmaşık arama** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Operasyon kolaylığı** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Maliyet (büyük ölçek)** | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Real-time analytics** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Geliştirici deneyimi** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

#### Algolia

Algolia, dünyanın en popüler **SaaS arama API'sidir.** Hiçbir sunucu yönetmezsiniz — API key alırsınız, verilerinizi gönderirsiniz, milisaniyeler içinde arama yaparsınız. Bitmiş.

**Algolia Neden Bu Kadar Hızlı?**

Algolia'nın arama sonuçları global olarak **50ms'nin altında** döner. Bunu nasıl başarır? Verileriniz **CDN benzeri dağıtık altyapıda**, her kıtada replica'lar halinde tutulur. Kullanıcınız Tokyo'da mı? Tokyo'daki node cevap verir. İstanbul'da mı? Avrupa node'u. Bu, Elasticsearch'te kendiniz kurmanız gereken bir altyapıdır — Algolia'da kutudan çıkar.

**Developer Experience — Algolia'nın En Güçlü Yanı:**

Algolia'nın SDK'ları ve UI component'leri muhteşemdir. `InstantSearch.js` ile 30 dakikada tam fonksiyonlu bir arama sayfası (search box + filtered results + facets + pagination) kurabilirsiniz. React, Vue, Angular, iOS, Android — her platform için hazır widget'lar var. Typo tolerance (yazım hatası toleransı) da kutudan gelir: "iphne" yazarsanız "iPhone" döner.

**⚠️ Fiyat Uyarısı — Algolia'nın Karanlık Tarafı:**

Algolia küçük ölçekte harika, büyük ölçekte **PAHALI**'dır. Ücretlendirme search request ve record sayısına göre yapılır. Ayda 1 milyon arama yapıyorsanız sorun yok, ama 100 milyon arama yapıyorsanız fatura sizi öldürür. Bir startup'ın Algolia'dan Elasticsearch'e geçiş hikayesi: "Ayda $15K Algolia faturası ödüyorduk, kendi ES cluster'ımızı kurduk, maliyet $2K'ya düştü. Ama 2 mühendis 3 ay çalıştı." Her şeyin bir trade-off'u var.

**Gerçek Dünya:** Stripe'ın dokümantasyon araması, Twitch'in içerik araması, Medium'un yazı araması — hepsi Algolia kullanır. Eğer ürününüz dokümantasyon sitesi, e-ticaret veya içerik platformuysa ve hızlı, kaliteli arama istiyorsanız, Algolia ile başlayıp gerektiğinde Elasticsearch'e geçmek çok yaygın bir stratejidir.

```
Advantages:
✓ Fully managed (SaaS)
✓ Blazing fast (CDN-backed)
✓ Typo tolerance
✓ Faceted search
✓ Analytics built-in

Use Cases:
- E-commerce product search
- Documentation search
- Mobile apps

Pricing:
- Per search request
- Expensive at scale
```

```javascript
const algoliasearch = require('algoliasearch');
const client = algoliasearch('APP_ID', 'API_KEY');
const index = client.initIndex('products');

// Index objects
await index.saveObjects([
  { objectID: '1', name: 'iPhone', category: 'phones' },
  { objectID: '2', name: 'MacBook', category: 'laptops' }
]);

// Search
const { hits } = await index.search('phone', {
  filters: 'category:phones',
  hitsPerPage: 20
});
```

#### Typesense (Open-source Algolia alternative)
```
Advantages:
✓ Open-source
✓ Fast (in-memory)
✓ Easy to deploy
✓ Typo tolerance
✓ Faceting & filtering

Use Cases:
- Same as Algolia but self-hosted
- Cost-effective alternative
```

#### Meilisearch
```
Advantages:
✓ Open-source
✓ Ultra-relevant results
✓ Instant search (< 50ms)
✓ Easy setup
✓ Beautiful default UI

Use Cases:
- Documentation
- E-commerce
- SaaS applications
```

### Real-time Data Processing

#### Apache Kafka Streams

Kafka Streams, Kafka'nın kendisi **değildir** — onu bir kütüphane olarak düşünün. Kafka zaten orada, topic'lerde veri akıyor. Kafka Streams ise bu akan verinin üstüne oturan, onu **gerçek zamanlı işleyen** bir Java/Scala kütüphanesidir. Ayrı bir cluster kurmanıza gerek yok, ayrı bir framework öğrenmenize gerek yok — uygulamanızın içine embed olur ve çalışır.

**Stream Processing vs Batch Processing** — bunu şöyle hayal edin: Batch processing, bir fabrikadaki **gece vardiyası** gibidir. Gün boyunca ürünler depoda birikir, gece olunca bir ekip gelir, hepsini sıralar, paketler, etiketler. Sabah olduğunda her şey hazırdır ama **gecikme** vardır. Stream processing ise **konveyör bant** gibidir. Ürün bant üzerinden geçerken, o anda etiketlenir, paketlenir, yönlendirilir. Hiçbir şey beklemez — her şey *akan su gibi* gerçek zamanlı işlenir.

Kafka Streams tam da bu konveyör banttır. Event'ler Kafka topic'lerine düştüğü anda onları yakalar ve işler. Bu "real-time" mı yoksa "near-real-time" mı? Teknik olarak **near-real-time** (milisaniyeler seviyesinde gecikme var) ama pratik amaçlar için gerçek zamanlı kabul edebilirsiniz.

**Temel Kavramlar:**
- **KStream**: Sonsuz bir event akışı. Her kayıt bağımsızdır. "Kullanıcı X, ürün Y'yi satın aldı" gibi olaylar.
- **KTable**: Bir state tablosu. Her key'in **son değerini** tutar. "Kullanıcı X'in bakiyesi 500 TL" gibi. KStream append-only iken, KTable upsert mantığıyla çalışır.
- **Windowing**: Zaman bazlı gruplama. "Son 5 dakikadaki satışları topla", "Her saat başı ortalama hesapla" gibi. Tumbling (sabit pencere), Hopping (kayan pencere), Session (oturum bazlı) window türleri var.
- **Exactly-once semantics**: Kafka Streams, mesaj işleme garantisi sunar — bir event tam olarak **bir kez** işlenir.

**Ne Zaman Kullanılır?**
- 🏦 **Fraud detection**: Kredi kartı işlemi gerçekleştiği anda, son 5 dakikadaki pattern'lere bakıp anomali tespiti
- 📊 **Real-time analytics**: Canlı dashboard'lar, anlık metrikler
- 🔄 **Event transformation**: Bir topic'teki veriyi zenginleştirip başka bir topic'e yazma
- 🔗 **Stream-stream join**: İki farklı veri akışını birleştirme (sipariş + ödeme)

**Kafka Streams vs Flink vs Spark Streaming:**
| | Kafka Streams | Apache Flink | Spark Streaming |
|---|---|---|---|
| Deployment | Kütüphane (app içine embed) | Ayrı cluster | Ayrı cluster |
| Karmaşıklık | Düşük | Yüksek | Orta |
| Latency | Milisaniye | Milisaniye | Saniye (micro-batch) |
| State management | RocksDB (lokal) | Distributed state | RDD-based |
| Kullanım | Basit-orta stream işleme | Kompleks event processing | Büyük veri + ML pipeline |

Kafka Streams'in güzelliği **sadeliğidir**. Flink veya Spark gibi devasa bir cluster yönetmenize gerek yok. Ama çok kompleks event processing (CEP) yapacaksanız, Flink daha güçlüdür.

> 🎬 **Gerçek Dünya:** Netflix, Kafka Streams kullanarak **gerçek zamanlı kişiselleştirme** yapıyor. Siz bir film izlerken, izleme davranışınız Kafka'ya akıyor, Kafka Streams bu event'leri işleyerek "Bu kullanıcı aksiyon filmi seviyor" sonucunu çıkarıyor ve bir sonraki öneriniz buna göre şekilleniyor — hepsi siz filmi izlerken, gerçek zamanlı olarak.

```java
// Stream processing
StreamsBuilder builder = new StreamsBuilder();

KStream<String, Order> orders = builder.stream("orders");

// Filter
KStream<String, Order> largeOrders = orders.filter(
  (key, order) -> order.getTotal() > 1000
);

// Map transformation
KStream<String, OrderSummary> summaries = orders.mapValues(
  order -> new OrderSummary(order.getId(), order.getTotal())
);

// Group and aggregate
KTable<String, Long> orderCounts = orders
  .groupByKey()
  .count();

// Join streams
KStream<String, EnrichedOrder> enriched = orders.join(
  customers,
  (order, customer) -> new EnrichedOrder(order, customer),
  JoinWindows.of(Duration.ofMinutes(5))
);

// Write to output topic
enriched.to("enriched-orders");
```

#### AWS Kinesis

AWS Kinesis'i şöyle düşünün: Amazon bir gün Kafka'ya baktı ve dedi ki *"Bunu biz de yapabiliriz, hem de müşterilerimiz hiç cluster yönetmek zorunda kalmaz."* İşte Kinesis, **Amazon'un fully managed stream processing servisi**dir. Kafka'nın yaptığı işin çoğunu yapar, ama siz broker kurmaz, ZooKeeper/KRaft yönetmez, disk kapasitesi planlamazsınız — AWS her şeyi sizin yerinize halleder.

**Kinesis vs Kafka — büyük tartışma:**
| | AWS Kinesis | Apache Kafka |
|---|---|---|
| Yönetim | Fully managed (sıfır ops) | Self-managed veya Confluent Cloud |
| Maliyet | Shard başına saatlik ücret | Sunucu + disk + insan maliyeti |
| Throughput | Shard başına 1MB/s yazma, 2MB/s okuma | Partition başına teorik sınır çok yüksek |
| Retention | Default 24 saat (max 365 gün) | Sınırsız (disk izin verdiği kadar) |
| Ecosystem | AWS servislerine native entegrasyon | Devasa açık kaynak ekosistem |
| Vendor lock-in | Evet, tamamen AWS'ye bağlısınız | Hayır, her yerde çalışır |

**Kinesis Servisleri — dört kardeş:**
1. **Kinesis Data Streams**: Ana servis. Kafka topic'lerine benzer stream'ler oluşturursunuz. Shard'lara bölünür.
2. **Kinesis Data Firehose**: *"Veriyi al, şuraya yaz, ben uğraşmayım"* servisi. Stream'den gelen veriyi otomatik olarak S3, Redshift, Elasticsearch'e yazar. Zero-code ETL gibi.
3. **Kinesis Data Analytics**: Stream üzerinde SQL sorgusu yazmak! `SELECT * FROM user_events WHERE event = 'purchase' AND amount > 100` — gerçek zamanlı.
4. **Kinesis Video Streams**: Video akışlarını yakalamak, işlemek ve depolamak için. Güvenlik kameraları, drone görüntüleri gibi.

**Shard kavramı:** Kinesis'te **shard = partition**. Her shard:
- Yazma: **1 MB/s** veya **1000 kayıt/s**
- Okuma: **2 MB/s**
Daha fazla throughput istiyorsanız, daha fazla shard eklemeniz gerekir. Bu da maliyet demektir — Kafka'da partition eklemek bedava, Kinesis'te shard eklemek para.

**Ne Zaman Kinesis?**
- Zaten **AWS ekosistemindesiniz** ve her şey (Lambda, S3, DynamoDB) AWS'de
- Kafka cluster yönetmek **istemiyorsunuz** (veya DevOps kapasiteniz yok)
- Ölçeğiniz orta düzeyde — günde milyonlarca event, ama milyarlarca değil
- Hızlıca başlamak istiyorsunuz — 5 dakikada stream oluşturup veri akıtabilirsiniz

> 🌡️ **Gerçek Dünya Senaryosu:** Bir IoT projesi düşünün — binlerce sensör her saniye sıcaklık, nem, basınç verisi gönderiyor. Akış şöyle: **Sensörler → Kinesis Data Streams → Lambda (anomali tespiti) → DynamoDB (depolama) + SNS (alarm)**. Eğer bir sensör anormal değer gönderirse, Lambda bunu yakalar, DynamoDB'ye kaydeder ve SNS ile operasyon ekibine bildirim gönderir. Tüm bu pipeline'ı Kafka ile de kurabilirsiniz, ama Kinesis'te bunu **sıfır sunucu yönetimi** ile yaparsınız.

```javascript
const AWS = require('aws-sdk');
const kinesis = new AWS.Kinesis();

// Put record
await kinesis.putRecord({
  StreamName: 'user-events',
  Data: JSON.stringify({
    userId: '123',
    event: 'page_view',
    page: '/products',
    timestamp: Date.now()
  }),
  PartitionKey: 'user-123'
}).promise();

// Consumer (Lambda)
exports.handler = async (event) => {
  for (const record of event.Records) {
    const data = JSON.parse(
      Buffer.from(record.kinesis.data, 'base64').toString()
    );
    
    // Process event
    await processUserEvent(data);
  }
};
```

#### Redis Streams
```javascript
// Producer
await redis.xAdd('events', '*', {
  userId: '123',
  action: 'purchase',
  amount: '99.99'
});

// Consumer group
await redis.xGroupCreate('events', 'processors', '0', {
  MKSTREAM: true
});

// Read from stream
const messages = await redis.xReadGroup(
  'processors',
  'consumer-1',
  [{
    key: 'events',
    id: '>'
  }],
  {
    COUNT: 10,
    BLOCK: 5000
  }
);

// Process and acknowledge
for (const [stream, entries] of messages) {
  for (const { id, message } of entries) {
    await processEvent(message);
    await redis.xAck('events', 'processors', id);
  }
}
```

---

## 🔐 Security & Authentication

### Authentication Methods

**Kimlik doğrulama (Authentication)** = "SEN KİMSİN?" sorusunun cevabı.
**Yetkilendirme (Authorization)** = "SEN NE YAPABİLİRSİN?" sorusunun cevabı.

Bu ikisi FARKLI kavramlar! Authentication olmadan authorization olmaz, ama ayrı ayrı yönetilmelidirler.

#### JWT (JSON Web Tokens)

**JWT nedir?** Kullanıcı giriş yaptığında, sunucu ona bir "pas" verir. Bu pas 3 parçadan oluşur: Header (algoritma bilgisi) + Payload (kullanıcı verileri) + Signature (İmza). Client her istekte bu pası gönderir, sunucu imzayı doğrulayarak kullanıcıyı tanır.

**JWT vs Session:** 
- **Session:** Sunucu kullanıcı bilgisini HAFIZASINDA saklar (Redis/DB). Stateful.
- **JWT:** Kullanıcı bilgisi TOKEN'İN İÇİNDE! Sunucu hiçbir şey saklamaz. Stateless.

**JWT'nin Tüyoları ve Tuzakları:**
- ✅ Stateless = Ölçekleme kolay (her sunucu doğrulayabilir)
- ✅ Microservices'te ideal (her servis kendi başına doğrulayabilir)
- ❌ TOKEN İPTAL EDİLEMEZ! Access token süresi dolana kadar geçerli
- ❌ Büyük payload = her istekte KB'lar taşınır (cookie'de 4KB limit!)
- ❌ Token çalınırsa = hırsız da kullanabilir (refresh token + kısa access token süresi ile azalt)

**Gerçek dünya patikası:** Access token süresi 15 dakika, refresh token süresi 7 gün. Kullanıcı her 15 dakikada refresh token ile yeni access token alır. Refresh token çalınırsa? → Token rotation ile eski refresh token iptal olur.
```javascript
const jwt = require('jsonwebtoken');

// Generate token
function generateToken(user) {
  return jwt.sign(
    { 
      userId: user.id, 
      email: user.email,
      role: user.role 
    },
    process.env.JWT_SECRET,
    { expiresIn: '1h' }
  );
}

// Verify token
function verifyToken(token) {
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    return decoded;
  } catch (err) {
    throw new Error('Invalid token');
  }
}

// Middleware
function authMiddleware(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  try {
    req.user = verifyToken(token);
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

#### OAuth 2.0 / OpenID Connect

OAuth 2.0'u anlamak için en güzel analoji **vale parking anahtarı**dır. Bir otele gittiğinizde vale'ye arabanızın anahtarını verirsiniz, ama bu anahtar sadece arabayı park etmeye yarar — bagajı açamaz, torpido gözüne erişemez, hız sınırlayıcısı vardır. İşte OAuth 2.0 tam olarak budur: bir uygulamaya **sınırlı erişim** verirsiniz, **tam kontrolü değil**. "Spotify, Google kişilerime erişsin ama e-postalarımı okumasın" dediğinizde OAuth 2.0 devreye girer.

**OAuth 2.0 Rolleri (Oyuncular):**

Bu protokolde dört ana aktör vardır ve her birinin rolünü anlamak kritiktir:

| Rol | Açıklama | Örnek |
|-----|----------|-------|
| **Resource Owner** | Verilerin sahibi (yani siz, kullanıcı) | Google hesabınızın sahibi |
| **Client** | Verilerinize erişmek isteyen uygulama | Spotify, Notion, Slack |
| **Authorization Server** | Kimlik doğrulama ve token veren sunucu | Google OAuth Server |
| **Resource Server** | Korunan verileri barındıran API | Google Contacts API |

**OAuth 2.0 Flow'ları (Akışlar):**

🔹 **Authorization Code Flow** — Web uygulamaları için en yaygın ve en güvenli flow. Kullanıcı Authorization Server'a yönlendirilir, giriş yapar, bir authorization code döner, bu code backend'de access_token ile değiştirilir. Backend'in secret'ı güvenle saklaması gerekir. *"Klasik, güvenilir, herkesten önce bunu öğren."*

🔹 **Client Credentials Flow** — Machine-to-machine (M2M) iletişim için. Kullanıcı yok, iki sunucu birbirleriyle konuşuyor. Microservice A, Microservice B'nin API'ına erişmek istiyor — kendi client_id ve client_secret'ı ile doğrudan token alır. *"İnsan yok, robot robota konuşuyor."*

🔹 **Implicit Flow** — ⚠️ **DEPRECATED!** Eskiden SPA'lar için kullanılırdı. Token doğrudan URL fragment'ında dönerdi (`#access_token=xyz`). Sorun? Token browser history'de kalır, referrer header ile sızar, XSS'e açıktır. **Artık kullanmayın.** PKCE ile Authorization Code Flow kullanın.

🔹 **PKCE (Proof Key for Code Exchange) Flow** — Modern SPA'lar ve mobil uygulamalar için. Authorization Code Flow'un geliştirilmiş hali. Client bir `code_verifier` (rastgele string) oluşturur, bunun hash'ini (`code_challenge`) authorization request'e ekler. Token exchange sırasında orijinal `code_verifier`'ı gönderir. Bu sayede authorization code çalınsa bile, `code_verifier` olmadan token alınamaz. *"Zarfın içine mektup koyup mühürlüyorsunuz, sadece mühürün sahibi açabiliyor."*

**OAuth 2.0 vs OpenID Connect (OIDC):**

Bu ikisi sıkça karıştırılır ama farkları kritiktir:

| | OAuth 2.0 | OpenID Connect (OIDC) |
|--|-----------|----------------------|
| **Amaç** | Authorization (Yetkilendirme) | Authentication (Kimlik Doğrulama) |
| **Cevapladığı soru** | "Bu uygulama **ne yapabilir**?" | "Bu kullanıcı **kim**?" |
| **Token** | `access_token` | `id_token` (JWT formatında) |
| **Analoji** | Otel odası kartı (havuza girebilir, spor salonuna giremez) | Pasaport (kim olduğunuzu kanıtlar) |

OIDC, OAuth 2.0'ın **üzerine** inşa edilmiş bir katmandır. OAuth 2.0 tek başına kimlik doğrulama yapmaz — sadece erişim izni verir. OIDC eklenince "Bu kişi Hulusi Önel, e-postası xyz@gmail.com" bilgisini de alırsınız.

**Token'lar — Üç Silahşörler:**

- **`access_token`**: API'lara erişim için kullanılır. Kısa ömürlüdür (genellikle 15 dk - 1 saat). Hırsız çalsa bile kısa süre geçerlidir.
- **`refresh_token`**: Yeni `access_token` almak için kullanılır. Uzun ömürlüdür (günler/haftalar). **Backend'de güvenle saklanmalıdır.** Çalınırsa ciddi risk oluşturur.
- **`id_token`**: OIDC tarafından sağlanır. JWT formatında kullanıcı bilgilerini içerir (isim, e-posta, avatar). API çağrılarında kullanılmaz, sadece kimlik doğrulama içindir.

**"Login with Google" Butonuna Bastığınızda Ne Olur? (Adım Adım):**

1. Kullanıcı "Login with Google" butonuna tıklar
2. Uygulama, kullanıcıyı Google'ın Authorization Server'ına yönlendirir (`accounts.google.com/o/oauth2/v2/auth?client_id=...&scope=profile email&redirect_uri=...`)
3. Google kullanıcıya sorar: "Bu uygulama profilinize ve e-postanıza erişmek istiyor. İzin veriyor musunuz?"
4. Kullanıcı "Evet" der
5. Google, kullanıcıyı `redirect_uri`'ye yönlendirir ve URL'ye bir `authorization_code` ekler
6. Uygulamanın backend'i bu code'u alır ve Google'a gizlice bir POST request atar (client_secret ile birlikte)
7. Google `access_token` + `refresh_token` + `id_token` döner
8. Uygulama `id_token`'dan kullanıcı bilgilerini çıkarır, veritabanında arar/oluşturur
9. Kullanıcıya kendi session/JWT'sini verir — artık Google ile işi kalmaz

**Sık Yapılan Hatalar (Production'da Gözyaşı Garantili):**

- 🚫 **Token'ları `localStorage`'da saklamak**: XSS saldırısında tüm token'lar çalınır. `httpOnly` cookie kullanın.
- 🚫 **`access_token`'ı server-side validate etmemek**: Client'tan gelen her token'ı doğrulayın. İmza kontrolü, expiry kontrolü, issuer kontrolü yapın.
- 🚫 **`state` parametresini kullanmamak**: CSRF saldırılarına açık kalırsınız. Authorization request'e rastgele bir `state` ekleyin, callback'de doğrulayın.
- 🚫 **Scope'ları gereğinden geniş tutmak**: Sadece `profile` ve `email` yeterliyken `https://www.googleapis.com/auth/drive` istemek — kullanıcı güvenini kaybedersiniz.
- 🚫 **`redirect_uri`'yi wildcard yapmak**: `redirect_uri=https://*.myapp.com` gibi gevşek tanımlar open redirect saldırılarına kapı açar.

```javascript
// OAuth flow with Passport.js
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;

passport.use(new GoogleStrategy({
    clientID: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: '/auth/google/callback'
  },
  async (accessToken, refreshToken, profile, done) => {
    // Find or create user
    let user = await User.findOne({ googleId: profile.id });
    
    if (!user) {
      user = await User.create({
        googleId: profile.id,
        email: profile.emails[0].value,
        name: profile.displayName
      });
    }
    
    return done(null, user);
  }
));

// Routes
app.get('/auth/google',
  passport.authenticate('google', { scope: ['profile', 'email'] })
);

app.get('/auth/google/callback',
  passport.authenticate('google', { failureRedirect: '/login' }),
  (req, res) => {
    const token = generateToken(req.user);
    res.redirect(`/dashboard?token=${token}`);
  }
);
```

#### Session-based Authentication

Session-based authentication'ı anlamak için **müzik festivali bilekliği** analojisini düşünün. Festivale girişte biletinizi gösterirsiniz, görevli bileğinize bir bileklik takar. Artık festival boyunca her sahneye girişte biletinizi tekrar göstermezsiniz — sadece bileğinizi gösterirsiniz. Güvenlik görevlisi bileğe bakar, "tamam geç" der. İşte session-based auth tam olarak böyle çalışır: bir kez kimliğinizi kanıtlarsınız, sonra size bir "bileklik" (session ID cookie) verilir.

**Session Auth Nasıl Çalışır? (Adım Adım):**

1. **Login**: Kullanıcı email + password gönderir
2. **Server doğrular**: Credentials kontrol edilir (bcrypt ile hash karşılaştırma)
3. **Session oluşturulur**: Server tarafında bir session objesi yaratılır (`{ userId: 42, role: 'admin', createdAt: ... }`)
4. **Session saklanır**: Bu obje Redis/veritabanında bir unique session ID ile saklanır (örn: `sess:abc123xyz`)
5. **Cookie gönderilir**: Client'a `Set-Cookie: sessionId=abc123xyz` header'ı ile session ID iletilir
6. **Sonraki istekler**: Browser her request'te `Cookie: sessionId=abc123xyz` header'ını otomatik gönderir
7. **Server kontrol eder**: Session ID ile Redis'ten session verisini çeker, kullanıcıyı tanır

**Session Storage Seçenekleri:**

| Storage | Avantaj | Dezavantaj | Production? |
|---------|---------|------------|-------------|
| **In-Memory** (default) | Hızlı, kolay | Server restart = tüm session'lar silinir. Birden fazla server'da paylaşılamaz | ⛔ **ASLA!** |
| **Redis** | Ultra hızlı, TTL desteği, cluster desteği | Ek altyapı gerektirir | ✅ **Önerilen** |
| **PostgreSQL/MongoDB** | Persistent, mevcut DB kullanılır | Daha yavaş, connection overhead | ⚠️ Kabul edilebilir |
| **Memcached** | Hızlı | Persistence yok, eviction riski | ⚠️ Dikkatli kullanın |

**Neden Redis?** Çünkü Redis in-memory bir data store — okuma/yazma süresi ~1ms. TTL (Time-To-Live) desteği var, yani session otomatik expire olur, siz temizlemek zorunda kalmazsınız. Birden fazla Node.js instance'ınız varsa (ki production'da kesinlikle olmalı), tüm instance'lar aynı Redis'e bağlanır ve session state'i paylaşır. Sticky session gibi hacklerle uğraşmazsınız.

**Session Fixation Saldırısı ve Korunma:**

Bu saldırıda hacker, kurbanın session ID'sini önceden belirler. Senaryo: Hacker bir session başlatır (`sessionId=evil123`), bu ID'yi kurbanın browser'ına yerleştirir (XSS, URL manipulation vb.), kurban login olur — ama session ID hâlâ `evil123`tir! Artık hacker aynı session ID ile sisteme erişebilir. **Korunma**: Login sonrası **mutlaka** `req.session.regenerate()` çağırın. Bu, eski session ID'yi geçersiz kılar ve yeni bir tane oluşturur.

**JWT vs Session Karşılaştırması:**

| Özellik | JWT | Session |
|---------|-----|--------|
| **State** | Stateless (token'da her şey var) | Stateful (server'da session store) |
| **Ölçeklenebilirlik** | Kolay (her server doğrulayabilir) | Redis gibi shared store gerektirir |
| **Revocation (İptal)** | Zor! Token expire olana kadar geçerli | Kolay! Redis'ten session'ı silin, bitti |
| **Boyut** | Büyük (payload + signature ~800 byte) | Küçük (sadece session ID ~32 byte cookie) |
| **Güvenlik** | Token çalınırsa expire'a kadar yapacak bir şey yok | Session çalınırsa anında invalidate edebilirsiniz |
| **Kullanım** | Microservices, API'lar, mobile apps | Monolith web apps, admin paneller |
| **Logout** | Gerçek logout zor (blacklist gerekir) | `req.session.destroy()` — temiz ve kesin |

**Ne Zaman Session Kullanmalı?**
- Geleneksel web uygulamaları (server-rendered, SSR)
- Admin panelleri (anlık session iptal yeteneği kritik)
- Güvenlik hassasiyeti yüksek uygulamalar (bankacılık, sağlık)
- Kullanıcı cihaz/oturum yönetimi gerektiğinde ("Tüm cihazlardan çıkış yap")

**Cookie Ayarları — Her Birinin Anlamı:**

- **`httpOnly: true`** → JavaScript ile cookie'ye erişilemez. XSS saldırısında `document.cookie` ile session ID çalınamaz. **Her zaman `true` olmalı.**
- **`secure: true`** → Cookie sadece HTTPS üzerinden gönderilir. HTTP'de çalışmaz. Production'da **mutlaka `true`**. Development'ta `false` yapabilirsiniz.
- **`sameSite: 'strict'`** → Cookie sadece aynı site'den gelen isteklerde gönderilir. CSRF koruması sağlar. `'lax'` top-level navigation'a izin verir (link tıklama). `'none'` tüm cross-site isteklerde gönderir (sadece `secure: true` ile).
- **`maxAge: 86400000`** → Cookie'nin ömrü (milisaniye). 24 saat = 86.400.000 ms. Bu süre sonunda browser cookie'yi otomatik siler.

```javascript
const session = require('express-session');
const RedisStore = require('connect-redis').default;

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: true, // HTTPS only
    httpOnly: true, // No JS access
    maxAge: 24 * 60 * 60 * 1000 // 24 hours
  }
}));

// Login
app.post('/login', async (req, res) => {
  const user = await User.findByCredentials(req.body.email, req.body.password);
  req.session.userId = user.id;
  res.json({ success: true });
});

// Protected route
app.get('/profile', (req, res) => {
  if (!req.session.userId) {
    return res.status(401).json({ error: 'Not authenticated' });
  }
  // ...
});
```

### Authorization (RBAC, ABAC)

Authentication "**Sen kimsin?**" sorusunu cevaplar, Authorization ise "**Ne yapabilirsin?**" sorusunu. Bu ikisini karıştırmak, kapıda kimlik kontrolü yapmakla odaların hangisine girip giremeyeceğinizi belirlemek arasındaki farkı karıştırmak gibidir.

En güzel analoji **ofis binasındaki kapı kartı sistemi**dir. Binaya girişte kartınızı okutursunuz (authentication). Ama kartınız hangi katlara, hangi odalara erişim verir? İşte bu authorization. Stajyer kartıyla server odasına giremezsiniz, ama kafeteryaya girebilirsiniz. CTO'nun kartı her yeri açar. Aynı bina, aynı kart okuyucu — ama kartınızdaki **yetkiler** farklı.

---

#### RBAC (Role-Based Access Control) — Rol Tabanlı Erişim Kontrolü

RBAC'ın mantığı basittir: **Kullanıcılara roller atayın, rollere izinler atayın.** Kullanıcı doğrudan izin almaz — bir role dahil olur ve o rolün izinlerini miras alır.

**Nasıl çalışır?**
1. İzinleri tanımla: `read`, `write`, `delete`, `manage_users`
2. Rolleri tanımla ve izinleri ata:
   - `admin` → `[read, write, delete, manage_users]`
   - `editor` → `[read, write]`
   - `viewer` → `[read]`
3. Kullanıcıya rol ata: `hulusi.role = 'editor'`
4. Erişim kontrolü: `hulusi` bir kaynak silmek istediğinde → rolü `editor` → `delete` izni var mı? → **Hayır → 403 Forbidden**

**RBAC Hiyerarşisi (Role Inheritance):**

Akıllı RBAC sistemlerinde roller birbirinden miras alır:

```
admin ← her şeyi yapabilir (editor + delete + manage_users)
  └── editor ← okuyup yazabilir (viewer + write)
        └── viewer ← sadece okuyabilir (read)
```

Bu hiyerarşi sayesinde `admin` rolüne sadece `delete` ve `manage_users` eklemeniz yeterli — `read` ve `write` zaten `editor`'dan miras gelir.

**Gerçek Dünya Örneği — GitHub Repository Rolleri:**

| Rol | İzinler |
|-----|--------|
| **Owner** | Repo silme, üyeleri yönetme, billing, her şey |
| **Maintainer** | Branch protection, PR merge, issue yönetimi |
| **Developer (Write)** | Push, PR oluşturma, branch yönetimi |
| **Triage** | Issue ve PR etiketleme, atama (kod yazma yok) |
| **Read** | Sadece kodu okuma, issue/PR görüntüleme |

---

#### ABAC (Attribute-Based Access Control) — Nitelik Tabanlı Erişim Kontrolü

ABAC, RBAC'ın kardeşi ama çok daha **esnek ve güçlü**dür. ABAC'ta erişim kararları **niteliklere (attributes)** göre verilir. Dört tür nitelik değerlendirilir:

1. **User Attributes**: Kullanıcının departmanı, lokasyonu, kıdem seviyesi (`user.department === 'engineering'`)
2. **Resource Attributes**: Kaynağın sahibi, tipi, durumu (`resource.authorId`, `resource.status === 'published'`)
3. **Action Attributes**: Yapılmak istenen eylem (`action === 'delete'`)
4. **Environment Attributes**: Zaman, IP adresi, cihaz türü (`time > '09:00' && time < '18:00'`)

**Gerçek Dünya Örneği — AWS IAM Policies:**

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::company-data/*",
  "Condition": {
    "StringEquals": { "aws:PrincipalTag/department": "engineering" },
    "IpAddress": { "aws:SourceIp": "10.0.0.0/8" },
    "DateGreaterThan": { "aws:CurrentTime": "2024-01-01T00:00:00Z" }
  }
}
```
Bu policy şunu söylüyor: "Engineering departmanındaki kullanıcılar, şirket VPN'inden (10.0.0.0/8), 2024'ten sonra S3'teki company-data bucket'ına erişebilir." Bunu RBAC ile ifade etmeye çalışın — kafanız karışır.

**RBAC vs ABAC Karşılaştırması:**

| Özellik | RBAC | ABAC |
|---------|------|------|
| **Karmaşıklık** | Düşük — roller ve izinler basit | Yüksek — policy engine gerektirir |
| **Esneklik** | Sınırlı — rol tanımları statik | Çok esnek — dinamik kurallar yazılabilir |
| **Yönetim** | Kolay — 5-10 rol yeterli | Zor — policy'ler karmaşıklaşabilir |
| **Performans** | Hızlı — basit lookup | Daha yavaş — policy evaluation |
| **Ne zaman?** | Sabit roller yeterli olduğunda | Bağlama göre karar verilmesi gerektiğinde |
| **Örnek** | "Admin her şeyi yapabilir" | "Sadece kendi departmanındaki kaynakları düzenleyebilir" |

**RBAC Ne Zaman Yetmez?**

Şu senaryoyu düşünün: "Editor, sadece **kendi** yazılarını düzenleyebilir." RBAC ile bunu ifade edemezsiniz! Çünkü RBAC sadece **rolü** kontrol eder: "Sen editor mısın? Evet. O zaman `write` iznin var." Ama **hangi** kaynağa yazacağınızı kontrol edemez. İşte tam burada ABAC devreye girer: `user.id === resource.authorId && user.role === 'editor'` — nitelik bazlı kontrol.

Benzer senaryolar:
- "Kullanıcı sadece **mesai saatlerinde** (09:00-18:00) hassas verilere erişebilir" → Environment attribute
- "Sadece **Türkiye'deki** çalışanlar TR müşteri verilerini görebilir" → User location attribute
- "Draft durumundaki yazıları sadece **yazarı** görebilir, published olanları herkes" → Resource status attribute

**Permission Creep — Sessiz Katil:**

Permission creep, zamanla kullanıcılara izinlerin eklenmesi ama **eski izinlerin asla kaldırılmaması** durumudur. Bir çalışan proje A'da çalışırken admin yetkisi alır. Proje B'ye geçer, yeni yetkiler eklenir — ama proje A'daki admin yetkisi kaldırılmaz. 3 yıl sonra bu çalışan, şirketin yarısına admin erişimine sahiptir ve hiç kimse farkında değildir. 😱

**Korunma yolları:**
- **Regular access reviews**: Üç ayda bir tüm izinleri gözden geçirin
- **Principle of Least Privilege**: En az yetki prensibi — sadece ihtiyaç duyulan izinleri verin
- **Time-based access**: Geçici izinler verin, süre dolunca otomatik kaldırılsın
- **Access logging**: Kim, ne zaman, neye erişti — audit trail tutun
- **Role mining**: Mevcut erişim pattern'lerini analiz edip gereksiz izinleri tespit edin

---

**RBAC (Role-Based Access Control):**
```javascript
// Define roles and permissions
const roles = {
  admin: ['read', 'write', 'delete', 'manage_users'],
  editor: ['read', 'write'],
  viewer: ['read']
};

function can(user, permission) {
  const userPermissions = roles[user.role] || [];
  return userPermissions.includes(permission);
}

// Middleware
function requirePermission(permission) {
  return (req, res, next) => {
    if (!can(req.user, permission)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

// Usage
app.delete('/users/:id', 
  authMiddleware, 
  requirePermission('delete'), 
  deleteUser
);
```

**ABAC (Attribute-Based Access Control):**
```javascript
// More granular control
function authorize(user, resource, action) {
  // Can edit own posts
  if (action === 'edit' && resource.type === 'post') {
    return resource.authorId === user.id || user.role === 'admin';
  }
  
  // Can view published posts or own drafts
  if (action === 'view' && resource.type === 'post') {
    return resource.status === 'published' || resource.authorId === user.id;
  }
  
  return false;
}
```

### Security Best Practices

**Input Validation:**

🛂 **"Never Trust User Input" — Güvenliğin Altın Kuralı #1**

Input validation, backend güvenliğinin HAVALİMANI GÜVENLİĞİ'dir. Düşün: havalimanına girdiğinde çantanı X-ray'den geçirirler, pasaportunu kontrol ederler, metal dedektöründen geçersin. Neden? Çünkü **içeri giren her şey potansiyel tehdit**. Backend'de de AYNI mantık geçerli — kullanıcıdan gelen HER VERİ potansiyel bir saldırı vektörüdür.

Mantra'yı ezberle: **"Never trust user input."** Kullanıcı "Hulusi" yazabilir, ama aynı input alanına `<script>alert('hacked')</script>` veya `'; DROP TABLE users;--` de yazabilir. Sen bunu ENGELLEMELISIN.

**Whitelist vs Blacklist Validation:**
- ❌ **Blacklist (Kara liste):** "Şu karakterleri YASAKLA" → Hacker yeni bir karakter bulur, bypass eder. Kedi-fare oyunu.
- ✅ **Whitelist (Beyaz liste):** "SADECE şu formata uyan verileri KABUL ET" → Email alanına sadece email formatı, yaş alanına sadece sayı. Çok daha güvenli.

Whitelist DAIMA daha iyidir çünkü neyin YASAK olduğunu değil, neyin İZİNLİ olduğunu tanımlarsın. Saldırganın yaratıcılığına karşı değil, senin kurallarına karşı yarışır.

⚠️ **Client-side validation GÜVENLİK DEĞİLDİR!** Kullanıcı tarayıcıdaki JavaScript validasyonunu `curl`, Postman veya browser DevTools ile 2 saniyede bypass edebilir. Frontend validasyonu sadece UX içindir — gerçek güvenlik DAIMA backend'de olmalıdır.

😂 **Gerçek Dünya Dehşeti: Bobby Tables (xkcd #327)**

Bir okul, öğrenci kayıt sistemi yapıyor. Bir veli, çocuğunun adını şöyle giriyor:
```
Robert'); DROP TABLE students;--
```
Sistem input validation yapmadığı için bu "isim" direkt SQL query'ye giriyor ve... TÜM öğrenci tablosu siliniyor! 💀 Bu hikaye o kadar meşhur ki, "Bobby Tables" artık güvenlik dünyasında bir meme oldu.

**Schema Validation Kütüphaneleri:**
| Kütüphane | Artıları | Eksileri |
|-----------|----------|----------|
| **Joi** | En olgun, Hapi.js ekosistemi, zengin API | Bundle boyutu büyük, TypeScript desteği orta |
| **Yup** | React/Formik ile harika uyum, async validation | Frontend odaklı, backend'de Joi kadar güçlü değil |
| **Zod** | TypeScript-first, type inference harika, küçük boyut | Daha yeni, ekosistem henüz Joi kadar geniş değil |

2024+ projelerinde **Zod** TypeScript ile mükemmel uyum sağlıyor, ama Joi hâlâ Node.js backend'lerde standart.

```javascript
const Joi = require('joi');

const userSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/).required(),
  name: Joi.string().min(2).max(50).required()
});

app.post('/register', async (req, res) => {
  const { error, value } = userSchema.validate(req.body);
  
  if (error) {
    return res.status(400).json({ error: error.details[0].message });
  }
  
  // Sanitize
  const sanitizedData = {
    email: value.email.toLowerCase().trim(),
    password: await bcrypt.hash(value.password, 10),
    name: validator.escape(value.name)
  };
  
  // Create user
  const user = await User.create(sanitizedData);
  res.json(user);
});
```

**SQL Injection Prevention:**

🚪 **SQL Injection: Binanın İnterkomunu Hacklemek**

SQL Injection'ı şöyle düşün: bir apartmana giriyorsun, interkomda "Daire 5" yazıp zili çalıyorsun. Normal kullanım bu. Ama birisi interkom sistemini manipüle edip "Daire 5 VE tüm kapıları aç" komutunu gönderirse? İşte SQL Injection tam olarak budur — uygulamanın veritabanıyla konuştuğu "interkom" sistemine sızıp, **yetkisiz komutlar çalıştırmak**.

**Adım Adım Nasıl Çalışır?**

Bir login formu düşün:
1. Kullanıcı email alanına yazar: `admin@site.com`
2. Backend şu SQL'i oluşturur: `SELECT * FROM users WHERE email = 'admin@site.com'`
3. Tamam, bu normal. Ama ya kullanıcı şunu yazarsa: `' OR '1'='1`
4. SQL şöyle olur: `SELECT * FROM users WHERE email = '' OR '1'='1'`
5. `'1'='1'` HER ZAMAN true olduğu için → TÜM kullanıcılar döner! 💀

**SQL Injection Türleri:**
- **Classic (In-band):** Sonuç direkt ekranda görünür. En kolay tespit ve exploit edileni.
- **Blind SQL Injection:** Sonuç görünmez, ama saldırgan evet/hayır soruları sorarak veriyi çıkarır. "Veritabanı adının ilk harfi 'a' mı?" → true/false.
- **Time-based Blind:** Saldırgan `SLEEP(5)` gibi komutlar ekler. Sayfa 5 saniye geç yükleniyorsa → koşul doğru. Sherlock Holmes gibi dedektiflik!

**ORM Savunma Katmanı:**
Sequelize, Prisma, TypeORM gibi ORM'ler otomatik olarak **parameterized queries** kullanır. Yani `User.findOne({ where: { email: userInput } })` yazdığında, ORM arkada `$1` placeholder kullanır ve input'u ayrı parametre olarak gönderir. SQL Injection matematiksel olarak İMKANSIZ hale gelir.

🔴 **Gerçek Dünya Felaketi: 2008 Heartland Payment Systems**
ABD'nin en büyük ödeme işlemcilerinden Heartland, SQL Injection saldırısıyla hacklendi. Sonuç? **130 MİLYON kredi kartı bilgisi çalındı.** Şirket $140 milyon tazminat ödedi. Tek bir parameterized query kullanılmamış input alanı yüzünden. Tek. Bir. Alan. 😱

```javascript
// ❌ Bad (SQL Injection)
const query = `SELECT * FROM users WHERE email = '${req.body.email}'`;

// ✅ Good (Parameterized queries)
const query = 'SELECT * FROM users WHERE email = $1';
const result = await db.query(query, [req.body.email]);
```

**XSS Prevention:**

🏪 **XSS: Mağazaya Sahte Tabela Asmak**

XSS'i (Cross-Site Scripting) şöyle düşün: bir mağazaya giriyorsun ve duvarda bir tabela var: "Kampanya için kredi kartı bilgilerinizi şu linke girin!" Tabela mağazanın değil, birinin gizlice astığı SAHTE bir tabela. Ama sen mağazanın içinde olduğun için güveniyorsun. XSS tam olarak budur — saldırgan, güvenilir bir web sitesinin içine **kendi kodunu enjekte eder** ve kullanıcılar "bu site güvenli" diye düşündükleri için tuzağa düşer.

**XSS Türleri:**

1. **Stored XSS (En Tehlikeli! 💀):** Kötü kod veritabanına KAYDEDİLİR. Örneğin bir foruma `<script>document.cookie</script>` içeren yorum yazarsın. Bu yorum veritabanında saklanır ve sayfayı açan HER kullanıcıda çalışır. Tek seferde binlerce kurban.

2. **Reflected XSS:** Kötü kod URL'de taşınır. `site.com/search?q=<script>alert('xss')</script>` — Kullanıcı bu linke tıkladığında script çalışır. Phishing e-postalarıyla yayılır.

3. **DOM-based XSS:** JavaScript, DOM'u manipüle ederken oluşur. Sunucu görmez bile — tamamen browser tarafında gerçekleşir. `document.innerHTML = userInput` yazmak = intihar. 🙃

🐛 **Gerçek Dünya Efsanesi: 2005 Samy Worm (MySpace)**

Samy Kamkar adında 19 yaşında bir genç, MySpace profiline bir XSS worm yerleştirdi. Profili ziyaret eden herkesin profiline otomatik olarak "Samy is my hero" yazılıyordu VE aynı worm onların profiline de yayılıyordu. Sonuç? **20 saat içinde 1 MİLYON kullanıcı** etkilendi. MySpace'in tüm siteyi kapatması gerekti. Samy "Ben sadece arkadaş edinmek istemiştim" dedi. 😂 Tarihin en hızlı yayılan virus'ü olarak kayıtlara geçti.

🛡️ **Content Security Policy (CSP):**
CSP, tarayıcıya "Bu sayfada SADECE şu kaynaklardan gelen script'ler çalışabilir" diyen bir HTTP header'dır. Yani saldırgan bir `<script>` enjekte etse bile, CSP header'ı tarayıcıya "Bu script izin verilen listede yok, ÇALIŞTIRMA" der. İkinci bir savunma hattı.

**Üçlü Savunma Stratejisi:**
1. 🧹 **Sanitize Input:** Gelen veriyi temizle (DOMPurify, validator.js)
2. 🔒 **Encode Output:** Veriyi gösterirken HTML entity'lere çevir (`<` → `&lt;`)
3. 🛡️ **CSP Headers:** Tarayıcıya hangi kaynakların güvenilir olduğunu söyle

Bu üçünü birlikte kullanırsan, XSS saldırısı neredeyse imkansız hale gelir.

```javascript
// Helmet.js for security headers
const helmet = require('helmet');
app.use(helmet());

// Content Security Policy
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", 'data:', 'https:']
  }
}));

// DOMPurify for HTML sanitization
const sanitizedHtml = DOMPurify.sanitize(userInput);
```

**CSRF Protection:**
```javascript
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

app.get('/form', csrfProtection, (req, res) => {
  res.render('form', { csrfToken: req.csrfToken() });
});

app.post('/submit', csrfProtection, (req, res) => {
  // Protected
});
```

**Rate Limiting:**

🛗 **Rate Limiting: Asansörün Maksimum Kapasitesi**

Rate limiting'i şöyle düşün: bir asansör var, maksimum 10 kişi alıyor. 50 kişi aynı anda binmek istese ne olur? Asansör BOZULUR veya kablo kopar. Rate limiting, API'nin "asansör kapasitesi"dir — herkes aynı anda giremez, sırayla ve SINIRLI sayıda.

**Rate Limiting Algoritmaları:**

| Algoritma | Nasıl Çalışır? | Kullanım Alanı |
|-----------|---------------|----------------|
| **Fixed Window** | Her 1 dakikada 100 istek. Dakika dolunca sıfırla. | Basit, ama pencere sınırında burst problemi var |
| **Sliding Window** | Son 1 dakikadaki istekleri say (kayan pencere). | Fixed Window'un gelişmişi, daha adil |
| **Token Bucket** | Kovada token var, her istek 1 token harcar. Tokenlar sabit hızda dolur. | AWS API Gateway bunu kullanır. Burst'e izin verir |
| **Leaky Bucket** | İstekler kovaya girer, sabit hızda işlenir. Taşarsa → reject. | Smooth rate, queue mantığı |

**Nereye Uygulanır?**
- 🌐 **API Gateway (Global):** Tüm API'ye genel limit. Nginx, Kong, AWS API Gateway seviyesinde.
- 🎯 **Application (Per-endpoint):** `/login` endpoint'ine 5 istek/dakika, `/search`'e 100 istek/dakika. Hassas endpoint'ler daha sıkı.
- 👤 **Per-user:** Her kullanıcı kendi limitine sahip. JWT'den user ID çıkar, ona göre say.

**DDoS vs Brute Force — Farklı Saldırılar, Farklı Limitler:**
- **DDoS (Distributed Denial of Service):** Binlerce makineden aynı anda istek. Amaç: sunucuyu ÇÖKERTMEK. → Global rate limit + WAF + CDN ile korunursun.
- **Brute Force:** Tek kaynaktan login denemesi. `admin` / `password123`, `admin` / `qwerty`, ... → Per-endpoint rate limit + account lockout ile korunursun.

Bu ikisi için AYNI strateji kullanmazsın. DDoS'a karşı IP-bazlı global limit, brute force'a karşı endpoint-bazlı sıkı limit gerekir.

📊 **Gerçek Dünya: GitHub API Rate Limiting**
GitHub API şöyle çalışır:
- 🔓 Kimliksiz (unauthenticated): **60 istek/saat** — sadece deneme amaçlı
- 🔑 Kimlikli (authenticated): **5.000 istek/saat** — ciddi kullanım
- 🏢 GitHub App: **15.000 istek/saat** — enterprise seviye

Response header'larında `X-RateLimit-Remaining: 4999` gibi bilgiler döner. Limit aşılınca? **`429 Too Many Requests`** status code'u döner. Bu code'u sen de uygulamalısın — `429` HTTP standardında "yavaşla dostum" demektir. `Retry-After` header'ı ile kaç saniye beklemesi gerektiğini de söyleyebilirsin.

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests',
  standardHeaders: true,
  legacyHeaders: false
});

app.use('/api/', limiter);

// Stricter for login
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true
});

app.post('/login', loginLimiter, loginHandler);
```

---

## 📊 Monitoring & Observability

### The Three Pillars

Observability'nin 3 sütunu vardır. Birlikte kullanıldığında production'daki herhangi bir sorunu ANA NEDENE kadar takip edebilirsin.

**Analoji:** Bir araba kaza yaptığında:
- **Logging** = Kaza raporu (ne oldu, ne zaman oldu, detaylar)
- **Metrics** = Araç gösterge paneli (hız, devir, yakıt, sıcaklık)
- **Tracing** = Kaza hızı kameranın KAYDII (olayın başından sonuna kadar ne oldu)

Bu üçü bir arada OLMAZSA production'da körsün. 🙈

#### 1. Logging

**Structured Logging neden önemli?**

`console.log('User login failed')` yazmak kolay. Ama prod'da binlerce log arasından bu satırı BUL! 🙄

**Structured logging** = log'u JSON formatında yaz. Böylece Elasticsearch / CloudWatch ile filtreleyebilirsin:
- `{"level": "error", "message": "Login failed", "userId": "123", "ip": "1.2.3.4", "reason": "invalid_password"}`
- Artık `userId:123 AND level:error` diye arayabilirsin!

**Log seviyeleri stratejisi:**
- `error`: Bir şey KIRILDI, müşteri etkileniyor → ALERT ver
- `warn`: Bir şey şüpheli ama çalışıyor → izle
- `info`: Normal iş akışı → "User created", "Order placed"
- `debug`: Geliştirici detayı → prod'da KAPALI tut (yoksa disk dolar 💥)
```javascript
// Structured logging with Winston
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'order-service' },
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

// Log with context
logger.info('Order created', {
  orderId: '12345',
  userId: 'user123',
  amount: 99.99,
  timestamp: Date.now()
});

// Log levels: error, warn, info, http, verbose, debug, silly
```

**Centralized Logging (ELK Stack):**
```yaml
# Elasticsearch + Logstash + Kibana
# Filebeat config
filebeat.inputs:
  - type: log
    paths:
      - /var/log/app/*.log
    json.keys_under_root: true

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
  index: "app-logs-%{+yyyy.MM.dd}"
```

**CloudWatch Logs:**
```javascript
const AWS = require('aws-sdk');
const cloudwatch = new AWS.CloudWatchLogs();

async function sendToCloudWatch(message) {
  await cloudwatch.putLogEvents({
    logGroupName: '/aws/lambda/my-function',
    logStreamName: '2024/01/15/[$LATEST]abc123',
    logEvents: [{
      message: JSON.stringify(message),
      timestamp: Date.now()
    }]
  }).promise();
}
```

#### 2. Metrics

Metrics nedir? Arabanızın gösterge panelini düşünün — hız göstergesi, yakıt seviyesi, devir (RPM) sayacı, motor sıcaklığı. Bu göstergelere bakmadan araba kullanmak, gözleriniz kapalı otobanda gitmek gibidir. İşte metrics de uygulamanız için aynı şeyi yapar: **"Sistemim şu an nasıl?"** sorusuna anlık cevap verir.

**Google SRE'nin Dört Altın Sinyali (Four Golden Signals):**

Google'ın Site Reliability Engineering kitabı, her servis için izlenmesi gereken dört temel metrik tanımlar:

1. **Latency (Gecikme):** İsteklerin ne kadar sürede cevaplanıyor? Hem başarılı hem başarısız isteklerin ayrı ayrı ölçülmesi lazım. 500ms ortalama güzel görünebilir ama p99'unuz 10 saniyeyse, her 100 kullanıcıdan biri çıldırıyor demektir.

2. **Traffic (Trafik):** Sisteme ne kadar talep geliyor? HTTP requests/second, mesaj kuyruğu throughput'u, aktif bağlantı sayısı. Bu metrik kapasite planlaması için hayati.

3. **Errors (Hatalar):** Başarısız isteklerin oranı. Sadece HTTP 5xx değil — yanlış sonuç dönen 200 OK'ler de "error" sayılmalı! Bir e-ticaret sitesinde yanlış fiyat gösteren 200 OK, 500'den daha tehlikelidir.

4. **Saturation (Doygunluk):** Kaynakların ne kadarı kullanılıyor? CPU %90'daysa, bir traffic spike geldiğinde çökersiniz. Disk %95 doluysa, yarın log yazamaz hale gelirsiniz.

**Prometheus Metrik Tipleri:**

Prometheus dünyasında dört metrik tipi vardır, her birinin farklı bir kullanım amacı var:

- **Counter (Sayaç):** Sadece YUKARI gider, asla azalmaz — tıpkı araba kilometresi gibi. 150.000 km'den 149.000 km'ye düşmez. Toplam istek sayısı, toplam hata sayısı, toplam işlenen byte gibi metrikler için kullanılır. Reset olduğunda (restart) Prometheus bunu algılar ve `rate()` fonksiyonu doğru hesaplar.

- **Gauge (Gösterge):** Hem YUKARI hem AŞAĞI gider — tıpkı hız göstergesi gibi. Şu an 120 km/h, biraz sonra 60 km/h. Aktif bağlantı sayısı, CPU kullanımı, kuyruk uzunluğu, sıcaklık gibi anlık değerler için kullanılır.

- **Histogram:** Değerlerin dağılımını ölçer — tıpkı bir yarışta tur sürelerini kaydetmek gibi. "Son 5 dakikada isteklerin %50'si 100ms'den, %90'ı 500ms'den, %99'u 2s'den kısa sürdü" diyebilirsiniz. Bucket'lara böler: 0.1s, 0.5s, 1s, 2s, 5s gibi. Latency ölçümü için en yaygın tercih budur.

- **Summary:** Histogram'a benzer ama percentile'ları client tarafında önceden hesaplar. Avantajı: doğrudan p50, p90, p99 verir. Dezavantajı: birden fazla instance'ın summary'lerini birleştiremezsiniz (aggregation impossible). Bu yüzden çoğu durumda Histogram tercih edilir.

**⚠️ Cardinality Uyarısı — Metrik Patlaması:**

Her label kombinasyonu yeni bir time series oluşturur. Eğer `method` (5 değer) × `path` (1000 endpoint) × `status` (20 değer) = **100.000 time series** yaratırsınız. User ID'yi label olarak koymayı aklınızdan bile geçirmeyin — 1 milyon kullanıcı = 1 milyon time series = Prometheus sunucunuz patlar, RAM faturanız gözyaşı olur. Kural: **label değerleri sınırlı ve öngörülebilir olmalı.**

**PromQL Temelleri:**

- `rate(http_requests_total[5m])`: Son 5 dakikadaki istek hızı (req/s). Counter'lar için MUTLAKA rate kullanılmalı.
- `increase(http_requests_total[1h])`: Son 1 saatte kaç istek geldi? (rate × süre)
- `histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))`: p99 latency hesaplama.
- `sum by (status) (rate(http_requests_total[5m]))`: Status code'a göre gruplandırılmış istek hızı.

**Grafana Dashboards:**

Prometheus verileri çiğ haliyle okunmaz. Grafana, bu verileri güzel grafiklere, tablolara ve alarm panellerine dönüştürür. Her ekibin bir "Golden Dashboard"u olmalı — dört altın sinyal tek bakışta görülmeli. Alert kuralları da Grafana üzerinden tanımlanabilir: "p99 latency 2 saniyeyi geçerse Slack'e mesaj at."

**Gerçek Dünyadan:**

"Bizim p99 latency 2 saniye" dendiğinde ne kastedilir? Her 100 istekten 99'u 2 saniyeden kısa sürede cevaplanıyor, ama en yavaş %1'lik dilim 2 saniyenin üstünde. Bu o kadar da masum değil — günde 1 milyon isteğiniz varsa, 10.000 kullanıcı 2+ saniye bekliyor demektir. O yüzden sadece ortalamaya bakıp "her şey güzel" demek, evin yandığını görmezden gelmek gibidir.

```javascript
// Prometheus metrics
const prometheus = require('prom-client');

// Counter
const httpRequestsTotal = new prometheus.Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'path', 'status']
});

// Histogram (latency)
const httpRequestDuration = new prometheus.Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request latency',
  labelNames: ['method', 'path'],
  buckets: [0.1, 0.5, 1, 2, 5]
});

// Gauge (current value)
const activeConnections = new prometheus.Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    
    httpRequestsTotal.labels(req.method, req.path, res.statusCode).inc();
    httpRequestDuration.labels(req.method, req.path).observe(duration);
  });
  
  next();
});

// Metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', prometheus.register.contentType);
  res.end(await prometheus.register.metrics());
});
```

**CloudWatch Metrics:**
```javascript
const cloudwatch = new AWS.CloudWatch();

await cloudwatch.putMetricData({
  Namespace: 'MyApp/Orders',
  MetricData: [{
    MetricName: 'OrdersCreated',
    Value: 1,
    Unit: 'Count',
    Timestamp: new Date(),
    Dimensions: [{
      Name: 'Environment',
      Value: 'Production'
    }]
  }]
}).promise();
```

#### 3. Tracing

Distributed tracing nedir? Şu senaryoyu hayal edin: Bir kargo gönderiyorsunuz. Kargo, gönderici → yerel depo → bölgesel aktarma merkezi → şehirlerarası taşıma → hedef bölge deposu → teslimat aracı → alıcı yolculuğunu takip ediyor. Her durakta bir barkod okutma işlemi var ve siz kargonuzun nerede olduğunu, hangi aşamada ne kadar beklediğini tek bir takip numarasıyla görebiliyorsunuz. İşte distributed tracing de **bir HTTP isteğinin microservice'ler arasındaki yolculuğunu** aynı şekilde takip eder.

**Neden Loglama Tek Başına Yetmez?**

Monolitik bir uygulamada hata ayıklamak kolaydır — tüm loglar tek yerde, tek process. Ama microservice mimarisinde bir kullanıcı isteği 10-15 farklı servise temas edebilir: API Gateway → Auth Service → User Service → Order Service → Payment Service → Notification Service → ... Bir istekte yavaşlık var, ama hangisinde? Her servisin loglarını tek tek açıp timestamp'leri eşleştirmeye mi çalışacaksınız? 50 instance varsa? Samanlıkta iğne aramak bile daha kolay.

Distributed tracing olmadan microservice debugging yapmak, gözleri bağlı birinin fil tarif etmesi gibidir — herkes kendi gördüğü parçayı söyler ama bütünü kimse göremez.

**Temel Kavramlar — Trace, Span, SpanContext:**

- **Trace:** Bir isteğin baştan sona tüm yolculuğu. Tek bir trace, birçok span'den oluşur. Kargo analojisinde: gönderiden teslimata kadar olan tüm süreç.
- **Span:** Trace içindeki tek bir operasyon birimi. "User Service'te veritabanı sorgusu" veya "Payment Service'e HTTP çağrısı" gibi. Her span'in başlangıç zamanı, süresi, durumu ve metadata'sı var. Span'ler parent-child ilişkisiyle ağaç yapısı oluşturur.
- **SpanContext:** Span'ın servisler arası taşınan kimlik bilgisi — Trace ID + Span ID + trace flags. HTTP header'larında (genellikle `traceparent` veya `X-B3-TraceId`) propagate edilir.

**Trace ID Propagation — Sihir Burada:**

Bir istek ilk servise geldiğinde benzersiz bir Trace ID üretilir (örn: `4bf92f3577b34da6a3ce929d0e0e4736`). Bu ID, her downstream çağrıda HTTP header olarak iletilir. Her servis kendi span'ini oluşturur ama hepsinde aynı Trace ID bulunur. Böylece tüm span'ler tek bir trace altında birleşir ve Jaeger/X-Ray'de güzel bir waterfall (şelale) grafik olarak görülür.

**OpenTelemetry — Herkesin Benimsediği Standart:**

Eskiden her vendor kendi tracing SDK'sını dayatırdı — Jaeger client, Zipkin client, X-Ray SDK, Datadog agent... Uygulamanız vendor'a kilitlenirdi. OpenTelemetry (OTel), CNCF tarafından geliştirilen **vendor-neutral** bir standarttır: traces, metrics ve logs için tek bir API ve SDK. Bir kere instrument edin, istediğiniz backend'e (Jaeger, Zipkin, X-Ray, Datadog, Honeycomb) gönderin. 2024 itibarıyla OTel, production'da en çok benimsenen observability standardıdır.

**Jaeger vs Zipkin vs AWS X-Ray:**

| Özellik | Jaeger | Zipkin | AWS X-Ray |
|---------|--------|--------|-----------|
| Geliştirici | Uber (CNCF) | Twitter | AWS |
| Deployment | Self-hosted / K8s | Self-hosted | Managed (serverless) |
| Ölçek | Milyarlarca span/gün | Orta ölçek | AWS ekosistemine entegre |
| Storage | Cassandra, ES, Kafka | MySQL, Cassandra, ES | AWS managed |
| OTel Desteği | Native | Native | SDK + OTel collector |

- **Jaeger:** Uber tarafından geliştirildi, günde **milyarlarca span** işler. Kubernetes-native, Cassandra veya Elasticsearch backend kullanır. Open-source dünyasının favorisi.
- **Zipkin:** Twitter'ın geliştirdiği, daha eski ve hafif. Küçük-orta ölçek projeler için yeterli.
- **AWS X-Ray:** AWS servisleri (Lambda, ECS, API Gateway) ile sıfır konfigürasyon entegrasyon. Managed olduğu için operasyonel yük minimal, ama AWS dışına çıkamazsınız.

**Sampling Stratejileri — Her Şeyi Trace Edemezsiniz:**

Günde 100 milyon istek alan bir sistemde %100 tracing yapmak hem storage hem network açısından imkansız ve gereksizdir. Sampling stratejileri devreye girer:

- **Probabilistic (Olasılıksal):** İsteklerin %1'ini veya %5'ini trace et. Basit ve etkili. Çoğu production sistemde %1 sampling yeterlidir.
- **Rate Limiting:** Saniyede maksimum N trace. Ani traffic spike'larında storage'ı korur.
- **Adaptive / Dynamic:** Hatalı veya yavaş istekleri %100 trace et, başarılı olanları %0.1. En akıllı strateji — problem olan istekleri asla kaçırmazsınız.
- **Tail-based:** Trace tamamlandıktan sonra karar ver (örn: toplam süre > 5s ise sakla). Dezavantaj: tüm span'leri geçici olarak buffer'da tutmak gerekir.

**Gerçek Dünyadan:**

Uber'in Jaeger'ı, production'da günde **milyarlarca span** toplar. Google'ın Dapper paper'ı (2010) tüm distributed tracing dünyasının temelini attı. Netflix, her isteği 200+ microservice'ten geçirirken tracing olmadan 5 dakikada bug bulamazdı — tracing sayesinde "bu isteğin %40'ı Redis cache miss'ten dolayı yavaş" gibi insight'lar saniyeler içinde ortaya çıkar.

**AWS X-Ray:**
```javascript
const AWSXRay = require('aws-xray-sdk-core');
const AWS = AWSXRay.captureAWS(require('aws-sdk'));
const http = AWSXRay.captureHTTPs(require('http'));

// Express middleware
app.use(AWSXRay.express.openSegment('MyApp'));

app.get('/users/:id', async (req, res) => {
  // Custom subsegment
  const segment = AWSXRay.getSegment();
  const subsegment = segment.addNewSubsegment('fetchUser');
  
  try {
    const user = await User.findById(req.params.id);
    subsegment.addAnnotation('userId', req.params.id);
    subsegment.addMetadata('user', user);
    res.json(user);
  } finally {
    subsegment.close();
  }
});

app.use(AWSXRay.express.closeSegment());
```

### Alerting

**Grafana Alerts:**
```yaml
# Alert rule
groups:
  - name: api_alerts
    interval: 30s
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value }} req/s"
          
      - alert: HighLatency
        expr: histogram_quantile(0.95, http_request_duration_seconds_bucket) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency detected"
```

**CloudWatch Alarms:**
```javascript
await cloudwatch.putMetricAlarm({
  AlarmName: 'HighCPUUtilization',
  ComparisonOperator: 'GreaterThanThreshold',
  EvaluationPeriods: 2,
  MetricName: 'CPUUtilization',
  Namespace: 'AWS/EC2',
  Period: 300,
  Statistic: 'Average',
  Threshold: 80.0,
  ActionsEnabled: true,
  AlarmActions: ['arn:aws:sns:us-east-1:123456789012:alerts'],
  Dimensions: [{
    Name: 'InstanceId',
    Value: 'i-1234567890abcdef0'
  }]
}).promise();
```

### APM (Application Performance Monitoring)

**New Relic, Datadog, Dynatrace:**
- Automatic instrumentation
- Transaction tracing
- Error tracking
- Infrastructure monitoring
- Real user monitoring (RUM)

---

## 🚢 Deployment Strategies & GitOps

### Deployment Strategies

Bir deployment strategy seçmek, **açık bir restoranda tadilat yapmaya** benzer. Müşteriler hâlâ yemek yiyor, garsonlar servis yapıyor — ama siz mutfağı yeniliyorsunuz. Eğer yanlış strateji seçerseniz, müşterinin tabağına moloz düşer. Doğru strateji seçerseniz, müşteri tadilatın farkına bile varmaz. İşte modern yazılım dünyasında "zero downtime deployment" tam olarak budur: **kullanıcı hiçbir şey hissetmeden** sisteminizi güncellemek.

Eski günlerde "Bakım modu — lütfen daha sonra tekrar deneyin" sayfaları normaldi. 2026'da böyle bir sayfa göstermek, müşteriye "kapıyı kendin aç" demek kadar absürt. Kullanıcılar anlık erişim bekler, tolerance sıfırdır. Getir, Netflix, Amazon günde **binlerce deploy** yapıyor — ve kullanıcılar bunun farkında bile değil.

Deployment stratejilerini bir **risk spektrumu** olarak düşünün:

```
Risk & Complexity Spektrumu:

Rolling (Basit & Güvenli)     ──────────────────────────> A/B Testing (Akıllı & Kompleks)
  │                                                          │
  ├── Rolling:     Pod'ları teker teker güncelle              │
  ├── Blue-Green:  İki environment, anında geçiş              │
  ├── Canary:      %5'e deploy, izle, yavaşça arttır          │
  └── A/B Testing: Farklı kullanıcılara farklı versiyonlar    │
                                                              │
  Düşük maliyet, az kontrol  ◄──────────────────────►  Yüksek maliyet, tam kontrol
```

Hangi stratejiyi ne zaman kullanacağınız, uygulamanızın kritiklik seviyesine, takımınızın olgunluğuna ve bütçenize bağlıdır. Bir startup için Rolling Deployment yeterli olabilirken, bir fintech uygulaması için Canary Deployment olmazsa olmazdır. Haydi her birini detaylıca inceleyelim.

#### 1. Rolling Deployment
**Nedir:**
- Pod'ları kademeli olarak güncelleme
- Her seferinde birkaç pod update edilir
- Zero downtime

```yaml
# Kubernetes rolling update
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2        # Toplam pod sayısını 2 fazla yapabilir (12)
      maxUnavailable: 1  # En fazla 1 pod unavailable olabilir
```

**Avantajlar:**
✓ Zero downtime
✓ Otomatik rollback (readiness check fail ederse)
✓ Resource efficient

**Dezavantajlar:**
✗ Yavaş deployment
✗ İki version aynı anda çalışır (database migration problemleri)

**Ne Zaman Kullanılır:**
- Stateless applications
- Backward-compatible changes
- Default strategy

#### 2. Blue-Green Deployment

Blue-Green Deployment'ı anlamak için şu sahneyi hayal edin: Bir tiyatro var ve sahne arkasında **iki identik sahne** kurulu. Birinde (Blue) şu anki oyun oynanıyor, diğerinde (Green) yeni oyun prova ediliyor. Prova bitince, perde kapanır, sahne döner ve seyirci yeni oyunu görür. Eski sahne? Hâlâ orada duruyor — eğer yeni oyun beğenilmezse, sahne geri döner ve eski oyun devam eder. **5 saniyede rollback.** İşte bu yüzden Blue-Green, rollback konusunda en güvenli stratejilerden biridir.

Ama her güzelliğin bir bedeli var: **2x infrastructure maliyeti**. İki tam environment'ı aynı anda ayakta tutuyorsunuz. AWS faturanız geçici olarak ikiye katlanır. Küçük servisler için bu tolere edilebilir, ama 50 microservice'i Blue-Green yaparsanız CFO'nuz kapınızı çalar.

Ve en kritik zorluk: **database migration'ları.** Blue v1.0 şeması ile çalışırken, Green v2.0 şemasına ihtiyaç duyabilir. Ama geçiş anında her iki versiyon da **aynı veritabanına** bağlı! Bu yüzden Blue-Green yaparken DB migration'larınız mutlaka **backward compatible** olmalı. Yeni bir kolon ekleyebilirsiniz ama kolon silmek? Önce Blue'yu kapatana kadar beklemeniz lazım. Bu kısıtlama, deployment pipeline'ınızı doğrudan etkiler.

**Nedir:**
- İki identic environment (Blue = live, Green = new)
- Green'e deploy -> test -> traffic switch -> Blue'yu kaldır
- Instant rollback (traffic'i Blue'ya geri çevir)
- DNS veya service selector flip ile anında geçiş — load balancer seviyesinde yapılır

```yaml
# Service selector değiştirerek traffic switching
# Blue deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    metadata:
      labels:
        app: myapp
        version: blue
    spec:
      containers:
      - name: app
        image: myapp:v1.0

---
# Green deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: green
  template:
    metadata:
      labels:
        app: myapp
        version: green
    spec:
      containers:
      - name: app
        image: myapp:v2.0

---
# Service (traffic routing)
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
    version: blue  # Change to 'green' to switch traffic
  ports:
  - port: 80
```

**Implementation with Terraform:**
```hcl
# Blue environment
resource "aws_autoscaling_group" "blue" {
  name = "app-blue"
  launch_configuration = aws_launch_configuration.blue.id
  min_size = 3
  max_size = 10
  
  tag {
    key = "Environment"
    value = "blue"
  }
}

# Green environment
resource "aws_autoscaling_group" "green" {
  name = "app-green"
  launch_configuration = aws_launch_configuration.green.id
  min_size = 3
  max_size = 10
  
  tag {
    key = "Environment"
    value = "green"
  }
}

# Load balancer - switch target group
resource "aws_lb_target_group" "active" {
  name = "app-active"
  # Point to blue or green
  # Manually or via automation
}
```

**Avantajlar:**
✓ Instant rollback
✓ Test tam production environment'ta
✓ Zero downtime
✓ Risk azaltır

**Dezavantajlar:**
✗ 2x resources gerekir
✗ Database migration zor
✗ Daha kompleks

**Ne Zaman Kullanılır:**
- Critical applications
- Major version changes
- When you need instant rollback capability

#### 3. Canary Deployment

"Canary" ismi nereden geliyor biliyor musunuz? 19. yüzyılda, madenciler yeraltına inerken yanlarında bir **kanarya kuşu** götürürdü. Neden? Çünkü kanarya zehirli gazlara karşı insanlardan çok daha hassastır. Eğer kanarya ölürse, madenciler hemen çıkışa koşardı. İşte Canary Deployment'ta aynı mantık: yeni versiyonunuzu önce **küçük bir kullanıcı grubuna** deploy ediyorsunuz — onlar sizin kanaryalarınız. Eğer hata çıkarsa, sadece %5 etkilenir, %95 eski versiyonda güven içinde kalmaya devam eder.

Canary Deployment, deployment stratejileri arasında **en akıllı risk yönetimi**ni sunar. Şöyle çalışır:

```
Canary Aşamaları:

1. Deploy v2 → %5 traffic canary'ye  → 30 dk izle → Error rate OK mi?
2. Başarılı → %25 traffic canary'ye  → 1 saat izle → Latency OK mi?
3. Başarılı → %50 traffic canary'ye  → 2 saat izle → Business metrics OK mi?
4. Başarılı → %100 traffic canary'ye → Deployment tamamlandı! 🎉

❌ Herhangi bir aşamada problem → Otomatik rollback → Canary öldü ama production kurtuldu!
```

İzlenmesi gereken **key metrics** şunlardır:
- **Error Rate:** 5xx hataları artıyor mu? Canary versiyonunda error rate %1'i geçerse alarm.
- **Latency:** P99 response time yükseldi mi? Canary'de 500ms üzerine çıkarsa dikkat.
- **Business Metrics:** Conversion rate, order completion rate düştü mü? Bu en sinsi olandır — teknik olarak her şey çalışıyor ama kullanıcılar sipariş tamamlayamıyor.

Manuel canary yapmak mümkün ama **Flagger** ve **Argo Rollouts** gibi araçlar bu süreci tamamen otomatize eder. Metrics kötüyse otomatik rollback, iyiyse otomatik promotion — siz uyurken deploy olur.

> 🌍 **Gerçek Dünya:** Google, yeni bir versiyonu önce sunucularının sadece **%1'ine** deploy eder ve **saatlerce** izler. Bir problemin 100 milyon kullanıcıyı etkilemesi yerine, 1 milyon kullanıcıda yakalanmasını tercih ederler. Facebook da benzer şekilde "dark launching" yapar — yeni feature'ı açmadan önce production'da sessizce çalıştırıp performance etkisini ölçer.

**Nedir:**
- Yeni version'ı küçük bir kullanıcı grubuna deploy et
- Problemler yoksa kademeli olarak arttır
- Problem varsa rollback

```yaml
# Istio VirtualService ile canary
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: app-vs
spec:
  hosts:
  - app.example.com
  http:
  - match:
    - headers:
        user-type:
          exact: beta-tester
    route:
    - destination:
        host: app
        subset: v2
  - route:
    - destination:
        host: app
        subset: v1
      weight: 90  # %90 traffic to v1
    - destination:
        host: app
        subset: v2
      weight: 10  # %10 traffic to v2 (canary)
```

**Progressive Canary:**
```
Stage 1: 5% traffic  -> Monitor 30 min
Stage 2: 25% traffic -> Monitor 1 hour
Stage 3: 50% traffic -> Monitor 2 hours
Stage 4: 100% traffic -> Deployment complete
```

**Automated Canary with Flagger:**
```yaml
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: app-canary
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  service:
    port: 8080
  analysis:
    interval: 1m
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
    - name: request-duration
      thresholdRange:
        max: 500
    webhooks:
    - name: load-test
      url: http://loadtester.test/
      timeout: 5s
```

**Avantajlar:**
✓ Risk minimize
✓ Real user feedback
✓ Gradual rollout
✓ A/B testing yapılabilir

**Dezavantajlar:**
✗ Kompleks setup
✗ Monitoring gerekir
✗ Yavaş deployment

**Ne Zaman Kullanılır:**
- High-risk changes
- User-facing features
- Performance testing

#### 4. Feature Flags (Feature Toggles)
**Nedir:**
- Code'da feature'ları runtime'da açıp kapatabilme
- Deploy code != Release feature
- Rollout control

```javascript
// LaunchDarkly, Unleash, or custom implementation
const featureFlags = require('./featureFlags');

app.post('/orders', async (req, res) => {
  // Check feature flag
  const useNewCheckout = await featureFlags.isEnabled(
    'new-checkout-flow',
    { userId: req.user.id }
  );
  
  if (useNewCheckout) {
    return newCheckoutService.process(req.body);
  } else {
    return oldCheckoutService.process(req.body);
  }
});

// Feature flag targeting
{
  "new-checkout-flow": {
    "enabled": true,
    "rules": [
      {
        "percentage": 10,  // 10% of users
        "attributes": {
          "country": "US",
          "plan": "premium"
        }
      }
    ]
  }
}
```

**Custom Feature Flag Service:**
```javascript
class FeatureFlagService {
  constructor(redisClient) {
    this.redis = redisClient;
  }
  
  async isEnabled(flagName, context = {}) {
    const config = await this.redis.get(`flag:${flagName}`);
    if (!config) return false;
    
    const flag = JSON.parse(config);
    if (!flag.enabled) return false;
    
    // Check targeting rules
    for (const rule of flag.rules || []) {
      if (this.matchesRule(rule, context)) {
        // Percentage rollout
        if (rule.percentage) {
          const hash = this.hashUserId(context.userId);
          return hash < rule.percentage;
        }
        return true;
      }
    }
    
    return false;
  }
  
  matchesRule(rule, context) {
    for (const [key, value] of Object.entries(rule.attributes || {})) {
      if (context[key] !== value) return false;
    }
    return true;
  }
  
  hashUserId(userId) {
    // Return 0-100 based on userId hash
    const hash = crypto.createHash('md5').update(userId).digest('hex');
    return parseInt(hash.substring(0, 8), 16) % 100;
  }
}

// Usage
const flags = new FeatureFlagService(redisClient);

// Admin API to manage flags
app.post('/admin/flags/:name', async (req, res) => {
  await redis.set(
    `flag:${req.params.name}`,
    JSON.stringify(req.body)
  );
  res.json({ success: true });
});
```

**Avantajlar:**
✓ Decouple deployment from release
✓ Instant enable/disable
✓ A/B testing
✓ Gradual rollout
✓ Kill switch

**Dezavantajlar:**
✗ Code complexity
✗ Technical debt (old flags)
✗ Testing combinations

**Best Practices:**
- Clean up old flags
- Short-lived flags
- Monitor flag usage
- Document flags

### GitOps

**Nedir:**
- Git repository as single source of truth
- Declarative infrastructure & applications
- Automated deployment via Git operations
- Pull-based deployment (vs push-based)

**Traditional CI/CD vs GitOps:**
```
Traditional:
CI/CD Pipeline pushes to cluster
├─ Build
├─ Test
└─ kubectl apply (push to K8s)

GitOps:
Git repo -> Operator pulls changes
├─ Git commit (update manifest)
├─ Operator detects change
└─ Operator syncs cluster state
```

#### ArgoCD

ArgoCD'yi anlamak için önce **GitOps** felsefesini kavramak gerekir. GitOps'un temel fikri şudur: **Git, altyapınızın tek gerçek kaynağıdır (Single Source of Truth).** Cluster'ınızda neyin çalışması gerektiği Git'te yazılıdır. Eğer biri `kubectl edit` ile production'da bir şey değiştirirse, ArgoCD bunu tespit eder ve **Git'teki hale geri döndürür.** Git'te ne yazıyorsa, cluster'da o olacak — ne eksik ne fazla.

GitOps'un dört temel prensibi vardır:
1. **Declarative:** Sistem durumu deklaratif olarak tanımlanır (YAML/Helm/Kustomize).
2. **Versioned:** Tüm değişiklikler Git'te versiyon kontrolündedir. Kim, ne zaman, neyi değiştirdi — hepsi `git log`'da.
3. **Automated:** Git'e push yapıldığında, değişiklikler otomatik olarak uygulanır.
4. **Reconciled:** Actual state ile desired state sürekli karşılaştırılır. Fark varsa otomatik düzeltilir (self-healing).

ArgoCD, bir Kubernetes cluster'ına kurulur ve belirttiğiniz **Git repository'sini izler.** Main branch'e bir değişiklik merge edildiğinde, ArgoCD bunu algılar ve cluster'ı günceller. Rollback mi istiyorsunuz? `git revert` yapın, ArgoCD gerisini halleder. Bu kadar basit. Artık production'a SSH ile girip `kubectl apply` yapmak yok — bunu yaparsanız ArgoCD zaten 3 dakika içinde geri alır. 😄

Peki neden GitOps?
- **Audit Trail:** "Production'da cuma gecesi kim ne değiştirdi?" sorusunun cevabı artık `git log`'da. Büyük bir outage'dan sonra blame game oynamak yerine commit history'e bakarsınız.
- **Easy Rollback:** Bad deploy? `git revert <commit>` ve bekle. ArgoCD 30 saniyede eski halini geri getirir.
- **PR-based Approvals:** Production deploy'u bir Pull Request'tir. Code review gibi infra review yaparsınız. Junior engineer PR açar, Senior approve eder, merge olunca deploy olur. Artık kimsenin "yanlışlıkla production'a deploy ettim" demesi mümkün değil.

> **ArgoCD vs Flux:** İkisi de GitOps operatörüdür. ArgoCD'nin güçlü bir **Web UI**'ı var — uygulamalarınızın sync durumu, health check'leri görsel olarak takip edebilirsiniz. Flux ise daha **lightweight ve composable**'dır, UI yoktur ama her bileşeni (source controller, kustomize controller, helm controller) bağımsız çalışır. Büyük organizasyonlar genelde ArgoCD'yi tercih eder (UI ve RBAC); küçük takımlar veya çok sayıda cluster yönetenler Flux'a yönelir. İkisini de bilmek avantajdır.

**Setup:**
```yaml
# Application definition
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/myapp-manifests
    targetRevision: main
    path: k8s/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true      # Delete resources not in Git
      selfHeal: true   # Revert manual changes
    syncOptions:
    - CreateNamespace=true
```

**Multi-environment with Kustomize:**
```
myapp-manifests/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
├── overlays/
│   ├── dev/
│   │   └── kustomization.yaml
│   ├── staging/
│   │   └── kustomization.yaml
│   └── production/
│       └── kustomization.yaml
```

```yaml
# base/kustomization.yaml
resources:
- deployment.yaml
- service.yaml

# overlays/production/kustomization.yaml
bases:
- ../../base

replicas:
- name: app
  count: 10

images:
- name: myapp
  newTag: v1.2.3

configMapGenerator:
- name: app-config
  literals:
  - ENVIRONMENT=production
```

**ArgoCD CLI:**
```bash
# Login
argocd login argocd.example.com

# Create app
argocd app create myapp \
  --repo https://github.com/myorg/myapp-manifests \
  --path k8s/production \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace production

# Sync app
argocd app sync myapp

# Get app status
argocd app get myapp

# Rollback
argocd app rollback myapp
```

#### Flux

**Installation:**
```bash
# Bootstrap Flux
flux bootstrap github \
  --owner=myorg \
  --repository=fleet-infra \
  --branch=main \
  --path=clusters/production \
  --personal
```

**GitRepository:**
```yaml
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: GitRepository
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/myorg/myapp-manifests
  ref:
    branch: main
```

**Kustomization:**
```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta1
kind: Kustomization
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 5m
  path: ./k8s/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: myapp
  healthChecks:
  - apiVersion: apps/v1
    kind: Deployment
    name: app
    namespace: production
  validation: client
```

**HelmRelease:**
```yaml
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: nginx
  namespace: flux-system
spec:
  interval: 5m
  chart:
    spec:
      chart: nginx
      version: '1.x.x'
      sourceRef:
        kind: HelmRepository
        name: bitnami
  values:
    replicaCount: 3
    service:
      type: LoadBalancer
```

### GitOps Workflow

```
Developer Workflow:
1. Developer commits code
2. CI pipeline builds Docker image
3. CI updates image tag in Git manifest repo
4. GitOps operator detects change
5. Operator deploys to cluster
6. Operator reports status

Ops Workflow:
1. Update manifest in Git (scale, config, etc.)
2. Create Pull Request
3. Review & approve
4. Merge to main
5. GitOps operator auto-deploys
6. Monitor rollout
```

**Automated Image Updates (Flux):**
```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageRepository
metadata:
  name: myapp
spec:
  image: myregistry/myapp
  interval: 1m

---
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImagePolicy
metadata:
  name: myapp
spec:
  imageRepositoryRef:
    name: myapp
  policy:
    semver:
      range: '>=1.0.0 <2.0.0'

---
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageUpdateAutomation
metadata:
  name: myapp
spec:
  interval: 1m
  sourceRef:
    kind: GitRepository
    name: myapp
  git:
    commit:
      author:
        name: fluxbot
        email: flux@example.com
  update:
    path: ./k8s
    strategy: Setters
```

### Progressive Delivery with Flagger

Progressive Delivery, CI/CD'nin **bir sonraki evrimi**dir. CI/CD size "kodu derle, test et, deploy et" der. Progressive Delivery ise şunu ekler: **"deploy et ama yavaşça, dikkatli ve geri alınabilir şekilde."** Yani deploy etmek ile release etmek arasına bir kontrol katmanı koyar.

**Flagger**, Weaveworks (Flux'un yaratıcıları) tarafından geliştirilen ve Kubernetes üzerinde **canary, blue-green ve A/B testing deployment'larını otomatize eden** bir araçtır. Flagger'ın güzelliği şudur: siz sadece Deployment'ınızı güncellersiniz, Flagger gerisini halleder.

Flagger şu service mesh ve ingress controller'larla çalışır:
- **Istio** (en yaygın kullanım)
- **Linkerd** (lightweight alternative)
- **NGINX Ingress Controller**
- **AWS App Mesh**
- **Gloo, Contour, Traefik**

Flagger nasıl çalışır?
1. Siz `myapp` Deployment'ınızı güncellersiniz (yeni image tag).
2. Flagger bunu tespit eder ve **iki deployment** oluşturur: `myapp-primary` (eski, stable) ve `myapp-canary` (yeni).
3. Traffic'i kademeli olarak canary'ye yönlendirir: %5 → %10 → %20 → %50.
4. Her adımda **metrics'leri kontrol eder** (Prometheus'tan request success rate, latency vb.).
5. Metrics iyi → bir sonraki adıma geç. Metrics kötü → **otomatik rollback**, canary kapatılır.
6. Tüm adımlar başarılı → canary promote edilir, primary güncellenir. 🎉

**Otomatik Rollback** Flagger'ın en değerli özelliğidir. Gece 3'te deploy yaptınız, error rate yükseldi — Flagger sizi uyandırmadan rollback yapar ve Slack'e bildirim atar. Sabah ofise geldiğinizde "Flagger gece bir rollback yaptı, şu metrics'ler bozulmuştu" mesajını görürsünüz. **İnsanları loop'tan çıkarmak**, progressive delivery'nin temel vaadlerinden biridir.

> 🌍 **Gerçek Dünya:** Weaveworks, Flux ile GitOps'u popularize ettikten sonra, "deploy ettik ama kontrollü bir şekilde release edemiyoruz" problemini çözmek için Flagger'ı geliştirdi. Bugün CNCF (Cloud Native Computing Foundation) projesi olan Flagger, production-grade workload'lar için endüstri standardı haline gelmiştir.

```yaml
# Canary deployment with Flagger + Istio/Linkerd
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: myapp
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  progressDeadlineSeconds: 60
  service:
    port: 8080
    targetPort: 8080
    gateways:
    - public-gateway
    hosts:
    - app.example.com
  analysis:
    interval: 1m
    threshold: 10
    maxWeight: 50
    stepWeight: 5
    metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
      interval: 1m
    - name: request-duration
      thresholdRange:
        max: 500
      interval: 1m
    webhooks:
    - name: acceptance-test
      type: pre-rollout
      url: http://flagger-loadtester.test/
      timeout: 30s
      metadata:
        type: bash
        cmd: "curl -s http://myapp-canary:8080/ | grep OK"
    - name: load-test
      url: http://flagger-loadtester.test/
      timeout: 5s
      metadata:
        cmd: "hey -z 1m -q 10 -c 2 http://myapp-canary.test:8080/"
    - name: notify
      type: post-rollout
      url: http://slack-bot/
      metadata:
        message: "Canary deployment successful"
```

---

## 🏗️ Architecture Patterns

### Design Patterns

Design pattern'ler, yazılım mühendisliğinin **yemek tarifleri**dir. Nasıl ki bir şef yeni bir yemek icat etmek yerine yüzyılların birikimiyle oluşmuş tarifleri kullanıyorsa, biz de tekrar tekrar karşılaştığımız problemlere **kanıtlanmış çözümler** uyguluyoruz. Tekerleği yeniden icat etmeye gerek yok — ama tekerleğin neden yuvarlak olduğunu anlamak şart.

1994 yılında Erich Gamma, Richard Helm, Ralph Johnson ve John Vlissides — nam-ı diğer **Gang of Four (GoF)** — "Design Patterns: Elements of Reusable Object-Oriented Software" kitabını yayınladı. Bu kitap, yazılım dünyasının Magna Carta'sı gibidir. GoF, pattern'leri üç kategoriye ayırdı:

- **Creational (Yaratımsal):** Objelerin nasıl oluşturulacağını ele alır. Factory, Singleton, Builder gibi. "Bir nesneyi `new` ile mi oluşturayım, yoksa daha akıllıca bir yol var mı?" sorusuna cevap verir.
- **Structural (Yapısal):** Objelerin nasıl birleştirileceğini/organize edileceğini ele alır. Adapter, Decorator, Facade gibi. "Bu iki uyumsuz sistemi nasıl konuşturayım?" sorusuna cevap verir.
- **Behavioral (Davranışsal):** Objeler arasındaki iletişimi ve sorumluluk dağılımını ele alır. Observer, Strategy, Command gibi. "Kim neyi ne zaman yapacak?" sorusuna cevap verir.

Backend geliştirmede pattern'ler neden bu kadar önemli?

1. **Maintainability (Bakım Kolaylığı):** Pattern'ler kodunuzu modüler ve değiştirilebilir kılar. 6 ay sonra geri döndüğünüzde "ben bunu niye böyle yazmışım?" demezsiniz.
2. **Testability (Test Edilebilirlik):** Doğru pattern kullanımı, mocklanabilir, izole edilebilir kod üretir. Unit test yazmak cehennemden cennet'e döner.
3. **Team Communication (Takım İletişimi):** "Burada Strategy pattern kullandım" dediğinizde, takımdaki herkes ne yaptığınızı anlar. Ortak bir dil oluşturur.
4. **Onboarding:** Yeni katılan bir geliştirici, tanıdık pattern'leri gördüğünde kodu çok daha hızlı kavrar.

> ⚠️ **Uyarı: Pattern saplantısına düşmeyin!** Bir pattern'i sırf "pattern kullanmış olayım" diye kullanmak, hastalığı olmayan birine ilaç vermek gibidir. Her pattern bir problemi çözer — eğer o problem yoksa, pattern de gereksizdir. Over-engineering, under-engineering kadar tehlikelidir. **YAGNI (You Aren't Gonna Need It)** prensibini unutmayın.

Bu bölümde ele alacağımız pattern'ler ve ne zaman işe yaradıkları:

- **Repository Pattern:** Veri erişimini soyutlamak istediğinizde. Database değişikliklerinde iş mantığına dokunmamak için.
- **Factory Pattern:** Obje oluşturma mantığı karmaşıklaştığında veya runtime'da hangi objenin oluşturulacağı belirleniyorsa.
- **Strategy Pattern:** Aynı işi farklı algoritmalarla yapmanız gerektiğinde. Algoritma seçimi runtime'da değişiyorsa.
- **Observer Pattern:** Bir olay gerçekleştiğinde birden fazla bileşeni haberdar etmeniz gerektiğinde. Event-driven mimarinin temeli.

#### 1. Repository Pattern

Repository Pattern'i anlamanın en kolay yolu **restoran analojisi**dir: Siz müşterisiniz (business logic), mutfak ise veritabanıdır (database). Garson (repository) arada duran kişidir — siz garsona "biftek istiyorum" dersiniz, garson mutfağa gider, şefle konuşur, yemeği getirir. Siz **asla** mutfağa girip şefle doğrudan konuşmazsınız. Neden? Çünkü mutfağın nasıl çalıştığı sizi ilgilendirmez. Şef değişse, fırın değişse, tarif değişse — siz hâlâ garsona "biftek istiyorum" dersiniz.

Repository Pattern, **business logic ile data access katmanını birbirinden ayırır**. Controller veya service katmanınız asla `SELECT * FROM users WHERE...` gibi sorguları doğrudan çalıştırmaz. Bunun yerine `userRepository.findById(42)` der ve gerisini repository halleder.

Bu neden önemli?

- **Testing:** Repository'yi mocklayarak, veritabanına hiç dokunmadan business logic'inizi test edebilirsiniz. `const mockRepo = { findById: () => fakeUser }` — işte bu kadar basit.
- **Database Değiştirme:** PostgreSQL'den MongoDB'ye geçmek mi istiyorsunuz? Sadece repository implementasyonunu değiştirin, 100 tane service dosyasına dokunmanıza gerek yok. Service katmanı repository interface'ini kullanmaya devam eder.
- **Separation of Concerns:** SQL sorguları tek bir yerde toplanır. Bir sorgu optimize etmeniz gerektiğinde nereye bakacağınızı bilirsiniz.

> ⚠️ **Anti-pattern Uyarısı:** "Her entity için bir repository" yaklaşımı yaygın ama tehlikeli olabilir. DDD (Domain-Driven Design) perspektifinden, repository'ler **aggregate root** başına oluşturulmalıdır. Örneğin `OrderRepository` olmalı ama `OrderItemRepository` olmamalı — OrderItem, Order aggregate'inin bir parçasıdır ve Order üzerinden erişilmelidir. Aksi halde repository'leriniz birbiriyle tutarsız veri üretebilir.

```javascript
// Data access abstraction
class UserRepository {
  constructor(database) {
    this.db = database;
  }
  
  async findById(id) {
    return await this.db.query('SELECT * FROM users WHERE id = $1', [id]);
  }
  
  async findByEmail(email) {
    return await this.db.query('SELECT * FROM users WHERE email = $1', [email]);
  }
  
  async create(userData) {
    const { name, email, password } = userData;
    return await this.db.query(
      'INSERT INTO users (name, email, password) VALUES ($1, $2, $3) RETURNING *',
      [name, email, password]
    );
  }
  
  async update(id, updates) {
    const fields = Object.keys(updates).map((key, i) => `${key} = $${i + 2}`).join(', ');
    return await this.db.query(
      `UPDATE users SET ${fields} WHERE id = $1 RETURNING *`,
      [id, ...Object.values(updates)]
    );
  }
}

// Usage
const userRepo = new UserRepository(database);
const user = await userRepo.findByEmail('user@example.com');
```

#### 2. Factory Pattern

Factory Pattern'i **araba fabrikası** gibi düşünün: Siz bayiye gidip "bir sedan istiyorum" dersiniz. Fabrika, hangi modelin üretileceğine, hangi motorun takılacağına, hangi rengin boyanacağına karar verir. Siz sadece "sedan" dediniz — gerisini fabrika halletti.

Yazılımda da aynı mantık geçerli: Obje oluşturma mantığı karmaşıklaştığında veya **runtime'da** hangi objenin oluşturulacağına karar verilmesi gerektiğinde Factory Pattern devreye girer. `new` operatörünü doğrudan kullanmak yerine, oluşturma sorumluluğunu bir factory'ye devredersiniz.

Ne zaman kullanmalı?

- Obje oluşturma birden fazla adım gerektiriyorsa (validation, default değerler, dependency injection)
- Hangi sınıfın instantiate edileceği runtime'da belirleniyor ise (config, user input, feature flag)
- `if/else` veya `switch` ile obje oluşturma kodu birden fazla yere dağılmışsa — hepsini tek bir Factory'de toplayın

Gerçek dünya örneği: Kullanıcı tercihine göre **email, SMS veya push notification** göndermeniz gerekiyor. Her yerde `if (preference === 'email') new EmailNotification()` yazmak yerine, tek bir `NotificationFactory.create(preference)` çağrısı yeterli.

```javascript
class NotificationFactory {
  static create(type) {
    switch (type) {
      case 'email':
        return new EmailNotification();
      case 'sms':
        return new SMSNotification();
      case 'push':
        return new PushNotification();
      default:
        throw new Error('Unknown notification type');
    }
  }
}

// Usage
const notification = NotificationFactory.create('email');
await notification.send(user, message);
```

#### 3. Strategy Pattern

Strategy Pattern'i **GPS navigasyon** gibi düşünün: Hedefiniz aynı — "ofise git". Ama nasıl gideceğiniz değişebilir: arabayla, yürüyerek, toplu taşımayla veya bisikletle. Her biri farklı bir **strateji**dir. Hedefe ulaşma amacı değişmez, ama algoritma (rota) değişir. Ve en güzel tarafı: stratejiyi **runtime'da** değiştirebilirsiniz — trafiğe bakıp "bugün metroyla gideyim" diyebilirsiniz.

Strategy Pattern, bir iş mantığındaki **değiştirilebilir algoritmaları** kapsüller. Bu pattern **Open/Closed Principle**'ın (SOLID'in O'su) mükemmel bir uygulamasıdır: mevcut kodu değiştirmeden yeni stratejiler ekleyebilirsiniz. Yeni bir ödeme yöntemi mi geldi? Mevcut koda dokunmadan `CryptoPayment` sınıfı ekler ve sisteme takarsınız.

Ne zaman kullanmalı?

- Aynı işi yapmanın birden fazla yolu varsa ve bunlar runtime'da seçilebiliyorsa
- Büyük `if/else` veya `switch` blokları oluşmaya başladıysa — bu Strategy Pattern'e ihtiyacınız olduğunun sinyalidir
- Algoritmayı kullanan kodun, algoritmanın detaylarından habersiz olması gerekiyorsa

Gerçek dünya: Ödeme işleme (credit card, PayPal, crypto), fiyatlandırma (normal, premium, enterprise), sıkıştırma (gzip, brotli, deflate) — hepsi Strategy Pattern adayıdır.

```javascript
// Payment strategies
class CreditCardPayment {
  async process(amount) {
    // Credit card processing logic
  }
}

class PayPalPayment {
  async process(amount) {
    // PayPal processing logic
  }
}

class CryptoPayment {
  async process(amount) {
    // Crypto processing logic
  }
}

// Context
class PaymentProcessor {
  constructor(strategy) {
    this.strategy = strategy;
  }
  
  async processPayment(amount) {
    return await this.strategy.process(amount);
  }
}

// Usage
const processor = new PaymentProcessor(new CreditCardPayment());
await processor.processPayment(99.99);
```

#### 4. Observer Pattern

Observer Pattern'i **YouTube aboneliği** gibi düşünün: Bir kanala abone olursunuz (subscribe). Kanal yeni video yüklediğinde (event), tüm abonelere otomatik bildirim gider (notify). Siz kanalı her 5 dakikada bir kontrol etmezsiniz — kanal size gelir. Bu **push-based** iletişimdir.

Observer Pattern, **event-driven architecture**'ın temel taşıdır. Bir nesne (Subject/Publisher) durumunu değiştirdiğinde, ona bağlı tüm nesneler (Observers/Subscribers) otomatik olarak haberdar edilir. Producer ve consumer birbirini tanımak zorunda değildir — bu **loose coupling**'in en güzel halidir.

**Pub/Sub vs Observer — ne fark var?**
- **Observer Pattern:** Subject, observer'larını doğrudan bilir ve doğrudan çağırır. `subject.notify()` → observer'ların `update()` metodu çalışır.
- **Pub/Sub:** Arada bir **message broker/event bus** vardır. Publisher, subscriber'ları bilmez. Mesajı broker'a atar, broker ilgili subscriber'lara iletir. Daha decoupled, daha scalable.

🎯 **Node.js'te built-in Observer:** Node.js'in `EventEmitter` sınıfı, Observer Pattern'in doğrudan implementasyonudur! `emitter.on('event', callback)` — zaten her gün kullanıyorsunuz, sadece adını bilmiyordunuz.

Ne zaman kullanmalı?
- Bir olay gerçekleştiğinde birden fazla **bağımsız** işlem tetiklenmesi gerektiğinde
- Producer'ın consumer'ları bilmesini istemediğinizde (decoupling)
- Yeni consumer'lar eklendiğinde mevcut kodun değişmemesi gerektiğinde

Gerçek dünya: Sipariş oluşturuldu → email gönder, stok güncelle, depoya bildir, analytics'e kaydet — hepsi **bağımsız** olarak, birbirini beklemeden çalışır. Birinin hata vermesi diğerlerini etkilemez.

```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }
  
  on(event, callback) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(callback);
  }
  
  emit(event, data) {
    if (this.events[event]) {
      this.events[event].forEach(callback => callback(data));
    }
  }
}

// Usage
const orderEvents = new EventEmitter();

orderEvents.on('orderCreated', (order) => {
  console.log('Send confirmation email');
});

orderEvents.on('orderCreated', (order) => {
  console.log('Update inventory');
});

orderEvents.emit('orderCreated', { orderId: '123', total: 99.99 });
```

### Architectural Patterns

#### 1. Layered Architecture
```
┌─────────────────────────┐
│   Presentation Layer    │  (Controllers, Routes)
├─────────────────────────┤
│    Business Logic       │  (Services, Use Cases)
├─────────────────────────┤
│    Data Access Layer    │  (Repositories, ORM)
├─────────────────────────┤
│       Database          │
└─────────────────────────┘
```

```javascript
// Controllers (Presentation)
class OrderController {
  constructor(orderService) {
    this.orderService = orderService;
  }
  
  async createOrder(req, res) {
    try {
      const order = await this.orderService.create(req.body);
      res.json(order);
    } catch (error) {
      res.status(400).json({ error: error.message });
    }
  }
}

// Services (Business Logic)
class OrderService {
  constructor(orderRepo, inventoryService, paymentService) {
    this.orderRepo = orderRepo;
    this.inventoryService = inventoryService;
    this.paymentService = paymentService;
  }
  
  async create(orderData) {
    // Business logic
    await this.inventoryService.checkAvailability(orderData.items);
    const order = await this.orderRepo.create(orderData);
    await this.paymentService.processPayment(order);
    return order;
  }
}

// Repository (Data Access)
class OrderRepository {
  async create(orderData) {
    return await Order.create(orderData);
  }
}
```

#### 2. Hexagonal Architecture (Ports & Adapters)

Hexagonal Architecture'ı anlamanın en kolay yolu **USB port** analojisidir: Laptopunuzun USB portuna mouse takabilirsiniz, klavye takabilirsiniz, harici disk takabilirsiniz. Laptop, neyin takıldığını **umursamaz** — USB interface'ini implemente eden her şeyi kabul eder. İşte Hexagonal Architecture'da business logic (laptop) ile dış dünya (USB cihazlar) arasındaki ilişki tam olarak budur.

Alistair Cockburn tarafından 2005'te ortaya atılan bu mimari, bir temel ilkeye dayanır: **Business logic, dış dünyanın detaylarını bilmemelidir.** Uygulamanız, veritabanının PostgreSQL mi MongoDB mi olduğunu, iletişimin HTTP mi gRPC mi olduğunu, mesajlaşmanın RabbitMQ mu Kafka mı olduğunu bilmemeli. Business logic saf ve bağımsız kalmalıdır.

Bunu nasıl başarıyoruz?

- **Ports (Arayüzler):** Uygulamanın dış dünyayla iletişim kurmak için tanımladığı **interface**'lerdir. "Benim bir şeyleri kaydetme yeteneğine ihtiyacım var" diyen bir port gibi. Port, **ne** yapılacağını tanımlar, **nasıl** yapılacağını tanımlamaz.
- **Adapters (Uygulamalar):** Port'ları gerçekleyen somut implementasyonlardır. `PostgresOrderRepository`, `MongoOrderRepository`, `InMemoryOrderRepository` — hepsi aynı port'un (interface'in) farklı adapter'larıdır. **Nasıl** yapılacağını belirler.

Testing'de muazzam fayda sağlar: Production'da `PostgresAdapter` kullanırken, testlerde `InMemoryAdapter` takarsınız. Veritabanına hiç dokunmadan tüm business logic'i test edersiniz. Docker, migration, seed data — hiçbirine gerek yok.

> 🎯 **Netflix**, hexagonal architecture'ı yaygın olarak kullanır. Microservice'lerinin core domain logic'i herhangi bir framework'e veya infrastructure'a bağımlı değildir.

> 💡 **Sık karıştırılan konu:** Hexagonal Architecture, **Clean Architecture** (Uncle Bob) ve **Onion Architecture** (Jeffrey Palermo) ile aynı **temel prensibe** dayanır — hepsi "dependency'ler dışarıdan içeriye doğru akar, iç katman dış katmanı bilmez" der. Farklı isimlendirme ve katman sayıları vardır, ama ruh aynıdır. Hexagonal = Ports & Adapters, Clean = Use Cases & Boundaries, Onion = Layers. Ama üçünün de kalbi: **"Business logic'i koru, dış dünyayı soyutla."**

```javascript
// Domain (Core business logic)
class Order {
  constructor(items, userId) {
    this.items = items;
    this.userId = userId;
    this.status = 'PENDING';
  }
  
  calculateTotal() {
    return this.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  }
  
  confirm() {
    if (this.status !== 'PENDING') {
      throw new Error('Cannot confirm order');
    }
    this.status = 'CONFIRMED';
  }
}

// Port (Interface)
class OrderRepository {
  async save(order) {
    throw new Error('Not implemented');
  }
}

// Adapter (Implementation)
class PostgresOrderRepository extends OrderRepository {
  async save(order) {
    return await db.query('INSERT INTO orders ...', order);
  }
}

class MongoOrderRepository extends OrderRepository {
  async save(order) {
    return await Order.create(order);
  }
}
```

#### 3. CQRS (Command Query Responsibility Segregation)

CQRS'i **kütüphane** gibi düşünün: Bir tane "ödünç alma masası" (write/command) ve ayrı bir "arama/katalog terminali" (read/query) var. İkisi farklı işler yapar, farklı optimize edilmiştir. Ödünç alma masasında sıra bekliyorsunuz çünkü her işlem dikkatli kaydedilmeli. Ama katalog terminalinde anında arama yapabilirsiniz çünkü sadece okumaya optimize edilmiş.

CQRS, **okuma (query) ve yazma (command) operasyonlarını tamamen ayrı modellere böler**. Neden? Çünkü çoğu sistemde operasyonların **%90'ı okumadır**. Bir e-ticaret sitesinde ürün sayfası milyonlarca kez görüntülenir, ama ürün bilgisi günde belki 10 kez güncellenir. Bu iki işlemi aynı model ve aynı veritabanıyla yapmak, ikisini de suboptimal kılar.

Ayrı read/write veritabanları kullanabilirsiniz:
- **Write DB (PostgreSQL — normalized):** Veri tutarlılığı ve ACID garantisi için optimize edilmiş. Ürün, stok, fiyat ayrı tablolarda.
- **Read DB (MongoDB/Elasticsearch — denormalized):** Hızlı okuma için optimize edilmiş. Ürün bilgisi, stok, fiyat, yorumlar tek bir dokümanda — JOIN'e gerek yok.

Write model bir değişiklik yaptığında, bir **event bus** (Kafka, RabbitMQ) aracılığıyla read model'e "hey, veri değişti, kendini güncelle" mesajı gönderir. Bu **eventual consistency** yaratır — write'dan sonra read model'in güncellenmesi birkaç milisaniye sürebilir.

> ⚠️ **Complexity Warning:** CQRS **ciddi karmaşıklık** ekler. İki ayrı model, event bus, eventual consistency, data synchronization... Basit bir CRUD uygulaması için CQRS kullanmak, bir çiviyi çekiçle değil de buldozerle çakmak gibidir. CQRS'i **yalnızca** read ve write ihtiyaçlarının gerçekten çok farklı olduğu durumlarda kullanın.

Gerçek dünya: E-ticaret ürün kataloğu (nadiren yazılır, günde milyonlarca okunur), sosyal medya feed'i (write: post paylaş, read: timeline'ı göster — tamamen farklı veri şekilleri), raporlama sistemleri.

```javascript
// Commands (Write)
class CreateOrderCommand {
  constructor(userId, items) {
    this.userId = userId;
    this.items = items;
  }
}

class CreateOrderHandler {
  async handle(command) {
    const order = new Order(command.items, command.userId);
    await orderWriteRepo.save(order);
    
    // Publish event
    await eventBus.publish('OrderCreated', {
      orderId: order.id,
      userId: command.userId
    });
  }
}

// Queries (Read)
class GetOrderQuery {
  constructor(orderId) {
    this.orderId = orderId;
  }
}

class GetOrderHandler {
  async handle(query) {
    // Read from optimized read model
    return await orderReadRepo.getById(query.orderId);
  }
}

// Separate databases
const writeDb = new PostgresConnection(); // Normalized
const readDb = new MongoConnection();     // Denormalized, optimized for reads
```

#### 4. Event Sourcing

Event Sourcing'i **banka hesap ekstresi** gibi düşünün: Bankanız bakiyenizi "5000 TL" diye saklamaz. Bunun yerine her işlemi kaydeder: "maaş yatırıldı +10.000", "kira ödendi -3.000", "market alışverişi -500"... ve bakiyenizi bu olayların toplamından **hesaplar**. İstediğiniz zaman herhangi bir tarihteki bakiyenize dönebilirsiniz — çünkü tüm geçmiş mevcuttur.

Geleneksel yaklaşımda: `UPDATE users SET balance = 500`. Event Sourcing'de: `APPEND event: { type: 'WITHDRAWAL', amount: 100, timestamp: ... }`. Mevcut durumu görmek için tüm event'leri **replay** edersiniz.

**Faydaları çok güçlüdür:**

- **Complete Audit Trail (Tam Denetim İzi):** Her değişikliğin kim tarafından, ne zaman, neden yapıldığı kaydedilir. Finans ve sağlık sektöründe bu yasal zorunluluktur.
- **Time-Travel Debugging:** Bir bug mu var? Event'leri istediğiniz noktaya kadar replay edip, "tam olarak burada ne oldu?" diyebilirsiniz. Production'daki bir hatayı local'de birebir tekrarlayabilirsiniz.
- **Event Replay:** Yeni bir read model mi eklediniz? Tüm geçmiş event'leri yeni model üzerinden replay ederek, sanki baştan beri oradaymış gibi veri oluşturabilirsiniz.
- **What-if Senaryoları:** "Eğer fiyatlandırmayı 3 ay önce değiştirseydik ne olurdu?" — event'leri farklı mantıkla replay ederek cevaplayabilirsiniz.

**Zorlukları da vardır:**

- **Eventual Consistency:** Event store'a yazılan event, read model'e yansıyana kadar geçen süre. Kullanıcı "az önce güncelledim ama hâlâ eski veriyi görüyorum" diyebilir.
- **Event Schema Evolution:** 2 yıl önce yayınladığınız `OrderCreated` event'inin şeması değişti. Eski event'leri yeni şemayla nasıl okuyacaksınız? Versioning, upcasting gibi stratejiler gerekir.
- **Storage Growth:** Her değişiklik bir event. Yüksek trafikli sistemlerde event store çok hızlı büyür. Snapshotting (belirli aralıklarla mevcut durumu kaydetme) ile yönetilir.

**Ne zaman kullanmalı:**
- Finansal sistemler, ödeme sistemleri (denetim izi zorunlu)
- Audit-critical uygulamalar (sağlık, hukuk)
- Karmaşık domain event'leri olan sistemler
- Event replay ile yeni projections oluşturmanız gereken durumlar

**Ne zaman KULLANMAMALI:**
- Basit CRUD uygulamaları — muazzam overkill! Bir blog uygulaması için Event Sourcing kullanmak, karıncayı topla vurmak gibidir.
- Takımınız Event Sourcing deneyimine sahip değilse — öğrenme eğrisi diktir.
- Anlık tutarlılık (strong consistency) zorunluysa — Event Sourcing doğası gereği eventual consistency üzerine kuruludur.

```javascript
// Events
class OrderCreatedEvent {
  constructor(orderId, userId, items) {
    this.orderId = orderId;
    this.userId = userId;
    this.items = items;
    this.timestamp = Date.now();
  }
}

class OrderShippedEvent {
  constructor(orderId, trackingNumber) {
    this.orderId = orderId;
    this.trackingNumber = trackingNumber;
    this.timestamp = Date.now();
  }
}

// Event Store
class EventStore {
  async append(streamId, event) {
    await db.query(
      'INSERT INTO events (stream_id, event_type, data, timestamp) VALUES ($1, $2, $3, $4)',
      [streamId, event.constructor.name, JSON.stringify(event), event.timestamp]
    );
  }
  
  async getEvents(streamId) {
    const rows = await db.query('SELECT * FROM events WHERE stream_id = $1 ORDER BY timestamp', [streamId]);
    return rows.map(row => JSON.parse(row.data));
  }
}

// Aggregate
class Order {
  constructor() {
    this.id = null;
    this.status = 'PENDING';
    this.items = [];
  }
  
  // Replay events to rebuild state
  apply(event) {
    if (event instanceof OrderCreatedEvent) {
      this.id = event.orderId;
      this.items = event.items;
      this.status = 'CREATED';
    } else if (event instanceof OrderShippedEvent) {
      this.status = 'SHIPPED';
      this.trackingNumber = event.trackingNumber;
    }
  }
  
  static async load(orderId, eventStore) {
    const events = await eventStore.getEvents(orderId);
    const order = new Order();
    events.forEach(event => order.apply(event));
    return order;
  }
}
```

---

## 💼 CRM ve Diğer Business Uygulamaları

### CRM (Customer Relationship Management) Nedir?

**Tanım:**
CRM, müşteri ilişkilerini yönetmek için kullanılan yazılım ve stratejilerdir. Müşteri verilerini merkezi bir yerde toplar, satış süreçlerini takip eder ve müşteri etkileşimlerini optimize eder.

**CRM'in Temel Fonksiyonları:**
```
1. Contact Management (İletişim Yönetimi)
   - Müşteri bilgileri (isim, email, telefon, adres)
   - İletişim geçmişi
   - Segmentasyon (müşteri grupları)

2. Sales Pipeline (Satış Hunisi)
   - Lead tracking (potansiyel müşteri takibi)
   - Opportunity management (fırsat yönetimi)
   - Deal stages (anlaşma aşamaları)
   - Sales forecasting (satış tahminleri)

3. Marketing Automation
   - Email campaigns
   - Lead scoring (lead puanlama)
   - Campaign tracking
   - A/B testing

4. Customer Service
   - Ticket system (destek talepleri)
   - Knowledge base (bilgi tabanı)
   - Live chat
   - Customer satisfaction tracking

5. Analytics & Reporting
   - Sales reports
   - Customer insights
   - Revenue analytics
   - Performance dashboards
```

### Popüler CRM Sistemleri ve Özellikleri

#### 1. Salesforce
```
Öne Çıkan Özellikler:
- En kapsamlı CRM platformu
- Highly customizable (Apex, Lightning Components)
- AppExchange marketplace
- AI features (Einstein)
- Multi-cloud (Sales Cloud, Service Cloud, Marketing Cloud)

Kimler Kullanır:
- Enterprise şirketler
- B2B companies
- Complex sales processes

Dezavantajları:
- Pahalı
- Karmaşık setup
- Steep learning curve
```

#### 2. HubSpot
```
Öne Çıkan Özellikler:
- All-in-one (CRM + Marketing + Sales + Service)
- Free tier available
- User-friendly interface
- Inbound marketing odaklı
- Excellent content management

Kimler Kullanır:
- SMB (Small-Medium Business)
- Marketing-driven companies
- Startups

Avantajları:
- Kolay kullanım
- Ücretsiz başlangıç
- Güçlü marketing automation
```

#### 3. Zoho CRM
```
Öne Çıkan Özellikler:
- Uygun fiyat
- AI assistant (Zia)
- Omnichannel support
- Workflow automation

Kimler Kullanır:
- Budget-conscious businesses
- Small to medium businesses

Avantajları:
- Cost-effective
- Good integration options
```

#### 4. Microsoft Dynamics 365
```
Öne Çıkan Özellikler:
- Enterprise-level CRM
- Deep Microsoft ecosystem integration (Office 365, Teams)
- AI & ML capabilities
- Industry-specific solutions

Kimler Kullanır:
- Microsoft-centric organizations
- Large enterprises

Avantajları:
- Seamless Microsoft integration
- Powerful automation
```

#### 5. Pipedrive
```
Öne Çıkan Özellikler:
- Sales pipeline odaklı
- Visual pipeline management
- Simple & intuitive
- Mobile-first

Kimler Kullanır:
- Sales teams
- SMBs

Avantajları:
- Basit ve etkili
- Sales process optimization
```

### CRM Sistemi Nasıl Tasarlanır?

**Database Schema (Simplified):**
```sql
-- Contacts (Müşteriler)
CREATE TABLE contacts (
  id UUID PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(255) UNIQUE,
  phone VARCHAR(50),
  company_id UUID REFERENCES companies(id),
  owner_id UUID REFERENCES users(id),  -- Sales rep
  lead_source VARCHAR(50),  -- web, referral, cold call
  status VARCHAR(50),  -- lead, prospect, customer, churned
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Companies
CREATE TABLE companies (
  id UUID PRIMARY KEY,
  name VARCHAR(255),
  industry VARCHAR(100),
  size VARCHAR(50),  -- 1-10, 11-50, 51-200, etc.
  website VARCHAR(255),
  annual_revenue DECIMAL(15,2),
  created_at TIMESTAMP
);

-- Deals (Opportunities)
CREATE TABLE deals (
  id UUID PRIMARY KEY,
  name VARCHAR(255),
  contact_id UUID REFERENCES contacts(id),
  company_id UUID REFERENCES companies(id),
  amount DECIMAL(15,2),
  stage VARCHAR(50),  -- prospecting, qualification, proposal, negotiation, closed_won, closed_lost
  probability INT,  -- 0-100
  expected_close_date DATE,
  owner_id UUID REFERENCES users(id),
  created_at TIMESTAMP,
  closed_at TIMESTAMP
);

-- Activities (İletişim Geçmişi)
CREATE TABLE activities (
  id UUID PRIMARY KEY,
  type VARCHAR(50),  -- call, email, meeting, note
  subject VARCHAR(255),
  description TEXT,
  contact_id UUID REFERENCES contacts(id),
  deal_id UUID REFERENCES deals(id),
  user_id UUID REFERENCES users(id),
  scheduled_at TIMESTAMP,
  completed_at TIMESTAMP,
  created_at TIMESTAMP
);

-- Email Campaigns
CREATE TABLE campaigns (
  id UUID PRIMARY KEY,
  name VARCHAR(255),
  subject VARCHAR(255),
  content TEXT,
  status VARCHAR(50),  -- draft, scheduled, sent
  sent_at TIMESTAMP,
  created_at TIMESTAMP
);

-- Campaign Contacts (Many-to-Many)
CREATE TABLE campaign_contacts (
  campaign_id UUID REFERENCES campaigns(id),
  contact_id UUID REFERENCES contacts(id),
  sent_at TIMESTAMP,
  opened_at TIMESTAMP,
  clicked_at TIMESTAMP,
  PRIMARY KEY (campaign_id, contact_id)
);
```

**API Endpoints:**
```javascript
// Contacts
GET    /api/contacts              // List contacts
POST   /api/contacts              // Create contact
GET    /api/contacts/:id          // Get contact
PUT    /api/contacts/:id          // Update contact
DELETE /api/contacts/:id          // Delete contact
GET    /api/contacts/:id/activities  // Contact timeline

// Deals
GET    /api/deals                 // List deals
POST   /api/deals                 // Create deal
PUT    /api/deals/:id/stage       // Move deal stage
GET    /api/deals/pipeline        // Visual pipeline

// Activities
POST   /api/activities            // Log activity
GET    /api/activities/upcoming   // Upcoming tasks

// Reports
GET    /api/reports/sales         // Sales analytics
GET    /api/reports/pipeline      // Pipeline forecast
```

**Key Features Implementation:**

```javascript
// Lead Scoring
class LeadScoring {
  calculateScore(contact) {
    let score = 0;
    
    // Demographic scoring
    if (contact.company.size === '51-200') score += 20;
    if (contact.company.annual_revenue > 1000000) score += 30;
    
    // Engagement scoring
    if (contact.email_opened_count > 5) score += 15;
    if (contact.website_visits > 10) score += 10;
    if (contact.demo_requested) score += 25;
    
    return Math.min(score, 100);
  }
}

// Sales Pipeline Automation
class PipelineAutomation {
  async moveDealStage(dealId, newStage) {
    const deal = await Deal.findById(dealId);
    
    // Auto-update probability
    const stageProbabilities = {
      'prospecting': 10,
      'qualification': 25,
      'proposal': 50,
      'negotiation': 75,
      'closed_won': 100,
      'closed_lost': 0
    };
    
    deal.stage = newStage;
    deal.probability = stageProbabilities[newStage];
    
    // Trigger automation
    if (newStage === 'closed_won') {
      await this.onDealWon(deal);
    }
    
    await deal.save();
  }
  
  async onDealWon(deal) {
    // Create customer account
    await Customer.create({ contactId: deal.contact_id });
    
    // Send welcome email
    await emailService.sendTemplate('welcome', deal.contact.email);
    
    // Notify team
    await slack.notify(`🎉 Deal won: ${deal.name} - $${deal.amount}`);
  }
}

// Email Campaign Tracking
class CampaignTracking {
  async trackOpen(campaignId, contactId) {
    await CampaignContact.update({
      campaign_id: campaignId,
      contact_id: contactId
    }, {
      opened_at: new Date()
    });
    
    // Update contact engagement score
    await this.updateEngagementScore(contactId);
  }
  
  async trackClick(campaignId, contactId, linkUrl) {
    await CampaignContact.update({
      campaign_id: campaignId,
      contact_id: contactId
    }, {
      clicked_at: new Date()
    });
    
    await Analytics.track('email_click', {
      campaignId,
      contactId,
      linkUrl
    });
  }
}
```

### Diğer Business Uygulamaları

#### 1. ERP (Enterprise Resource Planning)
**Nedir:**
- Şirket kaynaklarını (finans, HR, üretim, lojistik) tek bir sistemde yönetme
- Departmanlar arası veri akışı

**Örnekler:**
- SAP
- Oracle ERP
- Microsoft Dynamics
- Odoo

**Modüller:**
```
Finance: Muhasebe, bütçe, raporlama
HR: İnsan kaynakları, bordro, izin yönetimi
Inventory: Stok yönetimi, warehouse
Manufacturing: Üretim planlama, MRP
Procurement: Satın alma, tedarikçi yönetimi
Sales: Sipariş yönetimi, faturalama
```

#### 2. E-Commerce Platforms
**Örnekler:**
- Shopify
- WooCommerce
- Magento
- BigCommerce

**Temel Özellikler:**
```javascript
// Product Catalog
class Product {
  id: string;
  name: string;
  price: number;
  inventory: number;
  variants: ProductVariant[];  // size, color, etc.
  images: string[];
  seo: SEOMetadata;
}

// Shopping Cart
class Cart {
  userId: string;
  items: CartItem[];
  
  calculateTotal() {
    return this.items.reduce((sum, item) => 
      sum + item.price * item.quantity, 0
    );
  }
}

// Order Processing
class Order {
  orderNumber: string;
  status: 'pending' | 'processing' | 'shipped' | 'delivered';
  payment: PaymentInfo;
  shipping: ShippingInfo;
  
  async processPayment() {
    const payment = await paymentGateway.charge(this.payment);
    if (payment.success) {
      this.status = 'processing';
      await this.reserveInventory();
      await this.createShipment();
    }
  }
}
```

#### 3. Content Management Systems (CMS)
**Örnekler:**
- WordPress
- Contentful (Headless CMS)
- Strapi
- Sanity

**Headless CMS Architecture:**
```javascript
// Content API
GET /api/posts
GET /api/posts/:slug
GET /api/pages/:slug

// Frontend (Any framework)
React / Vue / Next.js
├── Fetches content from CMS API
├── Renders content
└── Deploys to CDN (Vercel, Netlify)

// Benefits
- Decoupled frontend/backend
- Multi-channel (web, mobile, IoT)
- API-first approach
```

#### 4. Project Management Tools
**Örnekler:**
- Jira
- Asana
- Monday.com
- Trello

**Core Features:**
```javascript
// Task Management
class Task {
  id: string;
  title: string;
  description: string;
  assignee: User;
  status: 'todo' | 'in_progress' | 'review' | 'done';
  priority: 'low' | 'medium' | 'high' | 'urgent';
  dueDate: Date;
  tags: string[];
  attachments: File[];
  comments: Comment[];
  timeTracking: {
    estimated: number;
    actual: number;
  };
}

// Kanban Board
class Board {
  columns: Column[];
  
  moveTask(taskId, fromColumn, toColumn) {
    // Update task status
    // Trigger automation (e.g., notify assignee)
  }
}

// Sprint Management
class Sprint {
  name: string;
  startDate: Date;
  endDate: Date;
  tasks: Task[];
  
  calculateVelocity() {
    return this.tasks
      .filter(t => t.status === 'done')
      .reduce((sum, t) => sum + t.points, 0);
  }
}
```

#### 5. Analytics Platforms
**Örnekler:**
- Google Analytics
- Mixpanel
- Amplitude
- Segment

**Event Tracking:**
```javascript
// Track user behavior
analytics.track('ProductViewed', {
  productId: '12345',
  productName: 'iPhone 15',
  price: 999,
  category: 'Electronics'
});

analytics.track('AddedToCart', {
  productId: '12345',
  quantity: 1
});

analytics.track('PurchaseCompleted', {
  orderId: 'ORD-123',
  total: 999,
  items: [...]
});

// User properties
analytics.identify(userId, {
  email: 'user@example.com',
  plan: 'premium',
  signupDate: '2024-01-15'
});

// Funnel analysis
Funnel: ProductViewed -> AddedToCart -> CheckoutStarted -> PurchaseCompleted
Conversion rate at each step
```

---

## 👥 Team Leadership & Engineering Management

### Code Review Best Practices

#### Effective Code Reviews

**What to Look For:**
```
1. Functionality
   - Does code do what it's supposed to?
   - Edge cases handled?
   - Error handling proper?

2. Code Quality
   - Readable & maintainable?
   - Follows SOLID principles?
   - Proper naming?
   - Comments where necessary?

3. Testing
   - Adequate test coverage?
   - Test quality (not just coverage %)?
   - Edge cases tested?

4. Performance
   - N+1 queries?
   - Unnecessary loops?
   - Memory leaks?
   - Caching opportunities?

5. Security
   - Input validation?
   - SQL injection prevention?
   - XSS protection?
   - Sensitive data handling?

6. Architecture
   - Follows existing patterns?
   - Proper separation of concerns?
   - Scalability considerations?
```

**How to Give Feedback:**
```javascript
// ❌ Bad feedback
"This is wrong"
"Don't do this"
"Bad code"

// ✅ Good feedback
"Consider using Array.map() instead of forEach for better readability"
"This could cause a memory leak because... Suggest: ..."
"Great use of the factory pattern here! 👍"
"Question: Have you considered the case when user is null?"
"Nit: Variable name could be more descriptive (userData -> userProfile)"
"Suggestion: Extract this into a separate function for reusability"

// Tags
[CRITICAL]: Security vulnerability, must fix
[BLOCKER]: Breaks functionality
[SUGGESTION]: Optional improvement
[QUESTION]: Need clarification
[NIT]: Minor style issue
[PRAISE]: Good work!
```

**Code Review Checklist:**
```markdown
## Functionality
- [ ] Code works as intended
- [ ] Edge cases handled
- [ ] Error handling present

## Tests
- [ ] New tests added
- [ ] Existing tests pass
- [ ] Coverage maintained/improved

## Performance
- [ ] No obvious performance issues
- [ ] Database queries optimized
- [ ] Caching considered

## Security
- [ ] Input validated
- [ ] No security vulnerabilities
- [ ] Secrets not committed

## Documentation
- [ ] README updated if needed
- [ ] API docs updated
- [ ] Complex logic commented

## Architecture
- [ ] Follows existing patterns
- [ ] No unnecessary complexity
- [ ] Backwards compatible
```

#### Pull Request Best Practices

**Good PR Description:**
```markdown
## What
Add user profile photo upload feature

## Why
Users requested ability to personalize profiles

## How
- Add /upload endpoint with multipart/form-data
- Store images in S3
- Generate thumbnails (100x100, 300x300)
- Update User model with photo_url field

## Testing
- Unit tests for upload controller
- Integration test for full flow
- Tested with files: jpg, png, heic
- Tested error cases: too large, invalid format

## Screenshots
[Before/After images]

## Rollout Plan
- Feature flag: profile_photo_upload
- Enable for 10% users initially
- Monitor S3 usage & costs

## Checklist
- [x] Tests added
- [x] Documentation updated
- [x] No breaking changes
- [x] Backward compatible
```

**PR Size:**
```
Ideal: < 400 lines changed
Good: 400-800 lines
Warning: 800-1500 lines
Too Large: > 1500 lines

Solution for large PRs:
- Break into multiple PRs
- Use feature flags
- Split infrastructure & logic
```

### Technical Leadership Skills

#### Architecture Decision Records (ADR)

```markdown
# ADR-001: Use PostgreSQL for Main Database

## Status
Accepted

## Context
Need to choose primary database for new microservice.
Requirements:
- ACID transactions
- Complex queries with joins
- JSON support for flexible data
- Strong consistency

## Decision
Use PostgreSQL instead of MongoDB or DynamoDB.

## Consequences

### Positive
- ACID guarantees
- Excellent JSON support (JSONB)
- Mature ecosystem
- Team expertise

### Negative
- Scaling complexity (vs DynamoDB)
- Requires more operational overhead
- Sharding not built-in

### Mitigation
- Use read replicas for scaling reads
- Connection pooling (pgbouncer)
- Regular vacuum & maintenance

## Alternatives Considered

### MongoDB
- Pros: Flexible schema, easy scaling
- Cons: Limited transaction support, less consistency

### DynamoDB
- Pros: Fully managed, auto-scaling
- Cons: Query limitations, expensive, vendor lock-in

## References
- [PostgreSQL vs MongoDB benchmark]
- Team survey results
```

#### Tech Debt Management

**Tracking Tech Debt:**
```javascript
// Code comments
// TODO: Refactor this to use async/await
// FIXME: Memory leak in this loop
// HACK: Temporary solution, needs proper fix
// DEBT: Using deprecated API, migrate to v2

// Issue tracking
Label: tech-debt
Priority: P2 (after critical bugs)
Estimate: 3 days
Impact: Reduces deployment time by 30%
```

**Tech Debt Quadrant:**
```
High Impact, Low Effort -> DO NOW
├─ Update deprecated dependencies
├─ Fix N+1 queries
└─ Add missing indexes

High Impact, High Effort -> PLAN & SCHEDULE
├─ Migrate to microservices
├─ Database sharding
└─ Rewrite legacy module

Low Impact, Low Effort -> FILLER TASKS
├─ Update comments
├─ Rename variables
└─ Remove unused code

Low Impact, High Effort -> AVOID
├─ Premature optimization
├─ Over-engineering
└─ Rewrite working code
```

**Paying Down Debt:**
```
1. Allocate capacity
   - 20% of sprint for tech debt
   - One day per week
   - Dedicated refactoring sprints

2. Track metrics
   - Deployment frequency
   - Build time
   - Test coverage
   - Bug rate
   - Developer satisfaction

3. Make visible
   - Tech debt backlog
   - Regular reviews
   - Show business impact
```

### Mentoring & Knowledge Sharing

#### Onboarding New Engineers

**First Week:**
```markdown
## Day 1
- [ ] Setup development environment
- [ ] Access to systems granted
- [ ] Read architecture docs
- [ ] Meet the team

## Day 2-3
- [ ] Run application locally
- [ ] Make first commit (README update)
- [ ] Review codebase structure
- [ ] Pair programming session

## Day 4-5
- [ ] Pick up "good first issue"
- [ ] Submit first PR
- [ ] Shadow on-call engineer
- [ ] Learn deployment process

## Week 2+
- [ ] Own a small feature
- [ ] Present in team meeting
- [ ] Review others' PRs
```

**Pair Programming:**
```
Driver-Navigator:
- Driver: Writes code
- Navigator: Reviews, suggests, thinks ahead
- Switch every 20-30 minutes

Benefits:
- Knowledge transfer
- Code quality
- Reduced bugs
- Team bonding

When to use:
- Onboarding
- Complex problems
- Critical features
- Learning new tech
```

#### Tech Talks & Documentation

**Internal Tech Talk Topics:**
```
1. "How We Reduced API Latency by 50%"
2. "Introduction to Kubernetes"
3. "Our Journey to Microservices"
4. "Security Best Practices"
5. "Testing Strategies"
6. "Debugging Production Issues"
```

**Documentation Culture:**
```markdown
## Must Document

### Architecture
- System overview diagram
- Service dependencies
- Data flow
- Deployment architecture

### Runbooks
- Deployment process
- Rollback procedure
- Common issues & solutions
- On-call procedures

### API Documentation
- OpenAPI/Swagger spec
- Authentication
- Rate limits
- Examples

### Development
- Local setup instructions
- Testing guidelines
- Code contribution guide
- Architecture decisions (ADRs)
```

### Team Communication

#### Stand-ups (Daily Sync)

**Effective Stand-up:**
```
Each person shares:
1. What I did yesterday
2. What I'll do today
3. Any blockers

Keep it:
- Short (15 min max)
- Focused (no deep dives)
- Action-oriented

Red flags to address:
- Same blocker multiple days
- No progress
- Working on unknown tasks
```

#### Sprint Planning

**Story Estimation:**
```
Story Points (Fibonacci):
1 point:  < 4 hours, trivial
2 points: Half day, straightforward
3 points: Full day, well understood
5 points: 2-3 days, some unknowns
8 points: Week, significant complexity
13 points: Too large, needs breakdown

Factors:
- Complexity
- Uncertainty
- Amount of work
```

**Sprint Goals:**
```markdown
## Sprint 24 Goals

### Primary
- Complete user authentication feature
- Deploy payment service to production
- Reduce API error rate to < 0.1%

### Secondary
- Refactor order processing logic
- Update monitoring dashboards

### Tech Debt
- Upgrade to Node.js 20
- Fix flaky integration tests
```

### Making Technical Decisions

**Decision Framework:**
```
1. Define the problem
   - What are we trying to solve?
   - Why is current solution inadequate?

2. Gather requirements
   - Functional requirements
   - Non-functional (performance, security, cost)
   - Constraints (time, budget, team skills)

3. Research options
   - Industry standards
   - Team experience
   - Community support
   - Total cost of ownership

4. Prototype if needed
   - Spike (timeboxed exploration)
   - Proof of concept
   - Benchmark

5. Document decision (ADR)
   
6. Review with team
   - Get feedback
   - Build consensus
   - Address concerns

7. Commit & execute

8. Review after some time
   - Was it right decision?
   - What did we learn?
```

**Trade-off Analysis:**
```
Example: Choosing message queue

RabbitMQ:
+ Mature, stable
+ Rich features
+ Good for complex routing
- Operational overhead
- Scaling complexity

SQS:
+ Fully managed
+ Infinite scale
+ Pay per use
- Less features
- Vendor lock-in
- Higher latency

Decision factors:
- Team expertise (RabbitMQ +1)
- Operational capacity (SQS +1)
- Feature requirements (RabbitMQ +1)
- Cost at our scale (SQS +1)
- Time to market (SQS +1)

Result: Choose SQS for MVP speed,
might migrate to RabbitMQ later
```

---

## 🏆 Production Excellence

### Incident Management

#### On-Call Playbook

**Severity Levels:**
```
SEV-1 (Critical):
- Complete outage
- Data loss
- Security breach
Response: Immediate, all hands on deck
Example: Payment processing down

SEV-2 (High):
- Partial outage
- Performance degradation
- Major feature broken
Response: Within 1 hour
Example: Checkout flow broken for mobile users

SEV-3 (Medium):
- Minor feature broken
- Non-critical service down
Response: Next business day
Example: Email notifications delayed

SEV-4 (Low):
- Cosmetic issues
- Documentation errors
Response: Backlog
```

**Incident Response Process:**
```markdown
## 1. Detect & Alert
- Monitoring alert fires
- User report
- Internal discovery

## 2. Acknowledge
- On-call engineer acknowledges
- Updates status page
- Notifies stakeholders

## 3. Triage
- Assess severity
- Identify affected systems
- Gather initial information

## 4. Mitigate
- Stop the bleeding
- Rollback if possible
- Apply temporary fix

## 5. Resolve
- Identify root cause
- Apply permanent fix
- Verify resolution

## 6. Communicate
- Update stakeholders
- Post-mortem meeting
- Document learnings

## 7. Follow-up
- Implement preventions
- Update runbooks
- Track action items
```

**Incident Communication:**
```
Status Page Update:
[2024-04-13 14:30 UTC] Investigating
We are investigating reports of slow API responses.

[2024-04-13 14:45 UTC] Identified
Issue identified: Database connection pool exhausted.
Scaling up database replicas.

[2024-04-13 15:00 UTC] Monitoring
Fix deployed. Monitoring for stability.

[2024-04-13 15:30 UTC] Resolved
Incident resolved. API response times back to normal.
Post-mortem will be published within 48 hours.
```

#### Post-Mortems

**Blameless Post-Mortem Template:**
```markdown
# Post-Mortem: API Outage on 2024-04-13

## Summary
On April 13, 2024, our API experienced a complete outage
lasting 45 minutes, affecting all users. Root cause was
database connection pool exhaustion due to connection leak.

## Impact
- Duration: 14:15 - 15:00 UTC (45 minutes)
- Users affected: All users (~500K)
- Requests failed: ~2M
- Revenue impact: ~$50K

## Timeline (all times UTC)
- 14:15 - First alerts for elevated error rates
- 14:18 - On-call engineer acknowledges
- 14:25 - Database connection pool exhausted
- 14:30 - Incident escalated to SEV-1
- 14:35 - Rollback initiated
- 14:45 - Identified connection leak in new code
- 14:50 - Rollback completed
- 15:00 - System recovered, monitoring

## Root Cause
New deployment introduced a code path that didn't
properly close database connections. Under high load,
this exhausted the connection pool.

Code snippet:
\`\`\`javascript
// Missing connection.release()
async function getUser(id) {
  const connection = await pool.getConnection();
  const user = await connection.query('SELECT * FROM users WHERE id = ?', [id]);
  return user; // ❌ Connection never released!
}
\`\`\`

## Resolution
Rolled back to previous version. Then deployed fix:
\`\`\`javascript
async function getUser(id) {
  const connection = await pool.getConnection();
  try {
    const user = await connection.query('SELECT * FROM users WHERE id = ?', [id]);
    return user;
  } finally {
    connection.release(); // ✅ Always releases
  }
}
\`\`\`

## What Went Well
- Monitoring detected issue quickly
- Team mobilized efficiently
- Rollback was smooth
- Communication was clear

## What Went Wrong
- Code review missed the bug
- No pre-deployment load test
- Connection pool monitoring inadequate
- Rollback took longer than expected

## Action Items
1. [P0] @alice Add connection leak detection to linter (Due: Apr 20)
2. [P0] @bob Add pre-prod load testing to CI (Due: Apr 25)
3. [P1] @charlie Add connection pool metrics & alerts (Due: May 1)
4. [P1] @david Document rollback procedure (Due: Apr 18)
5. [P2] @eve Code review training session (Due: May 15)

## Lessons Learned
- Always use try/finally for resource cleanup
- Load testing critical for database changes
- Monitor resource pools (connections, threads, file descriptors)
```

### Chaos Engineering

**What is Chaos Engineering:**
```
Intentionally injecting failures to test system resilience

Principles:
1. Build hypothesis around steady state
2. Vary real-world events (server crash, network delay)
3. Run experiments in production
4. Automate experiments
```

**Chaos Experiments:**
```javascript
// Using Chaos Toolkit
{
  "title": "API survives database failure",
  "description": "Verify API gracefully handles database unavailability",
  "steady-state-hypothesis": {
    "title": "Application is healthy",
    "probes": [
      {
        "type": "probe",
        "name": "app-must-respond-ok",
        "tolerance": 200,
        "provider": {
          "type": "http",
          "url": "http://api/health",
          "timeout": 3
        }
      }
    ]
  },
  "method": [
    {
      "type": "action",
      "name": "terminate-db-pod",
      "provider": {
        "type": "python",
        "module": "chaosk8s.pod.actions",
        "func": "terminate_pods",
        "arguments": {
          "label_selector": "app=postgres",
          "ns": "production"
        }
      }
    },
    {
      "type": "probe",
      "name": "api-should-use-cache",
      "provider": {
        "type": "http",
        "url": "http://api/users/123",
        "timeout": 5
      },
      "tolerance": [200, 503]
    }
  ],
  "rollbacks": [
    {
      "type": "action", 
      "name": "redeploy-db"
    }
  ]
}
```

### Cost Optimization

#### AWS Cost Management

**Cost Monitoring:**
```javascript
// Set up budget alerts
const budget = {
  BudgetName: 'Monthly-Limit',
  BudgetLimit: {
    Amount: '5000',
    Unit: 'USD'
  },
  TimeUnit: 'MONTHLY',
  BudgetType: 'COST',
  NotificationsWithSubscribers: [
    {
      Notification: {
        ComparisonOperator: 'GREATER_THAN',
        Threshold: 80,
        ThresholdType: 'PERCENTAGE',
        NotificationType: 'ACTUAL'
      },
      Subscribers: [{
        SubscriptionType: 'EMAIL',
        Address: 'ops@company.com'
      }]
    }
  ]
};
```

**Cost Optimization Strategies:**
```
1. Right-sizing
   - Monitor CPU/memory usage
   - Downsize over-provisioned instances
   - Use t3 instances with burstable CPU

2. Reserved Instances / Savings Plans
   - 1-year or 3-year commitment
   - Up to 75% discount
   - Use for stable workloads

3. Spot Instances
   - Up to 90% discount
   - Use for fault-tolerant workloads
   - Batch processing, CI/CD runners

4. Auto-scaling
   - Scale down during low traffic
   - Schedule-based scaling (night/weekend)

5. S3 Lifecycle Policies
   - Move to cheaper storage classes
   - Delete old files
   - Archive to Glacier

6. Lambda Optimization
   - Right-size memory (affects CPU)
   - Use ARM architecture (20% cheaper)
   - Reduce cold starts (Provisioned Concurrency)

7. Database Optimization
   - Use read replicas (cheaper than scaling primary)
   - Archive old data
   - Consider Aurora Serverless for variable workloads

8. CDN Usage
   - Reduce origin hits
   - CloudFront cheaper than EC2 bandwidth

9. Monitoring Optimization
   - Reduce log retention
   - Sample metrics
   - Use metric filters
```

**Cost Allocation Tags:**
```javascript
// Tag all resources
{
  tags: [
    { Key: 'Environment', Value: 'production' },
    { Key: 'Team', Value: 'backend' },
    { Key: 'Project', Value: 'api-v2' },
    { Key: 'CostCenter', Value: 'engineering' }
  ]
}

// Cost reports by tag
- Which team/project costs most?
- Shutdown dev/test resources after hours
- Identify unused resources
```

### Disaster Recovery & Business Continuity

**Recovery Metrics:**
```
RTO (Recovery Time Objective):
Maximum acceptable downtime
Example: Must restore service within 4 hours

RPO (Recovery Point Objective):
Maximum acceptable data loss
Example: Can lose up to 1 hour of data
```

**Backup Strategies:**
```
Database:
- Automated daily snapshots
- Point-in-time recovery (binlogs/WAL)
- Cross-region replication
- Test restore regularly

Application:
- Infrastructure as Code (can rebuild)
- Docker images in registry
- Configuration in Git

Data:
- S3 versioning + replication
- Glacier for archives
- Immutable backups (ransomware protection)
```

**Disaster Recovery Strategies:**
```
1. Backup & Restore (cheapest, slowest)
   RTO: Hours to days
   RPO: Hours
   Cost: $
   
2. Pilot Light (minimal standby)
   RTO: Hours
   RPO: Minutes
   Cost: $$
   
3. Warm Standby (scaled-down replica)
   RTO: Minutes
   RPO: Seconds
   Cost: $$$
   
4. Multi-Site Active-Active
   RTO: Seconds
   RPO: Near-zero
   Cost: $$$$
```

**DR Testing:**
```markdown
## Quarterly DR Drill

### Objective
Verify ability to recover from total region failure

### Scenario
AWS us-east-1 region completely unavailable

### Steps
1. Trigger failover to us-west-2
2. Verify DNS updates
3. Check application functionality
4. Test database replication
5. Monitor for issues

### Success Criteria
- [ ] Failover completed within 30 minutes
- [ ] All critical services operational
- [ ] Data loss < 5 minutes
- [ ] No data corruption

### Lessons Learned
[Document improvements needed]
```

---

## 💡 Best Practices & Soft Skills

### Code Quality

#### 1. SOLID Principles
```javascript
// S - Single Responsibility
// ❌ Bad
class User {
  saveToDatabase() {}
  sendEmail() {}
  generateReport() {}
}

// ✅ Good
class User {
  // Only user data
}
class UserRepository {
  save(user) {}
}
class EmailService {
  send(user, template) {}
}

// O - Open/Closed (Open for extension, closed for modification)
class Shape {
  area() {
    throw new Error('Must implement');
  }
}
class Circle extends Shape {
  area() { return Math.PI * this.radius ** 2; }
}
class Rectangle extends Shape {
  area() { return this.width * this.height; }
}

// L - Liskov Substitution
// Subclass should be substitutable for parent class

// I - Interface Segregation
// Don't force classes to implement unused methods

// D - Dependency Inversion
// Depend on abstractions, not concretions
class OrderService {
  constructor(paymentProvider) {  // Interface, not concrete class
    this.payment = paymentProvider;
  }
}
```

#### 2. Clean Code Principles
```javascript
// Meaningful names
// ❌ Bad
const d = new Date();
const x = users.filter(u => u.a > 18);

// ✅ Good
const currentDate = new Date();
const adultUsers = users.filter(user => user.age > 18);

// Small functions
// ❌ Bad
function processOrder(order) {
  // 200 lines of code...
}

// ✅ Good
function processOrder(order) {
  validateOrder(order);
  const payment = processPayment(order);
  const shipment = createShipment(order);
  sendConfirmation(order, payment, shipment);
}

// Avoid magic numbers
// ❌ Bad
if (user.age < 18) {}

// ✅ Good
const LEGAL_AGE = 18;
if (user.age < LEGAL_AGE) {}
```

#### 3. Testing Strategies
```javascript
// Unit Tests
describe('OrderService', () => {
  it('should calculate total correctly', () => {
    const order = new Order([
      { price: 10, quantity: 2 },
      { price: 5, quantity: 3 }
    ]);
    
    expect(order.calculateTotal()).toBe(35);
  });
  
  it('should throw error for invalid items', () => {
    expect(() => new Order([])).toThrow('Order must have items');
  });
});

// Integration Tests
describe('POST /api/orders', () => {
  it('should create order and return 201', async () => {
    const response = await request(app)
      .post('/api/orders')
      .send({
        userId: 'user123',
        items: [{ productId: 'prod1', quantity: 2 }]
      });
    
    expect(response.status).toBe(201);
    expect(response.body.orderId).toBeDefined();
  });
});

// E2E Tests (Cypress, Playwright)
describe('Checkout Flow', () => {
  it('should complete purchase', () => {
    cy.visit('/products');
    cy.get('[data-testid="add-to-cart"]').click();
    cy.get('[data-testid="checkout"]').click();
    cy.get('[data-testid="card-number"]').type('4242424242424242');
    cy.get('[data-testid="submit"]').click();
    cy.contains('Order confirmed').should('be.visible');
  });
});

// Test Coverage
// Aim for 80%+ coverage
// Focus on critical paths
```

### Performance Optimization

#### 1. Database Optimization
```sql
-- Indexing
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Explain query plan
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = '123';

-- N+1 Query Problem
-- ❌ Bad
const users = await User.findAll();
for (const user of users) {
  const orders = await Order.findAll({ where: { userId: user.id } });
}

-- ✅ Good (Eager loading)
const users = await User.findAll({
  include: [{ model: Order }]
});

-- Pagination
SELECT * FROM products 
OFFSET 100 LIMIT 20;

-- Better: Cursor-based pagination
SELECT * FROM products 
WHERE id > last_seen_id 
ORDER BY id 
LIMIT 20;
```

#### 2. Caching Strategies
```javascript
// Multi-level caching
// L1: Application cache (in-memory)
const cache = new Map();

function getUser(id) {
  if (cache.has(id)) {
    return cache.get(id);
  }
  const user = await db.query('SELECT * FROM users WHERE id = ?', [id]);
  cache.set(id, user);
  return user;
}

// L2: Redis cache
async function getProduct(id) {
  // Check Redis
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);
  
  // Check database
  const product = await Product.findById(id);
  
  // Cache in Redis (1 hour)
  await redis.setEx(`product:${id}`, 3600, JSON.stringify(product));
  
  return product;
}

// Cache invalidation
async function updateProduct(id, updates) {
  await Product.update(id, updates);
  await redis.del(`product:${id}`);  // Invalidate cache
}

// HTTP Caching
app.get('/api/products', (req, res) => {
  res.set('Cache-Control', 'public, max-age=300');  // 5 minutes
  res.json(products);
});
```

#### 3. API Optimization
```javascript
// Rate limiting per above

// Compression
const compression = require('compression');
app.use(compression());

// Pagination
app.get('/api/posts', async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 20;
  const offset = (page - 1) * limit;
  
  const posts = await Post.findAll({ offset, limit });
  const total = await Post.count();
  
  res.json({
    data: posts,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit)
    }
  });
});

// Field selection (GraphQL-like)
app.get('/api/users/:id', async (req, res) => {
  const fields = req.query.fields?.split(',') || ['id', 'name', 'email'];
  const user = await User.findById(req.params.id, { attributes: fields });
  res.json(user);
});

// Batch requests
app.post('/api/batch', async (req, res) => {
  const requests = req.body.requests;  // [{ method: 'GET', url: '/users/1' }, ...]
  const results = await Promise.all(
    requests.map(r => processRequest(r))
  );
  res.json(results);
});
```

### System Design Interview Prep

**Klasik Sorular:**

#### 1. URL Shortener (bit.ly)
```
Requirements:
- Shorten long URLs
- Redirect to original URL
- Track clicks
- Custom aliases

Design:
┌──────────┐      ┌──────────────┐      ┌──────────┐
│  Client  │─────>│  API Server  │─────>│  Redis   │
└──────────┘      └──────────────┘      └──────────┘
                         │                     │
                         v                     v
                  ┌──────────────┐      ┌──────────┐
                  │  Database    │      │  Cache   │
                  │  (URLs)      │      └──────────┘
                  └──────────────┘

Database Schema:
- urls: id, short_code, original_url, created_at, expires_at
- clicks: id, short_code, clicked_at, ip, user_agent

Algorithm:
- Base62 encoding (a-z, A-Z, 0-9)
- 7 characters = 62^7 = 3.5 trillion URLs

Scale:
- 100M URLs/day
- Read:Write = 100:1
- CDN for redirects
- Database sharding by short_code
```

#### 2. Design Instagram
```
Features:
- Upload photos
- Follow users
- News feed
- Like/comment

Components:
1. Upload Service
   - S3/CDN for images
   - Image processing (resize, thumbnails)

2. Feed Service
   - Fan-out on write (eager) vs Fan-out on read (lazy)
   - Timeline generation
   - Ranking algorithm

3. Graph Service
   - Follow/unfollow
   - Friend suggestions

4. Engagement Service
   - Likes, comments
   - Real-time updates (WebSocket)

Database:
- Users: PostgreSQL
- Posts: Cassandra (time-series)
- Feed: Redis (sorted sets)
- Graphs: Neo4j or adjacency list

Scale:
- 500M users
- 100M photos/day
- CDN for global distribution
```

#### 3. Design Rate Limiter
```
Algorithms:

1. Token Bucket
   - Tokens refill at constant rate
   - Each request consumes token
   - If no tokens, reject

2. Leaky Bucket
   - Requests queued
   - Processed at fixed rate

3. Fixed Window
   - Count requests in time window
   - Reset counter at window boundary

4. Sliding Window Log
   - Log timestamp of each request
   - Count requests in rolling window

Implementation:
const rateLimit = async (userId, limit, window) => {
  const key = `rate:${userId}`;
  const now = Date.now();
  const windowStart = now - window;
  
  // Remove old entries
  await redis.zRemRangeByScore(key, 0, windowStart);
  
  // Count recent requests
  const count = await redis.zCard(key);
  
  if (count >= limit) {
    throw new Error('Rate limit exceeded');
  }
  
  // Add current request
  await redis.zAdd(key, { score: now, value: `${now}` });
  await redis.expire(key, Math.ceil(window / 1000));
};
```

### Advanced Topics

#### Multi-tenancy Patterns

**What is Multi-tenancy:**
- Tek application instance, multiple müşteriler (tenants)
- Her tenant izole edilmiş data
- Resource paylaşımı ile cost efficiency

**Isolation Strategies:**

**1. Database Per Tenant (Highest isolation)**
```javascript
// Route to correct database
function getTenantDb(tenantId) {
  return databases[tenantId];
}

async function getUsers(tenantId) {
  const db = getTenantDb(tenantId);
  return await db.query('SELECT * FROM users');
}

// Pros:
+ Complete data isolation
+ Easy to backup/restore per tenant
+ Can customize schema per tenant
+ Easy to move tenant to different server

// Cons:
- High cost (many databases)
- Complex connection pooling
- Schema migrations challenging
- Resource inefficiency
```

**2. Schema Per Tenant (Good isolation)**
```javascript
// PostgreSQL schemas
async function getUsers(tenantId) {
  await db.query(`SET search_path TO tenant_${tenantId}`);
  return await db.query('SELECT * FROM users');
}

// Pros:
+ Good data isolation
+ Share connection pool
+ Lower cost than separate DBs

// Cons:
- Still many schemas to manage
- Schema migrations complex
- Limited by database size
```

**3. Shared Schema with Tenant ID (Most efficient)**
```javascript
// Add tenant_id to all tables
CREATE TABLE users (
  id UUID PRIMARY KEY,
  tenant_id UUID NOT NULL,
  name VARCHAR(255),
  email VARCHAR(255),
  -- All queries filtered by tenant_id
);

CREATE INDEX idx_users_tenant ON users(tenant_id);

// Always filter by tenant
async function getUsers(tenantId) {
  return await db.query(
    'SELECT * FROM users WHERE tenant_id = $1',
    [tenantId]
  );
}

// Row Level Security (PostgreSQL)
CREATE POLICY tenant_isolation ON users
  USING (tenant_id = current_setting('app.current_tenant')::uuid);

ALTER TABLE users ENABLE ROW LEVEL SECURITY;

// Pros:
+ Most cost-effective
+ Easy to scale
+ Simple schema management

// Cons:
- Data not physically isolated
- Risk of data leakage (missing WHERE clause)
- Large tables
- Difficult to extract single tenant
```

**Tenant Context Middleware:**
```javascript
// Express middleware to set tenant context
async function tenantMiddleware(req, res, next) {
  // Extract tenant from subdomain or header or JWT
  const tenant = extractTenant(req);
  
  if (!tenant) {
    return res.status(400).json({ error: 'Tenant not found' });
  }
  
  // Verify tenant exists and is active
  const tenantConfig = await getTenantConfig(tenant.id);
  if (!tenantConfig || !tenantConfig.active) {
    return res.status(403).json({ error: 'Tenant inactive' });
  }
  
  // Set thread-local storage
  req.tenant = tenantConfig;
  
  // For RLS (Row Level Security) — parameterized query!
  await db.query(
    'SET app.current_tenant = $1', [tenantConfig.id]
  );
  
  next();
}

function extractTenant(req) {
  // From subdomain: acme.myapp.com -> acme
  const subdomain = req.hostname.split('.')[0];
  
  // Or from JWT
  const token = req.headers.authorization;
  const decoded = jwt.verify(token, secret);
  
  return { id: decoded.tenantId, name: subdomain };
}
```

#### Data Pipelines & ETL Basics

**ETL (Extract, Transform, Load):**
```
Extract: Get data from sources
  - Databases
  - APIs
  - Files (CSV, JSON)
  - Streaming (Kafka)

Transform: Clean and process
  - Filtering
  - Aggregation
  - Enrichment
  - Normalization

Load: Store in destination
  - Data warehouse (Snowflake, Redshift)
  - Data lake (S3)
  - Analytics database
```

**Simple ETL Pipeline:**
```javascript
// Extract from API
async function extractOrders() {
  const response = await fetch('https://api.example.com/orders');
  return await response.json();
}

// Transform
function transformOrders(orders) {
  return orders.map(order => ({
    order_id: order.id,
    customer_id: order.customer.id,
    total: order.items.reduce((sum, item) => sum + item.price, 0),
    order_date: new Date(order.created_at),
    status: order.status.toLowerCase()
  })).filter(order => order.total > 0);
}

// Load to data warehouse
async function loadOrders(orders) {
  await dataWarehouse.bulkInsert('orders', orders);
}

// Orchestration
async function runETL() {
  try {
    const rawOrders = await extractOrders();
    const transformedOrders = transformOrders(rawOrders);
    await loadOrders(transformedOrders);
    console.log(`Loaded ${transformedOrders.length} orders`);
  } catch (error) {
    console.error('ETL failed:', error);
    await notifyOps(error);
  }
}

// Schedule with cron
schedule('0 * * * *', runETL); // Every hour
```

**Apache Airflow (Workflow Orchestration):**
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-team',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'order_etl',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
)

def extract_task():
    # Extract logic
    pass

def transform_task():
    # Transform logic
    pass

def load_task():
    # Load logic
    pass

extract = PythonOperator(
    task_id='extract',
    python_callable=extract_task,
    dag=dag
)

transform = PythonOperator(
    task_id='transform',
    python_callable=transform_task,
    dag=dag
)

load = PythonOperator(
    task_id='load',
    python_callable=load_task,
    dag=dag
)

# Define dependencies
extract >> transform >> load
```

**Streaming ETL (Kafka + Spark):**
```javascript
// Kafka consumer -> transform -> write to warehouse
const { Kafka } = require('kafkajs');

const kafka = new Kafka({ brokers: ['localhost:9092'] });
const consumer = kafka.consumer({ groupId: 'etl-group' });

await consumer.connect();
await consumer.subscribe({ topic: 'events' });

await consumer.run({
  eachBatch: async ({ batch }) => {
    const events = batch.messages.map(msg => 
      JSON.parse(msg.value.toString())
    );
    
    // Transform
    const transformed = events.map(transformEvent);
    
    // Batch insert to warehouse
    await warehouse.bulkInsert(transformed);
  }
});
```

#### Mobile Backend Considerations

**API Design for Mobile:**
```javascript
// 1. Versioning (breaking changes)
app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);

// 2. Pagination & Limiting
app.get('/posts', async (req, res) => {
  const limit = Math.min(parseInt(req.query.limit) || 20, 100);
  const cursor = req.query.cursor;
  
  const posts = await Post.findAll({
    where: cursor ? { id: { $gt: cursor } } : {},
    limit: limit + 1
  });
  
  const hasMore = posts.length > limit;
  if (hasMore) posts.pop();
  
  res.json({
    data: posts,
    cursor: posts[posts.length - 1]?.id,
    hasMore
  });
});

// 3. Field Selection (reduce payload)
app.get('/users/:id', async (req, res) => {
  const fields = req.query.fields?.split(',') || ['id', 'name', 'avatar'];
  const user = await User.findById(req.params.id, { 
    attributes: fields 
  });
  res.json(user);
});

// 4. Conditional Requests (save bandwidth)
app.get('/posts', async (req, res) => {
  const etag = calculateETag(posts);
  
  if (req.headers['if-none-match'] === etag) {
    return res.status(304).end(); // Not Modified
  }
  
  res.set('ETag', etag);
  res.json(posts);
});

// 5. Batch Endpoints (reduce round trips)
app.post('/batch', async (req, res) => {
  const { requests } = req.body;
  
  const results = await Promise.all(
    requests.map(async (r) => {
      try {
        return await processRequest(r);
      } catch (error) {
        return { error: error.message };
      }
    })
  );
  
  res.json({ results });
});
```

**Push Notifications:**
```javascript
// Firebase Cloud Messaging (FCM)
const admin = require('firebase-admin');

async function sendPushNotification(userId, message) {
  // Get user's device tokens
  const tokens = await DeviceToken.findAll({ userId });
  
  const message = {
    notification: {
      title: 'New Order',
      body: 'Your order has been shipped!',
      imageUrl: 'https://example.com/image.jpg'
    },
    data: {
      orderId: '12345',
      type: 'order_shipped'
    },
    tokens: tokens.map(t => t.token)
  };
  
  const response = await admin.messaging().sendMulticast(message);
  
  // Remove invalid tokens
  if (response.failureCount > 0) {
    const failedTokens = [];
    response.responses.forEach((resp, idx) => {
      if (!resp.success) {
        failedTokens.push(tokens[idx].token);
      }
    });
    await DeviceToken.destroy({ where: { token: failedTokens } });
  }
}
```

**Offline Support:**
```javascript
// Optimistic updates + sync queue
app.post('/posts', async (req, res) => {
  const { temp_id, ...postData } = req.body;
  
  const post = await Post.create(postData);
  
  // Return temp_id mapping
  res.json({
    temp_id,
    post
  });
});

// Sync endpoint for offline changes
app.post('/sync', async (req, res) => {
  const { changes } = req.body;
  
  const results = await Promise.all(
    changes.map(async (change) => {
      switch (change.action) {
        case 'create':
          return await createResource(change);
        case 'update':
          return await updateResource(change);
        case 'delete':
          return await deleteResource(change);
      }
    })
  );
  
  res.json({ results });
});
```

#### CDN & Edge Computing

**CDN Benefits:**
```
1. Reduced Latency
   - Content served from nearest edge location
   - Users in Asia get content from Asia servers

2. Reduced Load on Origin
   - Cache static assets
   - Only cache miss hits origin

3. DDoS Protection
   - Distributed network absorbs attacks
   - WAF (Web Application Firewall)

4. Cost Savings
   - Bandwidth cheaper at CDN
   - Reduced origin infrastructure
```

**CloudFront Configuration:**
```javascript
// Terraform
resource "aws_cloudfront_distribution" "main" {
  origin {
    domain_name = aws_s3_bucket.assets.bucket_regional_domain_name
    origin_id   = "S3-assets"
    
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path
    }
  }
  
  enabled             = true
  default_root_object = "index.html"
  
  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-assets"
    
    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
    
    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600    # 1 hour
    max_ttl                = 86400   # 24 hours
    compress               = true
  }
  
  # Cache API responses
  ordered_cache_behavior {
    path_pattern     = "/api/*"
    allowed_methods  = ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "API-origin"
    
    forwarded_values {
      query_string = true
      headers      = ["Authorization", "Accept"]
      cookies {
        forward = "all"
      }
    }
    
    min_ttl                = 0
    default_ttl            = 0       # No caching for API
    max_ttl                = 0
  }
  
  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
  
  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate.cert.arn
    ssl_support_method  = "sni-only"
  }
}
```

**Edge Functions (Lambda@Edge, CloudFlare Workers):**
```javascript
// CloudFlare Worker - modify response at edge
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // A/B testing at edge
  const experiment = Math.random() < 0.5 ? 'A' : 'B';
  
  const response = await fetch(request);
  
  // Modify response
  const newResponse = new Response(response.body, response);
  newResponse.headers.set('X-Experiment', experiment);
  newResponse.headers.set('X-CDN', 'Cloudflare');
  
  return newResponse;
}

// Authentication at edge
async function authenticate(request) {
  const token = request.headers.get('Authorization');
  
  if (!token) {
    return new Response('Unauthorized', { status: 401 });
  }
  
  // Verify JWT at edge
  try {
    const payload = await verifyJWT(token);
    request.headers.set('X-User-Id', payload.userId);
    return await fetch(request);
  } catch (err) {
    return new Response('Invalid token', { status: 401 });
  }
}
```

**Cache Strategies:**
```javascript
// Set cache headers
app.get('/products/:id', async (req, res) => {
  const product = await Product.findById(req.params.id);
  
  // Cache for 1 hour, allow stale for 1 day
  res.set('Cache-Control', 'public, max-age=3600, stale-while-revalidate=86400');
  res.set('ETag', calculateETag(product));
  
  res.json(product);
});

// Vary by query params
app.get('/search', async (req, res) => {
  const results = await search(req.query);
  
  // Cache separately for each query
  res.set('Cache-Control', 'public, max-age=300');
  res.set('Vary', 'Accept-Encoding');
  
  res.json(results);
});

// No cache for personalized content
app.get('/recommendations', async (req, res) => {
  const recs = await getRecommendations(req.user.id);
  
  res.set('Cache-Control', 'private, no-cache');
  res.json(recs);
});
```

**Cache Invalidation:**
```javascript
// Invalidate CloudFront cache
const cloudfront = new AWS.CloudFront();

async function invalidateCache(paths) {
  await cloudfront.createInvalidation({
    DistributionId: 'DISTRIBUTION_ID',
    InvalidationBatch: {
      CallerReference: Date.now().toString(),
      Paths: {
        Quantity: paths.length,
        Items: paths // ['/products/*', '/index.html']
      }
    }
  }).promise();
}

// On product update
app.put('/products/:id', async (req, res) => {
  const product = await Product.update(req.params.id, req.body);
  
  // Invalidate CDN cache
  await invalidateCache([
    `/products/${req.params.id}`,
    '/products'
  ]);
  
  res.json(product);
});
```

### Soft Skills

#### 1. System Design Thinking
- Ask clarifying questions
- Define requirements (functional & non-functional)
- Estimate scale (back-of-envelope calculations)
- Start high-level, then deep dive
- Discuss trade-offs
- Consider bottlenecks

#### 2. Communication
- Document decisions (ADR - Architecture Decision Records)
- Write clear commit messages
- Code reviews: constructive feedback
- Technical writing (documentation, blog posts)

#### 3. Learning & Growth
- Follow tech blogs/newsletters
- Read source code of popular libraries
- Contribute to open source
- Build side projects
- Attend conferences/meetups
- Teach others (blog, mentor)

---

## ⚙️ Node.js Internals & Performance

Bu bölüm bir Node.js senior backend developer'ın mutlaka bilmesi gereken runtime iç yapılarını kapsar. Lambda, Express, Fastify ne kullanırsan kullan — altta hep **V8 + libuv + Event Loop** çalışır.

### Event Loop Derinlemesine 🔄

```
Node.js Event Loop FAZLARİ (libuv):

  ┌───────────────────────────────┐
  │         TIMERS                │ → setTimeout, setInterval callback'leri
  │  (min-heap sıralı)           │
  ├───────────────────────────────┤
  │    PENDING CALLBACKS          │ → Önceki döngüden ertelenmiş I/O callback'leri
  ├───────────────────────────────┤
  │    IDLE, PREPARE              │ → İç kullanım (Node internal)
  ├───────────────────────────────┤
  │         POLL                  │ → Yeni I/O event'leri al, I/O callback'lerini çalıştır
  │  (En çok zaman burada geçer) │   Eğer queue boşsa ve timer varsa → Timers'a git
  ├───────────────────────────────┤
  │         CHECK                 │ → setImmediate() callback'leri
  ├───────────────────────────────┤
  │    CLOSE CALLBACKS            │ → socket.on('close', ...) gibi
  └───────────────────────────────┘

  HER FAZ ARASINDA:
    → process.nextTick() kuyruğu BOŞALTILIR (microtask)
    → Promise.then() kuyruğu BOŞALTILIR (microtask)
    → nextTick > Promise öncelikli!
```

```javascript
// 🧪 Event Loop Sıralama Testi — Bu çıktıyı TAHMIN ET!
console.log('1: Script başladı');

setTimeout(() => console.log('2: setTimeout'), 0);
setImmediate(() => console.log('3: setImmediate'));

Promise.resolve().then(() => console.log('4: Promise.then'));
process.nextTick(() => console.log('5: nextTick'));

console.log('6: Script bitti');

// ÇIKTI:
// 1: Script başladı
// 6: Script bitti
// 5: nextTick        ← microtask, EN YÜKSEK öncelik
// 4: Promise.then    ← microtask, nextTick'ten sonra
// 2: setTimeout      ← Timer fazı (veya 3 önce gelebilir - belirsiz!)
// 3: setImmediate    ← Check fazı (veya 2 önce gelebilir - belirsiz!)
```

### V8 Engine & Memory Management 🧠

```
V8 Bellek Yapısı:

  HEAP MEMORY:
  ┌──────────────────────────────────────┐
  │ NEW SPACE (Young Generation)         │ → Kısa ömürlü objeler
  │   Semi-space A ←→ Semi-space B       │ → Scavenger GC (çok hızlı, ~1ms)
  │   Default: 16MB (64-bit)             │
  ├──────────────────────────────────────┤
  │ OLD SPACE (Old Generation)           │ → Uzun ömürlü objeler
  │   Default: ~1.5GB (64-bit)           │ → Mark-Sweep-Compact GC (yavaş)
  │   --max-old-space-size=4096          │ → Production'da artır!
  ├──────────────────────────────────────┤
  │ LARGE OBJECT SPACE                   │ → Büyük array/buffer'lar
  │ CODE SPACE                           │ → JIT compiled kod (TurboFan)
  │ MAP SPACE                            │ → Hidden class'lar
  └──────────────────────────────────────┘
```

```javascript
// 🔍 Memory Leak Tespiti
const v8 = require('v8');

// Heap snapshot al
function logMemory() {
  const stats = v8.getHeapStatistics();
  console.log({
    heapUsed: `${(stats.used_heap_size / 1024 / 1024).toFixed(1)} MB`,
    heapTotal: `${(stats.total_heap_size / 1024 / 1024).toFixed(1)} MB`,
    external: `${(stats.external_memory / 1024 / 1024).toFixed(1)} MB`,
  });
}

// ❌ MEMORY LEAK ÖRNEĞİ:
const cache = new Map(); // Asla temizlenmiyor!

async function handleRequest(req) {
  const data = await fetchData(req.id);
  cache.set(req.id, data); // Sonsuza kadar büyür! 💀
  return data;
}

// ✅ DOĞRU: WeakRef veya TTL ile
const cache2 = new Map();

function setWithTTL(key, value, ttlMs = 60000) {
  cache2.set(key, { value, expires: Date.now() + ttlMs });
  setTimeout(() => cache2.delete(key), ttlMs);
}

// ✅ VEYA: LRU Cache kullan
const LRU = require('lru-cache');
const cache3 = new LRU({ max: 500, ttl: 1000 * 60 * 5 });
```

### Worker Threads & Cluster Module 🧵

```javascript
// CPU-yoğun işleri MAIN THREAD'den çıkar!
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');

if (isMainThread) {
  // Ana thread — HTTP isteklerini handle eder
  async function processImage(imagePath) {
    return new Promise((resolve, reject) => {
      const worker = new Worker(__filename, {
        workerData: { imagePath }
      });
      worker.on('message', resolve);
      worker.on('error', reject);
    });
  }

  // Express route'da kullan
  app.post('/resize', async (req, res) => {
    const result = await processImage(req.body.path);
    res.json(result); // Main thread BLOKLANMADI! ✅
  });

} else {
  // Worker thread — CPU-yoğun iş burada
  const { imagePath } = workerData;
  const result = heavyImageProcessing(imagePath); // 2 saniye sürse bile OK
  parentPort.postMessage(result);
}
```

```javascript
// Cluster Module — Multi-core kullanımı
const cluster = require('cluster');
const os = require('os');

if (cluster.isPrimary) {
  const numCPUs = os.cpus().length;
  console.log(`Primary ${process.pid}: ${numCPUs} worker başlatılıyor...`);

  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} öldü, yenisi başlatılıyor...`);
    cluster.fork(); // Auto-restart! ✅
  });
} else {
  // Her worker kendi HTTP server'ını dinler
  const app = require('./app');
  app.listen(3000);
  console.log(`Worker ${process.pid} başladı`);
}

// NOT: Production'da PM2 veya Kubernetes tercih et
// cluster.fork() yerine → pm2 start app.js -i max
```

### Streams & Backpressure 🌊

```javascript
// Streams — Büyük dosyaları bellek DOLDURMADAN işle

// ❌ KÖTÜ: Tüm dosyayı RAM'e al
const fs = require('fs');
const data = fs.readFileSync('10GB-file.csv'); // 💀 BOOM! OutOfMemory!

// ✅ İYİ: Stream ile parça parça oku
const readline = require('readline');

async function processLargeFile(filePath) {
  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({ input: fileStream });

  let lineCount = 0;
  for await (const line of rl) {
    // Her satırı tek tek işle — RAM kullanımı SABİT kalır!
    await processLine(line);
    lineCount++;
    if (lineCount % 100000 === 0) {
      console.log(`${lineCount} satır işlendi...`);
    }
  }
  console.log(`Toplam: ${lineCount} satır`);
}

// ✅ Transform Stream — veri dönüşümü
const { Transform } = require('stream');

const csvToJson = new Transform({
  objectMode: true,
  transform(chunk, encoding, callback) {
    const line = chunk.toString().trim();
    const [name, age, city] = line.split(',');
    callback(null, { name, age: parseInt(age), city });
  }
});

// Pipeline ile backpressure otomatik yönetilir!
const { pipeline } = require('stream/promises');
await pipeline(
  fs.createReadStream('users.csv'),
  csvToJson,
  async function* (source) {
    for await (const user of source) {
      yield JSON.stringify(user) + '\n';
    }
  },
  fs.createWriteStream('users.jsonl')
);
```

### Error Handling Patterns 🚨

```javascript
// Senior seviye error handling:

// 1. Custom Error Hierarchy
class AppError extends Error {
  constructor(message, statusCode, errorCode, isOperational = true) {
    super(message);
    this.statusCode = statusCode;
    this.errorCode = errorCode;
    this.isOperational = isOperational; // Operational vs Programming error
    Error.captureStackTrace(this, this.constructor);
  }
}

class NotFoundError extends AppError {
  constructor(resource, id) {
    super(`${resource} with id ${id} not found`, 404, 'RESOURCE_NOT_FOUND');
  }
}

class ValidationError extends AppError {
  constructor(details) {
    super('Validation failed', 400, 'VALIDATION_ERROR');
    this.details = details;
  }
}

class ExternalServiceError extends AppError {
  constructor(service, originalError) {
    super(`${service} service failed`, 502, 'EXTERNAL_SERVICE_ERROR');
    this.service = service;
    this.originalError = originalError;
  }
}

// 2. Global Error Handler (Fastify)
app.setErrorHandler((error, request, reply) => {
  // Operational error → client'a anlamlı cevap
  if (error.isOperational) {
    return reply.status(error.statusCode).send({
      error: error.errorCode,
      message: error.message,
      ...(error.details && { details: error.details }),
    });
  }

  // Programming error → logla ve generic cevap ver
  logger.error({ err: error, requestId: request.id }, 'Unhandled error');
  return reply.status(500).send({
    error: 'INTERNAL_ERROR',
    message: 'An unexpected error occurred',
  });
});

// 3. Unhandled Rejection / Exception (Process Level)
process.on('unhandledRejection', (reason) => {
  logger.fatal({ err: reason }, 'Unhandled Rejection — shutting down');
  process.exit(1); // PM2 veya K8s restart edecek
});

process.on('uncaughtException', (error) => {
  logger.fatal({ err: error }, 'Uncaught Exception — shutting down');
  process.exit(1); // ASLA devam etme, state corrupted olabilir!
});

// 4. Retry with Exponential Backoff
async function withRetry(fn, { maxRetries = 3, baseDelay = 1000 } = {}) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === maxRetries) throw error;
      const delay = baseDelay * Math.pow(2, attempt - 1) + Math.random() * 1000;
      logger.warn({ attempt, delay, error: error.message }, 'Retrying...');
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

// Kullanım:
const result = await withRetry(() => axios.get('https://api.example.com/data'), {
  maxRetries: 3,
  baseDelay: 500,
});
```

### Caching Patterns 🗄️

```javascript
// Senior backend dev'in bilmesi gereken 4 caching pattern:

// 1. CACHE-ASIDE (Lazy Loading) — En yaygın
async function getUser(userId) {
  // Önce cache'e bak
  const cached = await redis.get(`user:${userId}`);
  if (cached) return JSON.parse(cached);

  // Cache miss → DB'den al
  const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);
  
  // Cache'e yaz (TTL ile!)
  await redis.set(`user:${userId}`, JSON.stringify(user), 'EX', 300);
  return user;
}

// 2. WRITE-THROUGH — Her yazma işleminde cache güncelle
async function updateUser(userId, data) {
  const user = await db.query(
    'UPDATE users SET name = $1 WHERE id = $2 RETURNING *',
    [data.name, userId]
  );
  await redis.set(`user:${userId}`, JSON.stringify(user), 'EX', 300);
  return user;
}

// 3. WRITE-BEHIND (Write-Back) — Cache'e yaz, DB'ye async yaz
class WriteBackCache {
  constructor() {
    this.pendingWrites = new Map();
    setInterval(() => this.flush(), 5000); // 5 sn'de bir DB'ye flush
  }

  async set(key, value) {
    await redis.set(key, JSON.stringify(value));
    this.pendingWrites.set(key, value);
  }

  async flush() {
    for (const [key, value] of this.pendingWrites) {
      await db.query('UPDATE users SET data = $1 WHERE id = $2', [value, key]);
    }
    this.pendingWrites.clear();
  }
}

// 4. Cache Invalidation Stratejileri
// "There are only two hard things in CS: cache invalidation and naming things."

// Time-based: TTL ile otomatik expire
// Event-based: DB değiştiğinde event ile cache temizle
// Version-based: Cache key'e versiyon ekle → user:v2:123
```

---

## 🤖 Yapay Zeka Çağında Backend Engineering

### AI Backend Developer'ın İşini Nasıl Değiştiriyor?

```
2025-2026'da Senior Backend Developer'ın AI ile ilişkisi:

  ✅ AI'ın GÜÇLÜ olduğu alanlar:
     → Boilerplate kod üretme (CRUD, schema, test)
     → Bug tespiti ve fix önerisi
     → Code review yardımcısı
     → Dokümantasyon oluşturma
     → SQL sorgusu optimizasyonu

  ❌ AI'ın ZAYIF olduğu alanlar (SEN yapmalısın):
     → Mimari kararlar (hangi pattern, hangi DB, hangi queue?)
     → Domain modelleme (iş kurallarını anlamak)
     → Performance tuning (profiling, bottleneck analizi)
     → Güvenlik mimarisi (threat modeling)
     → Trade-off analizi (consistency vs availability)
     → Ekip liderliği ve teknik vizyon
```

### Backend'de AI Entegrasyonu 🧠

```javascript
// 1. LLM API Entegrasyonu (OpenAI / Anthropic)
const { OpenAI } = require('openai');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function summarizeText(text) {
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'system', content: 'Kısa ve öz özetle.' },
      { role: 'user', content: text },
    ],
    max_tokens: 200,
    temperature: 0.3,
  });
  return response.choices[0].message.content;
}

// 2. RAG (Retrieval-Augmented Generation) Pattern
async function ragQuery(question) {
  // Step 1: Soruyu vektöre çevir
  const embedding = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: question,
  });

  // Step 2: Vector DB'de en yakın dokümanları bul
  const relevantDocs = await vectorDb.query({
    vector: embedding.data[0].embedding,
    topK: 5,
  });

  // Step 3: Context + soru ile LLM'e sor
  const context = relevantDocs.map(d => d.text).join('\n\n');
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'system', content: `Context:\n${context}\n\nBu context'e dayanarak cevapla.` },
      { role: 'user', content: question },
    ],
  });
  return response.choices[0].message.content;
}

// 3. AI Gateway Pattern — Rate limit, caching, fallback
class AIGateway {
  constructor() {
    this.providers = {
      primary: new OpenAI({ apiKey: process.env.OPENAI_KEY }),
      fallback: new Anthropic({ apiKey: process.env.ANTHROPIC_KEY }),
    };
    this.cache = new LRU({ max: 1000, ttl: 1000 * 60 * 10 });
  }

  async complete(prompt, options = {}) {
    // Cache check
    const cacheKey = `${prompt}:${JSON.stringify(options)}`;
    const cached = this.cache.get(cacheKey);
    if (cached) return cached;

    try {
      // Primary provider
      const result = await this.providers.primary.chat.completions.create({
        model: options.model || 'gpt-4o-mini',
        messages: [{ role: 'user', content: prompt }],
      });
      const response = result.choices[0].message.content;
      this.cache.set(cacheKey, response);
      return response;
    } catch (error) {
      // Fallback provider
      logger.warn({ error }, 'Primary AI failed, trying fallback');
      const result = await this.providers.fallback.messages.create({
        model: 'claude-sonnet-4-20250514',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 1024,
      });
      return result.content[0].text;
    }
  }
}
```

### Senior Dev İçin AI Prompt Şablonları

```
KOD REVIEW:
  "Bu Node.js kodunu senior backend developer perspektifinden incele:
   - Error handling eksik mi?
   - Memory leak riski var mı?
   - Race condition var mı?
   - N+1 query problemi var mı?
   - Proper logging var mı?
   - Input validation yeterli mi?"

MİMARİ KARAR:
  "Bu backend servisini tasarlıyorum:
   [servis açıklaması]
   
   Şu trade-off'ları analiz et:
   - SQL vs NoSQL
   - Sync vs Async iletişim
   - Monolith vs Microservice
   - Redis cache vs in-memory cache
   - REST vs gRPC vs GraphQL
   
   Her seçenek için pro/con listesi ver."

PERFORMANCE:
  "Bu Node.js API endpoint'i yavaş (P99: 2 saniye).
   [kodu göster]
   Olası bottleneck'ları analiz et:
   - DB query optimization
   - N+1 query detection
   - Unnecessary serialization
   - Missing index
   - Blocking operation on event loop
   - Memory allocation pattern"
```

---

## 📚 Öğrenme Kaynakları

### Books
```
Architecture & Design:
- Designing Data-Intensive Applications (Martin Kleppmann) ⭐
- System Design Interview (Alex Xu) ⭐
- Clean Architecture (Robert C. Martin)
- Domain-Driven Design (Eric Evans)
- Building Microservices (Sam Newman)
- Site Reliability Engineering (Google)
- The Phoenix Project (Gene Kim) - DevOps novel

Code Quality:
- Clean Code (Robert C. Martin) ⭐
- Refactoring (Martin Fowler)
- The Pragmatic Programmer (Hunt & Thomas)
- Working Effectively with Legacy Code (Michael Feathers)

Distributed Systems:
- Distributed Systems (Maarten van Steen)
- Database Internals (Alex Petrov)
- Release It! (Michael Nygard) - Production readiness

Leadership:
- The Manager's Path (Camille Fournier)
- Staff Engineer (Will Larson)
- An Elegant Puzzle (Will Larson)
```

### Online Platforms
```
Courses:
- System Design: educative.io, ByteByteGo, ExponentHQ
- AWS: A Cloud Guru, AWS Training, Stephane Maarek (Udemy)
- Kubernetes: KodeKloud, Linux Academy
- Algorithms: LeetCode, AlgoExpert, NeetCode

Newsletters:
- ByteByteGo (System Design)
- High Scalability
- AWS News Blog
- DevOps Weekly
- Software Lead Weekly
- Pointer.io
- TLDR Newsletter

YouTube Channels:
- Hussein Nasser (Backend Engineering)
- ByteByteGo
- Fireship
- Web Dev Simplified
- Tech Dummies (Narendra L)

Blogs:
- Martin Fowler (martinfowler.com)
- Netflix Tech Blog
- Uber Engineering
- Airbnb Engineering
- AWS Architecture Blog
```

### Practice
```
1. Build a mini-CRM from scratch
2. Implement a message queue (RabbitMQ clone)
3. Create a distributed cache (Redis clone)
4. Build a URL shortener with analytics
5. Design e-commerce platform with microservices
6. Create a real-time chat application
7. Build an API gateway with rate limiting
8. Implement a task scheduler (Cron clone)
9. Create a search engine (mini-Elasticsearch)
10. Build a streaming platform (mini-Netflix)
```

### Communities & Networking
```
- Dev.to
- Hashnode
- Reddit: r/backend, r/devops, r/kubernetes
- Discord: Programming communities
- Local meetups & conferences
- Tech Twitter
- GitHub discussions
```

---

## 🗺️ Gelişim Yol Haritası

### Level 1: Junior Developer ✅ (Completed)
- Basic CRUD operations
- REST APIs
- SQL basics
- Git fundamentals

### Level 2: Mid-Level Developer ✅ (Completed)
- Lambda, SQS, SNS kullanımı
- Testing practices
- Design patterns
- API design

### Level 3: Senior Developer (Current Goal)

**Teknik Beceriler:**

**Infrastructure & DevOps:**
- [ ] EC2, VPC, networking derinlemesine
- [ ] Kubernetes fundamentals (Pods, Deployments, Services)
- [ ] Terraform/CloudFormation ile IaC
- [ ] CI/CD pipeline setup (GitLab/GitHub Actions)
- [ ] Docker containerization best practices

**Architecture & Design:**
- [ ] Microservices architecture & trade-offs
- [ ] Event-driven design (SQS, SNS, Kafka)
- [ ] API design (REST, GraphQL, gRPC)
- [ ] Design patterns (Repository, Factory, Strategy, etc.)
- [ ] CQRS & Event Sourcing patterns
- [ ] Service mesh basics (Istio/Linkerd)

**Database & Caching:**
- [ ] PostgreSQL advanced (JSONB, full-text search, partitioning)
- [ ] Database optimization (indexing, query tuning)
- [ ] Redis advanced use cases
- [ ] Sharding & replication strategies
- [ ] Elasticsearch for search

**Deployment & Reliability:**
- [ ] Deployment strategies (Blue-Green, Canary, Rolling)
- [ ] GitOps (ArgoCD/Flux)
- [ ] Feature flags implementation
- [ ] Monitoring & observability (Prometheus, Grafana, X-Ray)
- [ ] Incident management & on-call

**Security:**
- [ ] Authentication & authorization (JWT, OAuth, RBAC)
- [ ] Security best practices (OWASP Top 10)
- [ ] Secret management
- [ ] Rate limiting & DDoS protection

**Advanced Topics:**
- [ ] Multi-tenancy patterns
- [ ] Real-time communication (WebSockets, SSE)
- [ ] CDN & edge computing
- [ ] Mobile backend considerations

**Soft Skills:**
- [ ] System design interviews (5+ practice sessions)
- [ ] Code review best practices
- [ ] Technical documentation (ADRs)
- [ ] Mentoring junior developers
- [ ] Architecture decision making
- [ ] Tech debt management
- [ ] Incident post-mortems

**Completed:**
- ✅ Lambda, SQS, SNS kullanımı
- ✅ Basic testing practices
- ✅ Design patterns basics
- ✅ REST API design

### Level 4: Staff/Principal Engineer (Future)

**Technical Leadership:**
- Multi-region deployment & disaster recovery
- Performance optimization at scale
- Cost optimization strategies
- Chaos engineering practices
- Technical strategy & roadmap

**People & Process:**
- Cross-team collaboration & influence
- Architecture review boards
- Technical mentorship program
- Engineering culture building

**Industry Impact:**
- Conference talks & presentations
- Technical blog writing
- Open source contributions
- Leading industry initiatives

---

## ✅ Özet & Aksiyon Planı

### Detaylı 16 Haftalık Program

**🎯 Hafta 1-2: Infrastructure Fundamentals**
- [ ] EC2 instance başlat, security groups yapılandır
- [ ] VPC oluştur (public/private subnets, NAT gateway)
- [ ] Load balancer setup (ALB)
- [ ] Auto Scaling Group kur
- [ ] Terraform ile yukarıdakileri kodla
- **Proje:** Blog hosting infrastructure

**🎯 Hafta 3-4: Kubernetes Basics**
- [ ] Local k8s cluster (minikube/kind)
- [ ] Pod, Deployment, Service kavramları
- [ ] ConfigMap & Secret kullanımı
- [ ] Ingress controller setup
- [ ] Helm chart oluşturma
- **Proje:** Microservice deployment to k8s

**🎯 Hafta 5-6: Event-Driven Architecture**
- [ ] SQS deep dive (FIFO, DLQ)
- [ ] SNS ile fan-out pattern
- [ ] EventBridge scheduled events
- [ ] Saga pattern implementation
- [ ] Dead letter queue handling
- **Proje:** E-commerce order processing system

**🎯 Hafta 7-8: API Design & Communication**
- [ ] REST API best practices
- [ ] GraphQL server setup
- [ ] gRPC service implementation
- [ ] API versioning strategies
- [ ] WebSocket real-time updates
- **Proje:** Multi-protocol API gateway

**🎯 Hafta 9-10: Database & Search**
- [ ] PostgreSQL JSONB, full-text search
- [ ] Query optimization & EXPLAIN
- [ ] Database indexing strategies
- [ ] Redis caching patterns
- [ ] Elasticsearch setup & search implementation
- **Proje:** Product search engine

**🎯 Hafta 11-12: Monitoring & Observability**
- [ ] Prometheus metrics setup
- [ ] Grafana dashboards
- [ ] Distributed tracing (Jaeger/X-Ray)
- [ ] Structured logging (ELK stack)
- [ ] Alert configuration
- **Proje:** Complete observability stack

**🎯 Hafta 13-14: Deployment & GitOps**
- [ ] Blue-Green deployment
- [ ] Canary deployment with Flagger
- [ ] Feature flags implementation
- [ ] ArgoCD setup
- [ ] CI/CD pipeline optimization
- **Proje:** Zero-downtime deployment pipeline

**🎯 Hafta 15-16: Production Excellence**
- [ ] Incident management playbook
- [ ] On-call rotation setup
- [ ] Chaos engineering experiment
- [ ] Cost optimization analysis
- [ ] Disaster recovery plan
- [ ] Post-mortem documentation
- **Proje:** Production readiness checklist

### Her Hafta Yapılacaklar

**Daily:**
- 1 saat hands-on practice
- Code reading (30 min)
- Tech article/documentation (20 min)

**Weekly:**
- 1 side project commit
- 1 blog post/notes
- 1 system design practice
- Review week's learning

**Monthly:**
- 1 tech talk izle
- 1 post-mortem oku
- 1 open source contribution
- Portfolio review & update

### Tavsiyeler & İpuçları

**1. Öğrenme Stratejisi:**
- ❌ Tutorial hell'den kaçının
- ✅ Build real projects
- ✅ Her konuyu production-ready olarak implemente edin
- ✅ Break things, fix them, learn

**2. Dokümantasyon:**
- Personal wiki (Notion, Obsidian)
- TIL (Today I Learned) journal
- Code snippets repository
- Architecture diagrams

**3. Networking:**
- Twitter'da tech leaders follow edin
- Discord/Slack communities'e katılın
- Local meetup'lara gidin
- Mentorship bulun (hem mentor, hem mentee olarak)

**4. İş Hayatında:**
- Production incidents'tan öğrenin
- Code review'larda aktif olun
- Tech debt için advocacy yapın
- Knowledge sharing sessions organize edin

**5. Portfolio:**
- GitHub'da public projects
- Medium/Dev.to blog
- System design diagrams
- Contribution history

### Kritik Kilometre Taşları

**3 Ay Sonra:**
- ✅ Kubernetes'e microservice deploy edebiliyorum
- ✅ Event-driven architecture tasarlayabiliyorum
- ✅ Production issue'ları debug edebiliyorum
- ✅ System design interview'e hazırım

**6 Ay Sonra:**
- ✅ Complete CI/CD pipeline kurabiliyorum
- ✅ Monitoring stack setup edebiliyorum
- ✅ Architecture decision verebiliyorum
- ✅ Junior developer mentor edebiliyorum

**12 Ay Sonra:**
- ✅ Multi-region architecture tasarlayabiliyorum
- ✅ Cost optimization yapabiliyorum
- ✅ Incident management lead edebiliyorum
- ✅ Tech talks verebiliyorum

### Kaynaklar Önceliklendirme

**Mutlaka Oku (Priority 1):**
1. Designing Data-Intensive Applications
2. System Design Interview - Alex Xu
3. Clean Code

**Sonra Oku (Priority 2):**
4. Building Microservices
5. Site Reliability Engineering
6. Domain-Driven Design

**İleri Seviye (Priority 3):**
7. Database Internals
8. Release It!
9. Staff Engineer

### Son Tavsiyeler

**Odaklan:**
- Breadth > Depth initially (genel görüntü)
- Sonra derinleş (özellikle ilgi alanın)
- T-shaped engineer ol (geniş bilgi + bir alan expert)

**Sabırlı Ol:**
- Senior olmak 3-5 yıl alır
- Her gün biraz ilerleme
- Burnout'tan kaçın
- Sustainable pace

**Pratik Yap:**
- Theory < Practice
- Fail fast, learn faster
- Production experience invaluable

**İletişim:**
- Teknik beceri yeterli değil
- Explain complex things simply
- Documentation MVP
- Collaboration > Solo hero

**Kendin Ol:**
- Başkalarıyla karşılaştırma
- Kendi yolunda ilerle
- Unique strengths'ini bul
- Continuous learning mindset

---

**Başarılar! 🚀**

*"The only way to do great work is to love what you do." - Steve Jobs*

**Bu doküman senin için özel olarak hazırlandı. Şimdi sıra uygulamada!**
