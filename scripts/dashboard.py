import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

engine = create_engine(
    'postgresql://postgres:cyq9ZwU3UcPksLP@localhost:5432/db_escola')

st.set_page_config(page_title="DataSchoolAnalyzer", layout="wide")

# Toda Carga e Lógica da engenharia...
df = pd.read_sql('dw_escola_completo', engine)
df['status'] = df['nota'].apply(
    lambda x: '✅ Aprovado' if x >= 6.0 else '❌ Reprovado')

# Sidebar que mostra os filtros...
st.sidebar.header("Filtros de Pesquisa")
disciplina_selecionada = st.sidebar.multiselect(
    "Selecione as Disciplinas:",
    options=df['disciplina'].unique(),
    default=df['disciplina'].unique()
)

# Dados filtrados
df_filtrado = df[df['disciplina'].isin(disciplina_selecionada)]

# Cálculo de Métricas
nota_media = df_filtrado['nota'].mean()
taxa_aprovacao = (
    len(df_filtrado[df_filtrado['nota'] >= 6]) / len(df_filtrado)) * 100

# Layout do Dashboard
st.title("📊 Painel de Desempenho Escolar (25 Alunos)")

m1, m2, m3 = st.columns(3)
m1.metric("Média Geral", f"{nota_media:.1f}")
m2.metric("Nota Máxima", f"{df_filtrado['nota'].max()}")
m3.metric("Taxa de Aprovação", f"{taxa_aprovacao:.1f}%")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Média por Disciplina vs Internet")
    fig_disc = px.bar(df_filtrado, x='disciplina', y='nota', color='acesso_internet',
                      barmode='group', title="Impacto Digital por Matéria",
                      color_discrete_map={True: '#2ecc71', False: '#e74c3c'})

    st.plotly_chart(fig_disc, width='stretch')

with col2:
    st.subheader("Distribuição de Status")

    fig_pizza = px.pie(df_filtrado, names='status', title="Proporção de Aprovados",
                       color='status',
                       color_discrete_map={'✅ Aprovado': 'blue', '❌ Reprovado': 'red'})
    st.plotly_chart(fig_pizza, width='stretch')

st.subheader("📋 Base de Dados Completa")

st.dataframe(df_filtrado[['nome', 'disciplina', 'nota',
             'status', 'acesso_internet']], width='stretch')
