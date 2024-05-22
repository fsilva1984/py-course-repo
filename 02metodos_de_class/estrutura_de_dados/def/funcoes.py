print()

# declaracao de funcoes

def exib_messagem():
    print('Hello, World')

exib_messagem()
print()


def exib_msg(param):
    print(f'Messagem recebida: {param}')

exib_msg('Hello, World!')
print()


def msg_default(name='Anonimo'):
    print(f'Nome do participante: {name}')

msg_default()
print()
msg_default('Flavio')

print()

# retorno de funcoes

def sum(a=0, b=0):
    return a+b

print(sum())
print(sum(12, 28))

print()


def double_args(arg1, arg2):
    arg1 = f'Argumento 1: {arg1}'
    arg2 = f'Argumento 2: {arg2}'

    return arg1, arg2

print(double_args('Flavio', 'Silva'))

print()

# essa funcao recebe multiplos argumentos e os devlve em forma de tupla

def mult_args_type_tuple(arg, *args):
    return arg, args

print(mult_args_type_tuple('My Tuple', 'Laranja', 'Banana', 'Melancia', 'Pessego'))

print()

# exemplo de uso

def mult_args_tuple(*args):
    enter = ''

    for value in args:
        enter += value + '\n'
    
    return enter

print(mult_args_tuple('Laranja', 'Banana', 'Melancia', 'Pessego'))

print()


print()

# essa funcao recebe multiplos argumentos e os devlve em forma de dicionario

def mult_args_dict(**kwargs):
    return kwargs

print(mult_args_dict(name='flavio', subname='Silva', age='40', status='On'))

print()

# exemplo de uso

def mult_args_dict2(**kwargs):
    enter = ''

    for i in kwargs.values():
        enter += i + '\n'
    
    return enter

print(mult_args_dict2(name='flavio', subname='Silva', age='40', status='On'))

print()



