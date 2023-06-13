import argparse
import logging
import sys
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from util.Ping import Ping


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main(args):
    # Create a new client and connect to the server
    database = _get_mongo_database_client(args.mongo_uri, args.database)

    try:
        if "ping" == args.action:
            ping = Ping(database, args.iterations)
            ping.ping()
        else:
            logger.error("Invalid choice.")
            raise NotImplementedError

    except Exception as e:
        logger.exception(e)
        raise e


def cli(argv=None):
    args = _get_args(argv)

    main(args)


def _get_args(argv=None):
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
    parser.add_argument(
        "-M",
        "--mongo-uri",
        type=str,
        nargs="?",
        default=os.getenv("MONGODB_URI"),
        help="The MongoDB URI to test against. If not set, will use the 'MONGODB_URI' environment variable.",
    )
    parser.add_argument(
        "-D",
        "--database",
        type=str,
        nargs="?",
        default=os.getenv("DATABASE_NAME"),
        help="The MongoDB Database to test against. If not set, will use the 'DATABASE_NAME' environment variable.",
    )

    return parser.parse_args(argv)


def _get_mongo_database_client(mongo_uri: str, database: str):
    client = MongoClient(mongo_uri, server_api=ServerApi("1"))
    database = client[database]
    return database


if __name__ == "__main__":
    sys.exit(cli())