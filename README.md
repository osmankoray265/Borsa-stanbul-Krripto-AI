# Borsa-Kripto-AI

---

# 📈 Borsa & Kripto AI Dashboard

**Streamlit** tabanlı, **Borsa İstanbul hisseleri**, **ABD hisseleri** ve **Kripto paralar** için
**canlı fiyat grafiği + haber tabanlı yapay zekâ duygu analizi** yapan interaktif analiz uygulaması.

---

## 🚀 Özellikler

* 📊 **Canlı Mum Grafiği (Candlestick)**
* 🤖 **Haberlerden AI Duygu Analizi**
* 🟢 Boğa / 🔴 Ayı / ⚪ Nötr piyasa tahmini
* 🇹🇷 Borsa İstanbul hisseleri desteği
* 🪙 Kripto paralar (BTC, ETH vb.)
* 🇺🇸 ABD hisseleri (AAPL, TSLA vb.)
* 📰 Türkçe haber tarama ve sıralama
* ⚡ Streamlit cache ile hızlı veri çekme
* 🧠 Plotly ile modern ve temiz grafikler

---

## 🧠 Yapay Zekâ Mantığı

* Haberler **sentiment_score** üzerinden analiz edilir
* Ortalama duygu skoruna göre piyasa durumu belirlenir:

| Skor Aralığı | Tahmin  |
| ------------ | ------- |
| > 0.1        | 🟢 BOĞA |
| < -0.1       | 🔴 AYI  |
| Diğer        | ⚪ NÖTR  |

---

## 🔎 Varlık Kodları Nasıl Yazılır?

| Piyasa    | Örnek      |
| --------- | ---------- |
| 🇹🇷 BIST | `THYAO.IS` |
| 🪙 Kripto | `BTC-USD`  |
| 🇺🇸 ABD  | `AAPL`     |

---

## 🛠️ Kullanılan Teknolojiler

* **Python 3.10+**
* **Streamlit**
* **Plotly**
* **Pandas**
* **Custom News Manager**
* **Custom Market Data Manager**

---

## 📂 Proje Yapısı

```
📦 borsa-kripto-ai
 ┣ 📜 app.py
 ┣ 📜 news_manager.py
 ┣ 📜 market_data.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## ⚙️ Kurulum

### 1️⃣ Depoyu Klonla

```bash
git clone https://github.com/kullanici-adi/borsa-kripto-ai.git
cd borsa-kripto-ai
```

### 2️⃣ Gerekli Paketleri Kur

```bash
pip install -r requirements.txt
```

### 3️⃣ Uygulamayı Çalıştır

```bash
streamlit run app.py
```

---

## 🧪 Örnek Ekran

* Canlı mum grafiği
* AI destekli piyasa durumu
* Türkçe haber listesi
* Hafta sonları otomatik gizleme (BIST için)

---

## ⚠️ Uyarı

> Bu uygulama **yatırım tavsiyesi değildir**.
> Sadece **bilgilendirme ve eğitim amaçlıdır**.

---

## 📌 Geliştirme Fikirleri

* 🔔 Alarm & bildirim sistemi
* 📉 Teknik indikatörler (RSI, MACD)
* 🧠 GPT destekli yorumlama
* 🌍 Çok dilli haber desteği
* ☁️ Cloud deploy (Streamlit Cloud / Docker)

---

## 👨‍💻 Geliştirici

**Osman Koray Sakar**
📍 Türkiye
🧠 AI • Finans • Veri Analizi

---

## ⭐ Destek

Projeyi beğendiysen ⭐ **Star** atmayı unutma!
Katkılar ve PR’lar her zaman açıktır 🚀

---

