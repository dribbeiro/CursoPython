#!/usr/bin/python
# arquivo: Servidores.py

from Modules.Model import session, Servidores
from Modules.Docker import criar_container, rm_container, ip_container


def cadastrar_servidor():
    servidor = Servidores()
    servidor.nome = raw_input('Nome do Servidor: ')
    servidor.descricao = raw_input('Descricao Servidor: ')

    try:
        criar_container(servidor.nome)
        servidor.ip = ip_container(servidor.nome)

        session.add(servidor)
        session.commit()

    except Exception as e:
        print e


def remover_servidor():
    print 'Remover selecionado'
    listar_servidores()
    svr = raw_input('Nome do Servidor: ')
    
    try:
        rm_container(svr)

        servidor = session.query(Servidores).filter(Servidores.nome==svr).first()
        session.delete(servidor)
        session.commit()

    except Exception as e:
        print e


def listar_servidores():
    print 'Listar selecionado'
    registros = session.query(Servidores).all()
    for r in registros:
        print 'Servidor: %s - Descricao: %s - Ip: %s' % (r.nome, r.descricao, r.ip)
