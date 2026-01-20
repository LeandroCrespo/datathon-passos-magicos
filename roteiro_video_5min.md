# Roteiro Otimizado para Vídeo de 5 Minutos (10 Slides)

**Objetivo:** Apresentação direta e focada nos resultados do modelo de 3 classes de risco.

---

### Estrutura e Tempos

| Slide # | Título | Tempo | Pontos Chave |
|:---:|---|:---:|---|
| 1 | Capa | 15s | Título e contexto do projeto. |
| 2 | O Desafio | 30s | Objetivo: prever risco de defasagem precocemente. |
| 3 | Os Dados | 30s | Dataset PEDE 2024 (860 alunos, 6 indicadores). |
| 4 | Descobertas | 45s | 70% em defasagem, padrões identificados. |
| 5 | Modelo | 45s | Random Forest 3 classes, Acurácia 75.6%, Recall 82%. |
| 6 | Features | 45s | INDE como principal preditor (34.7%). |
| 7 | Streamlit | 30s | Ferramenta para uso da equipe pedagógica. |
| 8 | Recomendações | 30s | Ações para alunos em cada nível de risco. |
| 9 | Conclusão | 15s | Resumo do valor entregue. |
| 10 | Obrigado | 15s | Encerramento. |
| **Total** | | **~300s (5 min)** | |

---

### Script Detalhado

**(Slide 1: Capa - 15s)**
> "Olá. Sou Leandro Leme Crespo e apresento agora o projeto de Data Analytics desenvolvido para o Datathon FIAP, em parceria com a Associação Passos Mágicos. Nosso foco foi criar um modelo preditivo para identificar o risco de defasagem educacional."

**(Slide 2: O Desafio - 30s)**
> "O grande desafio que enfrentamos foi: como usar os dados para agir antes que o aluno fique defasado? Nosso objetivo foi claro: analisar os indicadores educacionais e construir uma ferramenta capaz de alertar a equipe pedagógica sobre alunos em risco, permitindo intervenções preventivas."

**(Slide 3: Os Dados - 30s)**
> "Trabalhamos com os dados do PEDE 2024, contendo informações de 860 alunos. Analisamos 6 indicadores: IDA - Desempenho Acadêmico, IEG - Engajamento, IAA - Autoavaliação, IPS - Psicossocial, IPV - Ponto de Virada, e o INDE - índice geral de desenvolvimento."

**(Slide 4: Principais Descobertas - 45s)**
> "Nossa análise revelou dados importantes: 70% dos alunos estão em algum nível de defasagem. Apenas 30% estão sem risco - em fase adequada. 67% têm risco moderado - atrasados 1 a 2 fases. E 3% têm risco severo - atrasados 3 ou mais fases. Identificamos que alunos em risco apresentam indicadores consistentemente mais baixos em todas as dimensões."

**(Slide 5: Modelo Preditivo - 45s)**
> "Desenvolvemos um modelo Random Forest com 3 classes de risco, seguindo a metodologia oficial da Passos Mágicos. O modelo alcançou 75,6% de acurácia geral e 82% de recall para identificar alunos em risco moderado. Importante destacar: não usamos o IAN como feature, pois ele é derivado da defasagem. Usamos apenas os indicadores de desempenho para identificar padrões."

**(Slide 6: Features Mais Importantes - 45s)**
> "O modelo nos mostrou que o INDE é o indicador mais importante, responsável por 35% da decisão. Em seguida vem o IPV - Ponto de Virada com 16%, o IDA - Desempenho Acadêmico com 15%, IAA - Autoavaliação com 13%, IEG - Engajamento com 12%, e IPS - Psicossocial com 10%. Essa combinação permite identificar padrões de risco antes que a defasagem aconteça."

**(Slide 7: Aplicação Streamlit - 30s)**
> "Para colocar essa inteligência na mão da equipe, criamos uma aplicação interativa no Streamlit. Nela, é possível visualizar o dashboard com a evolução dos indicadores e, principalmente, fazer a predição de risco inserindo os indicadores de um aluno e recebendo a classificação: Sem Risco, Risco Moderado ou Risco Severo."

**(Slide 8: Recomendações - 30s)**
> "Com base nos padrões identificados, recomendamos: para alunos em risco severo, acompanhamento individualizado imediato. Para risco moderado, monitoramento mensal dos indicadores. E para todos, foco especial no INDE e IPV, que são os principais preditores de defasagem."

**(Slide 9: Conclusão - 15s)**
> "Entregamos uma análise completa dos dados, um modelo preditivo com 3 classes de risco e 75,6% de acurácia, e uma ferramenta prática no Streamlit. O grande valor é permitir intervenção preventiva: identificar alunos em risco antes que a defasagem aconteça."

**(Slide 10: Obrigado - 15s)**
> "Agradeço a atenção de todos. O código completo está disponível no GitHub e a aplicação Streamlit está publicada no Community Cloud. Muito obrigado!"

---

### Notas Técnicas

#### Métricas do Modelo
- **Acurácia:** 75.58%
- **Recall Sem Risco:** 69%
- **Recall Risco Moderado:** 82%
- **Recall Risco Severo:** 17% (poucos exemplos)

#### Feature Importance
1. INDE: 34.7%
2. IPV: 16.1%
3. IDA: 15.2%
4. IAA: 12.7%
5. IEG: 11.7%
6. IPS: 9.6%

#### Classificação de Risco (Metodologia Passos Mágicos)
- **Sem Risco:** D ≥ 0 (em fase ou adiantado)
- **Risco Moderado:** 0 > D ≥ -2 (1-2 fases atrasado)
- **Risco Severo:** D < -2 (3+ fases atrasado)

#### Links
- GitHub: https://github.com/LeandroCrespo/datathon-passos-magicos
- Streamlit: [URL do deploy no Community Cloud]
