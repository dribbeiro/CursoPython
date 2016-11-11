#!/usr/bin/python
# arquivo: ClienteDAO.py

from Models.Model import session, Clientes


class ClienteDAO:


    def salvar(self, cliente):
        try:
            novo = Clientes(cliente)
            session.add(novo)
            session.commit()
            print 'Cliente Salvo com Sucesso'
        except Exception as e:
            session.rollback()
            print 'Falha ao Cadastrar Cliente'


    def busca(self, id):
        try:
            cliente = session.query(Clientes).filter(Clientes.id==id).first()
            return cliente
        except Exception as e:
            print 'Cliente Inexistente'
