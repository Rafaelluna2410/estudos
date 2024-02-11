def fatorial_quadruplo(n):
    fatorial = 2 * n
    numerador = 1
    for i in range(1, fatorial+1):
        numerador *= i
    
    denominador =1

    for i in range(1, n+1):
        denominador *= i
    
    return f'Resultado: {numerador/denominador}'


print(fatorial_quadruplo(2))