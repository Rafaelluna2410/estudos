
linhas = 10
colunas = 10

matriz = [[0 for j in range(colunas)] for i in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        if i < j:
            matriz[i][j] = 2 * i + 7 * j
        elif i == j:
            matriz[i][j] = 3 * i + 7 * j
        else:
            matriz[i][j] = 4 * i + 7 * j


for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end="\t")
    print()

