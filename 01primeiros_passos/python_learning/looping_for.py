
name = 'Flavio'

# apenas o for 
for i in name:
  print(i.upper())

print()

# for com uma condicional if
vogais = 'AEIOU'
for i in name:
  if i.upper() in vogais:
    print(i.upper())

print("")

# for range
for n in range(1, 11):
  print(n, end=(' '))

print("")

# for range contando de 2 em 2
for n in range(0, 12, 2):
  print(n, end=(' '))

print("")