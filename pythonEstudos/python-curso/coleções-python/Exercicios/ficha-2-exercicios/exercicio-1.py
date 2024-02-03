matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append((i * 4 + j) * 10)
    matriz.append(linha)

for linha in matriz:
    print(linha)

contador = sum(1 for linha in matriz for elemento in linha if elemento > 10)
print(f'Valores maiores que 10: {contador}')
