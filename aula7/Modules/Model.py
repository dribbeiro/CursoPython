#!/usr/bin/python
# arquivo: Model.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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

class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(120))
    descricao = Column(String(120))
    ip = Column(String(20))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
#    novo = Usuarios()
#    novo.login = 'PythonAlchemy'
#    novo.senha = 'alchemy'
#    session.add(novo)
#    session.commit()
#    u = session.query(Usuarios).filter(Usuarios.login=="PythonAlchemy").first()
#    u.login = 'Alchemy'
#    session.commit()

#    todos = session.query(Usuarios).all()
#    for u in todos:
#        print u.login
#        print u.senha
