class FazerLoginRedis:
    def __init__(self, client_redis):
        self.client_redis = client_redis

    def processar(self, username: str, password: str):
        try:
            redis_password = self.client_redis.get(username)
            if redis_password == password:
                print("Login realizado com sucesso!")
                return True
            else:
                if redis_password == None:
                    print("Ocorreu um erro ao realizar login: Usuário não está cadastrado no sistema!")
                else:
                    print("Ocorreu um erro ao realizar login: Senha incorreta!")
                return False
        except Exception as e:
            print(f"Ocorreu um erro ao realizar o login: {e}")
            return False

