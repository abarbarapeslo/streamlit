import streamlit as st
import pandas as pd

st.title("Bem-vindo(a) ao Chat XPTO")

# Inicializa os estados da sessão, se ainda não existem
if "pagina" not in st.session_state:
    st.session_state.pagina = "Login"

if "logado" not in st.session_state:
    st.session_state.logado = False

# Função para trocar para a página de cadastro
def trocar_para_cadastro():
    st.session_state.pagina = 'Cadastre-se'

# Função da tela de login
def tela_login():
    email = st.text_input("Digite seu e-mail..")
    passwrd = st.text_input("Digite sua senha..", type="password")

    if st.button("Login"):
        if email and passwrd:
            st.session_state.logado = True
        else:
            st.warning("Por favor, preencha seu e-mail e senha.")

    if st.button("Cadastre-se"):
        trocar_para_cadastro()

# Função da tela de cadastro
def tela_cadastro():
    st.write("Tela de cadastro")
    # Aqui você vai construir o formulário depois

# Controle de qual tela exibir
if st.session_state.logado:
    st.success("Você está logado!")
    # Aqui futuramente você pode chamar a função do chat
elif st.session_state.pagina == "Login":
    tela_login()
elif st.session_state.pagina == "Cadastre-se":
    tela_cadastro()
