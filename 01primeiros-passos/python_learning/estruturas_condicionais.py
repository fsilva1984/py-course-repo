
# estrutura condicional if
#valor = float(input("Valor a sacar: "))

def saque(param) -> float:
  saldo = 500
  result = 0
  if param <= saldo:
    result = saldo - param
    print(f"R$: {param}, saldo: {result}")
    
  if param > saldo:
    print(f"saque ate: {saldo}, saldo: {saldo}")

#saque(valor)




# estrutura condicional if else
#valor = float(input("Valor a sacar: "))

def saque(param) -> float:
  saldo = 500
  result = 0
  if param <= saldo:
    result = saldo - param
    print(f"R$: {param}, saldo: {result}")
    
  else:
    print(f"saque ate: {saldo}, saldo: {saldo}")

#saque(valor)






# estrutura condicional if elif else
choice = int(input("Digite [1] para saques | [2] para saldo | [3] para extrato: "))



def saque():
  param = float(input("Valor: "))
  saldo = 500
  result = 0
  if param <= saldo:
    result = saldo - param
    print(f"R$: {param}, saldo: {result}")
    
  else:
    print(f"saque ate: {saldo}, saldo: {saldo}")


def show_saldo():
  saldo = 500
  print(f"saldo R$ {saldo}")
  
  
def extrato():
  print(f"Dep. 1.893")
  print(f"saq. 1.275")
  print(f"sal/dia, 618")
  print(f"pg/card, 118")
  print(f"sal/dia, 500")
  
  

def exec_choice(choice) -> int:
  if choice == 1:
    saque()
  elif choice == 2:
    show_saldo()
  elif choice == 3:
    extrato()
  else:
    print("Opcao invalida")

if __name__ == "__main__":
  exec_choice(choice)