class FazerCadastroRedis:
    def __init__(self, client_redis):
        self.client_redis = client_redis

    def processar(self, username, password):
        try:
            redis_password = self.client_redis.get(username)
            if redis_password == None:
                self.client_redis.setex(username, 10, password)
                print("Cadastro realizado com sucesso!")
                return True
            else:
                print("Ocorreu um erro ao realizar o cadastro: Usuário já cadastrado no sistema!")
                return False
        except Exception as e:
            print(f"Ocorreu um erro ao realizar cadastro: {e}")
            return False
