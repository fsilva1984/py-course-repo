# heranca simples
# quando uma class herda methodos e propriedades
# de uma class base ou chamada de class pai


class Veiculo:
  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas
    
  def __str__(self) -> str:
    return f'{self.__class__.__name__}: {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])}'


## O extendes e passado entre parenteses
# ou ceja  a class pai da nova class definida 
class Carro(Veiculo):
  pass

# a nova class tambem pode ter os seus proprios
# comportamentos definindos em seu construtor
# sem perder nada da clas pai
# para isso usamos a palavra reservada super()
class Caminhao(Veiculo):
  
  def __init__(self, cor, placa, numero_rodas, carregado=False):
    super().__init__(cor, placa, numero_rodas)
    self.carregado = carregado
    

volvo = Caminhao('Vermelho', '6789KJA', '18', True)

print(volvo)
print()


class Moto(Veiculo):
  pass


kavazak = Moto('Verde', '0012BCE', '2')

print(kavazak)
print()













