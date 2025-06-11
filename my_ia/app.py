import streamlit as st
from login import tela_login
from cadastro import tela_cadastro
from master import tela_chat  

# Inicializa a página atual na session_state
if "pagina" not in st.session_state:
    st.session_state.pagina = "login"

# Função para trocar a página
def mudar_pagina(pagina):
    st.session_state.pagina = pagina

# Menu simples para navegar entre páginas
st.sidebar.title("Navegação")
if st.sidebar.button("Login", key="botao_login_sidebar"):
    st.session_state.pagina = "login"
if st.sidebar.button("Cadastro"):
    mudar_pagina("cadastro")
if st.sidebar.button("Chat"):
    mudar_pagina("chat")

# Renderiza a página atual
if st.session_state.pagina == "login":
    tela_login()
elif st.session_state.pagina == "cadastro":
    tela_cadastro()
elif st.session_state.pagina == "chat":
    tela_chat()
