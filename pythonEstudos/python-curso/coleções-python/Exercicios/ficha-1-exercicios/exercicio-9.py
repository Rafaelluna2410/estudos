lista = []
contador = 0

for i in range(6):
    if contador % 2 == 0:
        lista.append(contador)
    contador += 1
lista.reverse()
print(f"Lista: {lista}")
