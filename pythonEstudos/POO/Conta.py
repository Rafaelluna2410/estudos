class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("inicializando uma conta")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def setDeposita(self, valor):
        self.__saldo += valor
    
    def setSaca(self, valor):
        self.__saldo -= valor

    def getExtrato(self):
        return self.__saldo
    
    def setTitular(self, nome):
        self.__titular = nome
    
    def getTitular(self):
        return self.__titular
    
    def getLimite(self):
        return self.__limite
    
    def setNumero(self, value):
        self.__numero = value

    def getNumero(self):
        return self.__numero