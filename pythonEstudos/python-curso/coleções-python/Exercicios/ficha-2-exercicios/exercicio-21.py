matriz_a = []
matriz_b = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor para A: ")))
    matriz_a.append(linha)


for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor para B: ")))
    matriz_b.append(linha)

while True:
    print("Escolha: ")
    valor = int(input(" 1 - somar duas matrizes\n 2 - subtrair a primeira matriz da segunda\n 3 - adicionar uma constante as duas matrizes\n 4 - imprimir as matrizes\n 5 - para sair\n "))

    if valor == 1:
        nova_matriz = []
        for i in range(2):
            nova_linha = []
            for j in range(2):
                nova_linha.append(matriz_a[i][j] + matriz_b[i][j])
            nova_matriz.append(nova_linha)
        print(f"A matriz após somada: {nova_matriz}")

    elif valor == 2:
        nova_matriz = []
        for i in range(2):
            nova_linha = []
            for j in range(2):
                nova_linha.append(matriz_a[i][j] - matriz_b[i][j])
            nova_matriz.append(nova_linha)
        print(f"A matriz após somada: {nova_matriz}")

    elif valor == 3:
        print(f"Constante")

    elif valor == 4:
        print(f"Matriz A: {matriz_a}, \n Matriz B: {matriz_b}")

    elif valor == 5:
        print("Saiu")
        break
    else:
        print("Digite um valor válido")        
