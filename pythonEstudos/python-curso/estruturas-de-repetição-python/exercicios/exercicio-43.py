contador = 0
soma = 0 
while True:
    idade = int(input("Digite a idade em anos: "))
    if idade == 0 and contador !=0:
        print(f"Média: {media}, idades lidas: {contador}")
        break
    if idade == 0 and contador ==0:
        print("Finalizado")
        break
    if idade > 0:
        contador +=1
        soma += idade
        media = soma / contador
    else:
        print("Digite valores maiores que zero ")

