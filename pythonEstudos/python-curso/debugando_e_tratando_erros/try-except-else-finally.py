'''
Try / Except / Else / Finally

1 -  Toda entrada do usuário deve ser tratada


# Else - > é executado somente se nao ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Vode digitou {num}')

# Finally
# Geralmente utilizado para fechar ou desalocar recursos, exemplot conexão com banco de dados
try:
    num = int(input("Informe um número: "))
except ValueError:
    print('voce digitou um valor  inválido')
else:
    print(f'Vc digitou: {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é sempre executado se houve erro ou não

# Exemplo mais completo, o tratamento deve ser na entrada da função

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'valor incorreto'
    except ZeroDivisionError:
        return 'Não se faz divisao por zero'
    except:
        return 'Houve um erro genérico'

num1 = input("informe valor 1: ")
num2 = input("informe valor 2: ")

print(dividir(num1, num2))

'''


# Exemplo semi-genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'

num1 = input("informe valor 1: ")
num2 = input("informe valor 2: ")

print(dividir(num1, num2))
