from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome()
response = chrome.get("https://www.google.com.br")
search_input = chrome.find_element("name", "q")
search_input.send_keys("Vitor Pereira")
search_input.send_keys(Keys.ENTER)

# Pausa de 5 segundos para visualizar o resultado
time.sleep(5)

chrome.quit()
