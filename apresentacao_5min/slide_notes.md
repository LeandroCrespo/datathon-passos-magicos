# 1 - Datathon FIAP - Passos Mágicos

Estamos aqui para apresentar o resultado do Datathon FIAP em parceria com a Associação Passos Mágicos. Nosso foco foi transformar dados em uma ferramenta prática para a educação. O objetivo central foi criar um Modelo Preditivo de Risco de Defasagem Escolar. Este projeto faz parte da Pós-Tech em Data Analytics da FIAP. Vamos mostrar como a análise de dados pode apoiar a Passos Mágicos a continuar transformando vidas. Agora, vamos entender o desafio que nos foi proposto.

# 2 - O Desafio

O desafio principal era identificar alunos em risco de defasagem de forma precoce. Precisamos agir antes que o problema se torne crônico. Para isso, definimos quatro objetivos claros. Primeiro, analisar a evolução dos dados educacionais de 2022 a 2024. Segundo, identificar quais fatores de risco são mais relevantes para a defasagem. Terceiro, construir um modelo preditivo robusto. E por fim, criar uma ferramenta interativa que os educadores possam usar no dia a dia. Mas para tudo isso, precisávamos entender a base de dados.

# 3 - Os Dados

A Passos Mágicos utiliza a Pesquisa de Desenvolvimento Educacional, a PEDE, que nos forneceu uma base rica. Analisamos um total de 3.030 registros de alunos ao longo de três anos. A base cresceu a cada ano, refletindo a expansão da ONG. A PEDE é estruturada em torno de indicadores-chave que medem o desenvolvimento do aluno. O IAN, por exemplo, mede a Adequação ao Nível, que é a nossa métrica de defasagem. Outros indicadores como Engajamento, Desempenho e Ponto de Virada nos dão uma visão 360 do aluno. Com essa base, pudemos partir para as descobertas.

# 4 - Principais Descobertas

Com a análise dos dados da PEDE, chegamos a descobertas cruciais. A primeira é que as ações da Passos Mágicos estão funcionando. Vimos que 42% dos alunos estão na fase correta em 2024, um aumento significativo em relação aos 29% de 2022. A segunda descoberta é que o Engajamento, o IEG, é o motor do desenvolvimento. Ele tem a maior correlação com o desempenho global do aluno. Isso significa que investir em engajamento gera um impacto em cascata. E a terceira descoberta é o Ponto de Virada, o IPV. Ele é um indicador de resiliência, mostrando quais alunos superaram dificuldades. Essas descobertas nos deram a base para construir o modelo. E é sobre esse modelo que vamos falar agora.

# 5 - Modelo Preditivo

Para transformar essas descobertas em uma ferramenta de ação, construímos um Modelo Preditivo usando o algoritmo Random Forest. Nosso objetivo era prever se um aluno teria defasagem. A métrica mais importante para a Passos Mágicos é o Recall, a sensibilidade. Precisamos identificar o máximo de alunos em risco real para que a intervenção seja feita. Nosso modelo atingiu 65.38% de Recall. Isso significa que ele consegue identificar a maioria dos alunos que realmente estão em risco. A qualidade global do modelo, medida pelo AUC-ROC, também é alta, em 87.75%. Mas quais fatores o modelo considerou mais importantes para essa predição?

# 6 - Features Mais Importantes

Entender quais fatores o modelo considera mais importantes é crucial para direcionar as intervenções. O IAN, ou Adequação ao Nível, é o preditor dominante, o que é esperado, pois ele mede diretamente a defasagem idade-série. Ele responde por 29.9% da decisão do modelo. Mas o modelo não depende só dele. O IPS, que mede os Aspectos Psicossociais, aparece em segundo lugar com 11.8%. Isso reforça que o bem-estar emocional e social do aluno é um fator de risco significativo. A Média Geral dos indicadores e o IPV, o Ponto de Virada, também são relevantes. O IPV, com 8.3%, mostra que a atitude e a superação do aluno são sinais fortes de que ele pode sair da zona de risco. Esses insights nos permitem focar as intervenções nos fatores que o modelo considera mais críticos. Agora, vamos ver como a equipe da Passos Mágicos pode usar isso no dia a dia.

# 7 - Aplicação Streamlit

Para que o modelo não fique apenas na teoria, criamos esta Aplicação Streamlit, tornando a predição acessível a todos. A ferramenta tem três funcionalidades principais. O Dashboard interativo permite visualizar a evolução histórica dos indicadores, facilitando a compreensão do contexto geral. A interface de Predição é onde o educador insere os dados de um novo aluno e recebe a avaliação de risco em tempo real. E o mais importante, a seção de Ação, que gera recomendações automáticas de intervenção baseadas no nível de risco identificado. Usamos tecnologias robustas como Python, Streamlit e Scikit-learn para garantir que a ferramenta seja prática e confiável. Com a ferramenta pronta, podemos traçar as recomendações estratégicas.

# 8 - Recomendações

Com o diagnóstico e a ferramenta em mãos, definimos um Plano de Ação com Recomendações Estratégicas para maximizar o impacto. Para os alunos em alto risco, a prioridade é o Acompanhamento Intensivo, focado nas áreas onde o IAN está mais crítico. Também é vital o Suporte Psicossocial, pois o modelo nos mostrou que fatores externos influenciam o desempenho. Para a organização, a principal recomendação é Priorizar o Engajamento, o IEG, pois vimos que ele é o motor do desenvolvimento. Além disso, a Passos Mágicos deve usar o modelo para Triagem Preditiva, identificando riscos logo na entrada de novos alunos. Essas ações transformam o dado em decisão. E com isso, chegamos à nossa conclusão.

# 9 - Conclusão

Em resumo, o Datathon entregou um valor significativo para a Passos Mágicos. Realizamos um Diagnóstico Completo, analisando a evolução educacional de 2022 a 2024 e confirmando o impacto positivo da organização. Entregamos um modelo de Alta Precisão, capaz de identificar 87% dos alunos em risco, o que é crucial para a intervenção preventiva. E o mais importante, criamos uma Ferramenta Prática, a aplicação Streamlit, que leva a inteligência de dados diretamente para a equipe pedagógica. O Engajamento e o Ponto de Virada se destacaram como os Insights Acionáveis mais importantes. Transformamos dados em oportunidades. Agora, queremos agradecer.

# 10 - Obrigado!

Chegamos ao fim da nossa apresentação. Queremos agradecer imensamente à Associação Passos Mágicos pela confiança e pelos dados, e à FIAP pela oportunidade de participar deste Datathon. Nossa equipe está à disposição para responder a quaisquer perguntas. Deixamos aqui o nosso contato e o link para o repositório no GitHub e para a aplicação Streamlit. Lembrem-se: estamos transformando dados em oportunidades, e oportunidades em vidas transformadas. Muito obrigado.
