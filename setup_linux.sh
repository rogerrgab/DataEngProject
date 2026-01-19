#!/bin/bash

echo "🚀 Iniciando setup do DataSchoolAnalyzer para Linux..."

# 1. Instala dependências do Python
echo "📦 Instalando bibliotecas..."
pip install -r requirements.txt

# 2. Executa o Pipeline em ordem
echo "🗄️ Populando o Banco de Dados..."
python3 scripts/popular_banco.py

echo "⚙️ Executando Transformação (ETL)..."
python3 scripts/analise_escola.py

echo "📊 Abrindo o Dashboard..."
streamlit run scripts/dashboard.py
