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