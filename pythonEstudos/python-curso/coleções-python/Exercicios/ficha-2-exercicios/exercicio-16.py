matriz_aluno = []

loop_alunos = 0
loop_colunas = 0

while True:

    if loop_alunos == 2:
        break

    linha = []
    if loop_colunas == 0:
        while True:
            matricula = input("Digite a matricula de 3 digitos: ")
            if len(matricula) != 3:
                print("A matricula tem menos caracteres")
            else:
                linha.append(matricula)
                loop_colunas += 1
                break
    
    for i in range(5):
        linha.append(input("Digite a resposta: "))
        loop_colunas += 1
    
    matriz_aluno.append(linha)
    loop_colunas = 0
    loop_alunos +=1

gabarito = ['a', 'e', 'c', 'b', 'd']
for i in range(len(matriz_aluno)):
    acertos = 0
    for j in range(len(matriz_aluno[0])-1):
        if matriz_aluno[i][j+1] == gabarito[j]:
            acertos += 1
    print(f"Aluno: {matriz_aluno[i][0]} Acertos: {acertos} respostas: {matriz_aluno[i]}")
print(f"Gabarito: {gabarito}")