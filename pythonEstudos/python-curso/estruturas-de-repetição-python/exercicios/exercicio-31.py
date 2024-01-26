soma  = 0
numerador = -1
for denominador in range(1, 101):
    numerador += 2
    soma += numerador / denominador
    resultado = numerador / denominador
    print(f'Soma: {soma}, resultado: {resultado}')
