#! usr/bin/env python

# Derek Bean
# ME 599
# lab 6
# 2/21/2017

import string
import sys

class Book:
	def __init__(self, book_title):
		data = open(book_title, 'r')
		words = data.readlines()
		self.words = []
		for i in range(len(words)):
			self.words += words[i].lower().strip('\n').replace('-', ' ').translate(None, string.punctuation).split()
		
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

if __name__ == '__main__':
	book_name = 'war_and_peace.txt'
	book_name2 = 'test_book.txt'
	dictionary = '/usr/share/dict/words'
	b = Book(book_name)
	c = Book(book_name2)
	d = Book(dictionary)
	print d.number_of_words()
	print b.number_of_words()
	print b.number_of_unique()
	print len(b-c)
# Word count for the book according to wc is 566308
