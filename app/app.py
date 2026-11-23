import os
import streamlit as st

st.title("Teste de Arquivos")

st.write("Pasta atual:")
st.write(os.getcwd())

st.write("Arquivos encontrados:")

for raiz, pastas, arquivos in os.walk("."):
    st.write(f"📁 {raiz}")
    for arquivo in arquivos:
        st.write(f"   📄 {arquivo}")
