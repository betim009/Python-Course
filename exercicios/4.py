pecas = []

# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    print('Você selecionou a opção de cadastrar peça')
    print('Código da peça: {}'.format(codigo))
    nome = input('Por favor, entre com o NOME da peça: ')
    fabricante = input('Por favor, entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor, entre com o VALOR (R$) da peça: '))
    dicionarioCadastro = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}
    pecas.append(dicionarioCadastro.copy())
    dicionarioCadastro.clear()

# Função para consultar peças
def consultarPeca():
    while True:
        print('Você selecionou a opção de consultar peças')
        opConsultar = int(input('Escolha a opção desejada:\n1 - Consultar Todas as Peças\n2 - Consultar Peças por Código\n'
                                '3 - Consultar Peças por Fabricante\n4 - Retornar\n>> '))

        if opConsultar == 1:
            print('--------------------')
            for registro in pecas:
                for key, value in registro.items():
                    print('{} : {}'.format(key, value))
                print('--------------------')

        elif opConsultar == 2:
            entrada = int(input('Digite o CÓDIGO da Peça: '))
            print('--------------------')
            for registro in pecas:
                if registro['codigo'] == entrada:
                    for key, value in registro.items():
                        print('{} : {}'.format(key, value))
                    print('--------------------')

        elif opConsultar == 3:
            entrada = input('Digite o FABRICANTE da Peça: ')
            print('--------------------')
            for registro in pecas:
                if registro['fabricante'] == entrada:
                    for key, value in registro.items():
                        print('{} : {}'.format(key, value))
                    print('--------------------')

        elif opConsultar == 4:
            break

# Função para remover uma peça
def removePeca():
    print('Você selecionou remover peça')
    entrada = int(input('Digite o código da peça a ser removida: '))
    for registro in pecas:
        if registro['codigo'] == entrada:
            pecas.remove(registro)

# Função principal
print('Bem-vindo ao Controle de Estoque da Bicicletaria do seu nome')
registroPeca = 0

while True:
    opcao = int(input('Escolha a opção desejada:\n1 - Cadastrar Peças\n2 - Consultar Peças\n3 - Remover Peças\n4 - Sair\n>> '))

    if opcao == 1:
        registroPeca += 1
        cadastrarPeca(registroPeca)

    elif opcao == 2:
        consultarPeca()

    elif opcao == 3:
        removePeca()

    elif opcao == 4:
        print('Sair')
        break
