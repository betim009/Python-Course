import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import csv


class CadastroUI:
    def __init__(self, master):
        self.master = master
        self.fonte_label = Font(size=12)
        self.fonte_entry = Font(size=12)
        self.create_widgets()

    def create_widgets(self):
        self.label_nome = tk.Label(self.master, text="Nome:", font=self.fonte_label)
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(self.master, font=self.fonte_entry)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_cpf = tk.Label(self.master, text="CPF:", font=self.fonte_label)
        self.label_cpf.grid(row=1, column=0, padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.master, font=self.fonte_entry)
        self.entry_cpf.grid(row=1, column=1, padx=5, pady=5)

        self.label_idade = tk.Label(self.master, text="Idade:", font=self.fonte_label)
        self.label_idade.grid(row=2, column=0, padx=5, pady=5)
        self.entry_idade = tk.Entry(self.master, font=self.fonte_entry)
        self.entry_idade.grid(row=2, column=1, padx=5, pady=5)

        self.label_cidade = tk.Label(self.master, text="Cidade:", font=self.fonte_label)
        self.label_cidade.grid(row=3, column=0, padx=5, pady=5)
        self.entry_cidade = tk.Entry(self.master, font=self.fonte_entry)
        self.entry_cidade.grid(row=3, column=1, padx=5, pady=5)

        self.label_bairro = tk.Label(self.master, text="Bairro:", font=self.fonte_label)
        self.label_bairro.grid(row=4, column=0, padx=5, pady=5)
        self.entry_bairro = tk.Entry(self.master, font=self.fonte_entry)
        self.entry_bairro.grid(row=4, column=1, padx=5, pady=5)

        self.label_internado = tk.Label(
            self.master, text="Já foi internado?", font=self.fonte_label
        )
        self.label_internado.grid(row=5, column=0, padx=5, pady=5)
        self.var_internado = tk.StringVar(self.master)
        self.var_internado.set("Não")
        self.combobox_internado = ttk.Combobox(
            self.master,
            textvariable=self.var_internado,
            values=["Sim", "Não"],
            font=self.fonte_entry,
        )
        self.combobox_internado.grid(row=5, column=1, padx=5, pady=5)

        self.label_busca_cpf = tk.Label(
            self.master, text="Busca Por CPF:", font=self.fonte_label
        )
        self.label_busca_cpf.grid(row=1, column=2, padx=5, pady=5)
        self.entry_busca_cpf = tk.Entry(self.master, font=self.fonte_entry)
        self.entry_busca_cpf.grid(row=1, column=3, padx=5, pady=5)

        self.button_cadastrar = tk.Button(
            self.master, text="Cadastrar", command=self.cadastrar
        )
        self.button_cadastrar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.label_info = tk.Label(
            self.master, text="", wraplength=400, font=self.fonte_label
        )
        self.label_info.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.button_pesquisar = tk.Button(
            self.master, text="Pesquisar", command=self.pesquisar
        )
        self.button_pesquisar.grid(row=1, column=4, padx=5, pady=5)

    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        idade = self.entry_idade.get()
        cidade = self.entry_cidade.get()
        bairro = self.entry_bairro.get()
        internado = self.var_internado.get()

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

        self.label_info["text"] = f"Informações cadastradas:\n{info}"

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
        self.entry_bairro.delete(0, tk.END)
        self.var_internado.set("Não")

    def pesquisar(self):
        cpf_pesquisado = self.entry_busca_cpf.get()

        if not cpf_pesquisado:
            messagebox.showerror("Erro", "Digite um CPF para pesquisar!")
            return

        try:
            with open("dados.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["CPF"] == cpf_pesquisado:
                        self.label_info["text"] = f"Informações encontradas:\n{row}"
                        return

            self.label_info[
                "text"
            ] = f"Nenhuma informação encontrada para o CPF: {cpf_pesquisado}"
        except FileNotFoundError:
            messagebox.showinfo("Informação", "Nenhum dado cadastrado ainda.")


def main():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Clínica")
    janela.geometry("900x900")

    # Inicia a interface do cadastro
    cadastro_ui = CadastroUI(janela)

    # Inicia o loop de eventos da janela
    janela.mainloop()


if __name__ == "__main__":
    main()
