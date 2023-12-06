import streamlit as st
import pandas as pd
import os, re

PATH_BASES = 'data'
def convert_df_encoding(df):
    return df.to_csv().encode('ISO-8859-1')
def transformar_em_string(inicio, fim):
    return list(map(str, range(inicio, fim + 1)))

def extrair_nome_arquivo(string):
    padrao = r'-(\w+)-\d{8}_\d{4}\.'
    correspondencia = re.search(padrao, string)
    if correspondencia:
        return correspondencia.group(1)
    else:
        raise ValueError("Padrão não encontrado na string.")
def listar_arquivos_em_pasta(caminho_da_pasta):
    if not os.path.isdir(caminho_da_pasta):
        raise ValueError("O caminho fornecido não é um diretório válido.")
    elementos = os.listdir(caminho_da_pasta)
    dict_arquivos = {extrair_nome_arquivo(elemento): os.path.join(caminho_da_pasta, elemento) for elemento in elementos}
    return dict_arquivos
def baixar_base(df_processado,base_selected):
    st.download_button(
            label="Baixar CSV",
            data=convert_df_encoding(df_processado),
            file_name=f"{base_selected}.csv",
            mime='text/csv',
            )
def selecionar_ano(df):
    if "ANO" in df.columns:
        ano_inicial = df.ANO.min()
        ano_final = df.ANO.max()
        st.write(f"Filtrar por faixa temporal")
        ano_inicial_consulta, ano_final_consulta= st.sidebar.select_slider('Selecione a faixa temporal',
                                            options=transformar_em_string(ano_inicial, ano_final),
                                            value=(transformar_em_string(ano_inicial, ano_final)[0], transformar_em_string(ano_inicial, ano_final)[-1]),
                                            on_change=True)
        df_selecionado = df.loc[(df['ANO'] >= ano_inicial) & (df['ANO'] <= ano_final)]   
    else:
        df_selecionado = df

    return df_selecionado
def metas_indicadores():
    st.header("Metas e Indicadores")
    # Filtros
    bases_disponiveis = listar_arquivos_em_pasta(PATH_BASES)
    base_options = list(bases_disponiveis.keys())
    base_selected = st.selectbox("Selecione a Base", base_options)
    # Exemplo da base
    df = pd.read_parquet(bases_disponiveis[base_selected])
    if "ANO" in df.columns:
            ano_inicial = df.ANO.min()
            ano_final = df.ANO.max()
            ano_inicial_consulta, ano_final_consulta= st.select_slider('Selecione a faixa temporal',
                                                options=transformar_em_string(ano_inicial, ano_final),
                                                value=(transformar_em_string(ano_inicial, ano_final)[0], transformar_em_string(ano_inicial, ano_final)[-1]))
            df = df.loc[(df['ANO'] >= int(ano_inicial_consulta)) & (df['ANO'] <= int(ano_final_consulta))]
    st.write(f"Amostra do DataFrame para {base_selected} :")
    st.dataframe(df.head())

    baixar_base(df,base_selected)

def selecionar_tipo_bases(op):
    if op=="Educacional":
        return ['Censo da Educação Básica','Censo da Educação Superior']
    elif op=="Populacional":
        return ['Estimativa populacional','Censo Populacional 2022']
    else:
         return ['MUNIC','Atlas BR 2019']

def dados_publicos():
    
    dados_orcamento_fake = {
    'Ano': [2020, 2020, 2021, 2021, 2022, 2022],
    'Mês': ['Janeiro', 'Fevereiro', 'Janeiro', 'Fevereiro', 'Janeiro', 'Fevereiro'],
    'Receitas': [100000, 120000, 110000, 130000, 105000, 125000],
    'Despesas': [80000, 90000, 85000, 95000, 88000, 92000]}
    df = pd.DataFrame(dados_orcamento_fake)
    st.header("Microdados públicos")

    st.write("Mussum Ipsum, cacilds vidis litro abertis. Viva Forevis aptent taciti sociosqu ad litora torquent. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Bota 1 metro de cachacis aí pra viagem! Pellentesque nec nulla ligula. Donec gravida turpis a vulputate ultricies.")
    st.write("Mussum Ipsum, cacilds vidis litro abertis. Viva Forevis aptent taciti sociosqu ad litora torquent. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Bota 1 metro de cachacis aí pra viagem! Pellentesque nec nulla ligula. Donec gravida turpis a vulputate ultricies.")


    st.subheader("Educacional")
    st.write("Lista das bases educacionais utilizadas para as metas.")


    st.subheader("Populacional")
    st.write("Lista das bases populacionais e do IBGE.")


    st.subheader("Outros dados públicos")
    st.write("Aqui temos a lista de outros dados públicos utilizados nesse projeto")

    tipo_dados = ["Educacional", "Populacional", "Outros dados públicos"]
    select_tipo_dados = st.selectbox("Selecione", tipo_dados)



    bases_tipo = selecionar_tipo_bases(select_tipo_dados)
    base_selecionada = st.selectbox("Selecione", bases_tipo)
    baixar_base(df,df.head())
