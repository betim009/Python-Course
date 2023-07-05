from data import data


class FiltroPacientes:
    def __init__(self):
        # Inicialização dos atributos vazios
        self.pacientes = []
        self.internacoes = []
        self.qtd = 0

    # método executar
    def executar(self):
        # Filtrando os pacientes com mais de uma internação
        # retornando nome do paciente
        self.pacientes = [
            paciente["paciente"]
            for paciente in data if
            paciente["internacoes"] > 1
        ]

        # Filtrando os pacientes com mais de uma internação
        # retornando internacoes do paciente
        self.internacoes = [
            paciente["internacoes"]
            for paciente in data
            if paciente["internacoes"] > 1
        ]

        # Armazenando a quantidade total de pacientes filtrados
        self.qtd = len(self.pacientes)

    # método exibir
    def exibir(self):
        start = 0
        while start < self.qtd:
            print(f"{self.pacientes[start]} {self.internacoes[start]}")
            start += 1


# Criando uma instância da classe FiltroPacientes
filtro = FiltroPacientes()

# Executando o filtro e armazenando os resultados nos atributos da instância
filtro.executar()

# Exibindo os resultados
filtro.exibir()
