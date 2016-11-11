#!/use/bin/python
# arquivo: Cloud.py

from Servidor import Servidor
from VNC import VNC

class Cloud(Servidor):
    
    def __init__(self):
        self.cpu = 4
        self.memoria = 512
        self.disco = 50

if __name__ == '__main__':
    cloud = Cloud()
    cloud.contratar_cpu()
    print cloud.cpu
    print cloud.memoria
    print cloud.disco
