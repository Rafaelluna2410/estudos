lista = []

for i in range(20):
    lista.append(i)

for i in range(len(lista)):
    if lista[i] %2 !=0 and lista[i] %3 !=0:
        print(f"Primo: {lista[i]}")