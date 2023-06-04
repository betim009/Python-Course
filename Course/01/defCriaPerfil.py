lista_de_perfil = []


def valida_perfil(perfil):
    campos_obrigatorios = ["id", "nome", "idade"]

    if not isinstance(perfil, dict):
        return False

    for campo in campos_obrigatorios:
        if campo not in perfil:
            return False

        valor = perfil[campo]

        if campo == "id" and not isinstance(valor, int):
            return False
        elif campo == "nome" and not isinstance(valor, str):
            return False
        elif campo == "idade" and not isinstance(valor, int):
            return False

    return True


def cria_perfil(perfil):
    if valida_perfil(perfil):
        lista_de_perfil.append(perfil)
        return lista_de_perfil
    else:
        print("O perfil é inválido. Certifique-se de que seja um dicionário.")
        print("Com os campos 'id', 'nome' e 'idade' corretos. \n")


def exibe_todos():
    return lista_de_perfil


def exibe_id(id):
    if id > len(lista_de_perfil):
        return "Não é possível econtrar perfil com esse id"
    else:
        for perfil in lista_de_perfil:
            if perfil["id"] == id:
                return perfil["nome"]


# Inválido, não é um dicionário
error = cria_perfil(4)
# Inválido, os campos "id" e "idade" devem ser números
brenda = cria_perfil({"id": "3", "nome": "brenda", "idade": "21"})

alberto = cria_perfil({"id": 1, "nome": "alberto", "idade": 27})  # Válido
ricardo = cria_perfil({"id": 2, "nome": "ricardo", "idade": 29})  # Válido


print(exibe_todos())
print(exibe_id(4))
