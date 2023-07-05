# dados de uma clinica
data = [
    {"paciente": "Antonio", "internacoes": 2},
    {"paciente": "Luiz Daniel", "internacoes": 1},
    {"paciente": "Carlos Henrrique", "internacoes": 1},
]

new_data = [
    paciente['paciente']
    for paciente in data if paciente['internacoes'] > 1
]

print(new_data)
