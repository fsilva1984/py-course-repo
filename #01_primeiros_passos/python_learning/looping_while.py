
opcao = -1

while opcao != 0:
  opcao = int(input(" [0] Sair\n [1] Sacar\n [2] Extrato\n : "))
  if opcao == 1:
    print(' Saldo disponovel: 1.255')
    print("")
  elif opcao == 2:
    print(' entrada: 2.210\n saida: 55/2.210\n saldo: 2.155\n saida: 900/2.155\n saldo: 1.255')
    print("")
  else:
    print(' Ate logo')
    print("")
SystemExit()
