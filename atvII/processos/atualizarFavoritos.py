from processos.listarProdutos import ListarProdutos
from pymongo import MongoClient

class AtualizarFavoritos:
    def __init__(self, client: MongoClient, favoritos: list[dict]):
        self.favoritos = favoritos
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Produtos

    def atualizar(self) -> list[dict]:
        while True:
            print("1 - Adicionar produto aos favoritos")
            print("2 - Remover produto dos favoritos")
            print("0 - Sair")
            k = int(input("Digite a opção desejada: "))
            print("-"*30)

            match k:
                case 1:
                    if len([produto for produto in self.collection.find({})]) == 0:
                        print("Não há produtos cadastrados")
                    else:
                        ListarProdutos(self.client).listar()
                        produtoIndex = int(input("Selecione o produto que deseja adicionar aos favoritos: "))
                        data = self.collection.find({})
                        produtos = [produto for produto in data]
                        produto = produtos[produtoIndex]
                        self.favoritos.append(produto)
                case 2:
                    if len(self.favoritos) == 0:
                        print("Não há produtos para remover")
                    else:
                        for i, produto in enumerate(self.favoritos):
                            print(f"{i} - {produto}")
                        produtoIndex = int(input("Selecione o produto que deseja remover: "))
                        self.favoritos.pop(produtoIndex)
                case 0:
                    break
                case _:
                    print("Opção inválida")
        return self.favoritos
        