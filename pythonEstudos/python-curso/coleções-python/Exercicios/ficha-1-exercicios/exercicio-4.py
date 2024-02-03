lista = []
incremento = 0
for i in range(8): 
    incremento +=1
    lista.append(incremento)
    

x = int(input("Digite um valor entre 0 e 7: "))
y = int(input("Digite um valor entre 0 e 7: "))

print(f"Lista: {lista}")
print(f"Soma dos valores: {lista[x] + lista[y]}")

