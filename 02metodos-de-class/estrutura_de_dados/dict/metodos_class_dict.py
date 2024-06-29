print()

# metodo get, para obter o valor de uma chave
# em um dicionario podemos usar a forma direta
# obj['key'], o problema de usar essa forma e que
# se nao existir a chave um erro e retornado

obj = {'id_12':'value12'}
# print(obj['id_14'])# keyError sera retornado

print(obj.get('id_14'))# None sera retornado

print()
# podemos passar para o metodo get um valor default
# de rtorno quando a chave nao existir

print(obj.get('id_14', 'Undefined'))# Undefined sera retornado
print()

print(obj.get('id_14', {}))# Objeto vazio sera retornado



print()

# metodo fromkeys, metodo usado para criar chaves
# sem nenhum valor ou criar uma chave com um valor
# padrao em um dicionario 

alpha = dict.fromkeys(['0', '1', '2', '3'])
print(alpha)

print()

# ja com um valor padrao
alpha2 = dict.fromkeys(['0', '1', '2', '3'], 'any')

print(alpha2)


print()
# metodo copy, para copiar um dicionario

numbers = {
    'n1':18,
    'n2':13,
    'n3':42,
    'n4':76,
}

dict_copy = numbers.copy()
dict_copy['n1'] = 1239

print(numbers)
print()
print(dict_copy)


print()
# metodo clear, limpa todos os dados de um dicionario

print(numbers)
print()
print(f'Dicionario limpo: {numbers.clear()} !')



print()