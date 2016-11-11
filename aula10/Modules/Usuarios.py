#!/usr/bin/python
# arquivo: Usuarios.py

from Modules.Model import session, Usuarios, Tokens


def cadastrar_usuario():
    print 'Cadastro selecionado'
    novo = Usuarios()
    novo.login = raw_input('Digite o login: ')
    novo.senha = raw_input('Digite a senha: ')
    
    try:
        session.add(novo)
        session.commit()
        print 'Usuario Cadastrado'
    except Exception as e:
        print e

def autenticar_usuario():
    print 'Autenticar'
    login = raw_input('Digite o login: ')
    senha = raw_input('Digite a senha: ')

    usuario = session.query(Usuarios).filter(Usuarios.login==login, Usuarios.senha==senha).first()

    if usuario:
        print 'Usuario Autenticado'
        t = Tokens()
        usuario.tokens.append(t)
        session.add(t)
        session.commit()
        print 'Token de Acesso: ', t.token
    else:
        print 'Login ou Senha Invalidos'

def remover_usuario():
    print 'Remover selecionado'
    listar_usuarios()
    user = raw_input('ID do Usuario: ')
    
    try:
        usuario = session.query(Usuarios).filter(Usuarios.id==user).first()
        session.delete(usuario)
        session.commit()
        print 'Usuario Removido'
    except Exception as e:
        print e


def listar_usuarios():
    print 'Listar selecionado'

    registros = session.query(Usuarios).all()
    print type(registros)
    for r in registros:
        print 'ID: %s - Login: %s - Senha: %s' % (r.id, r.login, r.senha)
