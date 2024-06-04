from modelos.endereco import Endereco

class AtualizarEnderecos:
    def __init__(self, enderecos: list[dict]) -> None:
        self.enderecos = enderecos

    def atualizar(self) -> list[dict]:
        while True:
            print("1 - Adicionar endereço")
            print("2 - Remover endereço")
            print("0 - Sair")
            k = int(input("Digite a opção desejada: "))
            print("-"*30)

            match k:
                case 1:
                    logradouro = input("Digite o logradouro: ")
                    numero = input("Digite o número: ")
                    bairro = input("Digite o bairro: ")
                    cidade = input("Digite a cidade: ")
                    estado = input("Digite o estado: ")
                    codigoPostal = input("Digite o código postal: ")
                    self.enderecos.append(Endereco(logradouro, numero, bairro, cidade, estado, codigoPostal).__dict__)
                case 2:
                    if len(self.enderecos) == 0:
                        print("Não há endereços para remover")
                    else:
                        for i, endereco in enumerate(self.enderecos):
                            print(f"{i} - {endereco}")
                        enderecoIndex = int(input("Selecione o endereço que deseja remover: "))
                        self.enderecos.pop(enderecoIndex)
                case 0:
                    break
                case _:
                    print("Opção inválida")
        return self.enderecos