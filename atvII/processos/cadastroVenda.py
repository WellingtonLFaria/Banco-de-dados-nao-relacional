from pymongo import MongoClient
from processos.listarUsuarios import ListarUsuarios
from processos.listarProdutos import ListarProdutos

class CadastroVenda:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Vendas

    def cadastrar(self):
        if len([usuario for usuario in self.db.Usuarios.find()]) == 0 or len([produto for produto in self.db.Produtos.find()]) == 0:
            if len([usuario for usuario in self.db.Usuarios.find()]) == 0 and len([produto for produto in self.db.Produtos.find()]) == 0:
                print("Não existem usuários e produtos cadastrados.")
            elif len([usuario for usuario in self.db.Usuarios.find()]) == 0:
                print("Não existem usuários cadastrados.")
            elif len([produto for produto in self.db.Produtos.find()]) == 0:
                print("Não existem produtos cadastrados.")
        else:
            processo = ListarUsuarios(self.client)
            processo.listar()
            usuarioIndex = int(input("Digite o número do usuário que deseja cadastrar a venda: "))
            usuario = processo.usuarios[usuarioIndex]

            produtos = []
            k = None
            while k != "n":  
                processo = ListarProdutos(self.client)
                processo.listar()
                produtoIndex = int(input("Digite o número do produto que deseja cadastrar a venda: "))
                quantidade = int(input("Digite a quantidade do produto que deseja cadastrar a venda: "))
                produto = processo.produtos[produtoIndex]
                produto["quantidade"] = quantidade
                produto["valorTotal"] = produto["valor"] * quantidade
                produtos.append(produto)
                k = input("Deseja cadastrar mais produtos? (s/n): ")
            
            valorTotal = sum([produto["valorTotal"] for produto in produtos])

            venda = {
                "usuario": usuario,
                "produtos": produtos,
                "valorTotal": valorTotal
            }
            self.collection.insert_one(venda)
