


# lembrando, apois o ultimo elemento dentro
# da tupla deve se finalizar co  virgula
# para que o interpretador do python nao a
# confunda com uma ordem de presedencia

frutas = ('Damasco', 'Abacaxi', 'Banana', 'Caju', 'Manga',)

print(frutas[2])
print(frutas[3])
print(frutas[4])

print()

# do inicio ao fim da tupla
print(frutas[:])

# do inicio ao indice 2
print(frutas[:2])

# do indice 2 ate o fim da tupla
print(frutas[2:])

# do inicio ao fim pulando de 2 em 2
print(frutas[::2])

# inicia no indice 1 ate fim pulando de 2 em 2
print(frutas[1::2])

print()

# numeros negatigos sao usados quando querremos
# deixar de fora elemento do final da tupla

# deixa de fora o ultimo elemento
print(frutas[:-1])

# deixaremos de fora o elemento do indice 0
# e os dois ultimos elementos da tupla
print(frutas[1:-2])

# deixaremos de fora os dois primeiros elementos e os dois ultimos
print(frutas[2:-2])

# deixaremos de fora os dois ultimos elementos ao passo de 2 em 2
print(frutas[:-2:2])