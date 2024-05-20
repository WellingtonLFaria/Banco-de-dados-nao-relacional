from pymongo import MongoClient
from processos.listarProdutos import ListarProdutos
from processos.listarVendedores import ListarVendedores

class AtualizarProduto:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Produtos
    
    def atualizar(self):
        if len([produto for produto in self.collection.find({})]) == 0:
            print("Nenhum produto cadastrado")
        else:
            ListarProdutos(self.client).listar()
            produtoIndex = int(input("Selecione o produto que deseja atualizar: "))
            data = self.collection.find({})
            produtos = [produto for produto in data]
            produto = produtos[produtoIndex]

            while True:
                print("1 - Atualizar nome")
                print("2 - Atualizar descrição")
                print("3 - Atualizar valor")
                print("4 - Atualizar vendedor")
                print("0 - Sair")
                k = int(input("Digite a opção desejada: "))
                print("-"*30)

                match k:
                    case 1:
                        nome = input("Digite o novo nome: ")
                        self.collection.update_one({"_id": produto["_id"]}, {"$set": {"nome": nome}})
                    case 2:
                        descricao = input("Digite a nova descrição: ")
                        self.collection.update_one({"_id": produto["_id"]}, {"$set": {"descricao": descricao}})
                    case 3:
                        valor = float(input("Digite o novo valor: "))
                        self.collection.update_one({"_id": produto["_id"]}, {"$set": {"valor": valor}})
                    case 4:
                        ListarVendedores(self.client).listar()
                        vendedorIndex = int(input("Selecione o vendedor: "))
                        data = self.db.Vendedores.find({})
                        vendedores = [vendedor for vendedor in data]
                        vendedor = vendedores[vendedorIndex]
                        self.collection.update_one({"_id": produto["_id"]}, {"$set": {"vendedor": {"_id": vendedor["_id"], "nome": vendedor["nome"], "cnpj": vendedor["cnpj"]}}})
                    case 0:
                        break
                    case _:
                        print("Opção inválida")