Portal de dados teste 
## Passos para Execução

### 1. Alterar a Branch

Certifique-se de estar na branch correta do projeto. Se você precisar mudar para a branch `monopage_app`, para a versão de uma pagina e `multipage_app` para multipagina.

```bash
git checkout monopage_app
```

### 2. Criar e ativar a venv

```bash
python -m venv venv
```
#### Ativando a venv Windows

```bash
.\venv\Scripts\activate
```

#### Ativando a venv MAC

```bash
source venv/bin/activate
```

### 3.Instalar Requerimentos

```bash
pip install -r requirements.txt
```

### 5.Executar a aplicação

```bash
streamlit run app.py
```
