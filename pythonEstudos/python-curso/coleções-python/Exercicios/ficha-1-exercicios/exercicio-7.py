lista = []
contador = 0 

for i in range(10):
    lista.append(contador)
    contador += 10

print(f"Max: {max(lista)} indice: {lista.index(max(lista))}")

