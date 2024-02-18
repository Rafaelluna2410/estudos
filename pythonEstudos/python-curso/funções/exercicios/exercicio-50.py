def soma(matriz):

    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i  == j:
                soma += matriz[i][j]
    return soma

matriz_exemplo = [[2, 3, 6, 3],
                  [4, 4, 4, 6],
                  [4, 3, 4, 6],
                  [5, 3, 4, 1]]

print(soma(matriz_exemplo))