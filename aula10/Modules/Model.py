#!/usr/bin/python
# arquivo: Model.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from random import randint
from datetime import datetime

engine = create_engine('mysql://root:123456@localhost/ADMSSH')
# engine = create_engine('sqlite:///banco.db')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String(20))
    senha = Column(String(20))
    tokens = relationship('Tokens')

class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(120))
    descricao = Column(String(120))
    ip = Column(String(20))

class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    servidores_id = Column(Integer, ForeignKey('servidores.id'))
    token = Column(String(20), default=randint(1000,9999))
    data = Column(DateTime, default=datetime.now())
    servidores = relationship('Servidores')
    usuarios = relationship('Usuarios')

if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
        token = Tokens()
        u = session.query(Usuarios).filter(Usuarios.id==2).first()
        u.tokens.append(token)
        #s = Servidores()
        #s.nome = 'NovoServidor'
        #s.ip = '172.17.0.2'
        s = session.query(Servidores).filter(Servidores.id==5).first()
        token.servidores_id = s.id
        session.add(token)
        session.commit()
    except Exception as e:
        print e
