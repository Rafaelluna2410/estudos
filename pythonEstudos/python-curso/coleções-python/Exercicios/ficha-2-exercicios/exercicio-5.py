matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(i +4)
    matriz.append(linha)
valor = int(input("Insira um valor: "))
flag = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == valor:
            flag = True

for linha in matriz:
    print(linha)

if flag == True:
    print("Valor encontrado")
else:
    print("Valor não encontrado")