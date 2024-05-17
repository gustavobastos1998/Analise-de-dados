## *O que são subqueries?*
***

-  São consultas dentro de outra consulta. 

## *Subqueries no SELECT*
***

- Subqueries na cláusula <mark style="background: #ABF7F7A6;">SELECT</mark> auxiliam na criação de uma nova coluna, além de fazer uma operação específica com intuito de coletar informações de colunas para serem usadas na query principal. 
- Exemplo: ![[exemplo subquery select.png]]
- As vezes, as subqueries podem ser reescritas com auxílio de <mark style="background: #ABF7F7A6;">JOIN</mark> no SQL. 
- Exemplo: ![[equivalente subquery select left join.png]]

## *Subqueries no WHERE*
***

- Subqueries na cláusula <mark style="background: #ABF7F7A6;">WHERE</mark> permitem filtrar linhas da tabela principal a partir do resultado de uma consulta em outra.
- Exemplo: ![[exemplo subquery where.png]]
- ![[equivalente subquery where left join.png]]

## *Subqueries no FROM*
***

- Subqueries na cláusula FROM auxiliam na criação de uma nova tabela origem. 
- Para fazer isso, devemos primeiro fazer as subqueries necessárias para a criação da tabela origem da query principal. 
- Exemplo: ![[subquery from 1.png]]
- ![[subquery from 2.png]]
- ![[subquery from 3.png]]
- Query principal utilizando as três subqueries a cima:
- ![[resultante subquery from.png]]

## *OBS*

*** 
### *subquery vs join*

- Subquery é a forma correta logicamente de resolver problemas do tipo "colete fatos da tabela A e fatos condicionais da tabela B". Além de correta é mais segura que um <mark style="background: #ABF7F7A6;">LEFT JOIN</mark>, pois não corre o risco de pegar duplcatas da tabela A para casar com as linhas da tabela B.
- Na prática, as subqueries ganham em performance perante as junções. Porém, a leitura de queries contendo subqueries torna-se um desafio ante os joins. 