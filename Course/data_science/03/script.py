import csv
from tabulate import tabulate


# Resgata todos os dados
def get_all():
    with open("data.csv", encoding="utf-8") as file:
        data_reader = csv.reader(file, delimiter=",", quotechar='"')

        header, *data = data_reader

        table = []
        for row in data:
            produto = row[0]  # Nome do produto na coluna 0
            tipo = row[1]
            sabor = row[2]
            intensidade = row[3]
            table.append(
                [produto, tipo, sabor, intensidade]
            )  # Uma lista com todos os valores da linha

        headers = header
        table_style = 'grid'

        print(tabulate(table, headers, tablefmt=table_style))


def get_produtc_intensity():
    with open("data.csv", encoding="utf-8") as file:
        data_reader = csv.reader(file, delimiter=",", quotechar='"')

        header, *data = data_reader

        table = []
        for row in data:
            produto = row[0]
            intensidade = row[3]
            table.append([produto, intensidade])

        headers = header[0], header[3]
        table_style = "grid"

        print(tabulate(table, headers, tablefmt=table_style))


def create_product():
    produto = input("Digite o nome do produto: ")
    tipo = input("Digite o tipo do produto: ")
    sabor = input("Digite o sabor do produto: ")
    intensidade = input("Digite a intensidade do produto: ")

    new_product = [produto, tipo, sabor, intensidade]

    # Abre o arquivo CSV no modo de append ('a')
    with open("data.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Adiciona as informações do novo produto ao arquivo CSV
        writer.writerow(new_product)

    print("Produto adicionado com sucesso!")


# Loop de menu
while True:
    print("Menu:")
    print("1. Listar todos os produtos")
    print("2. Listar produtos por intensidade")
    print("3. Adicionar um novo produto")
    print("4. Sair")

    choice = input("Digite o número da opção desejada: ")

    if choice == "1":
        get_all()
    elif choice == "2":
        get_produtc_intensity()
    elif choice == "3":
        create_product()
    elif choice == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
