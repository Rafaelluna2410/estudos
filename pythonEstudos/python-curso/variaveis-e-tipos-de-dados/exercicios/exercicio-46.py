numero = int(input("Digite um valor de 3 algarismos"))

if numero > 99  and numero <= 999:
    print(str(numero)[::-1])
else:
    print("Digite um valor de 3 algarismos")
