valor = int(input("Digite um valor: "))
for i in range (valor, valor+17):
    if i % 11 == 0 and i != 11:
        print(f"Valor: {i}, multiplo de 11")
        break
    if i % 13 == 0 and i != 13:
        print(f"Valor: {i}, multiplo de 13")
        break
    if i % 17 == 0 and i != 17:
        print(f"Valor: {i},multiplo de 17")
        break
