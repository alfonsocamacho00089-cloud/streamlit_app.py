import streamlit as st
import requests
import time

def obtener_p2p_seguro():
    url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    payload = {
        "asset": "USDT", "fiat": "VES", "merchantCheck": True,
        "rows": 1, "tradeType": "BUY", "publisherType": "merchant"
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        if res.status_code == 200:
            return res.json()['data'][0]['adv']['price']
        return None
    except:
        return None

st.set_page_config(page_title="Antena v2", page_icon="📡")
st.title("📡 Antena P2P - Señal Limpia")

tasa = obtener_p2p_seguro()

if tasa:
    st.metric(label="Binance P2P Real", value=f"{tasa} Bs")
    # Tu app de Acode buscará esta línea
    st.write(f"VALOR_REAL|{tasa}|") 
    st.success("✅ Conectado con IP nueva")
else:
    st.error("⚠️ Esperando señal...")

# 5 Minutos de tregua para que no nos quemen la IP de nuevo
time.sleep(300)
st.rerun()
