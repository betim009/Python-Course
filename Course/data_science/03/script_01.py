import csv
from tabulate import tabulate


def get_all():
    with open("data.csv", encoding="utf-8") as file:
        data_reader = csv.reader(file, delimiter=",", quotechar='"')

        header, *data = data_reader
        return header, data


def show_all():
    header, data = get_all()
    print(tabulate(data, headers=header))


def show_intensity():
    header, data = get_all()

    new_table = []
    for row in data:
        produto = row[0]
        intensity = row[3]
        new_table.append([produto, intensity])

    table_style = 'grid'

    print(tabulate(new_table, header, tablefmt=table_style))


# PRINT:
show_intensity()
