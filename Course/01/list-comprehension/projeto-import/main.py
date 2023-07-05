from data import data


def filtro_paciente_int():
    new_data = [
        paciente['internacoes']
        for paciente in data
        if paciente["internacoes"] > 1]
    return new_data


def filtro_paciente_paciente():
    new_data = [
        paciente['paciente']
        for paciente in data
        if paciente["internacoes"] > 1]
    return new_data


def main():
    paciente = filtro_paciente_paciente()
    qtd = filtro_paciente_int()

    stop = len(paciente)
    start = 0

    print(stop)

    while start < stop:
        print(f'{paciente[start]} {qtd[start]}')
        start += 1


main()
