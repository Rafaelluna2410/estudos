matriz_aluno = []

for i in range(2):
    colunas = []
    for j in range(5):
        colunas.append(input("Digite a resposta: "))
    matriz_aluno.append(colunas)
    print(f"Aluno: {i}, respostas: {matriz_aluno[i]}")
gabarito = ['c', 'a', 'd', 'b', 'e']

for i in range(len(matriz_aluno)):
    count = 0
    for j in range(len(colunas)):
        if matriz_aluno[i][j] == gabarito[j]:
            count +=1
    
print(f"Gabarito: {gabarito}")