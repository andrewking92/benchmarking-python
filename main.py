from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from util.Ping import Ping


class Main:
    @staticmethod
    def main():
        MONGODB_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
        DATABASE_NAME = "admin"  # Replace with your database name

        # Create a new client and connect to the server
        client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
        database = client[DATABASE_NAME]

        # Send a ping to confirm a successful connection
        try:
            ping = Ping(database)
            ping.ping()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    Main.main()
