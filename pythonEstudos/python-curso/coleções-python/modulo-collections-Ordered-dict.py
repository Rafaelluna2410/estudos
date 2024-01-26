'''
Módulo Collections - Ordered Dict
 
Garante que o dicionário vai ser impresso em ordem


'''

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario.items():
    print(f'Chave={chave}:valor={valor}')

# Dicionários comuns

dict1 = {'a': 1, 'b':2}
dict2 = {'b':2, 'a':1}
print(dict1 == dict2) # True -> já que a ordem dos elementos não importa

# Ordered Dict 

odict1 = OrderedDict({'a': 1, 'b':2})
odict2 = OrderedDict({'b':2, 'a':1})

print(odict1 == odict2) # False -> já que a ordem dos elementos importa
