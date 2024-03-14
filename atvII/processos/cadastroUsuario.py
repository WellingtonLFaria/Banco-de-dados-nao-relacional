from pymongo.mongo_client import MongoClient
from modelos.usuario import Usuario
from modelos.endereco import Endereco
from modelos.telefone import Telefone

class CadastroUsuario:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Usuario

    def cadastrar(self):
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        cpf = input("Digite seu CPF: ")
        ddd = input("Digite o ddd do seu telefone: ")
        numero = input("Digite o número do seu telefone: ")
        telefone = Telefone(ddd, numero)
        enderecos = []
        k = None
        while k != "n":
            logradouro = input("Digite seu logradouro: ")
            numero = input("Digite o número: ")
            bairro = input("Digite o bairro: ")
            cidade = input("Digite a cidade: ")
            estado = input("Digite o estado: ")
            codigoPostal = input("Digite o código postal: ")
            endereco = Endereco(logradouro, numero, bairro, cidade, estado, codigoPostal)
            enderecos.append(endereco.__dict__)
            k = input("Deseja cadastrar mais um endereço? (s/n): ")
        
        usuario = Usuario(nome, sobrenome, email, senha, cpf, telefone.__dict__, enderecos, [])
        self.collection.insert_one(usuario.__dict__)
