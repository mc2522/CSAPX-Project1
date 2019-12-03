'''
Mike Cao
10/6/18
letter_freq.py Project 1
'''


import numpy as np
import matplotlib.pyplot as plt
import collections
import module
import argparse
import word_count

Word = collections.namedtuple('Word', ('word', 'year', 'times'))

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="display letter frequencies to standard output", action="store_true") #optional argument output
parser.add_argument("-p", "--plot", help="plot letter frequencies using matplotlib", action="store_true")   #optional argument plot
parser.add_argument("filename", help="a comma separated value unigram file", type=str) #positional argument filename

def frequency(words, alphabet):
    '''
    Returns a dictionary of alphabets with their frequencies.
    :param words: dictionary of named tuples containing the names, years, and times used
    :param alphabet: dictionary of the alphabet as keys and 0 as the values
    :return: alphabet with updated values as frequencies
    '''

    used = []
    occurences = 0
    for x in words:
        if words[x] not in used: #if the word hasn't been run through word_count
            counter = word_count.count(words, words[x].word)
            used.append(words[x])   #assign the word to used
            currentword = words[x].word
            for char in currentword:    #goes through every single letter in the current word
                alphabet[char] += counter   #assigns the times it was used to the letter's corresponding value
                occurences += counter    #adds counter to total number of times a letter was counted
    for char in "abcdefghijklmnopqrstuvwxyz":
        alphabet[char] = alphabet[char]/occurences   #updates the values by dividing the individual number of times a letter was used by total occurences to get frequencies.
    return alphabet

def plot(freq, name):
    '''
    Takes the dictionary of frequencies and plots it on a bar graph using matplotlib.
    :param freq: grabs the dictionary of letters and their frequencies
    :param name: the name of the file
    :return: None
    '''

    keys = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    values = []
    index = 0
    for x in freq:
        values.append(freq[x])
    y_pos = np.arange(len(keys))
    plt.margins(x=0)
    plt.bar(y_pos, values, width=1.0, edgecolor='black')
    plt.xticks(y_pos, keys)
    plt.ylabel('Frequency')
    plt.xlabel('Letter')
    plt.title('Letter Frequencies: ' + str(name))
    plt.show()

def main():
    '''
    Reads the filename using module.reader(), calls frequency and prints it out depending on whether or not output was specified. Also plots a bar graph if plot was specified.
    :return: None
    '''

    args = parser.parse_args()
    words = module.reader(args.filename) #reads the file name
    alphabet = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        alphabet[char] = 0   #create a dictionary of the alphabet and sets all their values as 0
    freq = frequency(words, alphabet)
    if args.output:
        for char in "abcdefghijklmnopqrstuvwxyz":
            print(char, ': ', alphabet[char])   #prints the results vertically.
    if args.plot:
        plot(freq, args.filename)    #plot the bar graph

if __name__ == '__main__':
    main()