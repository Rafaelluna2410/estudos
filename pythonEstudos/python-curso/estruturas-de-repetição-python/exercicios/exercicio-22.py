contador = 0
while True:
    
    nota = int(input("Digite a nota:\n"))
    if nota <10 or nota > 20:
        print(f"valor inválido: {nota}")
        break
    if contador != 0:
        nota += nota
    contador += 1
if contador != 0:
    print(f"Média: {nota/contador}")
