def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        chute = lista[meio]

        if chute == alvo:
            return True, meio, lista[meio]
        elif chute > alvo:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return False

minha_lista = [1, 3, 5, 7, 9]
print(busca_binaria(minha_lista, 3))  

def bubble_sort(v,  n):
    if n == 1:
        return
    for i in range(n - 1):
        if v[i] > v[i + 1]:
            v[i], v[i + 1] = v[i + 1], v[i]
        print(v)    
    bubble_sort(v, n - 1)

a = [24, 3, 45, 29, 15, 8]
def bubble_sort(v,  n):
    if n == 1:
        return
    for i in range(n - 1):
        if v[i] > v[i + 1]:
            v[i], v[i + 1] = v[i + 1], v[i]
        print(v)    
    bubble_sort(v, n - 1)

bubble_sort(a, len(a))
