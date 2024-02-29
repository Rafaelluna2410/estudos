'''

**kwargs


Ordem de declarações

parâmetros Obrigatórios
*args
parâmetros default
*kwargs

O **kwargs exige que utilizemos parâmetros nomeados e transforma-os em parâmetros
extras em um dicionário

def cores_favorita(**kwargs):
    print(kwargs)

cores_favorita(marcos='verde',julia='amarelo', fernando='azul')


def cores_favorita(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favorita(marcos='verde',julia='amarelo', fernando='azul')

# Sequência de declaração correta dos parâmetros

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome }  tem {idade} anos')
    print(args)
    if solteiro:
        print(solteiro)
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(10, 'Felipe', 4,5,3, solteiro =True)
minha_funcao(20,'Felicity', eu='Não', voce='Vai')
minha_funcao(40,'Carla', 9,4,3, java=False, python=True)

OBS: os nomes das chaves do dicionário devem ser os mesmo dos parâmetros da função  
para desempacotar usa **kwargs

'''


# Decorators com argumentos




