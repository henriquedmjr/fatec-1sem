from Aula5ex1 import media
from Aula5ex1 import maximo
from Aula5ex1 import se_par


x = int(input("Digite o número X:   "))
y = int(input("Digite o número Y:   "))
z = int(input("Digite o número Z:   "))
escolha = input("Média, maximo ou se par?(M/Ma/P):   ")
if escolha == "M":
    resultado = media(x,y,z)
    print(f"A média é: {resultado:.2f}")
elif escolha == "Ma":
    resultado = maximo(x,y,z)
    print(f"O máximo é: {resultado}")
elif escolha == "P":
    resultado = se_par(x)
    print(f"O número X é par? {resultado}")