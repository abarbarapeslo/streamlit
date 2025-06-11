import streamlit as st
from cadastro import tela_cadastro

def tela_login():
    st.title("Login XPTO")
    
    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", key="btn_entrar"):
        if email and senha:
            st.success("Login realizado com sucesso!")
            st.session_state.pagina = "chat"
        else:
            st.warning("Por favor, preencha todos os campos.")

    st.markdown("---")
    if st.button("Cadastre-se", key="btn_cadastro_login"):
        st.session_state.pagina = "cadastro"
