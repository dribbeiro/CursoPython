#!/usr/bin/python
# arquivo: Usuarios.py

from Modulos.Banco import exec_query, exec_select


def cadastrar_usuario():
    print 'Cadastro selecionado'
    novo = {}
    novo['nome'] = raw_input('Digite o Nome: ')
    novo['email'] = raw_input('Digite o Email: ')
    novo['senha'] = raw_input('Digite a senha: ')
    sql = "INSERT INTO usuarios (nome,email,senha) VALUES ('{0}','{1}','{2}')"
    sql = sql.format(novo.get('nome'),
                     novo.get('email'),
                     novo.get('senha'))
    exec_query(sql)

def alterar_usuario():
    print 'Alterar selecionado'
    listar_usuarios()
    userID = raw_input('ID do Usuario: ')
    novo = {}
    novo['nome'] = raw_input('Digite o Nome: ')
    novo['email'] = raw_input('Digite o Email: ')
    novo['senha'] = raw_input('Digite a senha: ')
    sql = "UPDATE usuarios SET nome = '{0}', email = '{1}', senha = '{2}' \
                           WHERE id = {3}"
    sql = sql.format(novo.get('nome'),
                     novo.get('email'),
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
    'Print Usuario Removido Com Sucesso'


def listar_usuarios():
    print 'Listar selecionado'
    sql = "SELECT * FROM produtos"
    registros = exec_select(sql)
    print registros
