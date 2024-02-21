"""
Módulos Customizados

Todos os arquivos que foram criados até aqui são módulos py

from funcoes_com_parametro import soma_impares

print(soma_impares([1,2,3,4,5,6,7]))


"""

# importando módulo de um diretóro
import funcoes.teste as soma

print(soma.total(3))

# importando módulo de um subdiretório
import funcoes.funcoes_2.teste_2 as soma2

print(f'outro módulo: {soma2.total(3)}')


