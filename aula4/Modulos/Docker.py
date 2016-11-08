#!/usr/bin/python
# arquivo: Docker.py

import json
from Modulos.SSH import exec_comandos


def criar_container(nome):
    cmd = 'docker run -tdi --name {0} debian /bin/bash'.format(nome)
    exec_comandos(cmd)
    print 'Servidor %s Criado...' % nome


def rm_container(nome):
    cmd = 'docker stop {0} && docker rm {0}'.format(nome)
    exec_comandos(cmd)
    print 'Servidor %s Removido' % nome


def ip_container(nome):
    cmd = 'docker inspect {0}'.format(nome)
    ip = json.loads(exec_comandos(cmd))
    return ip[0].get('NetworkSettings').get('IPAddress')
