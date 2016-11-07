#!/usr/bin/python
# arquivo: for.py

for i in range(0,10):
    print i

produtos = ['tenis', 'chinelo', 'tv', 'livro']
for i,p in enumerate(produtos):
    print i, " - ", p

dicionario = {'desc': 'Produto', 'valor': 20.50}
for i in dicionario:
    print '%s - %s' % (i,dicionario.get(i))

servidores = ['ldap', 'apache', 'redis']
for s in servidores:
    # startswith / endswith / in (string)
    if s == 'ldap':
        continue        
    print 'Fazendo manuentcao '+s
