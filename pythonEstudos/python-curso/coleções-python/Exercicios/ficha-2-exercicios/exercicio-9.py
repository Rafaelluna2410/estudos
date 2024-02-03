matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(i + 4 + 2)
    matriz.append(linha)


for linha in matriz:
    print(linha)

soma = 0
for i in range(len(matriz)):
    for j in range(i):
        soma += matriz[i][j]

print(soma)