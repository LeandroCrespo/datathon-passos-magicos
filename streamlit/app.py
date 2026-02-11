"""
Datathon FIAP - Passos Mágicos
Dashboard de Análise e Predição de Risco de Defasagem

Autor: Leandro Leme Crespo
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle
import os
import pathlib

# Configuração da página
st.set_page_config(
    page_title="Datathon - Passos Mágicos",
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
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .risk-high {
        background-color: #991B1B;
        border-left: 4px solid #EF4444;
        padding: 1rem;
        border-radius: 5px;
        color: #ffffff;
    }
    .risk-high h2 { color: #FCA5A5; margin-bottom: 10px; }
    .risk-high p { color: #ffffff; }
    .risk-moderate {
        background-color: #92400E;
        border-left: 4px solid #F59E0B;
        padding: 1rem;
        border-radius: 5px;
        color: #ffffff;
    }
    .risk-moderate h2 { color: #FCD34D; margin-bottom: 10px; }
    .risk-moderate p { color: #ffffff; }
    .risk-attention {
        background-color: #854D0E;
        border-left: 4px solid #FBBF24;
        padding: 1rem;
        border-radius: 5px;
        color: #ffffff;
    }
    .risk-attention h2 { color: #FDE68A; margin-bottom: 10px; }
    .risk-attention p { color: #ffffff; }
    .risk-low {
        background-color: #166534;
        border-left: 4px solid #22C55E;
        padding: 1rem;
        border-radius: 5px;
        color: #ffffff;
    }
    .risk-low h2 { color: #86EFAC; margin-bottom: 10px; }
    .risk-low p { color: #ffffff; }
</style>
""", unsafe_allow_html=True)

# Função para carregar dados
@st.cache_data
def carregar_dados():
    """Carrega os dados do arquivo Excel"""
    try:
        paths = [
            'data/BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx',
            '../data/BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx',
            str(pathlib.Path(__file__).parent / 'BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx'),
            str(pathlib.Path(__file__).parent.parent / 'data' / 'BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx'),
        ]
        
        for path in paths:
            if os.path.exists(path):
                xlsx = pd.ExcelFile(path)
                all_data = []
                for sheet in xlsx.sheet_names:
                    df_year = pd.read_excel(xlsx, sheet_name=sheet)
                    df_year.columns = [c.upper() for c in df_year.columns]
                    if 'DEFAS' in df_year.columns:
                        df_year = df_year.rename(columns={'DEFAS': 'DEFASAGEM'})
                    df_year['ANO_PEDE'] = sheet.replace('PEDE', '')
                    all_data.append(df_year)
                return pd.concat(all_data, ignore_index=True)
        
        st.error("Arquivo de dados não encontrado!")
        return None
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

# Função para carregar modelo
@st.cache_resource
def carregar_modelo():
    """Carrega o modelo de ML treinado"""
    try:
        paths = [
            'streamlit/',
            './',
            '/home/ubuntu/datathon-passos-magicos/streamlit/'
        ]
        
        for base_path in paths:
            modelo_path = os.path.join(base_path, 'modelo_risco_defasagem.pkl')
            if os.path.exists(modelo_path):
                with open(modelo_path, 'rb') as f:
                    modelo = pickle.load(f)
                with open(os.path.join(base_path, 'scaler.pkl'), 'rb') as f:
                    scaler = pickle.load(f)
                with open(os.path.join(base_path, 'label_encoders.pkl'), 'rb') as f:
                    le_dict = pickle.load(f)
                with open(os.path.join(base_path, 'modelo_info.pkl'), 'rb') as f:
                    info = pickle.load(f)
                return modelo, scaler, le_dict, info
        
        return None, None, None, None
    except Exception as e:
        st.error(f"Erro ao carregar modelo: {e}")
        return None, None, None, None

def classificar_nivel_risco(prob):
    """Classifica o nível de risco baseado na probabilidade"""
    if prob < 0.30:
        return 'Sem Risco', '✅', 'risk-low'
    elif prob < 0.60:
        return 'Atenção', '⚡', 'risk-attention'
    elif prob < 0.85:
        return 'Risco Moderado', '⚠️', 'risk-moderate'
    else:
        return 'Risco Alto', '🚨', 'risk-high'

# Carregar dados e modelo
df = carregar_dados()
modelo, scaler, le_dict, modelo_info = carregar_modelo()

# Sidebar
_logo_path = pathlib.Path(__file__).parent / "logo_passos_magicos.png"
if _logo_path.exists():
    st.sidebar.image(str(_logo_path), width=200)
else:
    st.sidebar.title("🎓 Passos Mágicos")
st.sidebar.title("📊 Navegação")

pagina = st.sidebar.radio(
    "Selecione a página:",
    ["🏠 Visão Geral", "📈 Análise Exploratória", "🔮 Predição de Risco", "📋 Sobre o Projeto"]
)

# ==================== PÁGINA: VISÃO GERAL ====================
if pagina == "🏠 Visão Geral":
    st.markdown('<p class="main-header">🎓 Datathon FIAP - Passos Mágicos</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Análise de Indicadores Educacionais e Predição de Risco de Defasagem</p>', unsafe_allow_html=True)
    
    if df is not None:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total de Registros", f"{len(df):,}")
        with col2:
            anos = df['ANO_PEDE'].nunique()
            st.metric("Anos Analisados", f"{anos}")
        with col3:
            if 'DEFASAGEM' in df.columns:
                df['DEFASAGEM'] = pd.to_numeric(df['DEFASAGEM'], errors='coerce')
                sem_risco = (df['DEFASAGEM'] >= 0).sum()
                st.metric("Sem Risco", f"{sem_risco:,}")
        with col4:
            if 'DEFASAGEM' in df.columns:
                com_risco = (df['DEFASAGEM'] < 0).sum()
                st.metric("Com Risco", f"{com_risco:,}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Distribuição por Ano")
            if 'ANO_PEDE' in df.columns:
                contagem = df['ANO_PEDE'].value_counts().sort_index()
                fig = px.bar(x=contagem.index, y=contagem.values, 
                            labels={'x': 'Ano', 'y': 'Quantidade'},
                            color=contagem.values, color_continuous_scale='Blues')
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 Distribuição de Risco")
            if 'DEFASAGEM' in df.columns:
                df_valid = df.dropna(subset=['DEFASAGEM'])
                sem_risco = (df_valid['DEFASAGEM'] >= 0).sum()
                com_risco = (df_valid['DEFASAGEM'] < 0).sum()
                
                fig = px.pie(values=[sem_risco, com_risco], 
                            names=['Sem Risco', 'Com Risco'],
                            color_discrete_sequence=['#22C55E', '#EF4444'])
                st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("📈 Indicadores Médios")
        indicadores = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'IPP']
        medias = []
        for ind in indicadores:
            if ind in df.columns:
                df[ind] = pd.to_numeric(df[ind], errors='coerce')
                medias.append(df[ind].mean())
            else:
                medias.append(0)
        
        fig = px.bar(x=indicadores, y=medias,
                    labels={'x': 'Indicador', 'y': 'Média'},
                    color=medias, color_continuous_scale='Viridis')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# ==================== PÁGINA: ANÁLISE EXPLORATÓRIA ====================
elif pagina == "📈 Análise Exploratória":
    st.markdown('<p class="main-header">📈 Análise Exploratória</p>', unsafe_allow_html=True)
    
    if df is not None:
        st.sidebar.subheader("Filtros")
        anos_disponiveis = sorted(df['ANO_PEDE'].unique())
        ano_selecionado = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)
        
        df_filtrado = df[df['ANO_PEDE'].isin(ano_selecionado)]
        
        st.subheader("🔗 Correlação entre Indicadores")
        indicadores = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'IPP']
        ind_disponiveis = [i for i in indicadores if i in df_filtrado.columns]
        df_ind = df_filtrado[ind_disponiveis].apply(pd.to_numeric, errors='coerce').dropna()
        
        if len(df_ind) > 0:
            corr = df_ind.corr()
            fig = px.imshow(corr, text_auto='.2f', aspect='auto',
                           color_continuous_scale='RdBu_r')
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("📊 Distribuição dos Indicadores")
        indicador_sel = st.selectbox("Selecione o indicador:", ind_disponiveis)
        
        if indicador_sel in df_filtrado.columns:
            df_filtrado[indicador_sel] = pd.to_numeric(df_filtrado[indicador_sel], errors='coerce')
            fig = px.histogram(df_filtrado, x=indicador_sel, nbins=30,
                              color_discrete_sequence=['#3B82F6'])
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("📊 Indicadores por Classe de Risco")
        if 'DEFASAGEM' in df_filtrado.columns:
            df_filtrado['DEFASAGEM'] = pd.to_numeric(df_filtrado['DEFASAGEM'], errors='coerce')
            df_filtrado['CLASSE_RISCO'] = df_filtrado['DEFASAGEM'].apply(
                lambda x: 'Sem Risco' if x >= 0 else 'Com Risco' if pd.notna(x) else None
            )
            
            df_risco = df_filtrado.dropna(subset=['CLASSE_RISCO'])
            
            media_risco = df_risco.groupby('CLASSE_RISCO')[ind_disponiveis].mean()
            
            fig = go.Figure()
            for classe in media_risco.index:
                fig.add_trace(go.Bar(
                    name=classe,
                    x=ind_disponiveis,
                    y=media_risco.loc[classe].values,
                    marker_color='#22C55E' if classe == 'Sem Risco' else '#EF4444'
                ))
            fig.update_layout(barmode='group')
            st.plotly_chart(fig, use_container_width=True)

# ==================== PÁGINA: PREDIÇÃO DE RISCO ====================
elif pagina == "🔮 Predição de Risco":
    st.markdown('<p class="main-header">🔮 Predição de Risco de Defasagem</p>', unsafe_allow_html=True)
    
    if modelo is not None and modelo_info is not None:
        st.success(f"✅ Modelo carregado: **{modelo_info['modelo_nome']}** | "
                   f"Acurácia: **{modelo_info['accuracy']*100:.1f}%** | "
                   f"AUC-ROC: **{modelo_info['auc_roc']*100:.1f}%** | "
                   f"CV: **{modelo_info.get('cv_accuracy_mean', 0)*100:.1f}% (+/- {modelo_info.get('cv_accuracy_std', 0)*100:.1f}%)**")
        
        st.markdown("---")
        st.subheader("📝 Insira os dados do aluno:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Indicadores PEDE**")
            ida = st.slider("IDA (Desempenho Acadêmico)", 0.0, 10.0, 7.0, 0.1)
            ieg = st.slider("IEG (Engajamento)", 0.0, 10.0, 7.0, 0.1)
            iaa = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 7.0, 0.1)
            ips = st.slider("IPS (Psicossocial)", 0.0, 10.0, 7.0, 0.1)
            ipv = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 7.0, 0.1)
        
        with col2:
            st.markdown("**Notas por Matéria**")
            mat = st.slider("Matemática", 0.0, 10.0, 7.0, 0.1)
            por = st.slider("Português", 0.0, 10.0, 7.0, 0.1)
        
        with col3:
            st.markdown("**Dados Contextuais**")
            idade = st.number_input("Idade", min_value=6, max_value=25, value=12)
            ano_ingresso = st.number_input("Ano de Ingresso", min_value=2015, max_value=2025, value=2022)
            genero_display = st.selectbox("Gênero", ["Feminino", "Masculino"])
            # Mapeamento: dados usam "Feminino"/"Menina" e "Masculino"/"Menino" dependendo do ano
            genero = genero_display  # O encoder conhece ambos os termos
            
            instituicao_opcoes = {
                "Pública": "Pública",
                "Privada": "Privada",
                "Privada - Programa de Apadrinhamento": "Privada - Programa de Apadrinhamento",
                "Privada com Bolsa 100%": "Privada *Parcerias com Bolsa 100%",
                "Privada - Empresa Parceira": "Privada - Pagamento por *Empresa Parceira",
                "Escola JP II": "Escola JP II",
                "Rede Decisão": "Rede Decisão",
                "Bolsista Universitário (Formado)": "Bolsista Universitário *Formado (a)",
                "Concluiu o 3º EM": "Concluiu o 3º EM",
                "Desconhecido": "Desconhecido",
                "Nenhuma das opções acima": "Nenhuma das opções acima"
            }
            instituicao_display = st.selectbox("Instituição de Ensino", list(instituicao_opcoes.keys()))
            instituicao = instituicao_opcoes[instituicao_display]
        
        st.markdown("---")
        
        # Níveis de risco explicação
        with st.expander("ℹ️ Como funciona a classificação por níveis de risco?"):
            st.markdown("""
            O modelo gera uma **probabilidade** de risco que é convertida em 4 níveis:
            
            | Probabilidade | Nível | Ação Sugerida |
            |---------------|-------|---------------|
            | < 30% | ✅ **Sem Risco** | Acompanhamento normal |
            | 30% - 60% | ⚡ **Atenção** | Monitoramento preventivo |
            | 60% - 85% | ⚠️ **Risco Moderado** | Intervenção pedagógica |
            | > 85% | 🚨 **Risco Alto** | Intervenção urgente |
            """)
        
        if st.button("🔮 Realizar Predição", type="primary", use_container_width=True):
            try:
                # Preparar dados
                genero_enc = le_dict['GÊNERO'].transform([genero])[0]
                instituicao_enc = le_dict['INSTITUIÇÃO DE ENSINO'].transform([instituicao])[0]
                
                # Criar array de features na ordem correta (11 features, sem ING)
                features = np.array([[ida, ieg, iaa, ips, ipv, idade, ano_ingresso, mat, por, genero_enc, instituicao_enc]])
                
                # Normalizar
                features_scaled = scaler.transform(features)
                
                # Predição com probabilidade
                probabilidade = modelo.predict_proba(features_scaled)[0]
                prob_risco = probabilidade[1]
                
                # Classificar nível de risco
                nivel, emoji, css_class = classificar_nivel_risco(prob_risco)
                
                st.markdown("---")
                st.subheader("📊 Resultado da Predição")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    descricoes = {
                        'Sem Risco': 'O aluno apresenta indicadores adequados para sua fase escolar. Manter acompanhamento regular.',
                        'Atenção': 'O aluno apresenta alguns sinais que merecem atenção. Recomenda-se monitoramento preventivo.',
                        'Risco Moderado': 'O aluno apresenta indicadores que sugerem risco moderado de defasagem. Intervenção pedagógica recomendada.',
                        'Risco Alto': 'O aluno apresenta indicadores críticos de risco de defasagem. Intervenção urgente necessária.'
                    }
                    
                    st.markdown(f"""
                    <div class="{css_class}">
                        <h2>{emoji} {nivel.upper()}</h2>
                        <p>{descricoes[nivel]}</p>
                        <p style="font-size: 24px; font-weight: bold; margin-top: 10px;">Probabilidade de Risco: {prob_risco*100:.1f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    # Gauge com 4 níveis
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=prob_risco * 100,
                        number={'suffix': '%', 'font': {'size': 40}},
                        title={'text': "Probabilidade de Risco", 'font': {'size': 18}},
                        gauge={
                            'axis': {'range': [0, 100], 'tickwidth': 1},
                            'bar': {'color': "darkgray", 'thickness': 0.2},
                            'bgcolor': "white",
                            'borderwidth': 2,
                            'bordercolor': "gray",
                            'steps': [
                                {'range': [0, 30], 'color': "#22C55E"},
                                {'range': [30, 60], 'color': "#FBBF24"},
                                {'range': [60, 85], 'color': "#F97316"},
                                {'range': [85, 100], 'color': "#EF4444"}
                            ],
                            'threshold': {
                                'line': {'color': "black", 'width': 4},
                                'thickness': 0.8,
                                'value': prob_risco * 100
                            }
                        }
                    ))
                    fig.update_layout(
                        height=350,
                        margin=dict(l=20, r=20, t=50, b=20),
                        paper_bgcolor='rgba(0,0,0,0)',
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                # Feature Importance
                st.subheader("📈 Fatores que Influenciaram a Predição")
                
                feature_importance = modelo_info.get('feature_importance', {})
                if feature_importance:
                    # Nomes legíveis
                    nomes = {
                        'IDA': 'Desempenho Acadêmico (IDA)',
                        'IEG': 'Engajamento (IEG)',
                        'IAA': 'Autoavaliação (IAA)',
                        'IPS': 'Psicossocial (IPS)',
                        'IPV': 'Ponto de Virada (IPV)',
                        'IDADE': 'Idade',
                        'ANO INGRESSO': 'Ano de Ingresso',
                        'MAT': 'Nota Matemática',
                        'POR': 'Nota Português',
                        'GÊNERO_ENC': 'Gênero',
                        'INSTITUIÇÃO DE ENSINO_ENC': 'Instituição de Ensino',
                    }
                    
                    df_imp = pd.DataFrame({
                        'Feature': [nomes.get(k, k) for k in feature_importance.keys()],
                        'Importância': [v * 100 for v in feature_importance.values()]
                    }).sort_values('Importância', ascending=True)
                    
                    fig = px.bar(df_imp, x='Importância', y='Feature', orientation='h',
                                color='Importância', color_continuous_scale='Blues',
                                labels={'Importância': 'Importância (%)'})
                    fig.update_layout(showlegend=False, height=400)
                    st.plotly_chart(fig, use_container_width=True)
                
                # Recomendações por nível
                st.subheader("💡 Recomendações")
                if nivel == 'Risco Alto':
                    st.error("""
                    **Ações Urgentes:**
                    - 🚨 Intervenção pedagógica imediata
                    - 👥 Avaliação psicossocial completa
                    - 📊 Monitoramento semanal dos indicadores
                    - 🎯 Plano de recuperação personalizado
                    - 👨‍👩‍👧 Contato com a família
                    """)
                elif nivel == 'Risco Moderado':
                    st.warning("""
                    **Ações Recomendadas:**
                    - 📚 Acompanhamento pedagógico individualizado
                    - 👥 Avaliação psicossocial
                    - 📊 Monitoramento quinzenal dos indicadores
                    - 🎯 Plano de intervenção personalizado
                    """)
                elif nivel == 'Atenção':
                    st.info("""
                    **Ações Preventivas:**
                    - 📈 Monitoramento mensal dos indicadores
                    - 🎯 Estabelecer metas de desenvolvimento
                    - 📚 Reforço em áreas com menor desempenho
                    """)
                else:
                    st.success("""
                    **Manutenção:**
                    - ✅ Manter acompanhamento regular
                    - 📈 Continuar estimulando o engajamento
                    - 🎯 Estabelecer metas de evolução
                    """)
                    
            except Exception as e:
                st.error(f"Erro na predição: {e}")
                st.info("Verifique se os valores de Gênero e Instituição são compatíveis com os dados de treino.")
    else:
        st.warning("⚠️ Modelo não carregado. Execute o notebook de treinamento primeiro.")
        st.info("""
        Para usar a predição de risco:
        1. Execute o notebook `03_Modelo_Preditivo.ipynb` no Google Colab
        2. Os arquivos do modelo serão salvos automaticamente
        3. Recarregue esta página
        """)

# ==================== PÁGINA: SOBRE O PROJETO ====================
elif pagina == "📋 Sobre o Projeto":
    st.markdown('<p class="main-header">📋 Sobre o Projeto</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎯 Objetivo
    
    Este projeto foi desenvolvido para o **Datathon FIAP** em parceria com a **Passos Mágicos**, 
    com o objetivo de analisar indicadores educacionais e criar um modelo preditivo para 
    identificar alunos em risco de defasagem escolar.
    
    ## 📊 Indicadores Analisados
    
    | Indicador | Descrição |
    |-----------|-----------|
    | **IDA** | Índice de Desempenho Acadêmico |
    | **IEG** | Índice de Engajamento |
    | **IAA** | Índice de Autoavaliação |
    | **IPS** | Índice Psicossocial |
    | **IPV** | Índice de Ponto de Virada |
    | **IPP** | Índice Psicopedagógico |
    | **IAN** | Índice de Adequação de Nível |
    | **INDE** | Índice de Desenvolvimento Educacional |
    
    ## 🤖 Modelo de Machine Learning
    
    Foram testados **4 algoritmos** de Machine Learning:
    - Logistic Regression
    - SVM (RBF)
    - Random Forest
    - **Gradient Boosting** ← Selecionado
    
    ### Resultados do Modelo Final (Gradient Boosting)
    
    | Métrica | Teste (80/20) | CV (Stratified 5-fold) |
    |---------|---------------|------------------------|
    | Acurácia | 78.7% | 78.5% (+/- 1.1%) |
    | AUC-ROC | 86.2% | 85.1% (+/- 1.9%) |
    | F1-Score | 82.7% | 82.5% (+/- 0.9%) |
    
    ### Níveis de Risco
    
    | Probabilidade | Nível | % Real com Risco |
    |---------------|-------|------------------|
    | < 30% | Sem Risco | 10.0% |
    | 30% - 60% | Atenção | 44.6% |
    | 60% - 85% | Risco Moderado | 74.8% |
    | > 85% | Risco Alto | 90.5% |
    
    ### Decisões Técnicas
    
    - **Remoção do Inglês (ING):** Apenas 33% de preenchimento em 2022, ausente nos demais anos.
      Mantê-lo reduziria o dataset de 2.467 para ~660 registros.
    - **Split estratificado por ano:** Garante representatividade temporal nos conjuntos de treino/teste.
    - **Stratified K-Fold:** Validação robusta com variação de apenas 1.1% entre folds.
    
    ## 👨‍💻 Autor
    
    **Leandro Leme Crespo**
    
    ## 🔗 Links
    
    - [GitHub do Projeto](https://github.com/LeandroCrespo/datathon-passos-magicos)
    - [Passos Mágicos](https://www.passosmagicos.org.br/)
    - [FIAP](https://www.fiap.com.br/)
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido para o Datathon FIAP 2025")
st.sidebar.markdown("© Leandro Leme Crespo")
