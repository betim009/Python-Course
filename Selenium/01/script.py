# importação do webdriver, que é o que possibilita a implementação para todos
# os principais navegadores da web
# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# criação de uma instância de navegador utilizando o Firefox
chrome = webdriver.Chrome()

# requisições para essa instância criada utilizando o método `get`
response = chrome.get("https://www.google.com.br")

# pesquisa na instância aberta do navegador pela primeira ocorrência
# do nome 'q'
search_input = chrome.find_element("name", "q")

# escreve selenium dentro do campo de pesquisa
search_input.send_keys("Vitor Pereira")

# # pressiona enter para realizar a busca
search_input.send_keys(Keys.ENTER)
