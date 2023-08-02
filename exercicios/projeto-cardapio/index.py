import tkinter
from tkinter import ttk
import csv

# Valor Total Global
valor_total = 0.0


# Funções:
# função de calcular o valor
def calcular_valor():
    global valor_total
    codigo = entry_codigo.get()
    if codigo == "101":
        valor_total += 12.0
    elif codigo == "102":
        valor_total += 14.0
    elif codigo == "103":
        valor_total += 14.0
    elif codigo == "104":
        valor_total += 17.0
    elif codigo == "201":
        valor_total += 10.0
    elif codigo == "202":
        valor_total += 3.5
    elif codigo == "203":
        valor_total += 8.0
    elif codigo == "204":
        valor_total += 8.0
    else:
        print("Codigo Invalido")
    label_valor.config(text="Valor do pedido: {:.2f}".format(valor_total))


# função de finalizar pedido
def finalizar_pedido():
    janela.quit()


# função de salvar pedido
def salvar_pedido():
    global valor_total
    with open("pedidos.csv", mode="a", newline="") as file:
        escrever = csv.writer(file)
        escrever.writerow([valor_total])
    print("Salvo com sucesso")


# Janela:
janela = tkinter.Tk()
style = ttk.Style()
janela.title("Cardapio")
janela.geometry("600x900")
janela.configure(bg="#E12222")

# Tabela:
tabela = ttk.Treeview(
    janela,
    columns=("Código", "Descrição", "Valor"),
    show="headings",)

# Cabeçalho:
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")

# Estilo para Cabeçalho:
style.configure(
    "Treeview.Heading",
    font=("Britannic Bold", 14, "bold"),
    background="#950C0C",
    foreground="white",)

# Linhas da tabela:
tabela.insert(
    "", "end", text="1",
    values=("101", "X-Burguer", "12.00"))

tabela.insert(
    "", "end", text="2",
    values=("102", "X-Bacon", "14.00"))

tabela.insert(
    "", "end", text="3",
    values=("103", "X-egg", "14.00"))

tabela.insert(
    "", "end", text="4",
    values=("104", "X-Tudo", "17.00"))

tabela.insert(
    "", "end", text="5",
    values=("201", "Coca Cola 2 litros", "10.00"))

tabela.insert(
    "", "end", text="6",
    values=("202", "Bacana 2 litros", "3.50"))

tabela.insert(
    "", "end", text="7",
    values=("203", "pepsi 2 litros", "8.00"))

tabela.insert(
    "", "end", text="8",
    values=("204", "Antartica 2 litros", "8.00"))

# Label Código
label_codigo = tkinter.Label(
    janela,
    font=("Britannic Bold", 14, "bold"),
    background="#E12222",
    foreground="white",
    text="Insira o codigo desejado:",)

# Entry Código
entry_codigo = tkinter.Entry(
    janela,
    font=("Britannic Bold", 14))

# Botão Enviar
botao = tkinter.Button(
    janela,
    font=("Britannic Bold", 14, "bold"),
    width=40,
    background="white",
    command=calcular_valor,
    text="Enviar",)

# Label para o valor do pedido
label_valor = tkinter.Label(
    janela,
    font=("Britannic Bold", 14, "bold"),
    background="#E12222",
    foreground="white",
    text="Valor do pedido: {:.2f}".format(valor_total))

# Botão Finalizar
botao_finalizar = tkinter.Button(
    janela,
    font=("Britannic Bold", 14, "bold"),
    width=40,
    background="white",
    command=finalizar_pedido,
    text="Finalizar Pedido!",)

# Botão Salvar
botao_salvar = tkinter.Button(
    janela,
    font=("Britannic Bold", 14, "bold"),
    width=40,
    background="white",
    command=salvar_pedido,
    text="Salvar pedido",)

# Ordem dos elementos:
tabela.pack(pady=10)
label_codigo.pack(pady=10)
entry_codigo.pack(pady=10)
botao.pack(pady=10)
botao_salvar.pack(pady=10)
label_valor.pack(pady=50)
botao_finalizar.pack(pady=10)

# Iniciar o loop
janela.mainloop()
