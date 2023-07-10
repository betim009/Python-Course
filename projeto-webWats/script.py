# importar bibliotecas necesserias
import pywhatkit
import keyboard
import time
from datetime import datetime

# 2. Definir para quais contatos iremos enviar as mensagens
contatos = ["+5561991259875", "+5561991259875"]

# 3. Definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(
        contatos[0],
        "VAMOS AUTOMATIZAR TUDO!",
        datetime.now().hour,
        datetime.now().minute + 2,
    )
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release("ctrl + w")
