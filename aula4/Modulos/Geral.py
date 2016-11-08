#!/usr/bin/python
# arquivo: Geral.py

import json


def ler_json():
    with open('banco.json', 'r') as f:
        arquivo = f.read()
        arquivo = json.loads(arquivo)
        return arquivo


def gravar_json(dicionario):
    with open('banco.json', 'w') as f:
        arq = json.dumps(dicionario)
        f.write(arq)
