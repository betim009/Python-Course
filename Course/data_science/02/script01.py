# Sem dúvidas, análise de dados é o que se destaca
# quando estamos falando sobre manipular arquivos CSV

# Vamos analisar uma base de dados a respeito dos cursos de graduação
# oferecidos pela Universidade de Brasília (UnB).
# O arquivo utilizado é o graduacao_unb.csv.

# O módulo csv, contém duas principais funções:

# Um leitor (reader) que nos ajuda a ler o conteúdo,
# já fazendo as transformações dos valores para Python;

# E um escritor (writer) para facilitar a escrita nesse formato.

import csv

with open("graduacao_unb.csv", encoding="utf-8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader


# Saídas:
# print(header)  # Cabeçalhos
# print(data)  # Array de arrays
# print(data[0])  # Primeiro elemento do array
print(data[0][15])  # Acessando informação dentro do array
