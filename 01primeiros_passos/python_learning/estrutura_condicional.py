
# estrutura if:
a = 67
A = 97

if a == A:
  print(True)
SystemExit()
print("")
# estrutura if else:

if a != A:
  print(False)
else:
  print(True)
SystemExit()
print("")
# estrutura if else elsif

if A > a:
  print('"A" e maior')
elif a < A:
  print('"a" e maior')
else:
  print("Os dois sao iguais")
SystemExit()
print("")
# estrutura if aninhada

if A < a:
  print("'A' e menor")
  if A > a:
    print("'A' e maior")
    if A == a:
      print("'A' e 'a' sao iguais")
      SystemExit()

# estrutura if ternario
status = True if A > a else False
print(status)
