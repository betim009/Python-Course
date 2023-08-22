import pygame

# Incialização do Pygame
pygame.init()

# Definição da janela
largura = 1000
altura = 800

# Criação da janela com as dimensões
janela = pygame.display.set_mode((largura, altura))

# Configuração do título do game
pygame.display.set_caption("First Game")

# Posição do Quadrado na janela
x_quadrado = largura // 2
y_quadrado = altura // 2

# Tamanho do Quadrado
tamanho_do_quadrado = 50

# Velocidade do quadrado
velocidade = 5

# Loop
executando = True

# Relógio para controle de FPS
clock = pygame.time.Clock()

# Iniciando Loop
while executando:
    for evento in pygame.event.get():
        # se o evento for o fechamento da janela, encerra o loop
        if evento.type == pygame.QUIT:
            executando = False

    # Capturando as teclas
    teclas = pygame.key.get_pressed()

    # Movimentos do quadrado, com base na tecla pressionada
    if teclas[pygame.K_LEFT]:
        x_quadrado -= velocidade
    if teclas[pygame.K_RIGHT]:
        x_quadrado += velocidade
    if teclas[pygame.K_UP]:
        y_quadrado -= velocidade
    if teclas[pygame.K_DOWN]:
        y_quadrado += velocidade

    # Limitando os limites da tela
    if x_quadrado < 0:
        x_quadrado = 0
    if x_quadrado > largura - tamanho_do_quadrado:
        x_quadrado = largura - tamanho_do_quadrado
    if y_quadrado < 0:
        y_quadrado = 0
    if y_quadrado > altura - tamanho_do_quadrado:
        y_quadrado = altura - tamanho_do_quadrado

    # Preenchendo a tela com uma cor
    janela.fill((0, 0, 0))  # Por exemplo, preto

    # Desenhando o quadrado na tela
    pygame.draw.rect(
        janela,
        (255, 0, 0),
        (x_quadrado, y_quadrado, tamanho_do_quadrado, tamanho_do_quadrado),
    )

    # Atualizando a tela
    pygame.display.update()

    # Controlando a taxa de atualização (FPS)
    clock.tick(60)  # 60 FPS

# Encerrando o Pygame ao final
pygame.quit()
