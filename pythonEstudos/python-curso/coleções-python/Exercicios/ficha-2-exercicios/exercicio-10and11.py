matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(i + 4 + 2)
    matriz.append(linha)

for linha in matriz:
    print(linha)

soma = 0
diagonal_secundaria = 0
for i in range(len(matriz)):
    soma += matriz[i][i]
    diagonal_secundaria += matriz[i][len(matriz) - 1 - i]

print(soma)
print(diagonal_secundaria)