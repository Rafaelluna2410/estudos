lista = []
contador = 0
pares = 0
for i in range(10):
    lista.append(contador)
    contador +=1
    if lista[i] % 2 == 0:
        pares +=1

print(f"Lista: {lista}")
print(f"Pares: {pares}")

