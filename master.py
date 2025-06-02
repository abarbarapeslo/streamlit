import streamlit as st
import pandas as pd

st.title("Bem-vindo(a) ao Chat MoreTalk")

with st.chat_message("user"):
    st.write("Hello Human!")

agradecimentos = ["obrigado", "valeu", "agradeço", "muito obrigada"]
mensagem = st.chat_input()

def resposta(agradecimentos,mensagem):
    mensagem = mensagem.lower()
    for palavra in agradecimentos:
        if palavra in mensagem:
            return ("Um das palavras está contida na mensagem!")

    return ("Nenhuma palavra está contida na mensagem!")

if mensagem: #Só executa se o usuário digitou algo
    with st.chat_message("bot"): #mensagem formatada para o usuário...
        st.write(resposta(agradecimentos, mensagem)) #A mensagem entregue ao usuário

