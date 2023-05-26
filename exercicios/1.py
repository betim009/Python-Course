def dimensoesObjeto():
    while True:
        try:
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            altura = float(input("Digite a altura do objeto (em cm): "))
            volume = comprimento * largura * altura
            print("O volume do objeto é (em cm³): {}".format(volume))
            if volume < 1000:
                return 10
            elif 1000 <= volume < 10000:
                return 20
            elif 10000 <= volume < 30000:
                return 30
            elif 30000 <= volume < 100000:
                return 50
            else:
                print("Não aceitamos objetos com dimensões tão grandes")
                print("Entre com as dimensões desejadas novamente")
                continue
        except ValueError:
            print("Você digitou alguma dimensão do objeto com valor não numérico")
            print("Por favor, entre com as dimensões desejadas novamente")
            continue


def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em Kg): "))
            if peso <= 0.1:
                return 1
            elif 0.1 < peso <= 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            elif peso > 30:
                print("Não aceitamos objetos tão pesados")
                print("Entre com o peso novamente")
                continue
            else:
                print("Entre com o peso desejado novamente")
                continue
        except ValueError:
            print("Você digitou o peso do objeto com valor não numérico")
            print("Por favor, entre com o peso desejado novamente")
            continue


def rotaObjeto():
    while True:
        rota = input(
            "Selecione a rota:\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo até Rio de Janeiro\n"
            "BS - De Brasília até São Paulo\nSB - De São Paulo para Brasília\nBR - De Brasília até Rio de Janeiro\n"
            "RB - De Rio de Janeiro até Brasília\n>> "
        )
        if rota == "RS" or rota == "SR":
            return 1
        elif rota == "BS" or rota == "SB":
            return 1.2
        elif rota == "BR" or rota == "RB":
            return 1.5
        else:
            print("Você digitou uma rota que não existe")
            print("Por favor, entre com a rota desejada novamente")
            continue


print("Bem-Vindo à Companhia de Logística seu nome S.A.")
tamanho = dimensoesObjeto()
peso = pesoObjeto()
trajeto = rotaObjeto()
total = tamanho * peso * trajeto  # Cálculo do valor total a ser pago
print(
    "O valor total é: R${:.2f}\n(Dimensões: {:.2f} * Peso: {:.2f} * Rota: {:.2f})".format(
        total, tamanho, peso, trajeto
    )
)
