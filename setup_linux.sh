#!/bin/bash

echo "🚀 Iniciando setup do DataSchoolAnalyzer para Linux (Debian/Ubuntu/Mint)..."

# 1. Instalar dependências de sistema
sudo apt update
sudo apt install python3-venv python3-pip -y

# 2. Criar o ambiente virtual (venv)
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# 3. Instalar as bibliotecas USANDO O PIP DO VENV (Isso evita o erro de externally-managed)
echo "🛠️ Instalando bibliotecas no ambiente isolado..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# 4. Rodar os scripts usando o python do venv
echo "🗄️ Populando o Banco de Dados..."
./venv/bin/python3 scripts/popular_banco.py

echo "⚙️ Executando Transformação (ETL)..."
./venv/bin/python3 scripts/analise_escola.py

# 5. Abrir o Dashboard
echo "📊 Abrindo o Dashboard..."
./venv/bin/streamlit run main.py