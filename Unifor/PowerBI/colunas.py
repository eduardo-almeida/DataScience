import streamlit as st

# Configurando o layout com colunas
st.title("Layout Personalizado com Colunas")
col1, col2 = st.columns(2)

with col1:
    st.write("Esta é a Coluna 1")
    st.button("Botão na Coluna 1")

with col2:
    st.write("Esta é a Coluna 2")
    st.button("Botão na Coluna 2")


""" col1, col2, col3 = st.columns(3)

with col1:
    st.write("blabla")

with col2:
    st.write("blabla")

with col3:
    st.write("blabla") """
