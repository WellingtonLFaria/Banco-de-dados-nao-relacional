class VerificarLogin:
    def __init__(self, client_redis, token):
        self.token
    
    def verificar(self) -> None:
        if not self.client_redis.exists(self.token.username):
            self.token.login = False