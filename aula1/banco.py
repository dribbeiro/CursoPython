#!/usr/bin/python
# arquivo: banco.py

saldo = 0
valor = input('Digite um valor: ')
saldo += valor

while saldo < 0:
    print 'Juros'
    valor = input('Valor deposito: ')
    saldo += valor

print 'Saldo Zerado'
