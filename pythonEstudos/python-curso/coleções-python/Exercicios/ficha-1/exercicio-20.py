vetor_a = []
contador = 0

while True:
    valor = int(input("Digite um valor entre 0 e 50: "))
    if valor >= 0  and  valor <= 50:
        vetor_a.append(valor)
        contador += 1
    else: 
        print("Digite um valor entre 0 e 50")
    
    if contador == 6:
        break 

vetor_impares = []

for itens in vetor_a:
    if itens % 2 != 0:
        vetor_impares.append(itens)

for i in range(0, len(vetor_a), 2):
    print(vetor_a[i], end='')
    if i + 1 <len(vetor_a):
        print(vetor_a[i+1])

for i in range(0, len(vetor_impares), 2):
    print(vetor_impares[i], end="")
    if i +1 < len(vetor_impares):
        print(vetor_impares[i + 1])
