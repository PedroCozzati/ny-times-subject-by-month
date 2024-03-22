from collections import Counter
import os
import re
from flask.cli import load_dotenv
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import altair as alt
from matplotlib.animation import FuncAnimation
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests

load_dotenv()
st.set_page_config(
    page_title="Análise de dados de vagas do linkedin",  # Title of your app
    page_icon=":chart_with_upwards_trend:",  # Icon for your app
    layout="centered",  # Layout mode ("wide" or "centered")
)

key = os.getenv("key")

@st.cache_data 
def fetch_data(month, year, key):
    url = f"https://pedrocozzati.pythonanywhere.com/subjects?month={month}&year={year}&key={key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().copy()
    else:
        return None


form = st.form(key="my_form")
month = form.text_input(label="Digite um mês e aperte Enter (1-12)")
year = form.text_input(label="Digite um ano e aperte Enter")
submit_button = form.form_submit_button(label="Submit")

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
