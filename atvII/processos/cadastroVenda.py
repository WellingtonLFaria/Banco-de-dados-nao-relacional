from pymongo import MongoClient
from processos.listarUsuarios import ListarUsuarios
from processos.listarProdutos import ListarProdutos

class CadastroVenda:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Venda

    def cadastrar(self):
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
