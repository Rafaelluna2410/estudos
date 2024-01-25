'''
Módulo Collections - Default dict

dicionaro = {'curso': 'teste'}
print(dicionaro)
print(dicionaro['curso'])
print(dicionaro['teste'] ) # ??? KeyError

Default Dict ->  Ao criar um dicionário utilizando-o , nós informamos
um valor default, podendo utilizar um lambda para isso. Este valor será
utilizado sempre que não houver um valor definido. Caso tentemos acessar uma
chave que não existe, essa chave será criada e o valor default será atribuido.


OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrafa
e retorna valores

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação teste'
print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.

print(dicionario)
'''


