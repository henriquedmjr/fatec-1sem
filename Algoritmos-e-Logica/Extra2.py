import os

def explorar(caminho, alvo, nivel=0):
    nome_pasta = os.path.basename(caminho) or "Home"
    espaco = "  " * nivel

    conteudo_encontrado = []
    
    try:
        itens = os.listdir(caminho)
    except PermissionError:
        return []

    if alvo in itens:
        return [f"{espaco}📂 {nome_pasta}/", f"{espaco}  📄 {alvo} (AQUI!)"]
    for item in itens:
        caminho_completo = os.path.join(caminho, item)
        
        if os.path.isdir(caminho_completo):
            achou_na_subpasta = explorar(caminho_completo, alvo, nivel + 1)
            if len(achou_na_subpasta) > 0:
                oq_achou = [f"{espaco}📂 {nome_pasta}/"] 
                return oq_achou + achou_na_subpasta

    return []

print("--- Iniciando Busca ---")
arquivo = input("Digite o nome do arquivo que deseja encontrar: ")
resultado_final = explorar(os.path.expanduser("~"), arquivo)

if resultado_final:
    print("Caminho encontrado:")
    for i in resultado_final:
        print(i)
else:
    print("Arquivo não encontrado.")