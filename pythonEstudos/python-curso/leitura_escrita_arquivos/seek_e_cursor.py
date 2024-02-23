'''

seek() -> é utilizada para movimentar o cursor no arquivo
recebe um parâmetro que indica onde vai ser direcionado 
o cursor - Em qual caracter começa

print(arquivo.read())
# Usando seek()

arquivo.seek(6)
print(arquivo.read())

readline() -> imprime a linha que o cursor está
print(arquivo.readline())

OBS: Toda vez que usar o read() é feita a conexao entre o sistema e o disco chama-se streamer e
deve-se fechar toda vez essa conexão após fazer o uso do arquivo. É feito o lock para evitar interrupções


closed() - verifica se está aberto ou fechado

close() - fecha o arquivo - false está aberto, true está fechado

'''

arquivo = open('leitura_escrita_arquivos/texto.txt')

linhas = arquivo.readlines()

#Escolhjendo a linha que vai ser impressa
print(linhas)
print(linhas[2])
print(len(linhas))


