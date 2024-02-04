'''
Funções com Parâmetro padrão

- Funções onde a passsagem de parâmetros seja opcional;
- Torna as funções mais flexiveis
- Evita erros de parâmetros incorrretos
- Facilita a legibilidade do código
- Aceita qualquer tipo de dado como valor default

Ex: print()

Parametro obrigatório:
def quadrado(numero):
    return numero  ** 2

Parametro Default:
def exponenicial(numero, potencia = 2):
    return numero ** potencia

print(exponenicial(2)) # Utiliza o padrão
print(exponenicial(2, 3))  # Posso definir caso eu precise

OBS: Os valores padrões devem estar no final da declaração, se 
colocar depois dos não-defaults vai gerar erro

# Exemplo-2:

def mostra_informacao(nome='Geek', instrutor = False):
    if nome == 'Geek' and instrutor: # E intrturo for True
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True)) # Preciso indicar que vou usar o segundo parametro
print(mostra_informacao('Ozzy'))

# Exemplo-3:

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 3, subtracao))

# Escopo - Evita erros

# Variáveis globais e locais

instrutor = 'Geek' #Variável global

def oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'
# OBS: se houver uma variável local com o mesmo nome da variável glocal, a local terá preferência

def oi():
    prof = 'Geek'
    return f'Olha {prof}'

# OBS: A local só existe dentro do bloco da função


ATENÇÂO:
- Evitar variáveis globais

Gera erro:
total = 0

def soma():
    total = total + 1
    return total

print(soma())

# Nonlocal  = avisa que não é local e está declarada antes
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador +=  1
        return contador
    return dentro()


###########
# Atenção #
###########
Isto em função não funciona:
precisa definir dentro da func
total = 0

def teste():
    total = total + 1
    return(total)

print(teste)


Isto em loop funciona:
total = 0

for i in range(3):
    total = total + 1
    print(total)



'''


