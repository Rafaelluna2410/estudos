matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append((i + 4))
    matriz.append(linha)

for linha in matriz:
    print(linha)

mult = 1
for i in range(5):
    mult *= matriz[i][i]

print(f"Diagonal: {mult}")