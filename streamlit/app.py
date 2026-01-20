"""
Datathon FIAP - Passos Mágicos
Aplicação Streamlit para Predição de Risco de Defasagem

Esta aplicação permite:
1. Visualizar análises exploratórias dos dados
2. Prever o risco de defasagem de alunos com base nos indicadores
3. Explorar os insights do modelo preditivo

Classificação de Risco (Metodologia Passos Mágicos):
- Sem Risco: Aluno em fase ou adiantado (D >= 0)
- Risco Moderado: Aluno 1-2 fases atrasado (0 > D >= -2)
- Risco Severo: Aluno 3+ fases atrasado (D < -2)
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from pathlib import Path

# Diretório base (onde está o app.py)
BASE_DIR = Path(__file__).parent

# Configuração da página
st.set_page_config(
    page_title="Passos Mágicos - Análise de Risco",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A5F;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .risk-severe {
        background-color: #8b1a1a;
        border-left: 5px solid #e74c3c;
        padding: 1rem;
        border-radius: 5px;
        color: white;
    }
    .risk-severe h3, .risk-severe p, .risk-severe strong {
        color: white;
    }
    .risk-moderate {
        background-color: #b8860b;
        border-left: 5px solid #f39c12;
        padding: 1rem;
        border-radius: 5px;
        color: white;
    }
    .risk-moderate h3, .risk-moderate p, .risk-moderate strong {
        color: white;
    }
    .risk-low {
        background-color: #1a5c2e;
        border-left: 5px solid #2ecc71;
        padding: 1rem;
        border-radius: 5px;
        color: white;
    }
    .risk-low h3, .risk-low p, .risk-low strong {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Funções auxiliares
@st.cache_resource
def carregar_modelo():
    """Carrega o modelo treinado e o scaler"""
    try:
        with open(BASE_DIR / 'modelo_risco_defasagem.pkl', 'rb') as f:
            modelo = pickle.load(f)
        with open(BASE_DIR / 'scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        with open(BASE_DIR / 'features.txt', 'r') as f:
            features = f.read().strip().split(',')
        # Carregar info do modelo se existir
        try:
            with open(BASE_DIR / 'modelo_info.pkl', 'rb') as f:
                modelo_info = pickle.load(f)
        except:
            modelo_info = None
        return modelo, scaler, features, modelo_info
    except Exception as e:
        st.error(f"Erro ao carregar modelo: {e}")
        return None, None, None, None

@st.cache_data
def carregar_dados():
    """Carrega os dados do PEDE"""
    try:
        # Tentar carregar arquivo único primeiro
        df = pd.read_excel(BASE_DIR / 'BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx')
        return df, None, None
    except:
        try:
            xlsx = pd.ExcelFile(BASE_DIR / 'BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx')
            df_2022 = pd.read_excel(xlsx, sheet_name='PEDE2022')
            df_2023 = pd.read_excel(xlsx, sheet_name='PEDE2023')
            df_2024 = pd.read_excel(xlsx, sheet_name='PEDE2024')
            return df_2022, df_2023, df_2024
        except:
            return None, None, None

def prever_risco(modelo, scaler, features, indicadores):
    """
    Realiza a predição de risco para um aluno
    
    Retorna:
    - classe: 0 (Sem Risco), 1 (Risco Moderado), 2 (Risco Severo)
    - probabilidades: array com probabilidade de cada classe
    """
    # Criar array de features na ordem correta
    X = np.array([[indicadores[f] for f in features]])
    
    # Normalizar
    X_scaled = scaler.transform(X)
    
    # Predição
    classe = modelo.predict(X_scaled)[0]
    probabilidades = modelo.predict_proba(X_scaled)[0]
    
    return classe, probabilidades

def get_classe_nome(classe):
    """Retorna o nome da classe de risco"""
    nomes = {0: 'Sem Risco', 1: 'Risco Moderado', 2: 'Risco Severo'}
    return nomes.get(classe, 'Desconhecido')

def get_classe_cor(classe):
    """Retorna a cor associada à classe de risco"""
    cores = {0: '#2ecc71', 1: '#f39c12', 2: '#e74c3c'}
    return cores.get(classe, '#95a5a6')

# Sidebar
st.sidebar.image("https://passosmagicos.org.br/wp-content/uploads/2021/09/logo-passos-magicos.png", width=200)
st.sidebar.title("🎓 Navegação")

pagina = st.sidebar.radio(
    "Selecione a página:",
    ["🏠 Início", "📊 Dashboard", "🔮 Predição de Risco", "📈 Sobre o Modelo", "ℹ️ Sobre"]
)

# Carregar modelo
modelo, scaler, features, modelo_info = carregar_modelo()

# Páginas
if pagina == "🏠 Início":
    st.markdown('<p class="main-header">🎓 Passos Mágicos</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Sistema de Análise e Predição de Risco de Defasagem Educacional</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Análise de Dados
        Explore os indicadores educacionais dos alunos da Passos Mágicos através de visualizações interativas.
        """)
    
    with col2:
        st.markdown("""
        ### 🔮 Predição de Risco
        Utilize nosso modelo de Machine Learning para identificar alunos em risco de defasagem educacional.
        """)
    
    with col3:
        st.markdown("""
        ### 📈 Insights
        Descubra os fatores que mais influenciam o desenvolvimento educacional dos alunos.
        """)
    
    st.divider()
    
    st.markdown("""
    ## Sobre a Associação Passos Mágicos
    
    A **Associação Passos Mágicos** tem uma trajetória de 32 anos de atuação, trabalhando na transformação 
    da vida de crianças e jovens de baixa renda em Embu-Guaçu. A missão da organização é promover a 
    educação de qualidade como ferramenta de transformação social.
    
    ### Indicadores Avaliados (PEDE)
    
    | Indicador | Descrição |
    |-----------|-----------|
    | **IDA** | Indicador de Desempenho Acadêmico |
    | **IEG** | Indicador de Engajamento |
    | **IAA** | Indicador de Autoavaliação |
    | **IPS** | Indicador Psicossocial |
    | **IPP** | Indicador Psicopedagógico |
    | **IPV** | Indicador de Ponto de Virada |
    | **INDE** | Índice de Desenvolvimento Educacional (global) |
    
    ### Classificação de Risco de Defasagem
    
    | Classificação | Defasagem (D) | Descrição |
    |---------------|---------------|-----------|
    | **Sem Risco** | D ≥ 0 | Aluno em fase adequada ou adiantado |
    | **Risco Moderado** | 0 > D ≥ -2 | Aluno 1-2 fases atrasado |
    | **Risco Severo** | D < -2 | Aluno 3+ fases atrasado |
    """)

elif pagina == "📊 Dashboard":
    st.markdown('<p class="main-header">📊 Dashboard de Indicadores</p>', unsafe_allow_html=True)
    
    # Carregar dados
    df_data = carregar_dados()
    
    if df_data[0] is not None:
        df = df_data[0]
        
        # Renomear colunas
        col_map = {}
        for col in df.columns:
            col_lower = col.lower()
            if col_lower == 'iaa': col_map[col] = 'IAA'
            elif col_lower == 'ieg' and 'destaque' not in col_lower: col_map[col] = 'IEG'
            elif col_lower == 'ips': col_map[col] = 'IPS'
            elif col_lower == 'ida' and 'destaque' not in col_lower: col_map[col] = 'IDA'
            elif col_lower == 'ipv' and 'destaque' not in col_lower: col_map[col] = 'IPV'
            elif col_lower == 'ian': col_map[col] = 'IAN'
            elif 'defas' in col_lower: col_map[col] = 'DEFASAGEM'
        
        if 'INDE 22' in df.columns:
            col_map['INDE 22'] = 'INDE'
        
        df = df.rename(columns=col_map)
        
        # Converter para numérico
        for col in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPV', 'IAN', 'DEFASAGEM']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Criar classificação de risco
        def classificar_risco(d):
            if pd.isna(d):
                return None
            if d >= 0:
                return 'Sem Risco'
            elif d >= -2:
                return 'Risco Moderado'
            else:
                return 'Risco Severo'
        
        df['CLASSE_RISCO'] = df['DEFASAGEM'].apply(classificar_risco)
        
        # Métricas principais
        st.subheader("📊 Visão Geral dos Dados")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total de Alunos", f"{len(df):,}")
        
        with col2:
            inde_medio = df['INDE'].mean()
            st.metric("INDE Médio", f"{inde_medio:.2f}")
        
        with col3:
            pct_risco = (df['DEFASAGEM'] < 0).mean() * 100
            st.metric("% em Defasagem", f"{pct_risco:.1f}%")
        
        with col4:
            pct_severo = (df['DEFASAGEM'] < -2).mean() * 100
            st.metric("% Risco Severo", f"{pct_severo:.1f}%")
        
        st.divider()
        
        # Distribuição de Risco
        st.subheader("🎯 Distribuição por Classificação de Risco")
        
        col1, col2 = st.columns(2)
        
        with col1:
            risco_counts = df['CLASSE_RISCO'].value_counts()
            cores = {'Sem Risco': '#2ecc71', 'Risco Moderado': '#f39c12', 'Risco Severo': '#e74c3c'}
            
            fig = px.pie(
                values=risco_counts.values,
                names=risco_counts.index,
                title='Distribuição de Risco',
                color=risco_counts.index,
                color_discrete_map=cores
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.bar(
                x=risco_counts.index,
                y=risco_counts.values,
                title='Quantidade de Alunos por Classificação',
                color=risco_counts.index,
                color_discrete_map=cores,
                labels={'x': 'Classificação', 'y': 'Quantidade'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Indicadores por Classificação de Risco
        st.subheader("📈 Média dos Indicadores por Classificação de Risco")
        
        indicadores = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'INDE']
        indicadores_existentes = [i for i in indicadores if i in df.columns]
        
        media_por_risco = df.groupby('CLASSE_RISCO')[indicadores_existentes].mean()
        
        fig = go.Figure()
        
        for risco in ['Sem Risco', 'Risco Moderado', 'Risco Severo']:
            if risco in media_por_risco.index:
                fig.add_trace(go.Bar(
                    name=risco,
                    x=indicadores_existentes,
                    y=media_por_risco.loc[risco].values,
                    marker_color=cores[risco]
                ))
        
        fig.update_layout(
            title='Comparação de Indicadores por Classificação de Risco',
            barmode='group',
            xaxis_title='Indicador',
            yaxis_title='Média'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Insights
        st.info("""
        **💡 Insights:**
        - Alunos em **Risco Severo** tendem a ter indicadores mais baixos em todas as dimensões
        - O **IEG (Engajamento)** mostra diferença significativa entre as classificações
        - O **INDE** reflete bem a classificação de risco geral
        """)
        
    else:
        st.warning("Dados não disponíveis. Por favor, faça upload do arquivo de dados.")

elif pagina == "🔮 Predição de Risco":
    st.markdown('<p class="main-header">🔮 Predição de Risco de Defasagem</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Insira os indicadores do aluno para avaliar o risco de defasagem</p>', unsafe_allow_html=True)
    
    if modelo is not None:
        st.info("""
        ℹ️ **Como funciona:** O modelo analisa os indicadores do aluno e identifica padrões 
        associados a alunos em defasagem. Isso permite uma **intervenção preventiva** antes 
        que a defasagem aconteça.
        """)
        
        st.markdown("### 📝 Indicadores do Aluno")
        st.caption("Insira os valores dos indicadores (escala de 0 a 10)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ida = st.slider("IDA - Desempenho Acadêmico", 0.0, 10.0, 5.0, 0.1,
                           help="Média das notas de Matemática, Português e Inglês")
            ieg = st.slider("IEG - Engajamento", 0.0, 10.0, 5.0, 0.1,
                           help="Participação em tarefas e atividades")
        
        with col2:
            iaa = st.slider("IAA - Autoavaliação", 0.0, 10.0, 5.0, 0.1,
                           help="Autoavaliação do aluno sobre seu desempenho")
            ips = st.slider("IPS - Psicossocial", 0.0, 10.0, 5.0, 0.1,
                           help="Avaliação comportamental, emocional e social")
        
        with col3:
            ipv = st.slider("IPV - Ponto de Virada", 0.0, 10.0, 5.0, 0.1,
                           help="Análise de progresso e desenvolvimento")
            inde = st.slider("INDE - Índice de Desenvolvimento", 0.0, 10.0, 5.0, 0.1,
                            help="Índice geral de desenvolvimento educacional")
        
        st.divider()
        
        if st.button("🔍 Analisar Risco", type="primary", use_container_width=True):
            # Preparar indicadores
            indicadores = {
                'IDA': ida, 'IEG': ieg, 'IAA': iaa,
                'IPS': ips, 'IPV': ipv, 'INDE': inde
            }
            
            # Fazer predição
            classe, probabilidades = prever_risco(modelo, scaler, features, indicadores)
            
            st.divider()
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Gauge de probabilidade da classe predita
                prob_classe = probabilidades[classe] * 100
                
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = prob_classe,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': f"Confiança: {get_classe_nome(classe)}"},
                    number = {'suffix': '%'},
                    gauge = {
                        'axis': {'range': [0, 100]},
                        'bar': {'color': get_classe_cor(classe)},
                        'steps': [
                            {'range': [0, 33], 'color': "#f8d7da"},
                            {'range': [33, 66], 'color': "#fff3cd"},
                            {'range': [66, 100], 'color': "#d4edda"}
                        ]
                    }
                ))
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)
                
                # Probabilidades de cada classe
                st.markdown("**Probabilidades por Classe:**")
                prob_df = pd.DataFrame({
                    'Classe': ['Sem Risco', 'Risco Moderado', 'Risco Severo'],
                    'Probabilidade': [f"{p*100:.1f}%" for p in probabilidades]
                })
                st.dataframe(prob_df, hide_index=True, use_container_width=True)
            
            with col2:
                if classe == 2:  # Risco Severo
                    st.markdown("""
                    <div class="risk-severe">
                        <h3>🚨 RISCO SEVERO</h3>
                        <p>O modelo identificou que este aluno apresenta padrões associados a <strong>defasagem severa</strong> (3+ fases atrasado).</p>
                        <p><strong>Confiança:</strong> {:.1f}%</p>
                    </div>
                    """.format(prob_classe), unsafe_allow_html=True)
                    
                    st.markdown("""
                    ### ⚠️ Ações Recomendadas:
                    - 🚨 **Intervenção imediata** necessária
                    - 📚 Acompanhamento pedagógico intensivo
                    - 👥 Suporte psicossocial urgente
                    - 📊 Monitoramento semanal dos indicadores
                    - 🎯 Plano de recuperação personalizado
                    """)
                    
                elif classe == 1:  # Risco Moderado
                    st.markdown("""
                    <div class="risk-moderate">
                        <h3>⚠️ RISCO MODERADO</h3>
                        <p>O modelo identificou que este aluno apresenta padrões associados a <strong>defasagem moderada</strong> (1-2 fases atrasado).</p>
                        <p><strong>Confiança:</strong> {:.1f}%</p>
                    </div>
                    """.format(prob_classe), unsafe_allow_html=True)
                    
                    st.markdown("""
                    ### ⚠️ Ações Recomendadas:
                    - 📋 Acompanhamento pedagógico regular
                    - 👥 Suporte psicossocial
                    - 📊 Monitoramento quinzenal dos indicadores
                    - 🎯 Plano de desenvolvimento personalizado
                    - 🌟 Incentivar participação em atividades
                    """)
                    
                else:  # Sem Risco
                    st.markdown("""
                    <div class="risk-low">
                        <h3>✅ SEM RISCO</h3>
                        <p>O modelo indica que este aluno apresenta padrões associados a alunos <strong>em fase adequada</strong>.</p>
                        <p><strong>Confiança:</strong> {:.1f}%</p>
                    </div>
                    """.format(prob_classe), unsafe_allow_html=True)
                    
                    st.markdown("""
                    ### ✅ Recomendações:
                    - 📈 Manter acompanhamento regular
                    - 🌟 Incentivar participação em atividades
                    - 🎯 Estabelecer metas de desenvolvimento
                    - 📊 Monitoramento mensal dos indicadores
                    """)
            
            # Radar chart dos indicadores
            st.subheader("📊 Perfil do Aluno")
            
            col1, col2 = st.columns(2)
            
            with col1:
                categorias = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'INDE']
                valores = [ida, ieg, iaa, ips, ipv, inde]
                
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=valores + [valores[0]],
                    theta=categorias + [categorias[0]],
                    fill='toself',
                    name='Aluno',
                    line_color=get_classe_cor(classe)
                ))
                
                # Adicionar média de referência
                fig.add_trace(go.Scatterpolar(
                    r=[5, 5, 5, 5, 5, 5, 5],
                    theta=categorias + [categorias[0]],
                    fill='toself',
                    name='Média (5.0)',
                    line_color='#95a5a6',
                    opacity=0.3
                ))
                
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                    showlegend=True,
                    title='Radar de Indicadores'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Barras comparativas
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=categorias,
                    y=valores,
                    name='Aluno',
                    marker_color=get_classe_cor(classe)
                ))
                fig.add_trace(go.Bar(
                    x=categorias,
                    y=[5, 5, 5, 5, 5, 5],
                    name='Média',
                    marker_color='#95a5a6',
                    opacity=0.5
                ))
                fig.update_layout(
                    title='Comparação com a Média',
                    barmode='group',
                    yaxis_range=[0, 10]
                )
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Modelo não carregado. Verifique se os arquivos do modelo estão disponíveis.")

elif pagina == "📈 Sobre o Modelo":
    st.markdown('<p class="main-header">📈 Sobre o Modelo Preditivo</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Metodologia
    
    O modelo de predição de risco de defasagem foi desenvolvido utilizando técnicas de Machine Learning
    para identificar padrões nos indicadores educacionais que possam indicar alunos em risco.
    
    ### Objetivo
    
    Identificar **padrões nos indicadores** (IDA, IEG, IAA, IPS, IPV, INDE) que estão associados 
    a alunos em defasagem, permitindo **intervenção preventiva** antes que a defasagem aconteça.
    
    ### Algoritmo Utilizado
    
    **Random Forest Classifier** - Um ensemble de árvores de decisão que combina múltiplas árvores
    para fazer predições mais robustas e precisas.
    
    ### Classes de Predição
    
    | Classe | Descrição | Defasagem (D) |
    |--------|-----------|---------------|
    | **Sem Risco** | Aluno em fase adequada ou adiantado | D ≥ 0 |
    | **Risco Moderado** | Aluno 1-2 fases atrasado | 0 > D ≥ -2 |
    | **Risco Severo** | Aluno 3+ fases atrasado | D < -2 |
    
    ### Features Utilizadas
    
    O modelo utiliza **apenas os indicadores de desempenho**, sem incluir o IAN (que é derivado da defasagem):
    
    | Feature | Descrição |
    |---------|-----------|
    | **IDA** | Indicador de Desempenho Acadêmico |
    | **IEG** | Indicador de Engajamento |
    | **IAA** | Indicador de Autoavaliação |
    | **IPS** | Indicador Psicossocial |
    | **IPV** | Indicador de Ponto de Virada |
    | **INDE** | Índice de Desenvolvimento Educacional |
    
    ### Métricas de Desempenho
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Acurácia Geral", "75.6%", help="Proporção de predições corretas")
    with col2:
        st.metric("Recall (Sem Risco)", "69%", help="Capacidade de identificar alunos sem risco")
    with col3:
        st.metric("Recall (Risco Moderado)", "82%", help="Capacidade de identificar alunos em risco moderado")
    
    st.markdown("""
    ### Importância das Features
    
    O gráfico abaixo mostra quais indicadores têm maior influência na predição de risco:
    """)
    
    # Gráfico de importância (valores do modelo treinado)
    features_imp = {
        'INDE': 0.347,
        'IPV': 0.161,
        'IDA': 0.152,
        'IAA': 0.127,
        'IEG': 0.117,
        'IPS': 0.096
    }
    
    fig = px.bar(
        x=list(features_imp.values()),
        y=list(features_imp.keys()),
        orientation='h',
        title='Importância das Features no Modelo',
        labels={'x': 'Importância', 'y': 'Feature'},
        color=list(features_imp.values()),
        color_continuous_scale='Blues'
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### Interpretação
    
    - **INDE** é o indicador mais importante (34.7%), pois representa o índice geral de desenvolvimento
    - **IPV** (Ponto de Virada) é o segundo mais importante (16.1%), indicando a relevância do progresso
    - **IDA** (Desempenho Acadêmico) tem peso significativo (15.2%)
    - **IAA** e **IEG** contribuem de forma similar (~12% cada)
    
    ### Como o Modelo Funciona
    
    1. O modelo foi treinado com dados de alunos que **já possuem classificação de defasagem**
    2. Ele aprendeu quais **padrões de indicadores** estão associados a cada nível de risco
    3. Quando um novo aluno é avaliado, o modelo compara seus indicadores com os padrões aprendidos
    4. Isso permite identificar alunos em risco **antes** que a defasagem aconteça
    
    ### Limitações
    
    - O modelo foi treinado com dados de 2024
    - A precisão pode variar para perfis de alunos muito diferentes dos dados de treino
    - Recomenda-se usar as predições como **apoio à decisão**, não como única fonte
    - O modelo não substitui a avaliação profissional dos educadores
    """)

elif pagina == "ℹ️ Sobre":
    st.markdown('<p class="main-header">ℹ️ Sobre o Projeto</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Datathon FIAP - Passos Mágicos
    
    Este projeto foi desenvolvido como parte do Datathon da FIAP, com o objetivo de analisar
    os dados educacionais da Associação Passos Mágicos e criar ferramentas para apoiar
    a identificação de alunos em risco de defasagem.
    
    ### Objetivo
    
    Construir uma aplicação no Streamlit para disponibilizar o modelo treinado para a Passos Mágicos 
    utilizar como solução preditiva via aplicação de dados.
    
    ### Equipe
    
    - **Curso:** Pós-Tech em Data Analytics
    - **Instituição:** FIAP
    - **Fase:** 5 - Deep Learning e Analytics
    
    ### Tecnologias Utilizadas
    
    - **Python** - Linguagem de programação
    - **Pandas/NumPy** - Análise de dados
    - **Scikit-learn** - Machine Learning
    - **Streamlit** - Interface web
    - **Plotly** - Visualizações interativas
    
    ### Repositório
    
    O código fonte está disponível no GitHub:
    - 📁 [github.com/LeandroCrespo/bolao-copa-2026](https://github.com/LeandroCrespo/bolao-copa-2026)
    
    ### Contato
    
    Para mais informações sobre a Associação Passos Mágicos:
    - 🌐 [passosmagicos.org.br](https://passosmagicos.org.br)
    
    ---
    
    *Desenvolvido com ❤️ para transformar vidas através da educação*
    """)

# Footer
st.sidebar.divider()
st.sidebar.markdown("---")
st.sidebar.markdown("**Datathon FIAP 2024**")
st.sidebar.markdown("Passos Mágicos")
