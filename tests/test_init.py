import unittest
import faker_a4t


class TestCore(unittest.TestCase):
    def test_hello(self):
        a4t = faker_a4t.A4tProvider
        self.assertEquals(a4t.hello(), 'world!!')
