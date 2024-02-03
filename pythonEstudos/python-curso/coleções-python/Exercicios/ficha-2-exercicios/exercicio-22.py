matriz_a =[]
matriz_b = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor para A: ")))
    matriz_a.append(linha)


for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor para B: ")))
    matriz_b.append(linha)

nova_matriz = []
for i in range(2):
    nova_linha = []
    for j in range(2):
        nova_linha.append(matriz_a[i][j] * matriz_b[j][i])
    nova_matriz.append(nova_linha)

print(f"Matriz A: {matriz_a}\n Matriz B: {matriz_b}\n Nova matriz: {nova_matriz}")