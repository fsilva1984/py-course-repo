

# metodo antigo e em desuso o %
nome = 'Flavio'
idade = 39
sexo = 'Masculino'
salario= 3.800
tel = '(21)986289078'

print(' nome: %s\n idade: %d\n sexo: %s\n salario: %.3f\n telefone: %s' % (nome, idade, sexo, salario, tel))

print('')
# metodo um pouco mais novo e o .format
# podemos passar entre chaves o indice da variavel
# indicando assim a ordem de exibicao.

#  orderm sequencial
print(' nome: {}\n idade: {}\n sexo: {}\n salario: {}\n telefone: {}' .format(nome, idade, sexo, salario, tel))

print('')
# ordem prioritaria

print(' nome: {0}\n idade: {2}\n sexo: {1}\n salario: {4}\n telefone: {3}' .format(nome, idade, sexo, salario, tel))


print('')
# atribuindo variaveis default

print(' nome: {nome}\n idade: {idade}\n sexo: {sexo}\n salario: {salario}\n telefone: {tel}' .format(nome='Beatriz', idade=22, sexo='Feminino', salario=9.3, tel='(97)998736527'))


print('')
# metodo mais recente e o f

print(f' nome: {nome}\n idade: {idade}\n sexo: {sexo}\n salario: {salario}\n telefone: {tel}')

PI = 3.14159

print('')

print(f'Valor de PI:{PI:.2f}')

print('')
# adicionando espacos

print(f'Valor de PI:{PI:5.2f}')
print(f'Valor de PI:{PI:10.2f}')
print(f'Valor de PI:{PI:15.2f}')
