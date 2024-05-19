
# oset e uma estrutura de dados que elimina as duplicatas
# mas nao garante a ordem de precedencia

languages = {'Python', 'Java', 'Delphi', 'Fortran', 'Java'}

print(languages)

# no codigo abaixo , eliminaremos as strings em duplicatas
# ordenaremos em ordem crescente as strings e mostraremos
# o indice de cada string.
frutas = ['Pera', 'Maca', 'Uva', 'limao', 'Uva', 'Tangerina', 'Uva']

remove_duplicates = set(frutas)

for i, value in enumerate(sorted(remove_duplicates, key=lambda x: len(x))):
    print(f' {i} - {value}')
    

# convertendo o set para uma lista para usar os metodos
# da lista e consumir os dados disponiveis
new_list = list(set(frutas))

print(len(new_list))
print(new_list[0])
print(new_list[3])
print(new_list[-1])
print(new_list)
print(sorted(new_list, key=lambda i: len(i)))




 