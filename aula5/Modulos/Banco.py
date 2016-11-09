#!/usr/bin/python
# arquivo. Banco.py

import psycopg2
import MySQLdb


def getConn():
    con = MySQLdb.connect(host='localhost', db='python', user='root', passwd='123456')
#   con = psycopg2.connect('host=localhost dbname=aulapdo user=pdo password=123456')
    cur = con.cursor()
    return (con, cur)

def exec_query(query):
    try:
        con, cur = getConn()
        cur.execute(query)
        con.commit()
        print 'Query Executada com Sucesso'
    except Exception as e:
        con.rollback()
        print 'Erro ao Executar Query: ',e
    finally:
        print 'Encerrando Conn'
        cur.close()
        con.close()


def exec_select(query):
    con, cur = getConn()
    cur.execute(query)
    registros = cur.fetchall()
    return registros
    
    

