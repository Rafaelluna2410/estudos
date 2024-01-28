numero_aluno = []
altura_aluno = []

for i in range(11, 15):
    numero_aluno.append(i)
for i in range(1,5):
    altura_aluno.append(i*10)
print(f"Numero dos alunos: {numero_aluno}\n Altura dos alunos: {altura_aluno}")
    
print(f"Maior aluno: {max(altura_aluno)}, numero do aluno: {numero_aluno[altura_aluno.index(max(altura_aluno))]} ")
print(f"Menor aluno: {min(altura_aluno)}, numero do aluno: {numero_aluno[altura_aluno.index(min(altura_aluno))]}")