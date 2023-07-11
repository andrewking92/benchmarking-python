from locust import between, events

from models.simple_model import SimpleModel
from environment.mongodb_task import mongodb_task
from connection.singleton import MongoClientSingleton
import logging
from users.abstract import AbstractMongoUser


LOGGER = logging.getLogger("benchmarking")


@events.test_start.add_listener
def _(environment, **kw):
    print(f"Starting test...")


@events.test_stop.add_listener
def _(environment, **kw):
    print(f"Finishing test...")


@events.request.add_listener
def my_request_handler(request_type, name, response_time, response_length, total_sec, **kwargs):
        LOGGER.info({"request_type": request_type, "name": name, "response_time (ms)": response_time, "response_time (sec)": total_sec, "response_length": response_length})


class MongoUser(AbstractMongoUser):

    wait_time = between(1, 1.5)

    def __init__(self, environment):
        super().__init__(environment)
        self.client = MongoClientSingleton(self.environment.parsed_options.mongo_uri, self.environment.parsed_options.server_timeout)
        self.db = self.client.test
        self.simpleModel = SimpleModel()

    @mongodb_task(weight=1)
    def insert_empty_document(self):
        self.db.collection.insert_one({})

    @mongodb_task(weight=10)
    def insert_simple_document(self):
        self.db.collection.insert_one(self.simpleModel.output())

    @mongodb_task(weight=1)
    def insert_another_document(self):
        self.db.collection.insert_one({})