lista = []

for i in range(5):
    lista.append(int(input("Valor: ")))

print(f"Lista antiga: {lista}")

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0   
print(f"Lista nova: {lista}")