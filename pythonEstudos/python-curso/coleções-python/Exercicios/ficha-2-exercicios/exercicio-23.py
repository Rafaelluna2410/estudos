matriz_a =[]
matriz_b = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor para A: ")))
    matriz_a.append(linha)



nova_matriz = []
for i in range(2):
    nova_linha = []
    for j in range(2):
        nova_linha.append(matriz_a[i][j] * matriz_a[i][j])
    nova_matriz.append(nova_linha)

print(f"Matriz A: {matriz_a}\n Nova matriz: {nova_matriz}")