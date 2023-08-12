from selenium import webdriver
import time
import pyautogui

# Criação de uma instância de navegador utilizando o Chrome
chrome = webdriver.Chrome()

# Requisições para essa instância criada utilizando o método `get`
chrome.get("https://web.whatsapp.com/")
time.sleep(
    25
)  # Vamos esperar alguns segundos para que o usuário possa escanear o código QR

contatos = ["Jairo", "Lembretes"]
msg = "Olá, esse é um teste de mensagem automatizada. =)"


def buscar_contato(contato):
    # Clicar no campo de pesquisa
    campo_pesquisa = chrome.find_element(
        by="xpath", value="//div[@contenteditable='true']"
    )
    campo_pesquisa.click()
    time.sleep(1)

    # Digitar o nome do contato
    campo_pesquisa.send_keys(contato)
    time.sleep(1)

    # Selecionar o contato da lista de resultados
    resultado_contato = chrome.find_element(
        by="xpath", value=f"//span[@title='{contato}']"
    )
    resultado_contato.click()
    time.sleep(5)


def enviar_mensagem(mensagem):
    # Aguardar um curto período para garantir que o campo de mensagem esteja carregado
    time.sleep(5)

    try:
        # Simular a digitação da mensagem e pressionar Enter usando pyautogui
        pyautogui.write(mensagem)
        pyautogui.press("enter")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(msg)

time.sleep(10)
# Fechar o navegador ao final
chrome.quit()
