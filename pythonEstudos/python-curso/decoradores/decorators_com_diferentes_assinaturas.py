'''

def gritar(funcao):
    def aumentar(nome, nome2):
        return funcao(nome, nome2).upper()
    return aumentar
    
@gritar
def saudacao(nome, nome2):
    return f'Olá, eu sou {nome} {nome2}'

print(saudacao('rafael', 'miguel'))

# Usando decorators pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar
    
@gritar
def saudacao(nome, nome2):
    return f'Olá, eu sou {nome} {nome2}'

print(saudacao('rafael', 'miguel'))

@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'

print(saudacao('rafael'))

'''


# Decorator com argumentos

''''

verifica_primeiro_argumento(valor): Esta é uma função externa que recebe um valor como argumento. Ela retorna a função interna chamada interna.

interna(funcao): Esta é uma função interna de verifica_primeiro_argumento. Ela recebe outra função (funcao) como argumento. 
Ela retorna uma terceira função chamada outra.

outra(*args, **kargs): Esta é a função mais interna, que envolve a função original que foi decorada (comida_favorita, no caso). 
Ela é responsável por verificar se o primeiro 
argumento passado para a função decorada é igual ao valor especificado na chamada de 
verifica_primeiro_argumento. Se for diferente, retorna uma mensagem indicando que o argumento precisa ser 
igual ao valor especificado. Caso contrário, chama a função original 
(funcao) com os argumentos fornecidos.

Quanto à ordem de execução, quando você decora a função comida_favorita com @verifica_primeiro_argumento('pizza'), 
a função verifica_primeiro_argumento é chamada primeiro, com o argumento 'pizza'. Isso retorna a função interna. Em seguida, a função interna é
chamada com a função comida_favorita como argumento, o que retorna a função outra. Então, quando você chama 
comida_favorita posteriormente, ela é na verdade outra decorada, que primeiro verifica se o primeiro argumento 
passado é 'pizza'. Se não for, retorna uma mensagem; caso contrário, chama a função original (comida_favorita) 
com os argumentos fornecidos.
'''
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kargs):
            if args and args[0] !=valor:
                return f'precisa ser {valor}'
            return funcao(*args, **kargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

print(soma_dez(10, 22)) # funciona pq o primeiro argumento é 10

print(soma_dez(1, 22)) # não funciona pq o primeiro argumento não é 10

print(comida_favorita('sanduiche, pizza'))# não funciona pq o primeiro argumento não é pizza
