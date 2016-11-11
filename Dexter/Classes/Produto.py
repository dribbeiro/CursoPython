#!/usr/bin/python
# arquivo: Produto.py

from Classes.ProdutoDAO import ProdutoDAO


class Produto:
    

    def __init__(self, nome='', descricao='', imagem=''):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem


    def cadastrar(self):
        self.nome = raw_input('Nome do Produto: ')
        self.descricao = raw_input('Descricao do Produto: ')
        self.imagem = raw_input('Imagem do Produto: ')

        pdao = ProdutoDAO()
        pdao.salvar(self)


    def buscar(self):
        self.id = raw_input('Escolha o ID do Produto: ')
        
        pdao = ProdutoDAO()
        produto = pdao.busca(self.id)
        self.nome = produto.nome
        self.descricao = produto.descricao
        self.imagem = produto.imagem

        print 'Nome do Produto: ', produto.nome
        print 'Descricao do Produto: ', produto.descricao
        print 'Imagem do Produto: ', produto.imagem


if __name__ == '__main__':
    p = Produto()
    p.cadastrar()
    produto = p.busca()
    print produto.__dict__

