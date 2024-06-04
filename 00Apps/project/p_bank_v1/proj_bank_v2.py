print()        

# **** operations for logged in users ****
def operation_user(user):
    print(f' Welcome {user} '.center(24, '*'))
    print()
    print(f'''

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

print()

# ****  Display Login ****

print(f'''
    {' Welcome the internet bank '.center(36, '*')}
    
    To login, use your password and CPF.
    Enter 0 to register a new user.    
''')

# **** Data of User ****
data_user = {
    'name': '',
    'cpf': '',
    'passwd':''
}

# **** for unregistered users ****
def regystre_user():
    data_user['name'] = input('Nome: ')
    data_user['cpf'] = input('CPF: ')
    data_user['passwd'] = input('Senha: ')
    operation_user(data_user['name'])

def exit_function():
    print('Goodbye :)')
    SystemExit()
    

def call_of_registre():
    print()
    print('You don\'t have a registration yet, Reply yes or not')
    print()
    choise = input('Do you want to register: ')
    if choise == 'yes':
        regystre_user()
    else:
        exit_function()
        

# **** check if user is registered ****

def user_account():
    name = input('Nome: ')
    cpf = input('CPF: ')
    passwd = input('Senha: ')
    
    for data in data_user:
            if data_user[data] == name and data_user[data] == cpf and data_user[data] == passwd:
                operation_user(data_user['name'])
            else:
                call_of_registre()


access = 1

while access >= 1:
    user_account()
    access -= 1