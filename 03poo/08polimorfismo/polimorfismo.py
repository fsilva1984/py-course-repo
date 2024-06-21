
# polimorfismo IMPORTANTE! sem heranca nao ah polimorfismo
# onde um objeto pode apresentar
# deferentes resultados dependendo
# do tipo de dado que ele recebe


class Ave:
  def __init__(self):
    pass
  
  def voar(self):
    return 'Voando...'


class Pardao(Ave):
  pass

class Tucano(Ave):
  pass

# a class galinha recebeu a heranca da
# class Ave, porem teve seu metodo sobrescrito
class Galinha(Ave):
  def voar(self):
    return 'Nao voa'


def ave_que_voa(param):
  print(param.voar())



ave_que_voa(Pardao())
print()

ave_que_voa(Tucano())
print()

ave_que_voa(Galinha())
print()

ave_que_voa(Ave())

