import re
#print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

# ^\([0-9]{2}\)\s9[0-9]{4}[-][0-9]{4}$

pattern = r'^\([0-9]{2}\)\s9[0-9]{4}[-][0-9]{4}$'
tel = '(21) 98888-8888'
result = re.search(pattern, tel) 

if result:
  print(True)
else:
  print(False)


class Pet:
  def __init__(self, cor, raca, idade):
    self.cor = cor
    self.raca = raca
    self.idade = idade
    
  def __str__(self) -> str:
    return f'{self.__class__.__name__}: {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])}'


class Gato(Pet):
  pass

persa = Gato('Amarelo', 'Persa', '1.3')

print()
print(persa)


class Coelho(Pet):
  pass

class Cachorro(Pet):
  def __init__(self, cor, raca, idade, port_grande=False):
    super().__init__(cor, raca, idade)
    self.port_grande = port_grande


saobernado = Cachorro('castanho', 'sao bernado', '2 anos', True)

print()
print(saobernado)

