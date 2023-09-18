def criar_conta(nome, saldo, numero):
    conta = {"nome": nome, "saldo": saldo, "id": numero}
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -=valor

def extrato(conta):
    print("nome: {}	\nsaldo: {}".format(conta['nome'],	conta['saldo']))



conta =	criar_conta("rafael", 10, 2424)
depositar(conta, 50.0)
extrato(conta)













