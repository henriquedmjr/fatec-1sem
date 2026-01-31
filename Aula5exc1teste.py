from Aula5exc1 import potencia 
from Aula5exc1 import fatorial
from Aula5exc1 import produto   
from Aula5exc1 import divisao
from Aula5exc1 import letra
from Aula5exc1 import binario

func = int(input("Qual função executar? 1 - potencia, 2 - fatorial, 3 - produto, 4 - divisao, 5 - letra, 6 - binario, 7 - senha: "))
if func == 1:
    b = int(input("Digite a base: "))
    e = int(input("Digite o expoente: "))
    resultado = potencia(b,e)
    print(f"O resultado de {b} elevado a {e} é: {resultado}")
if func == 2:
    n = int(input("Digite um número para calcular o fatorial: "))
    resultado_fatorial = fatorial(n)
    print(f"O fatorial de {n} é: {resultado_fatorial}")

if func == 3:
    a = int(input("Digite um número: "))
    b = int(input("Digite quantas vezes multiplicar: "))
    resultado_produto = produto(a,b)
    print(f"O produto de {a} multiplicado por {b} é: {resultado_produto}")

if func == 4:
    p = int(input("Digite o dividendo: "))
    q = int(input("Digite o divisor: "))   
    resultado_divisao = divisao(p, q)
    print(f"O resultado da divisão de {p} por {q} é: {resultado_divisao}")

if func == 5:
    n = int(input("Digite um número para obter a letra correspondente: "))
    resultado_letra = letra(n)
    if resultado_letra:
        print(f"A letra correspondente ao número {n} é: {resultado_letra}")
    else:
        print("Número inválido. Digite um número entre 1 e 26.")
if func == 6:
    n = int(input("Digite um número para converter em binário: "))
    resultado_binario = binario(n)
    print(f"O número {n} em binário é: {resultado_binario}")
if func == 7:
    b = int(input("Digite a base: "))
    e = int(input("Digite o expoente: "))
    resultado = potencia(b,e)
    n = int(input("Digite um número para calcular o fatorial: "))
    resultado_fatorial = fatorial(n)
    a = int(input("Digite um número: "))
    b = int(input("Digite quantas vezes multiplicar: "))
    resultado_produto = produto(a,b)
    p = int(input("Digite o dividendo: "))
    q = int(input("Digite o divisor: "))   
    resultado_divisao = divisao(p, q)
    n = int(input("Digite um número para obter a letra correspondente: "))
    resultado_letra = letra(n)
    n = int(input("Digite um número para converter em binário: "))
    resultado_binario = binario(n)
    senha_n = int((resultado_fatorial / resultado_produto) + resultado)
    let = int(senha_n // 26)
    if resultado_letra == letra(resultado_divisao):
        senha_a = resultado_letra + letra(let)
        senha_b = (binario(senha_n) + resultado_binario)
        senha_f = senha_a + senha_b
        if senha_f == "HE10011000101100100":
            print("Senha correta! Acesso liberado.")
            acessar = True
            while acessar:
                acc = int(input("Qual dado quer acessar? 1- Email, 2- Telefone, 3 - CPF, 4 - Dinheiro ou 5 - Sair: "))
                if acc == 1:
                    print("Email e senha = xxxxxxxxxxxx@gmail.com = xxxxxxx")  
                elif acc == 2:
                    print("Telefone = (xx) xxxxx-xxxx")
                elif acc == 3:
                    print("CPF = XXX.XXX.XXX-XX")
                elif acc == 4:
                    print("Dinheiro = R$ 623,00")
                elif acc == 5:
                    print("Adeus!")
                    acessar = False
                    break
                else:
                    print("Dado inválido!")
                    continue
                con = int(input("Acessar mais algum dado? 1 - sim, 2 - não: "))
                if con != 1:
                    print("Adeus!")
                    acessar = False
    else:
            print("Senha incorreta! Acesso negado.")