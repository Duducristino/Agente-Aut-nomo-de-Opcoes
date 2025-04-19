import pandas as pd
import streamlit as st

# Título do app
st.set_page_config(page_title="Agente Autônomo de Opções", layout="wide")
st.title("Agente Autônomo de Opções")

# Carregar os dados
try:
    df = pd.read_csv("src/dados_opcoes.csv")
except FileNotFoundError:
    st.error("Arquivo 'dados_opcoes.csv' não encontrado na pasta 'src'. Verifique o caminho.")
    st.stop()

# Filtrar colunas relevantes (ajuste se necessário)
colunas_necessarias = ['ativo', 'tipo', 'strike', 'validade', 'cotacao_atual', 'cotacao_opcao', 'delta', 'volume']
df = df[[col for col in colunas_necessarias if col in df.columns]]

# Ajuste de tipos
df['validade'] = pd.to_datetime(df['validade'], errors='coerce')

# Filtros básicos
col1, col2 = st.columns(2)
tipo = col1.selectbox("Tipo de opção", ['call', 'put', 'ambos'])
min_delta = col2.slider("Delta mínimo", min_value=-1.0, max_value=1.0, value=0.3)

# Aplicar filtros
if tipo != 'ambos':
    df = df[df['tipo'].str.lower() == tipo]
df = df[df['delta'].abs() >= min_delta]

# Mostrar resultados
st.subheader("Opções Selecionadas")
st.dataframe(df.sort_values(by='volume', ascending=False).reset_index(drop=True))

# Métricas
st.subheader("Estatísticas")
st.write(f"Total de opções encontradas: {len(df)}")
st.write(f"Média de volume: {df['volume'].mean():.2f}")
st.write(f"Média de delta: {df['delta'].mean():.2f}")
