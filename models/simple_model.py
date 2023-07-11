from faker import Faker

class SimpleModel(Faker):
    def __init__(self):
        super().__init__()

        self.name = self.name()
        self.age = self.random_int(min=18, max=65)
        self.address = self.address()
        self.email = self.email()
        self.phone_number = self.phone_number()
        self.sentence = self.sentence()
        self.paragraph = self.paragraph()
        self.text = self.text()
        self.date = self.date()
        self.time = self.time()
        self.date_time = self.date_time()
        self.url = self.url()
        self.user_name = self.user_name()
        self.domain_name = self.domain_name()
        self.ip_addr = self.ipv4()


    def output(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'email': self.email,
            'phone_number': self.phone_number,
            'sentence': self.sentence,
            'paragraph': self.paragraph,
            'text': self.text,
            'date': self.date,
            'time': self.time,
            'date_time': self.date_time,
            'url': self.url,
            'user_name': self.user_name,
            'domain_name': self.domain_name,
            'ip_addr': self.ip_addr
        }


if __name__ == "__main__":
    for _ in range(10):
        s = SimpleModel()
        print(s.output())
