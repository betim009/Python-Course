def soma(n1, n2):
    # validacoes se nums são inteiros
    if (type(n1) == int and type(n2) == int):
        r = n1 + n2
        print(f"Resultado: {r}")
    else:
        print("Insira dados com o formato int!")


soma(10, 20)
soma('10', 20)
