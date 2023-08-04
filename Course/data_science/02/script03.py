import csv

with open("graduacao_unb.csv", encoding="utf-8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader


# new
group_by_department = []
for row in data:
    # departament
    departament = row[15]
    if departament not in group_by_department:
        group_by_department.append(departament)


# saidas:
print(group_by_department)
