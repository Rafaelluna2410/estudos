'''

### n recomendado
with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    print(dados)

    dados = dados.split(',')[2:]
    print(dados)

    
    - reader -> itera sobre as linhas do arquivo como listas
    - DictReader -> itera sobre as linhas do arquivo como OrderedDicts

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #pular cabeçalho
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no {linha[1]} e mede {linha[2]} cm')


OBS: por padrão usam ',' para delimitar os objetos. DictReader(arquivo, delimiter='/') 
qnd for '/' e assim por diantae
'''

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Precisa ter o nome correto do cabeçalho
        print(f'{linha['Nome']} nasceu no {'País'} e mede {'Altura'} cm')

