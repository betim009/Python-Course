def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")


def gravar_arquivo(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(dados + "\n")
        print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")


# Testando as funções
nome_do_arquivo = "dados.txt"

# Lendo o arquivo
ler_arquivo(nome_do_arquivo)

# Gravando dados no arquivo
dados_para_gravar = "Jairo"
gravar_arquivo(nome_do_arquivo, dados_para_gravar)

# Lendo o arquivo novamente para verificar a gravação
ler_arquivo(nome_do_arquivo)
