prc = float(input("Digite o preço do produto: R$ "))
qtd = int(input("Digite a quantidade comprada: "))
total = prc * qtd
if total > 200:
    dop = input("Desconto (D) de 5 porcento ou parcelar (P) em 4 vezes?")
    if dop == "D":
        total = total * 0.95
        print(f"Total a pagar com desconto: R$ {total:.2f}")
    else:
        total = total / 4
        print(f"Total a pagar em 4 vezes de: R$ {total:.2f}")
else:
    print(f"Total a pagar: R$ {total:.2f}")
