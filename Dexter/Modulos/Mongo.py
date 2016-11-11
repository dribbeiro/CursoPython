#!/usr/bin/python
# arquivo: Mongo.py

from pymongo import MongoClient

class Mongo:


    def __init__(self):
        self.client = MongoClient('localhost')
        self.db = self.client['Dexter']


    def fila(self):
        return self.db.fila.find().count()


    def pendentes(self):
        return self.db.fila.find({"status": 0})
        
