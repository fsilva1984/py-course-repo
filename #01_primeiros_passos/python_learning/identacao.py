

def sacar(valor):
  saldo = 500
  result = 0
  if valor <= saldo:
    result = saldo - valor
    print(f"Valor:{valor} saldo:{result}")


sacar(350)

sacar(76)