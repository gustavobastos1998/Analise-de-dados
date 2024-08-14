## *O que é Power Query?*
***
- O Power Query é uma ferramenta que prepara dados e faz parte da suíte Power BI da Microsoft.
- O principal objetivo do Power Query é auxiliar os usuários na importação, tratamento, limpeza e edição dos dados provenientes de diversas fontes. Isso possibilita que esses dados sejam facilmente utilizados posteriormente dentro do Power BI para a criação de relatórios e análises.

## *Tratamento de Dados no Power Query*
***

- Ao clicar com o botão direito sobre uma coluna no Power Query, encontramos algumas opções de tratamentos de dados muito úteis. 

### *Cortar (TRIM)*
***

- Usada para "limpar" espaços em branco. 

### *Substituir valores*
***

- Substitui valores de acordo com a regra direcionada pelo usuário.

## *Mesclando tabelas no Power Query*
***

- Para isso usaremos o recurso Mesclar Consultas do Power Query. O caminho para acessar este recurso é <mark style="background: #BBFABBA6;">Pagina Inicial > Combinar > Mesclar Consultas</mark>.
- ![[mesclar tabelas.png]]
- Parecido com os comandos de JOIN no banco de dados, a mescla das tabelas no Power BI é muito mais simples e intuitiva. Tudo é feito pela interface gráfica no Power BI, selecionando as tabelas e o campo em comum das tabelas para fazer a ligação, assim como é feito em um INNER JOIN ou LEFT JOIN.
- IMPORTANTE: duas etapas aplicadas, no power query, importantes para mesclagem de duas tabelas é a de cortar (trim) e limpar (clean). Essas applied steps são referentes a coluna que irá fazer a ligação entre as tabelas, ou seja, a chave primária de uma e estrangeira de outra, geralmente o id. 