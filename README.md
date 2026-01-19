# Datathon FIAP - Passos Mágicos

## Análise de Dados e Modelo Preditivo de Risco de Defasagem

Este projeto foi desenvolvido como parte do Datathon da Pós-Tech em Data Analytics da FIAP, em parceria com a **Associação Passos Mágicos**.

---

## 🚀 Aplicação Streamlit

**Acesse a aplicação online:** [https://datathon-passos-magicos.streamlit.app](https://datathon-passos-magicos.streamlit.app)

A aplicação permite:
- 📊 Visualizar dashboards interativos dos dados
- 🔮 Prever o risco de defasagem de alunos individuais
- 📋 Receber recomendações de intervenção pedagógica

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
│   └── feature_names.pkl                   # Nomes das features
├── data/
│   └── BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx  # Dados PEDE 2022-2024
├── apresentacao_5min/                      # Slides da apresentação
├── roteiro_video_5min.md                   # Roteiro para apresentação em vídeo
└── instrucoes_deploy_streamlit.md          # Guia de deploy
```

---

## Principais Resultados

### Análise Exploratória
- **42% dos alunos** na fase correta em 2024 (vs 29% em 2022)
- **Engajamento (IEG)** é o indicador mais correlacionado com o sucesso global
- **Ponto de Virada (IPV)** é um fator crucial de recuperação

### Modelo Preditivo (Random Forest - 3 anos de dados)
| Métrica | Valor |
|---------|-------|
| **Recall** | 75.00% |
| **AUC-ROC** | 87.87% |
| **Acurácia** | 78.91% |

### Features Mais Importantes
1. IAN (Adequação ao Nível) - 38.0%
2. MEDIA_INDICADORES - 11.2%
3. IAA (Autoavaliação) - 10.5%
4. IEG (Engajamento) - 10.1%
5. IPS (Psicossocial) - 8.6%

---

## Como Executar os Notebooks

### Opção 1: Google Colab (Recomendado)

Clique nos links abaixo para abrir diretamente no Colab:

- [01_EDA_Analise_Exploratoria.ipynb](https://colab.research.google.com/github/LeandroCrespo/datathon-passos-magicos/blob/main/notebooks/01_EDA_Analise_Exploratoria.ipynb)
- [02_Perguntas_Negocio.ipynb](https://colab.research.google.com/github/LeandroCrespo/datathon-passos-magicos/blob/main/notebooks/02_Perguntas_Negocio.ipynb)
- [03_Modelo_Preditivo.ipynb](https://colab.research.google.com/github/LeandroCrespo/datathon-passos-magicos/blob/main/notebooks/03_Modelo_Preditivo.ipynb)

### Opção 2: Localmente

```bash
git clone https://github.com/LeandroCrespo/datathon-passos-magicos.git
cd datathon-passos-magicos
pip install -r streamlit/requirements.txt
jupyter notebook
```

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Pandas, NumPy** - Manipulação de dados
- **Matplotlib, Seaborn, Plotly** - Visualizações
- **Scikit-learn, imbalanced-learn** - Machine Learning
- **Streamlit** - Aplicação web interativa

---

## Autor

**Leandro Leme Crespo**

Projeto desenvolvido para o Datathon FIAP 2025 - Pós-Tech Data Analytics

---

## Agradecimentos

- **Associação Passos Mágicos** - Pela parceria e dados
- **FIAP** - Pela oportunidade de aprendizado
- **Professores e Mentores** - Pelo suporte técnico

---

## Licença

Este projeto é de uso educacional e foi desenvolvido em parceria com a Associação Passos Mágicos.
