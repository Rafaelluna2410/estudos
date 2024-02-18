def substring(valor):

    posicao = valor.find("rafael")
    if posicao != -1:
        return print("A sub-string foi encontrada na posição:", posicao)
    else:
        return print("A sub-string não foi encontrada.")
   
palavras = 'teste de string e substring'
print(substring(palavras))