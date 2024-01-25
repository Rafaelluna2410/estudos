'''
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1,2,3)

Name Tuple -> São tupla onde especificamos nomes e parametros
'''
from collections import namedtuple

# Forma 1 -  Declaração Named Tuple 
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='lata', nome='Ray')
print(ray)

# Acessando

# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])


# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('lata'))
print(ray.count('lata'))


