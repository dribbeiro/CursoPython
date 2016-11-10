#!/usr/bin/python
# arquivo: mongo.py

from pymongo import MongoClient

def conn_mongo():
    try:
        client = MongoClient("localhost")
        db = client['python']
        return db
    except Exception as e:
        print e

def cadastrar_user():
    db = conn_mongo()
    novo = {}
    novo['nome'] = raw_input('Nome Usuario: ')
    novo['profissao'] = raw_input('Profissao Usuario: ')
    novo['skills'] = []
    novo['endereco'] = []
    novo['dependentes'] = []
    db.usuarios.insert(novo)
    print 'Dados Cadastrados'


def listar_users():
    db = conn_mongo()
    usuarios = db.usuarios.find()
    for u in usuarios:
        print "============================="
        print 'Nome: ', u.get('nome')
        print 'Profissao: ', u.get('profissao')
        print 'Skills: ', u.get('skills')
        print 'Endereco: ', u.get('endereco')
        print 'Dependentes: ', u.get('dependentes')


def remover_user():
    listar_users()
    db = conn_mongo()
    usuario = {}
    usuario['nome'] = raw_input('Nome Usuario: ')
    db.usuarios.remove(usuario)
    print 'Dados Removidos'

def add_skill():
    db = conn_mongo()
    listar_users()
    usuario = {}
    usuario['nome'] = raw_input('Escolha Usuario: ')
    print 'Digite #sair para Sair'
    while True:
        skill = raw_input('Digite a Skill: ')
        if skill == '#sair':
            break
        db.usuarios.update(usuario, {"$addToSet": {"skills": skill}})


def rm_skill():
    db = conn_mongo()
    listar_users()
    usuario = {}
    usuario['nome'] = raw_input('Escolha Usuario: ')
    print 'Digite #sair para Sair'
    skill = raw_input('Digite a Skill: ')
    db.usuarios.update(usuario, {"$pull": {"skills": skill}})


def add_endereco():
    db = conn_mongo()
    listar_users()
    usuario = {}
    usuario['nome'] = raw_input('Escolha Usuario: ')
    endereco = {}
    endereco['rua'] = raw_input('Digite a Rua: ')
    endereco['cidade'] = raw_input('Digite a Cidade: ')
    db.usuarios.update(usuario, {"$set": {"endereco": endereco}})


def add_dependente():
    db = conn_mongo()
    listar_users()
    usuario = {}
    usuario['nome'] = raw_input('Escolha Usuario: ')
    dependente = {}
    dependente['nome'] = raw_input('Nome Dependente: ')
    dependente['idade'] = input('Idade Dependente: ')
    db.usuarios.update(usuario, {"$addToSet": {"dependentes": dependente}})


def att_dependente():
    db = conn_mongo()
    listar_users()
    usuario = {}
    usuario['nome'] = raw_input('Escolha Usuario: ')
    dependente = {}
    dependente['nome'] = raw_input('Nome Dependente: ')
    dependente['idade'] = input('Idade Dependente: ')

    where = {
                "nome": usuario.get('nome'),
                    "dependentes.nome": dependente.get('nome')
            }
    update = {"$set": {"dependentes.$.idade": dependente.get('idade')}}
    db.usuarios.update(where, update)


def switch(x):
    functions = {
                    1: cadastrar_user,
                    2: remover_user,
                    3: listar_users,
                    4: add_skill,
                    5: rm_skill,
                    6: add_endereco,
                    7: add_dependente,
                    8: att_dependente
                }
    functions[x]()


if __name__ == '__main__':
    while True:
        opt = input('Opcao: ')
        switch(opt)
