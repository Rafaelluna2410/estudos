def consumo_carro(km, litro):
    if km/litro < 8:
        return f'Venda o carro, consumo de {km/litro}'
    elif km/ litro >=8 and km/litro <= 12:
        return f'Econômico, consumo de {km/litro}'
    return f'Super econômico, consumo de {km/litro}'

print(consumo_carro(13, 1))
