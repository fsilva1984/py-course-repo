
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

# a class galinha nao recebeu a heranca da class Ave.
class Galinha():
 pass

# o polimorfismo sica por conta da funcao "ave_que_voa"
# essa funcao verifica se a instancia tem o metodo "voar"
# e retorna um valor.

def ave_que_voa(instance, voar):
  if hasattr(instance, voar) and callable(instance.voar):
    print(instance.voar())
  else:
    print("Essa ave não vooa")


ave_que_voa(Pardao(), 'voar')
print()

ave_que_voa(Tucano(), 'voar')
print()

ave_que_voa(Galinha(), 'voar')
print()

ave_que_voa(Ave(), 'voar')

