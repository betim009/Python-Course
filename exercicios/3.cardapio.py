total = 0  # Muito importante o zero no início
start = 0

print("Bem vindo à Lanchonete")
print(
    """Cardápio:
| Código | Descrição             | Valor |
| 100    | Cachorro-quente       | 9,00  |
| 101    | Cachorro-quente Duplo | 11,00 |
| 102    | X-Egg                 | 12,00 |
| 103    | X-Salada              | 13,00 |
| 104    | X-Bacon               | 14,00 |
| 105    | X-Tudo                | 17,00 |
| 200    | Refrigerante Lata     | 5,00  |
| 201    | Chá Gelado            | 4,00  |
"""
)

while start == 0:
    codigo = input(
        "Entre com o código desejado: "
    )  # Onde será inserido o código dos pedidos

    if codigo == "100":
        total = total + 9  # O total guarda o valor final dos pedidos
        print("Você pediu um Cachorro-Quente no valor de 9,00")
    elif codigo == "101":
        total = total + 11
        print("Você pediu um Cachorro-quente Duplo no valor de 11,00")
    elif codigo == "102":
        total = total + 12
        print("Você pediu um X-Egg no valor de 12,00")
    elif codigo == "103":
        total = total + 13
        print("Você pediu um X-Salada no valor de 13,00")
    elif codigo == "104":
        total = total + 14
        print("Você pediu um X-Bacon no valor de 14,00")
    elif codigo == "105":
        total = total + 17
        print("Você pediu um X-Tudo no valor de 17,00")
    elif codigo == "200":
        total = total + 5
        print("Você pediu um Refrigerante Lata no valor de 5,00")
    elif codigo == "201":
        total = total + 4
        print("Você pediu um Chá Gelado no valor de 4,00")
    else:  # Caso o cliente digite o código errado, entra nesse else
        print("Opção Inválida")
        continue

    resposta = input("Deseja pedir mais alguma coisa?\n1 - SIM\n0 - Não\n>>")

    if (
        resposta == "1"
    ):  # Quando o código é digitado corretamente, ele continua com o pedido
        continue
    else:  # Caso o cliente não queira mais pedidos, cai nesse else encerrando
        # a conta
        print("O total a ser pago é: {:.2f}".format(total))
        break
