"""
Podemos adicionar estruturas condicionais lógicas 
às nossas lits

"""

# Exemplos

# 1

numeros = [1,2,3,4,5,6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Melhorando
# qualquer numero par modulo de 2 é 0 e 0 em python é false. not False =True
pares = [numero for numero in numeros if not numeros %2 ]

# Qualquer número impar módulo de 2 é 1 e 1 em python é True

impares =[numero for numero in numeros if numero %2]

print(pares)
print(impares)


# 2

res  = [numero *2 if numero %2 == 0 else numero /2 for numero in numeros]
print(res)