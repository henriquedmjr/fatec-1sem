num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
if num1 == num2:
    if num1 % 2 == 0:
        print("Números iguais e pares")
    else:
        print("Números iguais e ímpares")
else:
    print("Números diferentes")
