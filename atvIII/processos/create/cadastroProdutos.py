from processos.read.listarVendedores import ListarVendedores
from modelos.produto import Produto
from modelos.vendedor import Vendedor
from pprint import pprint
import json

class CadastroProdutos:
    def __init__(self, client_redis, client_mongo):
        self.client_redis = client_redis

        self.client_mongo = client_mongo
        self.db = self.client_mongo.MercadoLivre
        self.collection = self.db.Produtos

        self.client_redis.set("produtos", json.dumps([]))
    
    def enviarProdutoRedis(self, produto: Produto):
        # Pegar lista de produtos do redis
        produtos = json.loads(self.client_redis.get("produtos"))
        vendedor = {"nome": produto["vendedor"]["nome"], "cnpj": produto["vendedor"]["cnpj"]}
        produto["vendedor"] = vendedor
        # Adicionar produto a lista
        produtos.append(produto)

        # Devolver lista de produtos pro redis
        self.client_redis.set("produtos", json.dumps(produtos))
    
    def getProdutosRedis(self) -> list[Produto]:
        produtos = json.loads(self.client_redis.get("produtos"))
        return produtos
    
    def cadastrarProduto(self) -> Produto:
        nome = input("Nome do produto: ")
        descricao = input("Descrição do produto: ")
        valor = float(input("Valor do produto: "))

        # Listar vendedores
        processo = ListarVendedores(self.client_mongo)
        processo.listar()
        
        # Selecionar vendedor
        vendedorIndex = int(input("Selecione o vendedor: "))
        vendedor = processo.vendedores[vendedorIndex]
        produto = Produto(nome, descricao, valor, vendedor)
        return produto

    def cadastrarProdutosMongo(self):
        produtos = json.loads(self.client_redis.get("produtos"))
        for produto in produtos:
            self.collection.insert_one(produto)
        print("Produtos cadastrados")

    def cadastrar(self):
        run = True
        while run:
            print("[1] Adicionar produto")
            print("[2] Listar produtos")
            print("[0] Voltar")

            opcao = int(input("Digite a opção desejada: "))

            match opcao:
                case 1:
                    if len([vendedor for vendedor in self.db.Vendedores.find({})]) == 0:
                        print("Não há vendedores cadastrados para poder cadastrar um produto.")
                    else:
                        produto = self.cadastrarProduto()
                        self.enviarProdutoRedis(produto.__dict__)
                case 2:
                    produtos = self.getProdutosRedis()
                    for produto in produtos:
                        print(produtos.index(produto), end=" - ")
                        pprint(produto)
                case 0:
                    self.cadastrarProdutosMongo()
                    run = False
                    