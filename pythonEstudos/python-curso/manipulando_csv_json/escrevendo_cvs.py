'''
from csv import writer
                                            # se usar a ele escreve embaixo se usar w ele sobrepoem
with open('manipulando_csv_json/filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informa a duração: ')
            escritor_csv.writerow([filme, genero, duracao])

'''

from csv import DictWriter

with open('manipulando_csv_json/filmes.csv', 'w', encoding='utf-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informa a duração: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})