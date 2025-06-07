import streamlit as st
import pandas as pd
import requests

@st.cache_data(ttl=3600)
def get_data(endpoint, indicador):
    url = f"http://backend:8000/api/{endpoint}/{indicador}"
    return requests.get(url)
