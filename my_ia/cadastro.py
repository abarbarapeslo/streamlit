import streamlit as st
import pandas as pd

nome = st.text_input("Nome")
sobrenome = st.text_input("Sobrenome")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
data = st.date_input("Data de Nascimento")

tudo = [nome,sobrenome,email,senha,data]

def validacao(tudo):
    for itens in tudo:
        if not itens:
            return False
    return True
   
if st.button("Cadastre-se"):
    if validacao(tudo):
        st.success('Você está cadastrado!')
    else:
        st.warning('Você não preencheu todos os dados de cadastro')