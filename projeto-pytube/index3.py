import pafy

# URL do vídeo
url = "https://www.youtube.com/watch?v=CnZRzX0D7I8&t=2s"

# Criar um objeto Video a partir da URL
video = pafy.new(url)

# Obter o melhor stream disponível
best_stream = video.getbest()

# Definir o diretório de destino
diretorio_destino = "/home/alberto/Documents/Projetos"

# Baixar o vídeo
best_stream.download(filepath=diretorio_destino)

print("O vídeo foi baixado com sucesso!")
