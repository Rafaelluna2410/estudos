def triangulo(n):
    desenho = ''
    simbolo = '*'
    espaco = ' '

    for i in range(1, n + 1):
        desenho += espaco * (n - i) + (simbolo * (2 * i - 1)) + '\n'

    return desenho


print(triangulo(6))
