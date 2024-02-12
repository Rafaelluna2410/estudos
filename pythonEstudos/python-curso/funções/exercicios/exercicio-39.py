def troca(a, b):
    valor_first = a
    valor_second = b
    aux = b
    valor_second = a
    valor_first = aux
    
    
    return f"{valor_first}, {valor_second}"


print(troca(2, 3))