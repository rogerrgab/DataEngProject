@echo off
echo 🚀 Iniciando setup do DataSchoolAnalyzer para Windows...

:: Criando ambiente virtual se n existir
if not exist venv (
    echo 🐍 Criando ambiente virtual...
    python -m venv venv
)

:: Ativando ambiente virtual
echo 🔌 Ativando ambiente virtual...
call venv\Scripts\activate

:: Garantindo q estamos usando o pip do venv p/ instalar e atualizar
echo 📦 Instalando/Atualizando dependências...
python -m pip install --upgrade pip
pip install -r requirements.txt

:: Executando scripts usando o python do venv de forma explícita
echo 🗄️ Populando o Banco de Dados...
python scripts\popular_banco.py

echo ⚙️ Executando Transformação (ETL)...
python scripts\analise_escola.py

:: Executando Streamlit
echo 📊 Abrindo o Dashboard...
:: Usando 'python -m streamlit' para garantir que ele use o pacote instalado no venv
python -m streamlit run scripts\dashboard.py

pause