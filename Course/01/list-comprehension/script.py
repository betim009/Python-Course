# list comprehension / Compreensão de lista:
restaurantes = [
    {"name": "restaurante 1", "nota": 4},
    {"name": "restaurante 2", "nota": 4.6},
    {"name": "restaurante 3", "nota": 2.9},
]

nota_min = 3  # Filtro
# criando um novo restaurante com nota > 3:
new_restaurante = [
    restaurante
    # restaurante['name'] retorna o valor da chave name
    for restaurante in restaurantes
    if restaurante["nota"] > nota_min
]

print(new_restaurante)
