from peewee import*
from BaseModel import*
import os

class Endereco(BaseModel):
    cep = IntegerField()
    logradouro = CharField()
    numero = IntegerField()
    bairro = CharField()
    municipio = CharField()
    estado = CharField()

    def __str__(self):
        return self.logradouro + ", " + str(self.numero) + "\nBairro: " + self.bairro + "\nMunicipio: " + self.municipio + "/" + self.estado + " CEP: " + str(self.cep)

if __name__ == "__main__":
    if os.path.exists(arquivo):
        os.remove(arquivo)

    db.connect()
    db.create_tables([Endereco])
    endereco = Endereco.create(cep=89035100, logradouro="Rua nordeste", numero=112, bairro="Vila Itoupava", municipio="Blumenau", estado="SC")

    print(endereco)
