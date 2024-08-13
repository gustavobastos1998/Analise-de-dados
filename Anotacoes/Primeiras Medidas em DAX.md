## *O que é DAX?*
***

- Significa Data Analysis Expressions. Cria medidas no power BI.

## *O que são medidas?*
***

- Medidas calculam um resultado por meio de uma fórmula de expressão. Expressões podem ser medidas. Os resultados vão se alterando conforme sua interação com os relatórios, permitindo exploração de dados.
- São criadas e exibidas na '<mark style="background: #FFB86CA6;">Exibição de Relatório</mark>', na '<mark style="background: #FFB86CA6;">Exibição de Dados</mark>' ou na '<mark style="background: #FFB86CA6;">Exibição de Modelo</mark>'. 
- As medidas são exibidas na lista de **campos** com um ícone de **calculadora**. Elas podem ter o nome que desejar e há a possibilidade de adicioná-las a uma visualização nova ou existente, por exemplo em um gráfico.

## *Construindo suas Primeiras Medidas em DAX*
***

- <mark style="background: #ABF7F7A6;">COUNTROWS(_table_)</mark> : conta o número de linhas na tabela específica ou em uma tabela definida por uma expressão. 
- <mark style="background: #ABF7F7A6;">DISTINCTCOUNT(_coluna_)</mark> : conta valores distintos de uma coluna.
- <mark style="background: #ABF7F7A6;">SUM(_coluna_)</mark> : soma valores de uma coluna.

## *Como apresentar o resultado de uma medida*
***

- Para um único valor, como vendas totais, quantidade de produtos etc, a '<mark style="background: #FFB86CA6;">visualização de cartão</mark>' pode ser a melhor forma de exibição. 
- Assim como quase todas as visualizações nativas do Power BI, os cartões podem ser criados através da guia de '<mark style="background: #FFB86CA6;">visualizações</mark>'.

## *Gráfico de Barras*
***

- Usado para exibir séries combinadas, organizar e facilitar a visualização de dados.
- Comparação entre grupos é um ótimo exemplo de sua utilidade.

## *Segmentação de Dados (slicer)*
***

- Tipo de filtragem que restringe parte do conjunto de dados mostrado na visualização do relatório. 
- Não aceitam medidas (measures), só aceitam colunas ou colunas calculadas.