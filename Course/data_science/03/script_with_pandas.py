import csv
import pandas as pd
from tabulate import tabulate


# Função para listar todos os produtos
def list_all():
    data = pd.read_csv("data_2.csv")
    print(tabulate(data, headers="keys", tablefmt="grid"))


# Função para listar produtos por intensidade
def list_by_intensity():
    data = pd.read_csv("data_2.csv")
    intensity_data = data[["produto", "intensidade"]]
    print(tabulate(intensity_data, headers="keys", tablefmt="grid"))


# Função para adicionar um novo produto
def add_product():
    produto = input("Digite o nome do produto: ")
    tipo = input("Digite o tipo do produto: ")
    sabor = input("Digite o sabor do produto: ")
    intensidade = int(
        input("Digite a intensidade do produto: ")
    )  # Convertendo para inteiro

    with open("data_2.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow([produto, tipo, sabor, intensidade])

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
        list_all()
    elif choice == "2":
        list_by_intensity()
    elif choice == "3":
        add_product()
    elif choice == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
