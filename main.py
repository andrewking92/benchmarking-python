import os
import gevent
import json

from util.ping import Ping
from connection.singleton import MongoClientSingleton
from locust import events
from locust.env import Environment
from locust.argument_parser import get_parser
from users.mongo_user import MongoUser
from setup_logging import setup_logging


LOGGER = setup_logging()


def execute(args):

    env = Environment(user_classes=[MongoUser], events=events)

    env.parsed_options = args

    runner = env.create_local_runner()

    env.events.init.fire(environment=env, runner=runner)

    runner.start(500, spawn_rate=25)

    gevent.spawn_later(120, lambda: runner.quit())

    runner.greenlet.join()

    LOGGER.info(json.dumps(env.stats.serialize_stats(), indent=4))

    return env.stats


def main(args):
    try:

        client = MongoClientSingleton(args.mongo_uri, args.server_timeout)

        if args.action == "ping":
            ping = Ping(client, cli_flag=True)
            return ping.execute(args.iterations)
        elif args.action == "insert":
            return execute(args)
        else:
            LOGGER.error("Invalid choice.")
            raise NotImplementedError

    except Exception as e:
        LOGGER.exception(e)
        raise e


def cli(argv=None):
    args = _get_args(argv)

    return main(args)


def _get_args(argv=None):
    parser = get_parser()
    parser.add_argument("action", choices=["ping", "insert"], help="The action to perform.")
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
