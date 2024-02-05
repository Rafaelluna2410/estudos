def verificar(dado):
    if dado < 0:
        return -1
    elif dado > 0: 
        return +1
    
    return 0

print(verificar(10))