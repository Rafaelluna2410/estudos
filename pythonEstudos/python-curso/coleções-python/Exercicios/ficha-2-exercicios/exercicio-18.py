lista = [[5, -8, 10], [1, 2, 15], [25, 10, 7]]
novo = []
for i in range(3):
    soma = 0
    for j in range(3):
        soma += lista[j][i]
    novo.append(soma)

print(f"Antigo: {lista},\n novo: {novo}")
