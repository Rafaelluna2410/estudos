def triangulo(n):
    largura = 2 *n -1
    sinal = '*'
    desenho = ''

    for i in range(largura + 1):
        if i > n:
            desenho += (largura-i+1) * sinal + '\n'
        else:
            desenho += sinal * i + '\n'
        
    
    return desenho


print(triangulo(5))