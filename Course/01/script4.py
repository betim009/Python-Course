# 0. Um conjunto ou set pode ser inicializado
# utilizando-se também o método set():
conjunto = set()
# print(conjunto)
# print(type(conjunto))


# 1. Dicionarios / Dics
# Estrutura:
dic = {}  # Dicionario vazio
print(type(dic))


# dicionario data com nome e idade
data = {
    "Alberto": 27,
    "Paulo Victor": 27,
    "Brenda": 27,
    "Ricardo": 21,
}

# saida pela chave nome
print(data["Alberto"])  # 27

# dicionario id e nome
data_1 = {
    1: "Alberto",
    2: "Paulo Victor",
    3: "Brenda",
    4: "Ricardo",
}

# saida pela chave id:
print(data_1[4])

# alterando pelo id:
data_1[1] = "Denis"
print(data_1)

# removendo:
del data_1[1]
print(data_1)

# listando indices:
print(data_1.items())
print(data.items())

# listando resultados:
print(data.values())
print(data_1.values())

# add elemento:
data["João"] = 35
print(data)

# tamanho len():
print(len(data))

# Faça:
# calcule a média das idades de data:
print(list)

idades = list(data.values())
print(idades)
media = sum(idades) // len(idades)
print(media)


lista_usrs = [
    {"id": 1, "Usr": "alberto", "idade": 27},
    {"id": 2, "Usr": "brenda", "idade": 26},
    {"id": 3, "Usr": "paulo victor", "idade": 25},
]

print(lista_usrs[0]["id"])

print("id Nome")
for usr in lista_usrs:
    print(f"{usr['id']}  {usr['Usr']}")
