import requests
import json

# A variável 'API_KEY' armazenará a nossa chave da API:
API_KEY = "25da137932c8a699634fb8e9d5cecba3"

# No exemplo a seguir, buscamos apenas a cidade de São Paulo:
url = f"https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo&appid={API_KEY}"

# Aqui realizamos uma requisição utilizando o parâmetro GET e a 
#nossa URL que contém a chave:
requisicao = requests.request("GET", url)

# Transformamos os resultados em um JSON:
resultados = json.loads(requisicao.text)

# Apresentamos os resultados:
#print (resultados)


# Conforme explicado na documentação da API, ao tratar de unidades 
#de medida de temperatura, o sistema considera a escala Kelvin como 
#padrão. Por isso, faremos algumas conversões.

# Em nosso dicionário, acessamos o nó chamado 'main' e, em seguida, a 'temp':
kelvin = float(resultados["main"]["temp"])

# Convertemos para Fahrenheit:
fahrenheit = round(kelvin * 1.8 - 459.67, 2)

# E, em seguida, para Celsius. Observe que a conversão poderia ter sido 
#imediata de Kelvin para Celsius:
celsius = round(kelvin - 273.15, 2)

# Imprimimos o resultado:
print(f"Kelvin {kelvin} / Fahrenheit {fahrenheit} / Celsius {celsius}\n")

# Agora, imagine que estamos em frente a um painel e nele podemos 
#visualizar uma lista de cidades e suas temperaturas atuais, mínima 
#e máxima.

# Consumir essa API poderia ser uma opção razoável:
cidades = {"Sao Paulo", "San Francisco", "Paris", "Tokyo"}

# O comando for é utilizado para iterar os itens da nossa lista:
for cidade in cidades:
  # O resultado de cada requisição é armazenado em nossa variável 
  #‘resultados’:
  resultados = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric")

  # Transformamos o resultado em um arquivo JSON:
  catalogo = resultados.json()

  # Selecionamos os itens desejados:
  TEMPERATURA = catalogo["main"]["temp"]
  TEMP_MIN = catalogo["main"]["temp_min"]
  TEMP_MAX = catalogo["main"]["temp_max"]
  PAIS = catalogo["sys"]["country"]
  CIDADE = catalogo["name"]

  # Por fim, montamos o resultado para a impressão:
  print(f"Cidade: {CIDADE} ({PAIS}) - °C {TEMPERATURA} (Min °C {TEMP_MIN} / Max °C {TEMP_MAX})")
