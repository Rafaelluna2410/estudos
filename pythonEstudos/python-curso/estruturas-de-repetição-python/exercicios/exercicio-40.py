maior = float('-inf')  # Inicialize o maior com infinito negativo
menor = float('inf')   # Inicialize o menor com infinito positivo
while True:
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
    if valor < menor and valor > 0:
        menor = valor
    if valor <0:
        print(f"Maior: {maior}, menor: {menor}")
        break
