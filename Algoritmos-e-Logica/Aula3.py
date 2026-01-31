prod = float(input("Digite o numero do produto:  "))
quant = int(input("Digite a quantidade:  "))
if prod == 1:
    prc = 5.00
elif prod == 2:
    prc = 3.50
elif prod == 3:
    prc = 4.80
elif prod == 4:
    prc = 8.90
elif prod == 5:
    prc = 7.32
else:
    print("Produto nao existente")
    prc = 0
total = prc * quant
print("O total a pagar é: R$ %.2f" % total)
