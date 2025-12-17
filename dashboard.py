import streamlit as st
import plotly.graph_objects as go
from news_manager import NewsManager
from market_data import MarketManager
import time

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Borsa İstanbul & Kripto AI", layout="wide", page_icon="📈")

# --- 2. YAN MENÜ ---
with st.sidebar:
    st.title("🔎 Varlık Arama")
    
    st.info("""
    **Kodları Nasıl Yazmalısın?**
    🇹🇷 **Türk Hisseleri:** `.IS` ekle (Örn: `THYAO.IS`)
    🪙 **Kripto:** `-USD` ekle (Örn: `BTC-USD`)
    🇺🇸 **ABD:** Direkt yaz (Örn: `AAPL`)
    """)
    
    secilen_symbol = st.text_input("Hisse/Coin Kodu:", value="THYAO.IS").upper()
    
    if st.button("Analiz Et 🚀"):
        st.cache_data.clear()

# --- VERİ ÇEKME ---
@st.cache_data(ttl=60)
def tum_verileri_getir(symbol):
    mm = MarketManager()
    df_price = mm.get_crypto_data(symbol)
    
    nm = NewsManager()
    df_news = nm.get_unified_news()
    
    return df_price, df_news

# Yükleniyor...
with st.spinner(f'{secilen_symbol} taranıyor...'):
    df_price, df_news = tum_verileri_getir(secilen_symbol)

# --- ÜST KISIM ---
if not df_price.empty:
    son_fiyat = df_price['close'].iloc[-1]
    degisim = son_fiyat - df_price['open'].iloc[0]
    yuzde = (degisim / df_price['open'].iloc[0]) * 100
    para_birimi = "TL" if ".IS" in secilen_symbol else "$"
    
    col1, col2 = st.columns(2)
    col1.metric(label=f"💰 {secilen_symbol} Fiyatı", value=f"{son_fiyat:,.2f} {para_birimi}", delta=f"%{yuzde:.2f}")

    if not df_news.empty:
        ortalama_duygu = df_news['sentiment_score'].mean()
        if ortalama_duygu > 0.1:
            durum = "🟢 BOĞA SEZONU"
        elif ortalama_duygu < -0.1:
            durum = "🔴 AYI SEZONU"
        else:
            durum = "⚪ NÖTR"
        col2.metric(label="AI Tahmini", value=durum, delta=f"Skor: {ortalama_duygu:.2f}")

# --- 3. GRAFİK (GÜNCELLENMİŞ - BOŞLUKSUZ) ---
st.subheader(f"📈 {secilen_symbol} Canlı Grafiği")

if not df_price.empty:
    fig = go.Figure(data=[go.Candlestick(
        x=df_price['timestamp'],
        open=df_price['open'], high=df_price['high'],
        low=df_price['low'], close=df_price['close'],
        name=secilen_symbol
    )])
    
    # ROBOT KAFASI
    fig.add_annotation(
        text="🤖",
        font=dict(size=150, color="rgba(128, 128, 128, 0.1)"),
        showarrow=False, xref="paper", yref="paper", x=0.5, y=0.5
    )

    # 🔥 ÖNEMLİ AYAR: Boşlukları ve Karmaşayı Kaldır 🔥
    fig.update_layout(
        height=500,
        xaxis_rangeslider_visible=False, # Alttaki küçük haritayı gizle (Karmaşayı çözer)
        template="plotly_white" # Arka planı temiz yap
    )
    
    # Eğer bu bir hisse senediyse (Kripto değilse), boşlukları (haftasonu/gece) gizlemeye çalış
    if ".IS" in secilen_symbol or "-" not in secilen_symbol:
        # Borsa ise (Cumartesi-Pazar gizle)
        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]), # Hafta sonlarını gizle
                # dict(bounds=[18, 10], pattern="hour"), # Gece saatlerini gizle (Opsiyonel - bazen veri kaydırabilir)
            ]
        )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"❌ '{secilen_symbol}' verisi alınamadı.")

# --- HABERLER ---
st.subheader("📰 Türkçe Haberler")
if not df_news.empty:
    df_news = df_news.sort_values(by="sentiment_score", ascending=False)
    for index, row in df_news.iterrows():
        st.markdown(f"**{row['sentiment_label']}** | {row['title']}")