import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    return pd.read_csv("dados_opcoes.csv")  # Altere para o caminho correto se necessário

df_opcoes = carregar_dados()

def filtrar_opcoes_inteligentes(df, tipo='CALL'):
    try:
        df_filtrado = df[df['tipo'].str.upper() == tipo.upper()]
        df_filtrado = df_filtrado[df_filtrado['volumeFinanceiro'] > 100000]
        df_filtrado = df_filtrado[(df_filtrado['delta'] >= 0.3) & (df_filtrado['delta'] <= 0.7)]
        df_filtrado = df_filtrado[(df_filtrado['diasParaVencimento'] >= 3) & 
                                  (df_filtrado['diasParaVencimento'] <= 20)]
        df_filtrado = df_filtrado[df_filtrado['precoOpcao'] <= 5.00]

        preco_ativo = df_filtrado['precoAtivo'].iloc[0]
        df_filtrado['distanciaStrike'] = abs(df_filtrado['strike'] - preco_ativo)
        df_filtrado = df_filtrado.sort_values(by='distanciaStrike')

        return df_filtrado.head(5)
    except Exception as e:
        st.warning(f"Erro ao filtrar opções: {e}")
        return pd.DataFrame()

st.title("Agente Autônomo de Opções")

st.subheader("Melhores Opções CALL")
melhores_calls = filtrar_opcoes_inteligentes(df_opcoes, tipo='CALL')
st.dataframe(melhores_calls)

st.subheader("Melhores Opções PUT")
melhores_puts = filtrar_opcoes_inteligentes(df_opcoes, tipo='PUT')
st.dataframe(melhores_puts)
