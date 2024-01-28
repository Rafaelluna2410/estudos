lista = []

for i in range(5):
    valor = int(input("Insira um valor: "))
    lista.append(valor)

lista_iguais = []
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] == lista[j] and lista[i] not in lista_iguais:
            lista_iguais.append(lista[i])
print(lista_iguais)
