resultado= 0
for i in range(3):
    valor = int(input("Digite um valor: ")) 
    resultado += valor

print(f"({i})")
print(f"A média é: {resultado/(i+1)}")