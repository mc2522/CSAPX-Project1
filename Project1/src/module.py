'''
Mike Cao
10/6/18
module.py Project 1
'''

import collections
import sys
import time
Word = collections.namedtuple('Word', ('word', 'year', 'times'))

def reader(filename):
    '''
    Reads the filename and organizes the data into a dictionary of namedtuples.
    Returns dictionary of namedtupes.
    :param filename: name of file
    :return: dictionary of named tuples containing word, year, and times.
    '''

    words = {}
    index = 0
    try:
        with open(filename) as f:
            for line in f:
                stat  = line.split(', ') #splits each line into word, year, and number of times used
                words[index] = Word(str(stat[0]), int(stat[1]), int(stat[2])) # Puts the different parts of the line into the namedtuple format
                index += 1
    except Exception as e:
        sys.stderr.write("Error: " + str(filename) + " does not appear!") #Outputs error if filename doesn't exist
        sys.exit()
    return words