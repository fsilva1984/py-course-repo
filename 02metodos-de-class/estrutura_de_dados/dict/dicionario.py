print()
# estrutura de dicionarios armazena dados por chaves e valores

pessoa = {
    'nome': 'Flavio',
    'idade': 39,
    'sexo': 'Masculino',
    'contatos': {},
}

print(pessoa)
print()

# declarando apartir do contrutor dict 
carros = dict(
    Fabrica='Mercedesbenz',
    Modelo='Classe C 2024'
)
print(carros)
print()

# atribuindo novos valores ao dicionario

pessoa['contatos']['tel'] = '(21)986289078'
pessoa['contatos']['email'] = 'fsilva@gmail.com'

print(pessoa['contatos'])
print()

# sobrescrevendo um valor
pessoa['nome'] = 'Pedro'
pessoa['idade'] = '32'
pessoa['sexo'] = 'Masculino'
pessoa['contatos']['tel'] = '(97)987456924'
pessoa['contatos']['email'] = 'pedrogov@email.com'

print(pessoa)
print()

# dicionarios aninhados

db = {
    'persons':{
        
        'p1':'Miguel Assis nougget',
        'p2':'Anna Martinz cout'
    },
    'address':{
        
        'p1':{
            'street':'Adam first st3',
            'local':'Miamy'
        },
         'p2':{
            'street':'Center Marcovk',
            'local':'New York'
        }
        
    },
    'contacts':{
        'p1':{
            'phone':'552-2343-234',
            'email':'miguel-tom@email.com'
        },
         'p2':{
            'phone':'552-4343-681',
            'email':'martinz-cout@email.com'
        }
    }
}

data = {}

data['name'] = db['persons']['p2']
data['street'] = db['address']['p2']
data['contacts'] = db['contacts']['p2']

print(data)



for value in data:
    print(data[value])








