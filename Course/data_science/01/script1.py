# Tópico 3: Estruturas de Controle
# Exemplo de estrutura condicional (if-elif-else)
# para verificar a idade de uma pessoa.
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é adulto(a).")
else:
    print("Você é um(a) idoso(a).")

# Exemplo de loop (for) para imprimir os números de 1 a 5.
for i in range(1, 6):
    print(i)

# Exemplo de loop (while) para imprimir os números de 1 a 5.
num = 1
while num <= 5:
    print(num)
    num += 1
