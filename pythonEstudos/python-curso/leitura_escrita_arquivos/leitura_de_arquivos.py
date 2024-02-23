'''

Usa a função open(), é built-in(integrada)

Na forma mais simples, apenas um parâmetro de entrada que neste caso é o nome
do arquivo (path dele) a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que
trabalhamos. Por padrão abre o arquivo por leitura se n houver há o erro file not found

<_io.TextIOWrapper name='leitura_escrita_arquivos/texto.txt' mode='r' encoding='cp1252'>  

mode r -> modo leitura - read() -  é o modo padrão e ler todo o arquivo

read(50) -> ler só as 50 primeiras caracteres

'''

# exemplo

arquivo = open('leitura_escrita_arquivos/texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o arquivo precisa usar read()
# OBS: usar cursor para trabalhar com arquivo. Funciona da mesma forma como estamos escrevendo
# nisso ele printa todo o texto e o cursor fica no final e depois do texto é vázio
# por isso imprime vazio mesmo printando 2x.


print(arquivo.read())


