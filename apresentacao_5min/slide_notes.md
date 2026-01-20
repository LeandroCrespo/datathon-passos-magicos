# 1 - Datathon FIAP - Passos Mágicos

Estamos aqui para apresentar o resultado do Datathon FIAP em parceria com a Associação Passos Mágicos. Nosso foco foi transformar dados em uma ferramenta prática para a educação. O objetivo central foi criar um Modelo Preditivo de Risco de Defasagem Escolar. Este projeto faz parte da Pós-Tech em Data Analytics da FIAP. Vamos mostrar como a análise de dados pode apoiar a Passos Mágicos a continuar transformando vidas. Agora, vamos entender o desafio que nos foi proposto.

# 2 - O Desafio

O desafio principal era identificar alunos em risco de defasagem de forma precoce. Precisamos agir antes que o problema se torne crônico. Para isso, definimos quatro objetivos claros. Primeiro, analisar a evolução dos dados educacionais de 2022 a 2024. Segundo, identificar quais fatores de risco são mais relevantes para a defasagem. Terceiro, construir um modelo preditivo robusto. E por fim, criar uma ferramenta interativa que os educadores possam usar no dia a dia. Mas para tudo isso, precisávamos entender a base de dados.

# 3 - Os Dados

A Passos Mágicos utiliza a Pesquisa de Desenvolvimento Educacional, a PEDE, que nos forneceu uma base rica. Analisamos um total de 3.030 registros de alunos ao longo de três anos. A base cresceu a cada ano, refletindo a expansão da ONG. A PEDE é estruturada em torno de indicadores-chave que medem o desenvolvimento do aluno. O IAN, por exemplo, mede a Adequação ao Nível, que é a nossa métrica de defasagem. Outros indicadores como Engajamento, Desempenho e Ponto de Virada nos dão uma visão 360 do aluno. Com essa base, pudemos partir para as descobertas.

# 4 - Principais Descobertas

A análise dos dados da PEDE revelou uma realidade crítica: 70% dos alunos estão em algum nível de defasagem. Essa distribuição se divide em 67% em Risco Moderado e 3% em Risco Severo. Isso reforça a urgência de uma intervenção preditiva. Nossas descobertas indicam que o Índice Global de Desenvolvimento, o INDE, é o melhor preditor de risco, com 35% de importância. O Ponto de Virada e o Desempenho Acadêmico também são determinantes, somando 31% de importância. Esses insights nos guiaram na construção de um modelo focado nos indicadores mais relevantes.

# 5 - Modelo Preditivo

Para operacionalizar essas descobertas, construímos um Modelo Preditivo usando o algoritmo Random Forest. O modelo classifica o risco em três classes: Sem Risco, Risco Moderado e Risco Severo, seguindo a metodologia da Passos Mágicos. A acurácia geral do modelo é de 75.6%, um resultado sólido para um problema de classificação complexo. Mais importante, o Recall para Risco Moderado atingiu 82%. Isso significa que o modelo é altamente sensível em identificar alunos que precisam de atenção imediata. Agora, vamos detalhar quais features foram cruciais para o modelo atingir essa performance.

# 6 - Features Mais Importantes

O modelo é robusto, mas o que realmente define o risco de defasagem? A análise de Feature Importance nos mostra quais indicadores são cruciais para a decisão do modelo. O Índice Geral de Desenvolvimento, o INDE, é o preditor dominante, respondendo por 34.7% da decisão. Isso significa que o desempenho global do aluno é o fator mais crítico. Mas o modelo não depende só dele. O Ponto de Virada, o IPV, e o Desempenho Acadêmico, o IDA, somam mais de 31% da importância. Isso reforça que a capacidade de recuperação e as notas diretas são fatores de risco significativos. Esses insights nos permitem focar as intervenções nos fatores que o modelo considera mais críticos. Agora, vamos ver como a equipe da Passos Mágicos pode usar isso no dia a dia.

# 7 - Aplicação Streamlit

Para que o modelo não fique apenas na teoria, criamos esta Aplicação Streamlit, tornando a predição acessível a todos. A ferramenta tem três funcionalidades principais. O Dashboard interativo permite visualizar a evolução histórica dos indicadores, facilitando a compreensão do contexto geral. A interface de Predição é onde o educador insere os dados de um novo aluno e recebe a avaliação de risco em tempo real. E o mais importante, a seção de Ação, que gera recomendações automáticas de intervenção baseadas no nível de risco identificado. Usamos tecnologias robustas como Python e Streamlit para garantir que a ferramenta seja prática e confiável. Com a ferramenta pronta, podemos traçar as recomendações estratégicas.

# 8 - Recomendações

Com o diagnóstico e a ferramenta em mãos, definimos um Plano de Ação com Recomendações Estratégicas para maximizar o impacto. Para os alunos em alto risco, a prioridade é o Acompanhamento Intensivo, focado nas áreas onde a defasagem é mais crítica. Também é vital o Suporte Psicossocial, pois o modelo nos mostrou que fatores externos influenciam o desempenho. Para a organização, a principal recomendação é Priorizar o Engajamento, pois ele é um motor do desenvolvimento. Além disso, a Passos Mágicos deve usar o modelo para Triagem Preditiva, identificando riscos logo na entrada de novos alunos. Essas ações transformam o dado em decisão. E com isso, chegamos à nossa conclusão.

# 9 - Conclusão

Em resumo, o Datathon entregou um valor significativo para a Passos Mágicos. Realizamos um Diagnóstico Completo, confirmando que 70% dos alunos estão em defasagem e que o INDE é o principal preditor. Entregamos um modelo de Alta Sensibilidade, com 75.6% de acurácia e 82% de recall para risco moderado, crucial para a intervenção preventiva. E o mais importante, criamos uma Ferramenta Prática, a aplicação Streamlit, que leva a inteligência de dados diretamente para a equipe pedagógica. O modelo identifica padrões nos indicadores que permitem prever alunos em risco antes que a defasagem aconteça. Agora, queremos agradecer.

# 10 - Obrigado!

Chegamos ao fim da nossa apresentação. Queremos agradecer imensamente à Associação Passos Mágicos pela confiança e pelos dados, e à FIAP pela oportunidade de participar deste Datathon. Nossa equipe está à disposição para responder a quaisquer perguntas. Deixamos aqui o nosso contato e o link para o repositório no GitHub e para a aplicação Streamlit. Lembrem-se: estamos transformando dados em oportunidades, e oportunidades em vidas transformadas. Muito obrigado.
