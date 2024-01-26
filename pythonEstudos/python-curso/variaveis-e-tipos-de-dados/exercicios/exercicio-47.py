numero = int(input("Digite um valor entre 1000  e 9999: "))

if numero >= 1000 and numero <= 9999:
    for valor in str(numero):
        print(valor)
else:
    print("Digite um valor entre 1000 e 9999")

