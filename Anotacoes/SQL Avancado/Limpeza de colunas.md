## *Funções de manipulação*
***

### *COALESCE*
***

- Retorna o primeiro elemento não vazio. Na prática, serve para substituir dados faltantes.
- Exemplo:
- ![[exemplo coalesce.png]]
- Resultado: 
- ![[resultado exemplo coalesce.png]]
- Também é utilizado para junta texto com outras colunas.
- Exemplo2: 
- ![[exemplo2 coalesce.png]]
- Resultado: neste caso é feito uma concatenação dos texto com a utilização do pipe "|". Entre os pipes é colocado a string entre os textos.
- ![[resultado exemplo 2 coalesce.png]]

### *LOWER E UPPER*
***

- São utilizados para transformar todos os caracteres em caixa baixa ou alta. 

### *SUBSTRING*
***

- Tem a função de recortar texto, retornando uma substring. 
- Sintax: <mark style="background: #BBFABBA6;">SUBSTRING (coluna, -indice_inicio-, -qtd_de_caracteres_desejados_apos_o_indice_de_inicio-) AS substring</mark>. Observação importante: o índice de início conta para a quantidade de caracteres desejados após ele, portanto, no caso de 'SUBSTRING (coluna,5,2)', a substring retornada terá dois caracteres e partirá do quinto caracter da string original. 
- Útil para limpar emails.

### *REPLACE*
***

- Substitui um texto antigo por um novo. 
- Sintax: <mark style="background: #BBFABBA6;">REPLACE(coluna, -texto_antigo-, -texto_novo-)</mark>

### *ROUND*
***

- Arredonda números.
- Sintax: <mark style="background: #BBFABBA6;">ROUND (coluna, -qtd_de_casas_decimais)</mark>
- Caso não queira nenhuma casa decimal, basta colocar 0 como terceiro parâmetro. 

## *OBS*
***

- Essas sintaxes são para o SQLite, para outro banco a sintaxe irá mudar. 