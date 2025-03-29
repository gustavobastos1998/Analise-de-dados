#================================== IMPORTS ==================================
import os
import requests
import pandas as pd
import sqlite3

# diretorio destino
data_directory = "data"

#================================== Baixar arquivos ==================================

# URL base dos datasets do IMDB
base_url = "https://datasets.imdbws.com/"

# arquivos para serem baixados
files = [
    "name.basics.tsv.gz",
    "title.akas.tsv.gz",
    "title.basics.tsv.gz",
    "title.crew.tsv.gz",
    "title.episode.tsv.gz",
    "title.principals.tsv.gz",
    "title.ratings.tsv.gz",
]

os.makedirs(data_directory, exist_ok=True)

# baixar os arquivos
for file in files:
    url = base_url + file
    destiny_file_name = os.path.join(data_directory, file)

    # verificação se o arquivo ja foi baixado
    if not os.path.exists(destiny_file_name):
        print(f'Baixando {file}...')
        response = requests.get(url)

        # verificação da resposta da página (200 para sucesso)
        if response.status_code == 200:
            with open(destiny_file_name, 'wb') as f:
                f.write(response.content)
            print(f'{file} baixado com sucesso!')    
        else:
            print(f'Falha ao baixar o {file}. Código de status {response.status_code}')
    else:
        print(f'{file} já existe. Download já foi executado antes')
print('Download concluído.')

#================================ tratamento de dados ====================================

# diretorio de dados tratados
processed_data_directory = os.path.join(data_directory, 'tratado')

# certificação de existência do diretorio 'tratado'
os.makedirs(processed_data_directory, exist_ok=True)

# lista dos arquivos de dataset compactados
files = os.listdir(data_directory)

# loop para abrir, tratar e salvar cada arquivo
for file in files:
    file_path = os.path.join(data_directory, file)

    if os.path.isfile(file_path) and file.endswith('.gz'):
        print(f'Lendo e tratando o arquivo {file}')
        # leitura do arquivo TSV usando o pandas
        df = pd.read_csv(file_path, sep='\t', compression='gzip', low_memory=False)
    
        # substitui os caracters '\N' por fvalor nulo
        df.replace({'\\N':None}, inplace=True)
    
        # salva o dataframe no diretório de tratado após a descompressão dos arquivos
        destiny_directory = os.path.join(processed_data_directory, file[:-3]) # remove a extensão .gz
        df.to_csv(destiny_directory, sep='\t', index=False)
    
        print(f'Tratamento concluído para {file}. Arquivo tratado salvo em {destiny_directory}')

print('Todos os arquivos foram tratados e salvos.')

# Arquivo data base
data_base = 'imdb_data.db'

#================ Salvando em banco de dados com SQLite =================

# diretorios
processed_data_directory = os.path.join('data', 'tratado')

# conecta ao banco os dados SQLite
connection = sqlite3.connect(data_base)

# lista todos os arquivos do diretorio 'tratado'
files = os.listdir(processed_data_directory)

# loop para ler cada arquivo e salvar em tabela sqlite
for file in files:
    dir_file = os.path.join(processed_data_directory, file)

    if os.path.isfile(dir_file) and file.endswith('.tsv'):
        # lê o arquivo tsv com o pandas
        df = pd.read_csv(dir_file, sep='\t', low_memory=False)

        # remove a extensão do nome do arquivo
        table_name = os.path.splitext(file)[0]

        # substitui caracteres '.' e '-' para '_'
        table_name = table_name.replace('.', '_').replace('-', '_')

        # salva o dataframe na tabela sqlite
        df.to_sql(table_name, connection, index=False, if_exists='replace')

        print(f'Arquivo {file} salvo como tabela {table_name} no banco de dados')

# fecha a conexão com o banco de dados
connection.close()

print('Todos os arquivos foram salvos no banco de dados')

#================ Formular duas novas tabelas do banco =================

analitico_titulos = """
CREATE TABLE IF NOT EXISTS analitico_titulos AS
WITH participantes AS (
    SELECT
        tconst,
        COUNT(DISTINCT nconst) as qtdParticipantes
        
    FROM title_principals
    
    GROUP BY tconst
)
SELECT 
    tb.tconst,
    tb.titleType,
    tb.originalTitle,
    tb.startYear,
    tb.endYear,
    tb.genres,
    tr.averageRating,
    tr.numVotes,
    p.qtdParticipantes
    
FROM title_basics as tb

LEFT JOIN title_ratings as tr
    ON tr.tconst = tb.tconst
    
LEFT JOIN participantes as p
    ON p.tconst = tb.tconst
"""

analitico_participantes = """
CREATE TABLE IF NOT EXISTS analitico_participantes AS

SELECT
    tp.nconst,
    tp.tconst,
    tp.ordering,
    tp.category,
    tb.genres

FROM title_principals as tp

LEFT JOIN title_basics as tb
    ON tp.tconst = tb.tconst
"""

#================ Salvando novas tabelas em banco de dados com SQLite =================

queries = [analitico_titulos, analitico_participantes]

for query in queries:
    
    connection = sqlite3.connect(data_base)

    connection.execute(query)

    connection.close()

    print('Tabela Criada com sucesso!')