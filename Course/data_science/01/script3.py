# Tópico 5: Listas e Loops

# Exemplo de lista de números.
numeros = [1, 2, 3, 4, 5]

# Exemplo de loop (for) para percorrer a lista e exibir os elementos.
for numero in numeros:
    print(numero)

# Exemplo de lista vazia e loop (while) para adicionar elementos a ela.
nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)

print("Lista de nomes:", nomes)
