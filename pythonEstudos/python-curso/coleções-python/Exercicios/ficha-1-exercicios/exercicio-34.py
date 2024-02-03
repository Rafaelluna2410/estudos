lista = []

contador = 0

while True:
    valor = int(input("Digite um valor sem repetir: "))
    flag = True
    for i in range(len(lista)):
        if lista[i] == valor:
            flag = False
    
    if flag:
        lista.append(valor)
        contador +=1
    else:
        print("Esse valor já foi digitado")
    if contador == 5:
        print(f"Valores: {lista}")
        break