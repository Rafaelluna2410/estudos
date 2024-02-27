def meu_for(valores):
    it = iter(valores)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

#test = [1,2,3,4,5,6]
nome = 'rafeal'

#meu_for(test)
meu_for(nome)