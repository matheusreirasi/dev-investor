import streamlit as st
import pandas as pd
import requests
import os

@st.cache_data(ttl=3600)
def get_data(endpoint, indicador):
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")  # fallback opcional
    url = f"{BACKEND_URL}/api/{endpoint}/{indicador}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except Exception as e:
        st.error(f"Erro ao buscar dados da API: {e}")
        return []
