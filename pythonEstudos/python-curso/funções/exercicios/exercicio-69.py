def calculadora(numerador, denominador):

    maior = numerador
    if denominador> maior:
        maior = denominador

    for i in range(1, maior, 1):

        if numerador % i == 0 and denominador % i == 0:
            maximo_divisor = i

    return maximo_divisor

numerador  = 15
denominador = 30

print(calculadora(numerador, denominador))