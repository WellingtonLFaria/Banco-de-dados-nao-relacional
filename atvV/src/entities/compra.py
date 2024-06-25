class Compra:
    def __init__(self, usuario: dict, produtos: list[dict], valor: float, data: str):
        self.usuario = usuario
        self.produtos = produtos
        self.valor = valor
        self.data = data