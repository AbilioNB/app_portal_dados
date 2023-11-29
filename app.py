import streamlit as st
import pandas as pd
import os, re
from app_func import *
PATH_BASES = 'data'


st.title("ConectaPNE: Dados")
st.header("Acesso aos dados ")
st.write("Escolha entre os tipos de dados:")
st.write("Metas: Os resultados das metas e indicadores.")
st.write("Microdados: Os dados públicos que foram utilizados para o cálculo das metas.")
st.link_button("Documnetação", "https://aiboxlab-pne.github.io/dados/dict/serving/")

tipo_camada_dados = ["Metas e Indicadores", "Microdados"]
select_tipo_camada_dados = st.selectbox("Selecione", tipo_camada_dados)

if select_tipo_camada_dados=="Metas e Indicadores":
    metas_indicadores()
else:
    dados_publicos()

