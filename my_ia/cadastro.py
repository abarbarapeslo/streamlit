import streamlit as st
import pandas as pd

def tela_cadastro():
    st.title("Cadastro")

    nome = st.text_input("Nome")
    sobrenome = st.text_input("Sobrenome")
    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")
    data = st.date_input("Data de Nascimento")

    tudo = [nome, sobrenome, email, senha, data]

    def validacao(dados):
        for item in dados:
            if not item:
                return False
        return True

    # Add key
    if st.button("Cadastre-se", key="botao_cadastro"):
        if validacao(tudo):
            st.success("Você está cadastrado!")
        else:
            st.warning("Você não preencheu todos os dados de cadastro.")
