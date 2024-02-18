"""
Listas aninhadas
    unidimensionas array/vetores
    Multidimensionais matrizes

Em python há listas

listas = [[1,2,3], [4,5,6], [7,8,9]] # Matriz 3x3

print(listas[0][1])

for lista in listas:
    for num in lista:
        print(num)

        #List compreehension

listas = [[1,2,3], [4,5,6], [7,8,9]] # Matriz 3x3

[[print(valor) for valor in lista] for lista in listas]

"""


# Gerando um tabulerio 

tabuleiro = [[numero for numero in range(1,4)]for valor in range(1,4)]

print(tabuleiro)


# Gerando jogadas para o jogo da velha
velha = [['x' if numero %2 ==0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

# Gerando valor iniciais

print([['*' for i in range(1,4) for j in range(1,4) ]])

