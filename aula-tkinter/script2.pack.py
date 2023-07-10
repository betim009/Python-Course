import tkinter

# Criando a janela principal
janela = tkinter.Tk()
# título da janela
janela.title("Título do projeto")
# tamanho da janela
janela.geometry("650x450")


# elementos dentro da janela:
label = tkinter.Label(janela, text="Qual o seu nome?")
label.pack()

label_2 = tkinter.Label(janela, text="Qual a sua cidade?")
label_2.pack()

# Chamando a janela para exibir por meio de loop
janela.mainloop()
