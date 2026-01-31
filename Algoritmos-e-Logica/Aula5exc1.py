def fatorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
def potencia(b,e):
    resultado = 1
    for i in range(e):
        resultado = b * resultado
    return resultado
def produto(a,b):
    resultado = 0
    for i in range(b):
        resultado += a

    return resultado    
def divisao(p, q):
    if q == 0:
        return None
    else:
        resultado = 0
        restante = p
        while restante >= q:
            restante -= q
            resultado += 1
        return resultado
def letra(n):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if 1 <= n <= 26:
        return letras[n - 1]
    else:
        return None
def binario(n):
    if n == 0:
        return "0"
    resultado = ""
    while n > 0:
        resto = n % 2
        resultado = str(resto) + resultado
        n = n // 2
    return resultado