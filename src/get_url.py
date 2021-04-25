import validators
import requests
from bs4 import BeautifulSoup


class ValidUrl:
    """This class validate the users url
    ...

    Methods
    -------
    getting_url() validate the url by returning True if it is a valid url
    validating_url() checks if getting_url() is True
    """
    def __init__(self, website):
        self.website = website

    def getting_url(self):
        return validators.url(self.website)

    def validating_url(self):
        if self.getting_url() is True:
            return self.website
        else:
            return False


class GettingUrlHtml:
    """This class get the urls html file
    ...

    Methods
    -------
    getting_url_html_file() returns the urls html file
    """
    def __init__(self, validated_url):
        self.validated_url = validated_url

    def getting_url_html_file(self):
        return requests.get(self.validated_url).text


class Scraper:
    """This class get the parse a url and gets a giant string of all the text in url
    ...

    Methods
    -------
    parser() returns the parsed url
    getting_parser_text() returns the giant string of all the text
    """
    def __init__(self, url_text):
        self.url_text = url_text

    def parser(self):
        return BeautifulSoup(self.url_text, 'lxml')

    def getting_parser_text(self):
        return self.parser().body.get_text().lower()
