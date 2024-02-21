def fator_primo(valor):
    maior = 0
    for i in range(valor +1): 
        if i % 2 !=0 and i % 3 !=0:
            maior = i

    return maior

print(fator_primo(19))