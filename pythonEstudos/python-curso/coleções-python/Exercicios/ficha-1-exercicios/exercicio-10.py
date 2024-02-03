lista = []
contador = 0
soma = 0
for i in range(15):
    lista.append(contador)
    soma += lista[i]
    contador += 1

print(f"soma: {soma}, numero de notas: {len(lista)}, média: {soma / len(lista)}")
