import re
from src.utils import common_words
from collections import Counter


class GettingWords:
    """This class filter out the unwanted characters and words
    ...

    Methods
    -------
    getting_all_words() remove other characters except words
    removing_common_words() removes common words like is,and, etc
    """
    def __init__(self, large_string):
        self.large_string = large_string.lower()

    def getting_all_words(self):
        return re.findall(r'\b[a-zA-Z]+\b', self.large_string)

    def removing_common_words(self):
        return [word for word in self.getting_all_words() if word not in common_words and len(word) > 3]


class GettingMostUsedWords:
    """This class gives use the list of the most common words.
    ...

    Methods
    -------
    counting_most_used_words() returns a list of seven most common words in a tuple with the count of each word
    most_used_word() returns the most used word
    words_list() returns the list of the most common words
    word_count_list() returns the list of the counts of the seven most common words
    """
    def __init__(self, list_of_words):
        self.list_of_words = list_of_words

    def counting_most_used_words(self):
        return Counter(self.list_of_words).most_common(7)

    def most_used_word(self):
        return self.counting_most_used_words()[0][0].capitalize()

    def words_list(self):
        return [x[0].capitalize() for x in self.counting_most_used_words()]

    def words_count_list(self):
        return [y[1] for y in self.counting_most_used_words()]
