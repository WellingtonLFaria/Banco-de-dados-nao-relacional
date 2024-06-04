from processos.conectarBanco import ConectarBanco
from processos.conectarRedis import ConectarRedis
from processos.fazerLoginRedis import FazerLoginRedis
from processos.fazerCadastroRedis import FazerCadastroRedis
from processos.create.cadastroUsuario import CadastroUsuario
from processos.create.cadastroProduto import CadastroProduto
from processos.create.cadastroVendedor import CadastroVendedor
from processos.create.cadastroVenda import CadastroVenda
from processos.read.listarVendedores import ListarVendedores
from processos.read.listarProdutos import ListarProdutos
from processos.read.listarUsuarios import ListarUsuarios
from processos.read.listarVendas import ListarVendas
from processos.delete.deletarUsuario import DeletarUsuario
from processos.delete.deletarProduto import DeletarProduto
from processos.delete.deletarVendedor import DeletarVendedor
from processos.delete.deletarVenda import DeletarVenda
from processos.update.atualizarUsuario import AtualizarUsuario
from processos.update.atualizarProduto import AtualizarProduto
from processos.update.atualizarVendedor import AtualizarVendedor
from processos.update.atualizarVenda import AtualizarVenda
from processos.verificarLogin import VerificarLogin

import os

class Token:
    def __init__(self,  login: bool = False, username: str = None, password: str = None):
        self.login = login
        self. username = username
        self.password = password

processo = ConectarBanco("mongodb+srv://wellingtonfaria:fatec@cluster0.mb3qx5b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CLIENT = processo.conectar()

processo = ConectarRedis('redis-11718.c308.sa-east-1-1.ec2.redns.redis-cloud.com', 11718, "wellingtonfaria", 'F@tec123')
CLIENT_REDIS = processo.processar()

token = Token()
run = True
while run:
    os.system("cls")
    while True:
        print("1 - Realizar login")
        print("2 - Realizar cadastro")
        print("0 - Sair da aplicação")
        opcao = int(input())
        if opcao == 0:
            login = False
            run = False
            break
        elif opcao == 1:
            username = input("Nome de usuário: ")
            password = input("Senha: ")

            processo = FazerLoginRedis(CLIENT_REDIS)
            login = processo.processar(username, password)
            token.login = True
            token.username = username
            token.password = password
            if token.login: break
        elif opcao == 2:
            username = input("Nome de usuário: ")
            password = input("Senha: ")

            processo = FazerCadastroRedis(CLIENT_REDIS)
            registrar = processo.processar(username, password)

    if login:
        k = None
        while k != 0 and token.login:
            proc = VerificarLogin(CLIENT_REDIS, token)
            print("1 - Cadastrar usuário")
            print("2 - Cadastrar produto")
            print("3 - Cadastrar vendedor")
            print("4 - Cadastrar venda")
            print("5 - Listar usuários")
            print("6 - Listar produtos")
            print("7 - Listar vendedores")
            print("8 - Listar vendas")
            print("9 - Deletar usuário")
            print("10 - Deletar produto")
            print("11 - Deletar vendedor")
            print("12 - Deletar venda")
            print("13 - Atualizar usuário")
            print("14 - Atualizar produto")
            print("15 - Atualizar vendedor")
            print("16 - Atualizar venda")
            print("0 - Sair")
            k = int(input("Digite a opção desejada: "))
            print("-"*30)

            match k:
                case 1:
                    processo = CadastroUsuario(CLIENT)
                    processo.cadastrar()
                case 2:
                    processo = CadastroProduto(CLIENT)
                    processo.cadastrar()
                case 3:
                    processo = CadastroVendedor(CLIENT)
                    processo.cadastrar()
                case 4:
                    processo = CadastroVenda(CLIENT)
                    processo.cadastrar()
                case 5:
                    processo = ListarUsuarios(CLIENT)
                    processo.listar()
                case 6:
                    processo = ListarProdutos(CLIENT)
                    processo.listar()
                case 7:
                    processo = ListarVendedores(CLIENT)
                    processo.listar()
                case 8:
                    processo = ListarVendas(CLIENT)
                    processo.listar()
                case 9:
                    processo = DeletarUsuario(CLIENT)
                    processo.deletar()
                case 10:
                    processo = DeletarProduto(CLIENT)
                    processo.deletar()
                case 11:
                    processo = DeletarVendedor(CLIENT)
                    processo.deletar()
                case 12:
                    processo = DeletarVenda(CLIENT)
                    processo.deletar()
                case 13:
                    processo = AtualizarUsuario(CLIENT)
                    processo.atualizar()
                case 14:
                    processo = AtualizarProduto(CLIENT)
                    processo.atualizar()
                case 15:
                    processo = AtualizarVendedor(CLIENT)
                    processo.atualizar()
                case 16:
                    processo = AtualizarVenda(CLIENT)
                    processo.atualizar()
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                
