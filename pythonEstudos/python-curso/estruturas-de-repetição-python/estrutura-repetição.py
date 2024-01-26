"""
Loop for
for item in interavel:
    //execução do loop

Exemplos de iteráveis:
- String
    nome = 'Geek University'

- Lista
    lista =[1, 3, 5, 7, 9]

- Range
    numeros = range(1, 10)
"""
nome  = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo de for 2
for numero in lista:
    print(numero)

# Exemplo de for 3
"""
range(valor_inicial, valor_final)

O valor final não é incluido
1
2
3
4
5
6
7
8
9
10  - não
"""
for numero in range(1, 10):
    print(numero)

"""
Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

'''
Descartando variavel usando placeholder
'''
for _, letra in enumerate(nome):
    print(letra)

'''
Trás somente os indicies
'''
for letra in enumerate(nome):
    print(letra[0])

'''
Trás somente as letras
'''
for letra in enumerate(nome):
    print(letra[1])

'''
o enumerare funciona como um array bidimensional 
'''

qnt = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qntd+1):
    num = int(input(f'Inform o {n}/{qnt} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


'''
O padrão do print é \n, pode ser visto no help(print('texto'))
para negar isso basta usar end=''
abaixo tem o exemplo
'''

for letra in nome:
    print(letra, end='')

'''
Imprimindo emojis no terminal
'''

for _ in range(3):
    for num in range(1, 11):
        print(f'\U0001F60D' * num)