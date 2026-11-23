import pandas as pd
import streamlit as st

st.set_page_config(page_title="LGPD Compliance Analytics")

st.title("🔐 LGPD Compliance Analytics Dashboard")

titulares = pd.read_csv("data/titulares.csv")
incidentes = pd.read_csv("data/incidentes.csv")
solicitacoes = pd.read_csv("data/solicitacoes.csv")

st.metric("Titulares", len(titulares))
st.metric("Incidentes", len(incidentes))
st.metric("Solicitações", len(solicitacoes))

st.subheader("Incidentes por Criticidade")

st.bar_chart(
    incidentes["criticidade"].value_counts()
)

st.subheader("Dados por Setor")

st.bar_chart(
    titulares["setor"].value_counts()
)
