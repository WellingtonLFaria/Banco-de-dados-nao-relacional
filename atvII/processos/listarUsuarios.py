from pymongo import MongoClient

class ListarUsuarios:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Usuario

    def listar(self):
        data = self.collection.find()
        self.usuarios = [usuario for usuario in data]
        for usuario in self.usuarios:
            print(f'{self.usuarios.index(usuario)} - Nome: {usuario["nome"]} | CPF: {usuario["cpf"]}\n{"-"*30}')
