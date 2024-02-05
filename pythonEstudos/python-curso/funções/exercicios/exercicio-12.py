def soma_algarismos(valor):
    if valor> 0:
        transformado = str(valor)
        soma = 0
        for i in transformado:
            soma += int(i)
        return soma
    return 'Valor <= 0'

print(soma_algarismos(-1))