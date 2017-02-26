#! usr/bin/env python

# Derek Bean
# ME 599
# lab 6
# 2/21/2017

import string
from operator import itemgetter
import sys


class Book:
    def __init__(self, book_title):
        data = open(book_title, 'r')
        words = data.readlines()
        self.words = []
        for i in range(len(words)):
            self.words += words[i].lower().strip('\n').\
                               translate(None, string.punctuation).split()

    def number_of_words(self):
        return len(self.words)

    def unique_words(self):
        return set(self.words)

    def number_of_unique(self):
        return len(self.unique_words())

    def __sub__(self, other):
        try:
            return self.unique_words() - other.unique_words()
        except:
            new_book = Book(other)
            return self.unique_words() - new_book.unique_words()

    def __rsub__(self, other):
        return self.__sub__(other)

    def common_words(self, n=10):
        new_words = self.words[:]
        if n > len(new_words):
            n = len(new_words)
        word_count = []
        for i in self.unique_words():
                word_count.append([i, new_words.count(i)])
                new_words.remove(i)
        word_count.sort(key=lambda l: l[1])
        just_words = [i[0] for i in word_count]
        return just_words[len(just_words)-n:]

    def print_letter_frequencies(self):
        long_string = ''
        long_string = long_string.join(self.words)
        letters = string.ascii_lowercase
        letter_count = []
        for i in letters:
            letter_count.append(long_string.count(i))
            long_string.remove(i)
        letter_count = zip(letters, letter_count)
        letter_count.sort(key=lambda l: l[1])
        letter_count.reverse()
        for i in xrange(len(letters)):
            print letter_count[i][0], ':', letter_count[i][1]
            print '------'
        return None


if __name__ == '__main__':
    book_name = 'war_and_peace.txt'
    book_name2 = 'test_book.txt'
    dictionary = '/usr/share/dict/words'
    b = Book(book_name)
    c = Book(book_name2)
    dictionary = Book(dictionary)
    print 'Num dictionary words: ', dictionary.number_of_words()
    print 'Num war and peace words: ', b.number_of_words()
    print 'Num unique words: ', b.number_of_unique()
    print 'b - c: ', len(b-c)
    # Word count for the book according to wc is 566308
