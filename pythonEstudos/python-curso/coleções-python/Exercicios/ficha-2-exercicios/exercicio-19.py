matriz_aluno = []

linha = 0
coluna = 0
count_aluno = 0
maior = 0
aluno = 0

while True:

    if count_aluno == 2:
        soma_finais = 0
        for i in range(2):
            soma_finais += matriz_aluno[i][3]

        media_finais = soma_finais / count_aluno
        break

    linha = []
    if coluna == 0:
        matricula = int(input("Digite a matricula: "))
        linha.append(matricula)
        coluna += 1


    for i in range(2):
        nota = int(input("Digite a nota: "))
        linha.append(nota)
        coluna += 1
    linha.append((linha[1] + linha[2]) / 2)
        
    matriz_aluno.append(linha)

    if linha[3] > maior:
        maior = linha[3]
        matricula_aluno = linha[0]

    coluna = 0
    count_aluno +=1
print(f"{matriz_aluno[0]}\n {matriz_aluno[1]}")
print(f"Maior media: {maior}, aluno com a maior média: {matricula_aluno}\n média das finais: {media_finais}")

