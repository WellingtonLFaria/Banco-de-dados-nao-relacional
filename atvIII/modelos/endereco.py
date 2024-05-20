import json

class Endereco:
    def __init__(self, logradouro: str, numero: str, bairro: str, cidade: str, estado: str, codigoPostal: str):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.codigoPostal = codigoPostal
