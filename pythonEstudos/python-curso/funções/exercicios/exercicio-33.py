def soma(n):
    valor = str(n)
    soma = 0
    for i in range (len(valor)):
        soma += int(valor[i])

    return soma

print(soma(243))