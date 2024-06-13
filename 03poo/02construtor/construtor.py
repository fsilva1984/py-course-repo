
# O metodo inicializador das classes no python
# e escrito dessa forma __init__ conhecido por 'dunder init'

class Car:
  
  def __init__(self, cor, modelo, ano, novo=True):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.novo = novo

  def __str__(self) -> str:
    return f'{self.__class__.__name__}: {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])}'

fusca = Car('Blak Pianno', 'Novo Fusca 2.0 TSI ', '2022')

print()

print(fusca.__str__())











  