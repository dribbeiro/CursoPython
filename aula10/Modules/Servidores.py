#!/usr/bin/python
# arquivo: Servidores.py

from Modules.Model import session, Servidores, Tokens
from Modules.Docker import criar_container, rm_container, ip_container
from datetime import datetime


def cadastrar_servidor():
    t = input('Digite seu Token de Acesso: ')
    acesso = session.query(Tokens).filter(Tokens.token==t).first()

    if not acesso or (datetime.now() - acesso.data).total_seconds() > 3600:
        print 'Token Invalido ou Expirado'

    servidor = Servidores()
    servidor.nome = raw_input('Nome do Servidor: ')
    servidor.descricao = raw_input('Descricao Servidor: ')

    try:
        criar_container(servidor.nome)
        servidor.ip = ip_container(servidor.nome)

        session.add(servidor)
        s = session.query(Servidores).filter(Servidores.nome==servidor.nome).first()
        acesso.servidores_id = s.id
        session.commit()

    except Exception as e:
        session.rollback()
        print e


def remover_servidor():
    print 'Remover selecionado'
    listar_servidores()
    svr = raw_input('Nome do Servidor: ')
    
    try:
        rm_container(svr)

        servidor = session.query(Servidores).filter(Servidores.nome==svr).first()
        t = session.query(Tokens).filter(Tokens.servidores_id==servidor.id).first()
        session.delete(t)
        session.delete(servidor)
        session.commit()

    except Exception as e:
        print e


def listar_servidores():
    print 'Listar selecionado'
    registros = session.query(Servidores).all()
    for r in registros:
        print 'Servidor: %s - Descricao: %s - Ip: %s' % (r.nome, r.descricao, r.ip)
