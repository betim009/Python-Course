import csv
import tkinter


def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    bairro = entry_bairro.get()

    info_atual = label_info["text"]
    novo_info = f"""{info_atual}\nNome: {nome} Idade: {idade}\n
    Cidade: {cidade} Bairro: {bairro}"""
    label_info["text"] = novo_info

    # Salvar os dados em um arquivo CSV
    with open("dados.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([f"Nome: {nome}, Idade: {idade}, cidade: {cidade}"])


# Cria a janela
janela = tkinter.Tk()

# Cria os elementos da interface
# Label e Entry da nome:
label_nome = tkinter.Label(janela, text="Nome:")
entry_nome = tkinter.Entry(janela)

# Label e Entry da idade:
label_idade = tkinter.Label(janela, text="Idade:")
entry_idade = tkinter.Entry(janela)

# Label e Entry da cidade:
label_cidade = tkinter.Label(janela, text="Cidade:")
entry_cidade = tkinter.Entry(janela)

# Label e Entry da bairro:
label_bairo = tkinter.Label(janela, text="Bairro:")
entry_bairro = tkinter.Entry(janela)

# Botão de cadastrar:
button_cadastrar = tkinter.Button(janela, text="Cadastrar", command=cadastrar)
label_info = tkinter.Label(janela, text="")

# Organiza os elementos na janela
label_nome.pack()
entry_nome.pack()
label_idade.pack()
entry_idade.pack()
label_cidade.pack()
entry_cidade.pack()
label_bairo.pack()
entry_bairro.pack()
button_cadastrar.pack()
label_info.pack()

# Inicia o loop de eventos da janela
janela.mainloop()
