import tkinter
from tkinter import ttk

# Cria a janela principal
janela = tkinter.Tk()
janela.title("Cardápio")
janela.geometry("1000x800")

# Cria o Tabela com 3 colunas
tabela = ttk.Treeview(
    janela, columns=("Código", "Descrição", "Valor"), show="headings")
# Cabeçalhos
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")
# Linhas
tabela.insert("", "end", text="1", values=("101", "X-Burguer", 12.00, ))
tabela.insert("", "end", text="2", values=("102", "X-Egg", 14.50, ))
tabela.insert("", "end", text="3", values=("103", "X-Egg Bacon", 12.00, ))
tabela.insert("", "end", text="4", values=("104", "X-Burguer", 12.00, ))
tabela.insert("", "end", text="5", values=("201", "Coca Cola 2lts", 12.00, ))
tabela.insert("", "end", text="6", values=("202", "Guarana 2lts", 10.00, ))
tabela.insert("", "end", text="7", values=("203", "Fanta Uva 2lts", 09.00, ))
tabela.insert("", "end", text="8", values=("204", "Fanta Laranja 2lts", 09.00))

# Entry
label_codigo = tkinter.Label(janela, text="Insira o código do pedido:")
entry_codigo = tkinter.Entry(janela)
botao = tkinter.Button(janela, text="Confirmar")

# Exibe a tabela
tabela.pack()
label_codigo.pack()
entry_codigo.pack()
botao.pack()

# Inicia o loop principal
janela.mainloop()
