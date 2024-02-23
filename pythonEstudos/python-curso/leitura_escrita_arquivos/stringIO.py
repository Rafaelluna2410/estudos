'''
StringIO -> Utilizado para ler e criar arquivos em memória

Para ler ou escrever é preciso permissões


'''
# primeiro fazemos o import

from io import StringIO

mensagem = 'string de teste'
#Podemos criar um arquivo em memoria vázio ou com conteúdo

arquivo = StringIO(mensagem)
print(arquivo.read())

arquivo.write(' Outro texto')
arquivo.seek(0)

print(arquivo.read())