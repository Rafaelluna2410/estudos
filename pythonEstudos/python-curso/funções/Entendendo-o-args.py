'''

Entendendo o *args

Ordem de declarações

parâmetros Obrigatórios
*args
parâmetros default
*kwargs

- O *args é um parâmetro, como outro qualquer. Isso significa que você
poderá chamar de qualquer coisa, desde que comece com asterisco

Por convenção usa-se *args, mas pode usar *xis

O parâmetro *args utilizado em uma função, coloca os valore extras informados
como entrada em uma tupla. Então lembr-se que tuplas são imutáveis

# Exemplo:
def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3
print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5)) # Gera TypeError

toda vez que eu quisesse passar mais um argumento seria 
necessário adiconar mais um parâmetro na função

# Entendendo o args
def soma_todos_numeros(nome, sobrenome, *args):
    return  sum(args) # Por saber que é tupla pode fazer sum e pq são inteiros

#print(soma_todos_numeros())
#print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros('rafael', 'luna', 2,3,4))


def  verifica_info(*args):
    if 'Geek' in args  and 'University' in args:
        return('Bem-vindo Geek University')
    return 'Não sei quem você é'

print(verifica_info('rafael'))
print(verifica_info('Geek', 'University', 'teste'))
print(verifica_info(1, 'University', 3.15))

# Desempacotar

def  soma_todos_numeros(*args):
    return (args)

numeros =  [1,2,3,4,5,6,7,]

print(soma_todos_numeros(*numeros))


O * indica que vai trabalhar com uma coleção e sabe que precisa desempacotar

'''

