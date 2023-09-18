from Conta import Conta

conta = Conta('123-4',	'João',	120.0,	1000.0)

print(conta.extrato())
conta.deposita(150)
print(conta.extrato())
conta.saca(20)
print(conta.extrato())