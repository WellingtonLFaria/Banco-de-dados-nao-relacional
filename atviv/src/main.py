from time import localtime
from db import DB
from pprint import pprint

db = DB()
collUser = db.db.get_collection("user")
collVendedor = db.db.get_collection("vendedor")
collCompra = db.db.get_collection("compra")
collProduto = db.db.get_collection("produto")

class Vendedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

class Usuario:
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str, cpf: str, telefone: dict, enderecos: list[dict], favoritos: list[dict]):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.enderecos = enderecos
        self.favoritos = favoritos

class Produto:
    def __init__(self, nome: str, descricao: str, valor: float, vendedor: dict):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.vendedor = vendedor

class Compra:
    def __init__(self, usuario: dict, produtos: list[dict], valor: float, data: str):
        self.usuario = usuario
        self.produtos = produtos
        self.valor = valor
        self.data = data

def cadastrarUsuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")

    print("Cadastrando telefone")
    ddd = input("DDD: ")
    numero = input("Número: ")
    telefone = {"ddd": ddd, "numero": numero}

    enderecos = []
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    codigoPostal = input("Código Postal: ")
    endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "codigoPostal": codigoPostal}
    enderecos.append(endereco)
    run = True
    while run:
        print("[1] Cadastrar mais um endereço\n[2] Sair")
        opcao = int(input("Selecione a opção desejada: "))
        match opcao:
            case 1:
                logradouro = input("Logradouro: ")
                numero = input("Numero: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ")
                codigoPostal = input("Código Postal: ")
                endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "codigoPostal": codigoPostal}
                enderecos.append(endereco)
            case 2:
                run = False

    produtos = [produto for produto in collProduto.find()]

    if len(produtos) == 0:
        favoritos = []
    else:
        favoritos = []
        run = True
        while run:
            print("[1] Adicionar produto aos favoritos\n[2] Sair")
            opcao = int(input("Selecione a opção desejada: "))
            match opcao:
                case 1:
                    for produto in produtos:
                        print(f"[{produtos.index(produto)}] - {produto}")
                    idProduto = int(input("Selecione o produto para adicionar aos favoritos: "))
                    produto = produtos[idProduto]
                    favoritos.append(produto)
                case 2:
                    run = False

    usuario = Usuario(nome, sobrenome, email, senha, cpf, telefone, enderecos, favoritos)

    collUser.insert_one(usuario.__dict__)
    

def cadastrarVendedor():
    nome = input("Nome: ")
    cnpj = input("CNPJ: ")

    vendedor = Vendedor(nome, cnpj)
    collVendedor.insert_one(vendedor.__dict__)


def cadastrarProduto():
    vendedores = [vendedor for vendedor in collVendedor.find()]
    if len(vendedores) == 0:
        print("Nenhum vendedor cadastrado!")
        return

    nome = input("Nome: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$ "))

    for vend in vendedores:
        print(f"[{vendedores.index(vend)}] = {vendedores}")
        idVendedor = int(input("Selecione o vendedor desejado: "))
    vendedor = vendedores[idVendedor]
    
    produto = Produto(nome, descricao, valor, vendedor)

    collProduto.insert_one(produto.__dict__)


def cadastrarCompra():
    usuarios = [user for user in collUser.find()]
    produtosBanco = [produto for produto in collProduto.find()]

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado!")
        return
    if len(produtosBanco) == 0:
        print("Nenhum produto cadastrado!")
        return

    for usuario in usuarios:
        print(f"[{usuarios.index(usuario)}] - {usuario}")
    idUsuario = int(input("Selecione o usuário desejado: "))
    usuario = usuarios[idUsuario]

    produtos = []
    for produto in produtosBanco:
        print(f"[{produtosBanco.index(produto)}] - {produto}")
    idProduto = int(input("Selecione o produto desejado: "))
    produto = produtosBanco[idProduto]
    produtos.append(produto)

    run = True
    while run:
        print("[1] Adicionar mais um produto a compra\n[2] Sair")
        opcao = int(input("Selecione a opção desejada: "))
        match opcao:
            case 1:
                for produto in produtosBanco:
                    print(f"[{produtosBanco.index(produto)}] - {produto}")
                idProduto = int(input("Selecione o produto desejado: "))
                produto = produtosBanco[idProduto]
                produtos.append(produto)
            case 2:
                run = False

    valor = 0
    for produto in produtos:
        valor += produto["valor"]

    tempo = localtime()
    dia = tempo.tm_mday
    mes = tempo.tm_mon
    ano = tempo.tm_year

    compra = Compra(usuario, produtos, valor, f"{dia}/{mes}/{ano}")

    collCompra.insert_one(compra.__dict__)


def atualizarUsuario():
    usuarios = [user for user in collUser.find()]

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado!")
        return
    
    for user in usuarios:
        print(f"[{usuarios.index(user)}] - ", end="")
        pprint(user)
    
    idUser = int(input("Informe o usuário que deseja atualizar os dados: "))
    usuarioBanco = usuarios[idUser]
    
    # Novo
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")

    print("Cadastrando telefone")
    ddd = input("DDD: ")
    numero = input("Número: ")
    telefone = {"ddd": ddd, "numero": numero}

    enderecos = []
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    codigoPostal = input("Código Postal: ")
    endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "codigoPostal": codigoPostal}
    enderecos.append(endereco)
    run = True
    while run:
        print("[1] Cadastrar mais um endereço\n[2] Sair")
        opcao = int(input("Selecione a opção desejada: "))
        match opcao:
            case 1:
                logradouro = input("Logradouro: ")
                numero = input("Numero: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ")
                codigoPostal = input("Código Postal: ")
                endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "codigoPostal": codigoPostal}
                enderecos.append(endereco)
            case 2:
                run = False

    produtos = [produto for produto in collProduto.find()]

    if len(produtos) == 0:
        favoritos = []
    else:
        favoritos = []
        run = True
        while run:
            print("[1] Adicionar produto aos favoritos\n[2] Sair")
            opcao = int(input("Selecione a opção desejada: "))
            match opcao:
                case 1:
                    for produto in produtos:
                        print(f"[{produtos.index(produto)}] - {produto}")
                    idProduto = int(input("Selecione o produto para adicionar aos favoritos: "))
                    produto = produtos[idProduto]
                    favoritos.append(produto)
                case 2:
                    run = False

    usuario = Usuario(nome, sobrenome, email, senha, cpf, telefone, enderecos, favoritos)

    collUser.update_one({"_id": usuarioBanco["_id"]}, {"$set": usuario.__dict__})


def listarProdutos():
    produtos = [produto for produto in collProduto.find()]

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")

    for produto in produtos:
        print(produto)


def excluirCompra():
    compras = [compra for compra in collCompra.find()]

    if len(compras) == 0:
        print("Nenhuma compra cadastrada!")
        return

    
    for compra in compras:
        print(f"[{compras.index(compra)}] - {compra}")
    
    idCompra = int(input("Informe a compra que deseja excluir: "))

    compra = compras[idCompra]

    collCompra.delete_one(compra)


while True:
    print("[1] Cadastrar Usuário\n[2] Cadastrar Vendedor\n[3] Cadastrar Produto\n[4] Cadastrar Compra\n[5] Atualizar Usuário\n[6] Listar Produtos\n[7] Excluir compra")
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
            atualizarUsuario()
        case 6:
            listarProdutos()
        case 7:
            excluirCompra()