## *As Operações Matemáticas no SQL*

- As operações matemáticas no SQL acontecem na cláusula SELECT. Algumas podem ser utilizadas no WHERE. 

### *Contagem*

- Contagem da quantidade de uma certa coluna. 
- SELECT COUNT (students_id)
   FROM tabela_matriculas

### *Soma*

- Soma o valor de determinada coluna.
- SELECT SUM (price)
   FROM tabela_matriculas

### *Média*

- Calcula a média dos valores da coluna.
- SELECT AVG (price)
   FROM tabela_matriculas

### *Máximo*

- Seleciona o maior valor entre todos os valores da coluna.
- SELECT MAX (price)
   FROM tabela_matriculas

### *Mínimo*

- Seleciona o menor valor entre todos os valores da coluna
- SELECT MIN (price)
   FROM tabela_matriculas

### *Valores Únicos*

- Seleciona somente valores únicos. Caso o valor da coluna escolhida venha a se repetir, ele não exibe. 
- SELECT DISTINCT course_name
   FROM tabela_cursos

### *Contagem de Valores Únicos*

- Conta a quantidade de valores únicos de uma coluna. 
- SELECT COUNT (DISTINCT student_id)
   FROM tabela_matriculas


## *Observações*

- Há como nomear essas funções no SQL, dando um nome adequado para tal operação. 
- SELECT COUNT (students_id) AS quantidade_de_alunos
   FROM tabela_matriculas