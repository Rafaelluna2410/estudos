soma =0 
incremento =0
for i in range(3):
    valor = int(input("Digite um valor: "))
    if valor > 0:
        soma += valor
        incremento += 1
    
print(f"Resultado: {soma/incremento}")