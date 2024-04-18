from pymongo import MongoClient
from processos.listarVendedores import ListarVendedores

class DeletarVendedor:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendedores
    
    def deletar(self) -> None:
        if len([vendedor for vendedor in self.collection.find()]) <= 0:
            print("Nenhum vendedor cadastrado.")
        else:
            ListarVendedores(self.client).listar()
            vendedorIndex = int(input("Selecione o vendedor que deseja deletar: "))
            data = self.collection.find()
            vendedores = [vendedor for vendedor in data]
            vendedor = vendedores[vendedorIndex]
            self.collection.delete_one({"_id": vendedor["_id"]})
            print("Vendedor deletado com sucesso!")
        print("-" * 30)
