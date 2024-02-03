import numpy as np

def gerar_matriz_aleatoria():
    return np.random.randint(1, 10, size=(4, 4))

def encontrar_tres_elementos(matriz, produto_alvo):
    linhas, colunas = matriz.shape

    for i in range(linhas):
        for j in range(colunas):
            if j + 2 < colunas and np.prod(matriz[i, j:j+3]) == produto_alvo:
                return [(i, j), (i, j+1), (i, j+2)]
            
            if i + 2 < linhas and np.prod(matriz[i:i+3, j]) == produto_alvo:
                return [(i, j), (i+1, j), (i+2, j)]

            if i + 2 < linhas and j + 2 < colunas and np.prod(np.diagonal(matriz[i:i+3, j:j+3])) == produto_alvo:
                return [(i, j), (i+1, j+1), (i+2, j+2)]
        
            if i - 2 >= 0 and j + 2 < colunas and np.prod(np.diagonal(np.flipud(matriz[i-2:i+1, j:j+3]))) == produto_alvo:
                return [(i, j+2), (i-1, j+1), (i-2, j)]
    
    return None
 
matriz_aleatoria = gerar_matriz_aleatoria()

produto_alvo = 10

indices = encontrar_tres_elementos(matriz_aleatoria, produto_alvo)

print("Matriz Aleatória:")
print(matriz_aleatoria)

if indices:
    print("\nÍndices dos três elementos cujo produto é 10:")
    print(indices)
else:
    print("\nNão foram encontrados três elementos em qualquer direção cujo produto seja 100.")
