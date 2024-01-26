valor = int(input("Digite um valor: "))
incremento = 0
while incremento < valor:
    incremento += 1
    if incremento %2 != 0:
        print(f"Valores impares: {incremento}")