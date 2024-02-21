'''

dunder_name -> __name__
dunder_main -> __main__

são utilizados dunder para criar funções, atributos, etc 
e double dunder para não gerar conflito com os nomes desses elementos

Se executar um módulo direto no terminal, internamente o python atribuirá a variável __name__ o valor __main__ indicando
que este módulo é o módulo de execução principal, se for importado o nome fica __nome-do-proprio-arquivo__

name-modulo.__name__ # para verificar como fica a saida caso n seja o main


from soma_impares import soma_valores

print(soma_valores([1,2,3,4,5,6]))

'''


import primeiro
import segundo
