import streamlit as st
import pandas as pd
from helpers.data import get_data

st.set_page_config(page_title="FIIs")

fiis = get_data('fiis','').json()
# df_fiis = pd.DataFrame(fiis)
dy_data = get_data('fiis','dy').json()
pvp_data = get_data('fiis','pvp').json()
df_imoveis = get_data('fiis','imoveis').json()
vacancia_data = get_data('fiis','vacancia').json()
selecionados_data = get_data('fiis','selecionados').json()

st.subheader('Tabela Bruta',divider='gray')
st.dataframe(fiis, use_container_width=True)

col1, col2, col3 = st.columns(3)


col1.subheader('Div. Yield',)
col1.dataframe(dy_data, use_container_width=True)

col2.subheader("P/VP")
col2.dataframe(pvp_data, use_container_width=True)

col3.subheader("Vacância Média")
col3.dataframe(vacancia_data, use_container_width=True)

st.subheader("Ações Selecionadas",divider='blue')
st.write("FIIs para análise que aparecem nas três tabelas.")
st.dataframe(selecionados_data, use_container_width=True)
st.write(pd.DataFrame(selecionados_data).shape)