def desenho(valor):    
    simbolo = '!'
    desenho = ''
    for i in range(valor +1):
        desenho += simbolo * i + '\n'
    return desenho
    
print(desenho(5))