from pymongo import MongoClient

from processos.atualizarEnderecos import AtualizarEnderecos
from processos.atualizarFavoritos import AtualizarFavoritos
from processos.listarUsuarios import ListarUsuarios

from modelos.telefone import Telefone


class AtualizarUsuario:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = self.client.MercadoLivre
        self.collection = self.db.Usuarios
    
    def atualizar(self):
        if len([usuario for usuario in self.collection.find({})]) == 0:
            print("Não há usuários cadastrados")
        else:
            ListarUsuarios(self.client).listar()
            usuarioIndex = int(input("Selecione o usuário que deseja atualizar: "))
            data = self.collection.find({})
            usuarios = [usuario for usuario in data]
            usuario = usuarios[usuarioIndex]

            while True:
                print("1 - Atualizar nome")
                print("2 - Atualizar sobrenome")
                print("3 - Atualizar email")
                print("4 - Atualizar senha")
                print("5 - Atualizar CPF")
                print("6 - Atualizar telefone")
                print("7 - Atualizar endereços")
                print("8 - Atualizar favoritos")
                print("0 - Sair")
                k = int(input("Digite a opção desejada: "))
                print("-"*30)

                match k:
                    case 1:
                        nome = input("Digite o novo nome: ")
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"nome": nome}})
                    case 2:
                        sobrenome = input("Digite o novo sobrenome: ")
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"sobrenome": sobrenome}})
                    case 3:
                        email = input("Digite o novo email: ")
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"email": email}})
                    case 4:
                        senha = input("Digite a nova senha: ")
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"senha": senha}})
                    case 5:
                        cpf = input("Digite o novo CPF: ")
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"cpf": cpf}})
                    case 6:
                        ddd = input("Digite o novo DDD: ")
                        numero = input("Digite o novo número: ")
                        telefone = Telefone(ddd, numero)
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"telefone": telefone.__dict__}})
                    case 7:
                        enderecos = usuario["enderecos"]
                        enderecos = AtualizarEnderecos(enderecos).atualizar()
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"enderecos": enderecos}})
                    case 8:
                        favoritos = usuario["favoritos"]
                        favoritos = AtualizarFavoritos(self.client, favoritos).atualizar()
                        self.collection.update_one({"_id": usuario["_id"]}, {"$set": {"favoritos": favoritos}})
                    case 0:
                        break
                    case _:
                        print("Opção inválida")