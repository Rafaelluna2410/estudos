def count_pares(vetor):
    pares= 0
    for i in vetor:
        if i % 2 ==0:
            pares += 1
            
    return pares


print(count_pares([2,3,4,6,5,3,2,10,20]))