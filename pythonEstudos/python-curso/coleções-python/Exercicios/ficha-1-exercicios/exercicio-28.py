vetor_x = []
vetor_a = []
vetor_b = []

for i in range(10, 20, 1):
    vetor_x.append(i)

for i in range(len(vetor_x)):
    if vetor_x[i] % 2 != 0:
        vetor_a.append(vetor_x[i])
    else:
        vetor_b.append(vetor_x[i])
print(f"imapares: {vetor_a}, pares: {vetor_b}")