from pymongo import MongoClient
from pymongo.server_api import ServerApi

class MongoClientSingleton:
    _instance = None

    def __new__(cls, mongo_uri):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._client = None  # Initialize client attribute

        if cls._instance._client is None:
            cls._instance._client = MongoClient(mongo_uri, server_api=ServerApi("1"))

        return cls._instance