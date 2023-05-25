# Faça: 1. Adicione o elemento “Ciência da Computação” à lista.
cursos = ["Introdução", "Front-end", "Back-end"]

# 1:
cursos.append("Ciência da Computação")

# Faça: 2. Acesse e altere o primeiro elemento da lista para “Fundamentos”.

# 2:
cursos[0] = "Fundamentos"
# print(cursos)


# 3. Tuplas:
# envolvidos por parênteses:
user = ("Denis", "Daniel", "Carlos")

# acesso também por índices
user[0]

# não aceita alterar:
# user[0] = "Alberto"

# 3.1 Criando uma nova tupla:
# Cria um novo dado
new_user_1 = "Alberto"

# E cria uma nova tupla, e addiciona o novo dado:
user_1 = user + (new_user_1,)
# print(user_1)

# 4. Conjuntos (set):
# Declarando o conjunto games:
games = {"Tibia", "Cs Go", "League of Legends"}

# Add um novo elemento ao conjunto:
games.add("Minecraft")
games.add("Tibia")  # Não é possível add um elemento que já existe

# Exibe conjunto atualizado:
print(f"Conjuto Games: {games}")

# Cria um novo conjunto, copia os dados de games
# e add Dark Souls
new_games = games.union({"Dark Souls"})
print(f"Conjunto new_games: {new_games}")


# Cria um novo conjunto, só com Tibia e Cs Go
tibia_cs_go = new_games.intersection({"Tibia", "Cs Go"})
print(f"Conjunto tibia_cs_go: {tibia_cs_go}")

# Diferença entre conjuntos
diff = games.difference(tibia_cs_go)
print(f"diff: {diff}")
