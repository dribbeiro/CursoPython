#!/use/bin/python
# arquivo: Fisico.py

from Servidor import Servidor
from IPMI import IPMI

class Fisico(Servidor, IPMI):
    
    def __init__(self):
        self.cpu = 2
        self.memoria = 512
        self.memoria_ocupada = 1
        self.memoria_total = 4
        self.disco = 1024
        self.disco_ocupado = 1
        self.disco_total = 4


    def contratar_cpu(self):
        print 'Voce precisa fazer um upgrade de maquina'


    def contratar_memoria(self):
        if self.memoria_ocupada < self.memoria_total:
            self.memoria_ocupada = 1
            self.memoria += 2048
        else:
            print 'Voce nao tem mais slots disponiveis'   


    def contratar_disco(self):
        if self.disco_ocupado < self.disco_total:
            self.disco_ocupado += 1
            self.disco += 1024
        else:
            print 'Voce nao tem mais slots disponiveis'   
        

if __name__ == '__main__':
    fisico = Fisico()
    fisico.contratar_cpu()
    fisico.contratar_memoria()
    fisico.contratar_disco()
    print fisico.cpu
    print fisico.memoria
    print fisico.disco
    fisico.acesso()
