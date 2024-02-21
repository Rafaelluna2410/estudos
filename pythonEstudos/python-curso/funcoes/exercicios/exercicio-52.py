def transposta(matriz):

    matriz_transposta = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            matriz_transposta[j][i]= matriz[i][j]

    return matriz_transposta


matriz_exemplo = [[2, 3],
                  [4, 4],
                  [4, 4],
                  [6, 3]]
print(matriz_exemplo)
print(transposta(matriz_exemplo))