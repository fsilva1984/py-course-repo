
# metodo union reune elementos de outros
# conjuntos em um so lugar removendo as duplicatas.


conj_a = {1, 2, 3}
conj_b = {4, 5, 6, 6}


print(conj_b.union(conj_a))
print()

# metodo intersection vai reunir os conjuntos
# apartir dos objetos  que se repetem

conj_c = {4, 8, 16, 32}
conj_d = {3, 5, 8, 12, 16} 

print(conj_d.intersection(conj_c))
print()


# metodo difference reune o conteudo
# que difere entre os conjuntos

conj_e = {'A', 'b', 'C', 'd', 'G'}
conj_f = {'A', 'B', 'C', 'd', 'F'}

# mosta o que esta em conj_e que o conj_f nao tem
print(conj_f.difference(conj_e))


# mosta o que esta em conj_f que o conj_e nao tem
print(conj_e.difference(conj_f))


print()
# metodo symmetric_difference tras so os elementos
# que nao se repetem em comparacao a outro conjunto


conj_g = {'A', 'c', 'b', 'L', 'F', 'g'}
conj_h = {'A', 'c', 'D', 'L', 'E', 'g'}

print(conj_g.symmetric_difference(conj_h))


print()
# subconjuntos
# metodo issubset verifica se um conjunto e
# subconjunto do outro ou ceja o que tem em um conjunto
# pode ser encontrado dentro do outro conjunto.

conj_n = {0, 1, 2, 3, 4}
conj_m = {0, 1, 2, 3, 4, 5, 6, 7, 8}

# false porque tudo o que tem dentro de conj_m
# nao esta dentro de conj_n
print(conj_m.issubset(conj_n))

# true porque tudo o que tem dentro de conj_n
# esta dentro de conj_m
print(conj_n.issubset(conj_m))



print()

# metodo issuperset verifica se um conjunto nao
# tem todos os elementos dentro de outro conjunto

# true porque tudo o que tem dentro de conj_n
# esta dentro de conj_m
print(conj_n.issubset(conj_m))
 
# false porque tudo o que tem dentro de conj_m
# nao esta dentro de conj_n
print(conj_m.issubset(conj_n))



print()

# metodo isdisjoint verifica se existe algum
# elemento em comum entre os conjuntos em comparacao

conj_t = {0, 1, 2, 3}
conj_s = {4, 5, 6, 7}
conj_x = {0, 5, 8, 9}

# conj_t e conj_s sao distintos
print(conj_t.isdisjoint(conj_s))


# conj_t e conj_s sao distintos
print(conj_s.isdisjoint(conj_x))





