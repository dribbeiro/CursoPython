#!/usr/bin/python
# arquivo: Docker.py

from Modulos.SSH import SSH

class Docker(SSH):


    def criar(self, nome, image):
        cmd = 'docker run -tdi --name {0} {1} /bin/bash'.format(nome, image)
        self.exec_comandos(cmd)
