course = ["Introdução", "Front-end", "Back-end"]

# Adicione o elemento “Ciência da Computação” à lista.

course.append("Ciência da Computação")

# Acesse e altere o primeiro elemento da lista para “Fundamentos”.
course[0] = "Fundamentos"
print(course)


# Tuplas
user = (
    "Will",
    "Marcondes",
    42,
)  # elementos são definidos separados por vírgula, envolvidos por parênteses

user[0]  # acesso também por índices
# user[0] = "Alberto"  # erroru

# Conjuntos (set)
permissions = {
    "member",
    "group",
}  # elementos separados por vírgula, envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto

permissions.add(
    "member"
)  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

permissions.union({"user"})  # retorna um conjunto resultado da união

permissions.intersection(
    {"user", "member"}
)  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos
