"""
Manipulação de arquivos


import os

# files
print(os.path.exists('texto.txt')) # False
print(os.path.exists('recebendo_inputs.txt')) # True

#diretório 
print(os.path.exists('funcoes')) # True

# Criandoa files

# 1

open('teste.txt', 'w').close()

# 2
open('teste2.txt', 'a').close()

# 3

with open('teste3.txt', 'w') as arquivo:
    pass
    
# Forma recomendada
os.mknod('teste4.txt')

# Se ja existir gera FileExistsError


# Criando diretórios (um a um)

os.mkdir('templates')
# Se ja existir gera FileExistsError
# Se n tiver permissao gera PermissionError

# Criando vários diretórios
os.makedirs('teste1/teste2/teste3')
# Se ja existir gera FileExistsError
# Se n tiver permissao gera PermissionError

# Renomear  arquivos e diretporios

# diretório 
os.rename('teste1/teste2', 'geek2')
# se n estiver vázio gera um OSError

# file

os.rename('teste1.txt', 'teste2.tx')


# ATENÇÂO, ao deletar arquivos ele não vai para a lixeira

# deletar arquivo
os.remove('geek.txt')
# se ele estiver em uso no windows haverá error
# se passar um diretório em vez de arquivo gera isDirError


# deletar diretório vazio

os.rmdir('teste')
# se tiver algo gera OSError

# deletar arvore de diretórios vázios

os.removedirs('teste1/teste2')
# se algum tiver algo o processo para



# Para deletar enviando para a lixeira usa
 send2trash

from send2trash import send2trash

# arquivo para lixeira
send2trash('testetrash.txt') # vai para a lixeira

# diretório para a lixeira

send2trash('testedirremove')


# Usando com arquivos e diretórios temporários

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'teste dir {tmp}')
    with open(os.path.join, 'arquivo_temporario.txt', 'w') as arquivo:
        arquivo.write('teste arquivo temporario')
    input()


# criando arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'teste')
    tmp.seek(0)
    print(tmp.read())
# OBS: em arquivo temporários so conseguimos escrever bit, por isso usa-se b


"""




