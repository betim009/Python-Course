# Um conjunto ou set pode ser inicializado utilizando-se também o método set()
conjunto = set()
# print(conjunto)

# Dicionários:
people_by_id = {
    1: "Maria",
    2: "Fernanda",
    3: "Felipe",
}  # elementos no formato "chave: valor" separados por vírgula,
# envolvidos por chaves

people_by_name = {
    "Maria": 1,
    "Fernanda": 2,
    "Felipe": 3,
}  # outro exemplo, dessa vez usando strings como chaves.
# As aspas são necessárias para que o Python não ache que `Maria`,
# `Fernanda` e `Felipe` sejam variáveis.

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Maria

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(2, "Fernanda"), (3, "Felipe")])
# é retornada uma coleção iterável de tuplas contendo chaves e valores
