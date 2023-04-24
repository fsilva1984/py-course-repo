
### Calculadora IMC 


array = [
  "Desnutricao", 
  "Abaixo do Peso", 
  "Peso normal", 
  "Acima do Peso",
  "Obesidade Grau 1",
  "Obesidade Grau 2",
  "Obesidade Grau 3",
]

print("")


peso = float(input("Peso: "))
print("")

altura = float(input("Altura: "))

result = peso / (altura **2)
print("")


if result < 16.9:
  print("Resultado:", array[0])

elif result > 17 and result <  18.4:
  print("Resultado:", array[1])

elif result > 18.5 and result < 24.9:
  print("Resultado:", array[2])

elif result > 25 and result < 29.9:
  print("Resultado:", array[3])

elif result > 30 and result < 34.9:
  print("Resultado:", array[4])

elif result > 35 and result < 40:
  print("Resultado:", array[5])

else:
  print("Resultado:", array[6])

print("")

print(''' 
------------------------------------------------------
  Tabela IMC de Classificação do IMC segundo a OMS

  < 16	Magreza Grau III

  16,0 a 16,9	Magreza Grau II

  17,0 a 18,4	Magreza Grau I

  18,5 a 24,9	Adequado

  25,0 a 29,9	Pré-Obeso

  30,0 a 34,9	Obesidade Grau I

  35,0 a 39,9	Obesidade Grau II

  >= 40	Obesidade Grau III
------------------------------------------------------
''')

print("")