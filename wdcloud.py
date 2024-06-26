import os
from flask.cli import load_dotenv
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests

load_dotenv()
st.set_page_config(
    page_title="Assuntos mais frequentes em artigos do New York Times",  # Title of your app
    page_icon=":chart_with_upwards_trend:",  # Icon for your app
    layout="centered",  # Layout mode ("wide" or "centered")
)

key = os.getenv("key")

st.subheader("WORDCLOUD - Assuntos mais frequentes em artigos do New York Times")
st.caption("Utilizando a API do NY Times, criei uma api que manipula esses dados e retorna os assuntos mais comentados de um determinado mês. O que é perfeito para criar uma nuvem de palavras (Wordcloud)")
st.divider()

@st.cache_data 
def fetch_data(month, year, key):
    url = f"https://pedrocozzati.pythonanywhere.com/subjects?month={month}&year={year}&key={key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().copy()
    else:
        return None


form = st.form(key="my_form")
month = form.text_input(label="Digite um mês (entre 1-12)")
year = form.text_input(label="Digite um ano")
submit_button = form.form_submit_button(label="Enviar")

if submit_button:
    jsonData = fetch_data(month, year, key)
    if jsonData is not None:
        ranks = {}
        for item in jsonData[f"{month}_{year}"]:
            words = item["subject"].replace(" ", "-").split()
            for word in words:
                ranks[word.replace("-", " ")] = item["amount"]

        wordcloud = WordCloud(
            contour_width=0,
            width=900,
            height=500,
            margin=0,
            background_color="black",
            contour_color= 'black',
            max_words=40,
            include_numbers=True,
            colormap="hsv",
            ranks_only=ranks,
            font_step=6
        ).generate_from_frequencies(ranks)

        fig, ax = plt.subplots()

        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
        
    else:
        st.error("Erro ao fazer a solicitação.")
