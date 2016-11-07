#!/usr/bin/python
# arquivo: variaveis.py

PI = 3.14
cep = 8664465
preco = 10.50
nome = "Produto"
lista = ['Produto 1', 'Produto 2', 'Prodtuo 3']
tupla = ('Produto 1', 'Produto 2', 'Prodtuo 3')
dicionario = {'desc': 'Produto 1', 'valor': 19.90}

print PI
print cep
print preco
print nome
print lista[0]
print tupla[1]
dicionario['valor'] = 21.90
print dicionario.get('valor')
