import unittest
from src.get_url import *


class TestValidUrl(unittest.TestCase):
    def setUp(self):
        self.url = 'http://python.org'
        self.valid_url = ValidUrl(self.url)

    def test_getting_url(self):
        self.assertEqual(self.valid_url.getting_url(), True)

    def test_validating_url(self):
        self.assertEqual(self.valid_url.validating_url(), 'http://python.org')


class TestInvalidUrl(unittest.TestCase):
    def setUp(self):
        self.url = 'http:/python.org'
        self.invalid_url = ValidUrl(self.url)

    def test_getting_url(self):
        self.assertNotEqual(self.invalid_url.getting_url(), True)

    def test_validating_url(self):
        self.assertEqual(self.invalid_url.validating_url(), False)


class TestGettingUrlHtml(unittest.TestCase):
    def setUp(self):
        self.validated_url = 'http://python.org'
        self.test_getting_url_html = GettingUrlHtml(self.validated_url).getting_url_html_file()

    def test_getting_url_html_file(self):
        self.assertIsNotNone(self.test_getting_url_html)


if __name__ == '__main__':
    unittest.main()
