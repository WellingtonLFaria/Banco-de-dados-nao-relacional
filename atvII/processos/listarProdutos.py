from pymongo import MongoClient
from pprint import pprint

class ListarProdutos:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Produto

    def listar(self):
        data = self.collection.find()
        self.produtos = [produto for produto in data]
        for produto in self.produtos:
            print(self.produtos.index(produto), end=" - ")
            pprint(produto)
