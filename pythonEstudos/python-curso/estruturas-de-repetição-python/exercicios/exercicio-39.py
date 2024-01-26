while True:
    base = int((input("base: ")))
    altura = int(input("Digite a base: "))
    if base and altura > 0:
        break
    else:
        print("Digite valores maiores do que 0") 
print(f"Área do triângulo: {(base * altura ) / 2}")
