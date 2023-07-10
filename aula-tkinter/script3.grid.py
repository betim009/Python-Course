import tkinter

# Criando a janela principal
janela = tkinter.Tk()
# título da janela
janela.title("Título do projeto")
# tamanho da janela
janela.geometry("650x450")


# elementos dentro da janela:
# 1 parametro, janela. 2 paramentro, texto.
label = tkinter.Label(janela, text="Qual o seu nome?")
label.grid(row=0, column=0)

label_2 = tkinter.Label(janela, text="Qual a sua cidade?")
label_2.grid(row=1, column=0)

# Chamando a janela para exibir por meio de loop
janela.mainloop()
