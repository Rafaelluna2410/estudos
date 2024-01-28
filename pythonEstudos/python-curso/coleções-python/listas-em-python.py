"""
Listas

São vetores/matrizes (arrays)
São dinâmicos e aceita qualquer tipo de dado
São representados por colchetes: []
lista_a = [1, 2, 3, 4, 5]
lista_b = ['a', 'b', 'c']
lista_c = list(range(11))
lista_d = list('Geek university)
lista_e = []

procurando numeros:
if 8 in lista_c:
    print("Valor encontrado)
else:
    print("Valor não encontrado)

procurando uma lista:
# Ele procura esse conjunto e não separadamente
if [8, 3, 1] in lista_a:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')


procurando letras:
if 'e' in lista_d:
    print("encontrado" )
else:
    print("não encontrado" )

# Podemos facilmente ordenar uma lista:
print(lista_a.sort())

# Podermos facilmente contar o número de ocorrência de um
# valor em uma lista

print(list_a.count(a))
print(lista_d.count('e'))

# Adicionar elementos em listas:
# Funcão append, adiciona um elemento por vez e no final da fila

print(lista_a)
lista_a.append(32)
print(lista_a)

# adiciona a lista como um elemento da lista maior, porque só aceita um dado por vez
lista.append([8, 3, 1])


Coloca cada elemento da lista como um valor adicional à lista e no final dela
lista_a.extend([123, 44, 67])
print(lista_a)

# Podemos inserir um novo elemento da lista informando a posição do indice
# e deslocando para direita o antigo valor daquele indice
lista_a.insert(2, 'novo valor')
print(lista_a)

# Juntar duas listas:  # pode usar o + ou o extend
lista_6 = lista_a + lista_b
print(lista_6)

# Inverter uma lista:
lista_a.reverse()
or
lista_a[::-1]

# Contar o tamanho da lista:
len(lista_a)

# Remover o último elemento de uma lista e printa:
lista_a.pop()
# Remove a partir de um indice:
lista_a.pop(2)
Limpar toda a lista:
lista_a.clear()

Conversão de String para uma lista: 

# Exemplo 1

curso = 'teste'
curso = curso.split()
print(curso)

OBS: Por padrão, o split separa os elementos da lista pelo espaço em branco

# Exemplo 2

curso = 'teste,a,b,c'
curso = curso.split(',') modifico o separado de elementos para virgula
print(curso)

# Exemplo 3
lista_7 =  ['teste', 'Em', 'Python']
curso = ' '.join(lista_7) Estou dizendo para colocar espaço entre os elementos, mas posso colocar qualquer outra coisa em vez de espaço


Iterando sobre listas

Exemplo 1 - utilizando for
aqui ele percorre os elementos diretament sem ser pelo indice
for elemento in lista_a:
    print(elemento)
    soma += elemento
print(soma)

lista = [1, 2, 3]
soma = 0

for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")
    soma += valor

print(f"Soma: {soma}")


Exemplo 2 = Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione produto a lista o sair para sair')
    if produto != 'sair'
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Utilizando variáveis em listas

numeros =  [1, 2, ,3, 4, 5]
num1 = 1
num2 = 2
num3 = 3

numeros = [num1, num2, num3]

# Fazemos o acesso aos elementos de forma indexada:

cores = ['verde', 'amarelo', 'vermelho']
print(cores[0])

# Fazemos o acesso aos elementos de forma indexada inversa:
# é como um circulo onde o final está ligado ao inicio da lista
cores[-1] # vermelho
cores[-2] # amarelo

# Gerar indice em um for:
Cria chave e valor
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos:

lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(42)


########################
# Alguns métodos uteis #
########################

#Encontrar o indice de um elemento na lista
numeros  = [5, 6, ,7, 8, 5, 9, 10]

Qual o indice de 6?
print(numeros.index(6))

Qual o indice de 7?
print(numeros.index(7))

Se o index não existir vai gerar um erro

print(numeros.index(5)) # printa o indice do primeiro elemento encontrado se houverem valores repetidos


print(numeros.index(5, 1 )) # buscando a partir de um indice 
print(numeros.index(8,3,6))# buscando em um ranger, 'busca o indice do valor 8 entre os indices 3 e 6'


#################
# Revisão slice #
#################

lista(inicio:fim:passo)
range(inicio:fim:passo)


##################
# Slice de lista #
##################

lista = [1, 2, 3, 4]
print(lista[1:]) pegando a partir do indice 1 e todos os elementos restantes
print(lista[:2]) começa em 0 e pega até o indice 2 sem incluir o valor do indice 2, pega até o indice 2 -1
print(lista[:4]) começa em 0, pega até o indice 4 - 1
print(lista[1:3]) começa do indice 1 e vai até o 3, pega até o indice 3 - 1
print(lista[1::2]) começa em 1, e vai até o final, de 2 em 2


###################################
# Invertendo valores em uma lista #
###################################

nomes = ['teste',  'invetido']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)

#############################################
# Soma, valor maximo, valor minimo, tamanho #
# Só para int e floats                      #
#############################################

lista = [1, 2, 3, 4]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

##############################
# Transforma lista em tupla  #
##############################

lista = [1, 2, 3, 4]
tupla = tuple(lista)
print(tupla)


#######################
# Desempacotar listas #
#######################

lista = [1, 2, 3, 4]
num1, num2, num3, num4 = lista # Se passar menos variáveis ou mais variáveis do que a quantidade de elementos na lista gera erro

print(num1)
print(num2)
print(num3)
print(num4)


############################################################
# Copiando uma lista para outra (Shallow copy e deep copy) #
############################################################

lista = [1, 2, 3]
nova = lista.copy()  # Elas são independentes, se uma for modificada não afeta a outra 'Deep copy'

lista = [1, 2, 3]
nova = lista # Elas são dependentes, se uma for modificada a outra é afetada (Shallow copy)

"""