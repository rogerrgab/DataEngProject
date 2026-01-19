import pandas as pd
from sqlalchemy import create_engine, text
import random

engine = create_engine(
    'postgresql://postgres:cyq9ZwU3UcPksLP@localhost:5432/db_escola')

disciplinas = ['Matemática', 'Português', 'Inglês', 'História', 'Geografia']
nomes_base = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia',
              'Kevin', 'Larissa', 'Maurício', 'Nathalia', 'Otávio', 'Paula', 'Ricardo', 'Sabrina', 'Tiago', 'Ursula',
              'Vitor', 'Wanessa', 'Xavier', 'Yasmim', 'Zeca']

try:
    # Limpeza de dados com o CASCADE...
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS tb_notas CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS tb_socioeconomico CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS tb_alunos CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS tb_frequencia CASCADE;"))
        conn.commit()

    # 1. Tabela de Alunos
    df_alunos = pd.DataFrame({
        'id_aluno': range(1, 26),
        'nome': [f"{nome} {random.choice(['Silva', 'Santos', 'Oliveira', 'Souza', 'Lima'])}" for nome in nomes_base],
        'idade': [random.randint(13, 17) for _ in range(25)]
    })

    # 2. Tabela Socioeconômica
    df_social = pd.DataFrame({
        'id_aluno': range(1, 26),
        'renda_familiar': [random.choice(['Baixa', 'Média', 'Alta']) for _ in range(25)],
        'acesso_internet': [True if i % 2 == 0 else False for i in range(1, 26)]
    })

    # 3. Tabela de Notas
    notas_lista = []
    for id_aluno in range(1, 26):
        tem_internet = df_social.loc[df_social['id_aluno']
                                     == id_aluno, 'acesso_internet'].values[0]
        for disc in disciplinas:
            base = 7.0 if tem_internet else 5.0
            nota = min(10, max(0, base + random.uniform(-2.5, 3.0)))
            notas_lista.append(
                {'id_aluno': id_aluno, 'disciplina': disc, 'nota': round(nota, 1)})

    df_notas = pd.DataFrame(notas_lista)

    # Salvando os dados no Postgres
    df_alunos.to_sql('tb_alunos', engine, if_exists='append', index=False)
    df_notas.to_sql('tb_notas', engine, if_exists='append', index=False)
    df_social.to_sql('tb_socioeconomico', engine,
                     if_exists='append', index=False)

    print("✅ Sucesso! O banco foi limpo e atualizado com 25 alunos.")

except Exception as e:
    print(f"Erro ao popular banco: {e}")
