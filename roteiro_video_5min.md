# Roteiro Otimizado para Vídeo de 5 Minutos (10 Slides)

**Objetivo:** Apresentação direta e focada nos resultados, sem introdução institucional longa.

---

### Estrutura e Tempos

| Slide # | Título | Tempo | Pontos Chave |
|:---:|---|:---:|---|
| 1 | Capa | 15s | Título e contexto do projeto. |
| 2 | O Desafio | 30s | Objetivo: prever risco de defasagem precocemente. |
| 3 | Os Dados | 30s | Dataset PEDE 2022-2024 (3 anos, +1000 alunos). |
| 4 | Descobertas | 45s | Queda na defasagem, Engajamento e Ponto de Virada. |
| 5 | Modelo | 45s | Random Forest, Recall 87% (segurança na detecção). |
| 6 | Features | 45s | IAN (34%) e Média (16%) como principais preditores. |
| 7 | Streamlit | 30s | Ferramenta para uso da equipe pedagógica. |
| 8 | Recomendações | 30s | Ações para alunos (suporte) e ONG (engajamento). |
| 9 | Conclusão | 15s | Resumo do valor entregue. |
| 10 | Obrigado | 15s | Encerramento. |
| **Total** | | **~300s (5 min)** | |

---

### Script Detalhado

**(Slide 1: Capa - 15s)**
> "Olá. Apresento agora o projeto de Data Analytics desenvolvido para o Datathon FIAP, em parceria com a Associação Passos Mágicos. Nosso foco foi criar um modelo preditivo para identificar o risco de defasagem escolar."

**(Slide 2: O Desafio - 30s)**
> "O grande desafio que enfrentamos foi: como usar os dados para agir antes que o aluno reprove ou evada? Nosso objetivo foi claro: analisar o histórico educacional e construir uma ferramenta capaz de alertar a equipe pedagógica sobre alunos em risco, permitindo intervenções preventivas."

**(Slide 3: Os Dados - 30s)**
> "Trabalhamos com a Pesquisa de Desenvolvimento Educacional (PEDE) de 2022, 2023 e 2024. Analisamos mais de 3.000 registros de alunos, cruzando indicadores acadêmicos (como IDA), psicossociais (IPS) e de engajamento (IEG) para entender a trajetória de desenvolvimento."

**(Slide 4: Principais Descobertas - 45s)**
> "Nossa análise exploratória trouxe ótimas notícias e insights. Primeiro, houve uma redução de 17% na defasagem média dos alunos ao longo dos três anos. Segundo, descobrimos que o Engajamento (IEG) é o motor do desenvolvimento, sendo o indicador que mais puxa a nota global para cima. E o Ponto de Virada (IPV) se mostrou um marcador crucial de recuperação."

**(Slide 5: Modelo Preditivo - 45s)**
> "Desenvolvemos um modelo de Machine Learning usando Random Forest. O resultado mais importante aqui é o Recall de 87%. Isso significa que, de cada 100 alunos que realmente estão em risco, nosso modelo consegue identificar 87. Priorizamos a segurança para não deixar nenhum aluno para trás."

**(Slide 6: Features Mais Importantes - 45s)**
> "Mas o que define esse risco? O modelo nos mostrou que a Adequação ao Nível (IAN) é responsável por 34% da decisão, seguida pela Média Geral e pelo Ponto de Virada. Isso confirma que a defasagem idade-série é o sinal de alerta mais forte, mas que o comportamento e a virada de chave também são fundamentais."

**(Slide 7: Aplicação Streamlit - 30s)**
> "Para colocar essa inteligência na mão da equipe, criamos uma aplicação interativa. Nela, é possível visualizar a evolução da ONG e, principalmente, fazer a predição de risco para novos alunos em tempo real, democratizando o acesso à ciência de dados."

**(Slide 8: Recomendações - 30s)**
> "Com base nisso, recomendamos: para os alunos em risco, foco total em suporte psicossocial e acompanhamento intensivo. Para a organização, sugerimos usar o modelo como triagem na entrada e investir pesado em programas que aumentem o engajamento, pois é ele que transforma o desempenho."

**(Slide 9: Conclusão - 15s)**
> "Entregamos, portanto, um diagnóstico completo, um modelo de alta precisão e uma ferramenta prática. É o uso de dados gerando impacto real na ponta."

**(Slide 10: Obrigado - 15s)**
> "Agradecemos à Passos Mágicos e à FIAP pela oportunidade. O código e a documentação completa estão disponíveis no nosso GitHub. Muito obrigado!"
