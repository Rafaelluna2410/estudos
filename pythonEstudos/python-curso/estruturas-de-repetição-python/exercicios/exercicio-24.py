valor = int(input("Digite um valor: "))
soma  = 0
for i in range(1, valor):
    if valor % i == 0:
        soma += i
print(f"Resultado da soma: {soma}")