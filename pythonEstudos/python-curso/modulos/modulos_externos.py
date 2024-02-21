'''

Uso do Pip para instalar packages

site para pacotes py: pypi.org 

exemplo: pip install colorama

colorama -> usado para textos coloridos no terminal


'''


from colorama import init

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')