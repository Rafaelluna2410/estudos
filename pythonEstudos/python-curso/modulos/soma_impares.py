def soma_valores(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7]
    print(soma_valores(lista))

    tupla = (1,2,3,4,5,6,7)
    print(soma_valores(tupla))

else:
    print('o módylo foi importado')