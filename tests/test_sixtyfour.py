import unittest
from sixtyfour import str_to_b64, b64_to_str


class TestSixtyfour(unittest.TestCase):

    def setUp(self):
        self.hello = 'Hello World'
        self.hello_b64 = 'SGVsbG8gV29ybGQ='

    def test_str_to_b64(self):
        self.assertEqual(
            str_to_b64(self.hello),
            self.hello_b64
        )

    def test_b64_to_str(self):
        self.assertEqual(
            b64_to_str(self.hello_b64),
            self.hello
        )
