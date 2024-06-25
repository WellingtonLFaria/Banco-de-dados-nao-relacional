class Produto:
    def __init__(self, nome: str, descricao: str, valor: float, vendedor: dict):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.vendedor = vendedor