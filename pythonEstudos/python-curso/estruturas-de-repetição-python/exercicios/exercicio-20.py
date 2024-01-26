contador_valores =0
pares = 0
while True:
    valor = int(input("Digite um valor: "))
    contador_valores += 1
    if valor % 2 == 0 and valor != 1000:
        pares += 1
    if valor == 1000:
        break

print(f"Valores pares: {pares}\n dados lidos: {contador_valores}")