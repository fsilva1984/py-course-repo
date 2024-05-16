

# metodo add, adiciona novos elementos a estrutura set
# com o metodo add, nao e posivel adicionar elementos repetidos
# ou ceja elementos que ja constam no conjunto

conj_a = {'A', 'B', 'C'}

conj_a.add('D')
conj_a.add('A')

print(conj_a)


print()


# metodo len() para obter o tamanho do conjunto

print(len(conj_a))

print()

# operador in para verificar se determinado elemento exixte no conjunto
print('D' in conj_a)

print()

# metodo copy para copiar um conjunto de estrutura set.

copy_conj_a = conj_a.copy()

print(copy_conj_a)

print()

# metodo remove remove um elemento passado por parametro

conj_a.remove('C')

print(conj_a)

print()



# metodo discard, deixa de fora o elemento que recebe por parametro
# a diferenca entre o discard e o remove e que se o elemento nao existir
# o remove lanca um error

conj_a.discard('A')

print(conj_a)

print()




# metodo pop para eliminar o primeiro elemento da estrutura.

conj_a.pop()
print(conj_a)


print()

# metodo clear limpa o conjunto

print(f' conj_a limpo. {conj_a.clear()}')

print()








