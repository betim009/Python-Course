# For:

restaurantes = [
    {"name": "restaurante 1", "nota": 4},
    {"name": "restaurante 2", "nota": 4.6},
    {"name": "restaurante 3", "nota": 2.9},
]

# exibindo nome do primeiro restaurante:
print(restaurantes[0]["name"])

# exibir apenas restaurantes com a nota maior que 3
new_rest = []
nota_min = 3.0

for restaurante in restaurantes:
    if restaurante["nota"] > nota_min:
        new_rest.append(restaurante)

print(new_rest)
