import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv('src/dados_opcoes.csv')

# Converter a data de vencimento
df['validade'] = pd.to_datetime(df['data_vencimento'], errors='coerce')

# Título do app
st.title("Agente Autônomo de Opções")

# Mostrar os dados
st.subheader("Dados das Opções")
st.dataframe(df)

# Filtros
tipo_opcao = st.selectbox("Selecione o tipo de opção", ["CALL", "PUT"])
data_filtro = st.date_input("Filtrar por data de vencimento (opcional)", value=None)

# Filtrar dados
df_filtrado = df[df['tipo'] == tipo_opcao]
if data_filtro:
    df_filtrado = df_filtrado[df_filtrado['validade'].dt.date == data_filtro]

st.subheader("Resultado do Filtro")
st.dataframe(df_filtrado)

# Lógica simples de decisão
st.subheader("Recomendações")
for _, row in df_filtrado.iterrows():
    if row['tipo'] == 'CALL':
        if row['preco_ativo'] > row['preco_exercicio']:
            st.write(f"CALL com vencimento em {row['validade'].date()}: **Vale a pena exercer.**")
        else:
            st.write(f"CALL com vencimento em {row['validade'].date()}: **Não vale a pena.**")
    elif row['tipo'] == 'PUT':
        if row['preco_ativo'] < row['preco_exercicio']:
            st.write(f"PUT com vencimento em {row['validade'].date()}: **Vale a pena exercer.**")
        else:
            st.write(f"PUT com vencimento em {row['validade'].date()}: **Não vale a pena.**")
