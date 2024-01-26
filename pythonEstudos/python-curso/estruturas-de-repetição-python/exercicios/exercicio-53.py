valor = int(input("Digite um valor: "))
numero = 1 
for linha in range(1, valor + 1):
    for coluna in range(1, linha + 1):
        print(numero, end=" ")
        numero += 1
    print()
