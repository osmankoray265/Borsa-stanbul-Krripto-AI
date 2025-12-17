import feedparser
import requests
import pandas as pd
from datetime import datetime

class NewsManager:
    def __init__(self):
        # Tarayıcı taklidi (Engel yememek için)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        
        # 🔥 TAMAMEN TÜRKÇE KAYNAKLAR 🔥
        self.rss_sources = {
            "Investing TR (Genel)": "https://tr.investing.com/rss/news.rss",
            "Investing TR (Borsa)": "https://tr.investing.com/rss/stock.rss",
            "Investing TR (Kripto)": "https://tr.investing.com/rss/crypto.rss",
            "DonanımHaber (Finans)": "https://www.donanimhaber.com/rss/tum/",
            "CoinTurk (Kripto)": "https://coin-turk.com/feed"
        }

    def analyze_sentiment_turkish(self, text):
        """
        Basit Türkçe Duygu Analizi (Kelime Bazlı)
        """
        text = text.lower()
        puan = 0
        
        # Pozitif Kelimeler (Boğa)
        pozitifler = ["yükseliş", "artış", "rekor", "kazan", "fırladı", "zirve", "olumlu", "boğa", "kar", "büyüme", "güçlü"]
        # Negatif Kelimeler (Ayı)
        negatifler = ["düşüş", "kayıp", "zarar", "çakıl", "kriz", "ayı", "olumsuz", "risk", "korku", "satış", "azal"]

        for kelime in pozitifler:
            if kelime in text:
                puan += 0.5
        
        for kelime in negatifler:
            if kelime in text:
                puan -= 0.5
                
        return puan

    def get_unified_news(self):
        all_news = []
        
        for source_name, url in self.rss_sources.items():
            try:
                response = requests.get(url, headers=self.headers, timeout=5)
                if response.status_code == 200:
                    feed = feedparser.parse(response.content)
                    for entry in feed.entries[:5]: # Her kaynaktan 5 haber
                        
                        title = entry.title
                        # Türkçe Analiz Yap
                        score = self.analyze_sentiment_turkish(title)
                        
                        # Etiketle
                        if score > 0:
                            label = "POZITIF"
                        elif score < 0:
                            label = "NEGATIF"
                        else:
                            label = "NOTR"

                        news_item = {
                            "source": source_name,
                            "title": title,
                            "link": entry.link,
                            "published": entry.get("published", datetime.now().strftime("%H:%M")),
                            "sentiment_score": score,
                            "sentiment_label": label
                        }
                        all_news.append(news_item)
            except:
                pass
        
        return pd.DataFrame(all_news)