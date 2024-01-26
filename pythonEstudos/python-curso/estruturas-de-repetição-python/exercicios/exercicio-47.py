while True:
    opcao = int(input("Digite: \n 1 - adição \n 2 - subtração \n 3 - multiplicação \n 4 - divisão \n 5 - sair \n Escreva: "))
    match opcao:
        case 1:
            valor_a = float(input("Valor a: "))
            valor_b = float(input("Valor b: "))
            print(f"Resultado: {valor_a + valor_b}")
        case 2: 
            valor_a = float(input("Valor a: "))
            valor_b = float(input("Valor b: "))
            print(f"Resultado: {valor_a - valor_b}")
        case 3:
            valor_a = float(input("Valor a: "))
            valor_b = float(input("Valor b: "))
            print(f"Resultado: {valor_a * valor_b}")
        case 4:
            valor_a = float(input("Valor a: "))
            valor_b = float(input("Valor b: "))
            print(f"Resultado: {valor_a / valor_b}")
        case 5:
            print("Finalizado")
            break
        case _:
            print("Digite uma opção válida10")

