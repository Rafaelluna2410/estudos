'''
Pacotes

Módulo = arquivo python
Pacote = diretório contendo uma coleção de módulos

OBS: Nas vrsões 2.x do Python, um pacote deveria conter dentro dele
um arquivo chamado __init__.py

Nas versões do Python 3.x. não é mais obrigatório a utilização desse arquivo,
mas normalmente é utilizado para manter compatibilidade


'''

from geek import geek1

print(geek1.funcao1(1, 2))

from geek import geek2

print(geek2.funcao2())

from geek.university import geek3, geek4

print(geek3.funcao3())
print(geek4.funcao4())