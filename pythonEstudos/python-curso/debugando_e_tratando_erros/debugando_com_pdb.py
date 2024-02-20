'''
PDB -> Python Debugger

# obs: uso do print pra debugar é uma pratica ruim
def dividir(a, b):

    print(f'a={a}, b{b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'

print(dividir(4, 7))


# Exemplo com PDB, só marcar a bolinha e executar em debug

def dividir(a, b):

    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'

print(dividir(4, 0))


# Utilizando pdb com biblioteca:
# A partir do Python 3.7 n precisa importar o pdb, ja é implementando built-in  
# basta escrever breakpoint() onde é necessário debugar q ele ja executa normalmente com
# os mesmo comandos

# l lista local corrente
# n proxima linha
# p imprime a env
# c continua a execução
import pdb; pdb.set_trace() # coloca perto de onde tem que debuggar

nome = 'rafael'
sobrenome = 'miguel'
nome_completo = nome +' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso de ' + curso
print(final)


OBS: evitar nomes de envs com os mesmos nomes dos comandos  do PDB para evitar conflito
'''




