# Importando a biblioteca Streamlit
import streamlit as st
import pandas as pd

# Exibindo um título no aplicativo
st.title("Hello, World com Streamlit")

# Exibindo um texto no aplicativo
st.write("Este é o meu primeiro aplicativo com Streamlit!")


df = pd.read_csv("vgsales.csv")
# Criando um botão
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")
