'''

Funções com parâmetro ( de entrada)
- Funções que recebem dados para serem processados dentro da mesma

def quadrado(numero):
    return numero * numero

print(quadrado(5))

def soma(a, b):
    return a + b

print(soma(2, 5))

# OBS: se passar o numero errado de parâmetro ou argumento gera typeError

def nome_completo(nome, sobrenome):
    return f'Seu nome completo:  é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# Parâmetros e Argumentos
# Parâmetros são variáveis declaradas na definição de uma função
# Argumenots são dados passados durante a execução de um função
# A ordem dos parâmetros importa!

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# utilizar quqlauqer ordem

print(nome_completo(nome='Nome1', sobrenom='sobre2'))
or
print(nome_completo(sobrenome='sobre3', nome='nome3'))

'''



