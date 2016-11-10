#!/usr/bin/python
# arquivo: produtos.python

class Produtos:

    def __init__(self, nome="", descricao="", categoria="", preco=0):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.__quant = 10

    def __str__(self):
        texto =  'Nome: %s\n' % self.nome
        texto += 'Descricao: %s\n' % self.descricao
        texto += 'Categoria: %s\n' % self.categoria
        texto += 'Preco: %s\n' % self.preco
        return texto


    def vender(self):
        self.quant -= 1
        print "Quanto Atl: ", self.quant


if __name__ == '__main__':
    p = Produtos('Sapato', 'Kanui', 'Vest', 50)
    print p
