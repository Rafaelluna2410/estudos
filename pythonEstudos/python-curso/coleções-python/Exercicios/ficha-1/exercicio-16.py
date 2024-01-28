lista = []

for i in range(5):
    lista.append(int(input("valor: ")))

decisao = int(input("digite\n 1 - ordem,\n 2 - inversa"))

while True:
    decisao = int(input("digite: \n 1 - direta,\n 2 - inversa\n"))
    if decisao == 1:
        print(lista)
        break
    elif decisao == 2:
        print(lista[::-1])
        break
    else:
        print("Digite 1 ou 2")
