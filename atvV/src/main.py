from pprint import pprint
from db import DB
from time import localtime
from entities.vendedor import Vendedor
from entities.compra import Compra
from entities.produto import Produto
from entities.usuario import Usuario

db = DB()

db.verifyConnection()

def cadastrarUsuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    
    print("TELEFONE")
    ddd = input("DDD: ")
    numero = input("Número: ")
    telefone = {
        "ddd": ddd,
        "numero": numero
    }
    
    print("ENDEREÇO")
    logradouro = input("Digite o logradouro: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    codigoPostal = input("Digite o código postal: ")

    enderecos = []
    endereco = {
        "logradouro": logradouro,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "codigoPostal": codigoPostal
    }
    enderecos.append(endereco)
    favoritos = []

    usuario = Usuario(nome, sobrenome, email, senha, cpf, telefone, enderecos, favoritos)

    db.createUsuario(usuario)

def cadastrarVendedor():
    nome = input("Nome do vendedor: ")
    cnpj = input("CNPJ: ")

    vendedor = Vendedor(nome, cnpj)
    
    db.createVendedor(vendedor)

def cadastrarProduto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    valor = float(input("Valor do produto: R$"))
    vendedores = db.buscarTodosVendedores()
    
    for vendedor in vendedores:
        print(f"[{vendedores.index(vendedor)}] - {vendedor}")
    idVendedor = int(input("Selecione o vendedor do produto: "))
    vendedor = vendedores[idVendedor]

    produto = Produto(nome, descricao, valor, vendedor)
    db.createProduto(produto)

def cadastrarCompra():
    produtos = db.buscarTodosProdutos()
    for produto in produtos:
        print(f"[{produtos.index(produto)}] - {produto}")
    idProduto = int(input("Selecione o produto da compra: "))
    produto = produtos[idProduto]

    usuarios = db.buscarTodosUsuarios()
    for usuario in usuarios:
        print(f"[{usuarios.index(usuario)}] - {usuario}")
    idUsuario= int(input("Selecione o usuário da compra: "))
    usuario = usuarios[idUsuario]

    valor = produto.valor
    data = f"{localtime().tm_mday}/{localtime().tm_mon}/{localtime().tm_year}"

    compra = Compra(usuario, [produto], valor, data)
    db.createCompra(compra)

db.deleteAll()

while True:
    print("[1] Cadastrar usuário\n[2] Cadastrar vendedor\n[3] Cadastrar produto\n[4] Cadastrar compra\n[5] Listar usuários\n[6] Listar vendedores\n[7] Listar produtos\n[8] Listar compras\n[0] Sair")
    opcao = int(input("Selecione a opção desejada: "))
    match opcao:
        case 1:
            cadastrarUsuario()
        case 2:
            cadastrarVendedor()
        case 3:
            cadastrarProduto()
        case 4:
            cadastrarCompra()
        case 5:
            print("Listagem Usuários")
            for entidade in db.buscarTodosUsuarios():
                pprint(entidade.__dict__["_properties"])
        case 6:
            print("Listagem Vendedores")
            for entidade in db.buscarTodosVendedores():
                pprint(entidade.__dict__["_properties"])
        case 7:
            print("Listagem Produtos")
            for entidade in db.buscarTodosProdutos():
                pprint(entidade.__dict__["_properties"])
        case 8:
            print("Listagem Compras")
            for entidade in db.buscarTodasCompras():
                pprint(entidade.__dict__["_properties"])
        case 0:
            break
        
# print("Dados deletados com sucesso!")

# vendedor = Vendedor("Dell", "1231231231231231")
# db.createVendedor(vendedor)
# print("Vendedor criado com sucesso!")

# produto = Produto("Notebook", "Notebook pessoal", 2000.00, vendedor.__dict__)
# db.createProduto(produto)
# print("Produto criado com sucesso!")

# usuario = Usuario("Wellington", "Faria", "wellington@gmail.com", "123", "12345678912", {"ddd": "12", "numero": "996680123"}, [{"logradouro": "Rua 2", "numero": "202", "bairro": "SH", "cidade": "SJC", "estado": "SP", "codigoPostal": "12225885"}], [produto.__dict__])
# db.createUsuario(usuario)
# print("Usuário criado com sucesso!")

# data = localtime()
# compra = Compra(usuario.__dict__, [produto.__dict__], produto.valor, f"{data.tm_mday}/{data.tm_mon}/{data.tm_year}")
# db.createCompra(compra)
# print("Compra criada com sucesso!")

# print("-"*100)

# print("-"*100)

# print("-"*100)

# print("-"*100)
