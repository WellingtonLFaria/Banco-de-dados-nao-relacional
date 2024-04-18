from pymongo import MongoClient
from processos.listarUsuarios import ListarUsuarios

class DeletarUsuario:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Usuarios

    def deletar(self):
        if len([usuario for usuario in self.collection.find()]) <= 0:
            print("Nenhum usuário cadastrado!")
        else:
            ListarUsuarios(self.client).listar()
            usuarioIndex = int(input("Selecione o usuário que deseja deletar: "))
            data = self.collection.find()
            usuarios = [usuario for usuario in data]
            usuario = usuarios[usuarioIndex]
            self.collection.delete_one({"_id": usuario["_id"]})
            print("Usuário deletado com sucesso!")
        print("-" * 30)
