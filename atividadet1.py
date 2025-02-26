import streamlit as st

st.header('st.button')
st.button('Say hello')
st.toggle("Toggle")
st.text_area("Enter text")
st.slider('Quantos anos você tem?', 0, 130, 25)
st.metric(
    label="Métrica de Vendas",  # Nome ou título da métrica
    value=100,          # Valor atual da métrica
    delta=15,             # Variação em relação ao valor anterior
    delta_color="off",      # Cor do delta (pode ser "normal", "inverse" ou "off")
)
st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))
