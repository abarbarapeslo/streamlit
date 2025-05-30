import streamlit as st

st.title("Bem-vindo(a) ao Chat MoreTalk")

with st.chat_message("user"):
    st.write("Hello Human!")

a1 = st.chat_input("Say something..")
if a1 == "Olá":
    st.write("Olá! Como posso te ajudar hoje? :)")
    