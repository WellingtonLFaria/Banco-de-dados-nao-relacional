import redis

class ConectarRedis:
    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def processar(self):
        try:
            CLIENT_REDIS = redis.StrictRedis(
                host = self.host,
                port = self.port,
                username=self.username,
                password = self.password,
                decode_responses = True
            )
            CLIENT_REDIS.ping()
            print("Conectado ao Redis com sucesso!")
            return CLIENT_REDIS
        except Exception as e:
            print(f"Erro ao conectar ao Redis: {e}")
            return False