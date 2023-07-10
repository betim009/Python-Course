import csv
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font


def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    bairro = entry_bairro.get()
    internado = var_internado.get()

    if not nome or not cpf or not idade or not cidade or not bairro:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "A idade deve ser um número inteiro!")
        return

    info = {
        "Nome": nome,
        "CPF": cpf,
        "Idade": idade,
        "Cidade": cidade,
        "Bairro": bairro,
        "Internado": internado,
    }

    arquivo_existe = True
    try:
        with open("dados.csv", "r"):
            pass
    except FileNotFoundError:
        arquivo_existe = False

    with open("dados.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=info.keys())

        if not arquivo_existe:
            writer.writeheader()

        writer.writerow(info)

    label_info["text"] = f"Informações cadastradas:\n{info}"

    limpar_campos()


def limpar_campos():
    entry_nome.delete(0, tkinter.END)
    entry_cpf.delete(0, tkinter.END)
    entry_idade.delete(0, tkinter.END)
    entry_cidade.delete(0, tkinter.END)
    entry_bairro.delete(0, tkinter.END)
    var_internado.set("Não")


def pesquisar():
    cpf_pesquisado = entry_busca_cpf.get()

    if not cpf_pesquisado:
        messagebox.showerror("Erro", "Digite um CPF para pesquisar!")
        return

    try:
        with open("dados.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["CPF"] == cpf_pesquisado:
                    label_info["text"] = f"Informações encontradas:\n{row}"
                    return

        label_info[
            "text"
        ] = f"Nenhuma informação encontrada para o CPF: {cpf_pesquisado}"
    except FileNotFoundError:
        messagebox.showinfo("Informação", "Nenhum dado cadastrado ainda.")


janela = tkinter.Tk()
# Define o título da janela
janela.title("Clínica")
janela.geometry("900x900")
janela["padx"] = 10
janela["pady"] = 10

fonte_label = Font(size=12)
fonte_entry = Font(size=12)

label_nome = tkinter.Label(janela, text="Nome:", font=fonte_label)
entry_nome = tkinter.Entry(janela, font=fonte_entry)
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_cpf = tkinter.Label(janela, text="CPF:", font=fonte_label)
entry_cpf = tkinter.Entry(janela, font=fonte_entry)
label_cpf.grid(row=1, column=0, padx=5, pady=5)
entry_cpf.grid(row=1, column=1, padx=5, pady=5)

label_idade = tkinter.Label(janela, text="Idade:", font=fonte_label)
entry_idade = tkinter.Entry(janela, font=fonte_entry)
label_idade.grid(row=2, column=0, padx=5, pady=5)
entry_idade.grid(row=2, column=1, padx=5, pady=5)

label_cidade = tkinter.Label(janela, text="Cidade:", font=fonte_label)
entry_cidade = tkinter.Entry(janela, font=fonte_entry)
label_cidade.grid(row=3, column=0, padx=5, pady=5)
entry_cidade.grid(row=3, column=1, padx=5, pady=5)

label_bairro = tkinter.Label(janela, text="Bairro:", font=fonte_label)
entry_bairro = tkinter.Entry(janela, font=fonte_entry)
label_bairro.grid(row=4, column=0, padx=5, pady=5)
entry_bairro.grid(row=4, column=1, padx=5, pady=5)

label_internado = tkinter.Label(janela, text="Já foi internado?", font=fonte_label)
var_internado = tkinter.StringVar(janela)
var_internado.set("Não")
combobox_internado = ttk.Combobox(
    janela, textvariable=var_internado, values=["Sim", "Não"], font=fonte_entry
)
label_internado.grid(row=5, column=0, padx=5, pady=5)
combobox_internado.grid(row=5, column=1, padx=5, pady=5)

label_busca_cpf = tkinter.Label(janela, text="Busca Por CPF:", font=fonte_label)
entry_busca_cpf = tkinter.Entry(janela, font=fonte_entry)
label_busca_cpf.grid(row=1, column=2, padx=5, pady=5)
entry_busca_cpf.grid(row=1, column=3, padx=5, pady=5)

button_cadastrar = tkinter.Button(janela, text="Cadastrar", command=cadastrar)
button_cadastrar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

label_info = tkinter.Label(janela, text="", wraplength=400, font=fonte_label)
label_info.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

button_pesquisar = tkinter.Button(janela, text="Pesquisar", command=pesquisar)
button_pesquisar.grid(row=1, column=4, padx=5, pady=5)

janela.mainloop()
