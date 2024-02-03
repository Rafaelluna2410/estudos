lista_a = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    lista_a.append(valor)

lista_b = []
for i in range(len(lista_a)):
    valor = lista_a[i] **2
    lista_b.append(valor)

print(lista_a, lista_b)
