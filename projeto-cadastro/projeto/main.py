import tkinter as tk
from modules.cadastro_ui import CadastroUI


def main():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Clínica")

    # Inicia a interface do cadastro
    cadastro_ui = CadastroUI(janela)

    # Inicia o loop de eventos da janela
    janela.mainloop()


if __name__ == "__main__":
    main()
