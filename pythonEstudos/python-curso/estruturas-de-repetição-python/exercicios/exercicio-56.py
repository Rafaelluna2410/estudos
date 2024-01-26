valor = 2_000
soma = 0
for i in range(1, valor):
    if i % 2 == 0:
        print("Procurando primos...")
    elif i % 3 == 0:
        print("Procurando primos...")
    else:
        soma += i
        print(f"Primo: {i}, Soma dos primos atual: {soma}")
