soma_dos_quadrados = 0
quadrado_da_soma =0
for i in range(11):
   soma_dos_quadrados += i**2
   quadrado_da_soma += i

print(f"Soma dos quadrados: {soma_dos_quadrados} \n quadrado da soma: {quadrado_da_soma**2} \n")
print(f"A diferença de ambos: {(quadrado_da_soma**2) - soma_dos_quadrados}")
