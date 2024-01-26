'''
Formas gerais:

# Forma 1

range(valor_de_parada)

obs: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 1
for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)  

for nun in range(1, 11):
    print(num)


# Forma 3
range (valor_de_incio, valor_de_parada, passo)

Obs: valor_de_parada não inclusive (início especificado pelo usuário,e passo especificando pelo usuário)

vai de 2 em 2, so alterar pra ficar do jeito que quer
for num in range(1, 10, 2)
    print(num)

# Forma 4 (inversa)

range(valo_de_inicio, valor_de_parada, passo )
Obs: valor_de_parada não inclusive (início especificado pelo usuário,e passo especificando pelo usuário)

for num in range(10, 0, -1)
    print(num)


    
Para printar o ranger é necessário transforma-lo em uma lista
lista =  list(range(10))
lista
result:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

