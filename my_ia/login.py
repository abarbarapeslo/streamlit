import streamlit as st
import pandas as pd

st.title("Bem-vindo(a) ao MoreTalk")

# Função de tela de login
def tela_login():
    email = st.text_input("Digite seu e-mail..")
    passwrd = st.text_input("Digite sua senha..", type="password")
    
    if st.button("Login"):
        if email and passwrd:
            st.session_state.logado = True
        else:
            st.warning("Por favor, preencha seu e-mail e senha.")

# Inicializa o estado 'logado' se não existir ainda
if "logado" not in st.session_state:
    st.session_state.logado = False

# Verifica se o usuário está logado
if st.session_state.logado:
    st.success("Você está logado!")
    # Aqui futuramente você pode chamar a função do chat
else:
    tela_login()

#Função tela de cadastro
def tela_cadastro():
    st.button("Cadastre-se")
tela_cadastro()
