'''
        Isso cria um atributo "privado" chamado __limite. A inclusão de dois 
        sublinhados na frente do nome do atributo indica que ele é uma variável
        de instância privada, o que significa que não pode ser acessado 
        diretamente de fora da classe.

        Isso cria um atributo público chamado limite. Isso significa que o atributo 

        self.limite = limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # exemplo de set    
    def set_limite(self, limite):
        self.__limite = limite
    
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.limite

print(conta1.extrato())
print(conta2.extrato())

conta1.transferir(1000, conta2)
print(conta1.extrato())
print(conta2.extrato())


conta1.depositar(3000)
conta2.sacar(5000)

print(conta1.extrato())
print(conta2.extrato())



print(conta1.get_limite())
'''


class Conta:

    contador = 0 

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    @property
    def  numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    # por padrao @property é get, para ser set preciso definir
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite




conta1 = Conta('felicity', 3000, 10000)
conta2 = Conta('rafael', 1000, 20000)


print(conta1.saldo)
print(f'{conta2.saldo} \n')

print(conta2.limite)
conta2.limite = 30000
print(conta2.limite)

