from pymongo import MongoClient
from processos.read.listarVendedores import ListarVendedores

class AtualizarVendedor:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendedores
    
    def atualizar(self):
        if len([vendedor for vendedor in self.collection.find({})]) == 0:
            print("Não há vendedores cadastrados")
        else:
            ListarVendedores(self.client).listar()
            vendedorIndex = int(input("Selecione o vendedor que deseja atualizar: "))
            data = self.collection.find({})
            vendedores = [vendedor for vendedor in data]
            vendedor = vendedores[vendedorIndex]

            while True:
                print("1 - Atualizar nome")
                print("2 - Atualizar CNPJ")
                print("0 - Sair")
                k = int(input("Digite a opção desejada: "))
                print("-"*30)

                match k:
                    case 1:
                        nome = input("Digite o novo nome: ")
                        self.collection.update_one({"_id": vendedor["_id"]}, {"$set": {"nome": nome}})
                    case 2:
                        cnpj = input("Digite o novo CNPJ: ")
                        self.collection.update_one({"_id": vendedor["_id"]}, {"$set": {"cnpj": cnpj}})
                    case 0:
                        break
                    case _:
                        print("Opção inválida")
