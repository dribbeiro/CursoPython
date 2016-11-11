#!/usr/bin/python
# arquivo: ProdutoDAO.py

from Models.Model import session, Produtos


class ProdutoDAO:
    

    def salvar(self, produto):
        try:
            p = Produtos(produto)
            session.add(p)
            session.commit()
            print 'Produto Cadastrado com Sucesso'
        except Exception as e:
            session.rollback()
            print 'Falha ao Cadastrar Produto ', e


    def busca(self, id):
        try:
            produto = session.query(Produtos).filter(Produtos.id==id).first()
            return produto
        except Exception as e:
            'Produto Inexsitente'


