#!/usr/bin/python
# arquivo: Usuarios.py

from Modulos.Geral import ler_json, gravar_json


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
