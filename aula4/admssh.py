#!/usr/bin/python
# arquivo: admssh.py

import sys, os
from Modulos.Usuarios import cadastrar_usuario, remover_usuario, listar_usuarios, autenticar_usuario
from Modulos.Servidores import cadastrar_servidor, remover_servidor, listar_servidores


def menu():
    print '1 - Cadastro User'
    print '2 - Remover User'
    print '3 - Listar Users'
    print '4 - Autenticar User'
    print '5 - Cadstrar Servidor'
    print '6 - Remover Servidor'
    print '7 - Listar Servidores'
    print '8 - Sair'
    try:    
        opcao = input('Escolha uma opcao: ')
        return opcao
    except Exception as e:
        print 'Digite um numero de 1-8'
        return 0


def sair():
    print 'Bye...'
    sys.exit()


def switch(x):
    os.system('clear')
    funcoes = {1: cadastrar_usuario,
               2: remover_usuario,
               3: listar_usuarios,
               4: autenticar_usuario,
               5: cadastrar_servidor,
               6: remover_servidor,
               7: listar_servidores,
               8: sair}
    try:
        funcoes[x]()
    except Exception as e:
        print 'Opcao do menu invalida', e

while True:
    opcao = menu()
    switch(opcao)
