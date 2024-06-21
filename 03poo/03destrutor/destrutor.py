
# alinguagen python disponibiliza o garbage collector
# mas no paradigma poo em paython temos o desconstrutor
# para desalocar a memoria usada pela class
# nao sendo obrigatorio mas podemos usar o __del__ para isso.


class Car:
  
  def __init__(self, cor, modelo, ano, novo=True):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.novo = novo

  def __str__(self) -> str:
    return f'{self.__class__.__name__}: {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])}'
  
  def __del__(self):
    print('A memoria foi limpa!')


# uma instancia tambem chamadaa de objeto da class Car
fusca = Car('Branco', 'Antigo', '1986', False)

print()

print(fusca.__str__())



