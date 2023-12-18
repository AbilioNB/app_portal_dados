import streamlit as st
from app_func import metas_indicadores, dados_publicos
PATH_BASES = 'data'


st.title("ConectaPNE: Dados")
st.write("Os conjuntos de dados aqui apresentados são as bases de dados do portal ConectaPNE, os dados são responsáveis pelo calculo das metas exibidas no portal.")
 
st.write("Como principais fontes destes dados temos: o INEP para os dados educacionais; o AtlasBR para dados socioeconômicos; o IBGE para os dados bases de estimativas populacionais; o DataSUS para estimativas populacionais a partir das bases de nascimentos e mortalidade; o Geocapes para dados de titulações de mestrado e doutorado; e o Siconfi com informações contábeis e fiscais.")
# st.header("Acesso aos dados ")
# st.divider()
st.subheader("Categorias de dados disponíveis:")
st.write("Metas e Indicadores: Os resultados das metas e indicadores que possam ser filtrados por ano. ")
st.write("Microdados públicos: Os dados públicos que foram parcialmente processados para o cálculo das metas que são exibidas no sistema.")
st.write("Disponibilizamos também a documentação das bases e a ficha técnica ilustrando como foi cálculado cada indicador.")
st.link_button("Dicionário de dados", "https://aiboxlab-pne.github.io/dados/dict/serving/")
st.link_button("Fichas Técnicas-Metas", "https://aiboxlab-pne.github.io/dados/meta/01/")
# tipo_camada_dados = ["Metas e Indicadores", "Microdados"]
# select_tipo_camada_dados = st.selectbox("Selecione", tipo_camada_dados)
st.divider()
container_metas = st.container()
with container_metas:
    metas_indicadores()
st.divider()
container_microdados = st.container()
with container_microdados:
    dados_publicos()
st.divider()
st.header("Exemplos de uso")
st.link_button("1-Como carregar e abrir arquivos .parquet.","https://colab.google/")
st.link_button("2-Como unir bases de metas para meu município.","https://colab.google/")
st.link_button("3-Como selecionar as escolas da minha localidade nos dados do censo da educação básica.","https://colab.google/")