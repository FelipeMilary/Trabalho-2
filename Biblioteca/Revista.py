from peewee import*
from Produto import Produto
from BaseModel import*
import os

class Revista(Produto):
    editora = CharField()
    ano = IntegerField()

    def __str__(self):
        return super().__str__() + "\nEditora: " + self.editora + " - Ano: " + str(self.ano)

if __name__ == '__main__':
    if os.path.exists(arquivo):
        os.remove(arquivo)

    db.connect()
    db.create_tables([Revista])

    revista = Revista.create(nome="Rogue", preco=12.65, editora="Castelo Branco", ano=2008)
    
    print(revista)
    