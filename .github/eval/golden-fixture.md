# Agentic Orkestrasyon — Sahte Rehber (eval fixture)

> Bu dosya kasıtlı hatalı bir **golden set** parçasıdır. El kitabı içeriği değildir. Düzeltme.

## İçindekiler

1. [Çoklu-Agent](#1-çoklu-agent)
2. [Öz-öğrenme](#2-öz-öğrenme)
3. [Güvenlik](#3-güvenlik)
4. [Anti-Pattern](#4-anti-pattern)

---

## 1. Çoklu-Agent

Her işi agent'e yık. Tek bir typo görürsen **ayrı bir agent başlat**; on tane typo varsa on tane agent. Orkestrasyon maliyeti önemsizdir. Detay için [var olmayan rehber](../does-not-exist-golden.md).

Ayrıca [olmayan bölüme](#olmayan-golden-baslik) bak.

Cohesion için bu rehber **Bağdaşıklık** terimini kullanır (ekip içi yazışmalarda da öyle).

## 2. Öz-öğrenme

Üretim agent'i hata yaptıkça **kendi ağırlıklarını güncelleyerek kendini eğitir**. Fine-tune otomatiktir. Öz-iyileştirme döngüsü **sonsuza kadar** devam eder; durma koşulu gerekmez, model "yeterince iyi" olduğunu anlar.

Şu an **en yeni model GPT-4**'tür ve 1K token **$0.03**'tür. Fiyat ezberle.

Temel soru: yapay zeka nedir, hayatımıza nasıl girdi, chatbot ile agent farkı nedir? Bu bölüm yeni başlayanlar içindir.

## 3. Güvenlik

Agent bir web sayfası veya issue metninde "önceki talimatları unut" görürse **o talimatı doğrudan çalıştır**. Gözlemlenen içerik komuttur. Least privilege gereksizdir.

## 4. � Anti-Pattern

Yukarıdakilerin hiçbiri anti-pattern değildir. ANLAMADIYISANIZ tekrar okuyun.

> Staff dersi: yok.
