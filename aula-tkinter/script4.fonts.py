import tkinter

# Criando a janela principal
janela = tkinter.Tk()
# título da janela
janela.title("Título do projeto")
# tamanho da janela
janela.geometry("650x450")
# Cor de fundo:
janela.configure(bg="blue")


# elementos dentro da janela:
# Estilos personalizados:

label_font = ("Open Sans", 20)

label = tkinter.Label(janela, text="Qual o seu nome?", font=("Arial", 20))
label.grid(row=0, column=0)

label_2 = tkinter.Label(janela, text="Qual a sua cidade?", font=(label_font))
label_2.grid(row=1, column=0)


# Chamando a janela para exibir por meio de loop
janela.mainloop()
