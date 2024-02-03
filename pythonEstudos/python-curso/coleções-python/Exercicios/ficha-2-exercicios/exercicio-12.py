matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(i + 4 + 2)
    matriz.append(linha)

transposta = [[0 for j in range(len(matriz))] for i in range(len(matriz[0]))]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        transposta[j][i] = matriz[i][j]

print("\nMatriz Transposta:")
for row in transposta:
    print(row)