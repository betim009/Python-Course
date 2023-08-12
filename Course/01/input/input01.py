# A função input() em Python permite que você obtenha entrada de dados do
# usuário através do teclado.

nome = input("Digite o seu nome: ")
# print(nome)

idade = int(input("Digite idade: "))
peso = float(input("Digite seu peso: "))
# print(idade, peso)

print(
    f"""
Nome: {nome}.
Idade: {idade}.
Peso: {peso}."""
)
