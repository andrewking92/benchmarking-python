from pymongo import MongoClient
from pymongo.server_api import ServerApi


class MongoClientSingleton:
    _instance = None

    def __new__(cls, mongo_uri):
        is_mongo_uri = (
            hasattr(cls._instance, "mongo_uri") and cls._instance.mongo_uri != mongo_uri
        )

        if cls._instance is None or is_mongo_uri:
            cls._instance = super().__new__(cls)
            cls._instance._client = MongoClient(mongo_uri, server_api=ServerApi("1"), heartbeatFrequencyMS=500)
            cls._instance.mongo_uri = mongo_uri

        return cls._instance._client