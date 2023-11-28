import streamlit as st
import pandas as pd
import os, re

PATH_BASES = 'data'

# def convert_df_encoding(df):
#     return df.to_csv().encode('ISO-8859-1')
# def transformar_em_string(inicio, fim):
#     return list(map(str, range(inicio, fim + 1)))

# def extrair_nome_arquivo(string):
#     padrao = r'-(\w+)-\d{8}_\d{4}\.'
#     correspondencia = re.search(padrao, string)
#     if correspondencia:
#         return correspondencia.group(1)
#     else:
#         raise ValueError("Padrão não encontrado na string.")
# def listar_arquivos_em_pasta(caminho_da_pasta):
#     if not os.path.isdir(caminho_da_pasta):
#         raise ValueError("O caminho fornecido não é um diretório válido.")
#     elementos = os.listdir(caminho_da_pasta)
#     dict_arquivos = {extrair_nome_arquivo(elemento): os.path.join(caminho_da_pasta, elemento) for elemento in elementos}
#     return dict_arquivos
# def baixar_base(df_processado):
#     st.download_button(
#             label="Baixar CSV",
#             data=convert_df_encoding(df_processado),
#             file_name=f"{base_selected}.csv",
#             mime='text/csv',
#             )
# def selecionar_ano(df):
#     if "ANO" in df.columns:
#         ano_inicial = df.ANO.min()
#         ano_final = df.ANO.max()
#         st.write(f"Filtrar por faixa temporal")
#         ano_inicial_consulta, ano_final_consulta= st.sidebar.select_slider('Selecione a faixa temporal',
#                                             options=transformar_em_string(ano_inicial, ano_final),
#                                             value=(transformar_em_string(ano_inicial, ano_final)[0], transformar_em_string(ano_inicial, ano_final)[-1]),
#                                             on_change=True)
#         df_selecionado = df.loc[(df['ANO'] >= ano_inicial) & (df['ANO'] <= ano_final)]   
#     else:
#         df_selecionado = df

#     return df_selecionado

# Etapa 1: Descrição do Projeto
st.title("ConectaPNE: Dados")
st.header("Acesso aos dados ")
st.write("No canto esquerdo é possível acessar as páginas para aquisição dos dados:")
st.write("Metas: Os resultados das metas e indicadores.")
st.write("Microdados: Os dados públicos que foram utilizados para o cálculo das metas.")
# Etapa 2: Botões com Links
st.header("Links")

st.link_button("Documnetação", "https://aiboxlab-pne.github.io/dados/dict/serving/")
# st.link_button("Endpoint SPARQL ", "http://192.168.1.20:8890/sparql/")



# Etapa 3: Acesso aos Dados
# st.header("Etapa 3: Acesso aos Dados")


# st.sidebar.title("Navegação")
# page_options = ["Sobre", "Metas e Indicadores", "Microdados"]
# page = st.sidebar.radio("Escolha uma página", page_options)