def multiplicar_impares(n):
    impares =1
    for i in range(1,n+1):
        if i % 2 != 0:
            impares *= i

    return impares


print(multiplicar_impares(5))