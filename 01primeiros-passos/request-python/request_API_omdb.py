# O comando import foi utilizado para importarmos as bibliotecas:

import requests
import json

# Aqui mantivemos a chave da API recebida por e-mail na variável API_KEY:

API_KEY = "2bcb9bf2"

# Ao utilizarmos o comando input, o sistema apresenta uma caixa de diálogo
#que permite que a variável 'buscar' receba o termo digitado pelo usuário:

buscar = input("Informe o título procurado: ")

# A seguir, a variável chamada 'url' recebe uma URL com as variáveis 'buscar'
#e 'API_KEY'. Observe que a letra 'f', no início, possibilita que utilizemos 
#as variáveis integradas à nossa cadeia de caracteres: 

url = f"https://www.omdbapi.com/?s={buscar}&apikey={API_KEY}"

# Realizamos a requisição passando como parâmetro a URL:

resultados = requests.get(url)

# Aqui verificamos se o resultado da conexão é 200, que indica o sucesso
#da solicitação:

if resultados.status_code == 200:
	catalogo = resultados.json()

    # Agora temos o resultado completo da pesquisa. Faça o teste imprimindo 
    #os resultados com o comando print e, em seguida, visualize o resultado
    #na ferramenta 
    #JSON Parser (https://jsononline.net/json-parser).
    # Agora chegou o momento de iterar a lista:

	for filme in catalogo['Search']:

         # Criamos duas variáveis, 'tipo' e 'titulo'. Sinta-se convidado 
         #para testar o ano e o imdbID:

		tipo = filme["Type"]
		titulo = filme["Title"]

         # O resultado poderá ser trabalhado de diversas formas para 
         #facilitar a visualização do usuário. Aqui estamos exibindo 
         #somente os filmes:

		if tipo == "movie":
			print(f"Tipo: {tipo} - Título: {titulo}")


# sugestions of search Guardians of the Galaxy
