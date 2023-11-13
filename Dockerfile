# Use uma imagem base que tenha o Python e o pip instalados
FROM python:3.8

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instalação das dependências necessárias
RUN pip install --upgrade pip
RUN pip install streamlit

# Clona o repositório do GitHub
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/AbilioNB/app_portal_dados .

# Instala as dependências do projeto, se houver um arquivo requirements.txt
RUN pip install -r requirements.txt

# Expondo a porta necessária para o Streamlit (por padrão, é a porta 8501)
EXPOSE 8501

# Comando para executar o aplicativo Streamlit
CMD ["streamlit", "run", "nome_do_arquivo_streamlit.py"]