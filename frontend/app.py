import streamlit as st
import pandas as pd
import requests

from helpers.data import get_data

st.set_page_config(page_title="DevInvestor", layout="wide")
st.title("📊 Fundamentus - Ações e FIIs")

st.write("""
        Plataforma criada com o intuito de retornar as ações e os fundos imobiliários
        mais indicados de acordo com as análises fundamentalistas mais utilizadas pelo mercado,
        auxiliando no processo de escolha de ativos para minha carteira de investimentos.
        """)
