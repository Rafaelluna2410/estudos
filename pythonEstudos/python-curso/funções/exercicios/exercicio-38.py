def fatorial_exponencial(n):
    fatorial_first = n-2
    fatorial_second = (n-1) ** fatorial_first
    resultado = n ** fatorial_second
    
    return resultado


print(fatorial_exponencial(4))