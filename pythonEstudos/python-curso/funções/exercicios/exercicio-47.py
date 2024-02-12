'''
def valores_maiores(*args):

    count_maiores =0
    for linha in range(len(args)):
        for coluna in range(len(args)):
            if args[linha][coluna] > 3:
                count_maiores += 1
    
    return count_maiores

print(valores_maiores([2, 3, 4, 2],[2, 3, 4, 5],[2, 3, 4, 6],[2, 3, 4, 1]))
'''

def valores_maiores(vetor):

    count_maiores =0
    for linha in range(len(vetor)):
        for coluna in range(len(vetor)):
            if vetor[linha][coluna] > 3:
                count_maiores += 1
    
    return count_maiores

matriz = [[2, 3, 4, 2],[2, 3, 4, 5],[2, 3, 4, 6],[2, 3, 4, 1]]
print(valores_maiores(matriz))


