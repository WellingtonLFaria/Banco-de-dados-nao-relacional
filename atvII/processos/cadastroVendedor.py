from pymongo import MongoClient
from modelos.vendedor import Vendedor

class CadastroVendedor:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendedor
    
    def cadastrar(self):
        nome = input("Digite o nome do vendedor: ")
        cnpj = input("Digite o CNPJ do vendedor: ")
        vendedor = Vendedor(nome, cnpj)
        self.collection.insert_one(vendedor.__dict__)