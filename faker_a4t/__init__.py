from faker.providers import BaseProvider


class A4tProvider(BaseProvider):
    def hello(self):
        return 'world!!'
