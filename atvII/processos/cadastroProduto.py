from pymongo import MongoClient
from modelos.produto import Produto
from processos.listarVendedores import ListarVendedores

class CadastroProduto:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Produto
    
    def cadastrar(self):
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        valor = float(input("Digite o preço do produto: "))
        processo = ListarVendedores(self.client)
        processo.listar()
        vendedorIndex = int(input("Selecione o vendedor: "))
        vendedor = processo.vendedores[vendedorIndex]
        produto = Produto(nome, descricao, valor, vendedor)
        self.collection.insert_one(produto.__dict__)