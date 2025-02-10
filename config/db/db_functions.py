from pymongo import MongoClient
from app.server import settings

class Connection:
    def __init__(self, db_name, db_collection):
        self.db_name = db_name
        self.db_collection = db_collection

    async def start_connection(self):
        if settings.ENVIRONMENT == None:
            return "Something bad happened"
        
        self.db_client = MongoClient(settings.ENVIRONMENT)
    
    async def get_collection(self):
        database_name = self.db_client[self.db_name]
        database_collection = database_name[self.db_collection]
        return database_collection

    async def close_connection(self):
        self.db_client.close()