import yfinance as yf
import pandas as pd

class MarketManager:
    def get_crypto_data(self, symbol, timeframe='1h', limit=100):
        """
        Yahoo Finance üzerinden hem Kripto hem Hisse çeker.
        """
        try:
            # Yahoo Finance kütüphanesi ile veriyi çek
            # period='1d' (1 günlük), interval='15m' (15 dakikalık mumlar)
            ticker = yf.Ticker(symbol)
            
            # Veriyi indir (Son 5 günlük veri alalım ki grafik dolsun)
            df = ticker.history(period="5d", interval="1h") # 1 saatlik mumlar
            
            if df.empty:
                return pd.DataFrame()

            # Yahoo Finance sütun isimleri: Open, High, Low, Close, Volume
            # Sadece sütun isimlerini küçük harfe çevirelim
            df = df.reset_index()
            df.columns = [c.lower() for c in df.columns]
            
            # Tarih sütunu 'date' veya 'datetime' gelebilir, onu 'timestamp' yapalım standart olsun
            if 'date' in df.columns:
                df = df.rename(columns={'date': 'timestamp'})
            elif 'datetime' in df.columns:
                df = df.rename(columns={'datetime': 'timestamp'})

            return df

        except Exception as e:
            print(f"Hata: {e}")
            return pd.DataFrame()

# --- TEST KISMI ---
if __name__ == "__main__":
    mm = MarketManager()
    
    print("✈️ THY (THYAO.IS) deneniyor...")
    df_thy = mm.get_crypto_data("THYAO.IS")
    print(df_thy.head(2))
    
    print("\n💰 Bitcoin (BTC-USD) deneniyor...")
    df_btc = mm.get_crypto_data("BTC-USD")
    print(df_btc.head(2))