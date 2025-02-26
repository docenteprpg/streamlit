import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título da aplicação
st.title('Aplicação Streamlit Simples')

# Campo de entrada de texto
nome = st.text_input('Digite seu nome:', '')

# Se o usuário digitar algo, exibe uma saudação
if nome:
    st.write(f'Olá, {nome}! Bem-vindo à nossa aplicação.')

# Gerando dados para o gráfico
x = np.arange(1, 6)
y = np.random.randint(1, 10, size=5)

# Exibindo um gráfico de barras
fig, ax = plt.subplots()
ax.bar(x, y)

# Exibindo o gráfico na aplicação
st.pyplot(fig)
