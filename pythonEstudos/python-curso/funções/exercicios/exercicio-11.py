def media(tipo, *args):
    if tipo == 'A':
        soma = 0
        for numero in args:
            soma += numero
        return soma / len(args)
    elif tipo == 'P':
        pesos = (5, 3, 2)
        if len(args) != len(pesos):
            return 'A quantidade de notas está errada'
        soma = 0 
        for index, nota in enumerate(args):
            soma += nota * pesos[index]
        return soma / len(args)


print(media('P', 10,3,2))
