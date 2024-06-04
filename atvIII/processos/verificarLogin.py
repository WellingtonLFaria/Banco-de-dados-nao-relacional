class VerificarLogin:
    def __init__(self, client_redis, token):
        self.client_redis = client_redis
        self.token = token
    
    def verificar(self) -> None:
        print(self.client_redis.exists(self.token.username))
        if not self.client_redis.exists(self.token.username):
            self.token.login = False