# list comprehension / Compreensão de lista:

restaurantes = [
    {"name": "restaurante 1", "nota": 4},
    {"name": "restaurante 2", "nota": 4.6},
    {"name": "restaurante 3", "nota": 2.9},
]

nota_min = 3

new_restaurante = [
    restaurante
    for restaurante in restaurantes
    if restaurante["nota"] > nota_min
]

print(new_restaurante)


# lista de nomes:
lista_de_nomes = ['Dudu', "Zeca", "Tadeu", "Vini"]

# retira Dudu da lista
nova_lista = [
    name
    for name in lista_de_nomes
    if 'Dudu' not in name
]

print(nova_lista)
