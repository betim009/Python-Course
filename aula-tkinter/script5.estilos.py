import tkinter

# Criando a janela principal
janela = tkinter.Tk()
# título da janela
janela.title("Título do projeto")
# tamanho da janela
janela.geometry("650x650")
# Cor de fundo:
janela.configure(bg="blue")

# elementos dentro da janela:
# Estilos personalizados:

estilo_label = {
    "font": ("Open Sans", 20),
    "bg": "white",
    "padx": 5,
    "pady": 5,
    "bd": 2,
    "relief": "solid",
}

label = tkinter.Label(janela, text="Qual o seu nome?", **estilo_label)
label.grid(row=0, column=0)

label_2 = tkinter.Label(janela, text="Qual a sua cidade?", **estilo_label)
label_2.grid(row=4, column=0)

# Chamando a janela para exibir por meio de loop
janela.mainloop()
