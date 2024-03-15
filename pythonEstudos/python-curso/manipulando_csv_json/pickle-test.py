"""
Conhecendo o Pickle

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

OBS: O módulo pickle não é seguro contra  dados maliciosos
e não se deve usar dados pickle de fontes desconhecidas


#escrita
with open('manipulando_csv_json/animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)


"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def comer(self):
        print(f'{self.__nome} está comendo...')

    @property
    def nome(self):
        return self.__nome

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


with open('manipulando_csv_json/animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'Nome do gato: {gato.nome}')
    gato.mia()
    print(f'type do gato {type(gato)}')

    print(f'Nome do cachorro: {cachorro.nome}')
    cachorro.late()
    print(f'type do cachorro {type(cachorro)}')