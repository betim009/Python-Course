import tkinter
from tkinter import ttk

# Cria a janela principal
janela = tkinter.Tk()
janela.title("Cardápio")
janela.geometry("1000x800")

# Cria a tabela com 3 colunas
tabela = ttk.Treeview(
    janela, columns=("Código", "Descrição", "Valor"), show="headings")
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")
tabela.insert("", "end", text="1", values=("101", "X-Burguer", 12.00))
tabela.insert("", "end", text="2", values=("102", "X-Egg", 14.50))
tabela.insert("", "end", text="3", values=("103", "X-Egg Bacon", 12.00))
tabela.insert("", "end", text="4", values=("104", "X-Burguer", 12.00))
tabela.insert("", "end", text="5", values=("201", "Coca Cola 2lts", 12.00))
tabela.insert("", "end", text="6", values=("202", "Guarana 2lts", 10.00))
tabela.insert("", "end", text="7", values=("203", "Fanta Uva 2lts", 9.00))
tabela.insert("", "end", text="8", values=("204", "Fanta Laranja 2lts", 9.00))

# Variável para o valor total do pedido
valor_total = 0.0


# Função para calcular o valor com base no código
def calcular_valor():
    global valor_total
    codigo = entry_codigo.get()  # Obtém o código da entrada
    if codigo == "101":
        valor_total += 12.00
    elif codigo == "102":
        valor_total += 14.50
    elif codigo == "103":
        valor_total += 12.00
    elif codigo == "104":
        valor_total += 12.00
    elif codigo == "201":
        valor_total += 12.00
    elif codigo == "202":
        valor_total += 10.00
    elif codigo == "203":
        valor_total += 9.00
    elif codigo == "204":
        valor_total += 9.00
    else:
        print("Código inválido.")

    label_valor_pedido.config(
        text="Valor do pedido: {:.2f}".format(valor_total))

    print("Valor total:", valor_total)


# Label para exibir o valor do pedido
label_valor_pedido = tkinter.Label(
    janela, text="Valor do pedido: {:.2f}".format(valor_total)
)

# Entry
label_codigo = tkinter.Label(janela, text="Insira o código do pedido:")
entry_codigo = tkinter.Entry(janela)

# Botão
botao = tkinter.Button(janela, text="Confirmar", command=calcular_valor)

# Exibe a tabela, labels, entry e botão
tabela.pack()
label_valor_pedido.pack()
label_codigo.pack()
entry_codigo.pack()
botao.pack()

# Inicia o loop principal
janela.mainloop()
