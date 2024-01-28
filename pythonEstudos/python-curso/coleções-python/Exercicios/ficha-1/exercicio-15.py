lista = []

for i in range(5):
    lista.append(int(input("Valor: ")))


nova_lista = []
for elemento in lista:
    if elemento  not in nova_lista:
        nova_lista.append(elemento)

print(f"lista: {nova_lista}")
