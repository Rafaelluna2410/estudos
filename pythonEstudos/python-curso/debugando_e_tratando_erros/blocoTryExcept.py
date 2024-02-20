"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Evitand que o usuário recebe mensangens de erros
inesperadas e que o programa pare de funcionar


try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema


# 1 erro genérico

try:
    geek()
except:
    print("Teve algum problema")

OBS: tratar erro de forma genérica não é bom, o ideal é tratar de forma específica exemplo typeError

# 2 erro específico com apelido

try:
    geek()         
except NameError as err: 
    print(f'houve o seguinte erro: {err}')

# 3 tratando vários erros
try:
    len(5)
except NameError as erra:
    print(f'deu um erro: {erra}')
except TypeError as errb:
    print(f'Deu erro: {errb}')
except:
    print('deu um erro diferente')

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    except NameError:
        return None
    
dic = {'nome': 'Geek'}

print(pega_valor(dic, "nome"))










