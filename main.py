import sys
import os
import argparse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from util.Ping import Ping


class Main:
    @staticmethod
    def main(args):
        MONGODB_URI = os.getenv("MONGODB_URI")
        DATABASE_NAME = os.getenv("DATABASE_NAME")

        # Create a new client and connect to the server
        client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
        database = client[DATABASE_NAME]

        try:
            match args.action:
                case "ping":
                    ping = Ping(database, args.iterations)
                    ping.ping()

                case _:
                    print("Invalid choice.")
                    sys.exit(1)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to perform benchmarking tasks."
    )
    parser.add_argument("action", choices=["ping"], help="The action to perform.")
    parser.add_argument(
        "iterations",
        type=int,
        nargs="?",
        default=1,
        help="The number of iterations for the action. Default is 1.",
    )

    args = parser.parse_args()

    Main.main(args)
