
## *Operações Matemáticas em Agrupamentos*

- Resumem um conjunto de dados em apenas um número. São realizadas dentro de agrupamentos. 
## *Agrupamentos no SQL*

- Uma ou mais operações são aplicadas a um ou mais grupos e subgrupos.
- Os agrupamentos são feitos com a cláusula <mark style="background: #ABF7F7A6;">GROUP BY</mark>. Ele vem depois da cláusula <mark style="background: #ABF7F7A6;">FROM</mark> e deve ser escolhido uma ou mais colunas da tabela. 
- No caso de agrupamentos com duas dimensões ou mais, a ordem de escolha das colunas influencia na exibição do SQL. Essa ordem é definida no <mark style="background: #ABF7F7A6;">SELECT</mark>. Uma boa prática é colocar as colunas no <mark style="background: #ABF7F7A6;">GROUP BY</mark> na mesma ordem descrita no <mark style="background: #ABF7F7A6;">SELECT</mark>.
- Não é possível agrupar por funções agregadoras. A cláusula <mark style="background: #ABF7F7A6;">HAVING</mark> tem essa função. <mark style="background: #ABF7F7A6;">DATE</mark> não é função agregadora, ela muda o formato da data para ano mês dia (yyyy-mm-dd). 

### *Exemplo*

- ![[agrupamento uma variavel exemplo1.png]]
- ![[agrupamento uma variavel exemplo2.png]]
- ![[agrupamento duas variaveis exemplo1.png]]
- ![[agrupamento duas variaveis exemplo2.png]]

## *OBS*
***

- Somente as colunas presente na projeção, ou seja, na cláusula <mark style="background: #ABF7F7A6;">SELECT</mark>, devem aparecer no <mark style="background: #ABF7F7A6;">GROUP BY</mark>. Caso contrário, não funcionará. 
- O SQLite permite fazer isso, porém isso é um <mark style="background: #FF5582A6;">erro de lógica</mark>, ocasionando em queries erradas. 
- Funções agregadoras são permitidas na projeção.
- Oracle: SelectItems in the SelectExpression with a GROUP BY clause must contain only aggregates or grouping columns. 