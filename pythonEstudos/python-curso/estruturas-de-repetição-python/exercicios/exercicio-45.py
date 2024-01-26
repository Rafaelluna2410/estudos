while True:
    opcao = int(input("Digite: \n 1 - Converter de km/h para m/s \n 2 - Conveter de m/s  para km/h \n 0 - Para sair\n escreva: "))
    if opcao == 1:
        valor = float(input("Digite o valor: "))
        print(f"Valor convertido para m/s: {valor/ 3.6}")
    elif opcao == 2:
        valor = float(input("Digite o valor: "))
        print(f"Valor convertido para km/h: {valor * 3.6}")
    elif opcao == 0:
        print("Programa finalizado")
        break
    else:
        print("Digite uma opçãp válida")


