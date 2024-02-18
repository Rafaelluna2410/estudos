def soma_valores(vetor):
 #valores encima da diagona secundária
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


'''
def soma_acima_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j > i:
                soma += matriz[i][j]
    return soma

# Exemplo de matriz
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = soma_acima_diagonal(matriz_exemplo)
print("A soma dos valores acima da diagonal principal é:", resultado)


'''