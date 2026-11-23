import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LGPD Compliance Analytics",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 LGPD Compliance Analytics Dashboard")

st.markdown(
    """
    Dashboard para monitoramento de indicadores de
    conformidade LGPD, privacidade e segurança da informação.
    """
)

try:
    titulares = pd.read_csv("data/titulares.csv")
    incidentes = pd.read_csv("data/incidentes.csv")
    solicitacoes = pd.read_csv("data/solicitacoes.csv")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Titulares",
            len(titulares)
        )

    with col2:
        st.metric(
            "Incidentes",
            len(incidentes)
        )

    with col3:
        st.metric(
            "Solicitações",
            len(solicitacoes)
        )

    st.subheader("Incidentes por Criticidade")

    st.bar_chart(
        incidentes["criticidade"].value_counts()
    )

    st.subheader("Dados por Setor")

    st.bar_chart(
        titulares["setor"].value_counts()
    )

except Exception as erro:
    st.error(f"Erro ao carregar os dados: {erro}")
