
print(f'''
{' Welcome the internet bank '.center(36, '*')}

{' Menu '.center(24, '-')}
  
  [0] - for exit
  [1] - for deposit
  [2] - for extract
  [3] - for balance

{''.center(25, '-')}
''')
initial_value = -1
extract = ''
balance = 0.0

while initial_value != 0:
  choice = int(input(': '))

  if choice == 1:
    value = float(input('R$: '))

  # extract += ' ' + value
  # TypeError: can only concatenate str (not "float") to str


    extract += ' ' + value
    balance += value
  elif choice == 2:
    if balance == 0.0:
      print('sem movimentacao.')
    else:
      print(balance)
  elif choice == 3:
    print(extract)
  elif choice == 0:
    print('atel logo')
    initial_value = 0
  else:
    print('argumento desconhecido')
    print(f'''
  
{' help! '.center(25, '-')}
  
  [0] - for exit
  [1] - for deposit
  [2] - for extract
  [3] - for balance

{''.center(25, '-')}
''')
SystemExit()
