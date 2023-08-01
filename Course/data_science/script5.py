# Trabalhando com Dicionários e CSV:

# Podemos usar o formato de dicionários para representar os dados
# em um arquivo CSV, onde as chaves do dicionário correspondem
# aos nomes das colunas. Isso torna a manipulação dos dados mais intuitiva.

import csv

# Dados a serem escritos no arquivo CSV usando dicionários
dados = [
    {"Nome": "Pedro", "Idade": 28, "Cidade": "Salvador"},
    {"Nome": "Ana", "Idade": 35, "Cidade": "Curitiba"},
    {"Nome": "Mariana", "Idade": 19, "Cidade": "Fortaleza"},
]

# Abre o arquivo CSV em modo de escrita
with open("dados_dict.csv", "w", newline="") as arquivo_csv:
    # Define o cabeçalho do arquivo com base nas chaves do dicionário
    campos = ["Nome", "Idade", "Cidade"]
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)

    # Escreve o cabeçalho no arquivo
    escritor_csv.writeheader()

    # Escreve os dados na forma de linhas no arquivo CSV
    for linha in dados:
        escritor_csv.writerow(linha)
