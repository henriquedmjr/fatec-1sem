def escolher_matriz(matriz_A, matriz_B):
    escolha = input("Aplicar em qual matriz? (a/b): ").lower()
    return matriz_A if escolha == 'a' else matriz_B

def exibe_matriz(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(" %d" % a[i][j], end = "")
        print("")
    return a

def le_matriz(nome):
    print(f"\nCriando Matriz {nome}")
    linha = int(input("Linhas: "))
    coluna = int(input("Colunas: "))
    matriz = [
        [int(input(f"{nome}[{i}][{j}]: ")) for j in range(coluna)] 
        for i in range(linha)
    ]
    print(f"Sua matriz {nome} é: ")
    for i in range(linha):
        for j in range(coluna):
            print(" %d" % matriz[i][j], end = "")
        print("")
    return matriz

def geramatriz_identidade():
    print("\nInsira o tamanho da matriz identidade")    
    linha = int(input("Número de linhas da matriz identidade: "))
    coluna = int(input("Número de colunas da matriz identidade: "))
    a = [[0 for j in range(coluna)] for i in range(linha)]
    for i in range(linha):
        for j in range(coluna):
            a[i][j] = 1 if i == j else 0
    print("\nMatriz identidade gerada.")
    exibe_matriz(a)
    return a

def soma(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Erro: Matrizes de tamanhos diferentes não podem ser somadas!")
        return None
    c = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] += a[i][j] + b[i][j]
    print("\nA soma da matriz A com a matriz B é: ")
    exibe_matriz(c)
    return c

def minimo(a):
    minimo = a[0][0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] < minimo:
                minimo = a[i][j]
    print("\nO menor elemento da matriz é: ", minimo)
    return minimo

def impar(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] % 2 != 0:
                count += 1
    return count

def maiores(a):
    x = int(input("Digite o valor de x: "))
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > x:
                count += 1
    return count

def media(a):
    soma = 0
    total = len(a) * len(a[0])
    for i in range(len(a)):
        for j in range(len(a[0])):
            soma += a[i][j]
    print("\nA média dos elementos da matriz é: ", soma / total)
    return soma / total

def troca(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Erro: Matrizes de tamanhos diferentes não podem ser trocadas!")
        return None
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j], b[i][j] = b[i][j], a[i][j]
    print("\nMatrizes trocadas.")
    print("Matriz A:")
    exibe_matriz(a)
    print("Matriz B:")
    exibe_matriz(b)
    return a, b

def identidade(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j and a[i][j] != 1:
                print("\nA matriz não é identidade.")
                return False
            elif i != j and a[i][j] != 0:
                print("\nA matriz não é identidade.")
                return False
    print("\nA matriz é identidade.")
    return True

print("* Introdução às matrizes *")
while True:
    escolha = input("Deseja criar duas matrizes A e B ou uma matriz identidade? (Enter para matrizes A e B / i para identidade): ")
    if escolha == 'i':
        while True:
            geramatriz_identidade()
            esc = input("Deseja continuar? (s/n): ")
            if esc == 'n':
                print("Encerrando o programa...")
                break   
    else:
        A = le_matriz("A")
        B = le_matriz("B")
        
        while True:
            print("\nOpções: [s] Soma | [m] Minimo | [i] Impares | [x] Maiores que x | [med] Media | [t] Trocar | [ide] Identidade | [q] Sair")
            
            acoes = {
                'm': minimo,
                'i': impar,
                'med': media,
                't': troca,
                'ide': identidade,
                's': soma,
                'x': maiores,
                'q': None
            }
            choose = input("Escolha: ")

            if choose in acoes:
                if choose == 's':
                    resultado = soma(A, B)
                elif choose == 't':
                    resultado = troca(A, B)
                elif choose == 'q':
                    print("Encerrando...")
                    break
                else:
                    matriz_alvo = escolher_matriz(A, B)
                    funcao = acoes[choose]
                    resultado = funcao(matriz_alvo)
                    print(f"\nResultado da operação : {resultado}")
            else:
                print("Opção inválida.")
            
            inc = input("Deseja continuar com as matrizes A e B? (s/n): ")
            if inc == 'n':
                print("Voltando...")
                break
                
    esc = input("Deseja continuar no programa? (s/n): ")
    if esc == 'n':
        print("Encerrando o programa...")
        break