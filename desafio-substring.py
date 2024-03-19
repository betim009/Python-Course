def ex1(int_seq, subtotal):
    # Converte a sequência de números em uma lista de inteiros
    int_seq = list(map(int, int_seq.split(",")))
    substrings = []  # Inicializa uma lista vazia para armazenar as substrings
    n = len(int_seq)  # Obtém o comprimento da lista de inteiros

    for i in range(n):  # Loop externo para começar a partir de cada posição na lista
        current_sum = 0  # Inicializa a soma atual
        substring = []  # Inicializa uma lista vazia para armazenar a substring
        for j in range(i, n):
            print('valor de j', j)  # Loop interno para percorrer as posições a partir de i
            current_sum += int_seq[j]  # Adiciona o elemento atual à soma
            substring.append(int_seq[j])  # Adiciona o elemento atual à substring
            if current_sum == subtotal:  # Se a soma atual for igual ao subtotal
                substrings.append(substring[:])
                print(
                    "adicionando:", substring[:]
                )  # Adiciona uma cópia da substring à lista
            elif current_sum > subtotal:  # Se a soma atual for maior que o subtotal
                break  # Sai do loop interno

    return substrings  # Retorna a lista de substrings cuja soma é igual ao subtotal


int_seq = "3,0,4,0,3,1,0,1,0,0,5,0,4,2"
subtotal = 9
substrings = ex1(int_seq, subtotal)
print((substrings))
