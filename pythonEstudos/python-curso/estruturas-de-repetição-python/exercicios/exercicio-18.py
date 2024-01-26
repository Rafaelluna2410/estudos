total = int(input("Digite a quantidade de valores: "))
maior = 0
contador = 0
for i in range(total):
    valor = int(input("Digite um valor: "))
    if i ==0 or valor > maior:
        maior = valor
        contador=1
    elif maior ==valor:
        contador += 1

print(f"Maior: {maior}, vezes: {contador}")
