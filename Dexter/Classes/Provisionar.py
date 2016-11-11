#!/usr/bin/python
# arquivo: Provisionar.py

from Classes.Servico import Servico
from Classes.Docker import Docker

class Provisionar:


    def start(self,sid):
        s = Servico()
        servico = s.buscar(sid)
        print 'ID do Servico: ', servico.id
        print 'Contratante: ', servico.cliente.nome
        print 'Produto: ', servico.produto.nome
        print 'Date: ', servico.date
