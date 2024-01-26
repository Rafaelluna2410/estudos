'''
conjuntos

Se refere a teoria de conjuntos da Matemática

Em python, os conjuntos são chamados de Sets
    - Sets (conjuntos) não possuem valores duplicados
    - Sets não possuem valores ordenados
    - Elementos não são acessados via indice , ou seja, conjuntos não são indexados

São bons quando preciamos armazenar elementos, mas sem se necessidade da ordenação deles, quando
não precisamos nos preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre COnjuntos (sets) e mapas (dicionários) em python:
    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor
    - Um conjunto ordena os elementos e retira os duplicados

   
# Definindo um conjunto:

# Forma 1

s = set({1,2,3,4,5,5,6,7,2,3}) # Repare que temos valores repetidos
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, ele será ignorado sem gerar erro e não fará parte do conjunto

# Forma 2 - Mais comum

s = {1,2,3,4,5,5}
print(s)
print(type(s))


if 3 in s:
    print('Tem o 3')
else:
    print(' Não tem o 3') 

# Aceita tipos de dados misturados em Sets

# Usos intereassantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira
# e os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Bh', 'sp',  'RE', 'sp']

# Agora precisamos saber quantas cidades distintaas
# Podemos utilizar sets

print(len(set(cidades)))


# Adicionando elementos
s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro e é só ignorada
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # Não é indice, é o valor a ser removido
s.remove(33) # se não for encontrado gera um KeyError

# Forma 2

s.discard(2)
s.discard(22) # se não for encontrado nenhum erro é gerado

# Copiando um conjunto para outro

s = {1, 2, 3}

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(s)
print(novo)


# Forma 2 - Shallow copy
novo = s

novo.add(4)
print(s)
print(novo)

# Podemos limpar o conjnto

s.clear()
print(s)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso
# python e um contendo estudantes do curso de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Juia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'ana'}

# Veja que alguns alunos que estudam python também estudam java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe | 
unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Forma 3 
# igualar e ver se tem algo semelhante

# Gerar um conjunto de estudantes que estão em ambos os curos

# Forma 1 - Utilizando intersection

ambos1= estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

# Soma*, Valor máximo*, valor minimo*, tamanho
# * se forem reais ou inteiros
s = {1,2,3,4,5,6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
'''


