def soma_valores(vetor):

    soma= 0
    for i in range(0, len(vetor)):
        for j in range(len(vetor[i])-i-1):
                soma += vetor[i][j]
    
    return soma

matriz = [[2, 3, 6, 3],
          [4, 4, 4, 5],
          [4, 3, 4, 6],
          [5, 3, 4, 1]]
print(soma_valores(matriz))