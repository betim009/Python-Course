# CSV

# Claro! CSV (Comma-Separated Values) é um formato de arquivo amplamente
# utilizado para armazenar dados tabulares, onde cada linha do arquivo
# representa uma linha da tabela e os valores são separados por vírgulas
# (ou outro delimitador). Python possui bibliotecas nativas que facilitam
# a leitura, escrita e manipulação de arquivos CSV.
# Vamos explorar como trabalhar com CSV em Python:

import csv

# Abre o arquivo CSV em modo de leitura
with open("./data/dados.csv", "r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)  # Cria o objeto leitor_csv

    # Percorre as linhas do arquivo CSV e exibe os dados
    for linha in leitor_csv:
        nome, idade, cidade = linha  # Desestruturação da linha
        print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")


# Dados a serem escritos no arquivo CSV
dados = [
    ["Pedro", 28, "Salvador"],
    ["Ana", 35, "Curitiba"],
    ["Mariana", 19, "Fortaleza"],
]

# Abre o arquivo CSV em modo de escrita
with open("novo_dados.csv", "w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)  # Cria o objeto escritor_csv

    # Escreve os dados na forma de linhas no arquivo CSV
    for linha in dados:
        escritor_csv.writerow(linha)
