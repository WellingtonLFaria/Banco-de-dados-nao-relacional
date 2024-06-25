from pprint import pprint
from db import DB
from time import localtime
from entities.vendedor import Vendedor
from entities.compra import Compra
from entities.produto import Produto
from entities.usuario import Usuario

db = DB()

db.verifyConnection()

# db.deleteAll()
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

print("-"*100)
print("Listagem Usuários")
for entidade in db.buscarTodosUsuarios():
    pprint(entidade.__dict__["_properties"])

print("-"*100)
print("Listagem Vendedores")
for entidade in db.buscarTodosVendedores():
    pprint(entidade.__dict__["_properties"])

print("-"*100)
print("Listagem Produtos")
for entidade in db.buscarTodosProdutos():
    pprint(entidade.__dict__["_properties"])

print("-"*100)
print("Listagem Compras")
for entidade in db.buscarTodasCompras():
    pprint(entidade.__dict__["_properties"])
