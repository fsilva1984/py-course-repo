
# variaveis de class e variaveis de instancias



class Escola:
  
  course = "Python"
  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  def curso(self):
    return f'Aluno - {self.name}\nID - {self.id}\nCurso - {self.course}'
  
  def __str__(self):
    return f'{self.__class__.__name__}: {", ".join([f"{key}:{value}" for value, key in self.__dict__.items()])}'




InfoTech = Escola('Flavio', 12435)

print(InfoTech.curso())


