lista = []
contador = 0
for i in range(5):
    lista.append(contador)
    contador += 1

print(f"Max: {max(lista)}, Min: {min(lista)},\nmed: {sum(lista)/len(lista)}, lista: {lista}")

