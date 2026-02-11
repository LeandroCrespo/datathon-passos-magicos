# 🎓 Datathon FIAP - Passos Mágicos

## Análise de Dados e Modelo Preditivo de Risco de Defasagem

Este projeto foi desenvolvido como parte do **Datathon da Pós-Tech em Data Analytics da FIAP**, em parceria com a **Associação Passos Mágicos**.

---

## 🚀 Aplicação Streamlit

**Acesse a aplicação online:** [https://datathon-passos-magicos.streamlit.app](https://datathon-passos-magicos.streamlit.app)

A aplicação permite:
- 📊 Visualizar dashboards interativos dos dados
- 🔮 Prever o risco de defasagem de alunos individuais com 4 níveis de risco
- 📋 Receber recomendações de intervenção pedagógica

---

## Sobre a Passos Mágicos

A Associação Passos Mágicos atua há mais de 30 anos em Embu-Guaçu, transformando a vida de crianças e jovens de baixa renda através da educação de qualidade, apoio psicológico e ampliação da visão de mundo.

🔗 [Site oficial](https://passosmagicos.org.br/)

---

## Objetivo do Projeto

Utilizar técnicas de análise de dados e machine learning para:

1. **Analisar** os dados da Pesquisa de Desenvolvimento Educacional (PEDE) de 2022 a 2024
2. **Responder** às 11 perguntas de negócio do Datathon
3. **Prever** o risco de defasagem escolar de forma precoce
4. **Disponibilizar** uma ferramenta interativa para apoio à decisão pedagógica

---

## Estrutura do Repositório

```
datathon-passos-magicos/
├── data/
│   └── BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx   # Dataset PEDE 2022-2024
├── notebooks/
│   ├── 01_EDA_Analise_Exploratoria.ipynb        # Análise Exploratória dos Dados
│   ├── 02_Perguntas_Negocio.ipynb               # Respostas às 11 perguntas
│   └── 03_Modelo_Preditivo.ipynb                # Modelo de ML (Gradient Boosting)
├── streamlit/
│   ├── app.py                                    # Dashboard interativo
│   ├── requirements.txt                          # Dependências do Streamlit
│   ├── logo_passos_magicos.png                   # Logo da ONG
│   ├── modelo_risco_defasagem.pkl                # Modelo treinado
│   ├── scaler.pkl                                # Scaler para normalização
│   ├── label_encoders.pkl                        # Encoders categóricos
│   ├── modelo_info.pkl                           # Metadados do modelo
│   └── features.txt                              # Lista de features
├── instrucoes_deploy_streamlit.md                # Instruções de deploy
└── README.md                                     # Este arquivo
```

---

## Principais Resultados

### Modelo Preditivo: Gradient Boosting Classifier

Foram testados 4 algoritmos (Logistic Regression, SVM, Random Forest, Gradient Boosting). O **Gradient Boosting** foi selecionado por apresentar o melhor desempenho no dataset completo de **2.467 registros**.

| Métrica | Teste (80/20) | CV (Stratified 5-Fold) |
|---------|---------------|------------------------|
| **Acurácia** | 78.7% | 78.5% (± 1.1%) |
| **AUC-ROC** | 86.2% | 85.1% (± 1.9%) |
| **F1-Score** | 82.7% | 82.5% (± 0.9%) |

### Decisões Técnicas

- **11 features:** IDA, IEG, IAA, IPS, IPV, Idade, Ano Ingresso, Matemática, Português, Gênero, Instituição
- **Remoção do Inglês (ING):** Apenas 33% de preenchimento em 2022, ausente nos demais anos. Mantê-lo reduziria o dataset de 2.467 para ~660 registros.
- **Split estratificado por ano:** Garante representatividade temporal nos conjuntos de treino/teste.
- **Stratified K-Fold:** Validação cruzada robusta com variação de apenas 1.1% entre folds.

### 4 Níveis de Risco

O modelo gera uma probabilidade que é convertida em 4 níveis:

| Probabilidade | Nível | % Real com Risco | Ação Sugerida |
|---------------|-------|------------------|---------------|
| < 30% | ✅ Sem Risco | 10.0% | Acompanhamento normal |
| 30% - 60% | ⚡ Atenção | 44.6% | Monitoramento preventivo |
| 60% - 85% | ⚠️ Risco Moderado | 74.8% | Intervenção pedagógica |
| > 85% | 🚨 Risco Alto | 90.5% | Intervenção urgente |

### Features Mais Importantes

1. Idade — 28.6%
2. IPV (Ponto de Virada) — 10.5%
3. IEG (Engajamento) — 8.4%
4. IPS (Psicossocial) — 7.0%
5. Ano de Ingresso — 6.8%

---

## Perguntas de Negócio

Os notebooks respondem às 11 perguntas do Datathon:

| # | Pergunta | Insight Principal |
|---|---------|-------------------|
| 1 | Perfil de defasagem (IAN) | Defasagem média melhorou de -0.94 para -0.41 |
| 2 | Desempenho Acadêmico (IDA) | IDA estável (~6.5), sem correlação forte com defasagem |
| 3 | Engajamento (IEG) | Forte correlação com INDE (r=0.78) |
| 4 | Autoavaliação (IAA) | Parcialmente coerente com indicadores objetivos |
| 5 | Psicossocial (IPS) | Relação fraca com defasagem |
| 6 | Psicopedagógico (IPP) | Confirma tendências dos demais indicadores |
| 7 | Ponto de Virada (IPV) | IEG e IDA são os melhores preditores |
| 8 | Combinações (IDA+IEG+IPS+IPP) | Juntos explicam 82.3% do INDE; IDA é o mais importante |
| 9 | Modelo Preditivo | Gradient Boosting com 78.7% de acurácia |
| 10 | Efetividade | Defasagem média melhorou ao longo dos anos |
| 11 | Insights Criativos | Evasão Quartzo (60%), Matemática gargalo, retenção crescente |

---

## Como Executar

### Notebooks (Google Colab — Recomendado)

Clique nos links abaixo para abrir diretamente no Colab:

- [01_EDA_Analise_Exploratoria.ipynb](https://colab.research.google.com/github/LeandroCrespo/datathon-passos-magicos/blob/main/notebooks/01_EDA_Analise_Exploratoria.ipynb)
- [02_Perguntas_Negocio.ipynb](https://colab.research.google.com/github/LeandroCrespo/datathon-passos-magicos/blob/main/notebooks/02_Perguntas_Negocio.ipynb)
- [03_Modelo_Preditivo.ipynb](https://colab.research.google.com/github/LeandroCrespo/datathon-passos-magicos/blob/main/notebooks/03_Modelo_Preditivo.ipynb)

### Streamlit (Local)

```bash
cd streamlit
pip install -r requirements.txt
streamlit run app.py
```

### Streamlit (Deploy)

Consulte o arquivo `instrucoes_deploy_streamlit.md` para deploy no Streamlit Cloud.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Pandas, NumPy** — Manipulação de dados
- **Matplotlib, Seaborn, Plotly** — Visualizações
- **Scikit-learn** — Machine Learning
- **Streamlit** — Aplicação web interativa

---

## Autor

**Leandro Leme Crespo**

Projeto desenvolvido para o Datathon FIAP 2025 — Pós-Tech Data Analytics

---

## Agradecimentos

- **Associação Passos Mágicos** — Pela parceria e dados
- **FIAP** — Pela oportunidade de aprendizado
- **Professores e Mentores** — Pelo suporte técnico
