#!/usr/bin/python
# arquivo: ssh.py

import paramiko
from datetime import datetime
import time
import os


def conn_ssh():
    ssh = paramiko.SSHClient()
    #  le arquivo ~/.ssh/know_hosts
    ssh.load_system_host_keys()
    #  aceita chave de servidor automaticamente
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.0.2', username='forlinux', password='4linux')
    return ssh


def ler_comandos():
    with open('comandos.txt', 'r') as f:
        comandos = f.readlines()
        return comandos


def exec_comandos(comms, ssh):
    for comm in comms:
        os.system('clear')
        print 'Executando: ', comm
        dtinicio = datetime.now()
        print 'Inciado as: ', dtinicio.strftime('%d/%m/%Y')
        stdin, stdout, stderr = ssh.exec_command(comm)
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            #  saida padrao
            print stdout.read()
        dtfinal = datetime.now()
        print 'Finalizado as: ', dtfinal.strftime('%d/%m/%Y')
        print 'Tempo de execucao: ', (dtfinal-dtinicio).total_seconds()
        print 'Proximo comando iniciara em 3 segundos'
        time.sleep(3)

exec_comandos(ler_comandos(), conn_ssh())
