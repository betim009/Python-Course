import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo de Adivinhação")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Número aleatório a ser adivinhado
numero_secreto = random.randint(1, 100)

# Fontes
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)


def display_message(message, y):
    text = small_font.render(message, True, black)
    text_rect = text.get_rect(center=(width // 2, y))
    window.blit(text, text_rect)


def main():
    running = True
    input_text = ""
    message = "Tente adivinhar o número entre 1 e 100"
    hint = ""
    tries = 0

    while running:
        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(input_text)
                        tries += 1
                        if guess < numero_secreto:
                            hint = "Tente um número maior"
                        elif guess > numero_secreto:
                            hint = "Tente um número menor"
                        else:
                            message = f"Parabéns! Você acertou em {tries} tentativas"
                            hint = ""
                    except ValueError:
                        hint = "Digite um número válido"
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.draw.rect(window, blue, (50, 300, width - 100, 40))
        txt_surface = font.render(input_text, True, white)
        txt_rect = txt_surface.get_rect(center=(width // 2, 320))
        window.blit(txt_surface, txt_rect)

        display_message(message, height // 2)
        display_message(hint, height // 2 + 30)

        pygame.draw.rect(window, black, (50, 250, width - 100, 40), 2)
        label = small_font.render("Digite sua tentativa:", True, black)
        window.blit(label, (60, 260))

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()


main()
