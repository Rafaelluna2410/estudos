vetor_a = []
vetor_b = []
vetor_c = []
soma_a = 0
soma_b = 0
for i in range(0, 10, 2):
    vetor_a.append(i)
for i in range(10, 25, 3):
    vetor_b.append(i)

for i in range(5):
    vetor_c.append(vetor_a[i] - vetor_b[i])

print(f"Vetor a: {vetor_a}, vetor b: {vetor_b}, vetor c: {vetor_c}")