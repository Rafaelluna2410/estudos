valor = int(input("Digite um valor: "))
soma = 1

for i in range(1, valor+1):
    mult = 1
    for j in range(1, i+1):
        mult *= j
    soma += i/mult
print(f"E = {soma}")    

