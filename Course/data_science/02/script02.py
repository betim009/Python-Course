import csv

with open("mangas.csv", encoding="utf-8") as file:
    mangas_reader = csv.reader(file, delimiter=",", quotechar='"')
    # header, *data = mangas_reader
    for manga in mangas_reader:
        print(manga)

# Saídas:
# print(data)

# for manga in data:
#     print(manga)
