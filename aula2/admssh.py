#!/usr/bin/python
# arquivo: admssh.py

import sys
import json


def ler_json():
    with open('banco.json', 'r') as f:
        arquivo = f.read()
        arquivo = json.loads(arquivo)
        return arquivo


def gravar_json(dicionario):
    with open('banco.json', 'w') as f:
        arq = json.dumps(dicionario)
        f.write(arq)


def menu():
    print '1 - Cadastro User'
    print '2 - Remover User'
    print '3 - Listar Users'
    print '4 - Autenticar'
    print '5 - Sair'
    opcao = input('Escolha uma opcao: ')
    return opcao


def cadastrar_usuario():
    print 'Cadastro selecionado'
    novo = {}
    novo['login'] = raw_input('Digite o usuario: ')
    novo['senha'] = raw_input('Digite a senha: ')
    print 'Usuario Cadastrado'
    banco = ler_json()
    banco.get('usuarios').append(novo)
    gravar_json(banco)


def remover_usuario():
    print 'Remover selecionado'
    user = raw_input('Nome do Usuario: ')
    
    banco = ler_json()
    for b in banco.get('usuarios'):
        if b.get('login') == user:
            print 'Usuario Removido'
            print b
            banco.get('usuarios').remove(b)
            gravar_json(banco)
            break
    else:
        print 'Usuario nao encontrado'


def listar_usuarios():
    print 'Listar selecionado'
    banco = ler_json()
    for b in banco.get('usuarios'):
        print 'Usuario: %s - Senha: %s' % (b.get('login'), b.get('senha'))


def autenticar_usuario():
    print 'Autenticar Usuario'
    user = raw_input('Digite o usuario: ')
    senha = raw_input('Digite a senha: ')
    banco = ler_json()

    for b in banco.get('usuarios'):
        if b.get('login') == user and b.get('senha') == senha:
            print 'Logado'
            break
    else:
        print 'Usuario ou Senha Invalido'


def sair():
    print 'Bye...'
    sys.exit()


def switch(x):
    funcoes = {1: cadastrar_usuario,
               2: remover_usuario,
               3: listar_usuarios,
               4: autenticar_usuario,
               5: sair}
    funcoes[x]()

while True:
    opcao = menu()
    switch(opcao)
