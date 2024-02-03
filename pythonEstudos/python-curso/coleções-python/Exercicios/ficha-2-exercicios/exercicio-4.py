matriz =[]

for i in range(4):
    linha = []
    for j in range(4):
        linha.append((i * 4 + j) * 10)
    matriz.append(linha)

maior = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

for i in matriz:
    print(i)
print(f"Maior: {maior}")