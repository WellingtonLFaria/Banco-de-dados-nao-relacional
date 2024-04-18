from pymongo import MongoClient
from pprint import pprint

class ListarUsuarios:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Usuarios

    def listar(self):
        data = self.collection.find()
        self.usuarios = [usuario for usuario in data]
        for usuario in self.usuarios:
            print(self.usuarios.index(usuario), end=" - ")
            pprint(usuario)
