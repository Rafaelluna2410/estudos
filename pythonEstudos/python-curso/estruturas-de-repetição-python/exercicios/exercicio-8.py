for i in range(3):
    if i != 0:
        valor = float(input("Digite um valor: "))
        if valor < menor:
            menor = valor 
    else:
        menor = float(input("Digite um valor: "))

print(f"O menor é: {menor}")