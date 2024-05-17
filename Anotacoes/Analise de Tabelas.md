
- De maneira simples e sucinta, é importante analisar as tabelas do banco de dados individualmente e suas junções depois. 
- Ao analisar as tabelas de maneira individual, fica claro se há repetições de linhas nelas. Importante ressaltar que dependendo da estrutura de negócio a "duplicidade" de uma linha faz sentido. A palavra duplicidade está entre aspas pois não se trata de um clone de outra linha, pois para que isso aconteça alguma coluna tem que ser necessariamente diferente entre as linhas.
- É imprescindível fazer a mesma análise quando for feito a junção de duas ou mais tabelas. Caso haja "duplicidade" de linhas, qual coluna está causando essa diferenciação? Ao localizá-la, fica fácil enxergar qual o sentido e propósito desta diferença. 


## *Para uma tabela*

- Para fazer a análise de uma tabela, basta fazer uma contagem da chave primária, agrupar por ela e pegar os resultados para essa contagem que sejam maiores do que um. Fazendo isso, uma filtragem de quantos id's existem para cada chave primária daquela tabela será mostrada. 
- Caso não esboce um resultado para essa query, significa que não há repetição de chave primária na tabela. 
- Exemplo: 
  ![[analise uma tabela.png]]

## *Para mais de uma tabela*

- A análise para mais de uma tabela é bem parecida com a de cima. A diferença é que um JOIN será feito para unir as tabelas e implicações equivocadas aparentam acontecer como: um pedido se repetir mais de uma vez.
- Como dito anteriormente, é necessário averiguar qual coluna se modifica entre as linhas e analisar se faz sentido para as regras de negócios da empresa. 
- Exemplo: ![[analise mais de uma tabela.png]]
- O resultado da query acima é:
- ![[resultado query analise duas tabelas.png]]
- Isso implica que o order_id, que é uma chave primária única, está se repetindo ao fazer a junção com a order_items. 
- Para analisar qual coluna está causando esta "duplicidade" basta pegarmos um order_id que se repita e ver todas as suas colunas. 
- ![[checagem coluna id especifico para analise.png]]

## *Conclusão*

- Ao fazer essas análises, fica muito mais claro como o negócio da empresa funciona. Além de facilitar o entendimento do banco de dados em si. 