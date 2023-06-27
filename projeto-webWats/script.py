import pywhatkit
import keyboard
import time
from datetime import datetime

# Definir o identificador único do grupo
grupo = "Lembretes"  # Substitua pelo nome único do grupo

# Definir o intervalo de envio
while True:
    # Enviar mensagem para o grupo
    pywhatkit.sendwhatmsg_to_group(
        grupo,
        "VAMOS AUTOMATIZAR TUDO!",
        datetime.now().hour,
        datetime.now().minute + 2,
    )

    # Aguardar um tempo antes de enviar a próxima mensagem
    time.sleep(60)

    # Fechar a janela do WhatsApp Web

    keyboard.press_and_release("ctrl + w")
