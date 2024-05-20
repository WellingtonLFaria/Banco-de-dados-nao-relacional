from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class ConectarBanco:
    def __init__(self, uri: str):
        self.uri = uri
        
    def conectar(self):
        # Create a new client and connect to the server
        CLIENT = MongoClient(self.uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            CLIENT.admin.command('ping')
            print("Conectado com sucesso ao MongoDB!")
        except Exception as e:
            print(e)

        return CLIENT