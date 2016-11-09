#!/usr/bin/python
# arquivo: Usuarios.py

from Modules.Banco import exec_query, exec_select


def cadastrar_usuario():
    print 'Cadastro selecionado'
    novo = {}
    novo['login'] = raw_input('Digite o login: ')
    novo['senha'] = raw_input('Digite a senha: ')

    sql = "INSERT INTO usuarios (login,senha) VALUES ('{0}','{1}')"
    sql = sql.format(novo.get('login'),
                     novo.get('senha'))
    exec_query(sql)

def alterar_usuario():
    print 'Alterar selecionado'
    listar_usuarios()
    userID = raw_input('ID do Usuario: ')
    novo = {}
    novo['login'] = raw_input('Digite o login: ')
    novo['senha'] = raw_input('Digite a senha: ')

    sql = "UPDATE usuarios SET login = '{0}', senha = '{1}' \
                           WHERE id = {2}"

    sql = sql.format(novo.get('login'),
                     novo.get('senha'),
                     userID)
    exec_query(sql)


def remover_usuario():
    print 'Remover selecionado'
    listar_usuarios()
    user = raw_input('ID do Usuario: ')

    sql = "DELETE FROM usuarios WHERE id = '{0}'"
    sql = sql.format(user)
    exec_query(sql)


def listar_usuarios():
    print 'Listar selecionado'

    sql = "SELECT * FROM usuarios"
    registros = exec_select(sql)
    for r in registros:
        print 'ID: %s - Login: %s - Senha: %s' % (r[0], r[1], r[2])
