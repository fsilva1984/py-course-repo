
# propriedades
# as propriedades que definimos em uma classe
# parece com um metodo mas se comporta diferente
# a meneira visivel de diferenciarmos em um codigo python
# e a atribuicao do @property
# a principal diferencao entre o metodo e uma propriedade
# e que a propriedade guarda uma informacao ja o metodo
# realiza uma acao. 


class Foo:
  def __init__(self, x=None):
    self._x = x

  @property
  def x(self):
    return self._x or 0

  # o setter e uma funcao acessora para uma propriedade
  # como a propriedade nao pederia receber um valor diretamente
  # o setter recebe o valor e define na propriedade
  @x.setter
  def x(self, value):
    self._x += value


foo = Foo(20)

# Aqui nao precisamos invocar o x com parenteses
# pois o python compreende que se trata de uma
# propriedade da class caso contrario,
# sem o @property o print seria dessa forma print(foo.x())
print(foo.x)

foo.x = 30

print(foo.x)
