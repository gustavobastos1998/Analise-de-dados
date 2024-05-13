## *Operadores de Intervalo*

### *BETWEEN*

- Utilizado para determinar intervalo entre A e B. OBS: os elementos A e B estão inclusos na operação.
- Este operador só pode ser utilizado para intervalos numéricos. 
- Exemplo: ![[between_exemplo.png]]

### *IN*

- Permite o usuário especificar múltiplos valores para seleção. 
- Quando utilizado na cláusula <mark style="background: #ABF7F7A6;">WHERE</mark> ele filtra todos os valores cujo valor seja igual a X, Y ou Z.
- Exemplo: ![[IN exemplo1.png]]
- ![[IN exemplo2.png]]

### *LIKE*

- Busca padrão no valor da coluna. 
- Filtra todas as linhas caso encontre esse padrão especificado no valor da coluna.
- Ele é utilizado em conjunto com apóstrofos e o sinal de porcentagem (%). 
- Tudo a esquerda da porcentagem é o padrão do começo de algo que é desejado e tudo a direita o final. Para especificar algo no meio, basta adicionar um segundo %.
- Exemplo: nesse exemplo, ele filtrará todas as categorias de produtos cujo o nome delas comece com a letra 'a'. 
- ![[LIKE exemplo1.png]]
- Exemplo: nesse exemplo, ele filtrará todas as categorias de produtos cujo o nome delas termine em 'ria'.
- ![[LIKE exemplo2.png]]
- Exemplo: nesse exemplo, ele filtrará todas as categorias cujo o nome delas comece com 'a' tenha um 's' em qualquer parte que não seja o último caractere e termine com a letra 'o'. 
- ![[LIKE exemplo3.png]]

### *HAVING*

- Permite filtrar linhas a partir do resultado de uma função agregadora. 
- Exemplo: 
- ![[HAVING exemplo1.png]]
- ![[HAVING exemplo2.png]]

## *OBSERVAÇÕES*

- <mark style="background: #ABF7F7A6;">NOT</mark> pode ser utilizado em conjuntos com diversos operadores de intervalo para exclusão. Por exemplo, junto de <mark style="background: #ABF7F7A6;">IN</mark> ele exclui todos os valores especificados. Sempre vem antes dos operadores.
- Exemplo: 
- ![[NOT exemplo1.png]]
- ![[NOT exemplo2.png]]