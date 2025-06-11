import streamlit as st
import os
from openai import OpenAI  

def tela_chat():
    st.title("Chat com IA")

    # Criar o cliente OpenAI passando a chave da variável de ambiente
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    mensagem = st.chat_input("Digite sua mensagem:")

    if "historico" not in st.session_state:
        st.session_state.historico = []

    if mensagem:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                *[
                    {"role": "user", "content": item["mensagem"]}
                    for item in st.session_state.historico
                ],
                {"role": "user", "content": mensagem},
            ],
        )
        resposta_texto = response.choices[0].message.content

        st.session_state.historico.append({
            "mensagem": mensagem,
            "resposta": resposta_texto
        })

    for item in st.session_state.historico:
        with st.chat_message("user"):
            st.write(item["mensagem"])
        with st.chat_message("bot"):
            st.write(item["resposta"])