from pymongo import MongoClient

class ListarProdutos:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Produto

    def listar(self):
        data = self.collection.find()
        self.produtos = [produto for produto in data]
        for produto in self.produtos:
            print(f'{self.produtos.index(produto)} - Nome: {produto["nome"]} | Descrição: {produto["descricao"]} | Valor: {produto["valor"]}\n{"-"*30}')