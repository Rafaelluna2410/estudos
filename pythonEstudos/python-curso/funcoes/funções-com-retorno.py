'''
Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()
print(ret)
print(numeros)

OBS: quando n retorna nenhum valor, o retorno é none
OBS: para retornar usa a palavra reservada return

def quadrado_de_7():
    return 7*7

ret = quadrado_de_7()
print(ret)

# ou

print(f"Retorno {quadrado_de_7()}")

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função 
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

exemplo-1

def diz_oi():
    return 'OI'
    print('dps do return') # após o return nada é executado

exemplo-2

def diz_oi():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 2
    
    return 'b'
    
exemplo-3

def outra_funcao():
    return 2,3,4,5


num1,num2,num3,num4, = outra_funcao()

print(num1, num2, num3, num4)

# ou

print(outra_funcao())


# Cria uma função de jogar a moeda

from random import random

def joga_moeda():
    if random() > 0.5:
        return 'cara'
    return 'Coroa'

print(joga_moeda())

'''


