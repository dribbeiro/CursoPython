

from Modulos.Mongo import Mongo

class Daemon:


    def main(self):
        m = Mongo()
        print 'Servico na Fila: ', m.fila()
        pendentes = m.pendentes()
        for p in pendentes:
            print 'ID do Servico: ', p.get('servico')
            print 'Status do Servico: ', p.get('status')


if __name__ == '__main__':
    d = Daemon()
    d.main()
