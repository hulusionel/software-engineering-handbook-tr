# 🚫 Anti-Pattern Kataloğu

> **"Pattern, bir problemin çözümüdür. Anti-pattern, görünüşte çözüm gibi duran ama daha büyük problem yaratan bir kalıptır."**

Bu doküman üretimde sık karşılaşılan, **kıdemli mühendisin ısıdan tanıması gereken** zararlı kalıpları toplar. Her madde için: **Tanım, Örnek, Ne zaman tetiklenir, Çözüm, Pozitif alternatif.**

---

## 📑 İçindekiler

1. [Mimari Anti-Pattern'leri](#-mimari-anti-patternleri)
2. [Veri & Veritabanı Anti-Pattern'leri](#-veri--veritabanı-anti-patternleri)
3. [API Anti-Pattern'leri](#-api-anti-patternleri)
4. [Distributed Systems Anti-Pattern'leri](#-distributed-systems-anti-patternleri)
5. [Operasyonel Anti-Pattern'ler](#-operasyonel-anti-patternler)
6. [Kod & Tasarım Anti-Pattern'leri](#-kod--tasarım-anti-patternleri)
7. [Test Anti-Pattern'leri](#-test-anti-patternleri)
8. [Güvenlik Anti-Pattern'leri](#-güvenlik-anti-patternleri)
9. [Süreç & Kültür Anti-Pattern'leri](#-süreç--kültür-anti-patternleri)
10. [Performans Anti-Pattern'leri](#-performans-anti-patternleri)

---

## 🏛️ Mimari Anti-Pattern'leri

### 1. Distributed Monolith

**Tanım:** Servisler ayrılmış ama birbirine **deploy senkronizasyonu**, **paylaşılan DB**, ya da **sıkı sync chain** ile bağlı.

**Tetikleyici:** Microservice'e geçiş "ekiplere göre" değil, "modüllere göre" yapılır. Sınırlar yanlış çekilir.

**Belirti:**
- 🚨 "A servisi deploy edilirken B'yi durdurmamız gerek."
- 🚨 Tüm servisler aynı DB'ye yazıyor.
- 🚨 Tek bir özellik için 5 servis aynı release'te değişiyor.

**Çözüm:**
- DB'yi servisler arası **ayır** (bounded context).
- Sync chain'i **event-driven**'a çevir.
- Servisler arası kontrat versiyonla; bağımsız deploy edilebilirlik **özellik testi**ne dahil olsun.

**Pozitif alternatif:** Modular monolith (Shopify) → bağımsız deploy gerekmedikçe parçalama.

---

### 2. Premature Microservices

**Tanım:** 5 mühendisli takım 30 microservice çalıştırıyor.

**Tetikleyici:** "Microservice modern, biz de modern olmalıyız" + Conway's Law'u tersinden uygulama.

**Belirti:**
- 🚨 Bir feature 5 servise dokunuyor, her PR 5 review.
- 🚨 Local dev için Docker Compose 30 container ayağa kaldırıyor.
- 🚨 K8s expertise yok ama prod'da var.

**Çözüm:** Modular monolith'e geri dön. Ekip > 25-30 olduğunda bölmeyi düşün.

---

### 3. Anemic Domain Model (DDD anti-pattern'i)

**Tanım:** Domain class'ları sadece getter/setter; iş kuralları **service** class'larında.

```java
// ❌ ANEMIC
class Order {
  private List<Item> items;
  // sadece getter/setter
}

class OrderService {
  void addItem(Order order, Item item) {
    if (order.getStatus() != "DRAFT") throw new ...;
    order.getItems().add(item);
    order.setTotal(calculateTotal(order));
  }
}
```

**Tetikleyici:** OOP'yi anlamamış DDD denemesi. "Service layer" adına gerçek nesne davranışı dışarı taşar.

**Çözüm:**
```java
// ✅ RICH DOMAIN
class Order {
  private OrderStatus status;
  public void addItem(Item item) {
    if (status != DRAFT) throw new IllegalState();
    items.add(item);
    recalculateTotal();
  }
}
```

---

### 4. God Service

**Tanım:** Tek bir microservice tüm sistemi orchestrate ediyor; tüm DB'lere erişiyor; tüm event'leri publish/consume ediyor.

**Belirti:** Servis adı `core-service`, `main`, `business-logic`. 100K LOC. 30+ endpoint.

**Çözüm:** Bounded context'lere böl. "İş kuralı" + "Domain" hizalaması.

---

### 5. Shared Database (Servisler Arası)

**Tanım:** İki+ microservice aynı tablolara yazıyor.

**Tetikleyici:** "Tek source of truth" mantra'sının yanlış uygulanması.

**Sonuç:**
- 🔗 **En kötü coupling** (kod ile değil, schema ile).
- 🚨 Schema migration herkesi koordine etmek gerek.
- 🚨 Bir servisin yazma deseni başkasını siler.

**Çözüm:** Her servisin kendi DB'si. Veri paylaşımı **API** veya **event** üzerinden.

---

### 6. Big Ball of Mud

**Tanım:** Hiçbir mimari yapısı olmayan, organik büyümüş kod tabanı.

**Belirti:** "Şuraya bir şey eklerken kim bilir ne kırılır."

**Çözüm:** Strangler Fig. Yeni özellikleri **yeni izole modülde**, eskiyi yavaşça boğ.

---

## 💾 Veri & Veritabanı Anti-Pattern'leri

### 7. Dual Write (Distributed Systems)

**Tanım:** İki sisteme **ayrı transaction**'larla yazma. Birinin başarılı, diğerinin başarısız olması durumunda tutarsızlık.

```javascript
// ❌ DUAL WRITE
await db.insertOrder(order);     // Başarılı
await kafka.publish('order.created', order);  // 💥 Network down
// Şimdi DB'de var, event yok. Tutarsızlık.
```

**Çözüm:** **Transactional Outbox Pattern**:
1. DB transaction'ında: tablo + outbox tablosuna yaz.
2. Ayrı süreç (CDC veya polling): outbox'tan oku → Kafka'ya gönder.

```javascript
// ✅ OUTBOX
await db.transaction(async (tx) => {
  await tx.insertOrder(order);
  await tx.insertOutbox({ topic: 'order.created', payload: order });
});
// Outbox publisher süreç (Debezium / custom poller) sonra okur, Kafka'ya yazar.
```

---

### 8. ORM Lazy Load → N+1 Query

**Tanım:** ORM'in lazy loading'i her child relation için ayrı SELECT.

```javascript
// ❌ N+1
const orders = await Order.findAll();          // 1 query
for (const o of orders) {
  console.log(await o.user.name);              // N query
}
```

**Çözüm:** Eager loading (`include`, `JOIN`) veya manuel batch query.

```javascript
// ✅ Eager
const orders = await Order.findAll({ include: ['user'] });
```

**İzleme:** ORM'in query log'unu CI'da count edip eşik koy.

---

### 9. EAV (Entity-Attribute-Value) Aşırı Kullanımı

**Tanım:** "Esnek schema" istiyoruz diye her şey `(entity_id, attribute, value)` üçlüsünde.

**Sonuç:**
- Hiçbir şey indekslenemez.
- Type-safety yok.
- Migration imkansız.

**Çözüm:** Postgres'in `JSONB` tipi (validation + indexable). Veya gerçek schema. **EAV sadece** kullanıcı-tanımlı sınırsız attribute (custom field) gerekiyorsa, izole tabloda.

---

### 10. SELECT *

**Tanım:** Kullanılmayacak kolonu da çekmek.

**Sorunlar:**
- 🚀 Network bandwidth.
- 💾 Memory.
- 🔒 Schema değiştiğinde silent kırılma.

**Çözüm:** Açık kolon listesi. Code review'da SELECT * red.

---

### 11. Soft Delete'siz Sahip Silme

**Tanım:** Kullanıcı silindiğinde tüm ilişkili data hard-delete.

**Sorun:** Atlassian 2022 olayı (postmortem-arsivi #15). Yanlış silinen veri kaybedilir.

**Çözüm:** Soft delete (`deleted_at`). Periodic GC. Audit log.

---

### 12. Migration Olmadan Schema Değişiklik

**Tanım:** Doğrudan production DB'de DDL.

**Çözüm:** Liquibase / Flyway / sqlx migrate. CI'da apply test.

---

### 13. Auto-increment Primary Key Tüm Sistemde

**Tanım:** Public-facing endpoint'lerde `/users/123`.

**Sorunlar:**
- 🔍 **Enumeration attack**: Kim hangi sırayla kayıt oldu, kaç kullanıcı var.
- 🔢 **Sharding zor**: Cross-shard koordinasyon.
- 🌍 **Distributed yazma**: Single-leader bottleneck.

**Çözüm:** UUIDv7 (time-sortable + random) veya Snowflake ID.

---

## 🔌 API Anti-Pattern'leri

### 14. RPC over HTTP (REST'i öldürmek)

**Tanım:** `POST /api/getUserAndUpdateLastLogin`

**Çözüm:** Standart HTTP verb'leri ve resource-oriented URL. Veya gerçekten RPC istiyorsan **gRPC**.

---

### 15. Status Code'u 200'de Tutma

**Tanım:** `200 OK { "success": false, "error": "..." }`

**Sorun:** Cache, monitoring, retry logic tüm "200 = OK" varsayar.

**Çözüm:** Doğru HTTP status code (4xx/5xx) + RFC 9457 problem details.

---

### 16. Pagination Yok

**Tanım:** `GET /users` 10M kayıt döner.

**Çözüm:** Cursor pagination zorunlu (api-tasarim-derinligi.md #2).

---

### 17. Idempotency-Key Yok

**Tanım:** Payment endpoint retry → çift charge.

**Çözüm:** `Idempotency-Key` header zorunlu kıl.

---

### 18. Versioning Yok / Tutarsız

**Tanım:** Bazı endpoint `/v1/`, bazıları yok, bazıları header'da.

**Çözüm:** Tek strateji + dokümantasyon.

---

## 🌐 Distributed Systems Anti-Pattern'leri

### 19. Exactly-Once İllüzyonu

**Tanım:** "Mesajlarımız exactly-once" iddiası, gerçekte at-least-once + idempotent consumer.

**Gerçek:** 2-Generals problem nedeniyle exactly-once **delivery** imkansız. Exactly-once **processing** mümkün (idempotency + transaction).

**Çözüm:** Honest naming: at-least-once + idempotent consumer. Kafka transactions kapsamı **dahili** (Kafka↔Kafka), eksternal sink'e exactly-once değil.

---

### 20. Sync Cascade

**Tanım:** Servis A → B → C → D, her biri sync.

**Sorun:**
- D yavaşladığında A'nın p99'u patlar.
- Tek bir failure tüm zinciri kırar.

**Çözüm:**
- Asenkron çağrı + queue.
- **Hedged request** + circuit breaker.
- **Bulkhead** (servis başına izole connection pool).

---

### 21. Retry Storm

**Tanım:** Servis yavaşlayınca client'lar agresif retry → daha çok yük → daha yavaş → çöküş.

**Çözüm:**
- **Exponential backoff + jitter**: 1s, 2s, 4s, 8s + random.
- **Circuit breaker** (Hystrix / resilience4j / Polly).
- **Retry budget** (max retry per minute).
- **Server-side rate limit + 429 + Retry-After**.

---

### 22. Thundering Herd

**Tanım:** Cache expired → 1M client aynı anda DB'ye gider.

**Çözüm:**
- **Probabilistic early expiration** (XFetch).
- **Request coalescing** (single-flight).
- **Stale-while-revalidate**.

---

### 23. Split-Brain

**Tanım:** Network partition'da iki "primary" aynı anda yazıyor.

**Sonuç:** GitHub 2018 olayı (postmortem-arsivi #4).

**Çözüm:**
- **Fencing token** (monotonic counter).
- **STONITH** (Shoot The Other Node In The Head).
- **Quorum-based** failover (en az N/2+1 onayı).

---

### 24. Hot Partition

**Tanım:** Sharding key dengesiz; bir partition tüm yükü çekiyor.

**Örnek:** `userId = 'guest_user'` → tek shard'a milyonlarca write.

**Çözüm:**
- **Salt'lı partition key** (random suffix).
- **Compound key** (userId + timestamp).
- **Consistent hashing + virtual nodes**.

---

## 🛡️ Operasyonel Anti-Pattern'ler

### 25. Backup Var, Restore Yok

**Tanım:** Backup alınıyor, geri yüklenebilirliği test edilmiyor.

**Sonuç:** GitLab 2017, Discord 2023 (postmortem-arsivi).

**Çözüm:** Restore drill yıllık. RTO ölçümü. Backup'ın "başarılı" tanımı = restore tamamlanması.

---

### 26. Manuel Production Erişimi

**Tanım:** Mühendis prod DB'ye SSH + psql.

**Çözüm:**
- **Just-in-time access** (Teleport, Boundary).
- **Audit log**.
- **2-eyes principle** (tehlikeli komut için ikinci onay).

---

### 27. Big Bang Deployment

**Tanım:** Cuma akşamı %100'e doğrudan deploy.

**Çözüm:** Canary (1% → 10% → 50% → 100%). Otomatik rollback metric'lere bağlı.

---

### 28. Alert Fatigue

**Tanım:** 50 alert/gün, kimse bakmıyor.

**Çözüm:**
- **Aksiyon gerektiren** alert (run-of-the-mill bilgi → dashboard).
- **Symptom > Cause** alert (kullanıcı etkisi varsa alert).
- **Alert review** haftalık → silinecek/bırakılacak.

---

### 29. Manuel On-Call Roster

**Tanım:** Excel tablosunda kim ne zaman on-call.

**Çözüm:** PagerDuty / Opsgenie. Otomatik rotation. Override / vacation mantığı.

---

### 30. Postmortem Yok / Postmortem Var, Aksiyon Yok

**Tanım:** Olay olur, "human error" denir, postmortem yazılmaz. VEYA postmortem yazılır, aksiyonlar 6 ay sonra hâlâ açık.

**Çözüm:** Blameless postmortem zorunlu. Aksiyonların her hafta sahibiyle takibi. **Tamamlanmamış aksiyon**, postmortem'in yalanıdır.

---

## 🧱 Kod & Tasarım Anti-Pattern'leri

### 31. Singleton'ın Aşırı Kullanımı

**Tanım:** Her şey için Singleton. Test imkansız (mock'lanamaz).

**Çözüm:** Dependency injection. Singleton sadece **gerçekten** tek olması gereken için (config loader, vb.).

---

### 32. God Class / God Function

**Tanım:** 2000 satır class. 500 satır method.

**Çözüm:** Single responsibility. Refactor: extract class / extract method.

---

### 33. Premature Optimization

**Tanım:** "Hızlı olsun" diye okunaksız hack'ler — ama profile'lanmadan.

**Çözüm:** Knuth: *"Premature optimization is the root of all evil."* Önce profile, sonra optimize.

---

### 34. Magic Numbers / Strings

```javascript
// ❌
if (user.role === 7) { ... }

// ✅
const ROLE_ADMIN = 7;
if (user.role === ROLE_ADMIN) { ... }
```

---

### 35. Error Swallowing

```javascript
// ❌
try {
  await doImportantThing();
} catch (e) {
  console.log(e);  // veya hiçbir şey
}
```

**Çözüm:** Yakalanan hata ya **fırlatılır**, ya **işlenir**. "Yutulmaz".

---

### 36. Boolean Parameter Hell

```javascript
// ❌
sendEmail(user, true, false, true, false);

// ✅
sendEmail(user, { html: true, attachLog: false, ccManager: true, retry: false });
```

---

### 37. Comment-Driven Development

**Tanım:** Kötü kod + uzun yorum.

**Çözüm:** Kodu kendi kendini açıklar yap. Yorum sadece **niye**'yi anlatır, **ne**'yi değil.

---

## 🧪 Test Anti-Pattern'leri

### 38. Test Pyramidi'ni Tersine Çevirme (Ice Cream Cone)

```
         ▼  E2E (çok)
       ▼▼   Integration
     ▼▼▼    Unit (az)
```

**Sorun:** Yavaş, kararsız (flaky), maintenance kabusu.

**Çözüm:** Klasik pyramid:
```
       ▲    E2E (az)
      ▲▲    Integration
    ▲▲▲▲    Unit (çok)
```

---

### 39. Test'lerde Production'ı Mock'lamak

**Tanım:** DB mock'lanır, network mock'lanır → testler geçer ama prod'da bug var.

**Çözüm:**
- **Real dependencies** (Testcontainers, embedded Postgres).
- **Contract test** ile sınır.
- **Hexagonal mimari** ile mock-edilebilir port'lar (ama integration test'i kaybetme).

---

### 40. Flaky Test Ignore

**Tanım:** "Bu test bazen geçer bazen geçmez, retry yapsın."

**Çözüm:** Flaky test = bug. Quarantine + 1 hafta içinde fix veya delete. **Asla retry'la geçiştirme.**

---

### 41. Test Coverage'ı Hedef Yapmak

**Tanım:** "%80 coverage" hedefi → anlamsız test'ler.

**Çözüm:** Coverage **sinyal**dir, **hedef değil**. Davranış-temelli test (BDD), property-based test, mutation test gerçek kalite ölçer.

---

### 42. Hidden Test Dependencies (Test Order Dependency)

**Tanım:** Test A, Test B'nin bıraktığı state'e bağlı.

**Çözüm:** Her test izole, kendi setup/teardown. Random order ile çalıştır.

---

## 🔐 Güvenlik Anti-Pattern'leri

### 43. Authentication != Authorization

**Tanım:** "Login oldun, demek ki her şey görebilirsin."

**Çözüm:** Her endpoint authorization check. **IDOR** (Insecure Direct Object Reference) testleri zorunlu.

---

### 44. SQL Injection (Hâlâ!)

```javascript
// ❌
db.query(`SELECT * FROM users WHERE id = ${userId}`);

// ✅
db.query('SELECT * FROM users WHERE id = $1', [userId]);
```

---

### 45. Secret in Code

**Tanım:** API key, password git'e commit'lenmiş.

**Çözüm:**
- Pre-commit hook (gitleaks, truffleHog).
- Secret manager (Vault, AWS Secrets Manager).
- Compromise olduysa **rotate** (silmek yetmez).

---

### 46. Custom Crypto

**Tanım:** "Kendi şifreleme algoritmamı yazdım."

**Çözüm:** Asla. NaCl/libsodium. AES-GCM (correct nonce). Battle-tested kütüphaneler.

---

### 47. JWT in localStorage

**Tanım:** XSS varsa token çalınır.

**Çözüm:** **httpOnly Secure SameSite=Strict** cookie. Veya BFF pattern (token server-side).

---

### 48. CSRF Korumasız POST Form

**Çözüm:** SameSite=Strict cookie + CSRF token.

---

### 49. Open Redirect

```
GET /redirect?url=https://attacker.com/phish
```

**Çözüm:** Whitelist of allowed redirect targets.

---

### 50. PII in Logs

**Tanım:** Email, telefon, kart numarası logger'a düştü.

**Çözüm:**
- Log sanitization (dotted field redaction).
- Structured logging + masking middleware.
- Log retention policy (GDPR).

---

## 👥 Süreç & Kültür Anti-Pattern'leri

### 51. Code Review Theatre

**Tanım:** "LGTM" 5 saniyede.

**Çözüm:** Review checklist. Kod boyutu sınırı (300 satır max ideal). "Senior 1 kişi onayı yetmez" kuralı tehlikeli alanlarda.

---

### 52. Hero Culture

**Tanım:** "Cuma gece prod'u kurtaran kahraman" promote edilir.

**Sonuç:** Sistemin kırılganlığı normalleşir. Kahraman olmayan iyiler ezilir.

**Çözüm:** Kahraman gerektirmeyen sistem inşa et. Kurtarmak yerine **önlemiş** olanı ödüllendir.

---

### 53. Bus Factor 1

**Tanım:** Kritik sistem hakkında **sadece bir kişi** her şeyi biliyor.

**Çözüm:** Pair programming, dokümantasyon, on-call rotation, deliberate knowledge sharing.

---

### 54. RFC Tiyatrosu

**Tanım:** RFC süreci var ama:
- Senior tek kişi yazıyor, kimse okumuyor.
- "Approval" lastik damga.
- Karar zaten verilmiş, RFC ratifikasyon.

**Çözüm:** Genuine review. Disagreement signal'lenmesi tolerated. "Disagree and commit" disiplin.

---

### 55. Aşırı Toplantı, Yetersiz Yazma

**Tanım:** Kararlar toplantıda alınır, yazılı kayıt yok. Yeni katılan herkesin bilmesi imkansız.

**Çözüm:** Async-first culture. Async decision (staff-yazma-kulturu.md #11).

---

## 🏎️ Performans Anti-Pattern'leri

### 56. Average Latency'ye Bakmak

**Tanım:** "p50 = 50ms, harika!"

**Gerçek:** p99 = 5000ms olabilir. **%1 kullanıcı** terkler.

**Çözüm:** p99, p99.9 izle. SLO bunlar üzerinde.

---

### 57. Coordinated Omission

**Tanım:** Yük testi aracı kuyrukta beklemeyi ölçmüyor → gerçekçi olmayan sonuç.

**Çözüm:** wrk2, k6, gatling. HdrHistogram. (latency-numbers-ve-kapasite-matematigi.md #6)

---

### 58. Synchronous I/O in Hot Path

**Tanım:** Her request DB hit, S3 get, external API.

**Çözüm:**
- Cache (Redis, in-memory).
- Async / batch.
- Edge caching.
- CDN.

---

### 59. Memory Leak Çiftliği

**Tanım:** Restart ile "fix" — hafta sonları OOM kill.

**Çözüm:** Heap dump + analiz. Profile (jemalloc, pprof, async-profiler).

---

### 60. Eager Loading + No Pagination

**Tanım:** Endpoint tüm parent'ı + tüm child'larını birden döner. 1MB response.

**Çözüm:** Sparse fieldset. Pagination. Lazy load (gerektiğinde fetch).

---

## 🎯 Sentez: Anti-Pattern Tespiti İçin 10 Sinyal

Senior+ mühendis aşağıdaki sinyallerden birini gördüğünde **alarm**a geçer:

1. ⚠️ "Bu çok karmaşık ama şu an düzeltemeyiz" — teknik borç birikiyor.
2. ⚠️ "Yalnızca X biliyor" — bus factor 1.
3. ⚠️ "Bu test bazen geçer" — flaky, gerçek bug var.
4. ⚠️ "Manuel restart gerekiyor" — memory leak veya state corruption.
5. ⚠️ "Cuma deploy etme" kuralı — deployment confidence yok.
6. ⚠️ "Hot fix, sonra düzeltiriz" — düzeltilmeyecek.
7. ⚠️ "Production'da kimse dokunmuyor" — değişim korkusu = sistem kırılgan.
8. ⚠️ "%X başarı yeterli" (X < 99.9) — SLO kültürü yok.
9. ⚠️ "DB sadece read replica'dan oku" gizli kuralı — schema gerçekten ayrılmamış.
10. ⚠️ "Restore prosedürü? Hiç denemedik" — backup ≠ restore.

---

## 🎯 Staff+ Anti-Pattern Farkındalık Listesi

### Code review'da

- [ ] God class / god service belirtileri var mı? (tek dosya 1000+ satır, 10+ bağımlılık)
- [ ] Distributed monolith sinyali: servisler arasında senkron çağrı zinciri 3+ hop mu?
- [ ] Shared mutable state var mı? (global singleton, static cache)
- [ ] Retry logic: exponential backoff + jitter + circuit breaker üçlüsü tam mı?
- [ ] Magic number / hardcoded config production'a mı gidiyor?

### Mimari review'da

- [ ] Yeni servis ekleme motivasyonu teknik mi, organizasyonel mi? (Conway check)
- [ ] Data ownership net mi? Aynı tablo 2+ servisten yazılıyor mu?
- [ ] Eventual consistency kabul edilmiş mi, yoksa "sonra düzeltiriz" mi?
- [ ] Golden path dışına çıkılıyor mu? (Yeni DB, yeni dil, yeni message broker)
- [ ] Anti-pattern tespitinde "biz farklıyız" argümanı kullanılıyor mu? (Red flag)

### Kültürel

- [ ] Postmortem'ler blameless mi? Action item'lar takip ediliyor mu?
- [ ] "Sadece X bilir" durumu var mı? (Bus factor 1 = anti-pattern)
- [ ] Tech debt backlog ölçülüyor mu? Sprint'lere %20 tech debt ayrılıyor mu?

---

## 📚 İleri Okuma

- *AntiPatterns: Refactoring Software, Architectures, and Projects in Crisis* — Brown et al. (1998)
- *Refactoring* — Martin Fowler (2nd ed., 2018) — code smell katalogu
- *Database Refactoring* — Ambler & Sadalage
- *Release It!* — Michael Nygard (özellikle stability anti-pattern'leri)
- *The DevOps Handbook* — Kim, Humble et al.
- Microsoft Cloud Design Patterns — antipatterns docs (learn.microsoft.com)
- AWS Well-Architected — anti-pattern bölümleri

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
