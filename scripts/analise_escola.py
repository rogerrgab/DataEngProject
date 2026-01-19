import pandas as pd
from sqlalchemy import create_engine

# Fazendo conexão com o PostgreSQL assim como fiz no script 'popular_banco.py'
engine = create_engine(
    'postgresql://postgres:cyq9ZwU3UcPksLP@localhost:5432/db_escola')

print("Iniciando processo de ETL para Análise de Inclusão...")

try:
    # 1. EXTRAÇÃO: Vamos ler os dados q acabamos de inserir...
    df_alunos = pd.read_sql('tb_alunos', engine)
    df_notas = pd.read_sql('tb_notas', engine)
    df_social = pd.read_sql('tb_socioeconomico', engine)

    # 2. TRANSFORMAÇÃO: Fazendo o Cruzamento dos Dados(Merge)
    # Irei unir Alunos + Notas + Social em uma única "tabela completa" de análise
    df_final = pd.merge(df_alunos, df_notas, on='id_aluno')
    df_final = pd.merge(df_final, df_social, on='id_aluno')

    # Criando um insight: Média de notas por acesso à internet...Isso responde de maneira direta ao objetivo do meu Projeto Extensionista...
    analise_inclusao = df_final.groupby('acesso_internet')[
        'nota'].mean().reset_index()
    analise_inclusao.columns = ['tem_internet', 'media_nota']

    print("\n--- Insight Gerado: Média de Notas vs Internet ---")
    print(analise_inclusao)

    # 3. CARGA: Aqui estou salvando o resultado em uma tabela de Analytics (dw_desempenho_escolar)
    analise_inclusao.to_sql('dw_desempenho_escolar',
                            engine, if_exists='replace', index=False)

    # Salvando também a "tabela completa" para o nosso Dashboard...
    df_final.to_sql('dw_escola_completo', engine,
                    if_exists='replace', index=False)

    print("\n✅ Processo de ETL Finalizado! Dados transformados e salvos no Analytics Layer.")

except Exception as e:
    print(f"❌ Erro durante a transformação: {e}")
