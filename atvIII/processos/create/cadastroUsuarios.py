from modelos.telefone import Telefone
from modelos.endereco import Endereco
from modelos.usuario import Usuario
from processos.read.listarVendedores import ListarVendedores
from modelos.vendedor import Vendedor
from pprint import pprint
import json

class CadastroUsuarios:
    def __init__(self, client_redis, client_mongo):
        self.client_redis = client_redis

        self.client_mongo = client_mongo
        self.db = self.client_mongo.MercadoLivre
        self.collection = self.db.Usuarios

        self.client_redis.set("usuarios", json.dumps([]))
    
    def enviarUsuarioRedis(self, usuario: Usuario):
        # Pegar lista de usuarios do redis
        usuarios = json.loads(self.client_redis.get("usuarios"))
        # Adicionar usuario a lista
        usuarios.append(usuario)

        # Devolver lista de usuarios pro redis
        self.client_redis.set("usuarios", json.dumps(usuarios))
    
    def getUsuariosRedis(self) -> list[Usuario]:
        usuarios = json.loads(self.client_redis.get("usuarios"))
        return usuarios
    
    def cadastrarUsuario(self) -> Usuario:
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

        return usuario

    def cadastrarUsuariosMongo(self):
        usuarios = json.loads(self.client_redis.get("usuarios"))
        for usuario in usuarios:
            self.collection.insert_one(usuario)
        print("Usuários cadastrados")

    def cadastrar(self):
        run = True
        while run:
            print("[1] Adicionar usuário")
            print("[2] Listar usuários")
            print("[0] Voltar")

            opcao = int(input("Digite a opção desejada: "))

            match opcao:
                case 1:
                    usuario = self.cadastrarUsuario()
                    self.enviarUsuarioRedis(usuario.__dict__)
                case 2:
                    usuarios = self.getUsuariosRedis()
                    for usuario in usuarios:
                        print(usuarios.index(usuario), end=" - ")
                        pprint(usuario)
                case 0:
                    self.cadastrarUsuariosMongo()
                    run = False