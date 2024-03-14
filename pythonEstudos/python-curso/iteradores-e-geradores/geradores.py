"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);
OBS: nem todo iterator é um generator

- util quando se precisa de um baixo custo de memória

Outra informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions 


-------------------------------------------------------------------------------------------
/ Funções                                   / Generators Functions                        /
-------------------------------------------------------------------------------------------
/ utilizam return                           / utilizam yield                              /
-------------------------------------------------------------------------------------------
/ retorna uma vez                           / podem usa yield várias vezes                /
-------------------------------------------------------------------------------------------
/ quando executada, retorna um valor        / quando executada, retorna um generator      /
-------------------------------------------------------------------------------------------

"""


# 1

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # só sai da funcção quando fazer o loop completo, diferente do return que pararia no primeiro valor
        contador +=1 

gen = conta_ate(5)
print(next(gen))
print(next(gen))

