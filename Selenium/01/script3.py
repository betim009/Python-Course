import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Criação de uma instância do navegador Chrome
chrome = webdriver.Chrome()

# Navegação para o site do Google
chrome.get("https://www.google.com.br")

# Localização do campo de pesquisa pelo atributo "name"
search_input = chrome.find_element("name", "q")

# Preenchimento do campo de pesquisa
search_input.send_keys("Vitor Pereira")

# Pressionar a tecla Enter para realizar a busca
search_input.send_keys(Keys.ENTER)

# Esperar alguns segundos para os resultados serem carregados
chrome.implicitly_wait(5)

# Coletar os elementos <h3> dos resultados da pesquisa
search_results = chrome.find_elements("css selector", "div.g h3")

# Exibir os textos dos 3 primeiros elementos <h3>
for result in search_results[:3]:
    print(result.text)

# Pausa por 10 segundos para visualização
time.sleep(10)

# Fechar o navegador
chrome.quit()
