from peewee import*
from Produto import Produto
from BaseModel import*
import os

class Livro(Produto):
    escritor = CharField()
    editora = CharField()
    ano = IntegerField()

    def __str__(self):
        return super().__str__() + "\nEscritor: " + self.escritor + "\nEditora: " + self.editora + " - Ano: " + str(self.ano)

if __name__ == '__main__':
    if os.path.exists(arquivo):
        os.remove(arquivo)

    db.connect()
    db.create_tables([Livro])

    livro = Livro.create(nome="Gato de botas", preco=3.50, escritor="Gtresk itralp", editora="av123", ano=1994)
    
    print(livro)
    