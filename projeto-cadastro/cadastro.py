import csv
import tkinter
from tkinter import ttk


def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    bairro = entry_bairro.get()
    internado = var_internado.get()

    info = {
        "Nome": nome,
        "Idade": idade,
        "Cidade": cidade,
        "Bairro": bairro,
        "Internado": internado,
    }

    # Verifica se o arquivo já existe
    arquivo_existe = True
    try:
        with open("dados.csv", "r"):
            pass
    except FileNotFoundError:
        arquivo_existe = False

    # Salvar os dados em um arquivo CSV
    with open("dados.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=info.keys())

        if not arquivo_existe:  # Se o arquivo não existir, escrever o cabeçalho
            writer.writeheader()

        writer.writerow(info)

    # Atualizar a label de informações
    info_atual = label_info["text"]
    novo_info = f"{info_atual}\n{info}"
    label_info["text"] = novo_info


# Cria a janela
janela = tkinter.Tk()

# Define o tamanho da janela
janela.geometry("900x900")

# Define o padding externo para todos os elementos
janela["padx"] = 10
janela["pady"] = 10

# Label e Entry do nome:
label_nome = tkinter.Label(janela, text="Nome:")
entry_nome = tkinter.Entry(janela)
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

# Label e Entry da idade:
label_idade = tkinter.Label(janela, text="Idade:")
entry_idade = tkinter.Entry(janela)
label_idade.grid(row=1, column=0, padx=5, pady=5)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

# Label e Entry da cidade:
label_cidade = tkinter.Label(janela, text="Cidade:")
entry_cidade = tkinter.Entry(janela)
label_cidade.grid(row=2, column=0, padx=5, pady=5)
entry_cidade.grid(row=2, column=1, padx=5, pady=5)

# Label e Entry do bairro:
label_bairro = tkinter.Label(janela, text="Bairro:")
entry_bairro = tkinter.Entry(janela)
label_bairro.grid(row=3, column=0, padx=5, pady=5)
entry_bairro.grid(row=3, column=1, padx=5, pady=5)

# Label e Combobox de "Já foi internado?"
label_internado = tkinter.Label(janela, text="Já foi internado?")
var_internado = tkinter.StringVar(janela)
var_internado.set("Não")  # Valor padrão selecionado
combobox_internado = ttk.Combobox(
    janela, textvariable=var_internado, values=["Sim", "Não"]
)
label_internado.grid(row=4, column=0, padx=5, pady=5)
combobox_internado.grid(row=4, column=1, padx=5, pady=5)

# Botão de cadastrar:
button_cadastrar = tkinter.Button(janela, text="Cadastrar", command=cadastrar)
button_cadastrar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Label de informações:
label_info = tkinter.Label(janela, text="", wraplength=400)
label_info.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Inicia o loop de eventos da janela
janela.mainloop()
