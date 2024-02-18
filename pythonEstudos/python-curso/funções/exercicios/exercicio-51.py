
### why the last number print is zero after loop for ?

def soma(matriz):

    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if  j == len(matriz)-i-1:
                print(matriz[i][len(matriz)-i-1])
                soma += matriz[i][len(matriz)-i-1]
    return soma

matriz_exemplo = [[2, 3, 6, 1],
                  [4, 4, 2, 6],
                  [4, 4, 4, 6],
                  [6, 3, 4, 1]]

print(soma(matriz_exemplo))
