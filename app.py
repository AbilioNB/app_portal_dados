import streamlit as st
from app_func import metas_indicadores, dados_publicos
PATH_BASES = 'data'


st.title("ConectaPNE: Dados")
st.write("Os conjuntos de dados adotados nos conjuntos de dados do Conecta PNE são: dados educacionais; dados socioeconômicos; dados contábeis; e dados populacionais.") 
st.write("Como principais fontes destes dados temos: o INEP para os dados educacionais; o AtlasBR para dados socioeconômicos; o IBGE para os dados bases de estimativas populacionais; o DataSUS para estimativas populacionais a partir das bases de nascimentos e mortalidade; o Geocapes para dados de titulações de mestrado e doutorado; e o Siconfi com informações contábeis e fiscais.")
st.header("Acesso aos dados ")
st.write("Escolha entre os tipos de dados:")
st.write("Metas: Os resultados das metas e indicadores.")
st.write("Microdados: Os dados públicos que foram utilizados para o cálculo das metas.")
st.link_button("Documnetação", "https://aiboxlab-pne.github.io/dados/dict/serving/")

# tipo_camada_dados = ["Metas e Indicadores", "Microdados"]
# select_tipo_camada_dados = st.selectbox("Selecione", tipo_camada_dados)

container_metas = st.container()
with container_metas:
    metas_indicadores()

container_microdados = st.container()
with container_microdados:
    dados_publicos()



# if select_tipo_camada_dados=="Metas e Indicadores":
#     metas_indicadores()
# else:
#     dados_publicos()