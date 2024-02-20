"""
raise - lança exceções

É uma palavra reservada igual a def

permite criar exceções e erros personalizados

sintaxe:

raise TipoDoError('Mensagem de erro')

O raisa assim como o return finaliza a função e nada depois dele é executado

#Exemplo

def colore(texto, cor):

    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore(1,'azul')
colore('texto', 2)
colore('texto', 'azul')


# Exemplo refatorado

def colore(texto, cor):
    cores = {'verde', 'amarelo', 'azul', 'branco'}
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A core precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('texto', 'roxo')

"""

#Exemplo

def colore(texto, cor):
    cores = {'verde', 'amarelo', 'azul', 'branco'}
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A core precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('texto', 'roxo')