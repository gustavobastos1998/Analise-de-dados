## *Operações com colunas na cláusula SELECT*
***

- É possível utilizar operações matemáticas em colunas com valores numéricos.
- Exemplo:
- ![[exemplo operacao select.png]]

## *Operações condicionais na cláusula SELECT*
***

- Também há a possibilidade de impor condições na exibição das colunas. Funcionando exatamente igual a um if else. Para fazer isso, utilizamos as palavras reservadas '<mark style="background: #ABF7F7A6;">CASE</mark>', '<mark style="background: #ABF7F7A6;">WHEN</mark>', '<mark style="background: #ABF7F7A6;">THEN</mark>', '<mark style="background: #ABF7F7A6;">ELSE</mark>' e '<mark style="background: #ABF7F7A6;">END</mark>'. 
- Outra forma de fazer é utilizando a função IIF que tem uma sintaxe um pouco diferente mas que atinge o mesmo resultado. 
- Exemplo: ![[case when iif exemplo.png]]

### *CASE WHEN aninhado*
***

- ![[case when aninhado.png]]