import unittest
from faker_a4t import A4tProvider
from faker import Faker


class TestCore(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(A4tProvider)

    def test_hello(self):
        self.assertEquals(self.fake.hello(), 'world!!')
