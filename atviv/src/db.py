from astrapy import DataAPIClient

class DB:
    def __init__(self):
        # Initialize the client
        self.client = DataAPIClient("AstraCS:nJmwFLWZvMlfGslgixnIidoD:e0b2fbd45ce56d8ca2409eab940517e0dd77b6bef60b4fe6d69567a2f0db0efc")
        self.db = self.client.get_database_by_api_endpoint(
        "https://04337ee4-cef2-4b32-81ce-b5482b409734-us-east-2.apps.astra.datastax.com"
        )

        print(f"Connected to Astra DB: {self.db.list_collection_names()}")