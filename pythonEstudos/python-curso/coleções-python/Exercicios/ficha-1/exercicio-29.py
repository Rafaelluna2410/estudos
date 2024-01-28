lista = []

for i in range(10, 20, 1):
    lista.append(i)

pares_soma = 0
pares_lista = []
impares_count = 0
impares_lista = []

for i in range(len(lista)):
    if lista[i] % 2 ==0:
        pares_soma += lista[i]
        pares_lista.append(lista[i])
    else:
        impares_lista.append(lista[i])
        impares_count +=1
    
print(f"Pares digitados: {pares_lista}, soma dos pares: {pares_soma}")
print(f"Impares digitados: {impares_lista}, quantidade de impares: {impares_count}")