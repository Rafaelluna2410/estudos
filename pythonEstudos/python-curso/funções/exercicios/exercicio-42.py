def media(vetor):
    soma = 0
    for i in vetor:
        soma  += i

    return soma / len(vetor)

print(media([2,3,4]))