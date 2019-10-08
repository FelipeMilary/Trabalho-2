from peewee import*
from Cliente import Cliente
from Endereco import Endereco
from BaseModel import*
import os

class Professor(Cliente):
    codigoDocente = CharField()

    def __str__(self):
        return super().__str__() + "\nCodigo do Docente: " + self.codigoDocente

if __name__ == '__main__':
    if os.path.exists(arquivo):
        os.remove(arquivo)

    db.connect()
    db.create_tables([Endereco, Professor])
    endereco = Endereco.create(cep=99666444, logradouro="Rua querty", numero=123, bairro="Itoupava Central", municipio="Blumenau", estado="SC")

    professor = Professor.create(nome="kjhostip ghsrtstk", endereco=endereco, email="teste@teste.com", codigoDocente="31654849")
    
    print(professor)
    