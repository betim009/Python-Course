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

    label_valor_pedido.config(text="Valor do pedido: {:.2f}".format(valor_total))

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
janela.configure(bg="#E12222")  # Laranja

# Logo
logo = tkinter.PhotoImage(file="logo.png")
# Cria um label para exibir a imagem
label_imagem = ttk.Label(janela, image=logo, borderwidth=0)
label_imagem.pack()

# # # Tabela
# Cria a tabela com 3 colunas
tabela = ttk.Treeview(
    janela, columns=("Código", "Descrição", "Valor"), show="headings")

# Cria Cabeçalho
tabela.heading("Código", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")

# Define a cor de fundo para o cabeçalho
style.configure("Treeview.Heading")

# Define a cor de fundo para as linhas pares (cinza claro)
tabela.tag_configure("par", background="#ccc")

# Define a cor de fundo para as linhas ímpares (branco)
tabela.tag_configure("impar", background="white")

# Cria as linhas com base nos dados do código
tabela.insert(
    "", "end", id="I001", values=("101", "X-Burguer", 12.00), tags=("par",))
tabela.insert(
    "", "end", id="I002", values=("102", "X-Egg", 14.50), tags=("impar",))
tabela.insert(
    "", "end", iid="I003", values=("103", "X-Egg Bacon", 12.00), tags=("par",))
tabela.insert(
    "", "end", iid="I004", values=("104", "X-Burguer", 12.00), tags=("impar",))
tabela.insert(
    "", "end", iid="I005", values=("201", "Coca Cola 2lts", 12.00), tags=("par",))
tabela.insert(
    "", "end", iid="I006", values=("202", "Guarana 2lts", 10.00), tags=("impar",))
tabela.insert(
    "", "end", iid="I007", values=("203", "Fanta Uva 2lts", 9.00), tags=("par",))
tabela.insert(
    "", "end", iid="I008", values=("301", "Pizza Grande", 40.00), tags=("impar",))
tabela.insert(
    "", "end", iid="I009", values=("302", "Pizza Super Grande", 55.00), tags=("par",))
tabela.insert(
    "", "end", values=("303", "Pizza Infinita", 70.00), tags=("impar",))

# Define a largura das colunas
tabela.column("Código", width=80)
tabela.column("Descrição", width=400)
tabela.column("Valor", width=80)

# Define tamanho da font para 14
fonte_tabela = 14
style.configure("Treeview", font=fonte_tabela)

# Estiliza o cabeçalho com a fonte desejada
fonte_cabecalho = ("Arial", 14, "bold")
style.configure(
    "Treeview.Heading",
    font=fonte_cabecalho,
    background="#950C0C",
    foreground="white")

# Label e Entry do Código
label_codigo = tkinter.Label(
    janela,
    text="Insira o código do pedido:",
    font=("Manjari", 16, "bold"),
    background="#E12222",
    foreground="white"
)
entry_codigo = tkinter.Entry(janela, font=("Manjari", 20))

# Botão Confirmar
botao_confirmar = tkinter.Button(
    janela,
    text="Confirmar",
    command=calcular_valor,
    font=("Manjari", 14, "bold"),
    width=45,
    background="white"
)

# Botão Salvar Pedido
botao_salvar = tkinter.Button(
    janela,
    text="Salvar Pedido",
    command=salvar_pedido,
    font=("Manjari", 14, "bold"),
    width=45,
    background="white"
)

# Botão Finalizar Pedido
botao_finalizar = tkinter.Button(
    janela,
    text="Finalizar Pedido",
    command=finalizar_pedido,
    font=("Manjari", 14, "bold"),
    width=45,
    background="white"
)

# Label para exibir o valor do pedido
label_valor_pedido = tkinter.Label(
    janela,
    text="Valor do pedido: {:.2f}".format(valor_total),
    font=("Manjari", 16, "bold"),
    width=45,
    background="#E12222",
    foreground="white"
)

# Exibe a tabela, labels, entry e botões
tabela.pack()
label_codigo.pack(pady=10)
entry_codigo.pack()
botao_confirmar.pack(pady=10)
botao_salvar.pack(pady=10)
botao_finalizar.pack(pady=10)
label_valor_pedido.pack(pady=20)

# Inicia o loop principal
janela.mainloop()
