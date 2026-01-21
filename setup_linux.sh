#!/bin/bash

echo "🚀 Iniciando setup do DataSchoolAnalyzer para Linux (Mint/Debian/Ubuntu)..."

# 1. Instalar dependências do sistema para o Python venv
sudo apt update
sudo apt install python3-venv python3-pip -y

# 2. Criar o ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# 3. Ativar o ambiente e instalar bibliotecas
echo "🛠️ Instalando bibliotecas no ambiente isolado..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 4. Rodar os scripts de dados
echo "🗄️ Populando o Banco de Dados..."
python3 scripts/popular_banco.py

echo "⚙️ Executando Transformação (ETL)..."
python3 scripts/analise_escola.py

# 5. Abrir o Dashboard
echo "📊 Abrindo o Dashboard..."
streamlit run scripts/dashboard.py 