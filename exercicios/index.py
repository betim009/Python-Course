import tkinter
from tkinter import ttk

# Janela
janela = tkinter.Tk()
janela.title("Cardápio")
janela.geometry("1000x800")

# Tabela
tabela = ttk.Treeview(
    janela, columns=("Código", "Descrição", "Valor"), show="headings")
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")

# Linhas
tabela.insert("", "end", text="1", values=("101", "X-Burguer", 10.00))
tabela.insert("", "end", text="2", values=("102", "X-Egg", 12.00))
tabela.insert("", "end", text="3", values=("103", "X-Egg Bacon", 14.50))
tabela.insert("", "end", text="4", values=("104", "X-Tudo", 19.00))
tabela.insert("", "end", text="5", values=("201", "Coca Cola 2 Litros", 15.00))
tabela.insert("", "end", text="6", values=("202", "Guaraná 2 Litros", 10.00))
tabela.insert("", "end", text="7", values=("203", "Pepsi 2 Litros", 9.00))
tabela.insert("", "end", text="8", values=("204", "Fanta Uva", 9.50))

valor_total = 0.0


def calcular_valor():
    global valor_total
    codigo = entry_codigo.get()
    if codigo == "101":
        valor_total += 10.00
    elif codigo == "102":
        valor_total += 12.00
    elif codigo == "103":
        valor_total += 14.50
    elif codigo == "104":
        valor_total += 19.00
    elif codigo == "201":
        valor_total += 15.00
    elif codigo == "202":
        valor_total += 10.00
    elif codigo == "203":
        valor_total += 9.00
    elif codigo == "204":
        valor_total += 9.50
    else:
        print("Código inválido!")

    print(valor_total)


# Entry
label_codigo = tkinter.Label(janela, text="Insira o código da descrição:")
entry_codigo = tkinter.Entry(janela)
botao = tkinter.Button(janela, text="Confirmar", command=calcular_valor)

# Exibindo elementos
tabela.pack()
label_codigo.pack()
entry_codigo.pack()
botao.pack()

# Iniciar a interface
janela.mainloop()
