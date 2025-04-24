import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Fundamentus Dashboard", layout="wide")
st.title("📊 Fundamentus - Ações e FIIs")

@st.cache_data(ttl=3600)
def get_data(endpoint):
    url = f"http://backend:8000/{endpoint}"
    return pd.DataFrame(requests.get(url).json())

st.subheader("📈 AÇÕES")
st.dataframe(get_data('acoes'), use_container_width=True)

st.subheader("🏢 FIIs")
st.dataframe(get_data('fiis'), use_container_width=True)

