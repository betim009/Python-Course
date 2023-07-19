import tkinter
from tkinter import ttk

# Janela
janela = tkinter.Tk()
janela.title("Cardapio")
janela.geometry("1000x800")

# Tabela
tabela = ttk.Treeview(
    janela, columns=("Código", "Descrição", "Valor"), show="headings")
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")

# Criar as linhas da tabela
tabela.insert("", "end", text="1", values=("101", "X-Burguer", "12.00"))
tabela.insert("", "end", text="2", values=("102", "X-Bacon", "14.00"))
tabela.insert("", "end", text="3", values=("103", "X-Egg", "14.00"))
tabela.insert("", "end", text="4", values=("104", "X-Tudo", "17.00"))
tabela.insert("", "end", text="5", values=("201", "Coca Cola 2 Litros", "10.00"))
tabela.insert("", "end", text="6", values=("202", "Cana Cola 2 Litros", "3.50"))
tabela.insert("", "end", text="7", values=("203", "Pepsi 2 Litros", "8.00"))
tabela.insert("", "end", text="8", values=("204", "Antartica 2 Litros", "8.00"))


# Label e Entry
label_codigo = tkinter.Label(janela, text="Insira o código desejado:", font=("Manjari", 14))
entry_codigo = tkinter.Entry(janela, font=("Manjari", 14))
botao = tkinter.Button(janela, text="Enviar", font=("Dyuthi", 14))

# Exibir elementos dentro da janela
tabela.pack()
label_codigo.pack()
entry_codigo.pack()
botao.pack()

# Iniciar o loop
janela.mainloop()
