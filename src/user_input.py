from src.chart import *
from src.get_url import *
from src.getting_words import *


class UserInput:
    @staticmethod
    def interface():
        on = True
        while on:
            # This ask if the user want to pass a url
            user_input = input('>>> Would you like to scrape a website (y/n)? ').lower()

            # This checks if the user wants to quit the app
            if user_input == 'n':
                print('>>> Thanks for analyzing! Come back again!')
                break

            elif user_input == 'y':

                user_url = input('>>> Enter a website to analyze: ')

                valid = ValidUrl(user_url)

                # This checks if the user put in a valid url
                if not valid.validating_url():
                    print('ConnectionError: Check your internet connection or invalid url')
                else:

                    # This get the html of the validated url
                    url_html = GettingUrlHtml(valid.validating_url())
                    # This scrap the url
                    url_text = Scraper(url_html.getting_url_html_file())
                    # This get the text in the url
                    all_text = url_text.getting_parser_text()

                    # This filter out the common words and unwanted characters
                    necessary_words = GettingWords(all_text)
                    most_used_words = GettingMostUsedWords(necessary_words.removing_common_words())

                    print(f'>>> The top word is: {most_used_words.most_used_word()}')

                    # This get the most used words
                    words = most_used_words.words_list()
                    # This get the count of the most used words
                    word_count = most_used_words.words_count_list()

                    print('>>> *** show bar plot ***')

                    # This plot the bar chart
                    bar = BarChart(words, word_count)
                    bar.plot()

                    # This plot the pie chart
                    pie = PieChart(word_count, words)
                    pie.plot()

            else:
                print('Invalid input')
