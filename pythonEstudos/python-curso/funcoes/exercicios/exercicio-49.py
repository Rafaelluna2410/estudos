def soma_abaixo_diagonal_secundaria(matriz):
    soma = 0
    tamanho = len(matriz)
    for i in range(tamanho):
        for j in range(tamanho):
            if i + j > tamanho-1:
                soma += matriz[i][j]
    return soma

matriz_exemplo = [[2, 3, 6, 3],
                  [4, 4, 4, 6],
                  [4, 3, 4, 6],
                  [5, 3, 4, 1]]

resultado = soma_abaixo_diagonal_secundaria(matriz_exemplo)
print("A soma dos valores abaixo da diagonal secundária é:", resultado)


'''
def soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j < i:
                soma += matriz[i][j]
    return soma

matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = soma_abaixo_diagonal(matriz_exemplo)
print("A soma dos valores abaixo da diagonal principal é:", resultado)

'''