import requests

# endpoint
url = "https://api.mercadolibre.com/sites/MLB/search?q=computador"

response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Converte a resposta para JSON
    data = response.json()

    # Acesse os resultados
    results = data["results"][0]
    print(results)

else:
    print(f"A requisição falhou com o código de status {response.status_code}")


if response.status_code == 200:
    # Converte a resposta para JSON
    data = response.json()

    # Acesse os resultados
    results = data["results"][0]
    print(results)

else:
    print(f"A requisição falhou com o código de status {response.status_code}")
