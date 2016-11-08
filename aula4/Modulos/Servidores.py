#!/usr/bin/python
# arquivo: Servidores.py

import json
from Modulos.Geral import ler_json, gravar_json
from Modulos.SSH import exec_comandos
from Modulos.Docker import criar_container, ip_container, rm_container


def cadastrar_servidor():
    servidor = {}
    servidor['nome'] = raw_input('Nome do Servidor: ')
    servidor['descricao'] = raw_input('Descricao Servidor: ')

    criar_container(servidor.get('nome'))
    servidor['ip'] = ip_container(servidor.get('nome'))

    banco = ler_json()
    banco['servidores'].append(servidor)
    gravar_json(banco)


def remover_servidor():
    print 'Remover selecionado'
    servidor = raw_input('Nome do Servidor: ')
    banco = ler_json()
    for b in banco.get('servidores'):
        if b.get('nome') == servidor:
            rm_container(servidor)
            banco.get('servidores').remove(b)
            gravar_json(banco)
            break
    else:
        print 'Servidor nao encontrado'


def listar_servidores():
    print 'Listar selecionado'
    banco = ler_json()
    for b in banco.get('servidores'):
        print 'Servidor: %s - Descricao: %s - Ip: %s' % (b.get('nome'), b.get('descricao'), b.get('ip'))
