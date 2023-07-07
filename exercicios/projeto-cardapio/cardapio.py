import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

total = 0
start = 0
pedidos = []


# Função para calcular o total do pedido
def calcular_total(codigo):
    global total

    if codigo == "100":
        total += 9
        pedidos.append("Cachorro-quente")
        messagebox.showinfo(
            "Pedido", "Você pediu um Cachorro-Quente no valor de R$ 9,00"
        )
    elif codigo == "101":
        total += 11
        pedidos.append("Cachorro-quente Duplo")
        messagebox.showinfo(
            "Pedido", "Você pediu um Cachorro-quente Duplo no valor de R$ 11,00"
        )
    elif codigo == "102":
        total += 12
        pedidos.append("X-Egg")
        messagebox.showinfo("Pedido", "Você pediu um X-Egg no valor de R$ 12,00")
    elif codigo == "103":
        total += 13
        pedidos.append("X-Salada")
        messagebox.showinfo("Pedido", "Você pediu um X-Salada no valor de R$ 13,00")
    elif codigo == "104":
        total += 14
        pedidos.append("X-Bacon")
        messagebox.showinfo("Pedido", "Você pediu um X-Bacon no valor de R$ 14,00")
    elif codigo == "105":
        total += 17
        pedidos.append("X-Tudo")
        messagebox.showinfo("Pedido", "Você pediu um X-Tudo no valor de R$ 17,00")
    elif codigo == "200":
        total += 5
        pedidos.append("Refrigerante Lata")
        messagebox.showinfo(
            "Pedido", "Você pediu um Refrigerante Lata no valor de R$ 5,00"
        )
    elif codigo == "201":
        total += 4
        pedidos.append("Chá Gelado")
        messagebox.showinfo("Pedido", "Você pediu um Chá Gelado no valor de R$ 4,00")
    else:
        messagebox.showwarning("Opção Inválida", "Código de pedido inválido!")

    atualizar_carrinho()


# Função para atualizar o carrinho
def atualizar_carrinho():
    carrinho_text.config(state="normal")
    carrinho_text.delete("1.0", tk.END)
    carrinho_text.insert(tk.END, "Carrinho:\n")
    for i, item in enumerate(pedidos, start=1):
        carrinho_text.insert(tk.END, "{:02d} - {}\n".format(i, item))
    carrinho_text.insert(tk.END, "Valor total: R$ {:.2f}".format(total))
    carrinho_text.config(state="disabled")


# Função para lidar com a ação do botão "Pedir"
def pedir():
    codigo = codigo_entry.get()
    calcular_total(codigo)
    codigo_entry.delete(0, tk.END)


# Função para lidar com a ação do botão "Finalizar"
def finalizar():
    global total
    messagebox.showinfo(
        "Total a Pagar", "O total a ser pago é: R$ {:.2f}".format(total)
    )
    total = 0
    pedidos = []
    atualizar_carrinho()
    root.destroy()


# Configuração da janela principal
root = tk.Tk()
root.title("Lanchonete")
root.geometry("1280x900")  # Definindo o tamanho da janela

# Estilos
background_color = "#f1f1f1"
font_label_title = ("Arial", 16, "bold")
font_label_cardapio = ("Arial", 12)
font_button = ("Arial", 12)

# Frame dos Pedidos
pedidos_frame = tk.Frame(root, bg=background_color)
pedidos_frame.pack(pady=20)

# Label e Entry para inserir o código do pedido
codigo_label = tk.Label(
    pedidos_frame,
    text="Entre com o código desejado:",
    font=font_label_cardapio,
    bg=background_color,
)
codigo_label.grid(row=0, column=0, padx=10)

codigo_entry = tk.Entry(pedidos_frame, font=font_label_cardapio)
codigo_entry.grid(row=0, column=1, padx=10)

# Botões "Pedir" e "Finalizar"
pedir_button = tk.Button(pedidos_frame, text="Pedir", command=pedir, font=font_button)
pedir_button.grid(row=1, column=0, pady=10)

finalizar_button = tk.Button(
    pedidos_frame, text="Finalizar", command=finalizar, font=font_button
)
finalizar_button.grid(row=1, column=1, pady=10)

# Frame da Tabela
tabela_frame = tk.Frame(root, bg=background_color)
tabela_frame.pack()

# Tabela
tabela = ttk.Treeview(tabela_frame)
tabela["columns"] = ("Descrição", "Valor")
tabela.column("#0", width=100, minwidth=50)
tabela.column("Descrição", width=250, minwidth=150)
tabela.column("Valor", width=100, minwidth=50)
tabela.heading("#0", text="Código")
tabela.heading("Descrição", text="Descrição")
tabela.heading("Valor", text="Valor")

# Adicionar linhas à tabela
tabela.insert("", tk.END, text="100", values=("Cachorro-quente", "R$ 9,00"))
tabela.insert("", tk.END, text="101", values=("Cachorro-quente Duplo", "R$ 11,00"))
tabela.insert("", tk.END, text="102", values=("X-Egg", "R$ 12,00"))
tabela.insert("", tk.END, text="103", values=("X-Salada", "R$ 13,00"))
tabela.insert("", tk.END, text="104", values=("X-Bacon", "R$ 14,00"))
tabela.insert("", tk.END, text="105", values=("X-Tudo", "R$ 17,00"))
tabela.insert("", tk.END, text="200", values=("Refrigerante Lata", "R$ 5,00"))
tabela.insert("", tk.END, text="201", values=("Chá Gelado", "R$ 4,00"))

tabela.pack()

# Frame do Carrinho
carrinho_frame = tk.LabelFrame(
    root, text="Carrinho", bg=background_color, font=font_label_cardapio
)
carrinho_frame.pack(pady=20)

# Texto do Carrinho
carrinho_text = tk.Text(
    carrinho_frame, height=10, width=40, font=font_label_cardapio
)
carrinho_text.pack(padx=10, pady=10)
carrinho_text.config(state="disabled")

root.mainloop()
