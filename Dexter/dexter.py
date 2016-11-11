#!/usr/bin/python
# arquivo: dexter.py

from Classes.Produto import Produto
from Classes.Cliente import Cliente
from Classes.Servico import Servico
import sys, os

p = Produto()
c = Cliente()
s = Servico()


def switch(x):
    os.system('clear')
    funcoes =   {
                    1: c.cadastrar,
                    2: c.buscar,
                    3: p.cadastrar,
                    4: p.buscar,
                    5: s.cadastrar,
                    6: s.buscar,
                    7: sair
                }

    funcoes[x]()


def sair():
    sys.exit()


while True:
    print '1 - Cadastrar Cliente'
    print '2 - Buscar Cliente'
    print '3 - Cadastrado Produto'
    print '4 - Buscar Produto'
    print '5 - Cadastrar Servico'
    print '6 - Buscar Servico'
    print '7 - Sair'

    opt = input('Opcao: ')
    switch(opt)
