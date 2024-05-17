print()


# metodo items retorna uma lista de tuplas
# e cada tupla contem uma par de chave e valor 

numbers = {
    'n1': 113,
    'n2': 444,
    'n3': 12,
    'n4': 1105,
    'n5': 16
}

print(numbers.items())
print()

# Uma boa maneira de utilizar o metodo items e em um loop for

for value in numbers.items():
    print(f'key: {value[0]} value: {value[1]}')

print()


# metodo keys(), metodo usado para obter todas
# as chaves de um dicionario

print(numbers.keys())

print()

# metodo pop, usado para remover um par chave : valor
# se a chave exixtir ele retorna a chave : valor
# que foi excluido, se a chave : valor nao existe ele
# retorna um keyError, podemos passar um valor padrao caso
# a chave : valo nao exista, assim evitamos o keyError. 

print(numbers.pop('n1'))
print()


print(numbers.pop('n1', 'Chave nao existe'))
print()


# metodo popitem() remove um item do final do dicionario
# se o dicionario estiver vazio e retornado um keyError

numbers.popitem()
print(numbers)
print()


print()
# metodo sedefault, cria uma novo par de chave : valor
# caso ja exista ele nao subscreve os valores

persson = {'name':'Luiz'}
persson.setdefault('age', 42)

print(persson)
print()

# nao ira subscrever a chave name
persson.setdefault('name', 'Angela')
print(persson)
print()


# metodo update(), esse metodo atualiza os valores
# de um dicionario, se caso a chave e o valor ja nao
# existir ele os cria.

persson.update({'name': 'Joao', 'age': 34})
print(persson)
print()


# metodo values(), retorna todos os valores
# de um dicionario dentro de uma lista
print(numbers.values())
print()

# uma boa forma de uso do metodo seria dentro
# de um loop for.
for value in numbers.values():
    print(value)


print()

# uma maneira de saber se uma chave existe dentro de
# um dicionario e o operador in.
print('name' in persson)
print('contacts' in persson)


print()
# metodo del, para remover alguma chave : valor em um dicionario

pessoa = {
    
    'p1':{
        'name': 'Marcos',
        'age':42,
        'gender':'Male',
        'contacts':{'tel':'(97)987390402'}
    },
    'p2':{
        'name': 'Anna',
        'age':25,
        'gender':'Famele',
        'contacts':{'tel':'(21)998836565'}
    },
    'p3':{
        'name': 'Miguel',
        'age':38,
        'gender':'Male',
        'contacts':{'tel':'(55)86937402'}
    }
}


del pessoa['p2']
print(pessoa)
print()


del pessoa['p3']['contacts']
print(pessoa)
print()


