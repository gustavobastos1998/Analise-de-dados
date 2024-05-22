## *O que é?*
***

- É uma função que é usada em um ou mais linhas para retornar um valor para cada linha. 
- Em termos simples, as window functions em SQL permitem que você realize cálculos ou agregações em um conjunto específico de linhas relacionadas a uma linha de dados específica.
- Essas funções operam sobre uma "janela" de dados que é definida com base em condições específicas, como uma partição ou ordenação.
- Elas são úteis para comparação entre valores de colunas individuais e operações feitas sobre elas. 

## *Sintaxe*
***

- ![[windows function sintax.png]]

## *Elementos da windows function*
***

- <mark style="background: #BBFABBA6;">windows_function</mark>: É a função de janela que vai ser utilizada.
- <mark style="background: #BBFABBA6;">(expression)</mark>: nome da coluna que deseja aplicar a operação. Algumas window functions não dependem de colunas. 
- <mark style="background: #BBFABBA6;">OVER</mark>: identifica uma window function. Sem a presença dele não é uma função de janela.
- <mark style="background: #BBFABBA6;">PARTITION BY</mark>: divide as linhas me partições.
- <mark style="background: #BBFABBA6;">partition_list</mark>: nome da coluna que deseja segmentar.
- <mark style="background: #BBFABBA6;">ORDER BY</mark>: usado para ordenar as linhas.
- <mark style="background: #BBFABBA6;">order_list</mark>: nome das colunas da ordenação.
- <mark style="background: #BBFABBA6;">ROWS</mark>: indica os limites da janela. 
- <mark style="background: #BBFABBA6;">frame_cause</mark>: determina os limites de linhas dentro da janela.

## *Tipos de funções de janela*
***

### *Agregação*
***

- <mark style="background: #FFF3A3A6;">AVG</mark>(): calcula média.
- <mark style="background: #FFF3A3A6;">MAX</mark>(): calcula o valor máximo.
- <mark style="background: #FFF3A3A6;">MIN</mark>(): calcula o menor valor.

### *Ranqueamento*
***

- <mark style="background: #FFF3A3A6;">ROW_NUMBER</mark>(): enumera as linhas, começando por 1 até o valor da última linha de acordo com a ordenação especificada dentro da janela. Essa função independe de parâmetros. Útil para ranquear produtos por preço descendente por exemplo, atrelando ao produto mais caro o rank 1, ao segundo mais caro rank 2 etc. 
- Exemplo: neste exemplo, os produtos estão sendo ranqueados por categoria e ordenados de maneira descente pelo preço. 
- ![[exemplo row number.png]]
- Obs: o <mark style="background: #ABF7F7A6;">ROW_NUMBER( )</mark> não atribui o mesmo rank para colunas com o mesmo valor, ou seja, caso dois ou mais produtos tenham o mesmo valor ele irá colocá-los em diferentes ranks. 
- <mark style="background: #FFF3A3A6;">RANK</mark>(): tem a mesma função de <mark style="background: #ABF7F7A6;">ROW_NUMBER( )</mark> porém ele ranqueia, para o mesmo valor, o mesmo rank. O problema do RANK( ) é que ele não continua o ranqueamento a partir do próximo número, ele continua a contagem internamente e atribui esse valor no lugar. Essa função independe de parâmetros.
- Exemplo: para este exemplo, dois produtos estão ranqueados como 9, porém os próximos deviam ser ranqueados como 10 e o mesmo serve para o produto de rank 17. 
- ![[tabela resultado rank.png]]
- <mark style="background: #FFF3A3A6;">DENSE_RANK</mark>(): para sanar os dois problemas dos outros dois ranks (), o DENSE_RANK( ) foi criado. Essa função independe de parâmetros.
- <mark style="background: #FFF3A3A6;">PERCENT_RANK</mark>(): utilizado para representar o percentual de cada coluna em detrimento do total. Essa função independe de parâmetros.
- <mark style="background: #FFF3A3A6;">NTILE</mark>(): separa todos os seguimentos em blocos e os ranqueia. É preciso indicar a quantidade de blocos desejado passando como parâmetro da função. Digamos que em um segmento há 100 linhas, para um NTILE(4) ele divide da seguinte maneira: [1, 26[ -> rank 1; [26, 50[ -> rank 2; [50, 76[ -> rank 3; [76, 100] -> rank 4

### *Valor*
***

- <mark style="background: #FFF3A3A6;">LAG</mark>(): causa deslocamento adiantado, avançando valores da coluna. Serve para curvas de comportamento. 
- Exemplo: neste exemplo, o shipping_limit_date aparece na linha de baixo na coluna de date_shift. Útil para comparar datas entre as compras.
- ![[exemplo lag.png]]
- ![[resultado lag.png]]
- <mark style="background: #FFF3A3A6;">LEAD</mark>(): contrário do lag(). Recua uma coluna, atrasando ao invés de avançar. 
- <mark style="background: #FFF3A3A6;">FIRST_VALUE</mark>(): retorna o primeiro valor da coluna escolhida. 
- <mark style="background: #FFF3A3A6;">LAST_VALUE</mark>(): retorna o último valor da coluna escolhida. 
- <mark style="background: #FFF3A3A6;">NTH_VALUE</mark>(): retorna o enésimo valor da coluna escolhida. Passa como parâmetro após a escolha da coluna.

## *Controle do tamanho da janela*
***

- PRECEDING - considera X linhas antes da linha atual
- CURRENT - considera até a linha atual
- FOLLOWING - considera X linhas após a linha atual
- Exemplo: neste exemplo, queremos calcular uma média móvel que pega sete valores antes até a linha atual. Quando chegar na 8ª linha, ele deixa de pegar a primeira linha da tabela. Por isso essa média é móvel.
- ![[exemplo preceding e current.png]]
- Exemplo 2: neste caso, as 3 linhas antes e 2 após o atual entram no cálculo da média. Detalhe, a linha atual também entra no cálculo. 
- ![[exemplo preceding e following.png]]