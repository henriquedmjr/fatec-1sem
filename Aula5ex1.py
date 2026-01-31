def media(a,b,c):
    return (a + b + c) / 3

def maximo(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
def se_par(num):
    if num % 2 == 0:
        return True
    else:  
        return False

