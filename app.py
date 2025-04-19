import streamlit as st
import pandas as pd
from datetime import datetime

# Título da aplicação
st.title("Agente Autônomo de Opções")

# Carregar dados
df = pd.read_csv("dados_opcoes.csv")

# Conversões e limpeza
df['data_vencimento'] = pd.to_datetime(df['data_vencimento'], errors='coerce')
df['validade'] = df['data_vencimento']  # cópia para exibição

# Mostrar dados brutos
st.subheader("Dados das Opções")
st.dataframe(df)

# Filtros
st.markdown("### Selecione o tipo de opção")
tipo_opcao = st.selectbox("Selecione o tipo de opção", df["tipo"].unique())

st.markdown("### Filtrar por data de vencimento (opcional)")
data_venc_input = st.text_input("YYYY/MM/DD")

# Aplicar filtros
df_filtrado = df[df["tipo"] == tipo_opcao]

if data_venc_input:
    try:
        data_formatada = datetime.strptime(data_venc_input, "%Y/%m/%d")
        df_filtrado = df_filtrado[df_filtrado["data_vencimento"] == data_formatada]
    except ValueError:
        st.error("Formato de data inválido. Use o formato YYYY/MM/DD.")

# Exibir resultado do filtro
st.subheader("Resultado do Filtro")
st.dataframe(df_filtrado)

# Lógica de recomendação
st.subheader("Recomendações")
for i, row in df_filtrado.iterrows():
    tipo = row['tipo']
    preco_ativo = row['preco_ativo']
    preco_exercicio = row['preco_exercicio']
    venc = row['data_vencimento'].date()

    if tipo == 'CALL':
        if preco_ativo > preco_exercicio:
            st.markdown(f"**CALL** com vencimento em {venc}: **Vale a pena exercer.**")
        else:
            st.markdown(f"**CALL** com vencimento em {venc}: Não vale a pena.")
    elif tipo == 'PUT':
        if preco_ativo < preco_exercicio:
            st.markdown(f"**PUT** com vencimento em {venc}: **Vale a pena exercer.**")
        else:
            st.markdown(f"**PUT** com vencimento em {venc}: Não vale a pena.")
