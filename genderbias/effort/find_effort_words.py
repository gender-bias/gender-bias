"""
Author: Catherine DeJager (cmd16 on GitHub)
Written for https://github.com/molliem/gender-bias
Detects gender bias in letters of recommendation by searching usage of words that denote effort vs words that denote accomplishment.
"""

import argparse
import nltk

# Create an argument parser and tell it about arguments
parser = argparse.ArgumentParser(description='Look for words that denote effort.')

# positional argument for input file
parser.add_argument(
  '-f', '--file', metavar="<file name>",
  help='name of input file',)

# optional argument for effort words file
parser.add_argument(
  '-e', '--effort_file', dest='effort_file', default="effort_words.wordlist",
  metavar="<effort file>",
  help='name of file containing effort words')

# optional argument for accomplishment words file
parser.add_argument(
  '-a', '--accomplishment_file', dest='accomplishment_file', default="accomplishment_words.wordlist",
  metavar="<accomplishment file>",
  help='name of file containing accomplishment words')

args = parser.parse_args()

# get the effort words
f_in = open(args.effort_file)
effort_words = f_in.readlines()
f_in.close()

# get the accomplishment words
f_in = open(args.accomplishment_file)
accomplishment_words = f_in.readlines()
f_in.close()

# get the letter's contents
f_in = open(args.file)
contents = f_in.read()
f_in.close()

effort_freqdist = nltk.FreqDist()
accomplishment_freqdist = nltk.FreqDist()

# Note: multi-word phrases are not detected this way (by using word_tokenize).
# TODO: create an option to search the raw text with regular expressions

# count the effort and accomplishment words
for word in nltk.word_tokenize(contents):
    if word in effort_words:
        effort_freqdist[word] += 1
    if word in accomplishment_words:  # the two lists should be mutually exclusive, but the user may not abide by that rule
        accomplishment_freqdist[word] += 1

# print the results

print("Effort words (and their frequencies:")
for word in effort_freqdist.most_common():  # sorts the words from most to least common
    print("%s\t%d" % (word, effort_freqdist[word]))

print("Accomplishment words (and their frequencies:")
for word in accomplishment_freqdist.most_common():  # sorts the words from most to least common
    print("%s\t%d" % (word, accomplishment_freqdist[word]))
