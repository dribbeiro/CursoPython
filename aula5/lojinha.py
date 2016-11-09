#!/usr/bin/python
# arquivo: lojinha.py

import os, sys
from Modulos.Usuarios import cadastrar_usuario, remover_usuario, listar_usuarios, alterar_usuario


def menu():
    print '1 - Cadastro User'
    print '2 - Remover User'
    print '3 - Alterar User'
    print '4 - Listar Users'
    print '5 - Sair'
    try:    
        opcao = input('Escolha uma opcao: ')
        return opcao
    except Exception as e:
        print 'Digite um numero de 1-4'
        return 0


def sair():
    print 'Bye...'
    sys.exit()


def switch(x):
    os.system('clear')
    funcoes = {1: cadastrar_usuario,
               2: remover_usuario,
               3: alterar_usuario,
               4: listar_usuarios,
               5: sair}
    try:
        funcoes[x]()
    except Exception as e:
        print 'Opcao do menu invalida', e

while True:
    opcao = menu()
    switch(opcao)
