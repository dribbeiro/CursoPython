#!/usr/bin/python
# arquivo strings.py

nome = 'Guido'
idade = 59
texto = ''

# texto += 'Nome do criador do Python '
# texto += nome
# texto += ' Idade: %s' % idade

texto = 'Nome do criado do Python %s \nIdade: %s' % (nome, idade)
texto2 = 'Nome do criado do Python {0} \nIdade: {1}'.format(nome, idade)
print texto
print texto2
