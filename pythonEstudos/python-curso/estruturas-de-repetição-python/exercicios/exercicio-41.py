while True:
    valor_r1 = int(input("Digite o R1: "))
    valor_r2 = int(input("Digite o R2: "))
    resistencia = (valor_r1 * valor_r2) / (valor_r1 + valor_r2) 
    if resistencia ==0:
        print(f"Resistência: {resistencia}")
        break
