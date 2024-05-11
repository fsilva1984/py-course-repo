

# ordenando uma lista com o sort

list_num = [23, 54, 25, 32, 78, 16]
list_num.sort()
print(list_num)

# ordem decrescente
list_num.sort(reverse=True)
print(list_num)

print()

list_alf = ['c', 'f', 'l', 'a', 'j']
list_alf.sort()
print(list_alf)

# ordem decrescente
list_alf.sort(reverse=True)

print(list_alf)

print()

# ordenando pelo tamanho da string
programe_languages = ['Javascript', 'C#', 'Python', 'Java', 'C++', 'C']

programe_languages.sort(key=lambda x: len(x))

print(programe_languages)

print()

# invertendo a ordem

programe_languages.sort(key=lambda x: len(x), reverse=True)

print(programe_languages)

print()

# Obter o tamanho de uma lista

print(f' Primeira lista tem {len(list_num)} elementos')
print(f' Segunda lista tem {len(list_alf)} elementos')
print(f' Terceira lista tem {len(programe_languages)} elementos')


print()


# o python tambem tem uma funcao built-in
# para ordenar listas, a funcao sorted

frutas = ['Manga', 'Jaca', 'Ameixa', 'Banana', 'Caju', 'Damasco']

print(sorted(frutas))

print()

print(sorted(frutas, reverse=True))

print()

# Ordenando pelo tamanho das strings detro da lista de forma crescente.
print(sorted(frutas, key=lambda x: len(x)))

print()

# ordenando de forma decrescente.
print(sorted(frutas, key=lambda x: len(x), reverse=True))

