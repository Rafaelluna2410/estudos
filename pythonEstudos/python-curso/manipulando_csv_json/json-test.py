'''
import json

ret = json.dumps(['produto', {'play4': ('2tb', 'novo', '220v', 2340)}])
print(type(ret))
print(ret)


# escrita:
felix = Gato('Felix', 'Vira-lata')

with open('manipulando_csv_json/jsonpickle', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

pip install jsonpickle
'''
class Gato:

    def __init__(self,nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca


import jsonpickle

#felix = {'name': 'Felix', 'age': 3, 'breed': 'Siamese'}
#
#serialized_felix = jsonpickle.encode(felix)
#
#print(serialized_felix)
#
#with open("felix.json", "w") as arquivo:
#    arquivo.write(serialized_felix)


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret['name'])
    print(ret['age'])
    
