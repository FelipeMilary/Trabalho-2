from peewee import*

arquivo = 'bancodedados.db'
db = SqliteDatabase(arquivo)

class BaseModel(Model):
    class Meta:
        database = db