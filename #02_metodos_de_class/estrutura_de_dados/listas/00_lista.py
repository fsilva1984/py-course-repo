
# declarando uma lista comum

fruits = ['Manga', 'Pera', 'Uva', 'Mamão']
print(fruits)

print('')

index = list(range(11))
print(index)

print('')

letters = list('Python3')
print(letters)

print('')

mix_list = [True, 'Strings', 1234.89, 1200]
print(mix_list)

print('')

# acessando um elemento da list de forma direta.
print('Forma direta')

print(fruits[0])

print('')

print(index[6])

print('')

print(letters[0])

print('')

print(mix_list[1])
print('')
# uso de index negativos


print('indices Negativos')

print(fruits[-1])

print('')

print(index[-6])

print('')

print(mix_list[-3])


# fatiamento de listas

print(index[0:])# inicio 0 e vai ate o final
print(index[0:6])# inicio no 0 e vai ate o 6
print(index[5:11])# inicio no 6 e vai ate o 11
print(index[0::2])# inicio no 0 e vai ate o final pulando de 2 em 2
print(index[::])# devolve uma copia da lista
print(index[:: -1])# devolve uma copia da lista "invertida" espelhada.


