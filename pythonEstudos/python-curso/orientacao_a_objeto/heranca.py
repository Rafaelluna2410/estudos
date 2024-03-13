
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):

    def __init__(self,  nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # forma n recomendada
        self.__renda = renda
    
    
class Funcionario(Pessoa):

    def __init__(self,  nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    #Sobrescrita de metódo
    def nome_completo(self):
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'

cliente1 = Cliente('Angelina', 'jolie', '123', 5000)
funcionario1 = Funcionario('rafael', 'luna', '456', 1234)
    
print(cliente1.nome_completo())
print(funcionario1.nome_completo())