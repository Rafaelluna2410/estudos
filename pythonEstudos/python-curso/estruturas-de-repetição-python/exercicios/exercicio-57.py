inicio = int(input("Valor inicial: "))
fim = int(input("Valor final: "))
soma = 0
for i in range(inicio, fim):
    if i % 2 == 0:
        print("Procurando primos...")
    elif i % 3 == 0:
        print("Procurando primos...")
    else:
        soma += 1
print(f"Quantida de primos:  {soma}")
