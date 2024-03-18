from pymongo import MongoClient
from processos.listarVendas import ListarVendas

# Falta terminar

class AtualizarVenda:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Venda
    
    def atualizar(self):
        if len([venda for venda in self.collection.find({})]) == 0:
            print("Não há vendas cadastradas")
        else:
            ListarVendas(self.client).listar()
            vendaIndex = int(input("Selecione a venda que deseja atualizar: "))
            data = self.collection.find({})
            vendas = [venda for venda in data]
            venda = vendas[vendaIndex]

            while True:
                print("1 - Atualizar status")
                print("0 - Sair")
                k = int(input("Digite a opção desejada: "))
                print("-"*30)
