

# adicionando itens a lista com o metodo append
# o metodo aceita apenas um argumento
# que pode cer um item ou uma lista um obj etc..

frutas = []
frutas.append('Caja')
frutas.append(['Manga', 'Pera', 'Uva', 'Mamão', 'Kiui'])
frutas.append(['Morango', 'Banana', 'Melancia'])

print(frutas)

print()

# copiando uma lista metodo copy
# o metodo faz uma copia exata de uma lista, sendo e o novo
# objeto é totalmente independende do obj original, assim ao
# modificar a copia o original permanece inalteravel

frutas_copia = frutas.copy()

print(f'Original {frutas}')
print(f'Copia {frutas_copia}')

print('')

# limpando uma lista metodo clear

frutas_copia.clear()

print(f'Original {frutas}')
print(f'Copia {frutas_copia}')

print('')


# podemos saber quantas vezes um elemento aparece
# em um determinado objeto com o metodo count


frutas.append('Caja')
frutas.append('Caja')
frutas.append('Caja')


print(f' A fruta caja aparece {frutas.count('Caja')} vezes no array frutas')

print('')

# adicionando mais de um elemento a lista com o metodo extend

frutas_copia.extend(['Manga', 'Abacaxi', 'Uva', 'Melancia'])

print(frutas_copia)

print('')

# obter o indice da primeira ocorrencia de um elemento

frutas_copia.extend(['Jaca', 'Caja', 'Tomate', 'Caja'])

print(f' A primeira ocorrencia de Caja esta no indice {frutas_copia.index('Caja')}')


# metodo pop para retirar o ultimo elemento da pilha
# pois a lista e uma estrutura de pilha
# porem podemos passar o indice do elemento a ser removido


print(f' Foi removido o elemento {frutas_copia.pop()}')

print(f' Foi removido o elemento {frutas_copia.pop(4)}')

print('')

# outro metodo para retirar um elemento da lista e o remove
# deve se passar o nome do elemento a ser deletado

frutas_copia.remove('Tomate')

frutas_copia.remove('Caja')

print(frutas_copia)

print('')

# invertendo a ordem da lista com o metodo reverse

frutas_copia.reverse()

print(frutas_copia)

print('')



















