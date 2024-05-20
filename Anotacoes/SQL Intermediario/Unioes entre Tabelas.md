## *Os Tipos de Uniões em SQL*

### *INNER JOIN*

- Retorna somente as linhas que estão tanto na tabela da esquerda quanto na tabela da direita. 
- Faz conexão de 1:1 entre as tabelas. Se o elemento da tabela da esquerda não tiver um correspondente na direita, ele não trás o resultado. 
- Exemplo: ![[exemplo inner join.png]]

### *LEFT JOIN*

- Retorna <mark style="background: #FF5582A6;">TODAS</mark> as linhas da esquerda e <mark style="background: #FF5582A6;">SOMENTE</mark> as linhas correspondentes da direita. Caso essa linha correspondente não existir na tabela da direita, o valor NULL é retornado. 
- Exemplo: ![[exemplo left join.png]]

### *RIGHT JOIN*

- Retorna <mark style="background: #FF5582A6;">TODAS</mark> as linhas da direita e <mark style="background: #FF5582A6;">SOMENTE</mark> as linhas correspondentes da esquerda. Caso essa linha correspondente não existir na tabela da direita, o valor NULL é retornado. 
- Exemplo: ![[exemplo right join.png]]

### *FULL OUTER JOIN*

- Retorna <mark style="background: #FF5582A6;">TODAS</mark> as linhas da direita e todas as linhas da esquerda, mesmo se não houver correspondentes. As linhas que não têm correspondência são preenchidas com NULL. 
- Exemplo: ![[exemplo full outer join.png]]

## *Diagrama de Venn*

- ![[diagrama de Venn.png]]
- Com a utilização de conceitos da teoria de conjuntos, esse diagrama ajuda a ilustrar como são feitas os joins do SQL. 

## *OBS*

- Na prática, outra palavra reservada pelo SQL é utilizada em conjunto com essas uniões sendo ela <mark style="background: #ABF7F7A6;">ON</mark>. Após ela, vem uma condicional informando quais linhas eu quero relacionar entre as tabelas. Importante ressaltar que essa conexão deve existir pela presença de chaves estrangeiras que interliguem as tabelas.