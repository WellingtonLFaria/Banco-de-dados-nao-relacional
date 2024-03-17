from processos.conectarBanco import ConectarBanco
from processos.cadastroUsuario import CadastroUsuario
from processos.cadastroProduto import CadastroProduto
from processos.cadastroVendedor import CadastroVendedor
from processos.cadastroVenda import CadastroVenda
from processos.listarVendedores import ListarVendedores
from processos.listarProdutos import ListarProdutos
from processos.listarUsuarios import ListarUsuarios
from processos.listarVendas import ListarVendas
from processos.deletarUsuario import DeletarUsuario
from processos.deletarProduto import DeletarProduto
from processos.deletarVendedor import DeletarVendedor
from processos.deletarVenda import DeletarVenda

processo = ConectarBanco("mongodb+srv://wellingtonfaria:fatec@cluster0.mb3qx5b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CLIENT = processo.conectar()

k = None
while k != 0:
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
        case 0:
            break
        case _:
            print("Opção inválida!")
