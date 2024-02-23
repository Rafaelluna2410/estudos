'''
Escrevendo em arquivos

# OBS: Se abrir um arquivo para leitura nao pode ser feito escrita
se for aberto para escrita nao se pode ler. 

É sobreescrito o arquivo e se não existir ele cria o arquivo

# 1 usa modo w para escrever

with open('leitura_escrita_arquivos/texto.txt', 'w') as arquivo:
    arquivo.write('Escrita de arquivo via py\n' * 10)
    arquivo.write('Outra linha de teste usando py para escrita')

'''

# 2
with open('leitura_escrita_arquivos/texto.txt', 'w') as arquivo:
    while True:
        fruta = input('informe uma fruta ou digite sair')
        if fruta != 'sair':
            arquivo.write(fruta+'\n')
            #arquivo.write('\n')
        else:
            break

