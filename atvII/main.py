from processos.conectarBanco import ConectarBanco
from processos.cadastroUsuario import CadastroUsuario
from processos.cadastroProduto import CadastroProduto
from processos.cadastroVendedor import CadastroVendedor
from processos.cadastroVenda import CadastroVenda
from processos.listarVendedores import ListarVendedores
from processos.listarProdutos import ListarProdutos
from processos.listarUsuarios import ListarUsuarios

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
    print("0 - Sair")
    k = int(input("Digite a opção desejada: "))
    print("-"*30)
    if k == 1:
        processo = CadastroUsuario(CLIENT)
        processo.cadastrar()
    elif k == 2:
        processo = CadastroProduto(CLIENT)
        processo.cadastrar()
    elif k == 3:
        processo = CadastroVendedor(CLIENT)
        processo.cadastrar()
    elif k == 4:
        processo = CadastroVenda(CLIENT)
        processo.cadastrar()
    elif k == 5:
        processo = ListarUsuarios(CLIENT)
        processo.listar()
    elif k == 6:
        processo = ListarProdutos(CLIENT)
        processo.listar()
    elif k == 7:
        processo = ListarVendedores(CLIENT)
        processo.listar()
    elif k == 0:
        break
    else:
        print("Opção inválida!")