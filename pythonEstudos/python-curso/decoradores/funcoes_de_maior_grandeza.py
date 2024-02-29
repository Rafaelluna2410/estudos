"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem tem suporte a HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar 
funções como argumentos para outras funções, e até mesmo criar variáveis do
tipo de funções nos nossos programas.

# 1

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir ))



# Nested Functions - Funções Aninhadas

# 1

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'tchau ', 'ok '))
    return humor() + pessoa

print(cumprimento('rafael'))

print((cumprimento('miguel')))


"""


from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaah', 'lolololo', 'kkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('rafael')


print(rindo)
print(rindo)
print(rindo)