import youtube_dl  # pip install youtube_dl

# URL do vídeo
url = "https://www.youtube.com/watch?v=CnZRzX0D7I8&t=2s"

# Defina as opções para o downloader
ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "outtmpl": "/home/alberto/Documents/Projetos/%(title)s.%(ext)s",
}

# Crie o objeto youtube_dl e baixe o vídeo
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("O vídeo foi baixado com sucesso!")
