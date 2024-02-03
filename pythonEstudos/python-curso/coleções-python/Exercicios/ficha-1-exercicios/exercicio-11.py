lista = []
negativo = 0
pares = 0
for i in range(5):
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    if lista[i] < 0:
        negativo += 1
    elif lista[i] % 2 == 0:
        pares += 1
print(f"Negativos: {negativo}, Pares: {pares}")
