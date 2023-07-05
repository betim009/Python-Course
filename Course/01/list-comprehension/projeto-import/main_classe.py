from data import data


class FiltroPacientes:
    def __init__(self):
        self.pacientes = []
        self.internacoes = []

    def executar(self):
        print(self.pacientes)


filtro = FiltroPacientes()
filtro.executar()
