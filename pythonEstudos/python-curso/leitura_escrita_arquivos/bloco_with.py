'''
O bloco with

# 1 - abrir arquivo
# 2 - manipular arquivo
# 3 - fechar arquivo


O block with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with

'''

# Ele cria um alias e fecha o arquivo apos a manipulação
with open('leitura_escrita_arquivos/texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)