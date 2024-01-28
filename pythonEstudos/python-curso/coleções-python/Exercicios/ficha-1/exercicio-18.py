lista = []
contador = 0
for i in range(10):
    lista.append(contador)
    contador +=1

x = int(input("Digite x: "))
mult = 0
for i in lista:
    if lista[i] % x:
        mult += 1

print(f"Mult count: {mult}")
