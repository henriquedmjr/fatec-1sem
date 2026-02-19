import os


def buscar_arquivo(pasta, alvo):
    try:
        itens = os.listdir(pasta)
    except PermissionError:
        return 
    for item in itens:
        caminho_completo = os.path.join(pasta, item)
        if os.path.isdir(caminho_completo):
            buscar_arquivo(caminho_completo, alvo)
        elif os.path.isfile(caminho_completo):
            if item == alvo:
                print(f"ACHEI! está em: {caminho_completo}")
                

arquivo = input("Digite o nome do arquivo que deseja encontrar: ")
resultado_final = buscar_arquivo(os.path.expanduser("~"), arquivo)
