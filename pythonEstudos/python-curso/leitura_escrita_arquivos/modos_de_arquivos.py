'''

r -> Leitura padrão
w -> sobreescreve caso exista ou cria caso não exista
x -> abre para escrita somente se o arquivo não existir
a -> escreve no final do arquivo
+ -> abre para o modo de leitura e escrita

# 1 - x
with open('leitura_escrita_arquivos/textoescrita.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo')

# 2 - a 
with open('leitura_escrita_arquivos/textoescrita.txt', 'a') as arquivo:
    arquivo.write('Teste de conteúdo\n')

# 3 - +

with open('leitura_escrita_arquivos/textoescrita.txt', 'a+') as arquivo:
    arquivo.write('novo Teste de conteúdo\n')
'''


with open('leitura_escrita_arquivos/textoescrita.txt', 'a+') as arquivo:
    arquivo.write('novo Teste de conteúdo\n')