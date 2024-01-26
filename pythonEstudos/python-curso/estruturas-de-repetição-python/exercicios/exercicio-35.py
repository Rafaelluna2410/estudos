valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))
if valor_inicial > valor_final:
    print(f"Intervalor inválido de {valor_inicial} e {valor_final}")
else:
    soma = 0
    for i in range(valor_inicial, valor_final, 1):
        if i % 2 != 0:
            soma += i
    print(f"A soma dos impares é: {soma}")

