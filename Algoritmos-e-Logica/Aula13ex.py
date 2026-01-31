def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5)) 

def binário(n):
    if n<2: print(n,end='')
    else:
        binário(n//2)
        print(n%2,end='')

binário(504)
print()

def hanói(n,origem,auxiliar,destino):
    if n==0: return
    hanói(n-1,origem,destino,auxiliar)
    print(origem, '->', destino)
    hanói(n-1,auxiliar,origem,destino)

hanói(3,'A','B','C')
print()

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

