def imparess_pares(vetor):
    vetor_pares = []
    vetor_impares = []

    for elemento in vetor:
        if elemento %2 ==0:
            vetor_pares.append(elemento)
        else:
            vetor_impares.append(elemento)


    return f'Pares: {vetor_pares}, impares: {vetor_impares}'


print(imparess_pares([2, 3, 4, 2, 5]))