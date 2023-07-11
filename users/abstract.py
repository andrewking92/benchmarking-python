from locust import User


class AbstractMongoUser(User):

    abstract = True

    def __init__(self, environment):
        super().__init__(environment)