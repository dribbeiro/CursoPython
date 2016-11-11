#!/usr/bin/python
# arquivo: Servico.py

from ServicoDAO import ServicoDAO
from Classes.Cliente import Cliente
from Classes.Produto import Produto


class Servico:


    def cadastrar(self):
        self.cliente = input('Escolha o ID do Cliente: ')
        self.produto = input('Escolha o ID do Produto: ')
        sdao = ServicoDAO()
        sdao.salvar(self)


    def buscar(self, id):
        self.id = id
        
        sdao = ServicoDAO()
        servico = sdao.busca(self.id)
        c = Cliente(servico.Clientes.nome, servico.Clientes.cpf, servico.Clientes.segmento)
        p = Produto(servico.Produtos.nome, servico.Produtos.descricao, servico.Produtos.imagem)

        self.cliente = c
        self.produto = p
        self.data = servico.Servicos.data
        
        print 'Servico ID: ', self.id
        print 'Cliente: ', self.cliente.nome
        print 'Produto: ', self.produto.nome
        print 'Data do Servico: ', self.data
