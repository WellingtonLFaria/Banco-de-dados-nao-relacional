from pymongo import MongoClient
from pprint import pprint

class ListarVendas:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Venda
    
    def listar(self):
        data = self.collection.find()
        self.vendas = [venda for venda in data]
        for venda in self.vendas:
            print(self.vendas.index(venda), end=" - ")
            pprint(venda)
