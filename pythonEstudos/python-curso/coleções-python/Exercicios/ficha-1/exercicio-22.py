vetor_a = []
vetor_b = []
vetor_c = []
for i in range(10):
    vetor_a.append(i)
    vetor_b.append(i+3)

for i in range(10):
    if i % 2 !=0:
        vetor_c.append(vetor_a[i])
    else:
        vetor_c.append(vetor_b[i])

print(vetor_a)
print(vetor_b)
print(vetor_c)
