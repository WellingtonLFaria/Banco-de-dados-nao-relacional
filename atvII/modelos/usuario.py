import json
from modelos.endereco import Endereco
from modelos.produto import Produto
from modelos.telefone import Telefone
from typing import List

class Usuario:
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str, cpf: str, telefone: dict, enderecos: List[dict], favoritos: List[dict]):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.enderecos = enderecos
        self.favoritos = favoritos
