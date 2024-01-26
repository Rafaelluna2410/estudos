'''
As tuplas são semelhantes a listas:
diferenças:

1 - São representadas por parenteses
2 - São imutáveis, significa que ao se criar uma tupla
ela não muda. Toda operação em uma tupla gera uma nova tupla

# CUIDADO - 1: As tuplas são representadas por (), mas veja:

tupla1 = (1,2,3,4,5,6)
tupla2 =  1,2,3,4,5,6

Entende-se que ambos são tuplas

# CUIDADO - 2: Tuplas com 1 elemento

tupla3 = (4) # isso não é uma tupla

tupla4 = (4,) # Isso é uma tupla

# Conclusão: Tuplas são definidas pela virgula e não pelo parenteses

# Podemos gerar uma tupla dinamicamente com range

tupla = tuple(range(11))

#  Desempacotamento de tupla

tupla = ('test-1', 'test-2')
opcao1, opcao2 = tupla

# Métodos para adicionar e remover não existem, porque são imutaveis

# Se os valores forem todos inteiros ou reais
tupla = 1,2,3,4
sum(tupla)
max(tupla)
min(tupla)
len(tupla)


# Concatenação de tuplas

tupla1 = 1,2,3
tupla2 = 4,5,6

tupla3 = tupla1 + tupla2
print(tupla1 + tupla2)

ele imprime 1,2,3,4,5,6
mas as tupla1 e tupla2 continuam iguais caso sejam printadas também

os valores  das tuplas podem ser sobrescritos 
tupla1 = tupla1 + tupla2


Verificando a existência do elemento na tupla
tupla  = 1,2,3
print(3 in tupla)

Iterando sobre uma tupla
tupla  = 1,2,3
for n i tupla

for indice, valor in enumerate(tupla):
print(indice, valor)

Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c')
print(tupla.count('c'))


#################################
# Dicas na utilização de tuplas #
#################################

Use quando não precisar trocar os dados de uma coleção

Exemplo - 1: meses do ano

Porque utilizar tuplas:

1 - Tuplas são mais rápidas do que listas
2 - Tuplas deixam seu código mais seguro(imutáveis)


Verificando o indice do elemento na tupla
print(tupla.index('elemento'))


'''