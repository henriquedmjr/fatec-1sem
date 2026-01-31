prc = float(input("Digite o preço do produto: R$ "))
qtd = int(input("Digite a quantidade comprada: "))
total = prc * qtd
if total > 200:
    dop = input("Desconto (D) de 5 porcento ou parcelar (P)?")
    if dop == "D":
        total = total * 0.95
        print(f"Total a pagar com desconto: R$ {total:.2f}")
    else:
        parc = int(input("Em quantas vezes deseja parcelar? "))
        total = total / parc
        print(f"Total a pagar em {parc} vezes de: R$ {total:.2f}")
else:
    print(f"Total a pagar: R$ {total:.2f}")
