import tkinter
from tkinter import ttk


# 4. Função criar:
def criar_personagem():
    nome = entry_nome.get()
    classe = combo_classe.get()

    # Código para criar um personagem com base nos valores inseridos
    label_resultado.config(text=f"Personagem criado:\nNome: {nome}\nClasse: {classe}")

    # 5. Atualiza a imagem correspondente à classe selecionada
    if classe == "Mago":
        imagem_classe = tkinter.PhotoImage(file="mago.png").subsample(2, 2)
    elif classe == "Guerreiro":
        imagem_classe = tkinter.PhotoImage(file="guerreiro.png").subsample(2, 2)
    elif classe == "Arqueiro":
        imagem_classe = tkinter.PhotoImage(file="arqueiro.png").subsample(2, 2)
    else:
        imagem_classe = None

    label_imagem.config(image=imagem_classe)
    label_imagem.image = imagem_classe


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
label_nome = tkinter.Label(janela, text="Nome do seu personagem:", font=("Arial", 12))
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


# 4. Botão:
botao_criar = tkinter.Button(
    janela,
    text="Criar Personagem",
    command=criar_personagem,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
)
botao_criar.place(x=50, y=150)

# 4. Resultados:
label_resultado = tkinter.Label(
    janela,
    text="",
    font=("Arial", 12),
    bg="#ECECEC",
    relief=tkinter.RIDGE,
    width=30,
    height=5,
)
label_resultado.place(x=50, y=200)

# 5. Label para exibir a imagem da classe selecionada
label_imagem = tkinter.Label(janela, image=None)
label_imagem.place(x=50, y=310)

# 1. Inicia o loop principal da interface gráfica
janela.mainloop()
