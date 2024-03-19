import pandas as pd

imoveis = [
    {
        "id": 1,
        "nome": "576",
        "titulo": "SALÃO COMERCIAL COM 373 M² DE ÁREA ÚTIL NO RUDGE RAMOS, SÃO BERNARDO DO CAMPO",
        "tipo": "comercial",
        "transação": "locaçao",
        "valor": 12800.00,
        "categoria": "galpao/deposito/armazem",
        "permalink": "https://canalpro.grupozap.com/ZAP_OLX/0/listings/update/2696125882",
        "endereço": "Avennomea Winston Churchill, 909 - Rudge Ramos, São Bernardo do Campo - SP",
        "quartos": {
                "quantidade": 0,
                "dormitorio": 0,
                "suite": 0,
            },
        "banheiros": {
            "quantidade": 3,
            "com_banheiro": 2,
            "sem_banheiro": 1
            },
        "vaga de garagem": 3,
    },
    {
        "id": 2,
        "nome": "575",
        "titulo": "Imóvel com 8 Quartos e 6 banheiros para Alugar, 287 m² por R$ 8.500/Mês",
        "tipo": "comercial",
        "transação": "locaçao",
        "valor": 8500.00,
        "categoria": "casa sobrado",
        "permalink": "https://www.vivareal.com.br/imovel/8-quartos-jardim-do-mar-bairros-sao-bernardo-do-campo-com-garagem-287m2-aluguel-RS8500-nome-2694769685/",
        "endereço": "Rua Continental - Jardim do Mar, São Bernardo do Campo - SP",
        "quartos": {
                "quantidade": 8,
                "dormitorio": 0,
                "suite": 0,
            },
        "banheiros": {
            "quantidade": 6,
            "com_banheiro": 0,
            "sem_banheiro": 0
            },
        "vagas de garagem": "2",
    },
    {
        "id": 3,
        "nome": "574",
        "titulo": "Sala/Conjunto - 70 m² no Bairro Jardim do Mar, São Bernardo do Campo-SP",
        "tipo": "comercial",
        "transação": "locaçao",
        "valor": 1900.00,
        "categoria": "sala/escritorio",
        "permalink": "https://www.vivareal.com.br/imovel/sala-comercial-jardim-do-mar-bairros-sao-bernardo-do-campo-70m2-aluguel-RS1900-nome-2694171724/",
        "endereço": "Rua Banda, 428 - Jardim do Mar, São Bernardo do Campo - SP",
        "quartos": {
                "quantidade": 0,
                "dormitorio": 0,
                "suite": 0,
            },
        "banheiros": {
            "quantidade": 1,
            "com_banheiro": 0,
            "sem_banheiro": 0
            },
        "vaga de garagem": 0,
    },
    {
        "id": 4,
        "nome": "573",
        "titulo": "Lindo apto. 127 m², 3 dormitórios no Jardim Chácara Inglesa, em São Bernardo do Campo",
        "tipo": "resnomeencial",
        "transação": "locaçao",
        "valor": 3100,
        "categoria": "apartamento",
        "permalink": "https://www.vivareal.com.br/imovel/apartamento-3-quartos-jardim-chacara-inglesa-bairros-sao-bernardo-do-campo-com-garagem-127m2-aluguel-RS3100-nome-2692447912/",
        "endereço": "Rua Myriam Dora Rossi, 70 - Jardim Chacara Inglesa, São Bernardo do Campo, SP",
        "quartos": {
                "quantidade": 3,
                "dormitorio": 2,
                "suite": 1,
            },
        "banheiros": {
            "quantidade": 1,
            "com_banheiro": 0,
            "sem_banheiro": 0
            },
        "vaga de garagem": 1,
    },
]


def get_imovel_valor(number):
    results = []
    for element in imoveis:
        if element['valor'] >= number:
            results.append({
                "NOME": element['nome'],
                "CATEGORIA": element['categoria'], 
                "LINK": element['permalink']
                })
    
    return pd.DataFrame(results)
            
            
print(get_imovel_valor(1000))
