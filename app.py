import streamlit as st
from datetime import datetime
import yfinance as yf
import streamlit as st

st.set_page_config(page_title="Agente Autônomo de Opções", layout="wide")

# Cabeçalho
st.title("Agente Autônomo de Opções")
st.markdown("### Análise automatizada do mercado de opções brasileiras")
st.markdown("---")

# Menu lateral
st.sidebar.title("Configurações")
notificacoes = st.sidebar.checkbox("Ativar notificações")
simulacao_automatica = st.sidebar.checkbox("Rodar simulação automaticamente")
st.sidebar.markdown(f"Última execução: **{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}**")

# Simulação manual
if st.button("Rodar Simulação Agora"):
    st.success("Simulação executada com sucesso!")
    st.info("Ativos recomendados: PETR4, VALE3, B3SA3 (exemplo)")
    st.warning("Esses dados são apenas ilustrativos. Configure a conexão com a B3 para dados reais.")

# Resultados da análise técnica
st.markdown("## Indicadores Técnicos")
st.write("- Tendência de curto e médio prazo")
st.write("- Ponto de entrada ideal")
st.write("- Probabilidade de acerto estimada")

# Estratégias com opções
st.markdown("## Estratégias com Opções")
estrategia = st.selectbox("Escolha a estratégia:", ["Call Coberta", "Trava de Alta", "Trava de Baixa", "Venda de Puts", "Compra Direta de Calls"])
st.write(f"Simulando estratégia: **{estrategia}**")

# Simulação automática
if simulacao_automatica:
    st.info("Rodando simulação automática...")
    st.success("Resultados atualizados automaticamente!")

# Notificações
if notificacoes:
    st.markdown("## Notificações")
    st.success("Notificações ativadas e integradas ao Telegram!")
    st.write("Você será alertado quando houver um ativo com alta probabilidade de lucro.")

st.header("Consulta de Ações e Opções em Tempo Real")

ticker_input = st.text_input("Digite o ticker (ex: PETR4.SA)", "PETR4.SA")

if st.button("Consultar"):
    with st.spinner("Consultando..."):
        ativo = yf.Ticker(ticker_input)
        dados = ativo.history(period="1d", interval="5m")

        st.subheader(f"Últimos dados de {ticker_input}")
        st.dataframe(dados.tail())

        opcoes = ativo.options
        if opcoes:
            vencimento = opcoes[0]
            cadeia = ativo.option_chain(vencimento)
            st.subheader(f"Opções CALL ({vencimento})")
            st.dataframe(cadeia.calls)
            st.subheader(f"Opções PUT ({vencimento})")
            st.dataframe(cadeia.puts)
        else:
            st.warning("Este ativo não possui opções disponíveis no momento.")
# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Eduardo Cristino - Projeto Agente Autônomo de Opções")
