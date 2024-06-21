
# O conseito de encapsulamento no python
# oficialmente nao foi implementado na linguagem
# mas existe uma convenao reconhecida pelo underscore

class Conta:
  
  # a variavel privada esta com o underscore
  def __init__(self, _saldo=0):
    self._saldo = _saldo

  # a variavel publica valor_deposito 
  def deposito(self, valor_deposito):
    self._saldo += valor_deposito


  def sacar(self, valor_saque):
    self._saldo -= valor_saque


  def valor_conta(self):
    return f'Saldo R$ {self._saldo}'


minha_conta = Conta()

minha_conta.deposito(1890)

print(minha_conta.valor_conta())

print()

minha_conta.sacar(1800)
print(minha_conta.valor_conta())











