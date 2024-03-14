import json
from usuario import Usuario
from produto import Produto
from typing import List

class Venda:
    def __init__(self, usuario: List[Usuario], produtos: List[Produto], valor: float, data: str):
        self.usuario = usuario
        self.produtos = produtos
        self.valor = valor
        self.data = data
