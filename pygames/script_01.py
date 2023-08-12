import pygame

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
largura = 1000
altura = 800

# Criação da janela com as dimensões especificadas
janela = pygame.display.set_mode((largura, altura))

# Configuração do título da janela
pygame.display.set_caption("Meu Primeiro Jogo")

# Posição inicial do quadrado
x_quadrado = largura // 2
y_quadrado = altura // 2

# Velocidade de movimento do quadrado
velocidade = 2

# Variável de controle para o loop principal
executando = True

# Loop principal do jogo
while executando:
    # Verificação de eventos
    for evento in pygame.event.get():
        # Se o evento for o fechamento da janela, encerra o loop
        if evento.type == pygame.QUIT:
            executando = False

    # Captura do estado das teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimentação do quadrado com base nas teclas pressionadas
    if teclas[pygame.K_LEFT]:
        x_quadrado -= velocidade
    if teclas[pygame.K_RIGHT]:
        x_quadrado += velocidade
    if teclas[pygame.K_UP]:
        y_quadrado -= velocidade
    if teclas[pygame.K_DOWN]:
        y_quadrado += velocidade

    # Limpeza da tela com a cor preta
    janela.fill((0, 0, 0))

    # Desenho do quadrado vermelho na posição atual
    pygame.draw.rect(janela, (255, 0, 0), (x_quadrado, y_quadrado, 50, 50))

    # Atualização da tela para mostrar as mudanças
    pygame.display.update()

# Encerramento do Pygame ao final do loop
pygame.quit()
