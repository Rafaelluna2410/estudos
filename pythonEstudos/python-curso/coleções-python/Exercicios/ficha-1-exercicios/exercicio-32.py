lista_a = [2, 4, 10, 14, 44]
lista_b = [2, 55, 44, 3, 9]

lista_somados = []
lista_mult = []
for i in range(len(lista_a)):
    lista_somados.append(lista_a[i] + lista_b[i])
    lista_mult.append(lista_a[i] * lista_b[i])

conjnto_a = set(lista_a)
conjnto_b = set(lista_b)
print(f"Soma: {lista_somados}\n mult: {lista_mult}")
print(f"Diferença de x em y: {conjnto_a.difference(conjnto_b)}")
print(f"Interseção: {conjnto_a.intersection(conjnto_b)}")
print(f"União: {conjnto_a.union(conjnto_b)}")
