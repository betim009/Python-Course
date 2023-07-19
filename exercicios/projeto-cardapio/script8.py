import tkinter
from tkinter import ttk
import csv


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
    elif codigo == "301":
        valor_total += 40.00
    elif codigo == "302":
        valor_total += 55.00
    elif codigo == "303":
        valor_total += 70.00
    else:
        print("Código inválido.")

    label_valor_pedido.config(
        text="Valor do pedido: {:.2f}".format(valor_total))

    print("Valor total:", valor_total)


# Função para salvar o valor do pedido em um arquivo CSV
def salvar_pedido():
    global valor_total
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([valor_total])
    print("Pedido salvo com sucesso!")


# Função para finalizar o pedido e fechar a janela
def finalizar_pedido():
    janela.quit()


# # # Janela
# Cria a janela principal e o Style
janela = tkinter.Tk()
style = ttk.Style()
janela.title("Cardápio")
janela.geometry("600x900")

# # # Tabela
# Cria a tabela com 3 colunas
tabela = ttk.Treeview(
    janela, columns=("Código", "Descrição", "Valor"), show="headings")

# Cria Cabeçalho
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")

# Cria Linhas
tabela.insert("", "end", text="1", values=("101", "X-Burguer", 12.00))
tabela.insert("", "end", text="2", values=("102", "X-Egg", 14.50))
tabela.insert("", "end", text="3", values=("103", "X-Egg Bacon", 12.00))
tabela.insert("", "end", text="4", values=("104", "X-Burguer", 12.00))
tabela.insert("", "end", text="5", values=("201", "Coca Cola 2lts", 12.00))
tabela.insert("", "end", text="6", values=("202", "Guarana 2lts", 10.00))
tabela.insert("", "end", text="7", values=("203", "Fanta Uva 2lts", 9.00))
tabela.insert("", "end", text="8", values=("301", "Pizza Grande", 40.00))
tabela.insert("", "end", text="9", values=("302", "Pizza Super Grande", 55.00))
tabela.insert("", "end", text="10", values=("303", "Pizza Infinita", 70.00))

# Define a largura das colunas
tabela.column("Código", width=80)
tabela.column("Descrição", width=300)
tabela.column("Valor", width=50)

# Define tamanho da font para 14
fonte_tabela = 14
style.configure("Treeview", font=fonte_tabela)

# Estiliza o cabeçalho com a fonte desejada
fonte_cabecalho = ("Arial", 14, "bold")
style.configure("Treeview.Heading", font=fonte_cabecalho)


# Label e Entry do Código
label_codigo = tkinter.Label(janela, text="Insira o código do pedido:")
entry_codigo = tkinter.Entry(janela)

# Botão Confirmar
botao_confirmar = tkinter.Button(
    janela, text="Confirmar", command=calcular_valor)

# Botão Salvar Pedido
botao_salvar = tkinter.Button(
    janela, text="Salvar Pedido", command=salvar_pedido)

# Botão Finalizar Pedido
botao_finalizar = tkinter.Button(
    janela, text="Finalizar Pedido", command=finalizar_pedido
)

# Label para exibir o valor do pedido
label_valor_pedido = tkinter.Label(
    janela, text="Valor do pedido: {:.2f}".format(valor_total)
)

# Exibe a tabela, labels, entry e botões
tabela.pack()
label_codigo.pack()
entry_codigo.pack()
botao_confirmar.pack()
botao_salvar.pack()
botao_finalizar.pack()
label_valor_pedido.pack()

# Inicia o loop principal
janela.mainloop()
