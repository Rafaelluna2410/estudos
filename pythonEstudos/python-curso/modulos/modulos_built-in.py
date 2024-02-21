'''
- Em python, modulos são outros arquivos em Python

Exemplo:
Modulo random -> Possui várias funções para geração de números pseudo-aleatórios

Existem 2 formas de utilizar módulos ou função

# Forma 1 - Importando todo o módulo ( Não recomendado, porque armazena ele todo na memória)

import random
# from random import *  também importa tudo so n precisa especificar o módulo para chamar a função

# Usando alias // import random as rdm 

#dir(random) para saber as funções de random

print(random.random()) # a partir do modulo random chamou a função random()

# Forma 2 -Importando função especifica 

from random import random # A partir do módulo random importe a função random()

for i in range(10):
    print(random())


# uniform() -> aleatórios com range estabelecido

from random import uniform

for i in range(10):
    print(uniform(5, 10)) #Gera até 10, ou seja, nunca vai ser 10


# randint() -> Gera valores inteiros pseudo-aleatórios

from import randint

for i in range(6):
    print(randint(1, 61), end=', ')

    

# Choice() -> Mostra um valor aleatório entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

print(choice('rafael')) #escolhe uma letra da string


# shuffle() -> embaralha dados

from random import shuffle

cartas = ['k', 'q', 'j', '2', '3', '3']

shuffle(cartas)
print(cartas)


# Uso de vários imports

from random import (
    shuffle, 
    random,
    choice
)

'''