from peewee import *
from Cliente import Cliente
from Endereco import Endereco
from BaseModel import *
import os

class Aluno(Cliente):
    matricula = CharField()

    def __str__(self):
        return super().__str__() + "\nMatricula: " + self.matricula

if __name__ == '__main__':
    if os.path.exists(arquivo):
        os.remove(arquivo)

    db.connect()
    db.create_tables([Endereco, Aluno])
    endereco = Endereco.create(cep=89899999, logradouro="Rua querty", numero=123, bairro="Itoupava Central", municipio="Blumenau", estado="SC")

    aluno = Aluno.create(nome="Gastroark trekat", endereco=endereco, email="teste@teste.com", matricula="31654849")
    print(aluno)