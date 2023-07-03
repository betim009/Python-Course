import tkinter
from tkinter import ttk


# 1. Janela Principal
janela = tkinter.Tk()
janela.title("Construa seu Personagem")

# 2. Configuração da imagem de fundo
imagem_fundo = tkinter.PhotoImage(file="fundo.png")
largura = imagem_fundo.width()
altura = imagem_fundo.height()

# 2. Define o tamanho da janela de acordo com a imagem de fundo
janela.geometry(f"{largura}x{altura}")

# 2. Canvas para exibir a imagem de fundo
canvas = tkinter.Canvas(janela, width=largura, height=altura)
canvas.pack()

# 2. Exibe a imagem de fundo no canvas
canvas.create_image(0, 0, image=imagem_fundo, anchor="nw")

# 3. Componentes da interface

# Campo nome:
label_nome = tkinter.Label(
    janela, text="Nome do seu personagem:", font=("Arial", 12))
label_nome.place(x=50, y=50)
# Entrada de nome:
entry_nome = tkinter.Entry(janela, font=("Arial", 12))
entry_nome.place(x=260, y=50)

# campo de classe:
label_classe = tkinter.Label(
    janela, text="Classe do seu personagem:", font=("Arial", 12)
)
label_classe.place(x=50, y=100)
# Escolha de classes:
classes = ["Mago", "Guerreiro", "Arqueiro"]
combo_classe = ttk.Combobox(janela, values=classes, font=("Arial", 12))
combo_classe.place(x=260, y=100)

# 1. Inicia o loop principal da interface gráfica
janela.mainloop()
