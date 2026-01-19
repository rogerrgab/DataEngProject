# 📊 DataSchoolAnalyzer - Projeto Extensionista

Este projeto automatiza o monitoramento e a análise da inclusão digital em escolas públicas.

## 🚀 Como instalar e rodar (Windows, Debian, Ubuntu, Mint, Fedora)

Siga os passos abaixo para instalar todas as dependências com um único comando:

### 1. Instalar Bibliotecas do Python
Abra o seu terminal (CMD, PowerShell ou Terminal Linux) e rode:
```bash
pip install -r requirements.txt```

### 2. Configurar o Banco de Dados
Certifique-se de que o PostgreSQL está rodando e que você criou o banco db_escola

### 3. Executar o Pipeline

Rode os scripts(terminal Linux/Windows/VSCode) na ordem exata para processar os dados:

    python3 popular_banco.py (Gera 25 alunos e notas)

    python3 analise_escola.py (Faz o ETL e processa indicadores)

    streamlit run dashboard.py (Abre o painel interativo)

###Ou então se quiser rodar os scripts .py na pasta raíz(root) sem estar dentro da pasta scripts/, faça o seguinte:
# Para popular o banco
python scripts/popular_banco.py

# Para rodar o ETL
python scripts/analise_escola.py

# Para abrir o Dashboard
streamlit run scripts/dashboard.py
