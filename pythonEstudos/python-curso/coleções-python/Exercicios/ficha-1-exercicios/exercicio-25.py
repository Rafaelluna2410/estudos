lista = []

for i in range(100):
    if i % 7 != 0 and i % 10 != 7:
        lista.append(i)
print(f"Sem multiplos de 7: {lista}")