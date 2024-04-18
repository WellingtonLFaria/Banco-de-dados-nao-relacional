from pymongo import MongoClient
from processos.listarVendas import ListarVendas
from processos.listarUsuarios import ListarUsuarios
from processos.listarProdutos import ListarProdutos

class AtualizarVenda:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendas
    
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
                print("1 - Atualizar usuário")
                print("2 - Atualizar produtos")
                print("0 - Sair")
                k = int(input("Digite a opção desejada: "))
                print("-"*30)

                match k:
                    case 1:
                        if len([usuario for usuario in self.db.Usuarios.find({})]) == 0:
                            print("Não há usuários cadastrados")
                        else:
                            ListarUsuarios(self.client).listar()
                            usuarioIndex = int(input("Selecione o usuário: "))
                            data = self.db.Usuarios.find({})
                            usuarios = [usuario for usuario in data]
                            usuario = usuarios[usuarioIndex]
                            self.collection.update_one({"_id": venda["_id"]}, {"$set": {"usuario": {"_id": usuario["_id"], "nome": usuario["nome"], "sobrenome": usuario["sobrenome"], "email": usuario["email"], "cpf": usuario["cpf"], "telefone": usuario["telefone"], "enderecos": usuario["enderecos"], "favoritos": usuario["favoritos"]}}})
                    case 2:
                        produtos = []
                        while True:
                            if len([produto for produto in self.db.Produtos.find({})]) == 0:
                                print("Não há produtos cadastrados")
                                break
                            else:
                                ListarProdutos(self.client).listar()
                                produtoIndex = int(input("Selecione o produto: "))
                                data = self.db.Produtos.find({})
                                produtosData = [produto for produto in data]
                                produto = produtosData[produtoIndex]
                                quantidade = int(input("Digite a quantidade do produto que deseja cadastrar a venda: "))
                                produto["quantidade"] = quantidade
                                produto["valorTotal"] = produto["valor"] * quantidade
                                produtos.append(produto)
                                k = input("Deseja adicionar mais produtos? (s/n): ")
                                if k.lower() == "n":
                                    break
                        self.collection.update_one({"_id": venda["_id"]}, {"$set": {"produtos": produtos}})
                        self.collection.update_one({"_id": venda["_id"]}, {"$set": {"valorTotal": sum([produto["valorTotal"] for produto in produtos])}})
                    case 0:
                        break
                    case _:
                        print("Opção inválida")
