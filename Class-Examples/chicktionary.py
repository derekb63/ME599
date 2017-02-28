#!/usr/bin/env python


from itertools import permutations


def load_dictionary(filename):
    words = set()

    with open(filename, 'r') as f:
        for line in f:
            words.add(line.strip().lower())

    print 'Got', len(words), 'words'

    return words

if __name__ == '__main__':
    dictionary = load_dictionary('/usr/share/dict/american-english')

    while True:
        letters = raw_input('Word? ').lower()

        answer = set()
        for i in xrange(3, len(letters) + 1):
            for word in permutations(letters, i):
                if ''.join(word) in dictionary:
                    answer.add(''.join(word))

        print 'Found', len(answer), 'words:'

        for w in sorted(sorted(answer), key=lambda x: len(x)):
            print ' ', w


