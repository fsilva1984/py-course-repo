
print(f'''
{' Welcome the internet bank '.center(36, '*')}

{' Menu '.center(24, '-')}
  
  [0] - for exit
  [1] - for deposit
  [2] - for balance
  [3] - for withdraw
  [4] - for extract

{''.center(25, '-')}
''')
initial_value = -1
extract = ''
balance = 0.0

while initial_value != 0:
  choice = int(input(': '))

  if choice == 1:
    value = float(input('R$: '))
    extract += 'Dep. R$ ' + str(value) + '\n'
    balance += value
    print('Done.')


  elif choice == 2:
    if balance == 0.0:
      print('no movement.')
    else:
      print('Balance available R$: %.2F' % (balance))


  elif choice == 3:
    withdraw = float(input('R$: '))
    if withdraw > balance:
      print('not enough balance')
      print(f'balance of the day R$: %.2f' % (balance))
    else:
      balance = balance - withdraw
      extract += 'Whd. R$ ' + str(withdraw) + '\n'


  elif choice == 4:
    print(extract)
    print(f'Total R$: %.2f' % (balance))


  elif choice == 0:
    print('Goodbye')
    initial_value = 0
    print('')


  else:
    print()
    print('unknown option'.center(19, ' '))
    print(f'''
  
  {' help! '.center(25, '-')}
  
    [0] - for exit
    [1] - for deposit
    [2] - for balance
    [3] - for withdraw
    [4] - for extract

  {''.center(25, '-')}''')
SystemExit()
