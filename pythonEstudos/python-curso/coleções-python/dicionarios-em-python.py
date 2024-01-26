'''

Obs: O que é conhecido por dicionário são os mapas em outras linguagens

São coleções do tipo chave e valor
key = valor

São representados por {}
As chaves e valores podem ser de qualquer tipo 

Exemplo - 1: (comum)
paises = {'br': 'brasil', 'eua': 'estados unidos'}

Exemplo - 2: (menos comum)
paises = dict(br='brasil', eua:'estados unidos')

#######################
# Acessando elementos #
#######################

Forma - 1: Acessando via chave

print(paises['br'])
print(paises['eua'])

Forma - 2: Acessando via get - recomendado

print(paises.get['br'])
print(paises.get['eua'])

O get é recomendado, porque facilita o tratamento de erro, por exemplo:

pais =  paises.get('ru', 'Não encontrado') Se a chave existir substituir pelo valro, caso contrário escreve 'Não encontrado'
print(f'Encontrei o país {pais}') 


Verificando se a chave existe no dicionário:
Ele busca por chave e não pelo valor, então não adianta buscar o valor no dicionário desta forma
print('br' in paises)
print('ru' in pasies)


# Podemos utilizar qualque tipo de dado como chaves

Tuplas são interessantes para serem as chaves, pois são imutáveis
localidade = {
    (33.65, 33.68): 'Tókio',
    (40.10, 40.33): 'Nova york',
}

# Adicionar elementos no dicionário

receita = {'jan': 100, 'fev': 120}

forma - 1:

receita['marco']= 350

forma - 2:

novo_dado = {'abr': 500}
receita.update(novo_dado) # receita.update({'abr': 500})


# Atualizando dados em um dicionário

forma - 1:

receita['mai'] = 550

forma - 2:

receita.update({'mai': 600})

##############
# IMPORTANTE #
##############
OBS: Não pode ter chaves repetidas, se não ele substitui os dados


# Remover dados

receita = {'jan': 100, 'fev': 120, 'mar': 130}

forma - 1:

receita.pop('mar')

obs: precisa sempre informar a chave
obs:  remove a chave e retorna o valor da chave que foi removido


forma - 2:

del receita['fev']


################
# Casos de uso #
################

Exemplo 1: Carrinho de compras 

    Produto 1:
        - nome
        - quantidade
        - preco
    produto 2: 
        - nome
        - quantidade
        - preco

Se utilizar uma lista para isso

# Teriamos que saber qual é o índice de cada informação no produto
carrinho = []

produto1 = ['Playstation 4', 1, 230.00]
produto2 = ['God of war', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)



#usando tuplas
produto1 = ('Playstation 4', 1, 230.00)
produto2 = ('God of war', 1, 150.00)

carrinho.append(produto1)
carrinho.append(produto2)


# Usando dicionário (forma recomendada)
# Adiciona e remove facilmente e tem certeza de cada informação
carrinho = []

produto1 = {'nome': 'PS4', 'quantidade': 1, 'preco': 230.00}
produto2 =  {'nome': 'God of war', 'quantidade': 1, 'preco': 50.00}
carrinho.append(produto1)
carrinho.append(produto2)

###########
# Métodos #
###########

d = ('a': 1, 'b': 2, 'c': 3)

# Limpar o dicionário
d.clear()

# Copiando um dicionário para outro

# Forma 1

novo = d.copy() # Deep copy

novo['d'] = 4


# Forma 2 

novo =  d  # shallow copy

novo['d'] = 4

# Forma não usual de criação de diocionários

outro = {}.fromkeys('a', 'b')

usuario = {}.fromkeys(['nome', 'teste'], 'Desconhecido')
# 'Desconhecido ' virou o valor de nome e teste
# O fromkeys recebe a chave e o valor 

veja = {}.fromkeys('teste', 'valor')
#para cada letra de 'teste' tem como valor o 'valor'

veja2 = {}.fromkeys(range(1, 11), 'novo')



###########################################
# Continuação da aula que foi em 2 partes #
###########################################

# Interar sobre dicionários

receita = {'jan': 100, 'fev': 120, 'mar': 130}

    imprime as chaves
for chave in receita:
    print(chave)

    imprime os valores
for chave in receita:
    print(receita[chave])

    
for chave in receita:
    print(f'Em {chave} recebi R$ {receita{chave}}')

listar todas as chaves:

print(receita.keys())


for chave in receita.keys()
    print(receita[chave])

listar todos os valores:

print(receita.values())

for valor in receita.values()
    print(valor)


# Desempacotar dicionário:

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# *soma, *valor máximo, *valor minimo, tamanho  
# * se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))


'''

