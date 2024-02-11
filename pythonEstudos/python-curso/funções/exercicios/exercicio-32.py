def simplifica(numerador, denominador):
    maior = numerador 

    if denominador > numerador:
        maior = denominador
    maior_divisor= 1

    for i in range(1, maior +1):

        if numerador % i == 0 and denominador % i == 0:
            maior_divisor = i
    

    return f'{(numerador/maior_divisor)} / {(denominador / maior_divisor)}'


print(simplifica(36, 60))