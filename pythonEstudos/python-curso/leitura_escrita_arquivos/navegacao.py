"""
Sistema de arquivos e navegação

precisa do módulo OS

import os

# getcwd() -> pega o current work directory

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

# checagem se um diretório é absoluto ou relativo

#OBS: em windows usa dupla barra \\ para usar navegação
print(os.path.isabs('/home/rafael/Estudos')) # true é relativo
print(os.path.isabs('home/rafael/Estudos')) # false n é relativo

#verificar o os

print(os.name) # posix linux and mac, nt windows
print(os.uname()) # informacoes completa sobre os

# outra forma de saber a plataforma
import sys
print(sys.platform)

# navegando em diretórios

import os

#/home/rafael/Estudos/pythonEstudos/python-curso

print(os.getcwd())

res = os.path.join(os.getcwd(), 'funcoes')
# primero recebe o diretório atual e escolhe o diretório que vai juntar no path
os.chdir(res)

print(os.getcwd())


import os

print(os.listdir())
print(len(os.listdir()))

print(os.listdir('funcoes'))
print(len(os.listdir('funcoes')))

print(list(os.scandir())) # posso escolher caso eu queira


"""

import os

scanner = os.scandir()

arquivos = list(scanner)

print(dir(arquivos[0]))


print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())

scanner.close()