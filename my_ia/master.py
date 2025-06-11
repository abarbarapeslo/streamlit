import streamlit as st
import pandas as pd
import openai

def tela_chat():
    st.title("Bem-vindo(a) ao Chat XPTO!")
tela_chat()

st.write("Say something..")

openai.api_key = "MY_API"
agradecimentos = ["obrigado", "valeu", "agradeço", "muito obrigada"]
mensagem = st.chat_input()

def resposta(agradecimentos,mensagem):
    mensagem = mensagem.lower()
    for palavra in agradecimentos:
        if palavra in mensagem:
            return ("Um das palavras está contida na mensagem!")

    return ("Nenhuma palavra está contida na mensagem!")

if "historico" not in st.session_state:
    st.session_state.historico = []

if mensagem:
    resposta_usuario = resposta(agradecimentos, mensagem)
    st.session_state.historico.append({
        "mensagem": mensagem,
        "resposta": resposta_usuario
    })

# EXIBIR O HISTÓRICO COMPLETO
for item in st.session_state.historico:
    with st.chat_message("user"):
        st.write(item["mensagem"])
    with st.chat_message("bot"):
        st.write(item["resposta"])