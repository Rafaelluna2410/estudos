matriz = []
contador = 1
for i in range (4):
    linha = []
    for j in range(4):
        linha.append(contador)
        contador+=1
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i in range(len(matriz)):
    for j in range(i + 1, len(matriz[i])):
        matriz[i][j] = 0
    
for linha in matriz:
    print(linha)
