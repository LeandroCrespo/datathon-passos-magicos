# Roteiro do Vídeo - Datathon Passos Mágicos
## Duração: 5 minutos

---

## SLIDE 1: CAPA (0:00 - 0:10) ⏱️ 10 segundos

**FALA:**
> "Olá! Somos a equipe [NOME DA EQUIPE] e vamos apresentar nossa análise do Datathon Passos Mágicos."

---

## SLIDE 2: O DESAFIO (0:10 - 0:30) ⏱️ 20 segundos

**FALA:**
> "A Passos Mágicos é uma ONG que transforma a vida de crianças e jovens de Embu-Guaçu através da educação. Nosso desafio foi analisar os dados educacionais de mais de 3 mil alunos para identificar padrões de risco de defasagem escolar e criar um modelo preditivo que ajude a ONG a intervir preventivamente."

---

## SLIDE 3: OS DADOS (0:30 - 0:55) ⏱️ 25 segundos

**FALA:**
> "Trabalhamos com dados de 2022 a 2024, totalizando 3.030 registros de alunos. Analisamos 7 indicadores principais: IDA para desempenho acadêmico, IEG para engajamento, IAA para autoavaliação, IPS para aspectos psicossociais, IPP para psicopedagógicos, IPV para ponto de virada, e IAN para adequação de nível. Também incluímos dados contextuais como idade, notas por matéria e instituição de ensino."

---

## SLIDE 4: DESCOBERTAS - PERGUNTAS 1 a 4 (0:55 - 1:35) ⏱️ 40 segundos

**FALA:**
> "Nossas principais descobertas:
> 
> Primeiro, sobre a defasagem: 55,7% dos alunos apresentam risco, mas a boa notícia é que esse número está caindo - de 70% em 2022 para 46% em 2024.
> 
> Segundo, o desempenho acadêmico medido pelo IDA está melhorando ao longo dos anos.
> 
> Terceiro, encontramos uma correlação forte de 0,54 entre engajamento e desempenho - alunos mais engajados têm melhor desempenho.
> 
> Quarto, a autoavaliação dos alunos tem correlação fraca com o desempenho real, sugerindo que os alunos nem sempre percebem suas dificuldades."

---

## SLIDE 5: DESCOBERTAS - PERGUNTAS 5 a 8 (1:35 - 2:15) ⏱️ 40 segundos

**FALA:**
> "Continuando as descobertas:
> 
> Os aspectos psicossociais têm correlação fraca com desempenho, indicando que fatores emocionais precisam de análise mais profunda.
> 
> As avaliações psicopedagógicas confirmam a defasagem identificada pelo IAN, com correlação positiva de 0,18.
> 
> O engajamento é o fator que mais influencia o ponto de virada, com correlação de 0,56.
> 
> E sobre o INDE, confirmamos que IDA, IEG e IPV representam 60% do peso no índice de desenvolvimento educacional."

---

## SLIDE 6: MODELO PREDITIVO (2:15 - 3:00) ⏱️ 45 segundos

**FALA:**
> "Para a pergunta 9, construímos um modelo de Machine Learning para prever risco de defasagem.
> 
> Testamos 10 algoritmos diferentes: Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Gradient Boosting, XGBoost, AdaBoost, MLP e Ensemble.
> 
> O melhor resultado foi o SVM - Support Vector Machine - com 84,3% de acurácia e 89,3% de AUC-ROC.
> 
> O modelo classifica os alunos em duas categorias: Sem Risco, quando a defasagem é zero ou positiva, e Com Risco, quando a defasagem é negativa."

---

## SLIDE 7: FEATURES E INSIGHTS (3:00 - 3:40) ⏱️ 40 segundos

**FALA:**
> "Analisando a importância das features, descobrimos que a idade é o fator mais determinante, representando 38% da importância do modelo. Isso faz sentido porque alunos mais velhos tiveram mais tempo para acumular defasagem.
> 
> Em seguida vêm o engajamento IEG com 9,6%, o ponto de virada IPV com 8,2%, e o desempenho acadêmico IDA com 6,7%.
> 
> Um insight importante: alunos mais velhos com desempenho médio são o grupo de maior risco - 90% dos alunos acima de 17 anos com desempenho médio estão em defasagem."

---

## SLIDE 8: SOLUÇÃO STREAMLIT (3:40 - 4:10) ⏱️ 30 segundos

**FALA:**
> "Desenvolvemos uma aplicação web em Streamlit que permite à equipe da Passos Mágicos:
> 
> Visualizar dashboards com métricas gerais e evolução dos indicadores.
> 
> Fazer análise exploratória dos dados com correlações e distribuições.
> 
> E o mais importante: usar o modelo preditivo para avaliar o risco de qualquer aluno, inserindo seus indicadores e recebendo a probabilidade de defasagem em tempo real."

---

## SLIDE 9: RECOMENDAÇÕES (4:10 - 4:40) ⏱️ 30 segundos

**FALA:**
> "Nossas recomendações para a Passos Mágicos:
> 
> Primeiro, priorizar intervenções em alunos mais velhos com desempenho médio - esse é o grupo de maior risco.
> 
> Segundo, investir em programas de engajamento, já que o IEG tem forte correlação com o ponto de virada.
> 
> Terceiro, implementar avaliações de autoavaliação mais frequentes para ajudar os alunos a perceberem suas dificuldades.
> 
> E quarto, usar o modelo preditivo como ferramenta de triagem para identificar alunos em risco antes que a defasagem se consolide."

---

## SLIDE 10: CONCLUSÃO (4:40 - 5:00) ⏱️ 20 segundos

**FALA:**
> "Concluindo, nossa análise mostrou que é possível prever o risco de defasagem com 84% de acurácia usando dados já coletados pela ONG. A chave está na intervenção precoce - quanto antes identificarmos os alunos em risco, maior a chance de transformar suas trajetórias.
> 
> Obrigado pela atenção! Estamos à disposição para perguntas."

---

## DICAS PARA GRAVAÇÃO:

1. **Pratique o roteiro** várias vezes antes de gravar
2. **Mantenha um ritmo constante** - nem muito rápido nem muito lento
3. **Use os tempos como guia** - ajuste conforme necessário
4. **Destaque os números importantes** com ênfase na voz
5. **Grave em ambiente silencioso** com boa iluminação
6. **Mostre a tela da apresentação** enquanto fala

---

## TEMPO TOTAL: 5 minutos
