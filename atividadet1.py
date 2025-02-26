import streamlit as st
import pandas as pd
import datetime

st.header('st.button')
st.button('Say hello')
st.toggle("Toggle")
st.text_area("Enter text")
st.text_input("Movie title", "Life of Brian")
st.slider('Quantos anos você tem?', 0, 130, 25)

st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)

st.metric(
    label="Métrica de Vendas",  # Nome ou título da métrica
    value=100,          # Valor atual da métrica
    delta=15,             # Variação em relação ao valor anterior
    delta_color="off",      # Cor do delta (pode ser "normal", "inverse" ou "off")
)
st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))

st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')

st.write("Sucesso! Aqui está o seu 🍦")


options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")

selection = st.segmented_control(
    "Directions", options, selection_mode="multi"
)

st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

st.color_picker("Pick A Color", "#00f900")

st.feedback("stars")


st.number_input("Insert a number")

st.chat_input("Say something")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

st.time_input("Set an alarm for", datetime.time(8, 45))

st.audio_input("Record a voice message")


st.file_uploader("Choose a file")
st.camera_input("Tire uma foto")

