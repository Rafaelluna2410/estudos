def comprimento(string, tamanho):
    if string is None:
        return -1 

    tamanho[0] = len(string) 
    return 0 


minha_string = "Hello, world!"
tamanho = [0] 

resultado = comprimento(minha_string, tamanho)

if resultado == 0:
    print("O comprimento da string é:", tamanho[0])
else:
    print("Erro ao calcular o comprimento da string.")
