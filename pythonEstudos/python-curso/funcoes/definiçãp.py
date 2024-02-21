"""

- Funções são pequenos trechos que realizam tarefas especificas
- Pode ou não receber entradas de dados e retornar uma saida de dados
- Muito úteis para executar procedimentos similares por repetidas vezes

OBS: se você escrever uma função que realiza várias tarefas dentro dela
é bom fazer uma verificação para que a função seja simplificada

Forma de cria uma função:

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao


nome_da_funcao -> SEMPRE, com letras minusculas, e  se for nome compost, separado por underline (snake_case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> corpo ou implementação da função, pode ou não ter retorno

OBS: para definir função usamos a palavra reservada 'def'
informando ao python que estamos escrevendo uma função


# Exemplos de utilização de funções:

cores = ['verde', 'amarelo', 'azul']

# Utilizando a função integrada do python print() (Built-in)
print(cores)

curso = 'teste'
print(curso)

"""

# Definindo a primeira função

def diz_oi():
    print('oi')

# Utilizando funções

# Chamada de execução
diz_oi()


# Em python, podemos criar variáveis do tipo de uma função  e executar a função por ela
comprimentar = diz_oi

comprimentar()
