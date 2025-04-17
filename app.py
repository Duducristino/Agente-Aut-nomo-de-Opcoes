import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Automatus - Options Agent", layout="wide")

st.title("Automatus Options Agent")
st.markdown("### Análise de ativos de opções com inteligência autônoma")

ticker = st.text_input("Digite o ticker da ação (ex: PETR4.SA)", "PETR4.SA")
if ticker:
    data = yf.download(ticker, period="6mo")
    st.line_chart(data["Close"])
