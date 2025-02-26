
import streamlit as st
import numpy as np

# Título da aplicação
st.title('Aplicação Streamlit Simples')

# Campo de entrada de texto
nome = st.text_input('Digite seu nome:', '')

# Se o usuário digitar algo, exibe uma saudação
if nome:
    st.write(f'Olá, {nome}! Bem-vindo à nossa aplicação.')




