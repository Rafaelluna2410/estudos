for numero in range(1000, 10000):
    d1 = numero // 100
    d2 = numero % 100

    soma_quadrados = (d1 + d2)**2

    if soma_quadrados == numero:
        print(numero)
