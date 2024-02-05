def soma(a, b):
    soma = 0

    for i in range(a+1, b):
        soma += i
    return soma

print(soma(1,4))