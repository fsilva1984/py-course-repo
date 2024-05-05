
"""
Operador is para saber se os objetos ocupam
o mesmo local em memoria
"""

CONST_CURSO = 'python3'
teoria_pratica = CONST_CURSO

v1 = CONST_CURSO is teoria_pratica
print(v1)


saldo, limite = 200, 800
v2 = saldo is not limite
print(v2)


a = 97
A = 97

v3 = a is A
print(v3)




