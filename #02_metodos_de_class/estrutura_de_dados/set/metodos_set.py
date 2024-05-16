
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

