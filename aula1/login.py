#!/usr/bin/python
# arquivo: login.py

usuarios = ['marvin', 'artur', 'ford', 'ze']
senhas = ['marvinpw', 'arturpw', 'fordpw', 'zepw']

print 'Autenticacao'
user = raw_input('Login: ')
# passw = raw_input('Senha: ')

for u in usuarios:
    if user == u:
        passw = raw_input('Senha: ')
        if passw == senhas[usuarios.index(u)]:
            print 'Logado'
            break
#  ELSE do FOR so eh executado se n acontecer um BREAK dentro do FOR
else:
    print 'Usuario ou Senha Invalido'
