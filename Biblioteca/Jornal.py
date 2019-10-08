from peewee import*
from Produto import Produto
from BaseModel import*
import os

class Jornal(Produto):
    editora = CharField()
    data = CharField()

    def __str__(self):
        return super().__str__() + "\nEditora: " + self.editora + " - Data: " + self.data

if __name__ == '__main__':
    if os.path.exists(arquivo):
        os.remove(arquivo)

    db.connect()
    db.create_tables([Jornal])

    jornal = Jornal.create(nome="Jornal Amanhã", preco=5.60, editora="Carro verde", data="12/05/19")
    
    print(jornal)
    