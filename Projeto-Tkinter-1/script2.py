import tkinter

# Janela Principal
janela = tkinter.Tk()
janela.title("Construa seu Personagem")

# Configuração da imagem de fundo
imagem_fundo = tkinter.PhotoImage(file="fundo.png")
largura = imagem_fundo.width()
altura = imagem_fundo.height()

# Define o tamanho da janela de acordo com a imagem de fundo
janela.geometry(f"{largura}x{altura}")

# Canvas para exibir a imagem de fundo
canvas = tkinter.Canvas(janela, width=largura, height=altura)
canvas.pack()

# Exibe a imagem de fundo no canvas
canvas.create_image(0, 0, image=imagem_fundo, anchor="nw")

# Inicia o loop principal da interface gráfica
janela.mainloop()
