import tkinter as tk

janela = tk.Tk()
janela.title("Título do projeto")
janela.geometry("650x650")
janela.configure(bg="#f0f0f0")  # Cor de fundo mais clara

# Estilos personalizados
estilo_label = {
    "font": ("Arial", 16),  # Tamanho da fonte reduzido
    "bg": "#f0f0f0",  # Mesma cor de fundo
    "bd": 1,
    "relief": "solid",
}

# Label nome:
label = tk.Label(janela, text="Qual o seu nome?", **estilo_label)
label.grid(row=0, column=0, padx=10, pady=10)  # Espaçamento externo

# Entry nome:
entry = tk.Entry(janela, width=25)
entry.grid(row=1, column=0, padx=10, pady=10)  # Espaçamento externo

# Label idade:
label_2 = tk.Label(janela, text="Qual a sua cidade?", **estilo_label)
label_2.grid(row=2, column=0, padx=10, pady=10)  # Espaçamento externo

# Entry idade:
entry_2 = tk.Entry(janela, width=25)
entry_2.grid(row=3, column=0, padx=10, pady=10)  # Espaçamento externo

# Label para exibir resultado:
label_3 = tk.Label(janela, font=("Arial", 14), bg="#f0f0f0", pady=10)
label_3.grid(row=4, column=0, padx=10, pady=10)  # Espaçamento externo


# Função para o botão:
def exibir():
    resultado = f"Resultado: {entry.get()}, {entry_2.get()}"
    label_3.configure(text=resultado)


# Botão:
botao = tk.Button(
    janela,
    text="Clique",
    font=("Arial", 14),
    bg="#ff4d4d",
    fg="white",
    padx=10,
    pady=5,
    command=exibir,
)
botao.grid(row=5, column=0, padx=10, pady=10)  # Espaçamento externo

# Chamando a janela para exibir por meio de loop
janela.mainloop()
