import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

def tela_chat():
    st.title("Chat com IA")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("API KEY não carregada. Verifique seu .env.")
        return

    client = OpenAI(api_key=api_key)

    mensagem = st.chat_input("Digite sua mensagem:")

    if "historico" not in st.session_state:
        st.session_state.historico = []

    if mensagem:
        try:
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

        except Exception as e:
            st.error(f"Erro ao chamar API OpenAI: {e}")
            return

    for item in st.session_state.historico:
        with st.chat_message("user"):
            st.write(item["mensagem"])
        with st.chat_message("bot"):
            st.write(item["resposta"])
