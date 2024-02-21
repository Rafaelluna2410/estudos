def maior(vetor):

    maior = 0
    for i in vetor:
        if i > maior:
            maior = i
    
    return maior


print(maior([2,3,4,60,5,3,2,10,20]))