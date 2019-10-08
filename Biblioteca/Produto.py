from abc import ABC, abstractmethod
from peewee import *
from BaseModel import *
import os

class Produto(BaseModel):
    nome = CharField()
    preco = DoubleField()

    def __str__(self):
        return "Nome:  " + self.nome + "\nPreço: R$" + str(self.preco)

if __name__ == "__main__":
    if os.path.exists(arquivo):
        os.remove(arquivo)
    db.connect()
    db.create_tables([Produto])
    saida = Produto.create(nome="Livreto educativo", preco=3.65)

    print(saida)
    