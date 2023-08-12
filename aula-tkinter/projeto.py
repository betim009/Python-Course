import tkinter  # palavra reservada

# Janela principal:
janela = tkinter.Tk()
# título:
janela.title("Projeto")
# tamanho:
janela.geometry("600x650")
# cor de fundo
janela.configure(bg="blue")

# LABELS:
nome = tkinter.Label(janela, text="Qual o seu nome:")
nome.grid(row=0, column=0, pady=10)

# ENTRYS:
nome_entrada = tkinter.Entry(janela)
nome_entrada.grid(row=1, column=0)


janela.mainloop()  # start
