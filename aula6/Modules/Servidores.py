#!/usr/bin/python
# arquivo: Servidores.py

from Modules.Banco import exec_query, exec_select
from Modules.Docker import criar_container, rm_container, ip_container


def cadastrar_servidor():
    servidor = {}
    servidor['nome'] = raw_input('Nome do Servidor: ')
    servidor['descricao'] = raw_input('Descricao Servidor: ')

    try:
        criar_container(servidor.get('nome'))
        servidor['ip'] = ip_container(servidor.get('nome'))

        sql = "INSERT INTO servidores (nome,descricao,ip) VALUES ('{0}','{1}','{2}')"
        sql = sql.format(servidor.get('nome'),
                         servidor.get('descricao'),
                         servidor.get('ip'))
        exec_query(sql)

    except Exception as e:
        print e


def remover_servidor():
    print 'Remover selecionado'
    listar_servidores()
    svr = raw_input('Nome do Servidor: ')
    
    try:
        rm_container(svr)

        sql = "DELETE FROM servidores WHERE nome = '{0}'"
        sql = sql.format(svr)
        exec_query(sql)

    except Exception as e:
        print e


def listar_servidores():
    print 'Listar selecionado'
    sql = "SELECT * FROM servidores"
    registros = exec_select(sql)
    for r in registros:
        print 'Servidor: %s - Descricao: %s - Ip: %s' % (r[1], r[2], r[3])
