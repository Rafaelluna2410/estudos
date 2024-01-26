'''
Módulo collections - Counter (contador)

Conhecido -> High-performace Container Datatypes

Counter -> Recebe um interável como parâmetro e cria um objeto 
do tipo collections counter que é parecido com um dicionário, contendo
como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento

# Exemplo 1
# Utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista

lista = [1,1,1,2,2,2,3,3,3,1,1,1,2,2,2,4,4,4,5,5,5,45,45,66,66,34]

# Utilizando o counter
res = Counter(lista)
print(type(res))

print(res)
# Counter({1: 6, 2: 6, 3: 3, 4: 3, 5: 3, 45: 2, 66: 2, 34: 1})
# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a
# quantidade de ocorrência

# Exemplo 3
from collections import Counter
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
'''

from collections import Counter
texto = '''A classe Beograd de contratorpedeiros consistia em três navios construídos para a Marinha Real Jugoslava no final da década de 1930, 
uma variante da classe Bourrasque francesa. O primeiro navio, o Beograd, foi construído na França e o restantes, o Zagreb e o Ljubljana foram 
construídos no Reino da Jugoslávia. Em janeiro de 1940, o Ljubljana atingiu um recife no porto de Šibenik e ainda estava em reparos quando a 
invasão do Eixo na Jugoslávia começou em abril de 1941. Durante a invasão, o Zagreb foi afundado para evitar a sua captura, e os outros dois 
navios foram capturados pelos italianos. A Marinha Real Italiana operou o Beograd e o Ljubljana como escoltas de comboio marítimos entre a Itália,
o Mar Egeu e o Norte de África, sob os nomes Sebenico e Lubiana, respectivamente'''

palavras = texto.split()
#print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
