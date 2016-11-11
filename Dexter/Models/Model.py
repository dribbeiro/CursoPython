#!/usr/bin/python
# arquivo: Model.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine = create_engine('mysql://root:123456@localhost/Dexter')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(120))
    cpf = Column(String(30))
    segmento = Column(String(80))

    servico = relationship('Servicos')

    def __init__(self, cliente=''):
        self.nome = cliente.nome
        self.cpf = cliente.cpf
        self.segmento = cliente.segmento


class Servicos(Base):
    __tablename__ = 'servicos'
    id = Column(Integer, primary_key=True, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    data = Column(DateTime, default=datetime.now())

    produto = relationship('Produtos')


class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(50))
    descricao = Column(String(120))
    imagem = Column(String(50))

    
    def _init_(self, produto=''):
        self.nome = produto.nome
        self.descricao = produto.descricao
        self.imagem = produto.imagem


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    c = Clientes()
    c.nome = 'Joao'
    c.cpf  = '1299383893'
    c.segmento = 'T.I'
    session.add(c)

    p = Produtos()
    p.nome = 'Backup'
    p.descricao = 'Servidor de Backup'
    p.imagem = 'ubuntu'
    session.add(p)
    cliente = session.query(Clientes).filter(Clientes.nome == 'Joao').first()
    produto = session.query(Produtos).filter(Produtos.nome == 'Backup').first()

    s = Servicos()
    s.produto_id = produto.id
    cliente.servico.append(s)
    session.add(s)
    session.commit()
