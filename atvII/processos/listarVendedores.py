from pymongo import MongoClient
from pprint import pprint

class ListarVendedores:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendedor
    
    def listar(self):
        data = self.collection.find()
        self.vendedores = [vendedor for vendedor in data]
        for vendedor in self.vendedores:
            print(self.vendedores.index(vendedor), end=" - ")
            pprint(vendedor)
