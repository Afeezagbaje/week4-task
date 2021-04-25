import unittest
from src.getting_words import *


class TestGettingWords(unittest.TestCase):
    def setUp(self):
        self.large_string = GettingWords("age number users python game of 5 7 us night longer is me 9 4")

    def test_getting_all_words(self):
        self.assertEqual(self.large_string.getting_all_words(), ['age', 'number', 'users', 'python', 'game', 'of', 'us',
                                                                'night', 'longer', 'is', 'me'])

    def test_removing_common_words(self):
        self.assertEqual(self.large_string.removing_common_words(), ['number', 'users', 'python', 'game',
                                                                    'night', 'longer'])


class TestGettingMostUsedWords(unittest.TestCase):
    def setUp(self):
        self.list_of_word = GettingMostUsedWords(['number', 'users', 'python', 'game', 'night', 'longer', 'game',
                                                'python', 'number', 'python', 'javascript'])

    def test_counting_most_used_words(self):
        self.assertEqual(self.list_of_word.counting_most_used_words(), [('python', 3), ('number', 2), ('game', 2),
                                                                        ('users', 1), ('night', 1), ('longer', 1),
                                                                        ('javascript', 1)])

    def test_most_used_words(self):
        self.assertEqual(self.list_of_word.most_used_word(), 'Python')

    def test_word_list(self):
        self.assertEqual(self.list_of_word.words_list(), ['Python', 'Number', 'Game', 'Users',
                                                        'Night', 'Longer', 'Javascript'])

    def test_word_count_list(self):
        self.assertEqual(self.list_of_word.words_count_list(), [3, 2, 2, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
