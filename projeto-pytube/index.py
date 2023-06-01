# terminal:
# pip --version
# pip install pytube

from pytube import YouTube

# url do video:
url = "https://www.youtube.com/watch?v=4p7axLXXBGU"

video = YouTube(url)

# array completo de video
# print(dir(video))

# Todas informações:
# print("Título:", video.title)
# print("Descrição:", video.description)
# print("Duração:", video.length, "segundos")
# print("Autor:", video.author)
# print("Visualizações:", video.views)

print("Título: ", video.title)
print("Resolução disponível: ",
      video.streams.filter(file_extension="mp4").all())
print("Duração: ", video.length, "segundos")

# 144, 240, 360, 480, 720, 1080
resolucao = 720

stream = video.streams.filter(res=resolucao, file_extension="mp4").first()

# diretorio salvo em:
# utilize pwd no terminal para linux:
diretorio_destino = "/home/alberto/Documents/Projetos"

stream.download(output_path=diretorio_destino)

print("O vídeo foi baixado com sucesso!")
