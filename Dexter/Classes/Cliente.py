#!/usr/bin/python
# arquivo: Cliente.py

from Classes.ClienteDAO import ClienteDAO

class Cliente:


    def __init__(self, nome='',cpf='', segmento=''):
        self.nome = nome
        self.cpf = cpf
        self.segmento = segmento

    
    def cadastrar(self):
        self.nome = raw_input('Nome do Cliente: ')
        self.cpf = raw_input('CPF do Cliente: ')
        self.segmento = raw_input('Segmento do Cliente: ')

        cdao = ClienteDAO()
        cdao.salvar(self)


    def buscar(self):
        self.id = raw_input('Escolha o ID do Cliente: ')

        cdao = ClienteDAO()
        cliente = cdao.busca(self.id)

        print cliente.nome
        print cliente.cpf
        print cliente.segmento
