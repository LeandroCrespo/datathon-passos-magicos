# Roteiro Otimizado para Vídeo de 5 Minutos (10 Slides)

**Objetivo:** Apresentação direta e focada nos resultados, sem introdução institucional longa.

---

### Estrutura e Tempos

| Slide # | Título | Tempo | Pontos Chave |
|:---:|---|:---:|---|
| 1 | Capa | 15s | Título e contexto do projeto. |
| 2 | O Desafio | 30s | Objetivo: prever risco de defasagem precocemente. |
| 3 | Os Dados | 30s | Dataset PEDE 2022-2024 (3 anos, +3000 registros). |
| 4 | Descobertas | 45s | Aumento de alunos na fase correta, Engajamento e Ponto de Virada. |
| 5 | Modelo | 45s | Random Forest com SMOTE, Recall 60%, AUC-ROC 82.5%. |
| 6 | Features | 45s | IAN (25%) e Média (13%) como principais preditores. |
| 7 | Streamlit | 30s | Ferramenta para uso da equipe pedagógica. |
| 8 | Recomendações | 30s | Ações para alunos (suporte) e ONG (engajamento). |
| 9 | Conclusão | 15s | Resumo do valor entregue. |
| 10 | Obrigado | 15s | Encerramento. |
| **Total** | | **~300s (5 min)** | |

---

### Script Detalhado

**(Slide 1: Capa - 15s)**
> "Olá. Sou Leandro Leme Crespo e apresento agora o projeto de Data Analytics desenvolvido para o Datathon FIAP, em parceria com a Associação Passos Mágicos. Nosso foco foi criar um modelo preditivo para identificar o risco de defasagem escolar."

**(Slide 2: O Desafio - 30s)**
> "O grande desafio que enfrentamos foi: como usar os dados para agir antes que o aluno reprove ou evada? Nosso objetivo foi claro: analisar o histórico educacional e construir uma ferramenta capaz de alertar a equipe pedagógica sobre alunos em risco, permitindo intervenções preventivas."

**(Slide 3: Os Dados - 30s)**
> "Trabalhamos com a Pesquisa de Desenvolvimento Educacional (PEDE) de 2022, 2023 e 2024. Analisamos mais de 3.000 registros de alunos, cruzando indicadores acadêmicos como IDA, psicossociais como IPS, e de engajamento como IEG, para entender a trajetória de desenvolvimento."

**(Slide 4: Principais Descobertas - 45s)**
> "Nossa análise exploratória trouxe insights importantes. Primeiro, houve um aumento significativo de alunos na fase correta: de 29% em 2022 para 42% em 2024. Isso mostra que as ações da ONG estão ajudando os alunos a se alinharem com a fase ideal para sua idade. Segundo, descobrimos que o Engajamento é o motor do desenvolvimento. E terceiro, o Ponto de Virada se mostrou um marcador crucial de recuperação."

**(Slide 5: Modelo Preditivo - 45s)**
> "Desenvolvemos um modelo de Machine Learning usando Random Forest com técnica de balanceamento SMOTE. O modelo alcançou 60% de Recall, ou seja, consegue identificar 6 em cada 10 alunos que realmente estão em risco. O AUC-ROC de 82,5% indica boa capacidade de discriminação. Priorizamos o Recall porque, neste contexto, é mais importante identificar o máximo de alunos em risco possível."

**(Slide 6: Features Mais Importantes - 45s)**
> "Mas o que define esse risco? O modelo nos mostrou que a Adequação ao Nível, o IAN, é responsável por 25% da decisão, seguida pela Média Geral com 13% e pelo Ponto de Virada com 11%. Isso confirma que a defasagem idade-série é o sinal de alerta mais forte, mas que o comportamento e a virada de chave também são fundamentais."

**(Slide 7: Aplicação Streamlit - 30s)**
> "Para colocar essa inteligência na mão da equipe, criamos uma aplicação interativa. Nela, é possível visualizar a evolução da ONG e, principalmente, fazer a predição de risco para novos alunos em tempo real, democratizando o acesso à ciência de dados."

**(Slide 8: Recomendações - 30s)**
> "Com base nisso, recomendamos: para os alunos em risco, foco total em suporte psicossocial e acompanhamento intensivo. Para a organização, sugerimos usar o modelo como triagem na entrada e investir em programas que aumentem o engajamento, pois é ele que transforma o desempenho."

**(Slide 9: Conclusão - 15s)**
> "Entregamos, portanto, um diagnóstico completo, um modelo preditivo funcional e uma ferramenta prática. É o uso de dados gerando impacto real na ponta."

**(Slide 10: Obrigado - 15s)**
> "Agradeço a atenção de todos. O código completo está disponível no GitHub e a aplicação Streamlit está publicada para uso. Muito obrigado!"
