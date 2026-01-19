# Datathon FIAP - Passos Mágicos

## Análise de Dados e Modelo Preditivo de Risco de Defasagem

Este projeto foi desenvolvido como parte do Datathon da Pós-Tech em Data Analytics da FIAP, em parceria com a **Associação Passos Mágicos**.

---

## Sobre a Passos Mágicos

A Associação Passos Mágicos atua há mais de 30 anos em Embu-Guaçu, transformando a vida de crianças e jovens de baixa renda através da educação de qualidade, apoio psicológico e ampliação da visão de mundo.

🔗 [Site oficial](https://passosmagicos.org.br/)

---

## Objetivo do Projeto

Utilizar técnicas de análise de dados e machine learning para:

1. **Analisar** os dados da Pesquisa de Desenvolvimento Educacional (PEDE) de 2022 a 2024
2. **Identificar** fatores que influenciam o desenvolvimento dos alunos
3. **Prever** o risco de defasagem escolar de forma precoce
4. **Disponibilizar** uma ferramenta interativa para apoio à decisão pedagógica

---

## Estrutura do Repositório

```
datathon-passos-magicos/
├── notebooks/
│   ├── 01_EDA_Analise_Exploratoria.ipynb   # Análise exploratória dos dados
│   ├── 02_Perguntas_Negocio.ipynb          # Respostas às 11 perguntas de negócio
│   └── 03_Modelo_Preditivo.ipynb           # Modelo de risco de defasagem
├── streamlit/
│   ├── app.py                              # Aplicação Streamlit
│   ├── requirements.txt                    # Dependências
│   ├── modelo_risco_defasagem.pkl          # Modelo treinado
│   ├── scaler.pkl                          # Normalizador
│   └── ...
├── images/                                 # Visualizações geradas
├── roteiro_video.md                        # Roteiro para apresentação em vídeo
└── instrucoes_deploy_streamlit.md          # Guia de deploy
```

---

## Principais Resultados

### Análise Exploratória
- **Redução de 17%** na defasagem média entre 2022 e 2024
- **Engajamento (IEG)** é o indicador mais correlacionado com o sucesso global
- **Ponto de Virada (IPV)** é um fator crucial de recuperação

### Modelo Preditivo
| Métrica | Valor |
|---------|-------|
| **Recall** | 87.06% |
| **AUC-ROC** | 83.25% |
| **F1-Score** | 50.34% |

### Features Mais Importantes
1. IAN (Adequação ao Nível) - 34%
2. Média dos Indicadores - 16%
3. IPV (Ponto de Virada) - 10%

---

## Aplicação Streamlit

A aplicação permite:
- 📊 Visualizar dashboards interativos dos dados
- 🔮 Prever o risco de defasagem de alunos individuais
- 📋 Receber recomendações de intervenção pedagógica

### Deploy
Acesse: **[Link do Streamlit App]** *(a ser preenchido após deploy)*

---

## Como Executar os Notebooks

1. Abra os notebooks no [Google Colab](https://colab.research.google.com/)
2. Monte seu Google Drive quando solicitado
3. Execute as células sequencialmente

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Pandas, NumPy** - Manipulação de dados
- **Matplotlib, Seaborn, Plotly** - Visualizações
- **Scikit-learn** - Machine Learning
- **Streamlit** - Aplicação web interativa

---

## Equipe

Projeto desenvolvido para o Datathon FIAP 2025 - Pós-Tech Data Analytics

---

## Agradecimentos

- **Associação Passos Mágicos** - Pela parceria e dados
- **FIAP** - Pela oportunidade de aprendizado
- **Professores e Mentores** - Pelo suporte técnico

---

## Licença

Este projeto é de uso educacional e foi desenvolvido em parceria com a Associação Passos Mágicos.
