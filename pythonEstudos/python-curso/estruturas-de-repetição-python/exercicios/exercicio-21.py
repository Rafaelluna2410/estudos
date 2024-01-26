valor_a = int(input("Digite o valor A: "))
valor_b = int(input("Digite o valor B: "))
maior = valor_a
menor = valor_b
if valor_b > maior:
    maior = valor_b
    menor= valor_a
pares = 0
impares = 1

if valor_a %2 == 0:
    pares += valor_a
if valor_b % 2 == 0:
    pares += valor_b

for i in range(menor, maior, 1):
    if i % 2 ==0:
        pares += i
    else:
        impares *= i

print(f"Soma dos pares: {pares} \n multiplicação dos impares: {impares}")