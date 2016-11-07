#!/usr/bin/python
# arquivo: menu.py

usuarios = []

while True:
    print '1 - Cadastro User'
    print '2 - Remover User'
    print '3 - Listar Users'
    print '4 - Autenticar'
    print '5 - Sair'
    opcao = input('Escolha uma opcao: ')

    if opcao == 1:
        print 'Cadastro selecionado'
        novo = {}
        novo['login'] = raw_input('Digite o usuario: ')
        novo['senha'] = raw_input('Digite a senha: ')
        usuarios.append(novo)
        print 'Usuario Cadastrado'

    elif opcao == 2:
        print 'Remover selecionado'
        user = raw_input('Nome do Usuario: ')

        for u in usuarios:
            if u.get('login') == user:
                usuarios.remove(u)
                print 'Usuario Removido'
                break
        else:
            print 'Usuario nao encontrado'

    elif opcao == 3:
        print 'Listar selecionado'
        for u in usuarios:
            print u

    elif opcao == 4:
        print 'Autenticar Usuario'
        user = raw_input('Digite o usuario: ')
        senha = raw_input('Digite a senha: ')

        for u in usuarios:
            if u.get('login') == user and u.get('senha') == senha:
                print 'Logado'
                break
        else:
            print 'Usuario ou Senha Invalido'

    elif opcao == 5:
        print 'Sair'
        break
    else:
        print 'Opcao invalida'
