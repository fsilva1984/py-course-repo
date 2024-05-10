import re
fruits = ['Manga', 'Pera', 'Uva', 'Mamão', 'Kiui', 'Morango', 'Banana', 'Melancia']

for fruit in fruits:
    print(fruit)

print()

# iteração com o indice usando o enumerate

for index, fruit in enumerate(fruits):
    print(f' {index + 1} - {fruit}')

print('')

frutas_inicial_M = []

for i, fruit in enumerate(fruits):
    if fruits[i][0] == 'M':
        frutas_inicial_M.append(fruit)

print(frutas_inicial_M)

print('')

# inline

frutas_inicial_diff_M = [fruit for fruit in fruits if fruit[0] != "M"]
print(frutas_inicial_diff_M)
 