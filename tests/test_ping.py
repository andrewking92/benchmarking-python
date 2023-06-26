import mongomock
import pymongo

import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.join(module_dir, '/Users/andrew.king/local/projects/benchmarking-python')

from util.Ping import Ping

@mongomock.patch(servers=(("localhost"),27017))
def test_ping():
    client = pymongo.MongoClient("localhost")
    ping_client = Ping(client)
    response = ping_client.execute(1)
    timings = response['localhost']
    assert len(timings) == 5
