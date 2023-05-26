# Projeto: Calculadora de IMC
# Agora vamos criar um projeto simples utilizando inputs: uma calculadora
# de Índice de Massa Corporal (IMC). O IMC é uma medida utilizada para avaliar
# se uma pessoa está abaixo do peso, peso normal, com sobrepeso ou obesa.

# Vamos criar um programa que solicita ao usuário seu peso em quilogramas e
# sua altura em metros, e então calcula e exibe o IMC.

# É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura**2)

print("Seu IMC é: ", imc)


# Tabela do IMC
# Entre 18,5 e 24,9	= Normal
# Entre 25,0 e 29,9	= Sobrepeso
# Entre 30,0 e 39,9 =	Obesidade
# Maior que 40,0	= Obesidade


if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal.")
elif imc >= 24.9 and imc < 30:
    print("Sobrepeso.")
else:
    print("Obsidade.")
