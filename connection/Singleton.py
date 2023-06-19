from pymongo import MongoClient
from pymongo.server_api import ServerApi


class MongoClientSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, mongo_uri):
        if not cls._instance:
            cls._instance = MongoClient(mongo_uri, server_api=ServerApi("1"))
        return cls._instance