

frutas = ('Damasco', 'Abacaxi', 'Banana', 'Caju', 'Manga', 'Caju', 'Acerola', 'Caju')


# com o metodo count saberemos quantas
# ocorrencias da string 'Caju' existem dentro da tupla
print(frutas.count('Caju'))

# com o metodo index saberemos qual o
# indice da primeira ocorrencia da string 'Caju'
print(frutas.index('Caju'))

# metodo len() para obter o tamanho exato da tupla
print(len(frutas))

# iterando a tpla
for i, fruit in enumerate(frutas):
    print(f' {i} - {frutas[i]}')
