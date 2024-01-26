valor = int(input("Digite um valor: "))
for i in range(1, valor):
    if i % 2 == 0:
        print("Procurando primos...")
    elif i % 3 == 0:
        print("Procurando primos...")
    else:
        print(f"Primo: {i}")
