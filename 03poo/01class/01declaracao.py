
# construcao de uma calss bicicleta

class Bicicleta:
    # O def indica que e um metodo da class
    # O __init__ e o construtor da class
    # O self representa o atributo da class, assim como o 'this' no javascript
    # mas diferentemente do javascript o self no python pode ter outro nome qualquer 
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    # definindo metodos da class
    
    def buzinar(self):
        return 'Prinn... Prinnn...'
    
    def pedalar(self):
        return 'bicicleta andando!'
    
    def freiar(self):
        return 'bicicleta parada.'

    # retornando os valores da class de forma direta
    # def __str__(self):
    #     return f'Bicicleta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}' 

    # retornando os valores da class de forma dinamica
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
        


# instanciando a class Bicicleta

bike = Bicicleta('Vermelha', 'Caloi', '2022', '1.200')

print(bike.modelo)
print(bike.cor)

print()

print(bike.buzinar())
print(bike.pedalar())
print()

print(bike.freiar())
print()

print(bike)


