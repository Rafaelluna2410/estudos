'''
Saindo de loops com break

Funciona da mesma forma que em C ou Java.

O break serve para sair de loops de forma projetada

# Exemplo 1

for numero in range(1, 11)
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')


while True:
    comando = input("Digite sair para sair: ")
    if comando == 'sair':
        break
'''