from unittest.mock import patch

import mongomock
import pytest

import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.join(module_dir, '/Users/andrew.king/local/projects/benchmarking-python')

sys.path.insert(0, main_dir)

print(sys.path)

from main import _get_args, cli, main


def test_cli():
    with patch("main.main"):
        cli(["ping", "--mongo-uri", "localhost"])


def test_main():
    with patch(
        "main.MongoClientSingleton",
        return_value=mongomock.MongoClient(),
    ):
        args = [
            "ping",
            "--mongo-uri",
            "localhost"
        ]

        args = _get_args(args)
        main(args)

        args.action = "invalid"

        with pytest.raises(NotImplementedError):
            main(args)