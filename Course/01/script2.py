# Tipos de dados
a = 10
b = 10.5
c = "10"

print("Tipos dos dados:")
print(type(a))  # Exibe o tipo de dado da variável 'a'
print(type(b))  # Exibe o tipo de dado da variável 'b'
print(type(c))  # Exibe o tipo de dado da variável 'c'
print(type(a == b))  # Exibe o tipo da condição 'a == b'

print("\n")
# Arrays / Listas
print("Arrays:")
fruits = ["laranja", "maçã", "uva", "abacaxi"]  # Lista de frutas

print(fruits[0])  # Acessando a primeira fruta da lista
print(fruits[-1])  # Acessando a última fruta da lista

fruits.append("banana")  # Adicionando uma nova fruta
print(fruits)  # Exibindo a lista atualizada

fruits.remove("abacaxi")  # Removendo uma fruta
print(fruits)  # Exibindo a lista atualizada

new_fruits = ["pera", "melão", "kiwi"]
fruits.extend(new_fruits)  # Acrescentando uma lista de frutas à lista original
print(fruits)  # Exibindo a lista atualizada

index = fruits.index("maçã")  # Obtendo o índice onde a fruta está localizada
print(index)

fruits.sort()  # Ordenando a lista de frutas em ordem alfabética
print(fruits)  # Exibindo a lista atualizada

print("\n")

# Saída com o print(f"{}"):
estados = ["SP", "ES", "MG", "RJ"]  # Lista de Estados

print(f"Exebindo os Estados: {estados}")
print(f"A posição pelo index [1]: {estados[1]}")
print(f"Adicionando um novo estado 'MA': {estados.append('MA')}")
print(f"Exibindo todos os estados atualizados {estados}")
print(f"Exibe tipo de estados: {type(estados)}")
