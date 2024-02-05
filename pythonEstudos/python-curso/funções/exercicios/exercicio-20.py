def fatorial(valor):
    fatorial = 1
    for i in range(1, valor+1):
        fatorial *= i

    return fatorial

print(fatorial(5))