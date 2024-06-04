from pymongo import MongoClient
from processos.read.listarVendas import ListarVendas

class DeletarVenda:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendas
    
    def deletar(self) -> None:
        if len([venda for venda in self.collection.find()]) <= 0:
            print("Nenhuma venda cadastrada.")
        else:
            ListarVendas(self.client).listar()
            vendaIndex = int(input("Digite o índice da venda que deseja deletar: "))
            data = self.collection.find()
            vendas = [venda for venda in data]
            venda = vendas[vendaIndex]
            self.collection.delete_one({"_id": venda["_id"]})
            print("Venda deletada com sucesso!")
        print("-" * 30)
