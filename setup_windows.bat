@echo off
echo 🚀 Iniciando setup do DataSchoolAnalyzer para Windows...

:: 1. Instala dependências
echo 📦 Instalando bibliotecas...
pip install -r requirements.txt

:: 2. Executa o Pipeline
echo 🗄️ Populando o Banco de Dados...
python scripts/popular_banco.py

echo ⚙️ Executando Transformação (ETL)...
python scripts/analise_escola.py

echo 📊 Abrindo o Dashboard...
streamlit run scripts/dashboard.py
pause
