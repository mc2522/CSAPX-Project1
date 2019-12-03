
'''
Mike Cao
10/6/18
word_count.py Project 1
'''

import collections
import module
import argparse
import sys

Word = collections.namedtuple('Word', ('word', 'year', 'times'))

parser = argparse.ArgumentParser()
parser.add_argument("word", help="a word to display the total occurrences of", type=str) #adds positional argument word
parser.add_argument("filename", help="a comma separated value unigram file", type=str) #adds positional argument filename

def count(words, look):

    '''
    Counts the number of times a word is used in the file throughout all the years.
    :param words: dictionary of namedtuples containing name, year, and times.
    :param look: word that is being counted
    :return: int of how many times look is repeated
    '''

    counter = 0
    for x in words:
        if words[x].word == look:  #if the word in words is the same as look
            counter += words[x].times  #add the times to counter
    return counter

def main():

    '''
    Gets the arguments and performs the reader function from module. It then calls the count function and prints it.
    :return: None
    '''

    args = parser.parse_args()
    look = args.word
    words = module.reader(args.filename)
    number = count(words, look)
    if number > 0:
        print(str(look) + ": " + str(number))
    else:
        sys.stderr.write("Error: " + str(look) + " does not appear!")
        sys.exit()

if __name__ == '__main__':
    main()