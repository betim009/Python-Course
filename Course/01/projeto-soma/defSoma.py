def soma(n, n2):
    if (type(n) == int and type(n2) == int):
        r = n + n2
        print(f"Resultado: {r}")
    else:
        print("Insira dados com o formato int!")


soma(10, 20)
soma('10', 20)
