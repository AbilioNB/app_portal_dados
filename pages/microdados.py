import streamlit as st

def selecionar_tipo_bases(op):
    if op=="Educacional":
        return ['Censo da Educação Básica','Censo da Educação Superior']
    elif op=="Populacional":
        return ['Estimativa populacional','Censo Populacional 2022']
    else:
         return ['MUNIC','Atlas BR 2019']

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

