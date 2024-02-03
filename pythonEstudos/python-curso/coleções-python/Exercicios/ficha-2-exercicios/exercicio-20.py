matriz = []
count = 0
for i in range(3):
    linha = []
    for j in range(6):
        linha.append(count)
        count += 1
    matriz.append(linha)

print(f"Matriz original: {matriz}")


for i in range(3):
    impares_soma = 0
    for j in range(1, 6, 2):
        impares_soma += matriz[i][j]
    print(f"soma das colunas impares: {impares_soma}, linha: {i}")

for i in range(3): 
    soma_media = 0 
    for j in range(1,4,2):
        soma_media += matriz[i][j]
    print(f"Média aritmética da coluna 2 e 4 da linha: {i}, média: {soma_media/2}")



for i in range(3):
    matriz[i][5] = matriz[i][0] + matriz[i][1]
print(f"Matriz modificada: {matriz}")