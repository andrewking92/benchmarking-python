import argparse
import logging
import sys
import os

from util.ping import Ping
from connection.singleton import MongoClientSingleton


def setup_logging():
    logger = logging.getLogger("benchmarking")
    logger.setLevel(logging.INFO)

    # Create a StreamHandler to output logs to stdout
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)

    # Define the log format
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(log_format)

    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger


def main(args):
    try:
        logger = setup_logging()

        client = MongoClientSingleton(args.mongo_uri, args.server_timeout)

        if args.action == "ping":
            ping = Ping(client, cli_flag=True)
            return ping.execute(args.iterations)
        else:
            logger.error("Invalid choice.")
            raise NotImplementedError

    except Exception as e:
        logger.exception(e)
        raise e


def cli(argv=None):
    args = _get_args(argv)

    return main(args)


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
        "-S",
        "--server-timeout",
        type=int,
        nargs="?",
        default=30000,
        help="The serverSelectionTimeoutMS to set when creating MongoClient.",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    cli()
