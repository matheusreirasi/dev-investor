import streamlit as st
import pandas as pd

from helpers.data import get_data

st.set_page_config(page_title="Ações")

indicadores_data = get_data('acoes','').json()
dy_data = get_data('acoes','dy').json()
pvp_data = get_data('acoes','pvp').json()
roe_data = get_data('acoes','roe').json()
selecionados_data = get_data('acoes', 'selecionados').json()


st.subheader('Tabela Bruta',divider='gray')
st.dataframe(indicadores_data, use_container_width= True)
col1, col2, col3 = st.columns(3)


col1.subheader('Div. Yield')
col1.dataframe(dy_data, use_container_width=True)

col2.subheader("P/VP")
col2.dataframe(pvp_data, use_container_width=True)

col3.subheader("ROE")
col3.dataframe(roe_data, use_container_width=True)

st.subheader("Ações Selecionadas",divider='blue')
st.write("Ações para análise que aparecem nas três tabelas.")
st.dataframe(selecionados_data, use_container_width=True)
st.write(pd.DataFrame(selecionados_data).shape)
