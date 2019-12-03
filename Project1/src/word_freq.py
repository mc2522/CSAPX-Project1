'''
Mike Cao
10/6/18
word_freq.py Project 1
'''

import numpy as np
import matplotlib.pyplot as plt
import module
import collections
import sys
import argparse

Word = collections.namedtuple('Word', ('word', 'year', 'times'))

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", default=0, help="display letter frequencies to standard output", nargs='?')  #optional argument output
parser.add_argument("-p", "--plot", help="plot letter frequencies using matplotlib", action="store_true")   #optional argument plot
parser.add_argument("word", help="a word to display the total occurrences of", type=str)    #positional argument word
parser.add_argument("filename", help="a comma separated value unigram file", type=str)  #positional argument filename

def word_frequency(words):
    '''
    Counts the number of times each word in words was used
    :param words: dicitonary of namedtuples containing the word, year, and times used
    :return: counter (a dictionary of each word and their number of times used)
    '''

    counter = {}
    used = []
    for x in words:
        if words[x].word not in used: #if the word hasn't been used, proceed
            used.append(words[x].word)   #add the word to used
            counter[words[x].word] = words[x].times #assign the number of times it was used that year to the word coutner
        else:
            counter[words[x].word] += words[x].times   #adds the number of times it was used to the word counter if the word has been used (has a value)
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)  #sorts the dictionary based on its values
    return counter

def plot(counter, name, look, place):
    '''
    Plots counter on a loglog graph
    :param counter: the dictionary of each word and their counters
    :param name: filename
    :param look: specified word
    :param place: look's rank
    :return: None
    '''

    x = []
    y = []
    for num in range(1, len(counter) + 1):
        x.append(num)
    for num in range(0, len(counter)):
        y.append(counter[num][1])
    plt.margins(x=0)
    plt.loglog(x, y, basex=10, marker='.', markerfacecolor='black', markevery = None)
    plt.plot(place, counter[place-1][1], marker='*', markeredgecolor="black", markersize=20)
    plt.annotate(look, (place, counter[place-1][1]))
    plt.ylabel('Total number of occurences')
    plt.xlabel('Rank of word ("' + str(look) + '" is rank ' + str(place) + ')')
    plt.title('Word Frequencies: ' + str(name))

    plt.show()

def main():
    '''
    calls word_frequency and outputs it if output is specified. Plots it if plot is specified.
    :return: None
    '''
    args = parser.parse_args()
    look = args.word
    words = module.reader(args.filename)

    counter = word_frequency(words)
    exist = False

    for x in range(0, len(counter)):
        if look == counter[x][0]: #prints the word if it hasn't been counted yet, gets the rank.
            print(str(look) + " is ranked #" + str(x+1))
            place = x + 1
            exist = True
        else:
            place = None
    if exist == False:
        sys.stderr.write("Error: " + str(look) + " does not appear!") #Error
        print()
    if args.output: #outputs the results if specified
        for x in range(0, int(args.output)):
            print("#" + str(x+1) + ": " + str(counter[x][0]) + " -> " + str(counter[x][1]))
    if args.plot: #plots the results if specified
        plot(counter, args.filename, look, place)

if __name__ == '__main__':
    main()