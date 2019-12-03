'''
Mike Cao
10/6/18
word_length.py Project 1
'''

import numpy as np
import matplotlib.pyplot as plt
import argparse
import module
import sys
import collections

Word = collections.namedtuple('Word', ('word', 'year', 'times'))

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="display the average word lengths over the years", action="store_true") #optional argument output
parser.add_argument("-p", "--plot", help="plot the average word lengths over the years", action="store_true")   #optional argument plot
parser.add_argument("start", help="the starting year range", type=int)  #starting year
parser.add_argument("end", help="the ending year range", type=int)  #ending year
parser.add_argument("filename", help="a coma separated value unigram file", type=str) #name of file

# evenly sampled time at 200ms intervals
#t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

def length(start, end, words):
    '''
    Gets the average word length of all the words from each year.
    :param start: starting year range
    :param end: ending year range
    :param words: dictionary of words, years, and times used
    :return: dictionary of the average word length for each year
    '''
    years = {}
    occurences = {}
    for year in range(start, end + 1):
        years[year] = 0
        occurences[year] = 0
    for ind in words:
        if words[ind].year in years:
            years[words[ind].year] += (len(words[ind].word) * words[ind].times)
            occurences[words[ind].year] += words[ind].times
    for year in range(start, end + 1):
        if occurences[year] == 0:
            occurences[year] = 1
    for year in range(start, end + 1):
        years[year] = int(years[year])/int(occurences[year])
    return years

def plot(avlen, start, end, filename):
    #plots a line graph and puts a star on the specified word.
    max = -1000
    min = 1000

    plt.figure(figsize=(6, 6))
    plt.subplot(1,1,1)
    xval = []
    for ind in range(start, end + 1):
        xval.append(ind)
    x = np.array(xval)
    plt.title('Average word lengths from ' + str(start) + " to " + str(end) + ": " + str(filename))
    plt.xlabel('Year')
    plt.ylabel('Average word length')
    lengths = []
    for ind in range(start, end+1):
        lengths.append(avlen[ind])
    y = np.array(lengths)
    for ind in range(0, len(lengths)):
        if max < lengths[ind]:
            max = lengths[ind]
        if min > lengths[ind]:
            min = lengths[ind]
    plt.ylim(min - 0.2, max + 0.2, 0.2)
    plt.plot(x, y)

    plt.show()

def main():
    '''
    Calls the word_length, outputs the results if specified, and plots the results if specified.
    :return: None
    '''
    args = parser.parse_args()
    start = args.start
    end = args.end
    words = module.reader(args.filename)
    if start <= end:
        avlen = length(start, end, words)
    else:
        sys.stderr.write("Error: start year must be less than or equal to end year!")
        sys.exit()
    if args.output:
        for year in range(start, end + 1):
            print(str(year) + ": " + str(avlen[year]))
    if args.plot:
        plot(avlen, start, end, args.filename)

if __name__ == '__main__':
    main()


