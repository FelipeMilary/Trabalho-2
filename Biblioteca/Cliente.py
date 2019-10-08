from Endereco import Endereco
from abc import ABC, abstractmethod
from peewee import *
from BaseModel import *
import os

class Cliente(BaseModel):
    nome = CharField()
    endereco = ForeignKeyField(Endereco)
    email = CharField()

    def __str__(self):
        return "Nome: " + self.nome + "\nEmail: " + self.email + "\nEndereço: " + str(self.endereco)

if __name__ == "__main__":
    if os.path.exists(arquivo):
        os.remove(arquivo)
    db.connect()
    db.create_tables([Cliente, Endereco])

    endereco = Endereco.create(cep=89035100, logradouro="Rua qwerty", numero=6547, bairro="Itoupava Central", municipio="Blumenau", estado="SC")
    saida = Cliente.create(nome="Perseu da Silva", endereco=endereco, email="teste@teste.com")
    
    print(saida)
