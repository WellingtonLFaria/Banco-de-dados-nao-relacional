from pymongo import MongoClient
from processos import listarProdutos

class DeletarProduto:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Produtos
    
    def deletar(self):
        if len([produto for produto in self.collection.find()]) <= 0:
            print("Nenhum produto cadastrado!")
        else:
            listarProdutos.ListarProdutos(self.client).listar()
            produtoIndex = int(input("Selecione o produto que deseja deletar: "))
            data = self.collection.find()
            produtos = [produto for produto in data]
            produto = produtos[produtoIndex]
            self.collection.delete_one({"_id": produto["_id"]})
            print("Produto deletado com sucesso!")
        print("-" * 30)
