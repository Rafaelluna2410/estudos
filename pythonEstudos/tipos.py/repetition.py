#fim = int(input("digite n\n"))
#x=0
#while x <=fim:
#    print(x)
#    x +=1

##apenas numeros pares
#par = int(input("digite par \n"))
#
#x =1
#
#while x <=par:
#    if x % 2 == 0:
#        print(x)
#
#    x +=1

##apenas numeros divisiveis por 3
#mult = int(input("digeite n: \n"))
#x=1
#
#while x<= mult:
#    if x %3 ==0:
#        print(x)
#    x+=1

##media aritmética

#notas = int(input("digite o numero de notas: \n"))
#x=0
#soma=0
#
#while x <notas:
#
#    valor = float(input("digite n: \n"))
#    soma += valor
#    x +=1
#    
#print(soma)


##Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma 
##poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período. 
#soma=0
#mes=0
#deposito = float(input("valores\n"))
#juros = float(input("juros em % \n"))
#x =1
#while x<24:
#    calculo = deposito * (1+juros/100)
#    soma +=  calculo
#    print(soma)
#    x +=1
#
#print(soma)

#Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal. Pergunte o valor mensal que será pago. 
#Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

#inicial = float(input("valor: \n"))
#juros = float(input("juros \n"))
#pago = float(input("valor a ser pago \n"))
#
#x= 0
#totalJuros = 0
#
#while inicial > 0:
#
#    inicial = inicial * (1+juros/100)
#    totalJuros += (inicial * (juros/100))
#    inicial -= pago
#    x +=1
#
#inicial += pago
#
#print("meses para quitar: \n ", x)
#print("total de juros pagao: \n ",  totalJuros)
#print("total pago: \n", inicial)


#x = 0
#soma = 0
#
#while True:
#    valor = int(input("digite: \n"))
#    if valor ==0:
#        break
#    soma += valor
#    x +=1
#
#resultado = soma / x
#
#print(resultado)








