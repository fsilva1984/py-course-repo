print()

# Parametros de funcoes, posicionais e nomeados.

# parametro posicional
def carro(marca, modelo, ano):
    print(f'Marca: {marca}\nModelo: {modelo}\nAno: {ano}')

carro('Chevrolet', 'Camaro', '18/05/1986')
print()


# parametros nomeados
def pessoa(nome='Anonimo', sobrenome='Desconhecido', idade='00'):
    print(f'{nome}\n{sobrenome}\n{idade}')

pessoa('40', 'Silva', 'Flavio')
print()
pessoa()


print()
# hybrido posicao + nomeado
def car(marca, modelo, ano, *, motor='1.5 16V i-VTEC', cor='Branco', status='Novo'):
    print(
        f'Marca: {marca}\nModelo: {modelo}\nAno: {ano}\n{motor}\n{cor}\n{status}'
    )

car('Honda', 'Honda City 2024', '18/05/2014')
print()

# funcao dentro de funcao

def desconto(valor, descont):
    result = '%.2f'% ((descont * 100) / valor)
    return result

def soma_produto(prod, qtdade):
    valor = prod * qtdade
    total_com_desconto = desconto(valor, 25)
    return total_com_desconto

print(soma_produto(prod=376.55, qtdade=3))

print()


# funcao como parametro
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def get_numbers(a, b, function):
    result = function(a, b)
    return f'Resultado: {result}'


print(get_numbers(26, 32, soma))

print()

print(get_numbers(95, 42, sub))

print()

# escopo local e escopo global
# quando precisar usar uma variavel global e tiver que
# chamala dentro de uma funcao, deve se usar a palavra reservada
# global, para o interpretador saber onde buscala. 
# ** se possivel evitar declaracoes de variaveis no escopo global 

salario = 2300

def soma_salario(bonus):
    global salario
    salario += bonus
    return f'Total: {salario}'

print(soma_salario(800))



print()
