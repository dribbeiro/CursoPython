#!/usr/bin/python
# arquivo: ServicoDAO.py

from Models.Model import session, Servicos, Clientes, Produtos

class ServicoDAO:
    

    def salvar(self, servico):
        cliente = session.query(Clientes).filter(Clientes.id == servico.cliente).first()
        produto = session.query(Produtos).filter(Produtos.id == servico.produto).first()

        try:
            s = Servicos()
            s.produto_id = produto.id
            cliente.servico.append(s)
            session.add(s)
            session.commit()
            print 'Servico Cadastrado com Sucesso'
        except Exception as e:
            session.rollback()
            print 'Falha ao Cadastrar Servico ', e


    def busca(self, id):
        try:
            servico = session.query(Servicos, Clientes, Produtos) \
                             .filter(Servicos.id==id) \
                             .join(Clientes).join(Produtos) \
                             .first()

            return servico
        except Exception as e:
            print 'Servico Inexistente ', e
