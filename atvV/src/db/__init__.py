import json
import os
from pathlib import Path
from neo4j import GraphDatabase
from dotenv import load_dotenv

from entities.compra import Compra
from entities.produto import Produto
from entities.usuario import Usuario
from entities.vendedor import Vendedor

path_to_env = Path(os.getcwd() + "\\src\\.env")
load_dotenv()

class DB:
    def __init__(self):
        self.URI = os.getenv("URI")
        self.AUTH = (os.getenv("USERNAMEDB"), os.getenv("PASSWORD"))
    

    def verifyConnection(self):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            driver.verify_connectivity()


    def deleteAll(self):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                session.run("MATCH (n) DETACH DELETE n")
    
    def createUsuario(self, usuario: Usuario):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                session.run("CREATE (u:Usuario {nome: $nome, sobrenome: $sobrenome, email: $email, senha: $senha, cpf: $cpf, telefone: $telefone, enderecos: $enderecos, favoritos: $favoritos})", 
                        nome=usuario.nome, 
                        sobrenome=usuario.sobrenome, 
                        email=usuario.email, 
                        senha=usuario.senha, 
                        cpf=usuario.cpf, 
                        telefone=json.dumps(usuario.telefone), 
                        enderecos=json.dumps(usuario.enderecos), 
                        favoritos=json.dumps(usuario.favoritos))
    
    def createVendedor(self, vendedor: Vendedor):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                session.run("CREATE (v:Vendedor {nome: $nome, cnpj: $cnpj})", nome=vendedor.nome, cnpj=vendedor.cnpj)
    
    def createProduto(self, produto: Produto):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                session.run("CREATE (p:Produto {nome: $nome, descricao: $descricao, valor: $valor})", 
                    nome=produto.nome, 
                    descricao=produto.descricao, 
                    valor=produto.valor)
                session.run("""
                    MATCH (v:Vendedor {nome: $nomeVendedor}), (p:Produto {nome: $nomeProduto})
                    CREATE (v)-[:VENDE]->(p)
                    """,
                    nomeVendedor=produto.__dict__["vendedor"]._properties["nome"],
                    nomeProduto=produto.nome)

    def createCompra(self, compra: Compra):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                produtos = []
                for produto in compra.__dict__["produtos"]:
                    produtos.append(produto._properties)
                session.run("CREATE (c:Compra {usuario: $usuario, produtos: $produtos, valor: $valor, data: $data})", 
                        usuario=json.dumps(compra.__dict__["usuario"].__dict__["_properties"]), 
                        produtos=json.dumps(produtos), 
                        valor=compra.valor, 
                        data=compra.data)
                
                for produto in compra.produtos:
                    session.run("""
                        MATCH (u:Usuario {nome: $nomeUsuario}), (p:Produto {nome: $nomeProduto})
                        CREATE (u)-[:COMPROU]->(p)
                        """,
                        nomeUsuario=compra.usuario._properties["nome"],
                        nomeProduto = produto._properties['nome'])
    
    def buscarTodosUsuarios(self):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                result = session.run("MATCH (u:Usuario) RETURN u")
                return [record["u"] for record in result]

    def buscarTodosProdutos(self):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                result = session.run("MATCH (p:Produto) RETURN p")
                return [record["p"] for record in result]

    def buscarTodosVendedores(self):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                result = session.run("MATCH (v:Vendedor) RETURN v")
                return [record["v"] for record in result]

    def buscarTodasCompras(self):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                result = session.run("MATCH (c:Compra) RETURN c")
                return [record["c"] for record in result]
                
