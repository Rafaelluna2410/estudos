def quantidade_primos(valor):

    count_primos = 0
    for i in range(valor+1):
        if i == 2 or i == 3:
            count_primos +=1
        if i % 2 != 0 and i % 3 !=0:
            count_primos +=1    
    return count_primos

print(quantidade_primos(13))


